# -*- coding: utf-8 -*-
"""Configuración compartida de las pruebas."""

from __future__ import annotations

import importlib
import os
import sys

import pytest

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "curriculum"))
sys.path.insert(0, os.path.join(RAIZ, "tools"))


@pytest.fixture(scope="session")
def raiz():
    return RAIZ


@pytest.fixture(scope="session")
def partes():
    from spec.partes import PARTES
    return PARTES


@pytest.fixture(scope="session")
def libros():
    from spec.bibliografia import LIBROS
    return LIBROS


@pytest.fixture(scope="session")
def clases_por_parte(partes):
    datos = {}
    for parte in partes:
        modulo = importlib.import_module("spec.clases_p{}".format(parte["num"]))
        datos[parte["num"]] = modulo.CLASES
    return datos


@pytest.fixture(scope="session")
def todas_las_clases(clases_por_parte):
    salida = []
    for num, clases in clases_por_parte.items():
        for c in clases:
            salida.append((num, c))
    return salida


def leer(ruta):
    with open(ruta, encoding="utf-8") as fh:
        return fh.read()
