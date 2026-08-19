# -*- coding: utf-8 -*-
"""Generador del currículo.

Lee `curriculum/spec/` y escribe:

* `curriculum/part-XX-*/README.md`         índice y contrato de la parte
* `curriculum/part-XX-*/class-YY-*.md`     clase completa (estándar clase-profunda-v1)
* `curriculum/curriculum.json`             índice legible por máquina (sitio, apps, tests)

Uso:
    python tools/build_curriculum.py            # genera todo
    python tools/build_curriculum.py --part 07  # genera una parte
    python tools/build_curriculum.py --check    # no escribe; informa faltantes

Sin dependencias externas: sólo biblioteca estándar.
"""

from __future__ import annotations

import argparse
import importlib
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "curriculum"))

from spec import bibliografia as bib  # noqa: E402
from spec.partes import EMPRESA, PARTES  # noqa: E402

FECHA = "2026-08-19"
VERSION_ESTANDAR = "clase-profunda-v1"


# --------------------------------------------------------------------------
# utilidades de redacción
# --------------------------------------------------------------------------

def rot(opciones, i):
    """Elige una variante de redacción según el índice de la clase."""
    return opciones[(i - 1) % len(opciones)]


def escribir(ruta, contenido):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(contenido)


def leer_specs(num):
    modulo = importlib.import_module("spec.clases_p{}".format(num))
    return modulo.CLASES


def enum_es(items):
    items = list(items)
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + " y " + items[-1]


def minus(texto):
    """Baja la primera letra sin tocar siglas."""
    if texto[:2].isupper():
        return texto
    return texto[0].lower() + texto[1:]


def sin_punto(texto):
    return texto.rstrip(".")


def cap(texto):
    """Sube la primera letra dejando el resto intacto."""
    return texto[0].upper() + texto[1:] if texto else texto


def comillas(texto):
    return "«{}»".format(sin_punto(texto).strip())


# --------------------------------------------------------------------------
# bloques de la clase
# --------------------------------------------------------------------------

APERTURAS = [
    "El punto de partida de esta clase no es la definición sino la decisión que la definición debe mejorar.",
    "Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales.",
    "Antes de cualquier herramienta, esta clase obliga a nombrar qué cambiaría si el análisis fuese correcto.",
    "El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta.",
    "La clase trata el tema como un problema de evidencia y de consecuencia, no como vocabulario.",
    "El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo.",
    "Esta sesión distingue lo que se sabe, lo que se supone y lo que todavía no se ha medido.",
]

CIERRES_DESARROLLO = [
    "Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.",
    "Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.",
    "El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.",
    "Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.",
    "La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.",
]


def front_matter(parte, clase):
    return "\n".join([
        "---",
        'title: "{}"'.format(clase["titulo"].replace('"', "'")),
        "type: class",
        "language: es",
        "standard: {}".format(VERSION_ESTANDAR),
        "part: {}".format(parte["num"]),
        "class: {}".format(clase["n"]),
        "level: {}".format(parte["nivel"]),
        "mastery_threshold: 80",
        "estimated_minutes: 150",
        "sources: {}".format(json.dumps(clase["libros"], ensure_ascii=False)),
        "updated: {}".format(FECHA),
        "---",
        "",
    ])


def bloque_proposito(parte, clase, i):
    conceptos = [c[0] for c in clase["conceptos"]]
    return "\n".join([
        "## 🎯 Propósito",
        "",
        clase["tesis"],
        "",
        "{} La parte {} busca **{}**; en esta clase esa progresión se concreta exigiendo que toda "
        "afirmación sobre **{}** termine en una definición operacional, una señal observable, una "
        "decisión y una condición de revisión.".format(
            rot(APERTURAS, i), parte["num"], parte["resultado"], minus(clase["titulo"])),
        "",
        "> **Pregunta rectora de la parte:** {}".format(parte["pregunta"]),
        "",
        "Los conceptos que estructuran la sesión son {}. No se estudian como lista de vocabulario: "
        "cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.".format(
            enum_es(["**{}**".format(c) for c in conceptos])),
        "",
    ])


def bloque_resultados(parte, clase):
    conceptos = [c[0] for c in clase["conceptos"]]
    metodo = clase["metodo"]
    senales = [s[0] for s in clase["senales"]]
    return "\n".join([
        "## 📚 Resultados de aprendizaje",
        "",
        "Al terminar esta clase serás capaz de:",
        "",
        "1. **Distinguir** {} por sus observables y no por su definición memorizada.".format(
            enum_es(["`{}`".format(c) for c in conceptos])),
        "2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **{}**.".format(
            parte["titulo"]),
        "3. **Aplicar** la secuencia **{}** conservando supuestos, alternativas descartadas y trazabilidad.".format(
            " → ".join(metodo)),
        "4. **Operacionalizar** {} indicando numerador, denominador, ventana, fuente y uso permitido.".format(
            enum_es(["**{}**".format(s) for s in senales])),
        "5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.",
        "6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.",
        "",
    ])


def bloque_agenda(clase):
    c = [x[0] for x in clase["conceptos"]]
    filas = [
        ("0–15 min", "Recuperación", "Define **{}** y **{}** sin mirar el material; corrige después con la tabla de conceptos.".format(c[0], c[1])),
        ("15–45 min", "Núcleo conceptual", "Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`."),
        ("45–75 min", "Medición", "Ficha de la señal **{}**: fórmula, fuente, ventana y lectura prohibida.".format(clase["senales"][0][0])),
        ("75–110 min", "Ejemplo trabajado", "Recorrido de los {} pasos del método sobre el caso de la clase.".format(len(clase["metodo"]))),
        ("110–140 min", "Caso ejecutivo", "Dos alternativas, trade-offs, recomendación y señal de detención."),
        ("140–150 min", "Cierre", "Entregable, preguntas de comprobación y registro de lo que aún no sabes."),
    ]
    lineas = ["## 🧭 Agenda sugerida (150 minutos)", "", "| Tramo | Foco | Evidencia de avance |", "|---|---|---|"]
    lineas += ["| {} | {} | {} |".format(*f) for f in filas]
    lineas.append("")
    return "\n".join(lineas)


COMO_DEMOSTRAR = [
    "Da un hecho compatible con la definición y otro que la refute.",
    "Explica qué decisión cambiaría si el concepto estuviera ausente.",
    "Construye un caso límite donde el concepto se confunde con el anterior.",
    "Indica qué dato tendrías que ver para afirmarlo en una reunión de comité.",
    "Traduce el concepto en una pregunta que puedas hacerle a un cliente real.",
]


def bloque_conceptos(clase, i):
    lineas = ["## 🧩 Conceptos centrales", "",
              "| Concepto | Definición operacional | Cómo demostrar que lo entendiste |", "|---|---|---|"]
    for j, (termino, definicion) in enumerate(clase["conceptos"]):
        lineas.append("| **{}** | {} | {} |".format(termino, definicion, rot(COMO_DEMOSTRAR, i + j)))
    lineas.append("")
    lineas.append("Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. "
                  "Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición "
                  "todavía no es operacional.")
    lineas.append("")
    return "\n".join(lineas)


def bloque_modelo_mental(clase):
    return "\n".join([
        "## 🧠 Modelo mental",
        "",
        "```text",
        " → ".join("{}. {}".format(k + 1, paso) for k, paso in enumerate(clase["metodo"])),
        "```",
        "",
        "La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto "
        "revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo "
        "cuesta más caro.",
        "",
        "**Frontera de aplicación.** {}".format(clase["limite"]),
        "",
    ])


ROLES_BLOQUE = [
    "mecanismo central",
    "frontera conceptual y error de clasificación",
    "operacionalización y medición",
    "trade-offs y efectos de segundo orden",
    "gobernanza, límites e integración",
]


def bloque_desarrollo(parte, clase, i):
    conceptos = clase["conceptos"]
    libros = clase["libros"]
    senales = clase["senales"]
    metodo = clase["metodo"]
    lineas = ["## 📖 Desarrollo", ""]

    # 1. mecanismo central
    t0, d0 = conceptos[0]
    l0 = libros[0]
    lineas += [
        "### 1. {}: {}".format(cap(t0), ROLES_BLOQUE[0]),
        "",
        "**{}** se entiende aquí como **{}**. Es la pieza desde la que se inicia el análisis de {}: antes de "
        "«{}», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería "
        "observarse si no lo está.".format(t0, sin_punto(d0), minus(clase["titulo"]), metodo[0]),
        "",
        "La lectura rectora de este bloque es {}. **Lente que aporta:** {}. Úsala sin convertirla en dogma: escribe una "
        "proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una "
        "consecuencia práctica. La evidencia mínima es **{}**; regístrala con periodo, unidad, población y "
        "línea base.".format(bib.cita(l0), bib.lente(l0), senales[0][0]),
        "",
        "Relaciona el mecanismo con **{}**. Si ambos se mueven juntos no concluyas causalidad: nombra una "
        "tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis "
        "refutable, no una recomendación anticipada.".format(conceptos[1][0]),
        "",
    ]

    # 2. frontera conceptual
    t1, d1 = conceptos[1]
    l1 = libros[1 % len(libros)]
    lineas += [
        "### 2. {}: {}".format(cap(t1), ROLES_BLOQUE[1]),
        "",
        "**Definición operacional:** {}. Su valor está en distinguirlo de **{}**. En una decisión real, "
        "clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, "
        "se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera "
        "una preferencia.".format(sin_punto(d1), t0),
        "",
        "Contrasta el problema con {} —**lente:** {}—. Formula dos mini-casos: uno que satisface la definición "
        "de **{}** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; "
        "**{}** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es "
        "directamente medible.".format(bib.cita(l1), bib.lente(l1), t1,
                                       senales[min(1, len(senales) - 1)][0]),
        "",
        "Antes de pasar a «{}», registra explícitamente qué decisión sería errónea si esta frontera se ignora. "
        "Esa frase convierte el vocabulario en criterio de gestión.".format(metodo[1]),
        "",
    ]

    # 3. operacionalización
    t2, d2 = conceptos[2 % len(conceptos)]
    l2 = libros[2 % len(libros)]
    s0, sd0 = senales[0]
    lineas += [
        "### 3. {}: {}".format(cap(t2), ROLES_BLOQUE[2]),
        "",
        "**{}** significa **{}**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con "
        "qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto "
        "suficiente para no confundir una mejora local con una mejora del sistema.".format(t2, sin_punto(d2)),
        "",
        "Ficha de medición obligatoria para **{}**: `{}`. Registra además fuente del dato, frecuencia, "
        "responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la "
        "salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la "
        "incertidumbre.".format(s0, sd0),
        "",
        "{} orienta este bloque —**lente:** {}—. Pregúntate si el indicador es adelantado o rezagado y si puede ser "
        "manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en "
        "que reemplaza al fenómeno, deja de servir.".format(bib.cita(l2), bib.lente(l2)),
        "",
    ]

    # 4. trade-offs
    t3, d3 = conceptos[3 % len(conceptos)]
    l3 = libros[3 % len(libros)]
    lineas += [
        "### 4. {}: {}".format(cap(t3), ROLES_BLOQUE[3]),
        "",
        "**Definición:** {}. Este concepto obliga a abandonar la idea de que {} tiene una solución gratuita. "
        "Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o "
        "tolerancia al riesgo. Por eso, antes de «{}», se comparan al menos dos alternativas plausibles y se "
        "explicita qué se sacrifica en cada una.".format(
            sin_punto(d3), minus(clase["titulo"]), metodo[min(3, len(metodo) - 1)]),
        "",
        "{} —**lente:** {}— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / "
        "stakeholder afectado / señal temprana`. La evidencia **{}** ayuda a detectar si el trade-off está "
        "ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del "
        "indicador principal.".format(bib.cita(l3), bib.lente(l3), senales[-1][0]),
        "",
        "Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres "
        "mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a "
        "**{}** y otro de un supuesto del caso que nunca fue validado.".format(t3),
        "",
    ]

    # 5. gobernanza
    l4 = libros[-1]
    lineas += [
        "### 5. Gobernanza, límites y responsabilidad",
        "",
        "La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué "
        "evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «{}», deja "
        "una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la "
        "información disponible en ese momento.".format(metodo[-1]),
        "",
        "{} sirve para contrastar la recomendación final desde otro lente: {}. La frontera de esta clase es "
        "explícita: {} Conviértela en una regla operativa con el formato `si ocurre X → no aplicar "
        "automáticamente → consultar, escalar o revalidar`.".format(bib.cita(l4), bib.lente(l4), clase["limite"]),
        "",
        "Esta parte vigila además un riesgo que es obligatorio declarar: **{}** Se documenta en el entregable "
        "con su mitigación y su responsable; no se resuelve en la conversación.".format(parte["riesgo"]),
        "",
    ]

    # 6. integración
    lineas += [
        "### 6. Integración: de conceptos a una decisión defendible",
        "",
        "Sintetizar {} no consiste en sumar definiciones. Empieza por **{}**, contrasta **{}** con **{}**, "
        "incorpora **{}** como restricción y cierra con la medición. Aplica entonces la secuencia completa "
        "conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del "
        "descarte.".format(minus(clase["titulo"]), t0, t1, t2, t3),
        "",
        "Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin "
        "ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. "
        "{}".format(rot(CIERRES_DESARROLLO, i)),
        "",
    ]
    return "\n".join(lineas)


def bloque_lectura(clase):
    lineas = ["## 📚 Lectura comparada", "",
              "Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe "
              "una discrepancia real entre al menos dos fuentes.", "",
              "| Fuente | Lente que aporta | Pregunta crítica |", "|---|---|---|"]
    for clave in clase["libros"]:
        lineas.append("| {} | {} | ¿Qué supuesto de esta clase ayuda a desafiar? |".format(
            bib.cita(clave), bib.lente(clave)))
    lineas += ["",
               "La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué "
               "tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta "
               "cambiarías después del contraste.", ""]
    return "\n".join(lineas)


def bloque_ejemplo(clase):
    lineas = ["## 🧮 Ejemplo trabajado", "", "**Situación.** {}".format(clase["caso"]), ""]
    conceptos = clase["conceptos"]
    senales = clase["senales"]
    plantillas = [
        "El equipo escribe primero el supuesto asociado a **{c}** y se prohíbe tratarlo como hecho. Contrasta "
        "ese supuesto con **{s}** y anota qué parte del dato todavía no existe. Del paso sale un artefacto "
        "revisable y una frase explícita: «cambiaríamos de rumbo si…».",
        "El trabajo aquí es separar lo observado de lo inferido sobre **{c}**. La evidencia que ordena la "
        "discusión es **{s}**; si su definición no está escrita, escribirla es parte del paso. Nada avanza "
        "mientras el equipo no acuerde qué contaría como refutación.",
        "El riesgo de este paso es cerrar demasiado rápido alrededor de **{c}**. Antes de concluir, el equipo "
        "enumera dos explicaciones alternativas del mismo patrón y revisa si **{s}** logra distinguirlas. Si no "
        "lo logra, hace falta otra evidencia y así debe quedar registrado.",
        "Con **{c}** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la "
        "caja y en la carga del equipo. **{s}** entrega la lectura cuantitativa; el juicio sobre el costo de "
        "oportunidad sigue siendo humano y debe quedar firmado.",
        "El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a "
        "**{c}**. **{s}** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y "
        "quién puede declarar el fracaso sin costo político.",
    ]
    for k, paso in enumerate(clase["metodo"]):
        concepto = conceptos[k % len(conceptos)][0]
        senal = senales[k % len(senales)][0]
        cuerpo = plantillas[k % len(plantillas)].format(c=concepto, s=senal)
        lineas += ["**Paso {} — {}.** {}".format(k + 1, cap(paso), cuerpo), ""]
    lineas += [
        "**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. "
        "Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.",
        "",
    ]
    return "\n".join(lineas)


def bloque_comparacion(clase):
    c = clase["conceptos"]
    s = clase["senales"]
    lineas = ["## 🔀 Comparación de caminos y límites", "",
              "| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |", "|---|---|---|---|"]
    lineas.append("| Actuar sobre **{}** | {} | Cuando **{}** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |".format(
        c[0][0], cap(sin_punto(c[0][1])), s[0][0]))
    lineas.append("| Actuar sobre **{}** | {} | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |".format(
        c[1][0], cap(sin_punto(c[1][1]))))
    lineas.append("| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |")
    lineas.append("| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |")
    lineas += ["", "**Frontera de aplicación.** {}".format(clase["limite"]), ""]
    return "\n".join(lineas)


def bloque_escalamiento(parte, clase):
    tema = minus(clase["titulo"])
    lineas = ["## 🪜 El mismo tema según el rol", "",
              "| Nivel | Responsabilidad sobre {} |".format(tema), "|---|---|"]
    lineas += [
        "| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |",
        "| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |",
        "| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como {}. |".format(
            enum_es(parte["roles"])),
        "| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |",
        "| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |",
        "",
        "Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. "
        "La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el "
        "alcance.",
        "",
    ]
    return "\n".join(lineas)


def bloque_caso_ejecutivo(clase):
    return "\n".join([
        "## 🏢 Caso ejecutivo",
        "",
        clase["caso"],
        "",
        "Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones "
        "realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la "
        "condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la "
        "lectura comparada para desafiar tu primera respuesta.",
        "",
    ])


def bloque_practica(clase):
    return "\n".join([
        "## 🧪 Práctica guiada",
        "",
        "1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.",
        "2. Ejecuta la secuencia **{}** y adjunta evidencia en cada transición.".format(" → ".join(clase["metodo"])),
        "3. Construye la ficha de medición de **{}**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.".format(
            clase["senales"][0][0]),
        "4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.",
        "5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.",
        "6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.",
        "",
    ])


def bloque_errores(clase):
    c = clase["conceptos"]
    lineas = ["## ⚠️ Errores frecuentes", "", "| Síntoma | Causa probable | Corrección |", "|---|---|---|"]
    lineas.append("| Usar **{}** y **{}** como sinónimos | Se perdió la distinción entre «{}» y «{}» | Vuelve a los observables y exige una señal distinta para cada concepto. |".format(
        c[0][0], c[1][0], sin_punto(c[0][1]), sin_punto(c[1][1])))
    lineas.append("| Empezar por «{}» | Se saltó «{}»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |".format(
        clase["metodo"][-1], clase["metodo"][0]))
    lineas.append("| Optimizar sólo **{}** | La métrica local reemplazó al resultado del sistema | Contrástala con **{}** y explicita el costo de oportunidad. |".format(
        clase["senales"][0][0], clase["senales"][-1][0]))
    lineas.append("| {} | Error específico de esta clase | {} |".format(
        clase["error"][0], clase["error"][1]))
    lineas.append("| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |")
    lineas.append("")
    return "\n".join(lineas)


def bloque_preguntas(clase):
    c = clase["conceptos"]
    s = clase["senales"]
    return "\n".join([
        "## ❓ Preguntas de comprobación",
        "",
        "1. Explica la diferencia entre **{}** y **{}** con un ejemplo donde elegir mal cambie la decisión.".format(c[0][0], c[1][0]),
        "2. ¿Qué observarías para validar **{}** y qué observación te obligaría a rechazar tu interpretación?".format(c[2 % len(c)][0]),
        "3. Aplica «{}» al caso de la clase. ¿Qué dato sigue faltando?".format(clase["metodo"][0]),
        "4. ¿Por qué **{}** no basta por sí sola para atribuir causalidad?".format(s[0][0]),
        "5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?",
        "6. ¿Qué decisión equivocada se produciría si se ignora este límite: {}?".format(comillas(clase["limite"])),
        "",
    ])


def bloque_chile(parte, clase):
    return "\n".join([
        "## 🇨🇱 Contexto chileno y cumplimiento",
        "",
        "Riesgo asociado a esta parte: **{}** Antes de ejecutar cualquier recomendación de esta clase en una "
        "operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria "
        "vigente.".format(parte["riesgo"]),
        "",
        "- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).",
        "- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).",
        "- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.",
        "",
        "La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma "
        "cambió después de la fecha de esta clase, gana la norma.",
        "",
    ])


def bloque_entregable(parte, clase):
    carpeta = "evidence/P{}-C{}-{}".format(parte["num"], clase["n"], clase["slug"])
    return "\n".join([
        "## 📥 Entregable",
        "",
        "Guarda en `{}/`:".format(carpeta),
        "",
        "- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.",
        "- `ficha-metricas.md` — definición operacional de {} con fuente, ventana y lectura prohibida.".format(
            enum_es(["**{}**".format(s[0]) for s in clase["senales"]])),
        "- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.",
        "- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.",
        "",
        "Este entregable alimenta el artefacto de la parte: **{}**.".format(parte["artefacto"]),
        "",
    ])


def bloque_evaluacion(clase):
    return "\n".join([
        "## ✅ Evaluación de la clase",
        "",
        "| Criterio | Peso | Evidencia esperada |",
        "|---|---:|---|",
        "| Precisión conceptual | 25 % | Distinciones correctas y observables entre los conceptos de la clase. |",
        "| Diagnóstico y evidencia | 30 % | Datos pertinentes, línea base, supuestos explícitos y límites del dato. |",
        "| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad y condición de revisión. |",
        "| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas y argumento ejecutivo trazable. |",
        "",
        "**Aprobación:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambios a "
        "otra clase se considera insuficiente.",
        "",
    ])


def bloque_fuentes(clase):
    lineas = ["## 📗 Fuentes y verificación", ""]
    for clave in clase["libros"]:
        lineas.append("- {}. **Uso en esta clase:** {}. Lectura selectiva: índice y capítulos pertinentes; "
                      "registra edición y páginas consultadas.".format(bib.cita(clave), bib.lente(clave)))
    lineas.append("")
    lineas.append("**Estándar pedagógico del programa:** " + "; ".join(
        bib.cita(k) for k in bib.NUCLEO_PEDAGOGICO) + ".")
    lineas += [
        "",
        "> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier "
        "norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente "
        "en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es "
        "original y no reproduce capítulos protegidos por derechos de autor.",
        "",
    ]
    return "\n".join(lineas)


def navegacion(parte, clases, idx):
    anterior = clases[idx - 1] if idx > 0 else None
    siguiente = clases[idx + 1] if idx < len(clases) - 1 else None
    partes = []
    if anterior:
        partes.append("← [Clase {} · {}](class-{}-{}.md)".format(
            anterior["n"], anterior["titulo"], anterior["n"], anterior["slug"]))
    partes.append("[Índice de la parte](README.md)")
    if siguiente:
        partes.append("[Clase {} · {}](class-{}-{}.md) →".format(
            siguiente["n"], siguiente["titulo"], siguiente["n"], siguiente["slug"]))
    return "\n".join(["---", "", " · ".join(partes), ""])


def render_clase(parte, clases, idx):
    clase = clases[idx]
    i = int(clase["n"])
    partes_doc = [
        front_matter(parte, clase),
        "# Clase {}.{} — {}\n".format(parte["num"], clase["n"], clase["titulo"]),
        "**Parte {} · {}** · Nivel: {} · Duración sugerida: 150 minutos · Estándar: `{}`\n".format(
            parte["num"], parte["titulo"], parte["nivel"], VERSION_ESTANDAR),
        bloque_proposito(parte, clase, i),
        bloque_resultados(parte, clase),
        bloque_agenda(clase),
        bloque_conceptos(clase, i),
        bloque_modelo_mental(clase),
        bloque_desarrollo(parte, clase, i),
        bloque_lectura(clase),
        bloque_ejemplo(clase),
        bloque_comparacion(clase),
        bloque_escalamiento(parte, clase),
        bloque_caso_ejecutivo(clase),
        bloque_practica(clase),
        bloque_errores(clase),
        bloque_preguntas(clase),
        bloque_chile(parte, clase),
        bloque_entregable(parte, clase),
        bloque_evaluacion(clase),
        bloque_fuentes(clase),
        navegacion(parte, clases, idx),
    ]
    return "\n".join(partes_doc)


# --------------------------------------------------------------------------
# README de la parte
# --------------------------------------------------------------------------

def render_readme(parte, clases):
    num = parte["num"]
    lineas = [
        "---",
        'title: "Parte {} — {}"'.format(num, parte["titulo"]),
        "type: part-index",
        "language: es",
        "part: {}".format(num),
        "updated: {}".format(FECHA),
        "---",
        "",
        "# Parte {} — {}".format(num, parte["titulo"]),
        "",
        "**Nivel:** {} · **Clases:** {} · **Carga estimada:** {} horas de estudio dirigido".format(
            parte["nivel"], len(clases), len(clases) * 25 // 10),
        "",
        "## Resultado de la parte",
        "",
        "Al terminar esta parte debes poder **{}**.".format(parte["resultado"]),
        "",
        "> **Pregunta rectora:** {}".format(parte["pregunta"]),
        "",
        "## Caso de la parte",
        "",
        parte["caso"],
        "",
        "El caso persistente del programa es **{}**: {}".format(EMPRESA["nombre"], EMPRESA["descripcion"]),
        "",
        "## Competencias que desarrolla",
        "",
    ]
    lineas += ["- {}".format(c) for c in parte["competencias"]]
    lineas += [
        "",
        "**Roles a los que habilita:** {}.".format(enum_es(parte["roles"])),
        "",
        "## Clases",
        "",
        "| # | Clase | Conceptos centrales |",
        "|---|---|---|",
    ]
    for clase in clases:
        conceptos = ", ".join(c[0] for c in clase["conceptos"][:3])
        lineas.append("| {} | [{}](class-{}-{}.md) | {} |".format(
            clase["n"], clase["titulo"], clase["n"], clase["slug"], conceptos))
    lineas += [
        "",
        "## Práctica y evaluación",
        "",
        "| Recurso | Ruta |",
        "|---|---|",
        "| Laboratorios | [`labs/part-{}/`](../../labs/part-{}/) |".format(num, num),
        "| Evaluación de la parte | [`assessments/part-{}-assessment.md`](../../assessments/part-{}-assessment.md) |".format(num, num),
        "| Caso extendido | [`cases/case-{}-*.md`](../../cases/) |".format(num),
        "| Plantillas | [`templates/`](../../templates/) |",
        "",
        "**Artefacto de portafolio:** {}.".format(parte["artefacto"]),
        "",
        "## Riesgo a vigilar",
        "",
        "{} Revisa `docs/MAPA-REGULATORIO-CHILE.md` y `docs/DATOS-PERSONALES-Y-ETICA.md` antes de llevar "
        "cualquier recomendación a una operación real.".format(parte["riesgo"]),
        "",
        "## Bibliografía rectora de la parte",
        "",
    ]
    lineas += ["- {} — {}.".format(bib.cita(k), bib.lente(k)) for k in parte["libros"]]
    lineas += [
        "",
        "---",
        "",
        "[⬅ Índice del currículo](../README.md) · [Programa](../../README.md)",
        "",
    ]
    return "\n".join(lineas)


def render_indice_curriculo(datos):
    lineas = [
        "---",
        'title: "Currículo — 24 partes y 336 clases"',
        "type: curriculum-index",
        "language: es",
        "updated: {}".format(FECHA),
        "---",
        "",
        "# Currículo",
        "",
        "24 partes, {} clases y un caso persistente. Cada clase sigue el estándar `{}`: conceptos con "
        "definición operacional, método, medición, caso, límites, evaluación y fuentes verificables.".format(
            sum(len(p["clases"]) for p in datos), VERSION_ESTANDAR),
        "",
        "## Caso persistente",
        "",
        "**{}** — {}".format(EMPRESA["nombre"], EMPRESA["descripcion"]),
        "",
        "**Estado inicial:** {}".format(EMPRESA["estado_inicial"]),
        "",
        "**Restricciones:** {}".format(EMPRESA["restricciones"]),
        "",
        "## Partes",
        "",
        "| # | Parte | Nivel | Clases | Artefacto |",
        "|---|---|---|---:|---|",
    ]
    for p in datos:
        lineas.append("| {} | [{}]({}/README.md) | {} | {} | {} |".format(
            p["num"], p["titulo"], p["slug"], p["nivel"], len(p["clases"]), p["artefacto"]))
    lineas += [
        "",
        "## Cómo estudiar una clase",
        "",
        "1. Responde la pregunta rectora antes de leer: fuerza la recuperación previa.",
        "2. Lee el desarrollo y completa la tabla `hecho / inferencia / supuesto / decisión`.",
        "3. Construye la ficha de medición de la clase.",
        "4. Resuelve el caso ejecutivo con dos alternativas reales.",
        "5. Guarda la evidencia en `evidence/` con la convención indicada en la clase.",
        "6. Aprueba la evaluación con 80 % o más antes de avanzar.",
        "",
        "---",
        "",
        "[⬅ Volver al programa](../README.md)",
        "",
    ]
    return "\n".join(lineas)


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Genera el currículo desde curriculum/spec/")
    ap.add_argument("--part", help="Genera sólo una parte (por ejemplo 07)")
    ap.add_argument("--check", action="store_true", help="No escribe; informa partes sin especificación")
    args = ap.parse_args()

    datos = []
    faltantes = []
    escritas = 0

    for parte in PARTES:
        if args.part and parte["num"] != args.part:
            continue
        try:
            clases = leer_specs(parte["num"])
        except ModuleNotFoundError:
            faltantes.append(parte["num"])
            continue

        if len(clases) != 14:
            raise SystemExit("Parte {}: se esperaban 14 clases y hay {}".format(parte["num"], len(clases)))

        destino = os.path.join(RAIZ, "curriculum", parte["slug"])
        if not args.check:
            esperados = {"README.md"}
            esperados |= {"class-{}-{}.md".format(c["n"], c["slug"]) for c in clases}
            if os.path.isdir(destino):
                for existente in os.listdir(destino):
                    if existente.endswith(".md") and existente not in esperados:
                        os.remove(os.path.join(destino, existente))
                        print("Eliminado obsoleto: {}/{}".format(parte["slug"], existente))
            for idx, clase in enumerate(clases):
                ruta = os.path.join(destino, "class-{}-{}.md".format(clase["n"], clase["slug"]))
                escribir(ruta, render_clase(parte, clases, idx))
                escritas += 1
            escribir(os.path.join(destino, "README.md"), render_readme(parte, clases))

        datos.append({
            "num": parte["num"],
            "slug": parte["slug"],
            "titulo": parte["titulo"],
            "nivel": parte["nivel"],
            "resultado": parte["resultado"],
            "artefacto": parte["artefacto"],
            "roles": parte["roles"],
            "libros": parte["libros"],
            "clases": [{
                "n": c["n"],
                "slug": c["slug"],
                "titulo": c["titulo"],
                "conceptos": [t for t, _ in c["conceptos"]],
                "senales": [s for s, _ in c["senales"]],
                "libros": c["libros"],
                "ruta": "curriculum/{}/class-{}-{}.md".format(parte["slug"], c["n"], c["slug"]),
            } for c in clases],
        })

    if faltantes:
        print("Partes sin especificación: {}".format(", ".join(faltantes)))
    if args.check:
        print("Partes con especificación: {}/24".format(len(datos)))
        return 0 if not faltantes else 1

    if not args.part:
        escribir(os.path.join(RAIZ, "curriculum", "README.md"), render_indice_curriculo(datos))
        with open(os.path.join(RAIZ, "curriculum", "curriculum.json"), "w", encoding="utf-8", newline="\n") as fh:
            json.dump({"version": VERSION_ESTANDAR, "actualizado": FECHA,
                       "empresa": EMPRESA, "partes": datos}, fh, ensure_ascii=False, indent=2)
            fh.write("\n")

    print("Clases escritas: {}".format(escritas))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
