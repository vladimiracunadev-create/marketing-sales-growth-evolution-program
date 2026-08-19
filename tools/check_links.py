# -*- coding: utf-8 -*-
"""Verificador de enlaces internos.

Comprueba que todos los enlaces relativos entre archivos Markdown apunten a
rutas existentes. No verifica enlaces externos: eso requiere red y produce
falsos negativos por límites de tasa.

Uso:
    python tools/check_links.py
    python tools/check_links.py --listar-externos
"""

from __future__ import annotations

import argparse
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RE_ENLACE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
IGNORAR_DIR = {".git", ".github", "site", "__pycache__", "node_modules", ".pytest_cache"}


def archivos_markdown():
    for actual, dirs, files in os.walk(RAIZ):
        dirs[:] = [d for d in dirs if d not in IGNORAR_DIR and not d.startswith(".")]
        for f in sorted(files):
            if f.endswith(".md"):
                yield os.path.join(actual, f)


def main():
    ap = argparse.ArgumentParser(description="Verifica enlaces internos")
    ap.add_argument("--listar-externos", action="store_true", help="Lista los enlaces externos encontrados")
    args = ap.parse_args()

    rotos = []
    externos = set()
    revisados = 0

    for ruta in archivos_markdown():
        with open(ruta, encoding="utf-8") as fh:
            contenido = fh.read()
        base = os.path.dirname(ruta)
        for destino in RE_ENLACE.findall(contenido):
            if destino.startswith(("http://", "https://", "mailto:")):
                externos.add(destino)
                continue
            if destino.startswith("#"):
                continue
            revisados += 1
            objetivo = destino.split("#", 1)[0]
            if not objetivo:
                continue
            absoluto = os.path.normpath(os.path.join(base, objetivo))
            if os.path.exists(absoluto):
                continue
            if os.path.isdir(absoluto.rstrip(os.sep)):
                continue
            rel = os.path.relpath(ruta, RAIZ).replace("\\", "/")
            rotos.append((rel, destino))

    print("Enlaces internos revisados: {}".format(revisados))
    print("Enlaces externos encontrados: {}".format(len(externos)))

    if args.listar_externos:
        print("\nExternos:")
        for e in sorted(externos):
            print("  · {}".format(e))

    if rotos:
        print("\nEnlaces rotos ({}):".format(len(rotos)))
        for archivo, destino in rotos[:40]:
            print("  [X] {} -> {}".format(archivo, destino))
        if len(rotos) > 40:
            print("  … y {} más".format(len(rotos) - 40))
        return 1

    print("\nTodos los enlaces internos resuelven correctamente.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
