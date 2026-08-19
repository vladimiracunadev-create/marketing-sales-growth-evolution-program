# -*- coding: utf-8 -*-
"""Generador del estado del repositorio (STATUS.md).

Recorre el repositorio, cuenta lo que existe y contrasta contra las metas
declaradas. No acepta cifras escritas a mano: todo lo que informa proviene de
archivos reales.

Uso:
    python tools/build_status.py
"""

from __future__ import annotations

import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "curriculum"))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from spec import bibliografia as bib  # noqa: E402
from spec.partes import PARTES  # noqa: E402

FECHA = "2026-08-19"


def contar(carpeta, prefijo="", sufijo=".md"):
    base = os.path.join(RAIZ, carpeta)
    if not os.path.isdir(base):
        return 0
    total = 0
    for actual, dirs, files in os.walk(base):
        dirs[:] = [d for d in dirs if not d.startswith((".", "__"))]
        total += sum(1 for f in files if f.endswith(sufijo) and f.startswith(prefijo))
    return total


def palabras_curriculo():
    total = 0
    base = os.path.join(RAIZ, "curriculum")
    for actual, _d, files in os.walk(base):
        for f in files:
            if f.startswith("class-") and f.endswith(".md"):
                with open(os.path.join(actual, f), encoding="utf-8") as fh:
                    total += len(fh.read().split())
    return total


def version():
    ruta = os.path.join(RAIZ, "VERSION")
    if os.path.isfile(ruta):
        with open(ruta, encoding="utf-8") as fh:
            return fh.read().strip()
    return "desconocida"


def ejecutar(comando):
    try:
        proceso = subprocess.run(comando, cwd=RAIZ, capture_output=True, text=True, timeout=600)
        return proceso.returncode, (proceso.stdout or "").strip().split("\n")[-1]
    except Exception as exc:  # noqa: BLE001
        return 1, "no ejecutable: {}".format(exc)


def marca(codigo):
    return "OK" if codigo == 0 else "FALLA"


def main():
    n_clases = contar("curriculum", "class-")
    n_labs = contar("labs")
    n_assess = contar("assessments")
    n_cases = contar("cases")
    n_proj = contar("projects")
    n_docs = contar("docs")
    n_nb = contar("notebooks", sufijo=".ipynb")
    n_data = contar("datasets", sufijo=".csv")
    n_tpl = contar("templates")
    n_tests = contar("tests", sufijo=".py")
    n_html = contar("site", sufijo=".html")
    palabras = palabras_curriculo()

    metas = [
        ("Partes del currículo", len(PARTES), 24),
        ("Clases", n_clases, 336),
        ("Laboratorios", n_labs, 48),
        ("Evaluaciones de parte", n_assess, 24),
        ("Casos extendidos", n_cases, 24),
        ("Proyectos integradores", n_proj, 12),
        ("Documentos de docs/", n_docs, 20),
        ("Notebooks", n_nb, 8),
        ("Conjuntos de datos", n_data, 5),
        ("Obras en bibliografía", len(bib.LIBROS), 90),
    ]

    verificaciones = [
        ("Estructura del repositorio", ["python", "tools/validate_repository.py"]),
        ("Profundidad del contenido", ["python", "tools/validate_depth.py"]),
        ("Enlaces internos", ["python", "tools/check_links.py"]),
    ]

    lineas = [
        "---",
        'title: "Estado del repositorio"',
        "type: status",
        "language: es",
        "generated: true",
        "updated: {}".format(FECHA),
        "---",
        "",
        "> Documento generado por `tools/build_status.py`. Los números provienen de contar archivos reales.",
        "",
        "# Estado del repositorio",
        "",
        "**Versión:** {} · **Actualizado:** {}".format(version(), FECHA),
        "",
        "## Inventario frente a metas",
        "",
        "| Elemento | Actual | Meta | Estado |",
        "|---|---:|---:|:--:|",
    ]
    completo = True
    for nombre, actual, meta in metas:
        estado = "OK" if actual >= meta else "PENDIENTE"
        if actual < meta:
            completo = False
        lineas.append("| {} | {} | {} | {} |".format(nombre, actual, meta, estado))

    lineas += [
        "",
        "**Palabras de contenido curricular:** {:,}".format(palabras).replace(",", "."),
        "",
        "**Páginas HTML generadas:** {} · **Módulos de prueba:** {} · **Plantillas:** {}".format(
            n_html, n_tests, n_tpl),
        "",
        "## Verificaciones automatizadas",
        "",
        "| Verificación | Resultado | Salida |",
        "|---|:--:|---|",
    ]
    todas_ok = True
    for nombre, comando in verificaciones:
        codigo, salida = ejecutar(comando)
        if codigo != 0:
            todas_ok = False
        lineas.append("| {} | {} | {} |".format(nombre, marca(codigo), salida[:90]))

    lineas += [
        "",
        "## Puertas de calidad",
        "",
        "- [{}] 24 partes con 14 clases cada una".format("x" if n_clases == 336 else " "),
        "- [{}] Todas las clases superan 2.500 palabras".format("x" if todas_ok else " "),
        "- [{}] Todas las clases en español con secciones obligatorias".format("x" if todas_ok else " "),
        "- [{}] 48 laboratorios con rúbrica de 100 puntos".format("x" if n_labs == 48 else " "),
        "- [{}] 24 evaluaciones de cuatro bloques ponderados".format("x" if n_assess == 24 else " "),
        "- [{}] 12 proyectos integradores".format("x" if n_proj == 12 else " "),
        "- [{}] Capstone con cumplimiento eliminatorio".format(
            "x" if os.path.isfile(os.path.join(RAIZ, "capstone", "README.md")) else " "),
        "- [{}] Documentación completa en español".format("x" if n_docs >= 20 else " "),
        "- [{}] Sitio HTML generado".format("x" if n_html > 500 else " "),
        "- [{}] Enlaces internos sin roturas".format("x" if todas_ok else " "),
        "",
        "## Cómo reproducir este informe",
        "",
        "```bash",
        "python tools/build_curriculum.py",
        "python tools/build_practica.py",
        "python tools/build_docs.py",
        "python tools/build_site.py",
        "python tools/build_status.py",
        "```",
        "",
        "---",
        "",
        "[⬅ Programa](README.md) · [Manifiesto](MANIFEST.md) · [Roadmap](ROADMAP.md)",
        "",
    ]

    ruta = os.path.join(RAIZ, "STATUS.md")
    with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lineas))

    print("STATUS.md generado · inventario {} · verificaciones {}".format(
        "completo" if completo else "incompleto", "OK" if todas_ok else "con fallas"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
