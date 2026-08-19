# -*- coding: utf-8 -*-
"""Escribe la bibliografía del programa dentro del README principal.

Un curso que dice apoyarse en 96 obras tiene que enseñarlas. Da igual lo bien
construido que esté el registro en JSON: si quien abre el repositorio no ve en
ninguna parte de qué libros sale el contenido, para él ese contenido no tiene
fuentes. Por eso la lista vive aquí, a la vista, con lo que aporta cada obra y
el enlace donde se resuelve su edición exacta —que es lo que faltaba antes: la
lista existía, pero sin una sola dirección que seguir—.

Las cifras del registro **no se escriben a mano**. Se toman de
`sources/bibliography.json` y `scripts/verify_sources.py` falla si el README
publica otras.

Marcas en README.md:
    <!-- BIBLIOGRAFIA:INICIO -->     ... bloque completo ...   <!-- BIBLIOGRAFIA:FIN -->
    <!-- REGISTRO-FUENTES:INICIO --> ... tabla de cifras ...   <!-- REGISTRO-FUENTES:FIN -->

Uso:
    python tools/build_readme_bibliografia.py
"""

from __future__ import annotations

import importlib
import json
import os
import sys
from collections import Counter

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "curriculum"))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from spec import bibliografia as bib  # noqa: E402
from spec.anclajes import ANCLAJES  # noqa: E402
from spec.aportes import APORTES  # noqa: E402
from spec.localizadores import acceso, acceso_legible, enlace, etiqueta  # noqa: E402
from spec.partes import PARTES  # noqa: E402

INICIO = "<!-- BIBLIOGRAFIA:INICIO -->"
FIN = "<!-- BIBLIOGRAFIA:FIN -->"
INICIO_CIFRAS = "<!-- REGISTRO-FUENTES:INICIO -->"
FIN_CIFRAS = "<!-- REGISTRO-FUENTES:FIN -->"

REGISTRO = os.path.join(RAIZ, "sources", "bibliography.json")

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

# Orden de lectura del bloque de cifras: del total a lo que falta.
ORDEN_CIFRAS = [
    "entradas del registro",
    "obras con localizador verificado",
    "libros con ISBN-13",
    "entradas pendientes",
]


def registro():
    if not os.path.exists(REGISTRO):
        raise SystemExit(
            "Falta sources/bibliography.json. Ejecuta primero:\n"
            "  python tools/build_bibliography_json.py")
    with open(REGISTRO, encoding="utf-8") as fh:
        return json.load(fh)


def uso_por_obra():
    """En cuántas clases distintas aparece cada obra.

    Se cuentan clases, no citas: una obra del núcleo pedagógico que además se
    cite de forma explícita en una clase no puede sumar esa clase dos veces y
    acabar declarando más clases de las que tiene el programa.
    """
    clases_de = {}
    for parte in PARTES:
        modulo = importlib.import_module("spec.clases_p{}".format(parte["num"]))
        for clase in modulo.CLASES:
            ref = "{}.{}".format(parte["num"], clase["n"])
            for clave in list(clase["libros"]) + list(bib.NUCLEO_PEDAGOGICO):
                clases_de.setdefault(clave, set()).add(ref)
    return Counter({k: len(v) for k, v in clases_de.items()})


def frase_acceso():
    """Cuántas obras se pueden leer gratis y cuántas no. Sin adornos.

    Un lector que abre la bibliografía y descubre a los tres clics que todo
    está detrás de un pago tiene derecho a saberlo antes.
    """
    cuenta = Counter(acceso(k) for k in bib.LIBROS)
    partes = []
    if cuenta["abierta"]:
        partes.append("**{}** se pueden leer completas y gratis en su fuente".format(
            cuenta["abierta"]))
    if cuenta["restringida"]:
        partes.append("**{}** están publicadas por su editor pero con acceso limitado o de "
                      "pago".format(cuenta["restringida"]))
    if cuenta["de-pago"]:
        partes.append("**{}** es una norma que hay que comprar al organismo emisor".format(
            cuenta["de-pago"]))
    if cuenta["comercial"]:
        partes.append("y **{}** son libros comerciales: se compran o se piden en "
                      "biblioteca".format(cuenta["comercial"]))
    return ("De las {} obras, {}. El programa no distribuye ninguna: las cita, las contrasta y "
            "enseña a usarlas de forma selectiva.".format(len(bib.LIBROS), "; ".join(partes)))


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
    veces = uso_por_obra()
    total_anclajes = sum(len(v) for v in ANCLAJES.values())
    total_aportes = sum(len(v) for v in APORTES.values())
    c = cifras(datos)

    lineas = [
        INICIO,
        "",
        "## 📚 Bibliografía: qué está comprobado y qué es atribución",
        "",
        "Estas son las **{} obras** sobre las que se apoya el programa. Antes de la lista conviene "
        "separar dos cosas que las bibliografías suelen mezclar, porque de esa mezcla salen las "
        "citas que nadie puede comprobar.".format(c["entradas del registro"]),
        "",
        "**Comprobado:** que cada obra existe y cuál es exactamente la edición. Los {} localizadores "
        "resuelven contra el catálogo de OpenLibrary, contra doi.org o contra el sitio del organismo "
        "emisor, y se revalidan periódicamente. Eso es un hecho verificable y cualquiera puede "
        "repetir la comprobación.".format(c["obras con localizador verificado"]),
        "",
        "**Atribución del programa:** que la idea que cada clase señala esté en el capítulo que "
        "indica. De estas obras se catalogaron **{} ideas**, y las 336 clases declaran cuál de ellas "
        "sostiene cada una de sus citas —**{} anclajes**—. Esa atribución es la lectura que el "
        "programa hace de cada obra; **no está cotejada frase por frase contra el texto**, y se "
        "declara con este detalle justamente para que se pueda contrastar. Si abres una obra y la "
        "idea no está donde se dice, la cita está mal puesta y corresponde reportarlo como error del "
        "material. En los términos del [estándar de evidencia](docs/ESTANDAR-DE-EVIDENCIA.md) del "
        "propio programa: el localizador es un hecho verificado; la atribución, una inferencia "
        "declarada.".format(total_aportes, total_anclajes),
        "",
        "**Qué cuesta comprobarlo.** {}".format(frase_acceso()),
        "",
        "La excepción son las normas chilenas, que sí se pueden leer completas y gratis: cada clase "
        "enlaza el texto oficial en Ley Chile, con el título tal como lo publica la Biblioteca del "
        "Congreso Nacional. Ahí no hay nada que creer.",
        "",
        INICIO_CIFRAS,
        "",
        "| Estado del registro de fuentes | Valor |",
        "|---|---:|",
    ]
    for etiq in ORDEN_CIFRAS:
        lineas.append("| {} | **{}** |".format(etiq, c[etiq]))
    lineas += [
        "",
        "Última revalidación contra openlibrary.org y las fuentes oficiales: "
        "**{}**.".format(datos["verified_on"]),
        "",
        FIN_CIFRAS,
        "",
        "> [!NOTE]",
        "> Estas cifras las produce `python scripts/verify_sources.py`, que falla si el README "
        "declara otras. No se escriben a mano. El registro completo, con el uso de cada obra clase "
        "a clase, está en [`sources/bibliography.json`](sources/bibliography.json).",
        "",
        "> [!NOTE]",
        "> Nunca se citan números de página: cambian entre ediciones y el programa no puede "
        "garantizarlas. El anclaje indica el capítulo o la sección **por su nombre dentro de la "
        "obra**. Por la misma razón cada obra enlaza a su localizador: para que no tengas que "
        "adivinar de qué edición se está hablando.",
        "",
        "El programa **no distribuye** ninguna de estas obras: las cita, las contrasta y enseña a "
        "usarlas de forma selectiva. Toda la redacción es original y no reproduce sus textos. El "
        "acceso debe obtenerse por biblioteca, editorial, librería o suscripción legítima.",
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
            "### {}".format(titulo_cat),
            "",
            "| Autoría | Obra | Edición | Qué aporta al programa | Clases | Localizador | Acceso |",
            "|---|---|---|---|---:|---|---|",
        ]
        for k in obras:
            autor, obra, edicion, lente, _cat = bib.LIBROS[k]
            lineas.append("| {} | {} | {} | {} | {} | {} | {} |".format(
                autor, enlace(k, "*{}*".format(obra)), edicion, lente,
                veces.get(k, 0), etiqueta(k), acceso_legible(k)))
        lineas.append("")

    faltan = sorted(set(bib.LIBROS) - vistos)
    if faltan:
        raise SystemExit("Categorías sin mapear en CATEGORIAS: {}".format(faltan))

    lineas += [
        "### Fuentes oficiales y normativas",
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
        "### Dónde encontrar esto mismo, más cerca del contenido",
        "",
        "Cada una de las 24 partes abre con su propia bibliografía: las obras que sostienen esa "
        "parte, cuántas de sus clases citan cada una y el mismo enlace al localizador. Y cada "
        "clase cierra declarando, obra por obra, **qué idea concreta** de ella sostiene lo que "
        "acabas de leer y en qué capítulo buscarla. La lista completa por categorías, con el uso "
        "clase a clase, está también en [`docs/BIBLIOGRAFIA.md`](docs/BIBLIOGRAFIA.md).",
        "",
        "**Núcleo pedagógico.** El diseño instruccional del programa —no su contenido comercial— "
        "se apoya en {}.".format("; ".join(
            "{} — {} ({})".format(bib.autor(k), enlace(k, "*{}*".format(bib.obra(k))),
                                  bib.LIBROS[k][2])
            for k in bib.NUCLEO_PEDAGOGICO)),
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

    c = cifras(registro())
    print("README.md: bibliografía de {} obras a la vista ({} con localizador, "
          "{} pendientes)".format(c["entradas del registro"],
                                  c["obras con localizador verificado"],
                                  c["entradas pendientes"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
