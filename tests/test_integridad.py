# -*- coding: utf-8 -*-
"""Pruebas de integridad del repositorio: enlaces, datos y herramientas."""

from __future__ import annotations

import csv
import json
import os
import re

RE_ENLACE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
IGNORAR = {".git", ".github", "site", "__pycache__", "node_modules", ".pytest_cache"}


def archivos_markdown(raiz):
    for actual, dirs, files in os.walk(raiz):
        dirs[:] = [d for d in dirs if d not in IGNORAR and not d.startswith(".")]
        for f in sorted(files):
            if f.endswith(".md"):
                yield os.path.join(actual, f)


def test_enlaces_internos_resuelven(raiz):
    rotos = []
    for ruta in archivos_markdown(raiz):
        with open(ruta, encoding="utf-8") as fh:
            contenido = fh.read()
        base = os.path.dirname(ruta)
        for destino in RE_ENLACE.findall(contenido):
            if destino.startswith(("http://", "https://", "mailto:", "#")):
                continue
            objetivo = destino.split("#", 1)[0]
            if not objetivo:
                continue
            absoluto = os.path.normpath(os.path.join(base, objetivo))
            if not os.path.exists(absoluto):
                rotos.append("{} -> {}".format(os.path.relpath(ruta, raiz), destino))
    assert not rotos, "Enlaces rotos:\n" + "\n".join(rotos[:20])


def test_curriculum_json_es_coherente(raiz):
    ruta = os.path.join(raiz, "curriculum", "curriculum.json")
    assert os.path.isfile(ruta)
    with open(ruta, encoding="utf-8") as fh:
        datos = json.load(fh)
    assert len(datos["partes"]) == 24
    assert sum(len(p["clases"]) for p in datos["partes"]) == 336
    for parte in datos["partes"]:
        for clase in parte["clases"]:
            assert os.path.isfile(os.path.join(raiz, clase["ruta"])), clase["ruta"]


def test_datasets_tienen_cabecera_y_filas(raiz):
    base = os.path.join(raiz, "datasets")
    csvs = [f for f in os.listdir(base) if f.endswith(".csv")]
    assert csvs, "No hay conjuntos de datos"
    for nombre in csvs:
        with open(os.path.join(base, nombre), encoding="utf-8", newline="") as fh:
            filas = list(csv.reader(fh))
        assert len(filas) >= 2, "{} sin filas de datos".format(nombre)
        assert all(c.strip() for c in filas[0]), "{} con cabecera vacía".format(nombre)
        ancho = len(filas[0])
        for i, fila in enumerate(filas[1:], start=2):
            if not fila:
                continue
            assert len(fila) == ancho, "{}: fila {} con {} columnas".format(nombre, i, len(fila))


def test_notebooks_son_json_valido(raiz):
    base = os.path.join(raiz, "notebooks")
    for nombre in os.listdir(base):
        if not nombre.endswith(".ipynb"):
            continue
        with open(os.path.join(base, nombre), encoding="utf-8") as fh:
            datos = json.load(fh)
        assert "cells" in datos, "{} sin celdas".format(nombre)


def test_herramientas_compilan(raiz):
    import py_compile
    base = os.path.join(raiz, "tools")
    for nombre in sorted(os.listdir(base)):
        if nombre.endswith(".py"):
            py_compile.compile(os.path.join(base, nombre), doraise=True)


def test_version_es_semantica(raiz):
    with open(os.path.join(raiz, "VERSION"), encoding="utf-8") as fh:
        version = fh.read().strip()
    assert re.match(r"^\d+\.\d+\.\d+$", version), "VERSION inválida: {}".format(version)


def test_readme_declara_cifras_coherentes(raiz):
    with open(os.path.join(raiz, "README.md"), encoding="utf-8") as fh:
        readme = fh.read()
    clases = 0
    for actual, dirs, files in os.walk(os.path.join(raiz, "curriculum")):
        dirs[:] = [d for d in dirs if not d.startswith((".", "__"))]
        clases += sum(1 for f in files if f.startswith("class-") and f.endswith(".md"))
    assert str(clases) in readme, "README no refleja el número real de clases ({})".format(clases)


def test_no_hay_marcadores_de_trabajo_pendiente(raiz):
    pendientes = []
    for ruta in archivos_markdown(raiz):
        if os.path.basename(ruta) in ("CHANGELOG.md", "ROADMAP.md", "CONTRIBUTING.md"):
            continue
        with open(ruta, encoding="utf-8") as fh:
            contenido = fh.read()
        for marcador in ("TODO:", "FIXME:", "XXX:", "Lorem ipsum"):
            if marcador in contenido:
                pendientes.append("{}: {}".format(os.path.relpath(ruta, raiz), marcador))
    assert not pendientes, "Marcadores pendientes:\n" + "\n".join(pendientes[:20])


def test_conversor_markdown_funciona():
    from markdown_min import render
    html, meta, encabezados = render(
        "---\ntitle: \"Prueba\"\n---\n\n# Título\n\nTexto con **negrita** y `código`.\n\n"
        "| A | B |\n|---|---:|\n| 1 | 2 |\n\n- uno\n- dos\n\n> Cita\n\n```python\nprint(1)\n```\n")
    assert meta["title"] == "Prueba"
    assert "<h1" in html and "<strong>negrita</strong>" in html
    assert "<code>código</code>" in html
    assert "<table>" in html and 'class="al-right"' in html
    assert "<ul>" in html and "<blockquote>" in html
    assert 'data-lang="python"' in html
