# -*- coding: utf-8 -*-
"""Cobertura estructural de la ampliación A–N."""

from pathlib import Path

from spec.ampliaciones_integrales import AMPLIACIONES


ROOT = Path(__file__).resolve().parents[1]


def todas():
    return [a for ampliaciones in AMPLIACIONES.values() for a in ampliaciones]


def test_cubre_los_catorce_ejes_sin_clases_nuevas():
    assert {a["eje"] for a in todas()} == set("ABCDEFGHIJKLMN")
    assert len(AMPLIACIONES) == 14


def test_cada_ampliacion_es_aplicable_medible_y_transferible():
    for ampliacion in todas():
        assert len(ampliacion["teoria"]) >= 2
        assert len(ampliacion["marco"]) >= 4
        assert len(ampliacion["conceptos"]) >= 4
        assert ampliacion["actividad"]["solucion"]
        assert ampliacion["actividad"]["rubrica"]
        assert ampliacion["referencias"]
        assert ampliacion["transferencias"]
        for ficha in ampliacion["metricas"]:
            for campo in ("numerador", "denominador", "ventana", "fuente", "responsable", "lectura", "limite"):
                assert ficha[campo]


def test_cada_uso_de_ia_tiene_controles_y_alternativa():
    for ampliacion in todas():
        uso = ampliacion["ia"]
        for campo in ("objetivo", "datos", "prompt", "resultado", "validacion", "riesgos", "limites", "alternativa"):
            assert uso[campo]


def test_plantillas_y_proyecto_transversal_estan_completos():
    entrevista = (ROOT / "templates/market-research/interview-guide.md").read_text(encoding="utf-8")
    assert all(f"{n}." in entrevista for n in range(1, 11))
    persona = (ROOT / "templates/customer/buyer-persona-evidence.md").read_text(encoding="utf-8")
    for contexto in ("Consumidor final", "Pequeña empresa", "Comprador corporativo", "Comprador institucional"):
        assert contexto in persona
    proyecto = (ROOT / "docs/PROYECTO-TRANSVERSAL-RUTA-ANDINA.md").read_text(encoding="utf-8")
    filas = [linea for linea in proyecto.splitlines() if linea.startswith("| ") and linea.split("|")[1].strip().isdigit()]
    assert len(filas) == 30
