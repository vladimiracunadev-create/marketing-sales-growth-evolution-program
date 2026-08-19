# -*- coding: utf-8 -*-
"""Pruebas de la fundamentación bibliográfica y del desarrollo escrito.

Verifican los requisitos que `clase-profunda-v2` añadió sobre `v1`:

* R8  — cada obra citada declara qué idea concreta suya sostiene la clase.
* R14 — el desarrollo está redactado para esa clase y no se reutiliza.

Son las dos condiciones que separan una cita real de una cita decorativa.
"""

from __future__ import annotations

import importlib
import re

import pytest


@pytest.fixture(scope="session")
def aportes():
    from spec.aportes import APORTES
    return APORTES


@pytest.fixture(scope="session")
def anclajes():
    from spec.anclajes import ANCLAJES
    return ANCLAJES


@pytest.fixture(scope="session")
def desarrollos(partes):
    """Devuelve {"PP.CC": [párrafos]} para las 336 clases."""
    salida = {}
    for parte in partes:
        modulo = importlib.import_module("spec.desarrollo_p{}".format(parte["num"]))
        for numero, parrafos in modulo.DESARROLLO.items():
            salida["{}.{}".format(parte["num"], numero)] = parrafos
    return salida


# ---------------------------------------------------------------- aportes

def test_todas_las_obras_tienen_aportes_catalogados(aportes, libros):
    faltan = sorted(set(libros) - set(aportes))
    assert not faltan, "Obras sin ideas catalogadas: {}".format(faltan)


def test_no_hay_aportes_de_obras_inexistentes(aportes, libros):
    sobran = sorted(set(aportes) - set(libros))
    assert not sobran, "Aportes de obras que no están en la bibliografía: {}".format(sobran)


def test_cada_aporte_declara_idea_y_donde_buscarla(aportes):
    for clave, ideas in aportes.items():
        for identificador, valor in ideas.items():
            assert isinstance(valor, tuple) and len(valor) == 2, \
                "{}:{} debe ser (idea, dónde buscarla)".format(clave, identificador)
            idea, donde = valor
            assert len(idea.split()) >= 5, \
                "La idea de {}:{} es demasiado vaga para citarse".format(clave, identificador)
            assert len(donde.split()) >= 3, \
                "{}:{} no indica dónde buscar la idea".format(clave, identificador)


def test_ninguna_pista_de_lectura_cita_paginas(aportes):
    """Las páginas cambian entre ediciones: el programa no puede garantizarlas."""
    # Sólo se rechaza la referencia numérica: «el capítulo sobre diseño de
    # páginas» habla de páginas web y es una pista de lectura legítima.
    numerada = re.compile(r"(p[áa]g(?:ina)?s?\.?|pp?\.)\s*\d", re.I)
    for clave, ideas in aportes.items():
        for identificador, (_idea, donde) in ideas.items():
            assert not numerada.search(donde), \
                "{}:{} cita páginas: «{}»".format(clave, identificador, donde)


# ---------------------------------------------------------------- anclajes

def test_cada_clase_tiene_anclaje(anclajes, todas_las_clases, partes):
    esperadas = set()
    for parte in partes:
        modulo = importlib.import_module("spec.clases_p{}".format(parte["num"]))
        for clase in modulo.CLASES:
            esperadas.add("{}.{}".format(parte["num"], clase["n"]))
    assert set(anclajes) == esperadas


def test_cada_obra_citada_esta_anclada(anclajes, partes):
    for parte in partes:
        modulo = importlib.import_module("spec.clases_p{}".format(parte["num"]))
        for clase in modulo.CLASES:
            ref = "{}.{}".format(parte["num"], clase["n"])
            mapa = anclajes[ref]
            assert set(mapa) == set(clase["libros"]), \
                "La clase {} cita {} y ancla {}".format(ref, clase["libros"], sorted(mapa))


def test_los_identificadores_de_anclaje_existen(anclajes, aportes):
    for ref, mapa in anclajes.items():
        for clave, identificador in mapa.items():
            assert identificador in aportes.get(clave, {}), \
                "{} ancla {}:{}, que no está catalogado".format(ref, clave, identificador)


def test_ningun_anclaje_repite_el_lente_general(anclajes, aportes, libros):
    """Si la frase sirve para cualquier clase que cite la obra, no ancla ninguna."""
    for ref, mapa in anclajes.items():
        for clave, identificador in mapa.items():
            idea = aportes[clave][identificador][0]
            lente = libros[clave][3]
            assert idea.strip().lower() != lente.strip().lower(), \
                "{} ancla {} con su lente general".format(ref, clave)


# ---------------------------------------------------------------- desarrollo

def test_cada_clase_tiene_cinco_parrafos_de_desarrollo(desarrollos, anclajes):
    assert set(desarrollos) == set(anclajes)
    for ref, parrafos in desarrollos.items():
        assert len(parrafos) >= 5, "La clase {} tiene {} párrafos".format(ref, len(parrafos))


def test_ningun_parrafo_de_desarrollo_se_reutiliza(desarrollos):
    """R14: el desarrollo se escribe para esa clase; no es una plantilla."""
    vistos = {}
    for ref, parrafos in desarrollos.items():
        for i, parrafo in enumerate(parrafos, start=1):
            clave = parrafo.strip()
            anterior = vistos.get(clave)
            assert anterior is None, \
                "El párrafo {}#{} repite el de {}".format(ref, i, anterior)
            vistos[clave] = "{}#{}".format(ref, i)


def test_los_parrafos_tienen_sustancia(desarrollos):
    for ref, parrafos in desarrollos.items():
        for i, parrafo in enumerate(parrafos, start=1):
            palabras = len(parrafo.split())
            assert palabras >= 35, \
                "El párrafo {}#{} tiene {} palabras".format(ref, i, palabras)
            assert parrafo.count(".") >= 2, \
                "El párrafo {}#{} es una sola frase".format(ref, i)
