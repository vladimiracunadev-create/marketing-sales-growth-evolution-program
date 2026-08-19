# -*- coding: utf-8 -*-
"""Genera `sources/bibliography.json` desde la especificación.

El registro de fuentes no se escribe a mano por la misma razón que no se
escribe a mano la bibliografía del README: una lista mantenida aparte se
desincroniza de lo que las clases citan realmente, y una lista desincronizada
declara una fundamentación que ya no existe.

Aquí se juntan dos cosas que viven separadas por buenas razones:

* `curriculum/spec/bibliografia.py`   qué obra es y qué aporta al programa.
* `curriculum/spec/localizadores.py`  dónde se resuelve esa obra y quién responde por ella.

El uso —en qué clases aparece cada obra— no se declara: se cuenta recorriendo
la especificación de las 336 clases.

Uso:
    python tools/build_bibliography_json.py
"""

from __future__ import annotations

import importlib
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "curriculum"))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from spec import bibliografia as bib  # noqa: E402
from spec.localizadores import LOCALIZADORES, POLITICA, VERIFICADO_EN, acceso  # noqa: E402
from spec.partes import PARTES  # noqa: E402

DESTINO = os.path.join(RAIZ, "sources", "bibliography.json")
BITACORA = os.path.join(RAIZ, "sources", "verification-log.json")

# Tipos que se resuelven por URL de la fuente primaria y exigen fecha de consulta.
TIPOS_URL = {"standard", "reference", "dataset"}


def bitacora():
    """Última fecha en que cada localizador resolvió de verdad.

    La escribe `scripts/refresh_sources.py`. Si todavía no existe, se usa la
    fecha declarada a mano en la especificación: nunca una fecha inventada.
    """
    if not os.path.exists(BITACORA):
        return {}
    with open(BITACORA, encoding="utf-8") as fh:
        return (json.load(fh).get("entries") or {})


def uso_por_obra():
    """Rutas de las clases que citan cada obra, según la especificación."""
    rutas = {}
    for parte in PARTES:
        modulo = importlib.import_module("spec.clases_p{}".format(parte["num"]))
        for clase in modulo.CLASES:
            ruta = "curriculum/{}/class-{}-{}.md".format(
                parte["slug"], clase["n"], clase["slug"])
            for clave in clase["libros"]:
                rutas.setdefault(clave, set()).add(ruta)
            # El estándar pedagógico se cita al pie de todas las clases.
            for clave in bib.NUCLEO_PEDAGOGICO:
                rutas.setdefault(clave, set()).add(ruta)
    return {k: sorted(v) for k, v in rutas.items()}


def localizador(datos):
    """Forma canónica del localizador según el tipo de fuente.

    Devuelve cadena vacía si la entrada todavía no tiene con qué construirlo:
    una entrada pendiente puede no tener ni ISBN, ni DOI, ni URL.
    """
    tipo = datos["tipo"]
    if tipo == "book" and datos.get("isbn13"):
        return "https://openlibrary.org/isbn/{}".format(datos["isbn13"])
    if tipo == "paper" and datos.get("doi"):
        return "https://doi.org/{}".format(datos["doi"])
    return datos.get("url", "")


def entrada(clave, rutas, log):
    autor_texto, obra, edicion, lente, categoria = bib.LIBROS[clave]
    datos = LOCALIZADORES[clave]
    tipo = datos["tipo"]
    estado = datos.get("estado", "verificada")

    e = {
        "id": clave,
        "type": tipo,
        "authors": list(datos["autores"]),
        "title": datos.get("titulo", obra),
        "published": datos["publicado"],
        "edition": edicion,
        "authority": datos["autoridad"],
        "category": categoria,
        "contribution": lente,
        "cited_as": autor_texto,
        # Qué cuesta llegar a la obra. Decirlo aquí evita que alguien descubra
        # a los tres clics que la fuente está detrás de un pago.
        "access": acceso(clave),
    }
    if datos.get("isbn13"):
        e["isbn13"] = datos["isbn13"]
    if datos.get("doi"):
        e["doi"] = datos["doi"]
    if estado == "verificada":
        e["locator"] = localizador(datos)
    else:
        # Marcar no es borrar: la pista que se tenía queda a la vista para que
        # alguien la confirme, no para darla por buena.
        e["locator"] = ""
        propuesto = localizador(datos)
        if propuesto:
            e["proposed_locator"] = propuesto
    consultado = (log.get(clave) or {}).get("last_ok") or datos.get("consultado", "")
    if tipo in TIPOS_URL or consultado:
        e["accessed"] = consultado
    if datos.get("nota"):
        e["note"] = datos["nota"]
    e["used_in"] = rutas
    e["status"] = estado
    return e


def main():
    rutas = uso_por_obra()

    faltan = sorted(set(bib.LIBROS) - set(LOCALIZADORES))
    if faltan:
        raise SystemExit(
            "Obras sin localizador declarado en spec/localizadores.py: {}".format(faltan))
    sobran = sorted(set(LOCALIZADORES) - set(bib.LIBROS))
    if sobran:
        raise SystemExit(
            "Localizadores que no corresponden a ninguna obra: {}".format(sobran))
    sin_uso = sorted(set(bib.LIBROS) - set(rutas))
    if sin_uso:
        raise SystemExit("Obras del catálogo que ninguna clase cita: {}".format(sin_uso))

    log = bitacora()
    registro = {
        "schema_version": 1,
        "verified_on": VERIFICADO_EN,
        "policy": POLITICA,
        "entries": [entrada(k, rutas[k], log) for k in sorted(bib.LIBROS)],
    }

    os.makedirs(os.path.dirname(DESTINO), exist_ok=True)
    with open(DESTINO, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(registro, fh, ensure_ascii=False, indent=2, sort_keys=False)
        fh.write("\n")

    verificadas = sum(1 for e in registro["entries"] if e["status"] == "verificada")
    pendientes = len(registro["entries"]) - verificadas
    print("sources/bibliography.json: {} entradas ({} verificadas, {} pendientes)".format(
        len(registro["entries"]), verificadas, pendientes))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
