# -*- coding: utf-8 -*-
"""Validador de profundidad del contenido.

Comprueba que cada clase alcance la extensión mínima del estándar
`clase-profunda-v1` y reporta la distribución para detectar degradación.

Uso:
    python tools/validate_depth.py
    python tools/validate_depth.py --minimo 3000
"""

from __future__ import annotations

import argparse
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MINIMO_CLASE = 2500
MINIMO_LAB = 500
MINIMO_EVAL = 400
MINIMO_CASO = 500


def palabras(ruta):
    with open(ruta, encoding="utf-8") as fh:
        return len(fh.read().split())


def recorrer(carpeta, prefijo=None, sufijo=".md"):
    base = os.path.join(RAIZ, carpeta)
    encontrados = []
    for actual, dirs, files in os.walk(base):
        dirs[:] = [d for d in dirs if not d.startswith((".", "__"))]
        for f in sorted(files):
            if not f.endswith(sufijo):
                continue
            if prefijo and not f.startswith(prefijo):
                continue
            encontrados.append(os.path.join(actual, f))
    return encontrados


def analizar(nombre, rutas, minimo):
    if not rutas:
        return [], {"nombre": nombre, "n": 0}
    conteos = [(r, palabras(r)) for r in rutas]
    valores = sorted(c for _r, c in conteos)
    fallas = [(r, c) for r, c in conteos if c < minimo]
    resumen = {
        "nombre": nombre,
        "n": len(conteos),
        "min": valores[0],
        "mediana": valores[len(valores) // 2],
        "max": valores[-1],
        "total": sum(valores),
        "minimo": minimo,
        "fallas": len(fallas),
    }
    return fallas, resumen


def main():
    ap = argparse.ArgumentParser(description="Valida la profundidad del contenido")
    ap.add_argument("--minimo", type=int, default=MINIMO_CLASE,
                    help="Palabras mínimas por clase (por defecto {})".format(MINIMO_CLASE))
    args = ap.parse_args()

    grupos = [
        ("Clases", recorrer("curriculum", prefijo="class-"), args.minimo),
        ("Laboratorios", recorrer("labs"), MINIMO_LAB),
        ("Evaluaciones", recorrer("assessments"), MINIMO_EVAL),
        ("Casos", recorrer("cases"), MINIMO_CASO),
    ]

    todas_las_fallas = []
    print("{:<16}{:>6}{:>9}{:>10}{:>9}{:>12}{:>8}".format(
        "Grupo", "N", "Mínimo", "Mediana", "Máximo", "Total", "Fallas"))
    print("-" * 70)
    for nombre, rutas, minimo in grupos:
        fallas, r = analizar(nombre, rutas, minimo)
        todas_las_fallas.extend((nombre, f, c, minimo) for f, c in fallas)
        if r["n"] == 0:
            print("{:<16}{:>6}".format(nombre, 0))
            continue
        print("{:<16}{:>6}{:>9}{:>10}{:>9}{:>12,}{:>8}".format(
            nombre, r["n"], r["min"], r["mediana"], r["max"], r["total"], r["fallas"]))

    if todas_las_fallas:
        print("\nContenido bajo el mínimo ({}):".format(len(todas_las_fallas)))
        for grupo, ruta, conteo, minimo in todas_las_fallas[:30]:
            rel = os.path.relpath(ruta, RAIZ).replace("\\", "/")
            print("  [X] {} · {} palabras (mínimo {}) · {}".format(grupo, conteo, minimo, rel))
        if len(todas_las_fallas) > 30:
            print("  … y {} más".format(len(todas_las_fallas) - 30))
        return 1

    print("\nProfundidad conforme: todo el contenido supera su mínimo.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
