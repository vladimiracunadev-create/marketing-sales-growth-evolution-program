# -*- coding: utf-8 -*-
"""Auditoría de la fundamentación bibliográfica del currículo.

Responde una pregunta concreta: ¿cada clase está realmente anclada en obras
identificables, o sólo las cita? Distingue tres niveles:

* **Cita**      la clase nombra la obra.
* **Lente**     la clase declara para qué sirve esa obra en general.
* **Anclaje**   la clase declara qué idea concreta de esa obra aplica aquí.

Sin anclaje, la misma frase sirve para cualquier clase que cite la obra, y eso
no es fundamentación: es decoración bibliográfica.

Uso:
    python tools/audit_fuentes.py
    python tools/audit_fuentes.py --detalle
"""

from __future__ import annotations

import argparse
import importlib
import os
import sys
from collections import Counter, defaultdict

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "curriculum"))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from spec import bibliografia as bib  # noqa: E402
from spec.anclajes import ANCLAJES  # noqa: E402
from spec.aportes import APORTES  # noqa: E402
from spec.partes import PARTES  # noqa: E402


def clases_de(num):
    return importlib.import_module("spec.clases_p{}".format(num)).CLASES


def main():
    ap = argparse.ArgumentParser(description="Audita la fundamentación bibliográfica")
    ap.add_argument("--detalle", action="store_true", help="Lista las clases sin anclaje")
    args = ap.parse_args()

    total_clases = 0
    citas = 0
    con_anclaje = 0
    sin_anclaje = []
    anclaje_incompleto = []
    anclaje_generico = []
    uso_por_obra = Counter()
    obras_por_parte = defaultdict(set)
    conteo_obras = Counter()

    for parte in PARTES:
        for c in clases_de(parte["num"]):
            total_clases += 1
            libros = c["libros"]
            citas += len(libros)
            conteo_obras[len(libros)] += 1
            for clave in libros:
                uso_por_obra[clave] += 1
                obras_por_parte[parte["num"]].add(clave)

            ref = "{}.{}".format(parte["num"], c["n"])
            anclas = ANCLAJES.get(ref) or {}
            if not anclas:
                sin_anclaje.append((ref, c["titulo"], len(libros)))
                continue
            con_anclaje += 1
            faltan = [k for k in libros if k not in anclas]
            if faltan:
                anclaje_incompleto.append((ref, c["titulo"], faltan))
            for clave, identificador in anclas.items():
                aporte = APORTES.get(clave, {}).get(identificador)
                if aporte is None:
                    anclaje_generico.append((ref, clave + ": identificador inexistente"))
                    continue
                if aporte[0].strip().lower() == bib.lente(clave).strip().lower():
                    anclaje_generico.append((ref, clave + ": idéntico al lente general"))

    print("=" * 72)
    print("AUDITORÍA DE FUNDAMENTACIÓN BIBLIOGRÁFICA")
    print("=" * 72)
    print()
    print("Clases analizadas:              {}".format(total_clases))
    print("Citas a obras:                  {}".format(citas))
    print("Obras distintas en catálogo:    {}".format(len(bib.LIBROS)))
    print("Ideas catalogadas (aportes):    {}".format(sum(len(v) for v in APORTES.values())))
    print("Obras efectivamente citadas:    {}".format(len(uso_por_obra)))
    print("Promedio de obras por clase:    {:.2f}".format(citas / total_clases))
    print()
    print("Distribución de obras por clase:")
    for n in sorted(conteo_obras):
        print("  {} obras: {} clases".format(n, conteo_obras[n]))
    print()

    print("-" * 72)
    print("NIVEL DE FUNDAMENTACIÓN")
    print("-" * 72)
    pct = 100.0 * con_anclaje / total_clases if total_clases else 0
    print("Clases con anclaje específico:  {}/{} ({:.1f} %)".format(con_anclaje, total_clases, pct))
    print("Clases sin anclaje:             {}".format(len(sin_anclaje)))
    print("Clases con anclaje incompleto:  {}".format(len(anclaje_incompleto)))
    print("Anclajes genéricos (= lente):   {}".format(len(anclaje_generico)))
    print()

    print("-" * 72)
    print("COBERTURA DEL CATÁLOGO")
    print("-" * 72)
    sin_uso = sorted(set(bib.LIBROS) - set(uso_por_obra) - set(bib.NUCLEO_PEDAGOGICO))
    if sin_uso:
        print("Obras del catálogo que ninguna clase cita ({}):".format(len(sin_uso)))
        for clave in sin_uso:
            print("  - {}".format(bib.cita(clave)))
    else:
        print("Todas las obras del catálogo se citan al menos una vez.")
    print()
    print("Obras citadas una sola vez ({}):".format(sum(1 for v in uso_por_obra.values() if v == 1)))
    for clave, n in sorted(uso_por_obra.items(), key=lambda x: x[1]):
        if n == 1:
            print("  - {}".format(bib.cita(clave)))
    print()
    print("Obras más citadas:")
    for clave, n in uso_por_obra.most_common(10):
        print("  {:>3} clases · {}".format(n, bib.cita(clave)))
    print()

    if args.detalle and sin_anclaje:
        print("-" * 72)
        print("CLASES SIN ANCLAJE ESPECÍFICO")
        print("-" * 72)
        for ref, titulo, n in sin_anclaje[:60]:
            print("  {} · {} ({} obras citadas)".format(ref, titulo, n))
        if len(sin_anclaje) > 60:
            print("  … y {} más".format(len(sin_anclaje) - 60))
        print()

    if anclaje_incompleto:
        print("-" * 72)
        print("CLASES CON OBRAS CITADAS PERO SIN ANCLAR")
        print("-" * 72)
        for ref, titulo, faltan in anclaje_incompleto[:30]:
            print("  {} · faltan: {}".format(ref, ", ".join(faltan)))
        print()

    print("=" * 72)
    if sin_anclaje or anclaje_incompleto or anclaje_generico:
        print("VEREDICTO: la fundamentación es NOMINAL en {} de {} clases.".format(
            len(sin_anclaje) + len(anclaje_incompleto) + len(anclaje_generico), total_clases))
        print("Las obras se citan sin declarar qué idea concreta de cada una sostiene")
        print("el contenido de esa clase en particular.")
        return 1
    print("VEREDICTO: las {} clases declaran, para cada una de sus {} citas, qué idea".format(
        total_clases, citas))
    print("concreta de la obra las sostiene y dónde buscarla. Fundamentación EFECTIVA.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
