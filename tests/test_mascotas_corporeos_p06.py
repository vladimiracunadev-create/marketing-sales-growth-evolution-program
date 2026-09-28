# -*- coding: utf-8 -*-
"""Regresiones de la integración de mascotas de marca y corpóreos en Parte 06."""

from __future__ import annotations

import os


PARTE_06 = "part-06-marca-branding-y-comunicacion-estrategica"


def leer(raiz, *partes):
    with open(os.path.join(raiz, *partes), encoding="utf-8") as fh:
        return fh.read()


def test_desarrollo_principal_persiste_en_0606(raiz):
    texto = leer(raiz, "curriculum", PARTE_06, "class-06-identidad-visual-criterios.md")
    for marcador in (
            "mascota de marca", "corpóreo", "intérprete", "acompañante",
            "atribución correcta a la empresa", "retorno incremental estimado",
            "sin contar varias fotos de una persona como varias personas", "Ley 21.430", "Decreto 594/1999"):
        assert marcador in texto, marcador


def test_conexiones_acotadas_estan_en_las_clases_previstas(raiz):
    esperadas = {
        "class-03-proposito-promesa-y-personalidad.md": "conducta observable",
        "class-12-coherencia-omnicanal.md": "Una mascota añade un canal conductual",
        "class-13-medicion-de-marca.md": "atribución correcta a la empresa",
        "class-14-brand-book-minimo-viable.md": "Si existe mascota",
    }
    for archivo, marcador in esperadas.items():
        assert marcador in leer(raiz, "curriculum", PARTE_06, archivo)


def test_tema_no_se_propaga_a_marca_personal_ni_otras_partes(raiz):
    marca_personal = leer(raiz, "curriculum", PARTE_06, "class-11-employer-y-personal-branding.md")
    assert "corpóreo" not in marca_personal
    for parte in os.listdir(os.path.join(raiz, "curriculum")):
        if not parte.startswith("part-") or parte == PARTE_06:
            continue
        carpeta = os.path.join(raiz, "curriculum", parte)
        for archivo in os.listdir(carpeta):
            if archivo.startswith("class-") and archivo.endswith(".md"):
                assert "corpóreo" not in leer(raiz, "curriculum", parte, archivo), (parte, archivo)


def test_caso_evaluacion_y_proyecto_exigen_decision_completa(raiz):
    unidos = "\n".join([
        leer(raiz, "cases", "case-06-marca-branding-y-comunicacion-estrategica.md"),
        leer(raiz, "assessments", "part-06-assessment.md"),
        leer(raiz, "projects", "project-03-parts-05-06.md"),
    ])
    for marcador in ("Ruti", "con y sin corpóreo", "continuar, ajustar o detener", "descarte el corpóreo"):
        assert marcador in unidos, marcador


def test_cantidades_publicadas_se_conservan(raiz):
    clases = sum(
        1 for base, _dirs, archivos in os.walk(os.path.join(raiz, "curriculum"))
        for archivo in archivos if archivo.startswith("class-") and archivo.endswith(".md"))
    laboratorios = sum(
        1 for base, _dirs, archivos in os.walk(os.path.join(raiz, "labs"))
        for archivo in archivos if archivo.endswith(".md"))
    assert clases == 336
    assert laboratorios == 48
