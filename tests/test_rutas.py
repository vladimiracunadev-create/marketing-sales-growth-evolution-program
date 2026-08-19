# -*- coding: utf-8 -*-
"""Pruebas de las rutas profesionales por rol."""

from __future__ import annotations

import os
import re

SECCIONES = [
    "## 🧭 Qué es y por qué importa",
    "## 🗓️ Un día en el puesto",
    "## 🧠 Qué necesitas saber",
    "## 📚 Tu ruta en el programa",
    "## 🧪 Práctica y evaluación",
    "## 📥 Artefactos que acreditan este rol",
    "## 🎓 Credenciales y señales de mercado",
    "## 📈 Progresión de carrera y rangos",
    "## ⚠️ Mitos y errores comunes",
    "## ⚖️ Nota de honestidad",
]


def leer(ruta):
    with open(ruta, encoding="utf-8") as fh:
        return fh.read()


def roles():
    from spec.roles import ROLES
    return ROLES


def test_hay_17_roles():
    assert len(roles()) == 17


def test_roles_tienen_campos_obligatorios():
    obligatorios = {"slug", "emoji", "titulo", "familia", "resumen", "nivel", "foco", "credencial",
                    "que_es", "dia", "tecnico", "herramientas", "blandas", "ruta", "clases",
                    "labs", "artefactos", "credenciales", "progresion", "salario", "mitos", "honestidad"}
    for rol in roles():
        faltantes = obligatorios - set(rol)
        assert not faltantes, "Rol {} sin campos: {}".format(rol.get("slug"), faltantes)


def test_slugs_unicos_y_validos():
    slugs = [r["slug"] for r in roles()]
    assert len(slugs) == len(set(slugs))
    patron = re.compile(r"^[a-z0-9-]+$")
    for s in slugs:
        assert patron.match(s), "Slug inválido: {}".format(s)


def test_familias_declaradas():
    from spec.roles import FAMILIAS
    for rol in roles():
        assert rol["familia"] in FAMILIAS, "Familia desconocida en {}".format(rol["slug"])


def test_rutas_referencian_partes_existentes(partes):
    numeros = {p["num"] for p in partes}
    for rol in roles():
        assert len(rol["ruta"]) >= 4, "Ruta corta en {}".format(rol["slug"])
        for num, por_que in rol["ruta"]:
            assert num in numeros, "Parte inexistente {} en {}".format(num, rol["slug"])
            assert len(por_que.split()) >= 5, "Justificación vaga en {}".format(rol["slug"])
        for num in rol["labs"]:
            assert num in numeros, "Lab de parte inexistente {} en {}".format(num, rol["slug"])


def test_clases_referenciadas_existen(clases_por_parte):
    for rol in roles():
        assert len(rol["clases"]) >= 6, "Pocas clases clave en {}".format(rol["slug"])
        for num_parte, n, por_que in rol["clases"]:
            assert num_parte in clases_por_parte, "Parte inexistente en {}".format(rol["slug"])
            ns = [c["n"] for c in clases_por_parte[num_parte]]
            assert n in ns, "Clase {}.{} inexistente en {}".format(num_parte, n, rol["slug"])
            assert len(por_que.split()) >= 4, "Motivo vago en {}".format(rol["slug"])


def test_contenido_sustantivo_por_rol():
    for rol in roles():
        assert len(rol["que_es"]) >= 3, "Descripción corta en {}".format(rol["slug"])
        for parrafo in rol["que_es"]:
            assert len(parrafo.split()) >= 30, "Párrafo corto en {}".format(rol["slug"])
        assert len(rol["dia"]) >= 5, "Día a día incompleto en {}".format(rol["slug"])
        assert len(rol["tecnico"]) >= 5, "Pocas competencias en {}".format(rol["slug"])
        assert len(rol["blandas"]) >= 4, "Pocas habilidades no técnicas en {}".format(rol["slug"])
        assert len(rol["artefactos"]) >= 3, "Pocos artefactos en {}".format(rol["slug"])
        assert len(rol["mitos"]) >= 3, "Pocos mitos en {}".format(rol["slug"])
        for mito, realidad in rol["mitos"]:
            assert len(realidad.split()) >= 8, "Refutación vaga en {}".format(rol["slug"])


def test_paginas_generadas_existen(raiz):
    base = os.path.join(raiz, "rutas")
    assert os.path.isfile(os.path.join(base, "README.md"))
    for rol in roles():
        ruta = os.path.join(base, "{}.md".format(rol["slug"]))
        assert os.path.isfile(ruta), "Falta rutas/{}.md".format(rol["slug"])


def test_paginas_tienen_todas_las_secciones(raiz):
    for rol in roles():
        texto = leer(os.path.join(raiz, "rutas", "{}.md".format(rol["slug"])))
        for seccion in SECCIONES:
            assert seccion in texto, "rutas/{}.md: falta {}".format(rol["slug"], seccion)


def test_paginas_tienen_profundidad(raiz):
    for rol in roles():
        texto = leer(os.path.join(raiz, "rutas", "{}.md".format(rol["slug"])))
        n = len(texto.split())
        assert n >= 900, "rutas/{}.md: {} palabras".format(rol["slug"], n)


def test_paginas_declaran_limite_del_programa(raiz):
    for rol in roles():
        texto = leer(os.path.join(raiz, "rutas", "{}.md".format(rol["slug"])))
        assert "no certifica ni garantiza empleo" in texto, \
            "rutas/{}.md sin la advertencia de alcance".format(rol["slug"])
        assert "orientativos" in texto, "rutas/{}.md sin advertencia sobre rangos".format(rol["slug"])


def test_indice_enlaza_todos_los_roles(raiz):
    indice = leer(os.path.join(raiz, "rutas", "README.md"))
    for rol in roles():
        assert "{}.md".format(rol["slug"]) in indice, "El índice no enlaza {}".format(rol["slug"])


def test_readme_principal_enlaza_las_rutas(raiz):
    readme = leer(os.path.join(raiz, "README.md"))
    assert "rutas/README.md" in readme
    for rol in roles():
        assert "rutas/{}.md".format(rol["slug"]) in readme, \
            "El README no enlaza la ruta {}".format(rol["slug"])
