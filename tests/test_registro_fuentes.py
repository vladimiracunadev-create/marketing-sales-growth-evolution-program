# -*- coding: utf-8 -*-
"""Pruebas del registro de fuentes.

`scripts/verify_sources.py` es el control que bloquea; estas pruebas cubren la
parte del contrato que conviene tener aislada, porque son las que fallan
primero cuando alguien añade una obra sin localizador o retoca un ISBN a mano:

* el dígito de control del ISBN-13 se calcula bien (si esta función miente,
  todo lo demás miente);
* toda obra que citan las clases tiene entrada, y ninguna entrada sobra;
* cada localizador tiene la forma canónica de su tipo;
* lo pendiente está declarado como pendiente y dice qué le falta;
* el registro publicado coincide con lo que produce el generador.
"""

from __future__ import annotations

import importlib
import json
import os
import re
import subprocess
import sys

import pytest

RE_ISBN13 = re.compile(r"^97[89]\d{10}$")
RE_FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")
RE_ID = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

TIPOS_URL = {"standard", "reference", "dataset"}


@pytest.fixture(scope="session")
def verificador():
    sys.path.insert(0, os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))
    return importlib.import_module("verify_sources")


@pytest.fixture(scope="session")
def registro(raiz):
    with open(os.path.join(raiz, "sources", "bibliography.json"), encoding="utf-8") as fh:
        return json.load(fh)


@pytest.fixture(scope="session")
def entradas(registro):
    return registro["entries"]


def test_el_digito_de_control_del_isbn_se_calcula_bien(verificador):
    """Casos conocidos. Si esta comprobación cede, el registro entero es humo."""
    assert verificador.isbn13_valido("9780262033848")   # ISBN real y bien formado
    assert not verificador.isbn13_valido("9780262033847")  # mismo ISBN, dígito cambiado
    assert not verificador.isbn13_valido("978026203384")   # una cifra de menos
    assert not verificador.isbn13_valido("")
    assert not verificador.isbn13_valido("abcdefghijklm")


def test_la_cabecera_del_registro_declara_su_politica(registro):
    assert registro["schema_version"] == 1
    assert RE_FECHA.match(registro["verified_on"])
    assert "localizador" in registro["policy"]


def test_cada_entrada_trae_los_campos_del_esquema(entradas):
    for e in entradas:
        assert RE_ID.match(e["id"]), e["id"]
        assert e["type"] in {"book", "paper", "standard", "reference", "dataset"}
        assert e["authors"] and all(a.strip() for a in e["authors"])
        assert e["title"].strip()
        assert re.match(r"^\d{4}$", e["published"]), e["id"]
        assert e["authority"].strip(), e["id"]
        assert e["status"] in {"verificada", "pendiente"}


def test_los_identificadores_no_se_repiten(entradas):
    ids = [e["id"] for e in entradas]
    assert len(ids) == len(set(ids))


def test_todo_libro_verificado_tiene_isbn13_valido(entradas, verificador):
    for e in entradas:
        if e["type"] == "book" and e["status"] == "verificada":
            assert RE_ISBN13.match(e["isbn13"]), e["id"]
            assert verificador.isbn13_valido(e["isbn13"]), e["id"]


def test_el_localizador_tiene_la_forma_canonica_de_su_tipo(entradas):
    for e in entradas:
        if e["status"] != "verificada":
            continue
        if e["type"] == "book":
            assert e["locator"] == "https://openlibrary.org/isbn/{}".format(e["isbn13"]), e["id"]
        elif e["type"] == "paper":
            assert e["locator"] == "https://doi.org/{}".format(e["doi"]), e["id"]
        else:
            assert e["locator"].startswith("https://"), e["id"]
            assert RE_FECHA.match(e["accessed"]), e["id"]


def test_lo_pendiente_dice_que_le_falta(entradas):
    """Un hueco declarado es información; un hueco mudo es una omisión."""
    for e in entradas:
        if e["status"] == "pendiente":
            assert not e["locator"], e["id"]
            assert e["note"].strip(), e["id"]


def test_toda_obra_citada_tiene_entrada_y_ninguna_entrada_sobra(entradas, libros):
    assert {e["id"] for e in entradas} == set(libros)


def test_el_uso_declarado_coincide_con_la_especificacion(entradas, partes, raiz):
    from spec.bibliografia import NUCLEO_PEDAGOGICO

    rutas = {}
    for parte in partes:
        modulo = importlib.import_module("spec.clases_p{}".format(parte["num"]))
        for clase in modulo.CLASES:
            ruta = "curriculum/{}/class-{}-{}.md".format(
                parte["slug"], clase["n"], clase["slug"])
            for clave in list(clase["libros"]) + list(NUCLEO_PEDAGOGICO):
                rutas.setdefault(clave, set()).add(ruta)

    for e in entradas:
        assert set(e["used_in"]) == rutas[e["id"]], e["id"]
        for r in e["used_in"]:
            assert os.path.exists(os.path.join(raiz, r.replace("/", os.sep))), r


def test_el_registro_publicado_es_el_que_produce_el_generador(raiz, tmp_path):
    """El registro es contenido generado: si se edita a mano, se pierde."""
    ruta = os.path.join(raiz, "sources", "bibliography.json")
    with open(ruta, encoding="utf-8") as fh:
        antes = fh.read()
    subprocess.check_call(
        [sys.executable, os.path.join(raiz, "tools", "build_bibliography_json.py")],
        stdout=subprocess.DEVNULL)
    with open(ruta, encoding="utf-8") as fh:
        despues = fh.read()
    assert antes == despues, (
        "sources/bibliography.json no coincide con curriculum/spec/. "
        "Ejecuta python tools/build_bibliography_json.py")


def test_toda_norma_nombrada_enlaza_su_texto(raiz, partes):
    """Nombrar una ley y no enlazarla obliga al lector a fiarse.

    Son las únicas fuentes del programa que se leen completas y gratis: si una
    clase las menciona, tiene que llevar a su texto oficial.
    """
    from spec import normas

    fallos = []
    for parte in partes:
        base = os.path.join(raiz, "curriculum", parte["slug"])
        for archivo in sorted(os.listdir(base)):
            if not archivo.startswith("class-"):
                continue
            with open(os.path.join(base, archivo), encoding="utf-8") as fh:
                texto = fh.read()
            for clave, datos in normas.NORMAS.items():
                if datos["numero"] in texto and normas.url(clave) not in texto:
                    fallos.append("{}/{}: {}".format(parte["slug"], archivo, datos["numero"]))
    assert not fallos, fallos[:5]


def test_el_acceso_de_cada_obra_esta_declarado(entradas):
    """Quien abre la bibliografía tiene derecho a saber qué puede leer gratis."""
    validos = {"abierta", "restringida", "de-pago", "comercial"}
    for e in entradas:
        assert e["access"] in validos, (e["id"], e.get("access"))


def test_el_verificador_da_verde(raiz):
    proceso = subprocess.run(
        [sys.executable, os.path.join(raiz, "scripts", "verify_sources.py")],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    assert proceso.returncode == 0, proceso.stdout.decode("utf-8", "replace")
