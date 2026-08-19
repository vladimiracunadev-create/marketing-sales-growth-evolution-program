---
title: "IA en customer success"
type: class
language: es
standard: clase-profunda-v2
part: 21
class: 11
level: IA y expansión
mastery_threshold: 80
estimated_minutes: 150
sources: ["mehta", "dixon-effort", "provost", "nist-airmf"]
anchors: {"dixon-effort": "resolucion-siguiente", "mehta": "salud", "nist-airmf": "caracteristicas", "provost": "evaluacion"}
updated: 2026-08-19
---

# Clase 21.11 — IA en customer success

**Parte 21 · IA aplicada a marketing, ventas y servicio** · Nivel: IA y expansión · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 21.10 — *Inteligencia de conversaciones*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de precisión de la predicción de baja para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El puntaje de salud construido con uso, resultado y relación, validado contra bajas — Nick Mehta, Dan Steinman y Lincoln Murphy. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

En éxito de cliente la IA se usa para predecir riesgo de baja, priorizar cartera y asistir respuestas. Su riesgo específico es la automatización de la empatía: responder con un sistema las consultas de un cliente frustrado suele empeorar la situación. La regla práctica es automatizar el diagnóstico y la priorización, y mantener humana la conversación difícil.

El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta. La parte 21 busca **usar IA como capacidad operativa con evaluación, control y responsabilidad humana**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **IA en customer success** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué tarea mejora con IA, cómo sé que mejora y quién responde cuando falla?

Los conceptos que estructuran la sesión son **predicción de riesgo**, **priorización de cartera**, **automatización de la respuesta** y **momento de escalamiento**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `predicción de riesgo`, `priorización de cartera`, `automatización de la respuesta` y `momento de escalamiento` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **IA aplicada a marketing, ventas y servicio**.
3. **Aplicar** la secuencia **usar modelos para predecir y priorizar → definir el momento de escalamiento a una persona → mantener humana la conversación de riesgo o reclamo → medir efecto en retención y en satisfacción → revisar los casos escalados para corregir el diseño** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **precisión de la predicción de baja**, **tasa de escalamiento a persona** y **satisfacción por tipo de atención** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **predicción de riesgo** y **priorización de cartera** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **precisión de la predicción de baja**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **predicción de riesgo** | estimación automatizada de la probabilidad de baja de una cuenta | Da un hecho compatible con la definición y otro que la refute. |
| **priorización de cartera** | ordenamiento de cuentas por riesgo y valor para asignar atención | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **automatización de la respuesta** | sustitución de la interacción humana por un sistema | Construye un caso límite donde el concepto se confunde con el anterior. |
| **momento de escalamiento** | condición que obliga a que una persona tome la conversación | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. usar modelos para predecir y priorizar → 2. definir el momento de escalamiento a una persona → 3. mantener humana la conversación de riesgo o reclamo → 4. medir efecto en retención y en satisfacción → 5. revisar los casos escalados para corregir el diseño
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un modelo predictivo sin capacidad de intervención sólo anticipa la pérdida. La predicción debe estar acompañada de una acción posible y de capacidad para ejecutarla.

## 📖 Desarrollo

### 1. Predicción de riesgo: mecanismo central

**Predicción de riesgo** se entiende aquí como **estimación automatizada de la probabilidad de baja de una cuenta**.

Aplicar modelos predictivos al éxito de cliente permite anticipar riesgo de baja y priorizar la atención. Su utilidad depende de dos condiciones: que la predicción llegue con tiempo suficiente para intervenir y que exista una intervención disponible. Un modelo que predice bien lo inevitable no aporta nada.

**De dónde viene esta afirmación.** Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) aporta la idea que sostiene este bloque: el puntaje de salud construido con uso, resultado y relación, validado contra bajas. Búscala en los capítulos sobre health score. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «precisión de la predicción de baja» debería moverse cuando cambie **predicción de riesgo**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **priorización de cartera**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Priorización de cartera: frontera conceptual y error de clasificación

**Definición operacional:** ordenamiento de cuentas por riesgo y valor para asignar atención. Su valor está en distinguirlo de **predicción de riesgo**.

La priorización de cartera es el uso más valioso: con capacidad limitada, atender primero a quien más lo necesita y donde la intervención puede cambiar el resultado. Eso exige combinar la probabilidad de baja con el valor de la cuenta y con la probabilidad de que la intervención funcione, que es el factor que casi nunca se modela.

**Contraste bibliográfico.** Matthew Dixon, Nick Toman y Rick DeLisi — *The Effortless Experience* (2013) aporta aquí una distinción concreta: la resolución del siguiente problema previsible en el mismo contacto (los capítulos sobre resolución anticipada). Formula dos mini-casos: uno que satisface la definición de **priorización de cartera** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «definir el momento de escalamiento a una persona», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Automatización de la respuesta: operacionalización y medición

**Automatización de la respuesta** significa **sustitución de la interacción humana por un sistema**.

La automatización de la respuesta tiene un límite claro: una cuenta en riesgo que recibe un correo automático percibe exactamente lo contrario de lo que la intervención pretendía. La automatización sirve para detectar y para preparar, no para responder en situaciones donde la relación está deteriorada.

Ficha de medición obligatoria para **precisión de la predicción de baja**: `bajas correctamente anticipadas, sobre bajas del periodo`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) pone una condición sobre la medición: la evaluación contra una línea base y no contra la nada (los capítulos sobre evaluación de modelos). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Momento de escalamiento: trade-offs y efectos de segundo orden

**Definición:** condición que obliga a que una persona tome la conversación.

Confiar más en el modelo libera tiempo de análisis y arriesga desatender cuentas que el modelo clasifica como seguras. Esa profecía autocumplida es un riesgo real: si nadie visita a las cuentas de bajo riesgo, algunas se volverán de alto riesgo sin que el modelo lo detecte hasta tarde.

**Lo que aporta la fuente.** NIST — *AI Risk Management Framework 1.0* (2023) aporta el criterio para pesar el intercambio: las características de un sistema de IA confiable, incluidas trazabilidad y responsabilidad (la sección sobre confiabilidad). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **satisfacción por tipo de atención** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **momento de escalamiento** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar los casos escalados para corregir el diseño», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El momento de escalamiento a una persona debe estar definido: qué nivel de riesgo, qué valor de cuenta o qué tipo de señal obliga a que intervenga alguien con autoridad. Sin esa regla, las situaciones graves se gestionan con el mismo procedimiento automatizado que las rutinarias, y el resultado es previsible.

**Frontera declarada.** Un modelo predictivo sin capacidad de intervención sólo anticipa la pérdida. La predicción debe estar acompañada de una acción posible y de capacidad para ejecutarla. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar IA en customer success no consiste en sumar definiciones. Empieza por **predicción de riesgo**, contrasta **priorización de cartera** con **automatización de la respuesta**, incorpora **momento de escalamiento** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) | El puntaje de salud construido con uso, resultado y relación, validado contra bajas | Los capítulos sobre health score | ¿Qué debería observarse en **predicción de riesgo** si aquí opera «el puntaje de salud construido con uso, resultado y relación, validado contra bajas»? ¿Y qué observación lo desmentiría en este caso? |
| Matthew Dixon, Nick Toman y Rick DeLisi — *The Effortless Experience* (2013) | La resolución del siguiente problema previsible en el mismo contacto | Los capítulos sobre resolución anticipada | ¿Qué debería observarse en **priorización de cartera** si aquí opera «la resolución del siguiente problema previsible en el mismo contacto»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La evaluación contra una línea base y no contra la nada | Los capítulos sobre evaluación de modelos | ¿Qué debería observarse en **automatización de la respuesta** si aquí opera «la evaluación contra una línea base y no contra la nada»? ¿Y qué observación lo desmentiría en este caso? |
| NIST — *AI Risk Management Framework 1.0* (2023) | Las características de un sistema de IA confiable, incluidas trazabilidad y responsabilidad | La sección sobre confiabilidad | ¿Qué debería observarse en **momento de escalamiento** si aquí opera «las características de un sistema de IA confiable, incluidas trazabilidad y responsabilidad»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El asistente automático de Ruta Andina respondió tres veces con el mismo texto a un cliente que llevaba dos semanas sin poder facturar. El cliente se dio de baja.

**Paso 1 — Usar modelos para predecir y priorizar.** El equipo escribe primero el supuesto asociado a **predicción de riesgo** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **precisión de la predicción de baja** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Definir el momento de escalamiento a una persona.** El trabajo aquí es separar lo observado de lo inferido sobre **priorización de cartera**. La evidencia que ordena la discusión es **tasa de escalamiento a persona**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Mantener humana la conversación de riesgo o reclamo.** El riesgo de este paso es cerrar demasiado rápido alrededor de **automatización de la respuesta**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **satisfacción por tipo de atención** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Medir efecto en retención y en satisfacción.** Con **momento de escalamiento** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **precisión de la predicción de baja** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar los casos escalados para corregir el diseño.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **predicción de riesgo**. **tasa de escalamiento a persona** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **predicción de riesgo** | Estimación automatizada de la probabilidad de baja de una cuenta | Cuando **precisión de la predicción de baja** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **priorización de cartera** | Ordenamiento de cuentas por riesgo y valor para asignar atención | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un modelo predictivo sin capacidad de intervención sólo anticipa la pérdida. La predicción debe estar acompañada de una acción posible y de capacidad para ejecutarla.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre IA en customer success |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager con IA, RevOps, Marketing manager y Sales enablement. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El asistente automático de Ruta Andina respondió tres veces con el mismo texto a un cliente que llevaba dos semanas sin poder facturar. El cliente se dio de baja.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **usar modelos para predecir y priorizar → definir el momento de escalamiento a una persona → mantener humana la conversación de riesgo o reclamo → medir efecto en retención y en satisfacción → revisar los casos escalados para corregir el diseño** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **precisión de la predicción de baja**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Customer Success* y la de *The Effortless Experience*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **predicción de riesgo** y **priorización de cartera** como sinónimos | Se perdió la distinción entre «estimación automatizada de la probabilidad de baja de una cuenta» y «ordenamiento de cuentas por riesgo y valor para asignar atención» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar los casos escalados para corregir el diseño» | Se saltó «usar modelos para predecir y priorizar»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **precisión de la predicción de baja** | La métrica local reemplazó al resultado del sistema | Contrástala con **satisfacción por tipo de atención** y explicita el costo de oportunidad. |
| Automatizar la conversación con clientes en riesgo | Error específico de esta clase | Define el escalamiento obligatorio a una persona ante señales de frustración o de riesgo. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **predicción de riesgo** y **priorización de cartera** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **automatización de la respuesta** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «usar modelos para predecir y priorizar» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **precisión de la predicción de baja** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un modelo predictivo sin capacidad de intervención sólo anticipa la pérdida. La predicción debe estar acompañada de una acción posible y de capacidad para ejecutarla»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **automatización de la respuesta** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **precisión de la predicción de baja**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Customer Success* y *AI Risk Management Framework 1.0*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P21-C11-ia-en-customer-success/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **precisión de la predicción de baja**, **tasa de escalamiento a persona** y **satisfacción por tipo de atención** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **operating model humano-IA con casos de uso, evaluaciones, guardrails y registro de incidentes**.

## ✅ Evaluación de la clase

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables entre los conceptos de la clase. |
| Diagnóstico y evidencia | 30 % | Datos pertinentes, línea base, supuestos explícitos y límites del dato. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas y argumento ejecutivo trazable. |

**Aprobación:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambios a otra clase se considera insuficiente.

## 📗 Fuentes y verificación

Cada obra aparece con la idea concreta que aporta a esta clase. Si al leer no encuentras esa idea, la cita está mal puesta y corresponde reportarlo como error del material.

- Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) — **aporta a esta clase:** el puntaje de salud construido con uso, resultado y relación, validado contra bajas. **Dónde buscarlo:** los capítulos sobre health score. Registra edición y páginas consultadas en tu nota de lectura.
- Matthew Dixon, Nick Toman y Rick DeLisi — *The Effortless Experience* (2013) — **aporta a esta clase:** la resolución del siguiente problema previsible en el mismo contacto. **Dónde buscarlo:** los capítulos sobre resolución anticipada. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — **aporta a esta clase:** la evaluación contra una línea base y no contra la nada. **Dónde buscarlo:** los capítulos sobre evaluación de modelos. Registra edición y páginas consultadas en tu nota de lectura.
- NIST — *AI Risk Management Framework 1.0* (2023) — **aporta a esta clase:** las características de un sistema de IA confiable, incluidas trazabilidad y responsabilidad. **Dónde buscarlo:** la sección sobre confiabilidad. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 10 · Inteligencia de conversaciones](class-10-conversation-intelligence.md) · [Índice de la parte](README.md) · [Clase 12 · Evaluación y guardrails](class-12-evaluacion-y-guardrails.md) →
