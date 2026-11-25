# -*- coding: utf-8 -*-
"""Los modelos mentales SVG existen para cada clase, son válidos y reflejan el contenido de su clase."""

import hashlib
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import modelos_svg  # noqa: E402


def svgs_del_curriculo():
    return sorted((ROOT / "curriculum").glob("part-*/modelos/modelo-*.svg"))


def test_hay_un_modelo_por_clase_y_ninguno_sobra():
    clases = list((ROOT / "curriculum").glob("part-*/class-*.md"))
    assert len(svgs_del_curriculo()) == len(clases) == 336
    for clase in clases:
        n = clase.name.split("-")[1]
        assert (clase.parent / "modelos" / "modelo-{}.svg".format(n)).exists(), clase.name


def test_cada_clase_enlaza_su_diagrama_con_texto_alternativo():
    for clase in (ROOT / "curriculum").glob("part-*/class-*.md"):
        texto = clase.read_text(encoding="utf-8")
        n = clase.name.split("-")[1]
        assert "(modelos/modelo-{}.svg)".format(n) in texto, clase.name
        assert "**Descripción textual del método.**" in texto, clase.name


def test_los_svg_son_xml_valido_y_accesibles():
    todos = svgs_del_curriculo() + list((ROOT / "curriculum" / "specializations").rglob("modelo-*.svg"))
    assert len(todos) == 346
    for ruta in todos:
        raiz = ET.fromstring(ruta.read_text(encoding="utf-8"))
        assert raiz.tag.endswith("svg"), ruta
        assert raiz.attrib["role"] == "img"
        nombres = {e.tag.split("}")[1] for e in raiz}
        assert {"title", "desc"} <= nombres, ruta
        assert "http" not in "".join(raiz.itertext()), ruta


def test_los_diagramas_no_son_una_misma_plantilla():
    huellas = set()
    formas = set()
    for ruta in svgs_del_curriculo():
        texto = ruta.read_text(encoding="utf-8")
        huellas.add(hashlib.sha1(texto.encode("utf-8")).hexdigest())
        formas.add(("anillo" if "<ellipse" in texto else "otra"))
    assert len(huellas) == len(svgs_del_curriculo())
    assert "anillo" in formas and "otra" in formas


def test_el_diagrama_contiene_el_texto_de_la_clase():
    import importlib
    sys.path.insert(0, str(ROOT / "curriculum"))
    modulo = importlib.import_module("spec.clases_p06")
    for clase in modulo.CLASES:
        svg = (ROOT / "curriculum" / "part-06-marca-branding-y-comunicacion-estrategica" / "modelos"
               / "modelo-{}.svg".format(clase["n"])).read_text(encoding="utf-8")
        assert clase["titulo"].replace("&", "&amp;") in svg
        primer_paso = modelos_svg.esc(clase["metodo"][0][0].upper() + clase["metodo"][0][1:])
        assert primer_paso.split()[0] in svg


def test_las_insignias_de_enlace_surgen_del_vocabulario_compartido():
    pasos = ["verificar la fuente y el estado procesal", "comunicar hechos confirmados"]
    conceptos = [("estado procesal", "etiqueta del avance judicial"), ("reputación", "juicio acumulado")]
    enlaces = modelos_svg.vinculos(conceptos, pasos)
    assert enlaces[0] == [1] and enlaces[1] == []


def test_las_fichas_se_dibujan_como_fraccion():
    assert modelos_svg.dividir_ficha("compras repetidas, sobre clientes activos") == ("compras repetidas", "clientes activos", "")
    num, den, nota = modelos_svg.dividir_ficha(
        "numerador: a; denominador o base sobre la que se calcula: b; ventana: mes; fuente: CRM")
    assert (num, den) == ("a", "b") and "mes" in nota
