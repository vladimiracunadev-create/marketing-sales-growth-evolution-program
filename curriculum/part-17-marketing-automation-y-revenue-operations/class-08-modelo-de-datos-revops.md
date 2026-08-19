---
title: "Modelo de datos de RevOps"
type: class
language: es
standard: clase-profunda-v2
part: 17
class: 08
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["diorio", "provost", "roberge", "kaplan-norton"]
anchors: {"diorio": "modelo-datos", "kaplan-norton": "traduccion", "provost": "formulacion", "roberge": "metricas-coaching"}
updated: 2026-08-19
---

# Clase 17.08 — Modelo de datos de RevOps

Clase 8 de 14 de la parte [17 — Marketing automation y revenue operations](README.md), de nivel Operación de ingresos. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 17.07, *Acuerdo de servicio entre marketing y ventas*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de datos con fuente autoritativa definida con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El modelo de datos común como condición para que las áreas discutan sobre lo mismo — Stephen G. Diorio y Chris K. Hummel. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

El modelo de datos es la infraestructura invisible de las decisiones comerciales. Define qué entidades existen, cómo se relacionan, qué estados son válidos y de dónde proviene cada dato. Cuando no está diseñado, cada informe requiere reconciliación manual y cada pregunta nueva exige un proyecto. Diseñarlo es más barato que rehacerlo después de tres años de deuda.

El punto de partida de esta clase no es la definición sino la decisión que la definición debe mejorar. La parte 17 busca **integrar marketing, ventas y servicio en un solo modelo de datos y de proceso**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **modelo de datos de RevOps** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué automatizo porque mejora el sistema y qué estaría solo escalando un desorden?

Los conceptos que estructuran la sesión son **entidad**, **fuente autoritativa**, **estado válido** y **deuda de datos**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `entidad`, `fuente autoritativa`, `estado válido` y `deuda de datos` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Marketing automation y revenue operations**.
3. **Aplicar** la secuencia **inventariar entidades y sistemas actuales → definir la fuente autoritativa de cada dato → documentar estados válidos y transiciones → resolver las inconsistencias más costosas primero → establecer el proceso de cambio del modelo** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **datos con fuente autoritativa definida**, **inconsistencias entre sistemas** y **tiempo de respuesta a preguntas nuevas** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **entidad** y **fuente autoritativa** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **datos con fuente autoritativa definida**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **entidad** | objeto del modelo que representa algo real: cuenta, contacto, oportunidad, suscripción | Construye un caso límite donde el concepto se confunde con el anterior. |
| **fuente autoritativa** | sistema que contiene la versión válida de cada dato | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **estado válido** | conjunto de valores permitidos para un campo y sus transiciones posibles | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **deuda de datos** | acumulación de inconsistencias que encarece cada análisis futuro | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. inventariar entidades y sistemas actuales → 2. definir la fuente autoritativa de cada dato → 3. documentar estados válidos y transiciones → 4. resolver las inconsistencias más costosas primero → 5. establecer el proceso de cambio del modelo
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un modelo perfecto que exige rehacer todos los sistemas no se implementa. El diseño debe priorizar lo que produce más valor con menos disrupción.

## 📖 Desarrollo

### 1. Entidad: mecanismo central

**Entidad** se entiende aquí como **objeto del modelo que representa algo real: cuenta, contacto, oportunidad, suscripción**.

El modelo de datos de ingresos define qué entidades existen, cómo se relacionan y cuál es la fuente autoritativa de cada dato. Es la decisión de arquitectura con mayor efecto sobre la capacidad analítica de la organización, y suele tomarse implícitamente al configurar la primera herramienta.

**De dónde viene esta afirmación.** Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) aporta la idea que sostiene este bloque: el modelo de datos común como condición para que las áreas discutan sobre lo mismo. Búscala en los capítulos sobre infraestructura de datos comercial. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «datos con fuente autoritativa definida» debería moverse cuando cambie **entidad**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **fuente autoritativa**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Fuente autoritativa: frontera conceptual y error de clasificación

**Definición operacional:** sistema que contiene la versión válida de cada dato. Su valor está en distinguirlo de **entidad**.

La fuente autoritativa debe ser única por dato: si el ingreso puede consultarse en el CRM, en facturación y en una planilla, las tres cifras diferirán y ninguna será confiable. Declarar cuál manda y hacer que las demás la reflejen es un trabajo tedioso que resuelve la mayoría de las discusiones sobre números.

**Contraste bibliográfico.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta aquí una distinción concreta: la formulación del problema de negocio como problema de datos antes de elegir técnica (los capítulos iniciales sobre pensamiento analítico). Formula dos mini-casos: uno que satisface la definición de **fuente autoritativa** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «definir la fuente autoritativa de cada dato», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Estado válido: operacionalización y medición

**Estado válido** significa **conjunto de valores permitidos para un campo y sus transiciones posibles**.

El estado válido de cada entidad debe estar definido y restringido: qué combinaciones de campos son posibles y cuáles no. Sin esas restricciones, el sistema acumula registros en estados imposibles —oportunidades cerradas sin fecha de cierre, cuentas activas sin contacto— que después distorsionan todo análisis.

Ficha de medición obligatoria para **datos con fuente autoritativa definida**: `campos críticos con fuente única declarada, sobre campos críticos`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Mark Roberge — *The Sales Acceleration Formula* (2015) pone una condición sobre la medición: el acompañamiento dirigido por una métrica diagnóstica por vendedor (los capítulos sobre la fórmula de gestión). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Deuda de datos: trade-offs y efectos de segundo orden

**Definición:** acumulación de inconsistencias que encarece cada análisis futuro.

Un modelo rico permite responder más preguntas y exige disciplina de registro y mantenimiento. Uno simple se sostiene y limita el análisis. La decisión debe partir de las preguntas de gestión efectivas y no de las capacidades de la herramienta, que siempre ofrecerán más de lo necesario.

**Lo que aporta la fuente.** Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) aporta el criterio para pesar el intercambio: la traducción de la estrategia en indicadores que la organización puede ejecutar (los capítulos sobre implantación). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **tiempo de respuesta a preguntas nuevas** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **deuda de datos** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «establecer el proceso de cambio del modelo», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La deuda de datos se acumula con cada excepción no resuelta y con cada campo agregado sin definición. Se paga con intereses cuando hay que migrar de sistema o construir un análisis nuevo. Medirla —proporción de registros con campos críticos vacíos o inconsistentes— la vuelve visible y gestionable.

**Frontera declarada.** Un modelo perfecto que exige rehacer todos los sistemas no se implementa. El diseño debe priorizar lo que produce más valor con menos disrupción. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar modelo de datos de RevOps no consiste en sumar definiciones. Empieza por **entidad**, contrasta **fuente autoritativa** con **estado válido**, incorpora **deuda de datos** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) | El modelo de datos común como condición para que las áreas discutan sobre lo mismo | Los capítulos sobre infraestructura de datos comercial | ¿Qué debería observarse en **entidad** si aquí opera «el modelo de datos común como condición para que las áreas discutan sobre lo mismo»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La formulación del problema de negocio como problema de datos antes de elegir técnica | Los capítulos iniciales sobre pensamiento analítico | ¿Qué debería observarse en **fuente autoritativa** si aquí opera «la formulación del problema de negocio como problema de datos antes de elegir técnica»? ¿Y qué observación lo desmentiría en este caso? |
| Mark Roberge — *The Sales Acceleration Formula* (2015) | El acompañamiento dirigido por una métrica diagnóstica por vendedor | Los capítulos sobre la fórmula de gestión | ¿Qué debería observarse en **estado válido** si aquí opera «el acompañamiento dirigido por una métrica diagnóstica por vendedor»? ¿Y qué observación lo desmentiría en este caso? |
| Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) | La traducción de la estrategia en indicadores que la organización puede ejecutar | Los capítulos sobre implantación | ¿Qué debería observarse en **deuda de datos** si aquí opera «la traducción de la estrategia en indicadores que la organización puede ejecutar»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El ingreso recurrente de Ruta Andina existe en el CRM, en la plataforma de facturación y en una planilla. Los tres números difieren y ninguno está declarado como autoritativo.

**Paso 1 — Inventariar entidades y sistemas actuales.** El equipo escribe primero el supuesto asociado a **entidad** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **datos con fuente autoritativa definida** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Definir la fuente autoritativa de cada dato.** El trabajo aquí es separar lo observado de lo inferido sobre **fuente autoritativa**. La evidencia que ordena la discusión es **inconsistencias entre sistemas**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Documentar estados válidos y transiciones.** El riesgo de este paso es cerrar demasiado rápido alrededor de **estado válido**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **tiempo de respuesta a preguntas nuevas** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Resolver las inconsistencias más costosas primero.** Con **deuda de datos** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **datos con fuente autoritativa definida** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Establecer el proceso de cambio del modelo.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **entidad**. **inconsistencias entre sistemas** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **entidad** | Objeto del modelo que representa algo real: cuenta, contacto, oportunidad, suscripción | Cuando **datos con fuente autoritativa definida** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **fuente autoritativa** | Sistema que contiene la versión válida de cada dato | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un modelo perfecto que exige rehacer todos los sistemas no se implementa. El diseño debe priorizar lo que produce más valor con menos disrupción.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre modelo de datos de RevOps |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing ops, RevOps manager y Sales ops. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El ingreso recurrente de Ruta Andina existe en el CRM, en la plataforma de facturación y en una planilla. Los tres números difieren y ninguno está declarado como autoritativo.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **inventariar entidades y sistemas actuales → definir la fuente autoritativa de cada dato → documentar estados válidos y transiciones → resolver las inconsistencias más costosas primero → establecer el proceso de cambio del modelo** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **datos con fuente autoritativa definida**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Revenue Operations* y la de *Data Science for Business*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **entidad** y **fuente autoritativa** como sinónimos | Se perdió la distinción entre «objeto del modelo que representa algo real: cuenta, contacto, oportunidad, suscripción» y «sistema que contiene la versión válida de cada dato» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «establecer el proceso de cambio del modelo» | Se saltó «inventariar entidades y sistemas actuales»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **datos con fuente autoritativa definida** | La métrica local reemplazó al resultado del sistema | Contrástala con **tiempo de respuesta a preguntas nuevas** y explicita el costo de oportunidad. |
| Operar sin fuente autoritativa declarada | Error específico de esta clase | Define para cada dato crítico cuál sistema manda y documenta la regla de reconciliación. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **entidad** y **fuente autoritativa** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **estado válido** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «inventariar entidades y sistemas actuales» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **datos con fuente autoritativa definida** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un modelo perfecto que exige rehacer todos los sistemas no se implementa. El diseño debe priorizar lo que produce más valor con menos disrupción»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **estado válido** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **datos con fuente autoritativa definida**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Revenue Operations* y *The Balanced Scorecard*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, comprueba la norma en su texto vigente. Los enlaces van al texto completo publicado por la Biblioteca del Congreso Nacional; son gratuitos y no hace falta creerle a este material.

- **Consumo y comercio.** [Ley 19.496](https://www.bcn.cl/leychile/navegar?idNorma=61438) — *Establece normas sobre protección de los derechos de los consumidores* (Ministerio de Economía, Fomento y Reconstrucción), y su reglamento de comercio electrónico, [Decreto 6/2021](https://www.bcn.cl/leychile/navegar?idNorma=1165504) — *Aprueba reglamento de comercio electrónico* (Ministerio de Economía, Fomento y Turismo).
- **Datos personales.** [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales* (Ministerio Secretaría General de la Presidencia), que sustituye progresivamente a [Ley 19.628](https://www.bcn.cl/leychile/navegar?idNorma=141599) — *Sobre protección de la vida privada* (Ministerio Secretaría General de la Presidencia).
- **Derecho a retracto.** [Decreto 52/2024](https://www.bcn.cl/leychile/navegar?idNorma=1206144) — *Aprueba reglamento que regula la forma y condiciones en que los proveedores deberán comunicar la exclusión del derecho a retracto y los bienes en que excepcionalmente y por su naturaleza procederá tal exclusión* (Ministerio de Economía, Fomento y Turismo).

Dentro del repositorio, el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) ordena qué norma aplica a cada decisión comercial, [datos personales y ética](../../docs/DATOS-PERSONALES-Y-ETICA.md) desarrolla el tratamiento de datos y [fuentes oficiales](../../docs/FUENTES-OFICIALES.md) lista los organismos con su fecha de consulta. Ninguno de esos documentos reemplaza al texto legal.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P17-C08-modelo-de-datos-revops/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **datos con fuente autoritativa definida**, **inconsistencias entre sistemas** y **tiempo de respuesta a preguntas nuevas** con fuente, ventana y lectura prohibida.
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

Aquí conviene separar dos cosas que suelen ir juntas y no son lo mismo.

**Lo que está comprobado.** Que cada obra existe y cuál es exactamente la edición: el enlace resuelve su ISBN contra el catálogo de OpenLibrary, y eso se revalida periódicamente. Las normas chilenas citadas más arriba enlazan su texto completo y gratuito.

**Lo que es atribución del programa.** Que la idea señalada esté en el capítulo que se indica. Eso es la lectura que este material hace de cada obra, no una cita textual cotejada frase por frase, y se declara así de explícito para que puedas contrastarlo: si abres la obra y no encuentras la idea donde se dice, la cita está mal puesta y **corresponde reportarlo como error del material**. No se citan números de página porque cambian entre ediciones.

- Stephen G. Diorio y Chris K. Hummel — [*Revenue Operations*](https://openlibrary.org/isbn/9781119871132) (2022) · ISBN 9781119871132 — **aporta a esta clase:** el modelo de datos común como condición para que las áreas discutan sobre lo mismo. **Dónde buscarlo:** los capítulos sobre infraestructura de datos comercial. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) · ISBN 9781449374280 — **aporta a esta clase:** la formulación del problema de negocio como problema de datos antes de elegir técnica. **Dónde buscarlo:** los capítulos iniciales sobre pensamiento analítico. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Mark Roberge — [*The Sales Acceleration Formula*](https://openlibrary.org/isbn/9781119047018) (2015) · ISBN 9781119047018 — **aporta a esta clase:** el acompañamiento dirigido por una métrica diagnóstica por vendedor. **Dónde buscarlo:** los capítulos sobre la fórmula de gestión. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Robert S. Kaplan y David P. Norton — [*The Balanced Scorecard*](https://openlibrary.org/isbn/9780875846514) (1996) · ISBN 9780875846514 — **aporta a esta clase:** la traducción de la estrategia en indicadores que la organización puede ejecutar. **Dónde buscarlo:** los capítulos sobre implantación. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 07 · Acuerdo de servicio entre marketing y ventas](class-07-sla-marketing-ventas.md) · [Índice de la parte](README.md) · [Clase 09 · Integraciones](class-09-integraciones.md) →
