# -*- coding: utf-8 -*-
"""Escribe en el README la sección de fuentes.

Corta y con enlaces. Aquí no van recuentos ni explicaciones sobre el método de
verificación: quien abre un repositorio de curso quiere ver de qué libros sale
el contenido, no leer un ensayo sobre bibliografía. La lista completa —qué
sostiene cada parte, los libros por área y las fuentes primarias— vive en
`docs/FUENTES.md`, y esta sección lleva hasta allí.

Lo único que se publica aquí además del enlace son las normas chilenas, porque
son las fuentes que cualquiera puede abrir y leer completas sin pagar.

Marcas en README.md:
    <!-- BIBLIOGRAFIA:INICIO -->  ... sección ...  <!-- BIBLIOGRAFIA:FIN -->

Uso:
    python tools/build_readme_bibliografia.py
"""

from __future__ import annotations

import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "curriculum"))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from spec import bibliografia as bib  # noqa: E402
from spec import normas  # noqa: E402

INICIO = "<!-- BIBLIOGRAFIA:INICIO -->"
FIN = "<!-- BIBLIOGRAFIA:FIN -->"


def bloque():
    lineas = [
        INICIO,
        "",
        "## 📚 Fuentes",
        "",
        "La redacción del material es original y se apoya en **{} obras** de referencia y en las "
        "normas chilenas vigentes. Están todas listadas, con su enlace, en "
        "**[`docs/FUENTES.md`](docs/FUENTES.md)**: qué obras sostienen cada parte, los libros "
        "agrupados por área y las fuentes primarias.".format(len(bib.LIBROS)),
        "",
        "Cada clase cierra indicando **qué idea concreta** de cada obra sostiene lo que acabas de "
        "leer y **en qué capítulo buscarla**. El identificador de cada obra —ISBN-13, DOI o "
        "dirección de la fuente— está en "
        "[`sources/bibliography.json`](sources/bibliography.json).",
        "",
        "### Normas chilenas",
        "",
        "Texto completo y gratuito. **La norma vigente manda sobre el material pedagógico**: si "
        "una clase la contradice, gana la norma.",
        "",
        "| Norma | Qué regula | Texto oficial |",
        "|---|---|---|",
    ]
    for clave, datos in normas.NORMAS.items():
        lineas.append("| **{}** | {} | <{}> |".format(
            datos["numero"], datos["materia"], normas.url(clave)))
    lineas += [
        "",
        "El programa **no distribuye** ninguna de las obras citadas: las cita, las contrasta y "
        "enseña a usarlas de forma selectiva. El acceso se obtiene por biblioteca, editorial, "
        "librería o suscripción legítima.",
        "",
        "[📚 Todas las fuentes](docs/FUENTES.md) · "
        "[Bibliografía por categoría](docs/BIBLIOGRAFIA.md) · "
        "[Registro con localizadores](sources/bibliography.json)",
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
            "README.md no tiene las marcas {} / {}. Añádelas donde deba ir la "
            "sección de fuentes.".format(INICIO, FIN))

    antes = texto.split(INICIO)[0]
    despues = texto.split(FIN, 1)[1]
    with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(antes + bloque() + despues)

    print("README.md: sección de fuentes actualizada ({} obras, {} normas)".format(
        len(bib.LIBROS), len(normas.NORMAS)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
