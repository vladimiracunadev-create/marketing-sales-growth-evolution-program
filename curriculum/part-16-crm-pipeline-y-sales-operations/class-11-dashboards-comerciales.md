# Clase 16.11 — Dashboards comerciales

Clase 11 de 14 de la parte [16 — CRM, pipeline y sales operations](README.md), de nivel Operación de ingresos. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 16.10, *Velocidad comercial*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de métricas con acción definida con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La prueba del «¿y entonces qué?» aplicada tres veces a cada informe — Avinash Kaushik. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Un tablero comercial debe responder tres preguntas: cómo vamos, qué está en riesgo y qué requiere decisión. Todo lo demás sobra. El error habitual es acumular gráficos hasta que nadie los mira: un tablero con treinta métricas no informa, distrae. La regla de diseño es que cada elemento debe tener una acción asociada cuando se sale de rango.

El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta. La parte 16 busca **convertir el CRM en un sistema de trabajo y de verdad operacional**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **dashboards comerciales** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿El pipeline describe la realidad o solo el optimismo del equipo?

Los conceptos que estructuran la sesión son **métrica accionable**, **jerarquía del tablero**, **rango esperado** y **audiencia del tablero**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `métrica accionable`, `jerarquía del tablero`, `rango esperado` y `audiencia del tablero` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **CRM, pipeline y sales operations**.
3. **Aplicar** la secuencia **definir la audiencia y sus decisiones → elegir las métricas que informan esas decisiones → establecer rangos esperados y acciones asociadas → eliminar todo lo que no tenga acción → revisar el uso real del tablero cada trimestre** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **métricas con acción definida**, **uso del tablero** y **decisiones tomadas con el tablero** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **métrica accionable** y **jerarquía del tablero** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **métricas con acción definida**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **métrica accionable** | indicador con una acción definida cuando se desvía de su rango | Da un hecho compatible con la definición y otro que la refute. |
| **jerarquía del tablero** | orden que refleja la importancia de las decisiones que informa | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **rango esperado** | banda de variación normal que evita reaccionar al ruido | Construye un caso límite donde el concepto se confunde con el anterior. |
| **audiencia del tablero** | rol específico para el que se diseña el conjunto de indicadores | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir la audiencia y sus decisiones → 2. elegir las métricas que informan esas decisiones → 3. establecer rangos esperados y acciones asociadas → 4. eliminar todo lo que no tenga acción → 5. revisar el uso real del tablero cada trimestre
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un tablero no reemplaza la conversación de gestión. Su función es enfocar la discusión, no sustituir el juicio sobre casos particulares.

## 📖 Desarrollo

### 1. Métrica accionable: mecanismo central

**Métrica accionable** se entiende aquí como **indicador con una acción definida cuando se desvía de su rango**.

Un tablero comercial existe para producir decisiones y no para mostrar información. La prueba es directa: por cada indicador, preguntar qué decisión cambia según su valor. Los que no responden esa pregunta ocupan espacio y desvían la atención de los que sí.

**De dónde viene esta afirmación.** Avinash Kaushik — *Web Analytics 2.0* (2009) aporta la idea que sostiene este bloque: la prueba del «¿y entonces qué?» aplicada tres veces a cada informe. Búscala en los capítulos sobre informes accionables. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «métricas con acción definida» debería moverse cuando cambie **métrica accionable**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **jerarquía del tablero**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Jerarquía del tablero: frontera conceptual y error de clasificación

**Definición operacional:** orden que refleja la importancia de las decisiones que informa. Su valor está en distinguirlo de **métrica accionable**.

La jerarquía del tablero debe corresponder a la audiencia. El indicador que un vendedor necesita a diario no es el que la dirección necesita mensualmente. Un tablero único para todos termina siendo demasiado detallado para unos y demasiado agregado para otros, y nadie lo usa.

**Contraste bibliográfico.** Andrew S. Grove — *High Output Management* (1983) aporta aquí una distinción concreta: los indicadores adelantados y pareados que permiten corregir a tiempo (los capítulos sobre medición en la producción). Formula dos mini-casos: uno que satisface la definición de **jerarquía del tablero** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «elegir las métricas que informan esas decisiones», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Rango esperado: operacionalización y medición

**Rango esperado** significa **banda de variación normal que evita reaccionar al ruido**.

El rango esperado es lo que convierte un número en información. Un valor sin contexto —sin periodo anterior, sin meta, sin banda de variación normal— no permite saber si hay que actuar. Incorporar límites de variación calculados con los propios datos evita reaccionar ante fluctuaciones normales.

Ficha de medición obligatoria para **métricas con acción definida**: `indicadores con acción asociada, sobre indicadores del tablero`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) pone una condición sobre la medición: los inductores de actuación frente a los indicadores de resultado (los capítulos sobre tipos de indicador). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Audiencia del tablero: trade-offs y efectos de segundo orden

**Definición:** rol específico para el que se diseña el conjunto de indicadores.

Más indicadores entregan más visibilidad y diluyen la atención; menos concentran y pueden ocultar problemas. La regla práctica es que un tablero de gestión no debería exigir desplazamiento para verse completo, y que cada indicador debe tener un responsable que actúe cuando se desvía.

**Lo que aporta la fuente.** Donald J. Wheeler — *Understanding Variation* (2000) aporta el criterio para pesar el intercambio: los gráficos de comportamiento del proceso como filtro entre señal y ruido (los capítulos sobre gráficos de control). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **decisiones tomadas con el tablero** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **audiencia del tablero** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar el uso real del tablero cada trimestre», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Los tableros heredan la calidad de los datos que los alimentan. Un indicador construido sobre un campo que el equipo completa de forma inconsistente produce una cifra precisa e inexacta. Antes de publicar un tablero conviene verificar la calidad de sus fuentes, porque una vez publicado se usará como si fuera confiable.

**Frontera declarada.** Un tablero no reemplaza la conversación de gestión. Su función es enfocar la discusión, no sustituir el juicio sobre casos particulares. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Tomar decisiones de contratación y presupuesto sobre un pipeline que no representa la realidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar dashboards comerciales no consiste en sumar definiciones. Empieza por **métrica accionable**, contrasta **jerarquía del tablero** con **rango esperado**, incorpora **audiencia del tablero** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Avinash Kaushik — *Web Analytics 2.0* (2009) | La prueba del «¿y entonces qué?» aplicada tres veces a cada informe | Los capítulos sobre informes accionables | ¿Qué debería observarse en **métrica accionable** si aquí opera «la prueba del «¿y entonces qué?» aplicada tres veces a cada informe»? ¿Y qué observación lo desmentiría en este caso? |
| Andrew S. Grove — *High Output Management* (1983) | Los indicadores adelantados y pareados que permiten corregir a tiempo | Los capítulos sobre medición en la producción | ¿Qué debería observarse en **jerarquía del tablero** si aquí opera «los indicadores adelantados y pareados que permiten corregir a tiempo»? ¿Y qué observación lo desmentiría en este caso? |
| Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) | Los inductores de actuación frente a los indicadores de resultado | Los capítulos sobre tipos de indicador | ¿Qué debería observarse en **rango esperado** si aquí opera «los inductores de actuación frente a los indicadores de resultado»? ¿Y qué observación lo desmentiría en este caso? |
| Donald J. Wheeler — *Understanding Variation* (2000) | Los gráficos de comportamiento del proceso como filtro entre señal y ruido | Los capítulos sobre gráficos de control | ¿Qué debería observarse en **audiencia del tablero** si aquí opera «los gráficos de comportamiento del proceso como filtro entre señal y ruido»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El tablero comercial de Ruta Andina tiene 22 gráficos. En la reunión semanal se revisan dos y las decisiones se toman con una planilla aparte.

**Paso 1 — Definir la audiencia y sus decisiones.** El equipo escribe primero el supuesto asociado a **métrica accionable** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **métricas con acción definida** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Elegir las métricas que informan esas decisiones.** El trabajo aquí es separar lo observado de lo inferido sobre **jerarquía del tablero**. La evidencia que ordena la discusión es **uso del tablero**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Establecer rangos esperados y acciones asociadas.** El riesgo de este paso es cerrar demasiado rápido alrededor de **rango esperado**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **decisiones tomadas con el tablero** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Eliminar todo lo que no tenga acción.** Con **audiencia del tablero** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **métricas con acción definida** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar el uso real del tablero cada trimestre.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **métrica accionable**. **uso del tablero** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **métrica accionable** | Indicador con una acción definida cuando se desvía de su rango | Cuando **métricas con acción definida** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **jerarquía del tablero** | Orden que refleja la importancia de las decisiones que informa | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un tablero no reemplaza la conversación de gestión. Su función es enfocar la discusión, no sustituir el juicio sobre casos particulares.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre dashboards comerciales |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Sales operations, RevOps analyst y Jefe de ventas. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El tablero comercial de Ruta Andina tiene 22 gráficos. En la reunión semanal se revisan dos y las decisiones se toman con una planilla aparte.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir la audiencia y sus decisiones → elegir las métricas que informan esas decisiones → establecer rangos esperados y acciones asociadas → eliminar todo lo que no tenga acción → revisar el uso real del tablero cada trimestre** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **métricas con acción definida**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Web Analytics 2.0* y la de *High Output Management*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **métrica accionable** y **jerarquía del tablero** como sinónimos | Se perdió la distinción entre «indicador con una acción definida cuando se desvía de su rango» y «orden que refleja la importancia de las decisiones que informa» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar el uso real del tablero cada trimestre» | Se saltó «definir la audiencia y sus decisiones»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **métricas con acción definida** | La métrica local reemplazó al resultado del sistema | Contrástala con **decisiones tomadas con el tablero** y explicita el costo de oportunidad. |
| Acumular métricas sin acción asociada | Error específico de esta clase | Elimina del tablero toda métrica que no tenga una acción definida cuando se sale de rango. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **métrica accionable** y **jerarquía del tablero** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **rango esperado** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir la audiencia y sus decisiones» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **métricas con acción definida** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un tablero no reemplaza la conversación de gestión. Su función es enfocar la discusión, no sustituir el juicio sobre casos particulares»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **rango esperado** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **métricas con acción definida**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Web Analytics 2.0* y *Understanding Variation*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Tomar decisiones de contratación y presupuesto sobre un pipeline que no representa la realidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, comprueba la norma en su texto vigente. Los enlaces van al texto completo publicado por la Biblioteca del Congreso Nacional; son gratuitos y no hace falta creerle a este material.

- **Consumo y comercio.** [Ley 19.496](https://www.bcn.cl/leychile/navegar?idNorma=61438) — *Establece normas sobre protección de los derechos de los consumidores* (Ministerio de Economía, Fomento y Reconstrucción), y su reglamento de comercio electrónico, [Decreto 6/2021](https://www.bcn.cl/leychile/navegar?idNorma=1165504) — *Aprueba reglamento de comercio electrónico* (Ministerio de Economía, Fomento y Turismo).
- **Datos personales.** [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales* (Ministerio Secretaría General de la Presidencia), que sustituye progresivamente a [Ley 19.628](https://www.bcn.cl/leychile/navegar?idNorma=141599) — *Sobre protección de la vida privada* (Ministerio Secretaría General de la Presidencia).
- **Derecho a retracto.** [Decreto 52/2024](https://www.bcn.cl/leychile/navegar?idNorma=1206144) — *Aprueba reglamento que regula la forma y condiciones en que los proveedores deberán comunicar la exclusión del derecho a retracto y los bienes en que excepcionalmente y por su naturaleza procederá tal exclusión* (Ministerio de Economía, Fomento y Turismo).

Dentro del repositorio, el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) ordena qué norma aplica a cada decisión comercial, [datos personales y ética](../../docs/DATOS-PERSONALES-Y-ETICA.md) desarrolla el tratamiento de datos y [fuentes oficiales](../../docs/FUENTES-OFICIALES.md) lista los organismos con su fecha de consulta. Ninguno de esos documentos reemplaza al texto legal.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P16-C11-dashboards-comerciales/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **métricas con acción definida**, **uso del tablero** y **decisiones tomadas con el tablero** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **diseño de sales operations con pipeline, criterios de etapa, forecast y gobierno de datos**.

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

- Avinash Kaushik — [*Web Analytics 2.0*](https://openlibrary.org/isbn/9780470596425) (2009) · ISBN 9780470596425 — **aporta a esta clase:** la prueba del «¿y entonces qué?» aplicada tres veces a cada informe. **Dónde buscarlo:** los capítulos sobre informes accionables. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Andrew S. Grove — [*High Output Management*](https://openlibrary.org/isbn/9780394532349) (1983) · ISBN 9780394532349 — **aporta a esta clase:** los indicadores adelantados y pareados que permiten corregir a tiempo. **Dónde buscarlo:** los capítulos sobre medición en la producción. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Robert S. Kaplan y David P. Norton — [*The Balanced Scorecard*](https://openlibrary.org/isbn/9780875846514) (1996) · ISBN 9780875846514 — **aporta a esta clase:** los inductores de actuación frente a los indicadores de resultado. **Dónde buscarlo:** los capítulos sobre tipos de indicador. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Donald J. Wheeler — [*Understanding Variation*](https://openlibrary.org/isbn/9780945320531) (2000) · ISBN 9780945320531 — **aporta a esta clase:** los gráficos de comportamiento del proceso como filtro entre señal y ruido. **Dónde buscarlo:** los capítulos sobre gráficos de control. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 10 · Velocidad comercial](class-10-sales-velocity.md) · [Índice de la parte](README.md) · [Clase 12 · Revisión de pipeline](class-12-revision-de-pipeline.md) →
