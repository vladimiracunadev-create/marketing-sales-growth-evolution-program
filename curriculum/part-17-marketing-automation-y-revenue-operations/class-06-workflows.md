---
title: "Workflows"
type: class
language: es
standard: clase-profunda-v2
part: 17
class: 06
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["diorio", "grove", "nist-airmf", "provost"]
anchors: {"diorio": "friccion", "grove": "delegacion", "nist-airmf": "funciones", "provost": "formulacion"}
updated: 2026-08-19
---

# Clase 17.06 — Workflows

Clase 6 de 14 de la parte [17 — Marketing automation y revenue operations](README.md), de nivel Operación de ingresos. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 17.05, *Nurturing*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de flujos documentados con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La fricción en los traspasos entre áreas como pérdida medible de ingreso — Stephen G. Diorio y Chris K. Hummel. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Un flujo automatizado es código que actúa sobre clientes. Como todo código, necesita documentación, control de versiones, pruebas y un responsable. La práctica habitual —crear flujos sin registro, sin pruebas y sin dueño— produce sistemas donde nadie sabe por qué un cliente recibió un mensaje y nadie puede corregirlo con seguridad.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 17 busca **integrar marketing, ventas y servicio en un solo modelo de datos y de proceso**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **workflows** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué automatizo porque mejora el sistema y qué estaría solo escalando un desorden?

Los conceptos que estructuran la sesión son **condición de entrada**, **condición de salida**, **prueba en ambiente controlado** y **documentación del flujo**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `condición de entrada`, `condición de salida`, `prueba en ambiente controlado` y `documentación del flujo` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Marketing automation y revenue operations**.
3. **Aplicar** la secuencia **documentar propósito y condiciones antes de construir → probar con registros de prueba → activar con volumen limitado y monitoreo → registrar responsable y fecha de revisión → auditar flujos activos cada semestre y retirar los obsoletos** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **flujos documentados**, **flujos sin responsable** y **errores detectados en pruebas** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **condición de entrada** y **condición de salida** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **flujos documentados**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **condición de entrada** | criterio que determina qué registros ingresan al flujo | Da un hecho compatible con la definición y otro que la refute. |
| **condición de salida** | criterio que retira al registro del flujo | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **prueba en ambiente controlado** | verificación del comportamiento antes de activar sobre datos reales | Construye un caso límite donde el concepto se confunde con el anterior. |
| **documentación del flujo** | registro de propósito, condiciones, responsable y fecha de revisión | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. documentar propósito y condiciones antes de construir → 2. probar con registros de prueba → 3. activar con volumen limitado y monitoreo → 4. registrar responsable y fecha de revisión → 5. auditar flujos activos cada semestre y retirar los obsoletos
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Probar todos los casos límite es imposible. El control complementario es el monitoreo posterior y la capacidad de detener el flujo rápidamente.

## 📖 Desarrollo

### 1. Condición de entrada: mecanismo central

**Condición de entrada** se entiende aquí como **criterio que determina qué registros ingresan al flujo**.

Un flujo automatizado se define por sus condiciones de entrada y de salida, y ambas deben ser explícitas. Un flujo sin condición de salida clara puede mantener a una persona recibiendo comunicaciones indefinidamente, incluso después de haberse convertido en cliente, que es una de las fallas más visibles para quien la sufre.

**De dónde viene esta afirmación.** Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) aporta la idea que sostiene este bloque: la fricción en los traspasos entre áreas como pérdida medible de ingreso. Búscala en los capítulos sobre procesos de ingreso. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «flujos documentados» debería moverse cuando cambie **condición de entrada**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **condición de salida**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Condición de salida: frontera conceptual y error de clasificación

**Definición operacional:** criterio que retira al registro del flujo. Su valor está en distinguirlo de **condición de entrada**.

La prueba en ambiente controlado antes de activar es una práctica básica y frecuentemente omitida por presión de tiempo. Consiste en ejecutar el flujo con registros de prueba que cubran los casos límite: dato faltante, condición cumplida dos veces, persona ya en otro flujo. Esa prueba toma horas y evita incidentes que toman semanas de reparación.

**Contraste bibliográfico.** Andrew S. Grove — *High Output Management* (1983) aporta aquí una distinción concreta: la delegación con nivel de supervisión ajustado a la madurez de la tarea (los capítulos sobre madurez relevante a la tarea). Formula dos mini-casos: uno que satisface la definición de **condición de salida** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «probar con registros de prueba», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Prueba en ambiente controlado: operacionalización y medición

**Prueba en ambiente controlado** significa **verificación del comportamiento antes de activar sobre datos reales**.

La documentación del flujo debe existir fuera de la herramienta: qué hace, por qué se creó, quién lo pidió, qué se espera de él y cuándo revisarlo. Sin esa documentación, en dos años nadie sabrá si un flujo activo sigue siendo necesario, y la opción cómoda —dejarlo— es la que acumula deuda.

Ficha de medición obligatoria para **flujos documentados**: `automatizaciones con documentación completa, sobre automatizaciones activas`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** NIST — *AI Risk Management Framework 1.0* (2023) pone una condición sobre la medición: las cuatro funciones: mapear, medir, gestionar y gobernar el riesgo de IA (el núcleo del marco). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Documentación del flujo: trade-offs y efectos de segundo orden

**Definición:** registro de propósito, condiciones, responsable y fecha de revisión.

Flujos más elaborados cubren más casos y son más difíciles de depurar y de modificar. Flujos simples se entienden y dejan casos sin cubrir. La recomendación práctica es preferir varios flujos simples y documentados a uno complejo con muchas ramas, aunque la segunda opción parezca más elegante.

**Lo que aporta la fuente.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta el criterio para pesar el intercambio: la formulación del problema de negocio como problema de datos antes de elegir técnica (los capítulos iniciales sobre pensamiento analítico). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **errores detectados en pruebas** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **documentación del flujo** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «auditar flujos activos cada semestre y retirar los obsoletos», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Toda automatización que se comunica con personas debe tener un responsable identificable y un mecanismo de detención inmediata. Cuando ocurre un error, la pregunta «quién puede apagar esto» debe tener respuesta en segundos. Verificarlo antes de activar es parte del procedimiento y no una formalidad.

**Frontera declarada.** Probar todos los casos límite es imposible. El control complementario es el monitoreo posterior y la capacidad de detener el flujo rápidamente. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar workflows no consiste en sumar definiciones. Empieza por **condición de entrada**, contrasta **condición de salida** con **prueba en ambiente controlado**, incorpora **documentación del flujo** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) | La fricción en los traspasos entre áreas como pérdida medible de ingreso | Los capítulos sobre procesos de ingreso | ¿Qué debería observarse en **condición de entrada** si aquí opera «la fricción en los traspasos entre áreas como pérdida medible de ingreso»? ¿Y qué observación lo desmentiría en este caso? |
| Andrew S. Grove — *High Output Management* (1983) | La delegación con nivel de supervisión ajustado a la madurez de la tarea | Los capítulos sobre madurez relevante a la tarea | ¿Qué debería observarse en **condición de salida** si aquí opera «la delegación con nivel de supervisión ajustado a la madurez de la tarea»? ¿Y qué observación lo desmentiría en este caso? |
| NIST — *AI Risk Management Framework 1.0* (2023) | Las cuatro funciones: mapear, medir, gestionar y gobernar el riesgo de IA | El núcleo del marco | ¿Qué debería observarse en **prueba en ambiente controlado** si aquí opera «las cuatro funciones: mapear, medir, gestionar y gobernar el riesgo de IA»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La formulación del problema de negocio como problema de datos antes de elegir técnica | Los capítulos iniciales sobre pensamiento analítico | ¿Qué debería observarse en **documentación del flujo** si aquí opera «la formulación del problema de negocio como problema de datos antes de elegir técnica»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina tiene 14 automatizaciones activas. Dos envían el mismo correo, una nunca se desactivó tras una campaña de 2025 y ninguna tiene responsable.

**Paso 1 — Documentar propósito y condiciones antes de construir.** El equipo escribe primero el supuesto asociado a **condición de entrada** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **flujos documentados** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Probar con registros de prueba.** El trabajo aquí es separar lo observado de lo inferido sobre **condición de salida**. La evidencia que ordena la discusión es **flujos sin responsable**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Activar con volumen limitado y monitoreo.** El riesgo de este paso es cerrar demasiado rápido alrededor de **prueba en ambiente controlado**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **errores detectados en pruebas** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Registrar responsable y fecha de revisión.** Con **documentación del flujo** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **flujos documentados** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Auditar flujos activos cada semestre y retirar los obsoletos.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **condición de entrada**. **flujos sin responsable** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **condición de entrada** | Criterio que determina qué registros ingresan al flujo | Cuando **flujos documentados** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **condición de salida** | Criterio que retira al registro del flujo | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Probar todos los casos límite es imposible. El control complementario es el monitoreo posterior y la capacidad de detener el flujo rápidamente.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre workflows |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing ops, RevOps manager y Sales ops. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina tiene 14 automatizaciones activas. Dos envían el mismo correo, una nunca se desactivó tras una campaña de 2025 y ninguna tiene responsable.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **documentar propósito y condiciones antes de construir → probar con registros de prueba → activar con volumen limitado y monitoreo → registrar responsable y fecha de revisión → auditar flujos activos cada semestre y retirar los obsoletos** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **flujos documentados**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Revenue Operations* y la de *High Output Management*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **condición de entrada** y **condición de salida** como sinónimos | Se perdió la distinción entre «criterio que determina qué registros ingresan al flujo» y «criterio que retira al registro del flujo» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «auditar flujos activos cada semestre y retirar los obsoletos» | Se saltó «documentar propósito y condiciones antes de construir»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **flujos documentados** | La métrica local reemplazó al resultado del sistema | Contrástala con **errores detectados en pruebas** y explicita el costo de oportunidad. |
| Activar flujos sin prueba ni responsable | Error específico de esta clase | Exige documentación, prueba controlada y dueño asignado antes de activar cualquier flujo. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **condición de entrada** y **condición de salida** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **prueba en ambiente controlado** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «documentar propósito y condiciones antes de construir» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **flujos documentados** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Probar todos los casos límite es imposible. El control complementario es el monitoreo posterior y la capacidad de detener el flujo rápidamente»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **prueba en ambiente controlado** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **flujos documentados**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Revenue Operations* y *Data Science for Business*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P17-C06-workflows/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **flujos documentados**, **flujos sin responsable** y **errores detectados en pruebas** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **operating model de RevOps con lifecycle, scoring, SLA, integraciones y observabilidad**.

## ✅ Evaluación de la clase

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables entre los conceptos de la clase. |
| Diagnóstico y evidencia | 30 % | Datos pertinentes, línea base, supuestos explícitos y límites del dato. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas y argumento ejecutivo trazable. |

**Aprobación:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambios a otra clase se considera insuficiente.

## 📗 Fuentes y verificación

Estas son las obras sobre las que se apoya lo que acabas de leer. Cada una aparece con la idea concreta que aporta a esta clase, dónde buscarla dentro del libro y el enlace donde se resuelve la edición exacta. Si al leer no encuentras esa idea, la cita está mal puesta y corresponde reportarlo como error del material.

- Stephen G. Diorio y Chris K. Hummel — [*Revenue Operations*](https://openlibrary.org/isbn/9781119871132) (2022) · ISBN 9781119871132 — **aporta a esta clase:** la fricción en los traspasos entre áreas como pérdida medible de ingreso. **Dónde buscarlo:** los capítulos sobre procesos de ingreso. Registra edición y páginas consultadas en tu nota de lectura.
- Andrew S. Grove — [*High Output Management*](https://openlibrary.org/isbn/9780394532349) (1983) · ISBN 9780394532349 — **aporta a esta clase:** la delegación con nivel de supervisión ajustado a la madurez de la tarea. **Dónde buscarlo:** los capítulos sobre madurez relevante a la tarea. Registra edición y páginas consultadas en tu nota de lectura.
- NIST — [*AI Risk Management Framework 1.0*](https://doi.org/10.6028/NIST.AI.100-1) (2023) · DOI 10.6028/NIST.AI.100-1 — **aporta a esta clase:** las cuatro funciones: mapear, medir, gestionar y gobernar el riesgo de IA. **Dónde buscarlo:** el núcleo del marco. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) · ISBN 9781449374280 — **aporta a esta clase:** la formulación del problema de negocio como problema de datos antes de elegir técnica. **Dónde buscarlo:** los capítulos iniciales sobre pensamiento analítico. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 05 · Nurturing](class-05-nurturing.md) · [Índice de la parte](README.md) · [Clase 07 · Acuerdo de servicio entre marketing y ventas](class-07-sla-marketing-ventas.md) →
