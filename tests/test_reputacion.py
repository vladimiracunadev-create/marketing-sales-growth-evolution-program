# -*- coding: utf-8 -*-
"""Cobertura y coherencia de la especialización de reputación, relaciones públicas y crisis."""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from spec import bibliografia, normas  # noqa: E402
from spec.ampliaciones_reputacion import AMPLIACIONES_REPUTACION  # noqa: E402
from spec.reputacion import ESPECIALIZACION, LABS, NIVELES, ROLES_RUTA, SCENARIOS  # noqa: E402
from spec.reputacion_clases import CLASES  # noqa: E402

SALIDA = ROOT / "curriculum" / "specializations" / ESPECIALIZACION["slug"]


def palabras(ruta):
    return len(Path(ruta).read_text(encoding="utf-8").split())


def test_cantidades_de_la_especializacion():
    assert len(CLASES) == 10
    assert len(LABS) == 6
    assert len(SCENARIOS) == 8
    assert len(ROLES_RUTA) == 8
    assert len(NIVELES) == 5


def test_la_grilla_del_curriculo_no_cambia():
    clases = [p for p in (ROOT / "curriculum").glob("part-*/class-*.md")]
    assert len(clases) == 336
    # las clases de la especialización no usan el prefijo `class-` de la grilla
    assert not list(SALIDA.glob("class-*.md"))


def test_cada_clase_cumple_el_estandar():
    for c in CLASES:
        archivo = SALIDA / "clase-{}-{}.md".format(c["n"], c["slug"])
        assert archivo.exists(), archivo
        assert palabras(archivo) >= 2500, archivo.name
        texto = archivo.read_text(encoding="utf-8")
        for seccion in ("## 🔤 Definiciones", "**Definición simple.**", "**Definición formal.**",
                        "## 🧮 Ejemplo resuelto", "## 📈 Casos progresivos", "## 🔬 Laboratorio",
                        "## ✍️ Ejercicios", "## ⚠️ Errores habituales", "## ✅ Evaluación",
                        "## 📗 Referencias verificables", "## 🧯 Riesgos jurídicos, éticos, comerciales y reputacionales"):
            assert seccion in texto, "{} sin «{}»".format(archivo.name, seccion)
        assert len(c["casos"]) == 3 and len(c["ejercicios"]) >= 5 and len(c["preguntas"]) >= 5
        assert {r[0] for r in c["riesgos"]} == {"Jurídico", "Ético", "Comercial", "Reputacional"}


def test_cada_obra_citada_existe_y_tiene_idea_anclada():
    from spec.aportes import APORTES
    for c in CLASES:
        for clave, ident in c["refs"]:
            assert clave in bibliografia.LIBROS, clave
            assert ident in APORTES[clave], (clave, ident)


def test_laboratorios_y_escenarios():
    for lab in LABS:
        archivo = SALIDA / "labs" / "lab-{}-{}.md".format(lab["n"], lab["slug"])
        assert palabras(archivo) >= 500, archivo.name
    for s in SCENARIOS:
        archivo = SALIDA / "scenarios" / "scenario-{}-{}.md".format(s["n"], s["slug"])
        assert palabras(archivo) >= 500, archivo.name
        assert len(s["decisiones"]) == 3
        for d in s["decisiones"]:
            assert len(d["opciones"]) >= 3 and d["mejor"]
        assert s["confirmados"] and s["inciertos"] and s["declaracion"]


def test_los_ocho_tipos_de_crisis_pedidos_estan_cubiertos():
    tipos = " ".join(s["titulo"].lower() + " " + s["tipo"].lower() for s in SCENARIOS)
    for clave in ("ejecutivo", "publicidad", "falla de producto", "reclamo", "digital", "filtraci",
                  "desinformaci", "empleado"):
        assert clave in tipos, clave


def test_las_siete_ampliaciones_existen_en_sus_clases():
    assert {a["eje"] for v in AMPLIACIONES_REPUTACION.values() for a in v} == set("OPQRSTU")
    for ref in AMPLIACIONES_REPUTACION:
        parte, n = ref.split(".")
        archivo = next((ROOT / "curriculum").glob("part-{}-*/class-{}-*.md".format(parte, n)))
        texto = archivo.read_text(encoding="utf-8")
        assert "### Eje " in texto and "Ampliación integral" in texto, archivo.name


def test_toda_norma_nombrada_enlaza_su_texto_oficial():
    for archivo in list(SALIDA.rglob("*.md")):
        texto = archivo.read_text(encoding="utf-8")
        for datos_clave, datos in normas.NORMAS.items():
            if datos["numero"] in texto:
                assert normas.url(datos_clave) in texto, (archivo.name, datos["numero"])


def test_entregables_existen_y_estan_enlazados():
    for nombre in ("plan-gestion-reputacional.md", "manual-marca-personal.md", "protocolo-comunicacion-crisis.md",
                   "guia-voceria.md", "plantillas-declaraciones.md", "matriz-partes-interesadas.csv",
                   "indicadores-reputacionales.csv"):
        assert (ROOT / "templates" / "reputation" / nombre).exists(), nombre
    readme = (SALIDA / "README.md").read_text(encoding="utf-8")
    for nombre in ("plan-gestion-reputacional", "manual-marca-personal", "protocolo-comunicacion-crisis",
                   "guia-voceria", "matriz-partes-interesadas", "plantillas-declaraciones",
                   "indicadores-reputacionales", "assessment.md", "MATRIZ-COMPETENCIAS-REPUTACION"):
        assert nombre in readme, nombre


def test_indicadores_declaran_ficha_completa():
    import csv
    filas = list(csv.DictReader((ROOT / "templates/reputation/indicadores-reputacionales.csv").open(encoding="utf-8")))
    assert len(filas) >= 10
    for f in filas:
        for campo in ("numerador", "denominador", "ventana", "fuente", "responsable", "lectura_permitida",
                      "limitacion", "umbral_de_accion"):
            assert f[campo].strip(), (f["indicador"], campo)


def test_el_generado_coincide_con_la_especificacion():
    import build_reputacion as b
    for i, c in enumerate(CLASES):
        esperado = b.render_clase(i).rstrip("\n") + "\n"
        real = (SALIDA / b.nombre_clase(c)).read_text(encoding="utf-8")
        assert real == esperado, "Regenerar con tools/build_reputacion.py: " + c["slug"]
    assert (SALIDA / "README.md").read_text(encoding="utf-8") == b.render_readme().rstrip("\n") + "\n"
    for i, s in enumerate(SCENARIOS):
        assert (SALIDA / "scenarios" / b.nombre_escenario(s)).read_text(encoding="utf-8") == \
            b.render_escenario(i).rstrip("\n") + "\n"


def test_no_hay_marcadores_pendientes():
    patron = re.compile(r"TODO|FIXME|lorem ipsum")
    for archivo in list(SALIDA.rglob("*.md")) + list((ROOT / "templates" / "reputation").glob("*")):
        assert not patron.search(archivo.read_text(encoding="utf-8")), archivo.name
