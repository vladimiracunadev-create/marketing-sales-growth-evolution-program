# -*- coding: utf-8 -*-
"""Revalidación en red del registro de fuentes. Manual o programada. NO bloquea.

Esta es la capa que sí usa red, y por eso vive fuera del CI. Un verificador que
depende de servicios externos falla por razones que no tienen que ver con el
repositorio; cuando eso pasa dos o tres veces, el equipo aprende a ignorar el
rojo y el control deja de servir. La comprobación que bloquea es
`scripts/verify_sources.py`, que es offline y determinista.

Qué hace aquí:

* resuelve cada ISBN-13 contra `openlibrary.org` y compara el título;
* resuelve cada DOI contra `api.crossref.org` y compara título y autoría;
* pide cada URL de norma o documentación oficial y registra el estado HTTP;
* escribe `sources/verification-log.json` con la última fecha en que cada
  entrada resolvió bien;
* informa de lo que dejó de resolver **sin borrarlo**.

Nada se elimina nunca. Una fuente que hoy no resuelve puede haber cambiado de
URL, estar caída o haberse retirado; las tres cosas se corrigen a mano y con
criterio, no borrando la entrada.

Uso:
    python scripts/refresh_sources.py
    python scripts/refresh_sources.py --solo book
    python scripts/refresh_sources.py --regenerar   # rehace el registro al terminar
    python scripts/refresh_sources.py --estricto    # devuelve 1 si algo dejó de resolver
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REGISTRO = os.path.join(RAIZ, "sources", "bibliography.json")
BITACORA = os.path.join(RAIZ, "sources", "verification-log.json")

AGENTE = {"User-Agent": "marketing-sales-growth-evolution-program/verificador-de-fuentes "
                       "(+https://github.com/vladimiracunadev-create/"
                       "marketing-sales-growth-evolution-program)"}
ESPERA = 25
REINTENTOS = 3


def hoy():
    return datetime.date.today().isoformat()


def pedir(url, acepta_json=True):
    """GET con reintentos. Devuelve (codigo, datos_o_texto, error)."""
    ultimo = None
    for intento in range(REINTENTOS):
        try:
            req = urllib.request.Request(url, headers=AGENTE)
            with urllib.request.urlopen(req, timeout=ESPERA) as r:
                cuerpo = r.read()
                if acepta_json:
                    try:
                        return r.getcode(), json.loads(cuerpo.decode("utf-8")), None
                    except ValueError:
                        return r.getcode(), None, "respuesta no JSON"
                return r.getcode(), None, None
        except urllib.error.HTTPError as e:
            return e.code, None, "HTTP {}".format(e.code)
        except Exception as e:  # noqa: BLE001
            ultimo = "{}: {}".format(type(e).__name__, e)[:120]
            time.sleep(2.0 * (intento + 1))
    return None, None, ultimo


def normalizar(texto):
    texto = (texto or "").lower()
    texto = re.sub(r"[^a-z0-9]+", " ", texto)
    return " ".join(texto.split())


def coincide(esperado, observado):
    """Coincidencia por solapamiento de palabras, tolerante a subtítulos."""
    a, b = set(normalizar(esperado).split()), set(normalizar(observado).split())
    if not a or not b:
        return False
    return len(a & b) / float(min(len(a), len(b))) >= 0.6


def comprobar_libro(e):
    codigo, datos, error = pedir("https://openlibrary.org/isbn/{}.json".format(e["isbn13"]))
    if datos is None:
        return {"resolved": False, "http": codigo, "error": error or "sin datos"}
    titulo = datos.get("title", "")
    return {
        "resolved": True,
        "http": codigo,
        "observed_title": titulo,
        "title_matches": coincide(e["title"], titulo),
        "observed_date": datos.get("publish_date", ""),
    }


def comprobar_articulo(e):
    codigo, datos, error = pedir("https://api.crossref.org/works/{}".format(
        urllib.parse.quote(e["doi"], safe="/")))
    if datos is None:
        return {"resolved": False, "http": codigo, "error": error or "sin datos"}
    m = datos.get("message", {})
    titulo = (m.get("title") or [""])[0]
    autores = ["{}, {}".format(a.get("family", ""), a.get("given", "")).strip(", ")
               for a in (m.get("author") or [])]
    return {
        "resolved": True,
        "http": codigo,
        "observed_title": titulo,
        "title_matches": coincide(e["title"], titulo),
        "observed_authors": autores,
        "authors_match": bool(autores) and coincide(" ".join(e["authors"]), " ".join(autores)),
    }


def comprobar_url(e):
    codigo, _datos, error = pedir(e["locator"], acepta_json=False)
    ok = codigo is not None and 200 <= codigo < 400
    return {"resolved": ok, "http": codigo, "error": None if ok else (error or "HTTP {}".format(codigo))}


def comprobar(e):
    tipo = e.get("type")
    if e.get("status") == "pendiente" or not e.get("locator"):
        return e["id"], {"resolved": False, "skipped": True,
                         "error": "entrada pendiente: no hay localizador que resolver"}
    try:
        if tipo == "book":
            r = comprobar_libro(e)
        elif tipo == "paper":
            r = comprobar_articulo(e)
        else:
            r = comprobar_url(e)
    except Exception as exc:  # noqa: BLE001
        r = {"resolved": False, "error": "{}: {}".format(type(exc).__name__, exc)[:120]}
    return e["id"], r


def main():
    ap = argparse.ArgumentParser(description="Revalida el registro de fuentes contra la red")
    ap.add_argument("--solo", help="Comprueba sólo un tipo (book, paper, standard, reference)")
    ap.add_argument("--regenerar", action="store_true",
                    help="Regenera sources/bibliography.json al terminar")
    ap.add_argument("--estricto", action="store_true",
                    help="Devuelve 1 si alguna fuente dejó de resolver")
    ap.add_argument("--hilos", type=int, default=6)
    args = ap.parse_args()

    with open(REGISTRO, encoding="utf-8") as fh:
        registro = json.load(fh)
    entradas = registro["entries"]
    if args.solo:
        entradas = [e for e in entradas if e.get("type") == args.solo]

    previo = {"schema_version": 1, "last_run": None, "entries": {}}
    if os.path.exists(BITACORA):
        with open(BITACORA, encoding="utf-8") as fh:
            previo = json.load(fh)

    print("=" * 72)
    print("REVALIDACIÓN EN RED DE {} ENTRADAS".format(len(entradas)))
    print("=" * 72)

    resultados = {}
    with ThreadPoolExecutor(max_workers=args.hilos) as pool:
        for i, (ident, r) in enumerate(pool.map(comprobar, entradas), 1):
            resultados[ident] = r
            marca = "ok " if r.get("resolved") else ("-- " if r.get("skipped") else "NO ")
            detalle = r.get("observed_title") or r.get("error") or ""
            if r.get("resolved") and r.get("title_matches") is False:
                marca = "?? "
                detalle = "resuelve pero el título observado difiere: " + detalle
            print("[{:3d}/{}] {}{:24s} {}".format(i, len(entradas), marca, ident, detalle[:60]),
                  flush=True)

    fecha = hoy()
    bitacora = {"schema_version": 1, "last_run": fecha, "entries": dict(previo.get("entries") or {})}
    for ident, r in resultados.items():
        anterior = bitacora["entries"].get(ident, {})
        registro_entrada = dict(r)
        registro_entrada["last_check"] = fecha
        if r.get("resolved"):
            registro_entrada["last_ok"] = fecha
        else:
            # No se borra nada: se conserva la última fecha en que sí resolvió.
            if anterior.get("last_ok"):
                registro_entrada["last_ok"] = anterior["last_ok"]
        bitacora["entries"][ident] = registro_entrada

    os.makedirs(os.path.dirname(BITACORA), exist_ok=True)
    with open(BITACORA, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(bitacora, fh, ensure_ascii=False, indent=2, sort_keys=True)
        fh.write("\n")

    fallos = sorted(k for k, r in resultados.items()
                    if not r.get("resolved") and not r.get("skipped"))
    dudosos = sorted(k for k, r in resultados.items() if r.get("title_matches") is False)
    saltados = sorted(k for k, r in resultados.items() if r.get("skipped"))

    print("")
    print("Resuelven:        {:>4}".format(sum(1 for r in resultados.values() if r.get("resolved"))))
    print("No resuelven:     {:>4}".format(len(fallos)))
    print("Título dudoso:    {:>4}".format(len(dudosos)))
    print("Pendientes:       {:>4}".format(len(saltados)))
    print("Bitácora:         {}".format(os.path.relpath(BITACORA, RAIZ)))

    if fallos:
        print("\nDejaron de resolver (NO se borran; se corrigen a mano):")
        for k in fallos:
            print("  - {}: {}".format(k, resultados[k].get("error")))
    if dudosos:
        print("\nResuelven pero el título observado no coincide (revisar el localizador):")
        for k in dudosos:
            print("  - {}: se esperaba «{}», se observó «{}»".format(
                k, next(e["title"] for e in entradas if e["id"] == k),
                resultados[k].get("observed_title")))

    if args.regenerar:
        print("\nRegenerando el registro con las fechas nuevas…")
        subprocess.check_call([sys.executable,
                               os.path.join(RAIZ, "tools", "build_bibliography_json.py")])

    if args.estricto and fallos:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
