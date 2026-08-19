# Clase 20.01 — Árbol de métricas

Clase 1 de 14 de la parte [20 — Analítica comercial y marketing science](README.md), de nivel Crecimiento y analítica. Dura unos 150 minutos.

## 🚦 Antes de empezar

Esta es la primera clase de la parte, así que no arrastras entregables de las anteriores. Si llegas desde otra parte, ten a la vista su artefacto final; si el programa empieza aquí para ti, lee antes [la ruta de aprendizaje](../../docs/RUTA-DE-APRENDIZAJE.md).

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de cobertura del árbol con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El mapa estratégico que conecta causalmente objetivos entre perspectivas — Robert S. Kaplan y David P. Norton. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Un árbol de métricas descompone el resultado de negocio en factores multiplicativos hasta llegar a variables sobre las que alguien puede actuar. Su valor es doble: muestra cómo se conecta cada trabajo con el ingreso y evita discusiones sobre métricas que nadie puede mover. Kaplan y Norton insistieron en que los indicadores deben estar causalmente conectados, no sólo agrupados en un tablero.

El punto de partida de esta clase no es la definición sino la decisión que la definición debe mejorar. La parte 20 busca **sostener decisiones de ingreso con métricas correctamente construidas**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **árbol de métricas** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Esta cifra mide lo que creo que mide, y qué decisión cambiaría si estuviera equivocada?

Los conceptos que estructuran la sesión son **descomposición multiplicativa**, **variable accionable**, **nivel de agregación** y **conexión causal**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `descomposición multiplicativa`, `variable accionable`, `nivel de agregación` y `conexión causal` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Analítica comercial y marketing science**.
3. **Aplicar** la secuencia **definir el resultado en la cima del árbol → descomponer en factores multiplicativos verificables → continuar hasta llegar a variables accionables → asignar responsable a cada rama → verificar la aritmética con datos reales** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **cobertura del árbol**, **consistencia aritmética** y **ramas con responsable** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **descomposición multiplicativa** y **variable accionable** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **cobertura del árbol**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **descomposición multiplicativa** | expresión del resultado como producto de factores medibles | Da un hecho compatible con la definición y otro que la refute. |
| **variable accionable** | factor del árbol que alguien puede modificar con una decisión | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **nivel de agregación** | grado de detalle en que se descompone cada rama | Construye un caso límite donde el concepto se confunde con el anterior. |
| **conexión causal** | relación explícita entre un factor y el resultado que afecta | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir el resultado en la cima del árbol → 2. descomponer en factores multiplicativos verificables → 3. continuar hasta llegar a variables accionables → 4. asignar responsable a cada rama → 5. verificar la aritmética con datos reales
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** No todos los factores son multiplicativos ni independientes. Un árbol demasiado simple puede esconder interacciones importantes entre variables.

## 📖 Desarrollo

### 1. Descomposición multiplicativa: mecanismo central

**Descomposición multiplicativa** se entiende aquí como **expresión del resultado como producto de factores medibles**.

Un árbol de métricas descompone el resultado en factores que se multiplican o se suman hasta llegar a variables sobre las que alguien puede actuar. Su valor está en la trazabilidad: permite responder por qué cambió el resultado sin recurrir a hipótesis, siguiendo la descomposición hasta el factor que se movió.

**De dónde viene esta afirmación.** Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) aporta la idea que sostiene este bloque: el mapa estratégico que conecta causalmente objetivos entre perspectivas. Búscala en los capítulos sobre relaciones causa-efecto. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «cobertura del árbol» debería moverse cuando cambie **descomposición multiplicativa**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **variable accionable**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Variable accionable: frontera conceptual y error de clasificación

**Definición operacional:** factor del árbol que alguien puede modificar con una decisión. Su valor está en distinguirlo de **descomposición multiplicativa**.

La variable accionable es el punto donde el árbol debe detenerse. Descomponer hasta un nivel que nadie controla produce un diagrama elegante e inútil. La prueba es preguntar, en cada hoja del árbol, quién puede modificarla y con qué palanca; si no hay respuesta, hay que seguir descomponiendo o reconocer que es una variable externa.

**Contraste bibliográfico.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) aporta aquí una distinción concreta: la métrica que importa ahora: una sola, según etapa y modelo de negocio (los capítulos sobre la métrica única). Formula dos mini-casos: uno que satisface la definición de **variable accionable** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «descomponer en factores multiplicativos verificables», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Nivel de agregación: operacionalización y medición

**Nivel de agregación** significa **grado de detalle en que se descompone cada rama**.

El nivel de agregación debe ser consistente en toda la descomposición: mezclar métricas mensuales con acumuladas, o de cliente con de transacción, produce árboles que no cierran aritméticamente. Verificar que las operaciones efectivamente reconstruyen el total es un control básico que revela errores de definición.

Ficha de medición obligatoria para **cobertura del árbol**: `ramas con métrica instrumentada, sobre ramas definidas`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) pone una condición sobre la medición: la formulación del problema de negocio como problema de datos antes de elegir técnica (los capítulos iniciales sobre pensamiento analítico). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Conexión causal: trade-offs y efectos de segundo orden

**Definición:** relación explícita entre un factor y el resultado que afecta.

Un árbol detallado permite diagnóstico fino y se vuelve difícil de mantener y de comunicar. Uno grueso se entiende y no localiza la causa. La solución practicable es un árbol de dos o tres niveles para gestión y ramas detalladas que se abren sólo cuando hay que diagnosticar un tramo específico.

**Lo que aporta la fuente.** Avinash Kaushik — *Web Analytics 2.0* (2009) aporta el criterio para pesar el intercambio: la prueba del «¿y entonces qué?» aplicada tres veces a cada informe (los capítulos sobre informes accionables). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **ramas con responsable** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **conexión causal** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «verificar la aritmética con datos reales», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La conexión entre niveles del árbol es aritmética y no causal. Que el resultado se descomponga en esos factores no significa que actuar sobre uno produzca el efecto proporcional: pueden existir compensaciones. Confundir descomposición con causalidad lleva a prometer resultados que la aritmética sugiere y el sistema no entrega.

**Frontera declarada.** No todos los factores son multiplicativos ni independientes. Un árbol demasiado simple puede esconder interacciones importantes entre variables. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar árbol de métricas no consiste en sumar definiciones. Empieza por **descomposición multiplicativa**, contrasta **variable accionable** con **nivel de agregación**, incorpora **conexión causal** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) | El mapa estratégico que conecta causalmente objetivos entre perspectivas | Los capítulos sobre relaciones causa-efecto | ¿Qué debería observarse en **descomposición multiplicativa** si aquí opera «el mapa estratégico que conecta causalmente objetivos entre perspectivas»? ¿Y qué observación lo desmentiría en este caso? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | La métrica que importa ahora: una sola, según etapa y modelo de negocio | Los capítulos sobre la métrica única | ¿Qué debería observarse en **variable accionable** si aquí opera «la métrica que importa ahora: una sola, según etapa y modelo de negocio»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La formulación del problema de negocio como problema de datos antes de elegir técnica | Los capítulos iniciales sobre pensamiento analítico | ¿Qué debería observarse en **nivel de agregación** si aquí opera «la formulación del problema de negocio como problema de datos antes de elegir técnica»? ¿Y qué observación lo desmentiría en este caso? |
| Avinash Kaushik — *Web Analytics 2.0* (2009) | La prueba del «¿y entonces qué?» aplicada tres veces a cada informe | Los capítulos sobre informes accionables | ¿Qué debería observarse en **conexión causal** si aquí opera «la prueba del «¿y entonces qué?» aplicada tres veces a cada informe»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El tablero de Ruta Andina muestra 34 métricas sin relación entre sí. Nadie puede explicar cómo el trabajo de contenido afecta el ingreso recurrente.

**Paso 1 — Definir el resultado en la cima del árbol.** El equipo escribe primero el supuesto asociado a **descomposición multiplicativa** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **cobertura del árbol** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Descomponer en factores multiplicativos verificables.** El trabajo aquí es separar lo observado de lo inferido sobre **variable accionable**. La evidencia que ordena la discusión es **consistencia aritmética**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Continuar hasta llegar a variables accionables.** El riesgo de este paso es cerrar demasiado rápido alrededor de **nivel de agregación**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **ramas con responsable** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Asignar responsable a cada rama.** Con **conexión causal** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **cobertura del árbol** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Verificar la aritmética con datos reales.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **descomposición multiplicativa**. **consistencia aritmética** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **descomposición multiplicativa** | Expresión del resultado como producto de factores medibles | Cuando **cobertura del árbol** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **variable accionable** | Factor del árbol que alguien puede modificar con una decisión | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** No todos los factores son multiplicativos ni independientes. Un árbol demasiado simple puede esconder interacciones importantes entre variables.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre árbol de métricas |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing analyst, Revenue analyst y Data-driven marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El tablero de Ruta Andina muestra 34 métricas sin relación entre sí. Nadie puede explicar cómo el trabajo de contenido afecta el ingreso recurrente.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir el resultado en la cima del árbol → descomponer en factores multiplicativos verificables → continuar hasta llegar a variables accionables → asignar responsable a cada rama → verificar la aritmética con datos reales** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **cobertura del árbol**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *The Balanced Scorecard* y la de *Lean Analytics*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **descomposición multiplicativa** y **variable accionable** como sinónimos | Se perdió la distinción entre «expresión del resultado como producto de factores medibles» y «factor del árbol que alguien puede modificar con una decisión» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «verificar la aritmética con datos reales» | Se saltó «definir el resultado en la cima del árbol»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **cobertura del árbol** | La métrica local reemplazó al resultado del sistema | Contrástala con **ramas con responsable** y explicita el costo de oportunidad. |
| Agrupar métricas sin conexión causal | Error específico de esta clase | Construye la descomposición aritmética y verifica que el cálculo reproduzca el resultado real. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **descomposición multiplicativa** y **variable accionable** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **nivel de agregación** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir el resultado en la cima del árbol» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **cobertura del árbol** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «No todos los factores son multiplicativos ni independientes. Un árbol demasiado simple puede esconder interacciones importantes entre variables»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **nivel de agregación** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **cobertura del árbol**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *The Balanced Scorecard* y *Web Analytics 2.0*. |
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

Guarda en `evidence/P20-C01-arbol-de-metricas/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **cobertura del árbol**, **consistencia aritmética** y **ramas con responsable** con fuente, ventana y lectura prohibida.
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

- Robert S. Kaplan y David P. Norton — [*The Balanced Scorecard*](https://openlibrary.org/isbn/9780875846514) (1996) · ISBN 9780875846514 — **aporta a esta clase:** el mapa estratégico que conecta causalmente objetivos entre perspectivas. **Dónde buscarlo:** los capítulos sobre relaciones causa-efecto. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Alistair Croll y Benjamin Yoskovitz — [*Lean Analytics*](https://openlibrary.org/isbn/9781449335670) (2013) · ISBN 9781449335670 — **aporta a esta clase:** la métrica que importa ahora: una sola, según etapa y modelo de negocio. **Dónde buscarlo:** los capítulos sobre la métrica única. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) · ISBN 9781449374280 — **aporta a esta clase:** la formulación del problema de negocio como problema de datos antes de elegir técnica. **Dónde buscarlo:** los capítulos iniciales sobre pensamiento analítico. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Avinash Kaushik — [*Web Analytics 2.0*](https://openlibrary.org/isbn/9780470596425) (2009) · ISBN 9780470596425 — **aporta a esta clase:** la prueba del «¿y entonces qué?» aplicada tres veces a cada informe. **Dónde buscarlo:** los capítulos sobre informes accionables. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

[Índice de la parte](README.md) · [Clase 02 · Conversión y embudos](class-02-conversion-y-funnels.md) →
