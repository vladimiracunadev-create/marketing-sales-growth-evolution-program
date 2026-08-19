---
title: "Margen de contribución"
type: class
language: es
standard: clase-profunda-v2
part: 20
class: 06
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["croll-yoskovitz", "provost", "nagle", "simon"]
anchors: {"croll-yoskovitz": "modelos", "nagle": "costo-piso", "provost": "formulacion", "simon": "valor-percibido"}
updated: 2026-08-19
---

# Clase 20.06 — Margen de contribución

Clase 6 de 14 de la parte [20 — Analítica comercial y marketing science](README.md), de nivel Crecimiento y analítica. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 20.05, *Periodo de recuperación*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de margen de contribución por segmento con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** Los seis modelos de negocio y las métricas que cambian entre ellos — Alistair Croll y Benjamin Yoskovitz. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

El margen de contribución es lo que queda del ingreso después de los costos variables y es la base de cualquier análisis comercial serio. Su cálculo exige decidir qué costos son efectivamente variables: soporte, implementación, comisiones y despacho suelen serlo aunque se registren como gasto fijo. Un margen mal calculado invalida todo lo que se construya encima.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 20 busca **sostener decisiones de ingreso con métricas correctamente construidas**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **margen de contribución** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Esta cifra mide lo que creo que mide, y qué decisión cambiaría si estuviera equivocada?

Los conceptos que estructuran la sesión son **costo variable**, **margen de contribución**, **costo escalonado** y **margen por segmento**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `costo variable`, `margen de contribución`, `costo escalonado` y `margen por segmento` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Analítica comercial y marketing science**.
3. **Aplicar** la secuencia **clasificar cada costo como variable, escalonado o fijo → atribuir los costos variables a clientes y segmentos → calcular el margen por segmento y por producto → identificar los segmentos con margen negativo → validar el resultado con contabilidad** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **margen de contribución por segmento**, **segmentos con margen negativo** y **diferencia con la contabilidad** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **costo variable** y **margen de contribución** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **margen de contribución por segmento**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **costo variable** | gasto que cambia con el volumen de clientes o de transacciones | Da un hecho compatible con la definición y otro que la refute. |
| **margen de contribución** | ingreso menos costos variables, en monto y en porcentaje | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **costo escalonado** | gasto que se comporta como fijo en tramos y salta al superar un umbral | Construye un caso límite donde el concepto se confunde con el anterior. |
| **margen por segmento** | contribución calculada separadamente para cada grupo de clientes | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. clasificar cada costo como variable, escalonado o fijo → 2. atribuir los costos variables a clientes y segmentos → 3. calcular el margen por segmento y por producto → 4. identificar los segmentos con margen negativo → 5. validar el resultado con contabilidad
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** La distinción entre costo fijo y variable depende del horizonte. En el largo plazo, casi todos los costos son variables y el análisis debe declarar su horizonte.

## 📖 Desarrollo

### 1. Costo variable: mecanismo central

**Costo variable** se entiende aquí como **gasto que cambia con el volumen de clientes o de transacciones**.

El margen de contribución es lo que queda de cada peso vendido después de los costos que varían con esa venta. Es la base de casi toda decisión comercial —qué promover, qué descontar, a quién servir— y su cálculo depende de clasificar correctamente los costos, tarea menos obvia de lo que parece.

**De dónde viene esta afirmación.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) aporta la idea que sostiene este bloque: los seis modelos de negocio y las métricas que cambian entre ellos. Búscala en la parte sobre modelos de negocio. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «margen de contribución por segmento» debería moverse cuando cambie **costo variable**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **margen de contribución**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Margen de contribución: frontera conceptual y error de clasificación

**Definición operacional:** ingreso menos costos variables, en monto y en porcentaje. Su valor está en distinguirlo de **costo variable**.

El costo escalonado complica el análisis: hay costos que no varían con cada unidad pero sí saltan al superar un umbral —una persona más de soporte, un servidor adicional—. Tratarlos como fijos subestima el costo del crecimiento; tratarlos como variables lo sobreestima. Registrar dónde están los escalones es la forma correcta.

**Contraste bibliográfico.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta aquí una distinción concreta: la formulación del problema de negocio como problema de datos antes de elegir técnica (los capítulos iniciales sobre pensamiento analítico). Formula dos mini-casos: uno que satisface la definición de **margen de contribución** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «atribuir los costos variables a clientes y segmentos», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Costo escalonado: operacionalización y medición

**Costo escalonado** significa **gasto que se comporta como fijo en tramos y salta al superar un umbral**.

El margen por segmento suele revelar diferencias grandes que el promedio esconde. Un segmento con buen precio y alto costo de servir puede tener margen menor que otro más barato y autónomo. Ese análisis, hecho una vez, suele reordenar la prioridad comercial más que cualquier estudio de mercado.

Ficha de medición obligatoria para **margen de contribución por segmento**: `ingreso menos costos variables, sobre ingreso, por segmento`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) pone una condición sobre la medición: el costo como piso de decisión y no como método de fijación (el capítulo sobre costos relevantes para la decisión). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Margen por segmento: trade-offs y efectos de segundo orden

**Definición:** contribución calculada separadamente para cada grupo de clientes.

Maximizar el margen unitario puede reducir el margen total si el volumen cae más de lo proporcional. La decisión correcta optimiza la contribución total y no el porcentaje, distinción que se pierde con facilidad cuando el indicador de gestión es el margen porcentual.

**Lo que aporta la fuente.** Hermann Simon — *Confessions of the Pricing Man* (2015) aporta el criterio para pesar el intercambio: el precio como reflejo del valor percibido y la tarea de comunicarlo (los capítulos sobre valor y precio). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **diferencia con la contabilidad** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **margen por segmento** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «validar el resultado con contabilidad», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El margen de contribución no incluye costos fijos y por lo tanto no indica rentabilidad. Un negocio puede tener margen de contribución positivo en todas sus líneas y perder dinero. Presentarlo como medida de rentabilidad es un error frecuente en presentaciones comerciales y produce decisiones de portafolio equivocadas.

**Frontera declarada.** La distinción entre costo fijo y variable depende del horizonte. En el largo plazo, casi todos los costos son variables y el análisis debe declarar su horizonte. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar margen de contribución no consiste en sumar definiciones. Empieza por **costo variable**, contrasta **margen de contribución** con **costo escalonado**, incorpora **margen por segmento** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | Los seis modelos de negocio y las métricas que cambian entre ellos | La parte sobre modelos de negocio | ¿Qué debería observarse en **costo variable** si aquí opera «los seis modelos de negocio y las métricas que cambian entre ellos»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La formulación del problema de negocio como problema de datos antes de elegir técnica | Los capítulos iniciales sobre pensamiento analítico | ¿Qué debería observarse en **margen de contribución** si aquí opera «la formulación del problema de negocio como problema de datos antes de elegir técnica»? ¿Y qué observación lo desmentiría en este caso? |
| Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) | El costo como piso de decisión y no como método de fijación | El capítulo sobre costos relevantes para la decisión | ¿Qué debería observarse en **costo escalonado** si aquí opera «el costo como piso de decisión y no como método de fijación»? ¿Y qué observación lo desmentiría en este caso? |
| Hermann Simon — *Confessions of the Pricing Man* (2015) | El precio como reflejo del valor percibido y la tarea de comunicarlo | Los capítulos sobre valor y precio | ¿Qué debería observarse en **margen por segmento** si aquí opera «el precio como reflejo del valor percibido y la tarea de comunicarlo»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El plan más vendido de Ruta Andina muestra 62 % de margen bruto. Al incluir las 9 horas de migración y el soporte del primer trimestre, la contribución real es 12 %.

**Paso 1 — Clasificar cada costo como variable, escalonado o fijo.** El equipo escribe primero el supuesto asociado a **costo variable** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **margen de contribución por segmento** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Atribuir los costos variables a clientes y segmentos.** El trabajo aquí es separar lo observado de lo inferido sobre **margen de contribución**. La evidencia que ordena la discusión es **segmentos con margen negativo**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Calcular el margen por segmento y por producto.** El riesgo de este paso es cerrar demasiado rápido alrededor de **costo escalonado**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **diferencia con la contabilidad** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Identificar los segmentos con margen negativo.** Con **margen por segmento** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **margen de contribución por segmento** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Validar el resultado con contabilidad.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **costo variable**. **segmentos con margen negativo** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **costo variable** | Gasto que cambia con el volumen de clientes o de transacciones | Cuando **margen de contribución por segmento** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **margen de contribución** | Ingreso menos costos variables, en monto y en porcentaje | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** La distinción entre costo fijo y variable depende del horizonte. En el largo plazo, casi todos los costos son variables y el análisis debe declarar su horizonte.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre margen de contribución |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing analyst, Revenue analyst y Data-driven marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El plan más vendido de Ruta Andina muestra 62 % de margen bruto. Al incluir las 9 horas de migración y el soporte del primer trimestre, la contribución real es 12 %.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **clasificar cada costo como variable, escalonado o fijo → atribuir los costos variables a clientes y segmentos → calcular el margen por segmento y por producto → identificar los segmentos con margen negativo → validar el resultado con contabilidad** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **margen de contribución por segmento**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Lean Analytics* y la de *Data Science for Business*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **costo variable** y **margen de contribución** como sinónimos | Se perdió la distinción entre «gasto que cambia con el volumen de clientes o de transacciones» y «ingreso menos costos variables, en monto y en porcentaje» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «validar el resultado con contabilidad» | Se saltó «clasificar cada costo como variable, escalonado o fijo»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **margen de contribución por segmento** | La métrica local reemplazó al resultado del sistema | Contrástala con **diferencia con la contabilidad** y explicita el costo de oportunidad. |
| Tratar soporte e implementación como costo fijo | Error específico de esta clase | Atribuye las horas de servicio a los clientes que las consumen y recalcula el margen por segmento. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **costo variable** y **margen de contribución** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **costo escalonado** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «clasificar cada costo como variable, escalonado o fijo» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **margen de contribución por segmento** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «La distinción entre costo fijo y variable depende del horizonte. En el largo plazo, casi todos los costos son variables y el análisis debe declarar su horizonte»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **costo escalonado** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **margen de contribución por segmento**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Lean Analytics* y *Confessions of the Pricing Man*. |
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

Guarda en `evidence/P20-C06-contribution-margin/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **margen de contribución por segmento**, **segmentos con margen negativo** y **diferencia con la contabilidad** con fuente, ventana y lectura prohibida.
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

- Alistair Croll y Benjamin Yoskovitz — [*Lean Analytics*](https://openlibrary.org/isbn/9781449335670) (2013) · ISBN 9781449335670 — **aporta a esta clase:** los seis modelos de negocio y las métricas que cambian entre ellos. **Dónde buscarlo:** la parte sobre modelos de negocio. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) · ISBN 9781449374280 — **aporta a esta clase:** la formulación del problema de negocio como problema de datos antes de elegir técnica. **Dónde buscarlo:** los capítulos iniciales sobre pensamiento analítico. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Thomas T. Nagle y Georg Müller — [*The Strategy and Tactics of Pricing*](https://openlibrary.org/isbn/9781138737501) (2018, 6.ª ed.) · ISBN 9781138737501 — **aporta a esta clase:** el costo como piso de decisión y no como método de fijación. **Dónde buscarlo:** el capítulo sobre costos relevantes para la decisión. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Hermann Simon — [*Confessions of the Pricing Man*](https://openlibrary.org/isbn/9783319204000) (2015) · ISBN 9783319204000 — **aporta a esta clase:** el precio como reflejo del valor percibido y la tarea de comunicarlo. **Dónde buscarlo:** los capítulos sobre valor y precio. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 05 · Periodo de recuperación](class-05-payback.md) · [Índice de la parte](README.md) · [Clase 07 · Análisis de cohortes aplicado](class-07-cohort-analysis.md) →
