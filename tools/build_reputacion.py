# -*- coding: utf-8 -*-
"""Generador de la especialización «Reputación, relaciones públicas y comunicación de crisis».

Lee `curriculum/spec/reputacion.py` y `curriculum/spec/reputacion_clases.py` y escribe en
`curriculum/specializations/reputacion-relaciones-publicas-y-crisis/`:

* `README.md`                   portada, rutas por rol, niveles de dominio y mapa de la especialización
* `clase-NN-*.md`               diez clases con el estándar `clase-profunda-v2`
* `labs/lab-NN-*.md`            laboratorios
* `scenarios/scenario-NN-*.md`  escenarios de crisis con decisiones alternativas

La especialización no altera la grilla de 24 partes × 14 clases: se cursa como ruta
transversal y se apoya en las ampliaciones O–U de las clases anfitrionas.

Uso:
    python tools/build_reputacion.py
"""

from __future__ import annotations

import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "curriculum"))
sys.path.insert(0, os.path.join(RAIZ, "tools"))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from spec import normas  # noqa: E402
from spec.aportes import APORTES  # noqa: E402
from spec.localizadores import acceso_legible  # noqa: E402
from spec.reputacion import (ESPECIALIZACION, LABS, NIVELES, ROLES_RUTA, SCENARIOS)  # noqa: E402
from spec.reputacion_clases import CLASES  # noqa: E402
from spec.reputacion_extras import CIERRES, LAB_EXTRAS  # noqa: E402
from build_curriculum import cita_localizada  # noqa: E402
import modelos_svg  # noqa: E402

SALIDA = os.path.join(RAIZ, "curriculum", "specializations", ESPECIALIZACION["slug"])
FECHA = "2026-11-25"
RE_NORMA = re.compile(r"\{n:([a-z0-9-]+)\}")


def N(texto):
    """Sustituye {n:clave} por la norma enlazada a su texto oficial."""
    return RE_NORMA.sub(lambda m: normas.enlace(m.group(1)), texto)


def escribir(ruta, contenido):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(contenido.rstrip("\n") + "\n")


def nombre_clase(c):
    return "clase-{}-{}.md".format(c["n"], c["slug"])


def nombre_lab(l):
    return "lab-{}-{}.md".format(l["n"], l["slug"])


def nombre_escenario(s):
    return "scenario-{}-{}.md".format(s["n"], s["slug"])


def navegacion(items, i, prefijo, nombre, retorno):
    ant = items[i - 1] if i > 0 else None
    sig = items[i + 1] if i < len(items) - 1 else None
    partes = [("[⬅ Anterior]({})".format(prefijo + nombre(ant))) if ant else "",
              "[Especialización]({})".format(retorno),
              ("[Siguiente ➡]({})".format(prefijo + nombre(sig))) if sig else ""]
    return " · ".join(p for p in partes if p)


def tabla(cabeceras, filas):
    lineas = ["| " + " | ".join(cabeceras) + " |", "|" + "---|" * len(cabeceras)]
    for f in filas:
        lineas.append("| " + " | ".join(N(str(x)) for x in f) + " |")
    return lineas


def render_clase(i):
    c = CLASES[i]
    lab = next(l for l in LABS if l["n"] == c["lab"])
    L = ["# Clase {} — {}".format(c["n"], c["titulo"]), "",
         "Clase {} de {} de la especialización [{}](README.md). Nivel de dominio: **{}**. Dura unos 150 minutos "
         "más el laboratorio asociado. Se cursa después de las partes 06 y 12 del currículo y puede leerse antes "
         "de la ampliación de la clase anfitriona {}.".format(
             int(c["n"]), len(CLASES), ESPECIALIZACION["titulo"], c["nivel"], c["anfitriona"]), "",
         navegacion(CLASES, i, "", nombre_clase, "README.md"), "",
         "## 🎯 Propósito", "", N(c["tesis"]), "",
         "## 🧭 Agenda sugerida (150 minutos)", "",
         "- **0–20 min.** Lee las definiciones y los siete conceptos; comprueba que puedes explicar cada uno con un ejemplo propio.",
         "- **20–60 min.** Estudia los fundamentos y las distinciones: anota qué afirmación de la clase cambiaría una decisión en tu organización.",
         "- **60–90 min.** Sigue el método paso a paso sobre el ejemplo resuelto, sin mirar la resolución, y compara.",
         "- **90–120 min.** Resuelve los tres casos progresivos y justifica cada decisión con la matriz.",
         "- **120–150 min.** Responde las preguntas de comprobación sin volver al texto y empieza el laboratorio {}.".format(c["lab"]), "",
         "### Resultados de aprendizaje", ""]
    L += ["- {}.".format(r) for r in c["resultados"]]
    _svg, forma = modelos_svg.modelo_svg(c, "25", "ESP." + c["n"], "Especialización")
    L += ["", "## 🧠 Modelo mental", "",
          "[![Modelo mental de la clase {}: {}](modelos/modelo-{}.svg)](modelos/modelo-{}.svg)".format(
              c["n"], c["titulo"], c["n"], c["n"]), "",
          "El diagrama se construye con el método y los conceptos de esta clase. Las insignias **↔ n** indican en "
          "qué pasos se usa el vocabulario de cada concepto. Descripción textual del método:", ""]
    L += ["{}. {}".format(k + 1, p[0].upper() + p[1:]) for k, p in enumerate(c["metodo"])]
    L += ["", "## 🔤 Definiciones", "",
          "**Definición simple.** {}".format(N(c["def_simple"])), "",
          "**Definición formal.** {}".format(N(c["def_formal"])), "",
          "## 🧩 Conceptos centrales", ""]
    L += tabla(["Concepto", "Definición operacional"], c["conceptos"])
    L += ["", "## 📖 Fundamentos", ""]
    for p in c["fundamentos"]:
        L += [N(p), ""]
    L += ["### Distinciones que evitan errores", ""]
    L += ["- **{}.** {}".format(a, N(b)) for a, b in c["distinciones"]]
    L += ["", "## 🛠️ Método paso a paso", ""]
    L += ["{}. {}.".format(k + 1, N(p)) for k, p in enumerate(c["metodo"])]
    L += ["", "## ⚖️ Matriz de decisión", "", c["matriz_intro"], ""]
    L += tabla(["Situación", "Decisión", "Condición que la sostiene", "Si falla"], c["matriz"])
    ej = c["ejemplo"]
    L += ["", "## 🧮 Ejemplo resuelto", "", "**Enunciado.** " + N(ej["enunciado"]), "", "**Resolución.**", ""]
    L += ["{}. {}".format(k + 1, N(p)) for k, p in enumerate(ej["pasos"])]
    L += ["", "**Resultado.** " + N(ej["resultado"]), "", "## 📈 Casos progresivos", ""]
    for k, (nivel, situacion, decision) in enumerate(c["casos"], 1):
        L += ["### Caso {} — nivel {}".format(k, nivel), "", "**Situación.** " + N(situacion), "",
              "**Decisión razonada.** " + N(decision), ""]
    L += ["## 🧯 Riesgos jurídicos, éticos, comerciales y reputacionales", ""]
    for etiqueta, texto in c["riesgos"]:
        L.append("- **{}.** {}".format(etiqueta, N(texto)))
    L += ["", "## 🔬 Laboratorio", "",
          "El laboratorio asociado es [{}](labs/{}). Entrega: {}.".format(lab["titulo"], nombre_lab(lab), lab["entregable"]),
          "", "## ✍️ Ejercicios", ""]
    L += ["{}. {}".format(k + 1, N(e)) for k, e in enumerate(c["ejercicios"])]
    L += ["", "## ⚠️ Errores habituales", ""]
    for err, correccion in c["errores"]:
        L.append("- **{}.** {}".format(err, N(correccion)))
    L += ["", "## ✅ Evaluación", "", "**Rúbrica.**", ""]
    L += tabla(["Criterio", "Peso", "Evidencia de logro"], c["rubrica"])
    L += ["", "**Preguntas de comprobación.**", ""]
    L += ["{}. {}".format(k + 1, N(q)) for k, q in enumerate(c["preguntas"])]
    if c.get("normas"):
        L += ["", "## 🇨🇱 Contexto chileno", "",
              "La norma manda sobre el material pedagógico. Antes de aplicar cualquier recomendación en una "
              "operación real, contrasta su texto vigente:", ""]
        L += ["- {}: {}.".format(normas.cita(k), normas.NORMAS[k]["materia"]) for k in c["normas"]]
    L += ["", "## 🧭 Síntesis y puente con otras clases", "", CIERRES[c["n"]]]
    L += ["", "## 📗 Referencias verificables", ""]
    for clave, ident in c["refs"]:
        idea, donde = APORTES[clave][ident]
        L.append("- {} — **aporta a esta clase:** {}. **Dónde buscarlo:** {}. **Acceso:** {}.".format(
            cita_localizada(clave), idea, donde, acceso_legible(clave)))
    L += ["", "> Las obras se citan, no se reproducen. Si la idea no está donde se indica, corresponde reportarlo "
          "como error del material. No se citan números de página porque cambian entre ediciones.", "",
          navegacion(CLASES, i, "", nombre_clase, "README.md")]
    return "\n".join(L)


def render_lab(i):
    lab = LABS[i]
    ex = LAB_EXTRAS[lab["n"]]
    L = ["# Laboratorio {} — {}".format(lab["n"], lab["titulo"]), "",
         navegacion(LABS, i, "", nombre_lab, "../README.md"), "",
         "## 🎯 Objetivo", "", N(lab["objetivo"]), "", "## 📌 Contexto", "", ex["contexto"], "",
         "## 🧰 Insumos", ""]
    L += ["- {}".format(N(x)) for x in lab["insumos"]]
    L += ["", "## 🪜 Procedimiento", ""]
    L += ["{}. {}".format(k + 1, N(p)) for k, p in enumerate(lab["pasos"])]
    L += ["", "## 🗂️ Datos de práctica", "", ex["datos"], "",
          "## 📥 Entregable", "", N(lab["entregable"]) + ".", "",
          "## 📏 Criterios de calidad", ""]
    L += ["- {}".format(N(x)) for x in lab["criterios"]]
    L += ["", "### Lectura por niveles de logro", ""]
    L += tabla(["Criterio", "Logrado", "Por mejorar"],
               [(x.rstrip("."), "se cumple y deja evidencia en el entregable", "se declara sin evidencia o no aparece") for x in lab["criterios"]])
    L += ["", "## ⏱️ Agenda de trabajo", "",
          "Reserva unos 120 minutos: 15 para leer el contexto y los datos, 60 para el procedimiento, 25 para redactar el entregable y 20 para contrastarlo con la solución orientadora y registrar qué corregirías.", ""]
    L += ["", "## 🗝️ Solución orientadora", "", N(lab["solucion"]), "",
          "## ⚠️ Errores habituales", ""] + ["- {}".format(x) for x in ex["errores"]] + ["", "## ➕ Extensión", "", ex["extension"], "",
          "## 🔗 Clases que lo sostienen", "",
          ", ".join("[{}](../{})".format("Clase " + c["n"], nombre_clase(c)) for c in CLASES if c["lab"] == lab["n"]) + ".", ""]
    return "\n".join(L)


def render_escenario(i):
    s = SCENARIOS[i]
    L = ["# Escenario {} — {}".format(s["n"], s["titulo"]), "",
         navegacion(SCENARIOS, i, "", nombre_escenario, "../README.md"), "",
         "**Tipo de crisis:** {}. **Caso base:** Ruta Andina SpA (datos sintéticos). **Duración de la simulación:** "
         "{}.".format(s["tipo"], s["duracion"]), "",
         "## 📌 Contexto y hechos", "", N(s["contexto"]), "", "### Hechos confirmados", ""]
    L += ["- {}".format(N(h)) for h in s["confirmados"]]
    L += ["", "### Aún no se sabe", ""]
    L += ["- {}".format(N(h)) for h in s["inciertos"]]
    L += ["", "## 🔀 Decisiones alternativas", ""]
    for k, d in enumerate(s["decisiones"], 1):
        L += ["### Decisión {} — {}".format(k, d["titulo"]), "", N(d["situacion"]), ""]
        L += tabla(["Opción", "Qué se hace", "Consecuencia probable"], d["opciones"])
        L += ["", "**Mejor decisión.** {}".format(N(d["mejor"])), ""]
    L += ["## 📣 Declaración modelo", "", "> " + N(s["declaracion"]), "",
          "## 📊 Indicadores de cierre", ""]
    L += ["- {}".format(N(x)) for x in s["indicadores"]]
    L += ["", "## ⚖️ Riesgos del escenario", ""]
    L += ["- **{}.** {}".format(a, N(b)) for a, b in s["riesgos"]]
    L += ["", "## 🧪 Variantes para repetir la simulación", ""]
    L += ["- {}".format(N(x)) for x in s["variantes"]]
    L += ["", "## 🧠 Aprendizaje esperado", "", N(s["aprendizaje"]), ""]
    return "\n".join(L)


def render_readme():
    e = ESPECIALIZACION
    L = ["# {}".format(e["titulo"]), "",
         "> {}".format(e["lema"]), "",
         "[⬅ Currículo](../../README.md) · [Mapa de competencias](../../../docs/MATRIZ-COMPETENCIAS-REPUTACION.md) · "
         "[Auditoría de la ampliación](../../../docs/AUDITORIA-AMPLIACION-REPUTACION.md)", "",
         "## 🎯 Para qué existe", ""]
    for p in e["proposito"]:
        L += [N(p), ""]
    L += ["## 🗺️ Lugar en el programa", "",
          "La especialización **no agrega una parte 25 ni cambia la grilla de 24 partes × 14 clases**. Es una ruta "
          "transversal con diez clases propias, seis laboratorios y ocho escenarios de crisis. Se articula con siete "
          "ampliaciones (ejes O–U) incorporadas a clases existentes, de modo que quien sólo cursa la parte 06 recibe "
          "lo imprescindible y quien necesita la competencia completa dispone de la ruta.", "",
          "| Clase anfitriona | Eje | Qué amplía |", "|---|---|---|"]
    L += ["| {} | {} | {} |".format(*f) for f in e["anfitrionas"]]
    L += ["", "## 📚 Clases", ""]
    L += tabla(["N.º", "Clase", "Nivel", "Pregunta que responde"],
               [("[{}]({})".format(c["n"], nombre_clase(c)), "[{}]({})".format(c["titulo"], nombre_clase(c)),
                 c["nivel"], c["pregunta"]) for c in CLASES])
    L += ["", "## 🔬 Laboratorios", ""]
    L += ["- [Laboratorio {} — {}](labs/{}): {}".format(l["n"], l["titulo"], nombre_lab(l), l["entregable"]) for l in LABS]
    L += ["", "## 🚨 Escenarios de crisis", "",
          "Cada escenario presenta hechos confirmados e inciertos, tres decisiones con alternativas defendibles y su "
          "consecuencia, una declaración modelo, indicadores de cierre y variantes para repetir.", ""]
    L += tabla(["N.º", "Escenario", "Tipo"],
               [(s["n"], "[{}](scenarios/{})".format(s["titulo"], nombre_escenario(s)), s["tipo"]) for s in SCENARIOS])
    L += ["", "## 📦 Entregables de la especialización", ""]
    L += tabla(["Entregable", "Ubicación"], e["entregables"])
    L += ["", "## 🧭 Rutas por rol", ""]
    L += tabla(["Rol", "Secuencia recomendada", "Entregable que lo acredita"], ROLES_RUTA)
    L += ["", "## 🪜 Niveles de dominio", ""]
    L += tabla(["Nivel", "Qué demuestra", "Evidencia mínima"], NIVELES)
    L += ["", "## ⚠️ Límites de esta especialización", ""]
    L += ["- {}".format(N(x)) for x in e["limites"]]
    L += [""]
    return "\n".join(L)


def main():
    for c in CLASES:
        assert c["lab"] in {l["n"] for l in LABS}, c["n"]
    for i, c in enumerate(CLASES):
        escribir(os.path.join(SALIDA, nombre_clase(c)), render_clase(i))
        svg, _forma = modelos_svg.modelo_svg(c, "25", "ESP." + c["n"], "Especialización")
        escribir(os.path.join(SALIDA, "modelos", "modelo-{}.svg".format(c["n"])), svg)
    for i, l in enumerate(LABS):
        escribir(os.path.join(SALIDA, "labs", nombre_lab(l)), render_lab(i))
    for i, s in enumerate(SCENARIOS):
        escribir(os.path.join(SALIDA, "scenarios", nombre_escenario(s)), render_escenario(i))
    escribir(os.path.join(SALIDA, "README.md"), render_readme())
    print("Especialización escrita: {} clases, {} laboratorios, {} escenarios".format(
        len(CLASES), len(LABS), len(SCENARIOS)))


if __name__ == "__main__":
    main()
