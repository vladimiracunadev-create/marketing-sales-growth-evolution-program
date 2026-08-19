# -*- coding: utf-8 -*-
"""Escribe en el README el resumen del registro de fuentes.

El README ya no lleva la bibliografía completa. Noventa y seis filas en la
portada eran una lista que nadie podía comprobar: sin ISBN, sin DOI y sin una
sola dirección resoluble, la declaración valía lo que valiera la confianza en
quien la escribió. Las obras viven ahora en `sources/bibliography.json`, donde
cada una tiene un localizador que se puede seguir, y el README hace lo único
que le corresponde: enlazar el registro, publicar sus cifras y decir qué obra
manda en cada parte.

Las cifras **no se escriben a mano**. Se toman del registro y
`scripts/verify_sources.py` falla si el README publica otras.

Marcas en README.md:
    <!-- BIBLIOGRAFIA:INICIO -->   ... bloque completo ...        <!-- BIBLIOGRAFIA:FIN -->
    <!-- REGISTRO-FUENTES:INICIO --> ... tabla de cifras ...      <!-- REGISTRO-FUENTES:FIN -->

Uso:
    python tools/build_readme_bibliografia.py
"""

from __future__ import annotations

import importlib
import json
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
INICIO_CIFRAS = "<!-- REGISTRO-FUENTES:INICIO -->"
FIN_CIFRAS = "<!-- REGISTRO-FUENTES:FIN -->"

REGISTRO = os.path.join(RAIZ, "sources", "bibliography.json")

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


def registro():
    if not os.path.exists(REGISTRO):
        raise SystemExit(
            "Falta sources/bibliography.json. Ejecuta primero:\n"
            "  python tools/build_bibliography_json.py")
    with open(REGISTRO, encoding="utf-8") as fh:
        return json.load(fh)


def uso_por_parte():
    """Cuántas clases de cada parte citan cada obra."""
    por_parte = defaultdict(Counter)
    for parte in PARTES:
        modulo = importlib.import_module("spec.clases_p{}".format(parte["num"]))
        for clase in modulo.CLASES:
            for clave in clase["libros"]:
                por_parte[parte["num"]][clave] += 1
    return por_parte


def rectora(conteo):
    """La obra que más veces sostiene las clases de una parte.

    Empate resuelto por orden alfabético de la clave: la elección tiene que ser
    la misma en cada ejecución o el README deja de ser reproducible.
    """
    return sorted(conteo.items(), key=lambda kv: (-kv[1], kv[0]))[0]


# Orden de lectura del bloque de cifras: del total a lo que falta.
ORDEN_CIFRAS = [
    "entradas del registro",
    "obras con localizador verificado",
    "libros con ISBN-13",
    "entradas pendientes",
]


def cifras(datos):
    entradas = datos["entries"]
    return {
        "entradas del registro": len(entradas),
        "obras con localizador verificado": sum(
            1 for e in entradas if e.get("status") == "verificada"),
        "entradas pendientes": sum(1 for e in entradas if e.get("status") == "pendiente"),
        "libros con ISBN-13": sum(1 for e in entradas if e.get("isbn13")),
    }


def bloque():
    datos = registro()
    por_id = {e["id"]: e for e in datos["entries"]}
    por_parte = uso_por_parte()
    total_anclajes = sum(len(v) for v in ANCLAJES.values())
    total_aportes = sum(len(v) for v in APORTES.values())
    c = cifras(datos)

    lineas = [
        INICIO,
        "",
        "<details>",
        "<summary><b>📚 Fundamentación — {} obras, cada una con un localizador que se puede "
        "seguir</b></summary>".format(c["entradas del registro"]),
        "",
        "<br>",
        "",
        "El programa usa estas obras para ordenar conceptos y profundidad; **toda la redacción es "
        "original y no reproduce sus textos**. Citar no basta: de cada obra se catalogaron "
        "**{} ideas concretas** y cada una de las 336 clases declara **cuál** de ellas sostiene "
        "cada una de sus cuatro citas —**{} anclajes**— y en qué capítulo buscarla.".format(
            total_aportes, total_anclajes),
        "",
        "Tampoco basta con anclar. Una obra nombrada sin localizador obliga al lector a salir a "
        "buscarla por su cuenta y le impide comprobar que es **esa** edición y no otra parecida. "
        "Por eso las obras no viven en esta portada: viven en "
        "[`sources/bibliography.json`](sources/bibliography.json), con ISBN-13, DOI o URL de la "
        "fuente primaria según lo que corresponda.",
        "",
        INICIO_CIFRAS,
        "",
        "| Estado del registro de fuentes | Valor |",
        "|---|---:|",
    ]
    for etiqueta in ORDEN_CIFRAS:
        lineas.append("| {} | **{}** |".format(etiqueta, c[etiqueta]))
    lineas += [
        "",
        "Última revalidación contra openlibrary.org y las fuentes oficiales: "
        "**{}**.".format(datos["verified_on"]),
        "",
        FIN_CIFRAS,
        "",
        "> [!NOTE]",
        "> Estas cifras las produce `python scripts/verify_sources.py`, que falla si el README "
        "declara otras. No se escriben a mano.",
        "",
        "> [!NOTE]",
        "> Nunca se citan números de página: cambian entre ediciones y el programa no puede "
        "garantizarlas. El anclaje indica el capítulo o la sección **por su nombre dentro de la "
        "obra**.",
        "",
        "#### La obra que manda en cada parte",
        "",
        "De las dos a cuatro obras que cita cada clase, esta es la que más veces sostiene el "
        "temario de la parte. El título enlaza a su localizador; el registro completo trae las "
        "{} obras con su uso clase a clase.".format(c["entradas del registro"]),
        "",
        "| # | Parte | Obra rectora | Clases de la parte que la citan |",
        "|---:|---|---|---:|",
    ]
    for parte in PARTES:
        clave, n = rectora(por_parte[parte["num"]])
        e = por_id[clave]
        autor, obra, edicion, _lente, _cat = bib.LIBROS[clave]
        titulo = "[*{}*]({})".format(obra, e["locator"]) if e.get("locator") else "*{}*".format(obra)
        lineas.append("| {} | {} | {} — {} ({}) | {} |".format(
            parte["num"], parte["titulo"], autor, titulo, edicion, n))

    lineas += [
        "",
        "#### Fuentes oficiales y normativas",
        "",
        "La bibliografía ordena el criterio; **la norma vigente manda sobre el material "
        "pedagógico**. Toda regla, tarifa o requisito mencionado en una clase debe comprobarse "
        "aquí antes de aplicarse.",
        "",
        "| Fuente | Enlace |",
        "|---|---|",
    ]
    for nombre, url in OFICIALES:
        lineas.append("| {} | <{}> |".format(nombre, url))
    lineas += [
        "",
        "Listado completo con fecha de consulta en "
        "[`docs/FUENTES-OFICIALES.md`](docs/FUENTES-OFICIALES.md) y mapa regulatorio en "
        "[`docs/MAPA-REGULATORIO-CHILE.md`](docs/MAPA-REGULATORIO-CHILE.md).",
        "",
        "**Núcleo pedagógico.** El diseño instruccional del programa se apoya además en {}.".format(
            "; ".join(bib.cita(k) for k in bib.NUCLEO_PEDAGOGICO)),
        "",
        "[Registro de fuentes con localizadores](sources/bibliography.json) · "
        "[Bibliografía completa con el uso de cada obra por clase](docs/BIBLIOGRAFIA.md) · "
        "[Verificador del registro](scripts/verify_sources.py) · "
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
            "README.md no tiene las marcas {} / {}. Añádelas donde deba ir la "
            "bibliografía.".format(INICIO, FIN))

    antes = texto.split(INICIO)[0]
    despues = texto.split(FIN, 1)[1]
    nuevo = antes + bloque() + despues

    with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(nuevo)

    datos = registro()
    c = cifras(datos)
    print("README.md: resumen del registro insertado ({} entradas, {} verificadas, "
          "{} pendientes)".format(c["entradas del registro"],
                                  c["obras con localizador verificado"],
                                  c["entradas pendientes"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
