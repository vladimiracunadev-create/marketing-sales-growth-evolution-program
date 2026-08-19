---
title: "Incrementalidad"
type: class
language: es
standard: clase-profunda-v2
part: 20
class: 09
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["kohavi", "provost", "kaushik", "binet-field"]
anchors: {"binet-field": "metricas-sesgo", "kaushik": "so-what", "kohavi": "guardarrailes", "provost": "valor-esperado"}
updated: 2026-08-19
---

# Clase 20.09 — Incrementalidad

Clase 9 de 14 de la parte [20 — Analítica comercial y marketing science](README.md), de nivel Crecimiento y analítica. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 20.08, *Modelos de atribución*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de efecto incremental estimado con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** Las métricas guardarraíl que impiden ganar en lo local perdiendo en el sistema — Ron Kohavi, Diane Tang y Ya Xu. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La incrementalidad responde la única pregunta que importa para decidir presupuesto: qué habría pasado sin esta inversión. Se estima con experimentos —grupos de control geográficos, suspensión de campañas, asignación aleatoria— y casi siempre revela que el efecto real es menor que el atribuido. Su costo es la complejidad; su beneficio es evitar escalar lo que no funciona.

Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales. La parte 20 busca **sostener decisiones de ingreso con métricas correctamente construidas**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **incrementalidad** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Esta cifra mide lo que creo que mide, y qué decisión cambiaría si estuviera equivocada?

Los conceptos que estructuran la sesión son **efecto incremental**, **grupo de control**, **prueba de suspensión** y **costo del experimento**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `efecto incremental`, `grupo de control`, `prueba de suspensión` y `costo del experimento` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Analítica comercial y marketing science**.
3. **Aplicar** la secuencia **identificar la inversión cuyo efecto se quiere verificar → diseñar el grupo de control comparable → calcular la duración necesaria para detectar el efecto → ejecutar y medir la diferencia con intervalo → decidir la asignación con el resultado obtenido** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **efecto incremental estimado**, **proporción de resultado incremental** y **costo del experimento** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **efecto incremental** y **grupo de control** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **efecto incremental estimado**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **efecto incremental** | resultado que no habría ocurrido sin la intervención | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **grupo de control** | conjunto comparable que no recibe la intervención | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **prueba de suspensión** | experimento que apaga una inversión para medir su efecto real | Da un hecho compatible con la definición y otro que la refute. |
| **costo del experimento** | ingreso resignado durante la prueba para obtener la información | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. identificar la inversión cuyo efecto se quiere verificar → 2. diseñar el grupo de control comparable → 3. calcular la duración necesaria para detectar el efecto → 4. ejecutar y medir la diferencia con intervalo → 5. decidir la asignación con el resultado obtenido
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Los experimentos de incrementalidad tienen costo real y requieren volumen. En presupuestos pequeños, la información puede costar más que la decisión que informa.

## 📖 Desarrollo

### 1. Efecto incremental: mecanismo central

**Efecto incremental** se entiende aquí como **resultado que no habría ocurrido sin la intervención**.

La incrementalidad responde la pregunta que la atribución no puede: cuántas de esas conversiones no habrían ocurrido sin la inversión. Su medición requiere un grupo que no reciba el tratamiento, y esa condición es la que la vuelve incómoda: implica renunciar deliberadamente a alcanzar a una parte de la audiencia.

**De dónde viene esta afirmación.** Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) aporta la idea que sostiene este bloque: las métricas guardarraíl que impiden ganar en lo local perdiendo en el sistema. Búscala en los capítulos sobre métricas y guardarraíles. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «efecto incremental estimado» debería moverse cuando cambie **efecto incremental**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **grupo de control**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Grupo de control: frontera conceptual y error de clasificación

**Definición operacional:** conjunto comparable que no recibe la intervención. Su valor está en distinguirlo de **efecto incremental**.

La prueba de suspensión —dejar de invertir en un canal o zona durante un periodo y comparar— es el diseño más accesible. Su costo es real y calculable: el ingreso perdido durante la prueba. Ese costo debe compararse con el valor de saber si la inversión sostenida durante todo el año está produciendo efecto.

**Contraste bibliográfico.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta aquí una distinción concreta: el marco de valor esperado que combina probabilidad y consecuencia económica (el capítulo sobre valor esperado). Formula dos mini-casos: uno que satisface la definición de **grupo de control** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «diseñar el grupo de control comparable», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Prueba de suspensión: operacionalización y medición

**Prueba de suspensión** significa **experimento que apaga una inversión para medir su efecto real**.

El grupo de control debe ser comparable en composición y estar sujeto a las mismas condiciones externas. Separar por zona geográfica es lo más común y exige verificar que las zonas eran comparables antes del experimento, comparándolas en el periodo previo.

Ficha de medición obligatoria para **efecto incremental estimado**: `diferencia entre grupo tratado y control, con intervalo de confianza`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Avinash Kaushik — *Web Analytics 2.0* (2009) pone una condición sobre la medición: la prueba del «¿y entonces qué?» aplicada tres veces a cada informe (los capítulos sobre informes accionables). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Costo del experimento: trade-offs y efectos de segundo orden

**Definición:** ingreso resignado durante la prueba para obtener la información.

Medir incrementalidad con frecuencia entrega mejor información y consume ingreso y tiempo. La práctica razonable la reserva para las inversiones grandes y sostenidas, donde un error de atribución tiene consecuencias significativas, y acepta la atribución convencional para el resto.

**Lo que aporta la fuente.** Les Binet y Peter Field — *The Long and the Short of It* (2013) aporta el criterio para pesar el intercambio: el sesgo de las métricas de corto plazo hacia la activación y su efecto sobre el presupuesto (la discusión sobre medición y horizonte temporal). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **costo del experimento** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **costo del experimento** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «decidir la asignación con el resultado obtenido», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Un resultado de incrementalidad vale para el periodo, el mercado y el nivel de inversión en que se midió. La incrementalidad no es constante: puede ser alta con inversión baja y caer al aumentar el gasto. Extrapolarla a otro nivel de inversión es un supuesto adicional que debe declararse.

**Frontera declarada.** Los experimentos de incrementalidad tienen costo real y requieren volumen. En presupuestos pequeños, la información puede costar más que la decisión que informa. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar incrementalidad no consiste en sumar definiciones. Empieza por **efecto incremental**, contrasta **grupo de control** con **prueba de suspensión**, incorpora **costo del experimento** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | Las métricas guardarraíl que impiden ganar en lo local perdiendo en el sistema | Los capítulos sobre métricas y guardarraíles | ¿Qué debería observarse en **efecto incremental** si aquí opera «las métricas guardarraíl que impiden ganar en lo local perdiendo en el sistema»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | El marco de valor esperado que combina probabilidad y consecuencia económica | El capítulo sobre valor esperado | ¿Qué debería observarse en **grupo de control** si aquí opera «el marco de valor esperado que combina probabilidad y consecuencia económica»? ¿Y qué observación lo desmentiría en este caso? |
| Avinash Kaushik — *Web Analytics 2.0* (2009) | La prueba del «¿y entonces qué?» aplicada tres veces a cada informe | Los capítulos sobre informes accionables | ¿Qué debería observarse en **prueba de suspensión** si aquí opera «la prueba del «¿y entonces qué?» aplicada tres veces a cada informe»? ¿Y qué observación lo desmentiría en este caso? |
| Les Binet y Peter Field — *The Long and the Short of It* (2013) | El sesgo de las métricas de corto plazo hacia la activación y su efecto sobre el presupuesto | La discusión sobre medición y horizonte temporal | ¿Qué debería observarse en **costo del experimento** si aquí opera «el sesgo de las métricas de corto plazo hacia la activación y su efecto sobre el presupuesto»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina suspendió su campaña de marca durante cuatro semanas en dos regiones comparables. El ingreso cayó 4 %, no el 38 % que la atribución le asignaba.

**Paso 1 — Identificar la inversión cuyo efecto se quiere verificar.** El equipo escribe primero el supuesto asociado a **efecto incremental** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **efecto incremental estimado** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Diseñar el grupo de control comparable.** El trabajo aquí es separar lo observado de lo inferido sobre **grupo de control**. La evidencia que ordena la discusión es **proporción de resultado incremental**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Calcular la duración necesaria para detectar el efecto.** El riesgo de este paso es cerrar demasiado rápido alrededor de **prueba de suspensión**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **costo del experimento** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Ejecutar y medir la diferencia con intervalo.** Con **costo del experimento** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **efecto incremental estimado** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Decidir la asignación con el resultado obtenido.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **efecto incremental**. **proporción de resultado incremental** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **efecto incremental** | Resultado que no habría ocurrido sin la intervención | Cuando **efecto incremental estimado** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **grupo de control** | Conjunto comparable que no recibe la intervención | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Los experimentos de incrementalidad tienen costo real y requieren volumen. En presupuestos pequeños, la información puede costar más que la decisión que informa.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre incrementalidad |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing analyst, Revenue analyst y Data-driven marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina suspendió su campaña de marca durante cuatro semanas en dos regiones comparables. El ingreso cayó 4 %, no el 38 % que la atribución le asignaba.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **identificar la inversión cuyo efecto se quiere verificar → diseñar el grupo de control comparable → calcular la duración necesaria para detectar el efecto → ejecutar y medir la diferencia con intervalo → decidir la asignación con el resultado obtenido** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **efecto incremental estimado**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Trustworthy Online Controlled Experiments* y la de *Data Science for Business*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **efecto incremental** y **grupo de control** como sinónimos | Se perdió la distinción entre «resultado que no habría ocurrido sin la intervención» y «conjunto comparable que no recibe la intervención» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «decidir la asignación con el resultado obtenido» | Se saltó «identificar la inversión cuyo efecto se quiere verificar»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **efecto incremental estimado** | La métrica local reemplazó al resultado del sistema | Contrástala con **costo del experimento** y explicita el costo de oportunidad. |
| Asignar presupuesto sin verificación de incrementalidad en las decisiones mayores | Error específico de esta clase | Diseña una prueba de suspensión para los canales que concentran el gasto. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **efecto incremental** y **grupo de control** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **prueba de suspensión** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «identificar la inversión cuyo efecto se quiere verificar» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **efecto incremental estimado** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Los experimentos de incrementalidad tienen costo real y requieren volumen. En presupuestos pequeños, la información puede costar más que la decisión que informa»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **prueba de suspensión** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **efecto incremental estimado**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Trustworthy Online Controlled Experiments* y *The Long and the Short of It*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, comprueba la norma en su texto vigente. Los enlaces van al texto completo publicado por la Biblioteca del Congreso Nacional; son gratuitos y no hace falta creerle a este material.

- **Consumo y comercio.** [Ley 19.496](https://www.bcn.cl/leychile/navegar?idNorma=61438) — *Establece normas sobre protección de los derechos de los consumidores* (Ministerio de Economía, Fomento y Reconstrucción), y su reglamento de comercio electrónico, [Decreto 6/2021](https://www.bcn.cl/leychile/navegar?idNorma=1165504) — *Aprueba reglamento de comercio electrónico* (Ministerio de Economía, Fomento y Turismo).
- **Datos personales.** [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales* (Ministerio Secretaría General de la Presidencia), que sustituye progresivamente a [Ley 19.628](https://www.bcn.cl/leychile/navegar?idNorma=141599) — *Sobre protección de la vida privada* (Ministerio Secretaría General de la Presidencia).
- **Derecho a retracto.** [Decreto 52/2024](https://www.bcn.cl/leychile/navegar?idNorma=1206144) — *Aprueba reglamento que regula la forma y condiciones en que los proveedores deberán comunicar la exclusión del derecho a retracto y los bienes en que excepcionalmente y por su naturaleza procederá tal exclusión* (Ministerio de Economía, Fomento y Turismo).

Dentro del repositorio, el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) ordena qué norma aplica a cada decisión comercial, [datos personales y ética](../../docs/DATOS-PERSONALES-Y-ETICA.md) desarrolla el tratamiento de datos y [fuentes oficiales](../../docs/FUENTES-OFICIALES.md) lista los organismos con su fecha de consulta. Ninguno de esos documentos reemplaza al texto legal.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P20-C09-incrementalidad/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **efecto incremental estimado**, **proporción de resultado incremental** y **costo del experimento** con fuente, ventana y lectura prohibida.
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

Aquí conviene separar dos cosas que suelen ir juntas y no son lo mismo.

**Lo que está comprobado.** Que cada obra existe y cuál es exactamente la edición: el enlace resuelve su ISBN contra el catálogo de OpenLibrary, y eso se revalida periódicamente. Las normas chilenas citadas más arriba enlazan su texto completo y gratuito.

**Lo que es atribución del programa.** Que la idea señalada esté en el capítulo que se indica. Eso es la lectura que este material hace de cada obra, no una cita textual cotejada frase por frase, y se declara así de explícito para que puedas contrastarlo: si abres la obra y no encuentras la idea donde se dice, la cita está mal puesta y **corresponde reportarlo como error del material**. No se citan números de página porque cambian entre ediciones.

- Ron Kohavi, Diane Tang y Ya Xu — [*Trustworthy Online Controlled Experiments*](https://openlibrary.org/isbn/9781108601375) (2020) · ISBN 9781108601375 — **aporta a esta clase:** las métricas guardarraíl que impiden ganar en lo local perdiendo en el sistema. **Dónde buscarlo:** los capítulos sobre métricas y guardarraíles. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) · ISBN 9781449374280 — **aporta a esta clase:** el marco de valor esperado que combina probabilidad y consecuencia económica. **Dónde buscarlo:** el capítulo sobre valor esperado. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Avinash Kaushik — [*Web Analytics 2.0*](https://openlibrary.org/isbn/9780470596425) (2009) · ISBN 9780470596425 — **aporta a esta clase:** la prueba del «¿y entonces qué?» aplicada tres veces a cada informe. **Dónde buscarlo:** los capítulos sobre informes accionables. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Les Binet y Peter Field — [*The Long and the Short of It*](https://openlibrary.org/isbn/9780852941348) (2013) · ISBN 9780852941348 — **aporta a esta clase:** el sesgo de las métricas de corto plazo hacia la activación y su efecto sobre el presupuesto. **Dónde buscarlo:** la discusión sobre medición y horizonte temporal. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 08 · Modelos de atribución](class-08-attribution-models.md) · [Índice de la parte](README.md) · [Clase 10 · A/B testing](class-10-a-b-testing.md) →
