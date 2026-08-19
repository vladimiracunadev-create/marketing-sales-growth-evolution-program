# -*- coding: utf-8 -*-
"""Escribe la bibliografía completa dentro del README principal.

El README declara que el programa se basa en obras identificables. Esa
declaración sólo vale si las obras están a la vista y si la lista no puede
desincronizarse de lo que las clases citan realmente. Por eso el bloque no se
escribe a mano: se genera desde `curriculum/spec/` y se inserta entre marcas.

Marcas en README.md:
    <!-- BIBLIOGRAFIA:INICIO -->
    ... contenido generado ...
    <!-- BIBLIOGRAFIA:FIN -->

Uso:
    python tools/build_readme_bibliografia.py
"""

from __future__ import annotations

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

INICIO = "<!-- BIBLIOGRAFIA:INICIO -->"
FIN = "<!-- BIBLIOGRAFIA:FIN -->"

# Nombre legible de cada categoría de la bibliografía y el orden de presentación.
CATEGORIAS = [
    ("marketing", "Marketing"),
    ("estrategia", "Estrategia y competencia"),
    ("cliente", "Cliente y trabajo por resolver"),
    ("investigacion", "Investigación de mercados"),
    ("comportamiento", "Comportamiento y decisión"),
    ("marca", "Marca"),
    ("comunicacion", "Comunicación e identidad"),
    ("contenido", "Contenido y copywriting"),
    ("publicidad", "Publicidad"),
    ("precio", "Precio y monetización"),
    ("oferta", "Oferta y producto"),
    ("producto", "Gestión de producto"),
    ("ventas", "Ventas"),
    ("negociacion", "Negociación"),
    ("digital", "Marketing digital y conversión"),
    ("ecommerce", "Comercio digital"),
    ("growth", "Crecimiento y experimentación"),
    ("retencion", "Retención y éxito de cliente"),
    ("revops", "Operaciones de ingresos"),
    ("analitica", "Analítica y medición"),
    ("ia", "Inteligencia artificial y riesgo"),
    ("etica", "Ética y consecuencias"),
    ("direccion", "Dirección y organización"),
    ("pedagogia", "Pedagogía del programa"),
]

# Fuentes oficiales verificables. No son bibliografía: son normas y organismos
# cuyo texto vigente manda sobre cualquier material pedagógico.
OFICIALES = [
    ("Ley 19.496 — Protección de los derechos de los consumidores",
     "https://www.bcn.cl/leychile/navegar?idNorma=61438"),
    ("Decreto 6/2021 — Reglamento sobre comercio electrónico",
     "https://www.bcn.cl/leychile/navegar?idNorma=1165504"),
    ("Ley 21.719 — Protección y tratamiento de datos personales",
     "https://www.bcn.cl/leychile/navegar?idNorma=1209272"),
    ("SERNAC — Derechos del consumidor y comercio electrónico",
     "https://www.sernac.cl/"),
    ("INAPI — Registro y búsqueda de marcas",
     "https://www.inapi.cl/marcas"),
    ("SII — Documentos tributarios y obligaciones de la venta",
     "https://www.sii.cl/"),
    ("Fiscalía Nacional Económica — Libre competencia",
     "https://www.fne.gob.cl/"),
]


def uso_por_obra():
    """Cuenta en cuántas clases se cita cada obra y en qué partes."""
    veces = Counter()
    partes_de = defaultdict(set)
    for parte in PARTES:
        modulo = importlib.import_module("spec.clases_p{}".format(parte["num"]))
        for clase in modulo.CLASES:
            for clave in clase["libros"]:
                veces[clave] += 1
                partes_de[clave].add(parte["num"])
    return veces, partes_de


def bloque():
    veces, partes_de = uso_por_obra()
    total_anclajes = sum(len(v) for v in ANCLAJES.values())
    total_aportes = sum(len(v) for v in APORTES.values())

    lineas = [
        INICIO,
        "",
        "<details>",
        "<summary><b>📚 Base bibliográfica — las {} obras que sostienen el programa, "
        "con su uso clase a clase</b></summary>".format(len(bib.LIBROS)),
        "",
        "<br>",
        "",
        "El programa usa estas obras para ordenar conceptos y profundidad; **toda la redacción es original y "
        "no reproduce sus textos**. Citar no basta: de cada obra se catalogaron **{} ideas concretas** "
        "y cada una de las 336 clases declara **cuál** de ellas sostiene cada una de sus cuatro citas "
        "—**{} anclajes**— y en qué capítulo buscarla.".format(total_aportes, total_anclajes),
        "",
        "> [!NOTE]",
        "> Nunca se citan números de página: cambian entre ediciones y el programa no puede garantizarlas. "
        "El anclaje indica el capítulo o la sección **por su nombre dentro de la obra**.",
        "",
        "La columna «Clases» indica en cuántas de las 336 se cita la obra. "
        "Verificable con `python tools/audit_fuentes.py`.",
        "",
    ]

    vistos = set()
    for clave_cat, titulo_cat in CATEGORIAS:
        obras = sorted(
            (k for k, v in bib.LIBROS.items() if v[4] == clave_cat),
            key=lambda k: (-veces.get(k, 0), bib.LIBROS[k][0]),
        )
        if not obras:
            continue
        vistos.update(obras)
        lineas += [
            "#### {}".format(titulo_cat),
            "",
            "| Autoría | Obra | Edición | Qué aporta al programa | Clases |",
            "|---|---|---|---|---:|",
        ]
        for k in obras:
            autor, obra, edicion, lente, _cat = bib.LIBROS[k]
            lineas.append("| {} | *{}* | {} | {} | {} |".format(
                autor, obra, edicion, lente, veces.get(k, 0)))
        lineas.append("")

    faltan = sorted(set(bib.LIBROS) - vistos)
    if faltan:
        raise SystemExit("Categorías sin mapear en CATEGORIAS: {}".format(faltan))

    lineas += [
        "#### Fuentes oficiales y normativas",
        "",
        "La bibliografía ordena el criterio; **la norma vigente manda sobre el material pedagógico**. "
        "Toda regla, tarifa o requisito mencionado en una clase debe comprobarse aquí antes de aplicarse.",
        "",
        "| Fuente | Enlace |",
        "|---|---|",
    ]
    for nombre, url in OFICIALES:
        lineas.append("| {} | <{}> |".format(nombre, url))
    lineas += [
        "",
        "Listado completo con fecha de consulta en [`docs/FUENTES-OFICIALES.md`](docs/FUENTES-OFICIALES.md) "
        "y mapa regulatorio en [`docs/MAPA-REGULATORIO-CHILE.md`](docs/MAPA-REGULATORIO-CHILE.md).",
        "",
        "**Núcleo pedagógico.** El diseño instruccional del programa se apoya además en {}.".format(
            "; ".join(bib.cita(k) for k in bib.NUCLEO_PEDAGOGICO)),
        "",
        "[Bibliografía completa con el uso de cada obra por clase](docs/BIBLIOGRAFIA.md) · "
        "[Auditoría de fundamentación](tools/audit_fuentes.py)",
        "",
        "</details>",
        "",
        FIN,
    ]
    return "\n".join(lineas)


def main():
    ruta = os.path.join(RAIZ, "README.md")
    with open(ruta, encoding="utf-8") as fh:
        texto = fh.read()

    if INICIO not in texto or FIN not in texto:
        raise SystemExit(
            "README.md no tiene las marcas {} / {}. Añádelas donde deba ir la bibliografía.".format(
                INICIO, FIN))

    antes = texto.split(INICIO)[0]
    despues = texto.split(FIN, 1)[1]
    nuevo = antes + bloque() + despues

    with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(nuevo)

    print("README.md: bibliografía de {} obras insertada ({} anclajes declarados)".format(
        len(bib.LIBROS), sum(len(v) for v in ANCLAJES.values())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
