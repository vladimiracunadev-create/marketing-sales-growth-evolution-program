---
title: "Valor de vida del cliente"
type: class
language: es
standard: clase-profunda-v2
part: 20
class: 04
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["fader-ltv", "fader", "provost", "croll-yoskovitz"]
anchors: {"croll-yoskovitz": "cohortes", "fader": "heterogeneidad", "fader-ltv": "ltv-modelo", "provost": "sobreajuste"}
updated: 2026-08-19
---

# Clase 20.04 — Valor de vida del cliente

Clase 4 de 14 de la parte [20 — Analítica comercial y marketing science](README.md), de nivel Crecimiento y analítica. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 20.03, *Costo de adquisición de cliente*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de valor de vida por segmento con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El valor de vida como proyección con supuestos declarados y no como cifra única — Peter Fader y Sarah Toms. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

El valor de vida es una proyección del margen que un cliente aportará durante su relación. Sus componentes son margen, permanencia esperada y expansión, y cada uno introduce incertidumbre. Fader advierte contra el uso de fórmulas simples con supuestos de retención constante: la retención varía por cohorte y por segmento, y el promedio agregado distorsiona la estimación.

El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta. La parte 20 busca **sostener decisiones de ingreso con métricas correctamente construidas**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **valor de vida del cliente** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Esta cifra mide lo que creo que mide, y qué decisión cambiaría si estuviera equivocada?

Los conceptos que estructuran la sesión son **margen de contribución del cliente**, **permanencia esperada**, **heterogeneidad** y **tasa de descuento**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `margen de contribución del cliente`, `permanencia esperada`, `heterogeneidad` y `tasa de descuento` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Analítica comercial y marketing science**.
3. **Aplicar** la secuencia **calcular el margen de contribución con costos completos → estimar permanencia desde curvas de retención por cohorte → incorporar expansión y contracción observadas → aplicar tasa de descuento y declarar supuestos → presentar el resultado como rango y no como cifra única** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **valor de vida por segmento**, **dispersión dentro del segmento** y **sensibilidad a la retención** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **margen de contribución del cliente** y **permanencia esperada** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **valor de vida por segmento**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **margen de contribución del cliente** | ingreso menos costos variables de servirlo, por periodo | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **permanencia esperada** | duración estimada de la relación, derivada de curvas de retención | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **heterogeneidad** | diferencia sustantiva de valor entre clientes del mismo segmento aparente | Da un hecho compatible con la definición y otro que la refute. |
| **tasa de descuento** | ajuste que refleja el valor temporal del dinero en la proyección | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. calcular el margen de contribución con costos completos → 2. estimar permanencia desde curvas de retención por cohorte → 3. incorporar expansión y contracción observadas → 4. aplicar tasa de descuento y declarar supuestos → 5. presentar el resultado como rango y no como cifra única
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Con cohortes jóvenes, la proyección tiene error alto. Presentarla como cifra única induce decisiones de inversión sobre una precisión inexistente.

## 📖 Desarrollo

### 1. Margen de contribución del cliente: mecanismo central

**Margen de contribución del cliente** se entiende aquí como **ingreso menos costos variables de servirlo, por periodo**.

El valor de vida del cliente es una proyección y no un dato. Se construye con supuestos sobre margen, permanencia y comportamiento futuro, y su precisión depende por completo de la calidad de esos supuestos. Presentarlo como una cifra exacta oculta que es un modelo, y los modelos se discuten por sus supuestos.

**De dónde viene esta afirmación.** Peter Fader y Sarah Toms — *The Customer Centricity Playbook* (2018) aporta la idea que sostiene este bloque: el valor de vida como proyección con supuestos declarados y no como cifra única. Búscala en los capítulos sobre cálculo del valor de vida. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «valor de vida por segmento» debería moverse cuando cambie **margen de contribución del cliente**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **permanencia esperada**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Permanencia esperada: frontera conceptual y error de clasificación

**Definición operacional:** duración estimada de la relación, derivada de curvas de retención. Su valor está en distinguirlo de **margen de contribución del cliente**.

La heterogeneidad es el punto que Peter Fader ha insistido en subrayar: los clientes no valen lo mismo y el promedio describe a pocos. Un valor de vida medio calculado sobre una base con distribución muy dispersa induce decisiones equivocadas, porque lleva a tratar igual a clientes cuyo valor difiere en un orden de magnitud.

**Contraste bibliográfico.** Peter Fader — *Customer Centricity* (2020, 2.ª ed.) aporta aquí una distinción concreta: la heterogeneidad del valor del cliente: no todos valen lo mismo ni deben tratarse igual (los capítulos sobre centricidad en el cliente). Formula dos mini-casos: uno que satisface la definición de **permanencia esperada** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «estimar permanencia desde curvas de retención por cohorte», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Heterogeneidad: operacionalización y medición

**Heterogeneidad** significa **diferencia sustantiva de valor entre clientes del mismo segmento aparente**.

La permanencia esperada es el supuesto más frágil y debe estimarse con datos de cohortes y no con una tasa de baja promedio invertida. Ese atajo —dividir uno entre la tasa de baja— supone una tasa constante que casi nunca se cumple, porque el riesgo de baja es mayor al principio y disminuye después.

Ficha de medición obligatoria para **valor de vida por segmento**: `margen acumulado esperado, por segmento y cohorte`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) pone una condición sobre la medición: el sobreajuste y la validación fuera de muestra (los capítulos sobre sobreajuste). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Tasa de descuento: trade-offs y efectos de segundo orden

**Definición:** ajuste que refleja el valor temporal del dinero en la proyección.

Un modelo más elaborado captura mejor la heterogeneidad y es más difícil de explicar y de mantener. Uno simple se comunica y sobreestima o subestima según el caso. La decisión debe considerar para qué se usará: para decidir cuánto invertir en adquisición basta un modelo grueso con rango; para priorizar cuentas individuales hace falta más.

**Lo que aporta la fuente.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) aporta el criterio para pesar el intercambio: el análisis de cohortes como corrección al promedio que esconde la mezcla (el capítulo sobre cohortes y segmentación). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **sensibilidad a la retención** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **tasa de descuento** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «presentar el resultado como rango y no como cifra única», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Todo cálculo de valor de vida debe declarar sus supuestos y su sensibilidad. Un cambio pequeño en la permanencia esperada modifica el resultado de forma considerable, y esa fragilidad es la información más importante que el análisis puede entregar. Sin ella, la cifra se usa como si fuera un hecho.

**Frontera declarada.** Con cohortes jóvenes, la proyección tiene error alto. Presentarla como cifra única induce decisiones de inversión sobre una precisión inexistente. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar valor de vida del cliente no consiste en sumar definiciones. Empieza por **margen de contribución del cliente**, contrasta **permanencia esperada** con **heterogeneidad**, incorpora **tasa de descuento** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Peter Fader y Sarah Toms — *The Customer Centricity Playbook* (2018) | El valor de vida como proyección con supuestos declarados y no como cifra única | Los capítulos sobre cálculo del valor de vida | ¿Qué debería observarse en **margen de contribución del cliente** si aquí opera «el valor de vida como proyección con supuestos declarados y no como cifra única»? ¿Y qué observación lo desmentiría en este caso? |
| Peter Fader — *Customer Centricity* (2020, 2.ª ed.) | La heterogeneidad del valor del cliente: no todos valen lo mismo ni deben tratarse igual | Los capítulos sobre centricidad en el cliente | ¿Qué debería observarse en **permanencia esperada** si aquí opera «la heterogeneidad del valor del cliente: no todos valen lo mismo ni deben tratarse igual»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | El sobreajuste y la validación fuera de muestra | Los capítulos sobre sobreajuste | ¿Qué debería observarse en **heterogeneidad** si aquí opera «el sobreajuste y la validación fuera de muestra»? ¿Y qué observación lo desmentiría en este caso? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | El análisis de cohortes como corrección al promedio que esconde la mezcla | El capítulo sobre cohortes y segmentación | ¿Qué debería observarse en **tasa de descuento** si aquí opera «el análisis de cohortes como corrección al promedio que esconde la mezcla»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El valor de vida que usa Ruta Andina supone retención constante de 96 % mensual. Sus cohortes reales muestran caídas de 8 % en los primeros meses y estabilización posterior.

**Paso 1 — Calcular el margen de contribución con costos completos.** El equipo escribe primero el supuesto asociado a **margen de contribución del cliente** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **valor de vida por segmento** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Estimar permanencia desde curvas de retención por cohorte.** El trabajo aquí es separar lo observado de lo inferido sobre **permanencia esperada**. La evidencia que ordena la discusión es **dispersión dentro del segmento**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Incorporar expansión y contracción observadas.** El riesgo de este paso es cerrar demasiado rápido alrededor de **heterogeneidad**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **sensibilidad a la retención** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Aplicar tasa de descuento y declarar supuestos.** Con **tasa de descuento** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **valor de vida por segmento** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Presentar el resultado como rango y no como cifra única.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **margen de contribución del cliente**. **dispersión dentro del segmento** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **margen de contribución del cliente** | Ingreso menos costos variables de servirlo, por periodo | Cuando **valor de vida por segmento** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **permanencia esperada** | Duración estimada de la relación, derivada de curvas de retención | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Con cohortes jóvenes, la proyección tiene error alto. Presentarla como cifra única induce decisiones de inversión sobre una precisión inexistente.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre valor de vida del cliente |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing analyst, Revenue analyst y Data-driven marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El valor de vida que usa Ruta Andina supone retención constante de 96 % mensual. Sus cohortes reales muestran caídas de 8 % en los primeros meses y estabilización posterior.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **calcular el margen de contribución con costos completos → estimar permanencia desde curvas de retención por cohorte → incorporar expansión y contracción observadas → aplicar tasa de descuento y declarar supuestos → presentar el resultado como rango y no como cifra única** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **valor de vida por segmento**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *The Customer Centricity Playbook* y la de *Customer Centricity*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **margen de contribución del cliente** y **permanencia esperada** como sinónimos | Se perdió la distinción entre «ingreso menos costos variables de servirlo, por periodo» y «duración estimada de la relación, derivada de curvas de retención» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «presentar el resultado como rango y no como cifra única» | Se saltó «calcular el margen de contribución con costos completos»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **valor de vida por segmento** | La métrica local reemplazó al resultado del sistema | Contrástala con **sensibilidad a la retención** y explicita el costo de oportunidad. |
| Proyectar con retención constante | Error específico de esta clase | Deriva la permanencia de curvas por cohorte y presenta el resultado como rango. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **margen de contribución del cliente** y **permanencia esperada** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **heterogeneidad** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «calcular el margen de contribución con costos completos» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **valor de vida por segmento** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Con cohortes jóvenes, la proyección tiene error alto. Presentarla como cifra única induce decisiones de inversión sobre una precisión inexistente»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **heterogeneidad** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **valor de vida por segmento**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *The Customer Centricity Playbook* y *Lean Analytics*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P20-C04-ltv/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **valor de vida por segmento**, **dispersión dentro del segmento** y **sensibilidad a la retención** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **caso analítico integral con árbol de métricas, cohortes, incrementalidad y dashboard ejecutivo**.

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

- Peter Fader y Sarah Toms — [*The Customer Centricity Playbook*](https://openlibrary.org/isbn/9781613630914) (2018) · ISBN 9781613630914 — **aporta a esta clase:** el valor de vida como proyección con supuestos declarados y no como cifra única. **Dónde buscarlo:** los capítulos sobre cálculo del valor de vida. Registra edición y páginas consultadas en tu nota de lectura.
- Peter Fader — [*Customer Centricity*](https://openlibrary.org/isbn/9781613631447) (2020, 2.ª ed.) · ISBN 9781613631447 — **aporta a esta clase:** la heterogeneidad del valor del cliente: no todos valen lo mismo ni deben tratarse igual. **Dónde buscarlo:** los capítulos sobre centricidad en el cliente. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) · ISBN 9781449374280 — **aporta a esta clase:** el sobreajuste y la validación fuera de muestra. **Dónde buscarlo:** los capítulos sobre sobreajuste. Registra edición y páginas consultadas en tu nota de lectura.
- Alistair Croll y Benjamin Yoskovitz — [*Lean Analytics*](https://openlibrary.org/isbn/9781449335670) (2013) · ISBN 9781449335670 — **aporta a esta clase:** el análisis de cohortes como corrección al promedio que esconde la mezcla. **Dónde buscarlo:** el capítulo sobre cohortes y segmentación. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 03 · Costo de adquisición de cliente](class-03-cac.md) · [Índice de la parte](README.md) · [Clase 05 · Periodo de recuperación](class-05-payback.md) →
