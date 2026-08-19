# -*- coding: utf-8 -*-
"""Pruebas del contenido publicado.

Verifican que el Markdown generado corresponda a la especificación, cumpla el
estándar `clase-profunda-v2` y esté escrito en español.
"""

from __future__ import annotations

import os
import re

SECCIONES_CLASE = [
    "## 🚦 Antes de empezar",
    "## 🎯 Propósito",
    "## 📚 Resultados de aprendizaje",
    "## 🧭 Agenda sugerida",
    "## 🧩 Conceptos centrales",
    "## 🧠 Modelo mental",
    "## 📖 Desarrollo",
    "## 📚 Lectura comparada",
    "## 🧮 Ejemplo trabajado",
    "## 🔀 Comparación de caminos y límites",
    "## 🪜 El mismo tema según el rol",
    "## 🏢 Caso ejecutivo",
    "## 🧪 Práctica guiada",
    "## ⚠️ Errores frecuentes",
    "## ❓ Preguntas de comprobación",
    "## 🗝️ Respuestas orientadoras",
    "## 🇨🇱 Contexto chileno y cumplimiento",
    "## 📥 Entregable",
    "## ✅ Evaluación de la clase",
    "## 📗 Fuentes y verificación",
]

MARCADORES_INGLES = [" the ", " and ", " with ", " must ", " should ",
                     "Why this matters", "Learning outcomes", "Worked example"]


def leer(ruta):
    with open(ruta, encoding="utf-8") as fh:
        return fh.read()


def solo_prosa(texto):
    sin = re.sub(r"\*\*[^*\n]+\*\*", " ", texto)
    sin = re.sub(r"\*[^*\n]+\*", " ", sin)
    sin = re.sub(r"`[^`\n]+`", " ", sin)
    sin = re.sub(r"^sources:.*$", " ", sin, flags=re.M)
    return sin


def rutas_de_clase(raiz, partes):
    for parte in partes:
        base = os.path.join(raiz, "curriculum", parte["slug"])
        for f in sorted(os.listdir(base)):
            if f.startswith("class-") and f.endswith(".md"):
                yield parte, os.path.join(base, f)


def test_existen_336_clases_publicadas(raiz, partes):
    total = sum(1 for _p, _r in rutas_de_clase(raiz, partes))
    assert total == 336


def test_cada_clase_de_la_especificacion_esta_publicada(raiz, clases_por_parte, partes):
    for parte in partes:
        base = os.path.join(raiz, "curriculum", parte["slug"])
        for c in clases_por_parte[parte["num"]]:
            ruta = os.path.join(base, "class-{}-{}.md".format(c["n"], c["slug"]))
            assert os.path.isfile(ruta), "Falta {}".format(ruta)


def test_clases_tienen_todas_las_secciones(raiz, partes):
    for parte, ruta in rutas_de_clase(raiz, partes):
        texto = leer(ruta)
        for seccion in SECCIONES_CLASE:
            assert seccion in texto, "{}: falta {}".format(os.path.basename(ruta), seccion)


def test_clases_superan_el_minimo_de_palabras(raiz, partes):
    for parte, ruta in rutas_de_clase(raiz, partes):
        n = len(leer(ruta).split())
        assert n >= 2500, "{}: {} palabras".format(os.path.basename(ruta), n)


def test_clases_en_espanol(raiz, partes):
    for parte, ruta in rutas_de_clase(raiz, partes):
        prosa = solo_prosa(leer(ruta))
        for marcador in MARCADORES_INGLES:
            assert marcador not in prosa, "{}: texto en inglés «{}»".format(
                os.path.basename(ruta), marcador.strip())


def test_las_clases_empiezan_por_su_titulo(raiz, partes):
    """Ningún documento abre con una ficha de metadatos.

    El front matter YAML se retiró porque GitHub lo pinta como una tabla justo
    encima del título: ocupa el lugar donde el lector busca el contenido y no
    le dice nada. Lo primero de una clase es su título.
    """
    for _parte, ruta in rutas_de_clase(raiz, partes):
        texto = leer(ruta)
        assert not texto.startswith("---"), "{}: abre con front matter".format(
            os.path.basename(ruta))
        assert texto.startswith("# Clase "), os.path.basename(ruta)


def test_los_metadatos_de_clase_viven_en_el_indice(raiz, partes):
    """Lo que el front matter declaraba sigue disponible, en su sitio.

    Quitar la ficha del documento no puede significar perder el dato: vive en
    `curriculum/curriculum.json`, que es donde una máquina lo lee sin ensuciar
    lo que lee una persona.
    """
    import json

    with open(os.path.join(raiz, "curriculum", "curriculum.json"), encoding="utf-8") as fh:
        indice = json.load(fh)

    total = 0
    for parte in indice["partes"]:
        for c in parte["clases"]:
            total += 1
            assert c["idioma"] == "es"
            assert c["estandar"] == "clase-profunda-v2"
            assert c["umbral_aprobacion"] == 80
            assert c["minutos_estimados"] == 150
            assert c["libros"], "{}.{} sin obras".format(parte["num"], c["n"])
            assert set(c["anclajes"]) == set(c["libros"])
            assert os.path.isfile(os.path.join(raiz, c["ruta"].replace("/", os.sep)))
    assert total == 336


def test_conceptos_de_la_especificacion_aparecen_en_la_clase(raiz, clases_por_parte, partes):
    for parte in partes:
        base = os.path.join(raiz, "curriculum", parte["slug"])
        for c in clases_por_parte[parte["num"]]:
            texto = leer(os.path.join(base, "class-{}-{}.md".format(c["n"], c["slug"])))
            for termino, _definicion in c["conceptos"]:
                assert termino in texto, "{}.{}: falta el concepto «{}»".format(
                    parte["num"], c["n"], termino)


def test_senales_de_la_especificacion_aparecen_en_la_clase(raiz, clases_por_parte, partes):
    for parte in partes:
        base = os.path.join(raiz, "curriculum", parte["slug"])
        for c in clases_por_parte[parte["num"]]:
            texto = leer(os.path.join(base, "class-{}-{}.md".format(c["n"], c["slug"])))
            for nombre, _definicion in c["senales"]:
                assert nombre in texto, "{}.{}: falta la señal «{}»".format(
                    parte["num"], c["n"], nombre)


def test_indices_de_parte_existen(raiz, partes):
    for parte in partes:
        ruta = os.path.join(raiz, "curriculum", parte["slug"], "README.md")
        assert os.path.isfile(ruta)
        texto = leer(ruta)
        assert parte["titulo"] in texto
        assert parte["artefacto"] in texto


def test_hay_48_laboratorios_con_rubrica(raiz, partes):
    total = 0
    for parte in partes:
        base = os.path.join(raiz, "labs", "part-{}".format(parte["num"]))
        archivos = [f for f in os.listdir(base) if f.endswith(".md")]
        assert len(archivos) == 2, "Parte {}: {} laboratorios".format(parte["num"], len(archivos))
        total += len(archivos)
        for f in archivos:
            texto = leer(os.path.join(base, f))
            assert "## Rúbrica (100 puntos)" in texto
            assert "**Aprobación:** 80/100" in texto
    assert total == 48


def test_evaluaciones_tienen_cuatro_bloques(raiz, partes):
    for parte in partes:
        ruta = os.path.join(raiz, "assessments", "part-{}-assessment.md".format(parte["num"]))
        texto = leer(ruta)
        for bloque in ["## A. Precisión conceptual", "## B. Caso de decisión",
                       "## C. Método y evidencia", "## D. Fuentes, límites y red team"]:
            assert bloque in texto, "Parte {}: falta {}".format(parte["num"], bloque)


def test_hay_24_casos_y_12_proyectos(raiz):
    casos = [f for f in os.listdir(os.path.join(raiz, "cases")) if f.endswith(".md")]
    proyectos = [f for f in os.listdir(os.path.join(raiz, "projects")) if f.endswith(".md")]
    assert len(casos) == 24
    assert len(proyectos) == 12


def test_capstone_tiene_cumplimiento_eliminatorio(raiz):
    texto = leer(os.path.join(raiz, "capstone", "README.md"))
    assert "eliminatorio" in texto.lower()
    assert os.path.isfile(os.path.join(raiz, "capstone", "CHECKLIST.md"))


def test_documentacion_esperada_existe(raiz):
    esperados = ["README.md", "METODOLOGIA.md", "ESTANDAR-PEDAGOGICO.md", "ESTANDAR-DE-EVIDENCIA.md",
                 "EVALUACION-Y-RUBRICAS.md", "ARQUITECTURA-DEL-PROGRAMA.md", "RUTA-DE-APRENDIZAJE.md",
                 "GUIA-DOCENTE.md", "PLAN-DE-CAPACITACION.md", "RUTAS-PROFESIONALES.md",
                 "ACCESIBILIDAD.md", "PREGUNTAS-FRECUENTES.md", "MAPA-REGULATORIO-CHILE.md",
                 "FUENTES-OFICIALES.md", "DATOS-PERSONALES-Y-ETICA.md", "GLOSARIO.md",
                 "FORMULAS-Y-METRICAS.md", "BIBLIOGRAFIA.md", "MAPA-DEL-CURRICULO.md",
                 "MAPA-DE-COMPETENCIAS.md"]
    for nombre in esperados:
        assert os.path.isfile(os.path.join(raiz, "docs", nombre)), "Falta docs/{}".format(nombre)


def test_glosario_cubre_los_conceptos(raiz, todas_las_clases):
    glosario = leer(os.path.join(raiz, "docs", "GLOSARIO.md"))
    muestra = [c["conceptos"][0][0] for _n, c in todas_las_clases[::17]]
    for termino in muestra:
        assert termino in glosario, "Glosario sin «{}»".format(termino)


def test_metricas_documentadas(raiz, todas_las_clases):
    doc = leer(os.path.join(raiz, "docs", "FORMULAS-Y-METRICAS.md"))
    muestra = [c["senales"][0][0] for _n, c in todas_las_clases[::23]]
    for nombre in muestra:
        assert nombre in doc, "Documento de métricas sin «{}»".format(nombre)
