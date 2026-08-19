# -*- coding: utf-8 -*-
"""Generador del currículo.

Lee `curriculum/spec/` y escribe:

* `curriculum/part-XX-*/README.md`         índice y contrato de la parte
* `curriculum/part-XX-*/class-YY-*.md`     clase completa (estándar clase-profunda-v2)
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
from spec import normas  # noqa: E402
from spec.anclajes import ANCLAJES  # noqa: E402
from spec.aportes import APORTES  # noqa: E402
from spec.localizadores import acceso_legible, enlace, etiqueta  # noqa: E402
from spec.partes import EMPRESA, PARTES  # noqa: E402


def cita_localizada(clave):
    """Cita con el título enlazado a su localizador y el ISBN a la vista.

    Que la obra esté nombrada no basta para comprobarla: hace falta poder ir a
    buscarla sin salir a adivinar la edición.
    """
    autor, obra, edicion, _lente, _cat = bib.LIBROS[clave]
    return "{} — {} ({}) · {}".format(
        autor, enlace(clave, "*{}*".format(obra)), edicion, etiqueta(clave))

FECHA = "2026-08-19"
VERSION_ESTANDAR = "clase-profunda-v2"


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
    """Carga las clases de una parte y les adjunta su desarrollo escrito.

    El desarrollo vive en `spec/desarrollo_pNN.py` porque es texto redactado
    clase a clase, no una plantilla: separarlo del resto de la especificación
    permite revisarlo y corregirlo como se corrige un manuscrito.
    """
    modulo = importlib.import_module("spec.clases_p{}".format(num))
    desarrollo = importlib.import_module("spec.desarrollo_p{}".format(num)).DESARROLLO
    clases = modulo.CLASES
    for clase in clases:
        parrafos = desarrollo.get(clase["n"])
        if not parrafos or len(parrafos) < 5:
            raise SystemExit(
                "Falta el desarrollo escrito de la clase {}.{}".format(num, clase["n"]))
        clase["desarrollo"] = parrafos
    return clases


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
# anclaje bibliográfico
# --------------------------------------------------------------------------

def anclas(parte, clase):
    """Devuelve [(clave, idea, dónde buscarla)] en el orden en que la clase cita.

    El anclaje es obligatorio: si falta, el generador se detiene en lugar de
    escribir una clase que cita obras sin declarar qué idea de cada una la
    sostiene.
    """
    ref = "{}.{}".format(parte["num"], clase["n"])
    mapa = ANCLAJES.get(ref)
    if not mapa:
        raise SystemExit("Falta anclaje bibliográfico para la clase {}".format(ref))
    salida = []
    for clave in clase["libros"]:
        ident = mapa.get(clave)
        if ident is None:
            raise SystemExit("La clase {} cita {} sin anclar una idea".format(ref, clave))
        idea, donde = APORTES[clave][ident]
        salida.append((clave, idea, donde))
    return salida


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


def bloque_antes(parte, clases, idx):
    """Entrada a la clase, en prosa.

    Esto era una ficha de cinco filas. Una tabla de requisitos al abrir una
    clase no enseña nada: obliga a leer campos sueltos antes de saber de qué
    trata la sesión, y lo que un estudiante necesita al empezar no son casillas
    sino una explicación de dónde está parado y por qué esta clase viene ahora.
    """
    clase = clases[idx]
    anterior = clases[idx - 1] if idx > 0 else None
    if anterior:
        previo = ("Vienes de la clase {}.{}, *{}*: ten a mano su entregable, porque esta sesión "
                  "lo retoma y lo lleva más lejos.".format(
                      parte["num"], anterior["n"], anterior["titulo"]))
    else:
        previo = ("Esta es la primera clase de la parte, así que no arrastras entregables de las "
                  "anteriores. Si llegas desde otra parte, ten a la vista su artefacto final; si "
                  "el programa empieza aquí para ti, lee antes "
                  "[la ruta de aprendizaje](../../docs/RUTA-DE-APRENDIZAJE.md).")
    obras = anclas(parte, clase)
    return "\n".join([
        "## 🚦 Antes de empezar",
        "",
        previo,
        "",
        "Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo "
        "mínimo que necesitas es una serie histórica de {} con la que calcular una línea base: sin "
        "ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten "
        "también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el "
        "índice y los capítulos que se indican al pie.".format(clase["senales"][0][0]),
        "",
        "Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que "
        "terminaste cuando exista el entregable y puedas responder las seis preguntas de "
        "comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que "
        "produjiste es un documento, no un criterio.",
        "",
        "Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de "
        "cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que "
        "producir. No avances de sección sin escribir algo: este material está hecho para dejar "
        "decisiones documentadas, no notas de lectura.",
        "",
        "**La idea que ordena la sesión.** {} — {}. Todo lo demás en esta clase existe para poner "
        "esa idea a prueba contra un caso concreto.".format(
            cap(obras[0][1]), bib.autor(obras[0][0])),
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
    senales = clase["senales"]
    metodo = clase["metodo"]
    obras = anclas(parte, clase)
    # Texto escrito para esta clase en particular. El andamiaje es común; el
    # argumento no. Sin él la clase no se genera.
    d = clase["desarrollo"]
    lineas = ["## 📖 Desarrollo", ""]

    # 1. mecanismo central
    t0, d0 = conceptos[0]
    l0, idea0, donde0 = obras[0]
    lineas += [
        "### 1. {}: {}".format(cap(t0), ROLES_BLOQUE[0]),
        "",
        "**{}** se entiende aquí como **{}**.".format(cap(t0), sin_punto(d0)),
        "",
        d[0],
        "",
        "**De dónde viene esta afirmación.** {} aporta la idea que sostiene este bloque: {}. Búscala en {}. "
        "Aplicada a esta clase, esa idea predice algo verificable: si es correcta, {} debería moverse cuando "
        "cambie **{}**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que "
        "montar antes de recomendar nada.".format(bib.cita(l0), idea0, donde0, comillas(senales[0][0]), t0),
        "",
        "Relaciona el mecanismo con **{}**. Si ambos se mueven juntos no concluyas causalidad: nombra una "
        "tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis "
        "refutable, no una recomendación anticipada.".format(conceptos[1][0]),
        "",
    ]

    # 2. frontera conceptual
    t1, d1 = conceptos[1]
    l1, idea1, donde1 = obras[1 % len(obras)]
    lineas += [
        "### 2. {}: {}".format(cap(t1), ROLES_BLOQUE[1]),
        "",
        "**Definición operacional:** {}. Su valor está en distinguirlo de **{}**.".format(sin_punto(d1), t0),
        "",
        d[1],
        "",
        "**Contraste bibliográfico.** {} aporta aquí una distinción concreta: {} ({}). Formula dos mini-casos: uno que satisface la "
        "definición de **{}** y otro que sólo se le parece en la superficie; después decide cuál de los dos "
        "describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es "
        "tuya y tienes que sostenerla con evidencia del caso, no con la cita.".format(
            bib.cita(l1), idea1, donde1, t1),
        "",
        "Antes de pasar a «{}», registra explícitamente qué decisión sería errónea si esta frontera se ignora. "
        "Esa frase convierte el vocabulario en criterio de gestión.".format(metodo[1]),
        "",
    ]

    # 3. operacionalización
    t2, d2 = conceptos[2 % len(conceptos)]
    l2, idea2, donde2 = obras[2 % len(obras)]
    s0, sd0 = senales[0]
    lineas += [
        "### 3. {}: {}".format(cap(t2), ROLES_BLOQUE[2]),
        "",
        "**{}** significa **{}**.".format(cap(t2), sin_punto(d2)),
        "",
        d[2],
        "",
        "Ficha de medición obligatoria para **{}**: `{}`. Registra además fuente del dato, frecuencia, "
        "responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la "
        "salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la "
        "incertidumbre.".format(s0, sd0),
        "",
        "**Control de lectura.** {} pone una condición sobre la medición: {} ({}). Contrasta tu ficha con ella: si la métrica que "
        "acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de "
        "usarla para decidir.".format(bib.cita(l2), idea2, donde2),
        "",
    ]

    # 4. trade-offs
    t3, d3 = conceptos[3 % len(conceptos)]
    l3, idea3, donde3 = obras[3 % len(obras)]
    lineas += [
        "### 4. {}: {}".format(cap(t3), ROLES_BLOQUE[3]),
        "",
        "**Definición:** {}.".format(sin_punto(d3)),
        "",
        d[3],
        "",
        "**Lo que aporta la fuente.** {} aporta el criterio para pesar el intercambio: {} ({}). Úsalo para construir una matriz `beneficio "
        "esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **{}** ayuda a detectar "
        "si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos "
        "laterales fuera del indicador principal.".format(bib.cita(l3), idea3, donde3, senales[-1][0]),
        "",
        "Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres "
        "mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a "
        "**{}** y otro de un supuesto del caso que nunca fue validado.".format(t3),
        "",
    ]

    # 5. gobernanza
    lineas += [
        "### 5. Gobernanza, límites y responsabilidad",
        "",
        "La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué "
        "evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «{}», deja "
        "una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la "
        "información disponible en ese momento.".format(metodo[-1]),
        "",
        d[4] if len(d) > 4 else
        "La frontera de esta clase no es una advertencia decorativa: delimita el rango de casos donde el "
        "método rinde y fuera del cual produce falsa confianza.",
        "",
        "**Frontera declarada.** {} Conviértela en una regla operativa con el formato `si ocurre X → no "
        "aplicar automáticamente → consultar, escalar o revalidar`.".format(clase["limite"]),
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


def bloque_lectura(parte, clase):
    """Lectura dirigida: qué idea buscar en cada obra y qué pregunta le hace a esta clase."""
    obras = anclas(parte, clase)
    conceptos = [c[0] for c in clase["conceptos"]]
    lineas = ["## 📚 Lectura comparada", "",
              "No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta "
              "clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura "
              "termina cuando puedes responder esa pregunta con evidencia del caso.", "",
              "| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |",
              "|---|---|---|---|"]
    for k, (clave, idea, donde) in enumerate(obras):
        concepto = conceptos[k % len(conceptos)]
        pregunta = ("¿Qué debería observarse en **{}** si aquí opera {}? ¿Y qué observación lo "
                    "desmentiría en este caso?".format(concepto, comillas(idea)))
        lineas.append("| {} | {} | {} | {} |".format(bib.cita(clave), cap(idea), cap(donde), pregunta))
    lineas += ["",
               "**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan "
               "recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué "
               "condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que "
               "leíste buscando confirmación.",
               "",
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


def bloque_practica(parte, clase):
    """Práctica con instrucción explícita y criterio de término por paso."""
    obras = anclas(parte, clase)
    s0 = clase["senales"][0][0]
    pasos = [
        ("Reconstruir los hechos",
         "Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado.",
         "El caso y nada más",
         "Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo."),
        ("Ejecutar el método",
         "Recorre la secuencia **{}** y adjunta la evidencia usada en cada transición.".format(" → ".join(clase["metodo"])),
         "La tabla del paso 1",
         "Cada paso deja un artefacto revisable y una alternativa descartada con su razón."),
        ("Operacionalizar la señal",
         "Construye la ficha de medición de **{}**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría.".format(s0),
         "Fuentes de datos reales o el diseño de captura",
         "Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado."),
        ("Atacar tu propia respuesta",
         "Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses.",
         "Tu borrador de recomendación",
         "Puedes nombrar el dato concreto que te haría cambiar de opinión."),
        ("Contrastar con la fuente",
         "Lee la idea anclada de *{}* y la de *{}*, y registra una coincidencia y una tensión con tu diagnóstico.".format(
             bib.obra(obras[0][0]), bib.obra(obras[1 % len(obras)][0])),
         "La tabla de lectura comparada",
         "La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué."),
        ("Subir de nivel",
         "Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad.",
         "El brief completo",
         "El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa."),
    ]
    lineas = ["## 🧪 Práctica guiada", "",
              "Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la "
              "última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.", "",
              "| # | Paso | Qué haces | Con qué | Criterio de término |", "|---:|---|---|---|---|"]
    for k, (titulo, que, con, criterio) in enumerate(pasos, start=1):
        lineas.append("| {} | **{}** | {} | {} | {} |".format(k, titulo, que, con, criterio))
    lineas += ["",
               "**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de "
               "conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema "
               "está ahí y no en el paso que estabas ejecutando.", ""]
    return "\n".join(lineas)


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


def bloque_respuestas(parte, clase):
    """Qué debe contener una respuesta suficiente. No entrega la respuesta: entrega el criterio."""
    c = [x[0] for x in clase["conceptos"]]
    s = clase["senales"]
    obras = anclas(parte, clase)
    filas = [
        ("1",
         "Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo "
         "funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida."),
        ("2",
         "Dos observaciones concretas: una que confirmaría **{}** y otra que te obligaría a abandonarlo. Una "
         "respuesta sin condición de refutación no es suficiente.".format(c[2 % len(c)])),
        ("3",
         "El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. "
         "«Faltan datos» no cuenta como respuesta."),
        ("4",
         "Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo "
         "movimiento de **{}**.".format(s[0][0])),
        ("5",
         "Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta "
         "correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *{}* y "
         "*{}*.".format(bib.obra(obras[0][0]), bib.obra(obras[-1][0]))),
        ("6",
         "Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. "
         "Un límite que no produce una decisión distinta no está operando como límite."),
    ]
    lineas = ["## 🗝️ Respuestas orientadoras", "",
              "No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta "
              "suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.", "",
              "| Pregunta | Una respuesta suficiente contiene |", "|:--:|---|"]
    lineas += ["| {} | {} |".format(n, texto) for n, texto in filas]
    lineas += ["",
               "Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el "
               "desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más "
               "adelante, decisiones que nadie puede auditar.", ""]
    return "\n".join(lineas)


def bloque_chile(parte, clase):
    """Cumplimiento chileno, con el texto de cada norma enlazado.

    Antes esta sección nombraba las leyes y remitía a documentos internos del
    repositorio. Nombrar una ley y no enlazarla obliga al lector a fiarse: es
    justo lo contrario de lo que la sección pide. Estas normas son además las
    únicas fuentes del programa que se pueden leer completas y gratis, así que
    aquí no hay nada que creer, hay un texto al que ir.
    """
    return "\n".join([
        "## 🇨🇱 Contexto chileno y cumplimiento",
        "",
        "Riesgo asociado a esta parte: **{}** Antes de ejecutar cualquier recomendación de esta clase en una "
        "operación real, comprueba la norma en su texto vigente. Los enlaces van al texto completo publicado "
        "por la Biblioteca del Congreso Nacional; son gratuitos y no hace falta creerle a este "
        "material.".format(parte["riesgo"]),
        "",
        "- **Consumo y comercio.** {}, y su reglamento de comercio electrónico, {}.".format(
            normas.cita("ley-19496"), normas.cita("decreto-6-2021")),
        "- **Datos personales.** {}, que sustituye progresivamente a {}.".format(
            normas.cita("ley-21719"), normas.cita("ley-19628")),
        "- **Derecho a retracto.** {}.".format(normas.cita("decreto-52-2024")),
        "",
        "Dentro del repositorio, el "
        "[mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) ordena qué norma aplica a cada decisión "
        "comercial, [datos personales y ética](../../docs/DATOS-PERSONALES-Y-ETICA.md) desarrolla el "
        "tratamiento de datos y [fuentes oficiales](../../docs/FUENTES-OFICIALES.md) lista los organismos con "
        "su fecha de consulta. Ninguno de esos documentos reemplaza al texto legal.",
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


def bloque_fuentes(parte, clase):
    lineas = ["## 📗 Fuentes y verificación", "",
              "Aquí conviene separar dos cosas que suelen ir juntas y no son lo mismo.",
              "",
              "**Lo que está comprobado.** Que cada obra existe y cuál es exactamente la edición: el enlace "
              "resuelve su ISBN contra el catálogo de OpenLibrary, y eso se revalida periódicamente. Las "
              "normas chilenas citadas más arriba enlazan su texto completo y gratuito.",
              "",
              "**Lo que es atribución del programa.** Que la idea señalada esté en el capítulo que se indica. "
              "Eso es la lectura que este material hace de cada obra, no una cita textual cotejada frase por "
              "frase, y se declara así de explícito para que puedas contrastarlo: si abres la obra y no "
              "encuentras la idea donde se dice, la cita está mal puesta y **corresponde reportarlo como error "
              "del material**. No se citan números de página porque cambian entre ediciones.",
              ""]
    for clave, idea, donde in anclas(parte, clase):
        lineas.append("- {} — **aporta a esta clase:** {}. **Dónde buscarlo:** {}. **Acceso:** {}. Registra "
                      "edición y páginas consultadas en tu nota de lectura.".format(
                          cita_localizada(clave), idea, donde, acceso_legible(clave)))
    lineas.append("")
    lineas.append("**Estándar pedagógico del programa:** " + "; ".join(
        "{} — {} ({})".format(bib.autor(k), enlace(k, "*{}*".format(bib.obra(k))),
                              bib.LIBROS[k][2])
        for k in bib.NUCLEO_PEDAGOGICO) + ".")
    lineas += [
        "",
        "> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier "
        "norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente "
        "en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es "
        "original y no reproduce capítulos protegidos por derechos de autor.",
        "",
        "> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian "
        "capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el "
        "[registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con "
        "todas sus obras, está en su [índice](README.md).",
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
        "# Clase {}.{} — {}\n".format(parte["num"], clase["n"], clase["titulo"]),
        "Clase {} de {} de la parte [{} — {}](README.md), de nivel {}. Dura unos 150 minutos.\n".format(
            int(clase["n"]), len(clases), parte["num"], parte["titulo"], parte["nivel"]),
        bloque_antes(parte, clases, idx),
        bloque_proposito(parte, clase, i),
        bloque_resultados(parte, clase),
        bloque_agenda(clase),
        bloque_conceptos(clase, i),
        bloque_modelo_mental(clase),
        bloque_desarrollo(parte, clase, i),
        bloque_lectura(parte, clase),
        bloque_ejemplo(clase),
        bloque_comparacion(clase),
        bloque_escalamiento(parte, clase),
        bloque_caso_ejecutivo(clase),
        bloque_practica(parte, clase),
        bloque_errores(clase),
        bloque_preguntas(clase),
        bloque_respuestas(parte, clase),
        bloque_chile(parte, clase),
        bloque_entregable(parte, clase),
        bloque_evaluacion(clase),
        bloque_fuentes(parte, clase),
        navegacion(parte, clases, idx),
    ]
    return "\n".join(partes_doc)


# --------------------------------------------------------------------------
# README de la parte
# --------------------------------------------------------------------------

def vecinas(parte):
    """La parte anterior y la siguiente, para situar ésta en el recorrido."""
    indice = [p["num"] for p in PARTES].index(parte["num"])
    previa = PARTES[indice - 1] if indice > 0 else None
    proxima = PARTES[indice + 1] if indice < len(PARTES) - 1 else None
    return previa, proxima


def obras_de_la_parte(clases):
    """Obras que aparecen en las clases de la parte, de la más usada a la menos.

    Se cuentan clases, no citas, e incluye el núcleo pedagógico, que aparece al
    pie de todas: el lector tiene que ver la lista completa de lo que sostiene
    la parte, no sólo lo que se citó de forma explícita.
    """
    veces = {}
    for clase in clases:
        for clave in set(list(clase["libros"]) + list(bib.NUCLEO_PEDAGOGICO)):
            veces[clave] = veces.get(clave, 0) + 1
    return sorted(veces.items(), key=lambda kv: (-kv[1], bib.obra(kv[0])))


def render_readme(parte, clases):
    """Índice de la parte, escrito para leerse.

    Antes esto era una sucesión de encabezados con listas y tablas debajo.
    Quien llega a una parte necesita entender qué se estudia aquí, por qué
    aparece en este punto del programa y sobre qué obras se apoya lo que va a
    leer; nada de eso cabe en una tabla de metadatos.
    """
    num = parte["num"]
    previa, proxima = vecinas(parte)
    horas = len(clases) * 25 // 10

    if previa:
        de_donde = ("Llegas desde la parte {}, *{}*, y lo que allí quedó resuelto se da por sabido "
                    "aquí.".format(previa["num"], previa["titulo"]))
    else:
        de_donde = ("Es la primera parte del programa: no supone nada previo salvo la disposición a "
                    "escribir lo que se decide.")
    if proxima:
        a_donde = ("Lo que produzcas aquí es material de entrada para la parte {}, *{}*."
                   .format(proxima["num"], proxima["titulo"]))
    else:
        a_donde = "Es la última parte: aquí se cierra el programa y se defiende el Capstone."

    lineas = [
        "# Parte {} — {}".format(num, parte["titulo"]),
        "",
        "Esta parte trabaja el nivel **{}** del programa y su propósito es que llegues a poder "
        "**{}**. {} {}".format(parte["nivel"], parte["resultado"], de_donde, a_donde),
        "",
        "Son {} clases, alrededor de {} horas de estudio dirigido, y todas empujan hacia la misma "
        "pregunta:".format(len(clases), horas),
        "",
        "> **{}**".format(parte["pregunta"]),
        "",
        "Esa pregunta no es retórica: al final de la parte tienes que poder responderla con un "
        "artefacto en la mano —{}— y no con una opinión.".format(parte["artefacto"]),
        "",
        "## Sobre qué caso vas a trabajar",
        "",
        parte["caso"],
        "",
        "Todo el programa ocurre en la misma empresa, **{}**: {} Trabajar siempre sobre el mismo "
        "caso permite comparar decisiones tomadas en partes distintas y ver cuáles se contradicen "
        "entre sí.".format(EMPRESA["nombre"], EMPRESA["descripcion"]),
        "",
        "## Qué vas a saber hacer",
        "",
        "Las competencias que se desarrollan aquí son {}. Con ellas la parte habilita para el "
        "trabajo de {}, que es donde estas decisiones se toman de verdad.".format(
            enum_es(["**{}**".format(c) for c in parte["competencias"]]),
            enum_es(parte["roles"])),
        "",
        "## Cómo avanza la parte, clase a clase",
        "",
        "Las clases van en orden y cada una supone la anterior. Esta es la secuencia y los "
        "conceptos que introduce cada sesión:",
        "",
        "| # | Clase | Conceptos que introduce |",
        "|---|---|---|",
    ]
    for clase in clases:
        conceptos = ", ".join(c[0] for c in clase["conceptos"][:3])
        lineas.append("| {} | [{}](class-{}-{}.md) | {} |".format(
            clase["n"], clase["titulo"], clase["n"], clase["slug"], conceptos))

    lineas += [
        "",
        "## Dónde se practica y cómo se evalúa",
        "",
        "Leer la parte no la acredita. Los [laboratorios](../../labs/part-{}/) te hacen ejecutar el "
        "método sobre el caso; la [evaluación de la parte](../../assessments/part-{}-assessment.md) "
        "comprueba que puedes sostener las decisiones sin el material delante; el "
        "[caso extendido](../../cases/) exige integrar lo aprendido en una recomendación completa, "
        "y en [`templates/`](../../templates/) están los formatos que se usan para producir el "
        "artefacto. El resultado que va a tu portafolio es **{}**.".format(
            num, num, parte["artefacto"]),
        "",
        "## Qué puede salir mal",
        "",
        "{} Antes de llevar cualquier recomendación de esta parte a una operación real, revisa el "
        "[mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) y las "
        "[reglas sobre datos personales](../../docs/DATOS-PERSONALES-Y-ETICA.md): la norma vigente "
        "manda sobre el material pedagógico.".format(parte["riesgo"]),
        "",
        "## Bibliografía de la parte",
        "",
        "Estas son las obras sobre las que se apoya la parte, con lo que aporta cada una y en "
        "cuántas de sus {} clases aparece. Está comprobado que cada obra existe y cuál es la "
        "edición —el título enlaza a su localizador—; que la idea atribuida esté en el capítulo "
        "que indica cada clase es la lectura del programa y está para que la contrastes. La "
        "columna «Acceso» dice de antemano qué puedes leer sin pagar.".format(len(clases)),
        "",
        "| Obra | Qué aporta | Clases | Localizador | Acceso |",
        "|---|---|---:|---|---|",
    ]
    for clave, veces in obras_de_la_parte(clases):
        autor, obra, edicion, lente, _cat = bib.LIBROS[clave]
        lineas.append("| {} — {} ({}) | {} | {} | {} | {} |".format(
            autor, enlace(clave, "*{}*".format(obra)), edicion, lente, veces,
            etiqueta(clave), acceso_legible(clave)))

    rectoras = [k for k in parte["libros"]]
    lineas += [
        "",
        "De todas ellas, las que ordenan el criterio de esta parte son {}. Si sólo puedes leer una, "
        "empieza por {}.".format(
            enum_es(["{} (*{}*)".format(bib.autor(k), bib.obra(k)) for k in rectoras]),
            "{} — *{}*".format(bib.autor(rectoras[0]), bib.obra(rectoras[0]))),
        "",
        "La bibliografía completa del programa, con el uso de cada obra clase a clase, está en "
        "[`docs/BIBLIOGRAFIA.md`](../../docs/BIBLIOGRAFIA.md); el registro con los localizadores "
        "comprobables, en [`sources/bibliography.json`](../../sources/bibliography.json).",
        "",
        "---",
        "",
        "[⬅ Índice del currículo](../README.md) · [Programa](../../README.md)",
        "",
    ]
    return "\n".join(lineas)


def render_indice_curriculo(datos):
    lineas = [
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
            # Los metadatos que antes iban en el front matter de cada clase
            # viven aquí. Es su sitio: una tabla de campos técnicos encima del
            # título no le sirve a quien lee, y aquí sí la puede leer una
            # máquina sin ensuciar el documento.
            "clases": [{
                "n": c["n"],
                "slug": c["slug"],
                "titulo": c["titulo"],
                "nivel": parte["nivel"],
                "estandar": VERSION_ESTANDAR,
                "idioma": "es",
                "umbral_aprobacion": 80,
                "minutos_estimados": 150,
                "conceptos": [t for t, _ in c["conceptos"]],
                "senales": [s for s, _ in c["senales"]],
                "libros": c["libros"],
                "anclajes": ANCLAJES["{}.{}".format(parte["num"], c["n"])],
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
