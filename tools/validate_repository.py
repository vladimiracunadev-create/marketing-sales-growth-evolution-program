# -*- coding: utf-8 -*-
"""Validador estructural del repositorio.

Verifica que el material publicado cumpla el estándar declarado en
`docs/ESTANDAR-PEDAGOGICO.md`. Devuelve código 1 si encuentra fallas.

Uso:
    python tools/validate_repository.py
    python tools/validate_repository.py --verboso
"""

from __future__ import annotations

import argparse
import importlib
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "curriculum"))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from spec import bibliografia as bib  # noqa: E402
from spec.partes import PARTES  # noqa: E402

# Estandar pedagogico vigente. Debe coincidir con el que declara el generador.
VERSION_ESTANDAR = "clase-profunda-v2"

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

PALABRAS_MINIMAS = 2500

# Términos en inglés que no deben aparecer como prosa. Se excluyen los que son
# nombre propio del dominio o título de obra citada.
ANGLICISMOS_PROHIBIDOS = [
    " the ", " and ", " with ", " must ", " should ", " learner ", " decision-ready ",
    " assumptions ", " evidence ladder ", " by the end", "Estimated study time",
    "Why this matters", "Learning outcomes", "Worked example", "Guided practice",
    "Knowledge check", "Common failure modes", "Transfer challenge",
]

ARCHIVOS_RAIZ = ["README.md", "SYLLABUS.md", "MANIFEST.md", "FILE_INDEX.md", "ROADMAP.md",
                 "CHANGELOG.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md",
                 "LICENSE", "VERSION"]

DOCS_ESPERADOS = ["README.md", "METODOLOGIA.md", "ESTANDAR-PEDAGOGICO.md", "ESTANDAR-DE-EVIDENCIA.md",
                  "EVALUACION-Y-RUBRICAS.md", "ARQUITECTURA-DEL-PROGRAMA.md", "RUTA-DE-APRENDIZAJE.md",
                  "GUIA-DOCENTE.md", "PLAN-DE-CAPACITACION.md", "RUTAS-PROFESIONALES.md",
                  "ACCESIBILIDAD.md", "PREGUNTAS-FRECUENTES.md", "MAPA-REGULATORIO-CHILE.md",
                  "FUENTES-OFICIALES.md", "DATOS-PERSONALES-Y-ETICA.md", "GLOSARIO.md",
                  "FORMULAS-Y-METRICAS.md", "BIBLIOGRAFIA.md", "MAPA-DEL-CURRICULO.md",
                  "MAPA-DE-COMPETENCIAS.md"]


class Reporte:
    def __init__(self):
        self.errores = []
        self.avisos = []
        self.comprobaciones = 0

    def error(self, mensaje):
        self.errores.append(mensaje)

    def aviso(self, mensaje):
        self.avisos.append(mensaje)

    def ok(self):
        self.comprobaciones += 1


def leer(ruta):
    with open(ruta, encoding="utf-8") as fh:
        return fh.read()


def _solo_prosa(texto):
    """Elimina títulos de obra en cursiva, código y metadatos antes de buscar
    anglicismos: las obras citadas conservan su título original en inglés."""
    # El énfasis fuerte se retira primero: si no, sus dos asteriscos se emparejan
    # con los de la cursiva siguiente y dejan el título en inglés al descubierto.
    sin = re.sub(r"\*\*[^*\n]+\*\*", " ", texto)
    sin = re.sub(r"\*[^*\n]+\*", " ", sin)
    sin = re.sub(r"`[^`\n]+`", " ", sin)
    sin = re.sub(r"^sources:.*$", " ", sin, flags=re.M)
    sin = re.sub(r"^---$.*?^---$", " ", sin, flags=re.M | re.S)
    return sin


def validar_estructura(rep):
    for nombre in ARCHIVOS_RAIZ:
        if os.path.isfile(os.path.join(RAIZ, nombre)):
            rep.ok()
        else:
            rep.error("Falta archivo de raíz: {}".format(nombre))

    for nombre in DOCS_ESPERADOS:
        if os.path.isfile(os.path.join(RAIZ, "docs", nombre)):
            rep.ok()
        else:
            rep.error("Falta documento: docs/{}".format(nombre))

    for carpeta in ["curriculum", "rutas", "labs", "assessments", "cases", "projects", "capstone",
                    "datasets", "notebooks", "templates", "simulations", "ai", "tools", "tests"]:
        if os.path.isdir(os.path.join(RAIZ, carpeta)):
            rep.ok()
        else:
            rep.error("Falta directorio: {}/".format(carpeta))


def validar_clases(rep, verboso=False):
    total = 0
    for parte in PARTES:
        destino = os.path.join(RAIZ, "curriculum", parte["slug"])
        if not os.path.isdir(destino):
            rep.error("Parte sin directorio: {}".format(parte["slug"]))
            continue
        if not os.path.isfile(os.path.join(destino, "README.md")):
            rep.error("Parte sin índice: {}/README.md".format(parte["slug"]))

        clases = sorted(f for f in os.listdir(destino) if f.startswith("class-") and f.endswith(".md"))
        if len(clases) != 14:
            rep.error("Parte {}: {} clases (se esperaban 14)".format(parte["num"], len(clases)))

        try:
            spec = importlib.import_module("spec.clases_p{}".format(parte["num"])).CLASES
        except ModuleNotFoundError:
            rep.error("Parte {}: sin especificación".format(parte["num"]))
            continue

        esperados = {"class-{}-{}.md".format(c["n"], c["slug"]) for c in spec}
        sobrantes = set(clases) - esperados
        for s in sobrantes:
            rep.error("Archivo huérfano (no está en la especificación): {}/{}".format(parte["slug"], s))

        for archivo in clases:
            total += 1
            ruta = os.path.join(destino, archivo)
            texto = leer(ruta)
            rel = "curriculum/{}/{}".format(parte["slug"], archivo)

            palabras = len(texto.split())
            if palabras < PALABRAS_MINIMAS:
                rep.error("{}: {} palabras (mínimo {})".format(rel, palabras, PALABRAS_MINIMAS))
            else:
                rep.ok()

            for seccion in SECCIONES_CLASE:
                if seccion in texto:
                    rep.ok()
                else:
                    rep.error("{}: falta la sección «{}»".format(rel, seccion))

            prosa = _solo_prosa(texto)
            for termino in ANGLICISMOS_PROHIBIDOS:
                if termino in prosa:
                    rep.error("{}: contiene texto en inglés «{}»".format(rel, termino.strip()))

    # Los metadatos de cada clase —idioma, estándar, umbral, obras citadas— ya
    # no viven en un front matter encima del título, donde GitHub los pintaba
    # como una tabla que no le decía nada al lector. Viven en el índice legible
    # por máquina, y es ahí donde se comprueban.
    ruta_indice = os.path.join(RAIZ, "curriculum", "curriculum.json")
    if not os.path.isfile(ruta_indice):
        rep.error("Falta curriculum/curriculum.json")
    else:
        with open(ruta_indice, encoding="utf-8") as fh:
            indice = json.load(fh)
        for parte in indice["partes"]:
            for c in parte["clases"]:
                ref = "{}.{}".format(parte["num"], c["n"])
                if c.get("idioma") != "es":
                    rep.error("{}: el índice no declara idioma español".format(ref))
                else:
                    rep.ok()
                if c.get("umbral_aprobacion") != 80:
                    rep.error("{}: el índice no declara umbral de aprobación".format(ref))
                else:
                    rep.ok()
                if c.get("estandar") != VERSION_ESTANDAR:
                    rep.error("{}: el índice no declara el estándar {}".format(
                        ref, VERSION_ESTANDAR))
                else:
                    rep.ok()
                for libro in c.get("libros", []):
                    if libro not in bib.LIBROS:
                        rep.error("{}: bibliografía inexistente «{}»".format(ref, libro))
                    else:
                        rep.ok()

    if verboso:
        print("Clases verificadas: {}".format(total))


def validar_practica(rep):
    labs = 0
    for parte in PARTES:
        dir_labs = os.path.join(RAIZ, "labs", "part-{}".format(parte["num"]))
        if not os.path.isdir(dir_labs):
            rep.error("Faltan laboratorios de la parte {}".format(parte["num"]))
            continue
        archivos = [f for f in os.listdir(dir_labs) if f.endswith(".md")]
        labs += len(archivos)
        if len(archivos) != 2:
            rep.error("Parte {}: {} laboratorios (se esperaban 2)".format(parte["num"], len(archivos)))
        for f in archivos:
            texto = leer(os.path.join(dir_labs, f))
            for seccion in ["## Escenario", "## Misión", "## Procedimiento", "## Entregables",
                            "## Rúbrica (100 puntos)"]:
                if seccion not in texto:
                    rep.error("labs/part-{}/{}: falta «{}»".format(parte["num"], f, seccion))
                else:
                    rep.ok()

        evaluacion = os.path.join(RAIZ, "assessments", "part-{}-assessment.md".format(parte["num"]))
        if not os.path.isfile(evaluacion):
            rep.error("Falta evaluación de la parte {}".format(parte["num"]))
        else:
            texto = leer(evaluacion)
            for bloque in ["## A. Precisión conceptual", "## B. Caso de decisión",
                           "## C. Método y evidencia", "## D. Fuentes, límites y red team"]:
                if bloque not in texto:
                    rep.error("assessments/part-{}: falta «{}»".format(parte["num"], bloque))
                else:
                    rep.ok()

    if labs != 48:
        rep.error("Total de laboratorios: {} (se esperaban 48)".format(labs))

    for carpeta, esperado in [("cases", 24), ("projects", 12)]:
        ruta = os.path.join(RAIZ, carpeta)
        n = len([f for f in os.listdir(ruta) if f.endswith(".md")]) if os.path.isdir(ruta) else 0
        if n != esperado:
            rep.error("{}/: {} archivos (se esperaban {})".format(carpeta, n, esperado))
        else:
            rep.ok()

    for archivo in ["capstone/README.md", "capstone/CHECKLIST.md"]:
        if os.path.isfile(os.path.join(RAIZ, archivo)):
            rep.ok()
        else:
            rep.error("Falta {}".format(archivo))


def validar_rutas(rep):
    """Cada rol declarado debe tener su página y sus enlaces deben resolver."""
    from spec.roles import ROLES

    base = os.path.join(RAIZ, "rutas")
    if not os.path.isdir(base):
        rep.error("Falta el directorio rutas/")
        return
    if not os.path.isfile(os.path.join(base, "README.md")):
        rep.error("Falta rutas/README.md")

    secciones = ["## 🧭 Qué es y por qué importa", "## 🗓️ Un día en el puesto",
                 "## 🧠 Qué necesitas saber", "## 📚 Tu ruta en el programa",
                 "## 📥 Artefactos que acreditan este rol",
                 "## 📈 Progresión de carrera y rangos",
                 "## ⚠️ Mitos y errores comunes", "## ⚖️ Nota de honestidad"]

    for rol in ROLES:
        ruta = os.path.join(base, "{}.md".format(rol["slug"]))
        if not os.path.isfile(ruta):
            rep.error("Falta la página de rol: rutas/{}.md".format(rol["slug"]))
            continue
        texto = leer(ruta)
        for seccion in secciones:
            if seccion in texto:
                rep.ok()
            else:
                rep.error("rutas/{}.md: falta «{}»".format(rol["slug"], seccion))
        if len(texto.split()) < 900:
            rep.error("rutas/{}.md: {} palabras (mínimo 900)".format(rol["slug"], len(texto.split())))
        else:
            rep.ok()


def validar_bibliografia(rep):
    for clave, valor in bib.LIBROS.items():
        if len(valor) != 5:
            rep.error("Bibliografía «{}»: estructura incorrecta".format(clave))
        elif not all(valor):
            rep.error("Bibliografía «{}»: campo vacío".format(clave))
        else:
            rep.ok()
    for clave in bib.NUCLEO_PEDAGOGICO:
        if clave not in bib.LIBROS:
            rep.error("Núcleo pedagógico referencia obra inexistente: {}".format(clave))
        else:
            rep.ok()


def main():
    ap = argparse.ArgumentParser(description="Valida la estructura del repositorio")
    ap.add_argument("--verboso", action="store_true")
    args = ap.parse_args()

    rep = Reporte()
    validar_estructura(rep)
    validar_clases(rep, args.verboso)
    validar_practica(rep)
    validar_rutas(rep)
    validar_bibliografia(rep)

    print("Comprobaciones superadas: {}".format(rep.comprobaciones))
    if rep.avisos:
        print("\nAvisos ({}):".format(len(rep.avisos)))
        for a in rep.avisos[:20]:
            print("  [!] {}".format(a))
    if rep.errores:
        print("\nErrores ({}):".format(len(rep.errores)))
        for e in rep.errores[:40]:
            print("  [X] {}".format(e))
        if len(rep.errores) > 40:
            print("  … y {} más".format(len(rep.errores) - 40))
        return 1

    print("\nRepositorio válido: estructura, profundidad, idioma y bibliografía conformes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
