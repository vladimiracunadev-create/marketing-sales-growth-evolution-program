# -*- coding: utf-8 -*-
"""Normas chilenas que el programa cita, con su texto oficial enlazado.

Estas son las únicas fuentes del programa que cualquiera puede abrir, leer
completas y contrastar sin pagar nada. Por eso se tratan distinto del resto de
la bibliografía: aquí no hay atribución que creer, hay un texto al que ir.

El título de cada norma no está escrito de memoria: es el que devuelve la
propia Biblioteca del Congreso Nacional en su servicio de metadatos
(``nuevo.leychile.cl/servicios/Consulta/obtxml?opt=7&idNorma=...``), consultado
en la fecha de ``CONFIRMADO_EN``. Si alguna vez deja de coincidir, es que la
norma cambió y manda la norma, no este archivo.

Cada entrada declara:

===============  ==========================================================
``numero``       cómo se la nombra en el texto de las clases
``titulo``       título oficial, tal como lo publica BCN
``organismo``    quién la dictó
``id_norma``     identificador de BCN, que es lo que hace resoluble la URL
``url``          texto completo y gratuito
``materia``      para qué se cita dentro del programa
===============  ==========================================================
"""

from __future__ import annotations

# Fecha en que se contrastó cada título contra el servicio de metadatos de BCN.
CONFIRMADO_EN = "2026-08-19"

BASE = "https://www.bcn.cl/leychile/navegar?idNorma={}"

NORMAS = {
    "ley-19496": {
        "numero": "Ley 19.496",
        "titulo": "Establece normas sobre protección de los derechos de los consumidores",
        "organismo": "Ministerio de Economía, Fomento y Reconstrucción",
        "id_norma": "61438",
        "materia": "derechos del consumidor, publicidad engañosa, información y garantías",
    },
    "ley-21719": {
        "numero": "Ley 21.719",
        "titulo": ("Regula la protección y el tratamiento de los datos personales y crea "
                   "la Agencia de Protección de Datos Personales"),
        "organismo": "Ministerio Secretaría General de la Presidencia",
        "id_norma": "1209272",
        "materia": "tratamiento de datos personales, bases de licitud y derechos del titular",
    },
    "ley-19628": {
        "numero": "Ley 19.628",
        "titulo": "Sobre protección de la vida privada",
        "organismo": "Ministerio Secretaría General de la Presidencia",
        "id_norma": "141599",
        "materia": "régimen previo de datos personales, todavía aplicable en lo no derogado",
    },
    "decreto-6-2021": {
        "numero": "Decreto 6/2021",
        "titulo": "Aprueba reglamento de comercio electrónico",
        "organismo": "Ministerio de Economía, Fomento y Turismo",
        "id_norma": "1165504",
        "materia": "obligaciones del proveedor en venta a distancia y comercio electrónico",
    },
    "decreto-52-2024": {
        "numero": "Decreto 52/2024",
        "titulo": ("Aprueba reglamento que regula la forma y condiciones en que los "
                   "proveedores deberán comunicar la exclusión del derecho a retracto y "
                   "los bienes en que excepcionalmente y por su naturaleza procederá tal "
                   "exclusión"),
        "organismo": "Ministerio de Economía, Fomento y Turismo",
        "id_norma": "1206144",
        "materia": "cómo debe comunicarse la exclusión del derecho a retracto",
    },
}


def url(clave):
    """Texto completo y gratuito de la norma en Ley Chile."""
    return BASE.format(NORMAS[clave]["id_norma"])


def enlace(clave):
    """La norma citada como se debe citar: nombre enlazado a su texto."""
    return "[{}]({})".format(NORMAS[clave]["numero"], url(clave))


def cita(clave):
    """Nombre, título oficial y enlace, para cuando hace falta el detalle."""
    n = NORMAS[clave]
    return "{} — *{}* ({})".format(enlace(clave), n["titulo"], n["organismo"])
