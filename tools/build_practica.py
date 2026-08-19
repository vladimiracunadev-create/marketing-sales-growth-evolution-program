# -*- coding: utf-8 -*-
"""Generador de la capa de práctica y evaluación.

Lee `curriculum/spec/` y escribe:

* `labs/part-XX/lab-XX-N-*.md`        48 laboratorios
* `assessments/part-XX-assessment.md` 24 evaluaciones con rúbrica ponderada
* `cases/case-XX-*.md`                24 casos extendidos
* `projects/project-NN-*.md`          12 proyectos acumulativos
* `capstone/README.md` y `CHECKLIST.md`

Sin dependencias externas.
"""

from __future__ import annotations

import importlib
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "curriculum"))

from spec import bibliografia as bib  # noqa: E402
from spec.partes import EMPRESA, PARTES  # noqa: E402

FECHA = "2026-08-19"


def escribir(ruta, contenido):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(contenido)


def clases(num):
    return importlib.import_module("spec.clases_p{}".format(num)).CLASES


def enum_es(items):
    items = list(items)
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + " y " + items[-1]


def minus(t):
    return t if t[:2].isupper() else t[0].lower() + t[1:]


def sin_punto(t):
    return t.rstrip(".")


# --------------------------------------------------------------------------
# laboratorios
# --------------------------------------------------------------------------

def render_lab(parte, cls, n_lab, anclas):
    num = parte["num"]
    principal, secundaria = anclas
    senales = principal["senales"] + secundaria["senales"]
    lineas = [
        "---",
        'title: "Lab {}.{} — {}"'.format(num, n_lab, principal["titulo"]),
        "type: lab",
        "language: es",
        "part: {}".format(num),
        "lab: {}".format(n_lab),
        "mastery_threshold: 80",
        "estimated_minutes: 240",
        "updated: {}".format(FECHA),
        "---",
        "",
        "# Lab {}.{} — {}".format(num, n_lab, principal["titulo"]),
        "",
        "**Parte {} · {}** · Duración estimada: 4 horas · Aprobación: 80/100",
        "",
        "## Escenario",
        "",
        "{} — {}".format(EMPRESA["nombre"], EMPRESA["descripcion"]),
        "",
        "**Situación específica del laboratorio.** {}".format(principal["caso"]),
        "",
        "**Restricciones vigentes.** {}".format(EMPRESA["restricciones"]),
        "",
        "## Misión",
        "",
        "Producir un componente defendible de **{}**, aplicando en particular {} y {}.".format(
            parte["artefacto"], "**" + minus(principal["titulo"]) + "**", "**" + minus(secundaria["titulo"]) + "**"),
        "",
        "> **Pregunta que debe quedar respondida:** {}".format(parte["pregunta"]),
        "",
        "## Insumos",
        "",
        "| Insumo | Ruta | Uso |",
        "|---|---|---|",
        "| Clases de la parte | [`curriculum/{}/`](../../curriculum/{}/) | Marco conceptual y método |".format(parte["slug"], parte["slug"]),
        "| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |",
        "| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |",
        "| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |",
        "| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |",
        "| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |",
        "",
        "## Procedimiento",
        "",
    ]
    pasos = list(principal["metodo"])
    lineas += ["{}. {}.".format(i + 1, p[0].upper() + p[1:]) for i, p in enumerate(pasos)]
    lineas += [
        "{}. Calcular o diseñar la captura de {}.".format(len(pasos) + 1, enum_es(["**{}**".format(s[0]) for s in senales[:3]])),
        "{}. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.".format(len(pasos) + 2),
        "{}. Verificar el riesgo declarado de la parte: {}".format(len(pasos) + 3, parte["riesgo"]),
        "{}. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.".format(len(pasos) + 4),
        "",
        "## Fichas de medición obligatorias",
        "",
        "| Señal | Definición operacional |",
        "|---|---|",
    ]
    vistas = set()
    for nombre, definicion in senales:
        if nombre in vistas:
            continue
        vistas.add(nombre)
        lineas.append("| **{}** | {} |".format(nombre, definicion))
    lineas += [
        "",
        "Cada ficha debe indicar además: fuente del dato, frecuencia de cálculo, responsable, lectura permitida "
        "y lectura prohibida. Si el dato no existe, se diseña el mecanismo de captura y se declara su costo.",
        "",
        "## Entregables",
        "",
        "1. `memo-decision.md` — problema, evidencia, dos alternativas, recomendación y gobierno.",
        "2. `calculo.md` o notebook — cálculos con supuestos explícitos y fuentes.",
        "3. `ficha-metricas.md` — definiciones operacionales completas.",
        "4. `escenario-adverso.md` — recálculo bajo la restricción indicada.",
        "5. `riesgo-y-cumplimiento.md` — verificación del riesgo de la parte y de la normativa aplicable.",
        "6. Resumen ejecutivo de una página para defensa de cinco minutos.",
        "",
        "## Rúbrica (100 puntos)",
        "",
        "| Criterio | Puntos | Qué se evalúa |",
        "|---|---:|---|",
        "| Encuadre del problema | 15 | La decisión está formulada antes que la herramienta. |",
        "| Calidad de la evidencia | 20 | Datos pertinentes con fuente, línea base y límites declarados. |",
        "| Aplicación del método | 15 | Ejecución completa de la secuencia con trazabilidad por paso. |",
        "| Medición | 20 | Fichas operacionales completas y cálculos verificables. |",
        "| Decisión y trade-offs | 15 | Dos alternativas reales, costo de oportunidad y condición de revisión. |",
        "| Riesgo y cumplimiento | 10 | Verificación del riesgo de la parte y de la normativa aplicable. |",
        "| Comunicación | 5 | Resumen ejecutivo comprensible por alguien ajeno al trabajo. |",
        "",
        "**Aprobación:** 80/100 y ningún criterio bajo el 60 % de su puntaje.",
        "",
        "## Errores que invalidan el laboratorio",
        "",
        "- {} {}".format(principal["error"][0] + ".", principal["error"][1]),
        "- {} {}".format(secundaria["error"][0] + ".", secundaria["error"][1]),
        "- Presentar métricas sin numerador, denominador y ventana.",
        "- Omitir el escenario adverso o presentarlo sin recálculo.",
        "- Usar datos personales sin verificar base de licitud y finalidad.",
        "",
        "## Fuentes de apoyo",
        "",
    ]
    for clave in principal["libros"][:3]:
        lineas.append("- {} — {}.".format(bib.cita(clave), bib.lente(clave)))
    lineas += [
        "",
        "---",
        "",
        "[⬅ Laboratorios de la parte {}](./) · [Clases](../../curriculum/{}/README.md) · "
        "[Evaluación](../../assessments/part-{}-assessment.md)".format(num, parte["slug"], num),
        "",
    ]
    texto = "\n".join(lineas)
    return texto.replace("**Parte {} · {}** · Duración estimada: 4 horas · Aprobación: 80/100",
                         "**Parte {} · {}** · Duración estimada: 4 horas · Aprobación: 80/100".format(
                             num, parte["titulo"]))


# --------------------------------------------------------------------------
# evaluaciones
# --------------------------------------------------------------------------

def render_assessment(parte, cls):
    num = parte["num"]
    conceptos = [c["conceptos"][0] for c in cls]
    lineas = [
        "---",
        'title: "Evaluación — Parte {}: {}"'.format(num, parte["titulo"]),
        "type: assessment",
        "language: es",
        "part: {}".format(num),
        "mastery_threshold: 80",
        "updated: {}".format(FECHA),
        "---",
        "",
        "# Evaluación — Parte {}: {}".format(num, parte["titulo"]),
        "",
        "Esta evaluación exige haber estudiado las 14 clases y haber ejecutado los dos laboratorios. Una "
        "respuesta genérica, que podría copiarse a otra parte sin cambios, se considera insuficiente.",
        "",
        "**Duración sugerida:** 120 minutos · **Aprobación:** 80/100 y ningún bloque bajo 60 %.",
        "",
        "## A. Precisión conceptual — 25 puntos",
        "",
    ]
    for i, (termino, definicion) in enumerate(conceptos[:5], start=1):
        lineas.append("{}. Define **{}** de forma operacional y da un hecho que lo confirme y otro que lo "
                      "refute. Definición de referencia: *{}*.".format(i, termino, sin_punto(definicion)))
    lineas += [
        "",
        "6. Elige dos conceptos de la parte que suelan confundirse. Construye un caso donde clasificar mal "
        "cambie la decisión comercial y explica el costo de ese error.",
        "",
        "## B. Caso de decisión — 30 puntos",
        "",
        "**Caso.** {}".format(parte["caso"]),
        "",
        "Construye dos alternativas realmente defendibles. Para cada una indica beneficio esperado, costo de "
        "oportunidad, riesgo, reversibilidad y quién asume la consecuencia. Recomienda una y declara qué "
        "información nueva te haría cambiar de opinión.",
        "",
        "## C. Método y evidencia — 30 puntos",
        "",
        "Aplica la secuencia de trabajo de la parte:",
        "",
    ]
    metodo_ref = cls[13]["metodo"]
    lineas += ["{}. {}.".format(i + 1, p[0].upper() + p[1:]) for i, p in enumerate(metodo_ref)]
    senal_ref = cls[13]["senales"]
    lineas += [
        "",
        "Debes operacionalizar {}. Separa hechos, inferencias y supuestos: una métrica sin línea base ni "
        "ventana no cuenta como evidencia suficiente.".format(
            enum_es(["**{}**".format(s[0]) for s in senal_ref])),
        "",
        "## D. Fuentes, límites y red team — 15 puntos",
        "",
        "Contrasta dos obras de la bibliografía rectora de la parte:",
        "",
    ]
    lineas += ["- {} — {}.".format(bib.cita(k), bib.lente(k)) for k in parte["libros"][:4]]
    lineas += [
        "",
        "Resume con tus palabras qué lente aporta cada una, identifica una tensión real entre ambas y explica "
        "cómo modifica tu recomendación. Después responde al límite de la parte:",
        "",
        "> **Riesgo declarado:** {}".format(parte["riesgo"]),
        "",
        "## Criterios de aprobación",
        "",
        "| Bloque | Peso | Evidencia esperada |",
        "|---|---:|---|",
        "| A. Precisión conceptual | 25 % | Distinciones observables, no definiciones memorizadas. |",
        "| B. Caso de decisión | 30 % | Dos opciones defendibles, trade-offs y condición de revisión. |",
        "| C. Método y evidencia | 30 % | Secuencia completa, métricas operacionalizadas y supuestos explícitos. |",
        "| D. Fuentes y límites | 15 % | Dos lecturas realmente usadas y tratamiento honesto del riesgo. |",
        "",
        "**Aprobación:** 80/100 y ningún bloque bajo el 60 % de su peso.",
        "",
        "## Guía para quien evalúa",
        "",
        "- Una respuesta correcta define, aplica y decide; definir sin aplicar es incompleto.",
        "- Verifica que las métricas incluyan numerador, denominador, ventana y fuente.",
        "- Penaliza las afirmaciones normativas o legales sin referencia a fuente oficial.",
        "- Valora explícitamente el reconocimiento de límites y de información faltante.",
        "",
        "---",
        "",
        "[⬅ Clases de la parte](../curriculum/{}/README.md) · [Laboratorios](../labs/part-{}/) · "
        "[Caso extendido](../cases/)".format(parte["slug"], num),
        "",
    ]
    return "\n".join(lineas)


# --------------------------------------------------------------------------
# casos extendidos
# --------------------------------------------------------------------------

def render_case(parte, cls):
    num = parte["num"]
    principal = cls[13]
    lineas = [
        "---",
        'title: "Caso {} — {}"'.format(num, parte["titulo"]),
        "type: case",
        "language: es",
        "part: {}".format(num),
        "updated: {}".format(FECHA),
        "---",
        "",
        "# Caso {} — {}".format(num, parte["titulo"]),
        "",
        "## Contexto",
        "",
        "{} — {}".format(EMPRESA["nombre"], EMPRESA["descripcion"]),
        "",
        "**Estado de la empresa.** {}".format(EMPRESA["estado_inicial"]),
        "",
        "**Restricciones.** {}".format(EMPRESA["restricciones"]),
        "",
        "## Situación",
        "",
        parte["caso"],
        "",
        "El equipo tiene tres semanas para presentar una recomendación al comité. Existen posiciones "
        "encontradas dentro de la empresa y la información disponible es incompleta en varios frentes.",
        "",
        "## Datos disponibles",
        "",
        "| Fuente | Contenido | Limitación conocida |",
        "|---|---|---|",
        "| `datasets/leads.csv` | Origen, estado y fecha de leads | Registro incompleto antes del último trimestre |",
        "| `datasets/customers.csv` | Cuentas, plan, antigüedad y estado | Sin costo de servir por cuenta |",
        "| `datasets/campaigns.csv` | Inversión y resultados por campaña | Atribución de último clic |",
        "| `datasets/ecommerce_orders.csv` | Pedidos, montos y devoluciones | Sin costo logístico desagregado |",
        "| `datasets/experiments.csv` | Pruebas ejecutadas y resultados | Varias sin tamaño de muestra registrado |",
        "",
        "## Preguntas de análisis",
        "",
        "1. ¿Cuál es el problema real y qué evidencia lo sostiene? Distingue síntoma de causa.",
        "2. ¿Qué información falta y cuánto costaría obtenerla? ¿Vale la pena esperarla?",
        "3. ¿Qué dos alternativas son realmente defendibles y qué sacrifica cada una?",
        "4. ¿Qué señal permitiría saber, en 60 días, si la decisión fue correcta?",
        "5. ¿Qué riesgo legal, ético o reputacional introduce la recomendación?",
        "",
        "## Complicación (leer después del primer análisis)",
        "",
        "A mitad del trabajo cambia una condición: el presupuesto disponible se reduce 30 %, un competidor "
        "anuncia una oferta más agresiva y el equipo pierde a una persona clave. Recalcula la recomendación y "
        "explica qué parte del razonamiento se mantiene y cuál cambia.",
        "",
        "## Entregable",
        "",
        "Un decision brief de dos páginas más anexos:",
        "",
        "- hechos, inferencias y supuestos separados;",
        "- dos alternativas con costo de oportunidad;",
        "- recomendación con responsable, fecha y condición de revisión;",
        "- verificación del riesgo: {}".format(minus(parte["riesgo"])),
        "",
        "## Método de discusión sugerido",
        "",
        "1. Lectura individual y registro de la posición inicial (20 minutos).",
        "2. Discusión en grupo con roles asignados: gerencia comercial, finanzas, operaciones y cliente.",
        "3. Presentación de dos posiciones contrapuestas (10 minutos cada una).",
        "4. Red team: el grupo intenta refutar la recomendación ganadora.",
        "5. Cierre con registro de la decisión y de lo que la haría cambiar.",
        "",
        "## Vínculo con el currículo",
        "",
        "Este caso integra la parte {} y en particular la clase {}.{} — {}. Su artefacto alimenta "
        "**{}**.".format(num, num, principal["n"], principal["titulo"], parte["artefacto"]),
        "",
        "---",
        "",
        "[⬅ Clases](../curriculum/{}/README.md) · [Laboratorios](../labs/part-{}/) · "
        "[Evaluación](../assessments/part-{}-assessment.md)".format(parte["slug"], num, num),
        "",
    ]
    return "\n".join(lineas)


# --------------------------------------------------------------------------
# proyectos acumulativos
# --------------------------------------------------------------------------

def render_project(n, p1, p2):
    lineas = [
        "---",
        'title: "Proyecto {} — Partes {} y {}"'.format(n, p1["num"], p2["num"]),
        "type: project",
        "language: es",
        "parts: [{}, {}]".format(p1["num"], p2["num"]),
        "mastery_threshold: 80",
        "updated: {}".format(FECHA),
        "---",
        "",
        "# Proyecto {} — Partes {} y {}".format(n, p1["num"], p2["num"]),
        "",
        "**Partes integradas:** {} y {}.".format(p1["titulo"], p2["titulo"]),
        "",
        "## Objetivo",
        "",
        "Integrar los artefactos de ambas partes en un entregable único y coherente: **{}** y **{}**, "
        "conectados de modo que las decisiones de la primera condicionen explícitamente a la segunda.".format(
            p1["artefacto"], p2["artefacto"]),
        "",
        "## Contexto",
        "",
        "{} — {}".format(EMPRESA["nombre"], EMPRESA["descripcion"]),
        "",
        "Este proyecto se construye sobre el estado acumulado de la simulación: las decisiones tomadas en "
        "proyectos anteriores siguen vigentes y sus consecuencias forman parte del contexto.",
        "",
        "## Entregables",
        "",
        "1. Artefacto de la parte {}: {}.".format(p1["num"], p1["artefacto"]),
        "2. Artefacto de la parte {}: {}.".format(p2["num"], p2["artefacto"]),
        "3. Documento de integración que responda: ¿qué decisión de la parte {} restringe lo posible en la "
        "parte {}?".format(p1["num"], p2["num"]),
        "4. Registro de supuestos con nivel de evidencia y plan de validación.",
        "5. Actualización del estado de la simulación en `simulations/state/`.",
        "",
        "## Preguntas rectoras",
        "",
        "- {}".format(p1["pregunta"]),
        "- {}".format(p2["pregunta"]),
        "- ¿Qué contradicción aparece entre ambos artefactos y cómo se resuelve?",
        "",
        "## Rúbrica (100 puntos)",
        "",
        "| Criterio | Puntos |",
        "|---|---:|",
        "| Calidad del artefacto de la parte {} | 25 |".format(p1["num"]),
        "| Calidad del artefacto de la parte {} | 25 |".format(p2["num"]),
        "| Integración y coherencia entre ambos | 25 |",
        "| Evidencia, supuestos y trazabilidad | 15 |",
        "| Riesgo, cumplimiento y comunicación | 10 |",
        "",
        "**Aprobación:** 80/100.",
        "",
        "## Riesgos a verificar",
        "",
        "- {}".format(p1["riesgo"]),
        "- {}".format(p2["riesgo"]),
        "",
        "---",
        "",
        "[⬅ Parte {}](../curriculum/{}/README.md) · [Parte {}](../curriculum/{}/README.md)".format(
            p1["num"], p1["slug"], p2["num"], p2["slug"]),
        "",
    ]
    return "\n".join(lineas)


# --------------------------------------------------------------------------
# capstone
# --------------------------------------------------------------------------

def render_capstone(cls24):
    lineas = [
        "---",
        'title: "Capstone — Empresa comercial completa"',
        "type: capstone",
        "language: es",
        "mastery_threshold: 80",
        "updated: {}".format(FECHA),
        "---",
        "",
        "# Capstone — Empresa comercial completa",
        "",
        "El Capstone integra las 24 partes del programa en una operación comercial defendible ante un panel "
        "que revisará números, evidencia y cumplimiento normativo.",
        "",
        "## Opciones de alcance",
        "",
        "| Opción | Descripción | Cuándo elegirla |",
        "|---|---|---|",
        "| **A. Empresa propia** | Operación real con datos propios | Si ya existe un negocio en marcha |",
        "| **B. Simulación persistente** | {} con los datos sintéticos del repositorio | Si no hay operación propia |".format(EMPRESA["nombre"]),
        "| **C. Proyecto de terceros** | Empresa real con autorización escrita | Si existe acuerdo formal y datos disponibles |",
        "",
        "En cualquier opción debe declararse explícitamente qué datos son reales y cuáles simulados.",
        "",
        "## Componentes obligatorios",
        "",
        "| # | Componente | Clase de referencia |",
        "|---|---|---|",
    ]
    for c in cls24:
        lineas.append("| {} | {} | [{}.{}](../curriculum/part-24-empresa-real-regulacion-y-capstone/"
                      "class-{}-{}.md) |".format(c["n"], c["titulo"], "24", c["n"], c["n"], c["slug"]))
    lineas += [
        "",
        "## Criterios de evaluación (100 puntos)",
        "",
        "| Bloque | Puntos | Qué se evalúa |",
        "|---|---:|---|",
        "| Diagnóstico y elección de mercado | 15 | Problema verificado, cliente accesible, capacidad de servir |",
        "| Oferta, precio y economía unitaria | 20 | Coherencia entre valor, precio y costo real de servir |",
        "| Go-to-market y adquisición | 15 | Movimiento coherente con el ticket y economía verificable |",
        "| Sistema comercial y operación | 15 | Proceso ejecutable por otra persona, CRM coherente |",
        "| Retención y expansión | 10 | Onboarding conectado con la promesa comercial |",
        "| Analítica y tablero | 10 | Cifras trazables y aritméticamente coherentes |",
        "| Cumplimiento normativo chileno | 10 | Obligaciones traducidas a requisitos de diseño |",
        "| Defensa ejecutiva | 5 | Argumentos sostenidos en evidencia y límites reconocidos |",
        "",
        "**Aprobación:** 80/100 y ningún bloque bajo el 60 % de su puntaje. El bloque de cumplimiento "
        "normativo es eliminatorio: una operación que infringe la Ley 19.496 o la normativa de datos "
        "personales no se aprueba aunque el resto sea excelente.",
        "",
        "## Calendario sugerido (8 semanas)",
        "",
        "| Semana | Foco | Hito verificable |",
        "|---|---|---|",
        "| 1 | Alcance, mercado y problema | Documento de alcance con criterio de suficiencia |",
        "| 2 | Investigación con evidencia | Ocho entrevistas documentadas y revisión de fuentes |",
        "| 3 | Oferta y pricing | Arquitectura de precios con economía unitaria |",
        "| 4 | Marca y activos comerciales | Activos con prueba de uso superada |",
        "| 5 | Go-to-market y campaña | Plan con presupuesto, medición y umbrales |",
        "| 6 | Sistema comercial y CRM | Proceso ejecutable y modelo de datos coherente |",
        "| 7 | Retención, analítica y cumplimiento | Tablero coherente y verificación normativa |",
        "| 8 | Defensa y portafolio | Presentación ejecutiva y portafolio documentado |",
        "",
        "## Reglas de integridad",
        "",
        "- Toda cifra debe poder rastrearse hasta su fuente.",
        "- Todo dato de terceros requiere autorización escrita.",
        "- Toda norma citada debe verificarse en su fuente oficial vigente.",
        "- Todo uso de IA debe declararse, indicando qué se generó y cómo se verificó.",
        "",
        "Ver la lista completa en [`CHECKLIST.md`](CHECKLIST.md).",
        "",
        "---",
        "",
        "[⬅ Parte 24](../curriculum/part-24-empresa-real-regulacion-y-capstone/README.md) · "
        "[Programa](../README.md)",
        "",
    ]
    return "\n".join(lineas)


def render_checklist(cls24):
    lineas = [
        "---",
        'title: "Checklist del Capstone"',
        "type: checklist",
        "language: es",
        "updated: {}".format(FECHA),
        "---",
        "",
        "# Checklist del Capstone",
        "",
        "Marca cada elemento sólo cuando exista evidencia verificable en el repositorio de entrega.",
        "",
        "## Alcance y método",
        "",
        "- [ ] Opción de alcance elegida y justificada.",
        "- [ ] Declaración de qué datos son reales y cuáles simulados.",
        "- [ ] Criterio de suficiencia definido por entregable.",
        "- [ ] Registro de supuestos con nivel de evidencia.",
        "",
    ]
    for c in cls24:
        lineas += ["## {}. {}".format(c["n"], c["titulo"]), ""]
        for termino, _definicion in c["conceptos"]:
            lineas.append("- [ ] Está resuelto y documentado lo relativo a **{}**.".format(termino))
        lineas.append("- [ ] Señal medida o mecanismo de captura diseñado: **{}**.".format(c["senales"][0][0]))
        lineas.append("")
    lineas += [
        "## Cumplimiento normativo (eliminatorio)",
        "",
        "- [ ] Información al consumidor: precio total, condiciones y garantía visibles antes de la compra.",
        "- [ ] Derecho a retracto informado cuando corresponde a venta a distancia.",
        "- [ ] Base de licitud documentada para todo tratamiento de datos personales.",
        "- [ ] Mecanismo operativo de ejercicio de derechos del titular.",
        "- [ ] Verificación de disponibilidad registral de la marca.",
        "- [ ] Obligaciones tributarias de la venta identificadas.",
        "- [ ] Ninguna práctica que infrinja la libre competencia.",
        "- [ ] Cada norma citada verificada en fuente oficial con fecha de consulta.",
        "",
        "## Integridad y uso de IA",
        "",
        "- [ ] Uso de IA declarado por componente.",
        "- [ ] Toda afirmación factual generada fue verificada en fuente primaria.",
        "- [ ] Autorización escrita para datos y testimonios de terceros.",
        "- [ ] Ninguna cifra sin trazabilidad hasta su fuente.",
        "",
        "## Defensa",
        "",
        "- [ ] Resumen ejecutivo de una página con la recomendación al inicio.",
        "- [ ] Respuestas preparadas para las preguntas de estrés.",
        "- [ ] Límites del trabajo declarados explícitamente.",
        "- [ ] Portafolio con al menos seis artefactos documentados.",
        "",
        "---",
        "",
        "[⬅ Capstone](README.md) · [Programa](../README.md)",
        "",
    ]
    return "\n".join(lineas)


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main():
    total = {"labs": 0, "assessments": 0, "cases": 0, "projects": 0}

    for parte in PARTES:
        cls = clases(parte["num"])
        num = parte["num"]

        # limpiar labs previos de la parte
        dir_labs = os.path.join(RAIZ, "labs", "part-{}".format(num))
        if os.path.isdir(dir_labs):
            for f in os.listdir(dir_labs):
                if f.endswith(".md"):
                    os.remove(os.path.join(dir_labs, f))

        anclas = [(cls[3], cls[6]), (cls[9], cls[12])]
        for i, par in enumerate(anclas, start=1):
            ruta = os.path.join(dir_labs, "lab-{}-{}-{}.md".format(num, i, par[0]["slug"]))
            escribir(ruta, render_lab(parte, cls, i, par))
            total["labs"] += 1

        escribir(os.path.join(RAIZ, "assessments", "part-{}-assessment.md".format(num)),
                 render_assessment(parte, cls))
        total["assessments"] += 1

        # limpiar caso previo de la parte
        dir_cases = os.path.join(RAIZ, "cases")
        if os.path.isdir(dir_cases):
            for f in os.listdir(dir_cases):
                if f.startswith("case-{}-".format(num)) and f.endswith(".md"):
                    os.remove(os.path.join(dir_cases, f))
        escribir(os.path.join(dir_cases, "case-{}-{}.md".format(num, parte["slug"].split("-", 2)[2])),
                 render_case(parte, cls))
        total["cases"] += 1

    for i in range(12):
        p1, p2 = PARTES[i * 2], PARTES[i * 2 + 1]
        escribir(os.path.join(RAIZ, "projects", "project-{:02d}-parts-{}-{}.md".format(i + 1, p1["num"], p2["num"])),
                 render_project(i + 1, p1, p2))
        total["projects"] += 1

    cls24 = clases("24")
    escribir(os.path.join(RAIZ, "capstone", "README.md"), render_capstone(cls24))
    escribir(os.path.join(RAIZ, "capstone", "CHECKLIST.md"), render_checklist(cls24))

    print("Labs: {} · Evaluaciones: {} · Casos: {} · Proyectos: {} · Capstone: 2".format(
        total["labs"], total["assessments"], total["cases"], total["projects"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
