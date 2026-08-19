# -*- coding: utf-8 -*-
"""Validador del sitio generado.

Comprueba que el artefacto de `site/` esté completo y sea autocontenido antes de
publicarlo: número de páginas, presencia de los índices, integridad del índice de
búsqueda y ausencia de recursos de terceros.

Uso:
    python tools/validate_site.py
    python tools/validate_site.py --minimo 600
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITIO = os.path.join(RAIZ, "site")

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

OBLIGATORIOS = [
    "index.html",
    "search-index.json",
    "manifest.webmanifest",
    ".nojekyll",
    "assets/estilo.css",
    "assets/app.js",
    "README.html",
    "SYLLABUS.html",
    "curriculum/index.html",
    "rutas/index.html",
    "apps/learning-dashboard/index.html",
]

RE_EXTERNO = re.compile(r'(?:src|href)="(https?://[^"]+)"')
DOMINIOS_PERMITIDOS = ()  # ninguno: el sitio debe ser autocontenido


def main():
    ap = argparse.ArgumentParser(description="Valida el sitio generado")
    ap.add_argument("--minimo", type=int, default=600, help="Páginas HTML mínimas esperadas")
    args = ap.parse_args()

    errores = []
    comprobaciones = 0

    if not os.path.isdir(SITIO):
        print("No existe site/. Ejecuta: python tools/build_site.py")
        return 1

    for rel in OBLIGATORIOS:
        if os.path.isfile(os.path.join(SITIO, rel)):
            comprobaciones += 1
        else:
            errores.append("Falta {}".format(rel))

    paginas = []
    for base, dirs, files in os.walk(SITIO):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        paginas += [os.path.join(base, f) for f in files if f.endswith(".html")]

    if len(paginas) < args.minimo:
        errores.append("Sólo {} páginas HTML (mínimo {})".format(len(paginas), args.minimo))
    else:
        comprobaciones += 1

    # ninguna página debe cargar recursos externos
    externos = {}
    for ruta in paginas:
        with open(ruta, encoding="utf-8") as fh:
            contenido = fh.read()
        for destino in RE_EXTERNO.findall(contenido):
            if destino.startswith(DOMINIOS_PERMITIDOS):
                continue
            # los enlaces de navegación a sitios externos son válidos; sólo se
            # prohíbe cargar recursos (script, hoja de estilo, imagen).
            if re.search(r'src="{}"'.format(re.escape(destino)), contenido) or destino.endswith((".css", ".js")):
                externos.setdefault(os.path.relpath(ruta, SITIO), []).append(destino)
    if externos:
        for archivo, urls in list(externos.items())[:10]:
            errores.append("Recurso externo en {}: {}".format(archivo, urls[0]))
    else:
        comprobaciones += 1

    # índice de búsqueda íntegro y con rutas existentes
    try:
        with open(os.path.join(SITIO, "search-index.json"), encoding="utf-8") as fh:
            indice = json.load(fh)
        if len(indice) < 400:
            errores.append("Índice de búsqueda con sólo {} entradas".format(len(indice)))
        else:
            comprobaciones += 1
        rotas = [e["u"] for e in indice[:80] if not os.path.isfile(os.path.join(SITIO, e["u"]))]
        if rotas:
            errores.append("Índice apunta a páginas inexistentes: {}".format(rotas[:3]))
        else:
            comprobaciones += 1
    except Exception as exc:  # noqa: BLE001
        errores.append("Índice de búsqueda ilegible: {}".format(exc))

    # una clase de muestra debe tener contenido real
    muestra = os.path.join(SITIO, "curriculum",
                           "part-07-pricing-y-monetizacion",
                           "class-04-value-based-pricing.html")
    if os.path.isfile(muestra):
        with open(muestra, encoding="utf-8") as fh:
            texto = fh.read()
        if len(texto) < 20000 or "<table>" not in texto:
            errores.append("La clase de muestra parece incompleta")
        else:
            comprobaciones += 1
    else:
        errores.append("Falta la clase de muestra en el sitio")

    print("Páginas HTML: {}".format(len(paginas)))
    print("Comprobaciones superadas: {}".format(comprobaciones))

    if errores:
        print("\nErrores ({}):".format(len(errores)))
        for e in errores[:20]:
            print("  [X] {}".format(e))
        return 1

    print("\nSitio válido: completo, autocontenido y con índice íntegro.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
