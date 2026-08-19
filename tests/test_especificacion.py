# -*- coding: utf-8 -*-
"""Pruebas de la especificación fuente del currículo.

Verifican que `curriculum/spec/` cumpla el estándar antes de generar nada:
si la especificación es incorrecta, el contenido publicado también lo será.
"""

from __future__ import annotations

import re


def test_hay_24_partes(partes):
    assert len(partes) == 24


def test_partes_tienen_campos_obligatorios(partes):
    obligatorios = {"num", "slug", "titulo", "nivel", "resultado", "pregunta",
                    "artefacto", "competencias", "roles", "libros", "caso", "riesgo"}
    for parte in partes:
        faltantes = obligatorios - set(parte)
        assert not faltantes, "Parte {} sin campos: {}".format(parte.get("num"), faltantes)


def test_numeros_de_parte_son_correlativos(partes):
    numeros = [p["num"] for p in partes]
    assert numeros == ["{:02d}".format(i) for i in range(1, 25)]


def test_slugs_de_parte_son_unicos(partes):
    slugs = [p["slug"] for p in partes]
    assert len(slugs) == len(set(slugs))


def test_cada_parte_tiene_14_clases(clases_por_parte):
    for num, clases in clases_por_parte.items():
        assert len(clases) == 14, "Parte {}: {} clases".format(num, len(clases))


def test_total_de_clases(todas_las_clases):
    assert len(todas_las_clases) == 336


def test_clases_tienen_campos_obligatorios(todas_las_clases):
    obligatorios = {"n", "slug", "titulo", "tesis", "conceptos", "metodo",
                    "senales", "caso", "limite", "libros", "error"}
    for num, c in todas_las_clases:
        faltantes = obligatorios - set(c)
        assert not faltantes, "Clase {}.{} sin campos: {}".format(num, c.get("n"), faltantes)


def test_numeracion_de_clases(clases_por_parte):
    for num, clases in clases_por_parte.items():
        assert [c["n"] for c in clases] == ["{:02d}".format(i) for i in range(1, 15)]


def test_slugs_de_clase_unicos_por_parte(clases_por_parte):
    for num, clases in clases_por_parte.items():
        slugs = [c["slug"] for c in clases]
        assert len(slugs) == len(set(slugs)), "Parte {} con slugs repetidos".format(num)


def test_slugs_sin_caracteres_invalidos(todas_las_clases):
    patron = re.compile(r"^[a-z0-9-]+$")
    for num, c in todas_las_clases:
        assert patron.match(c["slug"]), "Slug inválido en {}.{}: {}".format(num, c["n"], c["slug"])


def test_tesis_tiene_sustancia(todas_las_clases):
    """La tesis debe desarrollar un argumento, no enunciar un titular.

    El criterio no es la extensión sino la estructura: una tesis argumenta cuando
    encadena al menos tres oraciones —afirmación, mecanismo y consecuencia—.
    """
    for num, c in todas_las_clases:
        tesis = c["tesis"]
        n = len(tesis.split())
        assert n >= 40, "Tesis corta en {}.{}: {} palabras".format(num, c["n"], n)
        oraciones = [o for o in re.split(r"[.:;]\s", tesis) if len(o.split()) >= 5]
        assert len(oraciones) >= 3, \
            "Tesis sin desarrollo argumental en {}.{}: {} oraciones".format(num, c["n"], len(oraciones))


def test_conceptos_minimos_con_definicion(todas_las_clases):
    """Un concepto entra sólo con definición operacional, no con etiqueta."""
    for num, c in todas_las_clases:
        assert len(c["conceptos"]) >= 4, "Pocos conceptos en {}.{}".format(num, c["n"])
        for termino, definicion in c["conceptos"]:
            assert termino.strip(), "Concepto vacío en {}.{}".format(num, c["n"])
            assert definicion == definicion.strip(), \
                "Definición con espacios sobrantes en {}.{}".format(num, c["n"])
            assert len(definicion.split()) >= 5, \
                "Definición insuficiente de «{}» en {}.{}".format(termino, num, c["n"])
            assert termino.lower() not in definicion.lower().split()[:2], \
                "Definición circular de «{}» en {}.{}".format(termino, num, c["n"])


def test_metodo_tiene_cinco_pasos(todas_las_clases):
    for num, c in todas_las_clases:
        assert len(c["metodo"]) >= 5, "Método corto en {}.{}".format(num, c["n"])
        for paso in c["metodo"]:
            assert len(paso.split()) >= 3, "Paso vago en {}.{}: {}".format(num, c["n"], paso)


def test_senales_son_operacionales(todas_las_clases):
    """Una señal es operacional si nombra su base de cálculo o su ventana."""
    marcadores = ("sobre", "dividido", "entre", "por ", "en ", "durante", "al ", "menos",
                  "desde", "hasta", "cada", "%", "frente", "comparad", "respecto", "probabilidad", "mediana")
    for num, c in todas_las_clases:
        assert len(c["senales"]) >= 3, "Pocas señales en {}.{}".format(num, c["n"])
        for nombre, definicion in c["senales"]:
            assert nombre.strip(), "Señal sin nombre en {}.{}".format(num, c["n"])
            assert len(definicion.split()) >= 5, \
                "Señal «{}» demasiado breve en {}.{}".format(nombre, num, c["n"])
            assert any(m in definicion for m in marcadores), \
                "Señal «{}» sin base de cálculo ni ventana en {}.{}".format(nombre, num, c["n"])


def test_caso_es_concreto(todas_las_clases):
    for num, c in todas_las_clases:
        n = len(c["caso"].split())
        assert n >= 17, "Caso corto en {}.{}: {} palabras".format(num, c["n"], n)


def test_limite_es_explicito(todas_las_clases):
    for num, c in todas_las_clases:
        n = len(c["limite"].split())
        assert n >= 15, "Frontera de aplicación insuficiente en {}.{}".format(num, c["n"])


def test_error_tiene_sintoma_y_correccion(todas_las_clases):
    for num, c in todas_las_clases:
        assert len(c["error"]) == 2, "Error mal formado en {}.{}".format(num, c["n"])
        sintoma, correccion = c["error"]
        assert len(sintoma.split()) >= 4, "Síntoma vago en {}.{}".format(num, c["n"])
        assert len(correccion.split()) >= 6, "Corrección vaga en {}.{}".format(num, c["n"])


def test_bibliografia_de_clase_existe(todas_las_clases, libros):
    for num, c in todas_las_clases:
        assert 2 <= len(c["libros"]) <= 5, "Bibliografía fuera de rango en {}.{}".format(num, c["n"])
        for clave in c["libros"]:
            assert clave in libros, "Obra inexistente «{}» en {}.{}".format(clave, num, c["n"])


def test_bibliografia_de_parte_existe(partes, libros):
    for parte in partes:
        for clave in parte["libros"]:
            assert clave in libros, "Obra inexistente «{}» en parte {}".format(clave, parte["num"])


def test_bibliografia_bien_formada(libros):
    for clave, valor in libros.items():
        assert len(valor) == 5, "Estructura incorrecta en «{}»".format(clave)
        autor, obra, edicion, lente, categoria = valor
        assert autor and obra and edicion and lente and categoria, "Campo vacío en «{}»".format(clave)
        assert len(lente.split()) >= 5, "Lente insuficiente en «{}»".format(clave)


def test_toda_obra_se_usa_al_menos_una_vez(todas_las_clases, partes, libros):
    from spec.bibliografia import NUCLEO_PEDAGOGICO
    usadas = set(NUCLEO_PEDAGOGICO)
    for _num, c in todas_las_clases:
        usadas.update(c["libros"])
    for parte in partes:
        usadas.update(parte["libros"])
    sin_uso = set(libros) - usadas
    assert not sin_uso, "Obras citadas sin uso: {}".format(sorted(sin_uso))
