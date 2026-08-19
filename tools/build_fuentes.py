# -*- coding: utf-8 -*-
"""Genera `docs/FUENTES.md`: las obras y enlaces que sostienen el programa.

Una página, sin estadística: qué sostiene cada parte, los libros por área, las
fuentes primarias con su dirección y cuáles se pueden leer gratis. Todo con
enlace, para que comprobar una cita no dependa de creerle a nadie.

El detalle —qué idea concreta de cada obra sostiene cada clase y en qué
capítulo buscarla— vive donde sirve: al pie de cada clase. El localizador
comprobable de cada obra vive en `sources/bibliography.json`.

Uso:
    python tools/build_fuentes.py
"""

from __future__ import annotations

import importlib
import os
import sys
from collections import Counter

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "curriculum"))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from spec import bibliografia as bib  # noqa: E402
from spec import normas  # noqa: E402
from spec.localizadores import acceso, enlace  # noqa: E402
from spec.partes import PARTES  # noqa: E402

DESTINO = os.path.join(RAIZ, "docs", "FUENTES.md")

# Nombre legible de cada área y orden de presentación.
AREAS = [
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
    ("oferta", "Oferta y propuesta de valor"),
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

# Organismos cuyo criterio vigente manda sobre el material pedagógico.
ORGANISMOS = [
    ("SERNAC", "Derechos del consumidor y comercio electrónico", "https://www.sernac.cl/"),
    ("INAPI", "Registro y búsqueda de marcas", "https://www.inapi.cl/marcas"),
    ("SII", "Documentos tributarios y obligaciones de la venta", "https://www.sii.cl/"),
    ("Fiscalía Nacional Económica", "Libre competencia y conductas sancionables",
     "https://www.fne.gob.cl/"),
]


def cita(clave):
    """«Autor — *Obra* (edición)», con el título enlazado a donde se resuelve."""
    autor, obra, edicion, _lente, _cat = bib.LIBROS[clave]
    return "{} — {} ({})".format(autor, enlace(clave, "*{}*".format(obra)), edicion)


def obras_por_parte():
    """Obras que más sostienen cada parte, contando clases y no citas."""
    salida = {}
    for parte in PARTES:
        modulo = importlib.import_module("spec.clases_p{}".format(parte["num"]))
        veces = Counter()
        for clase in modulo.CLASES:
            for clave in clase["libros"]:
                veces[clave] += 1
        # Las rectoras que declara la parte, primero; después las más citadas.
        orden = list(parte["libros"])
        for clave, _n in veces.most_common():
            if clave not in orden:
                orden.append(clave)
        salida[parte["num"]] = (orden, veces)
    return salida


def bloque_partes(lineas):
    lineas += [
        "## Qué sostiene cada parte",
        "",
        "Las obras que ordenan el criterio de cada parte. El índice de cada una lista además "
        "todas las obras que sus clases citan, con el número de clases que usan cada una.",
        "",
        "| Parte | Obras que la sustentan |",
        "|---|---|",
    ]
    datos = obras_por_parte()
    for parte in PARTES:
        orden, _veces = datos[parte["num"]]
        ruta = "../curriculum/{}/README.md".format(parte["slug"])
        obras = " · ".join(cita(k) for k in orden[:3])
        lineas.append("| [{} · {}]({}) | {} |".format(
            parte["num"], parte["titulo"], ruta, obras))
    lineas.append("")


def bloque_areas(lineas):
    lineas += [
        "## Libros de referencia por área",
        "",
        "Las {} obras del programa, agrupadas por lo que aportan. El título enlaza al "
        "catálogo donde se resuelve su ISBN, para que no haya duda de qué edición se "
        "está hablando.".format(len(bib.LIBROS)),
        "",
    ]
    vistas = set()
    for clave_area, titulo in AREAS:
        obras = sorted(
            (k for k, v in bib.LIBROS.items() if v[4] == clave_area),
            key=lambda k: bib.LIBROS[k][1])
        if not obras:
            continue
        vistas.update(obras)
        lineas += ["### {}".format(titulo), ""]
        for k in obras:
            lineas.append("- {} — {}.".format(cita(k), bib.lente(k)))
        lineas.append("")
    faltan = sorted(set(bib.LIBROS) - vistas)
    if faltan:
        raise SystemExit("Obras sin área mapeada en AREAS: {}".format(faltan))


def bloque_normas(lineas):
    lineas += [
        "## Fuentes primarias: normas chilenas",
        "",
        "Texto completo y gratuito en Ley Chile. **La norma vigente manda sobre el material "
        "pedagógico**: si una clase la contradice, gana la norma. Cada clase enlaza aquí "
        "directamente desde su sección de cumplimiento.",
        "",
    ]
    for clave, datos in normas.NORMAS.items():
        lineas.append("- **{}** — {} ({}): <{}>".format(
            datos["numero"], datos["titulo"], datos["organismo"], normas.url(clave)))
    lineas += [
        "",
        "## Organismos que fiscalizan",
        "",
        "Criterios, guías y jurisprudencia administrativa. Cambian sin previo aviso: "
        "compruébalos antes de aplicar cualquier recomendación en una operación real.",
        "",
    ]
    for nombre, que, url in ORGANISMOS:
        lineas.append("- **{}** — {}: <{}>".format(nombre, que, url))
    lineas += [
        "",
        "Listado ampliado con fecha de consulta en "
        "[`FUENTES-OFICIALES.md`](FUENTES-OFICIALES.md) y mapa regulatorio en "
        "[`MAPA-REGULATORIO-CHILE.md`](MAPA-REGULATORIO-CHILE.md).",
        "",
    ]


def bloque_libres(lineas):
    libres = sorted((k for k in bib.LIBROS if acceso(k) == "abierta"),
                    key=lambda k: bib.LIBROS[k][1])
    lineas += [
        "## Qué puedes leer sin pagar",
        "",
        "Las normas de arriba, completas. Y estas obras, que su autor o su organismo "
        "publican de forma gratuita:",
        "",
    ]
    for k in libres:
        lineas.append("- {}.".format(cita(k)))
    lineas += [
        "",
        "El resto son libros comerciales y documentación de editor: se compran, se piden en "
        "biblioteca o se consultan por suscripción. El programa **no distribuye ninguna** y "
        "no reproduce sus textos.",
        "",
    ]


def main():
    lineas = [
        "# 📚 Fuentes",
        "",
        "> [⬅ Programa](../README.md) · [📚 Currículo](../curriculum/README.md) · "
        "[⚖️ Fuentes oficiales](FUENTES-OFICIALES.md)",
        "",
        "Todo lo que este programa afirma se apoya en obras y fuentes primarias "
        "identificables. Aquí están, con su enlace. La redacción del material es original y "
        "no reproduce el texto de ninguna: las cita y enseña a usarlas.",
        "",
        "Cada clase cierra indicando **qué idea concreta** de cada obra sostiene lo que acabas "
        "de leer y **en qué capítulo buscarla**. El identificador comprobable de cada obra "
        "—ISBN-13, DOI o dirección de la fuente— está en "
        "[`sources/bibliography.json`](../sources/bibliography.json).",
        "",
    ]
    bloque_partes(lineas)
    bloque_areas(lineas)
    bloque_normas(lineas)
    bloque_libres(lineas)
    lineas += [
        "---",
        "",
        "[⬅ Documentación](README.md) · [Programa](../README.md)",
        "",
    ]

    with open(DESTINO, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lineas))
    print("docs/FUENTES.md: {} obras, {} normas y {} organismos".format(
        len(bib.LIBROS), len(normas.NORMAS), len(ORGANISMOS)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
