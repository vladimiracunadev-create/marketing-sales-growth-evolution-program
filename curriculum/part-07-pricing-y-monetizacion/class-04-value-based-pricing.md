---
title: "Pricing basado en valor"
type: class
language: es
standard: clase-profunda-v2
part: 07
class: 04
level: Oferta comercial
mastery_threshold: 80
estimated_minutes: 150
sources: ["nagle", "ramanujam", "simon", "hubbard"]
anchors: {"hubbard": "medicion-definicion", "nagle": "valor-diferencial", "ramanujam": "disposicion-pagar", "simon": "valor-percibido"}
updated: 2026-08-19
---

# Clase 07.04 — Pricing basado en valor

Clase 4 de 14 de la parte [07 — Pricing y monetización](README.md), de nivel Oferta comercial. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 07.03, *Pricing por competencia*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de valor diferencial verificado con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El valor económico: precio de referencia de la alternativa más el valor diferencial cuantificado — Thomas T. Nagle y Georg Müller. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

El pricing basado en valor parte del beneficio económico que la oferta produce para un segmento y captura una fracción de él. Requiere tres piezas: una alternativa de referencia clara, el valor diferencial cuantificado en la unidad del cliente y una regla de captura explícita. Nagle advierte que el método no consiste en cobrar todo el valor: dejar excedente al cliente es lo que sostiene la relación y hace defendible el precio.

El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta. La parte 07 busca **diseñar una arquitectura de precios que capture valor sin destruir demanda ni confianza**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **pricing basado en valor** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Cuánto vale esto para quién, y qué estructura de cobro alinea precio con valor entregado?

Los conceptos que estructuran la sesión son **valor de referencia**, **valor diferencial**, **regla de captura** y **excedente para el cliente**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `valor de referencia`, `valor diferencial`, `regla de captura` y `excedente para el cliente` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Pricing y monetización**.
3. **Aplicar** la secuencia **identificar la alternativa de referencia del segmento → cuantificar el valor diferencial en unidades del cliente → verificar la cuantificación con clientes reales → definir la regla de captura y justificarla → probar el precio resultante antes de generalizarlo** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **valor diferencial verificado**, **tasa de aceptación al nuevo precio** y **proporción de valor capturado** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **valor de referencia** y **valor diferencial** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **valor diferencial verificado**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **valor de referencia** | costo de la mejor alternativa disponible para el cliente | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **valor diferencial** | beneficio adicional que la oferta produce frente a esa alternativa, cuantificado | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **regla de captura** | proporción del valor diferencial que la empresa decide cobrar | Da un hecho compatible con la definición y otro que la refute. |
| **excedente para el cliente** | parte del valor diferencial que queda en manos del cliente y sostiene la elección | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. identificar la alternativa de referencia del segmento → 2. cuantificar el valor diferencial en unidades del cliente → 3. verificar la cuantificación con clientes reales → 4. definir la regla de captura y justificarla → 5. probar el precio resultante antes de generalizarlo
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** El valor no es uniforme dentro de un segmento: el mismo cálculo puede sobreestimar el beneficio para clientes con menor volumen. La estimación debe declarar su rango.

## 📖 Desarrollo

### 1. Valor de referencia: mecanismo central

**Valor de referencia** se entiende aquí como **costo de la mejor alternativa disponible para el cliente**.

El precio basado en valor parte de una pregunta distinta: cuánto vale para este cliente la diferencia entre tu oferta y su mejor alternativa. El cálculo tiene dos términos —el precio de la alternativa de referencia y el valor diferencial— y ambos deben estimarse con datos del cliente. Es más trabajo que los otros métodos y es el único que conecta precio con beneficio real.

**De dónde viene esta afirmación.** Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) aporta la idea que sostiene este bloque: el valor económico: precio de referencia de la alternativa más el valor diferencial cuantificado. Búscala en el capítulo sobre estimación del valor económico. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «valor diferencial verificado» debería moverse cuando cambie **valor de referencia**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **valor diferencial**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Valor diferencial: frontera conceptual y error de clasificación

**Definición operacional:** beneficio adicional que la oferta produce frente a esa alternativa, cuantificado. Su valor está en distinguirlo de **valor de referencia**.

El valor de referencia no siempre es un competidor: puede ser el costo del proceso manual actual o el costo de no hacer nada. Identificarlo correctamente es la mitad del ejercicio, porque determina el punto de partida del cálculo. Un error frecuente es usar como referencia al competidor más caro porque conviene, cuando el cliente en realidad compara contra su planilla.

**Contraste bibliográfico.** Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) aporta aquí una distinción concreta: las técnicas de conversación sobre disposición a pagar con clientes reales (el capítulo sobre cómo preguntar por el precio). Formula dos mini-casos: uno que satisface la definición de **valor diferencial** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «cuantificar el valor diferencial en unidades del cliente», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Regla de captura: operacionalización y medición

**Regla de captura** significa **proporción del valor diferencial que la empresa decide cobrar**.

La regla de captura define qué proporción del valor diferencial se traslada al precio. Capturar todo elimina el incentivo del cliente para cambiar; capturar poco deja margen sobre la mesa. La proporción razonable depende de la evidencia disponible: cuanto más incierta sea la estimación del valor, mayor debe ser el excedente que se deja al cliente para compensar su riesgo.

Ficha de medición obligatoria para **valor diferencial verificado**: `clientes que confirman la magnitud estimada, sobre clientes consultados`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Hermann Simon — *Confessions of the Pricing Man* (2015) pone una condición sobre la medición: el precio como reflejo del valor percibido y la tarea de comunicarlo (los capítulos sobre valor y precio). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Excedente para el cliente: trade-offs y efectos de segundo orden

**Definición:** parte del valor diferencial que queda en manos del cliente y sostiene la elección.

Un precio basado en valor puede ser muy distinto entre clientes, lo que mejora la captura y complica la administración y la percepción de justicia. Cuando los clientes se comunican entre sí —habitual en gremios y en sector público— las diferencias no justificadas por criterios verificables generan conflicto. La solución es que la diferencia se explique por una barrera legítima y declarada.

**Lo que aporta la fuente.** Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) aporta el criterio para pesar el intercambio: medir es reducir incertidumbre, no eliminarla (los capítulos que redefinen la medición). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **proporción de valor capturado** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **excedente para el cliente** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «probar el precio resultante antes de generalizarlo», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El método exige poder estimar el valor con alguna precisión y hay servicios donde eso no es posible: cuando el resultado depende mayoritariamente de la ejecución del cliente o cuando el beneficio es difuso. En esos casos, forzar una cuantificación produce cifras que no resisten la primera pregunta y dañan la credibilidad de toda la propuesta.

**Frontera declarada.** El valor no es uniforme dentro de un segmento: el mismo cálculo puede sobreestimar el beneficio para clientes con menor volumen. La estimación debe declarar su rango. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar pricing basado en valor no consiste en sumar definiciones. Empieza por **valor de referencia**, contrasta **valor diferencial** con **regla de captura**, incorpora **excedente para el cliente** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) | El valor económico: precio de referencia de la alternativa más el valor diferencial cuantificado | El capítulo sobre estimación del valor económico | ¿Qué debería observarse en **valor de referencia** si aquí opera «el valor económico: precio de referencia de la alternativa más el valor diferencial cuantificado»? ¿Y qué observación lo desmentiría en este caso? |
| Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) | Las técnicas de conversación sobre disposición a pagar con clientes reales | El capítulo sobre cómo preguntar por el precio | ¿Qué debería observarse en **valor diferencial** si aquí opera «las técnicas de conversación sobre disposición a pagar con clientes reales»? ¿Y qué observación lo desmentiría en este caso? |
| Hermann Simon — *Confessions of the Pricing Man* (2015) | El precio como reflejo del valor percibido y la tarea de comunicarlo | Los capítulos sobre valor y precio | ¿Qué debería observarse en **regla de captura** si aquí opera «el precio como reflejo del valor percibido y la tarea de comunicarlo»? ¿Y qué observación lo desmentiría en este caso? |
| Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) | Medir es reducir incertidumbre, no eliminarla | Los capítulos que redefinen la medición | ¿Qué debería observarse en **excedente para el cliente** si aquí opera «medir es reducir incertidumbre, no eliminarla»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Para un taller que pierde 6 citas semanales a CLP 45.000 cada una, el valor diferencial de reducir inasistencias a la mitad es del orden de CLP 540.000 mensuales. El plan cuesta CLP 79.000.

**Paso 1 — Identificar la alternativa de referencia del segmento.** El equipo escribe primero el supuesto asociado a **valor de referencia** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **valor diferencial verificado** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Cuantificar el valor diferencial en unidades del cliente.** El trabajo aquí es separar lo observado de lo inferido sobre **valor diferencial**. La evidencia que ordena la discusión es **tasa de aceptación al nuevo precio**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Verificar la cuantificación con clientes reales.** El riesgo de este paso es cerrar demasiado rápido alrededor de **regla de captura**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **proporción de valor capturado** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Definir la regla de captura y justificarla.** Con **excedente para el cliente** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **valor diferencial verificado** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Probar el precio resultante antes de generalizarlo.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **valor de referencia**. **tasa de aceptación al nuevo precio** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **valor de referencia** | Costo de la mejor alternativa disponible para el cliente | Cuando **valor diferencial verificado** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **valor diferencial** | Beneficio adicional que la oferta produce frente a esa alternativa, cuantificado | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** El valor no es uniforme dentro de un segmento: el mismo cálculo puede sobreestimar el beneficio para clientes con menor volumen. La estimación debe declarar su rango.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre pricing basado en valor |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Pricing manager, Product marketing, CFO comercial y Founder. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Para un taller que pierde 6 citas semanales a CLP 45.000 cada una, el valor diferencial de reducir inasistencias a la mitad es del orden de CLP 540.000 mensuales. El plan cuesta CLP 79.000.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **identificar la alternativa de referencia del segmento → cuantificar el valor diferencial en unidades del cliente → verificar la cuantificación con clientes reales → definir la regla de captura y justificarla → probar el precio resultante antes de generalizarlo** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **valor diferencial verificado**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *The Strategy and Tactics of Pricing* y la de *Monetizing Innovation*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **valor de referencia** y **valor diferencial** como sinónimos | Se perdió la distinción entre «costo de la mejor alternativa disponible para el cliente» y «beneficio adicional que la oferta produce frente a esa alternativa, cuantificado» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «probar el precio resultante antes de generalizarlo» | Se saltó «identificar la alternativa de referencia del segmento»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **valor diferencial verificado** | La métrica local reemplazó al resultado del sistema | Contrástala con **proporción de valor capturado** y explicita el costo de oportunidad. |
| Cuantificar el valor sin verificarlo con clientes | Error específico de esta clase | Presenta el cálculo a cinco clientes y ajusta los supuestos que rechacen. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **valor de referencia** y **valor diferencial** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **regla de captura** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «identificar la alternativa de referencia del segmento» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **valor diferencial verificado** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «El valor no es uniforme dentro de un segmento: el mismo cálculo puede sobreestimar el beneficio para clientes con menor volumen. La estimación debe declarar su rango»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **regla de captura** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **valor diferencial verificado**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *The Strategy and Tactics of Pricing* y *How to Measure Anything*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, comprueba la norma en su texto vigente. Los enlaces van al texto completo publicado por la Biblioteca del Congreso Nacional; son gratuitos y no hace falta creerle a este material.

- **Consumo y comercio.** [Ley 19.496](https://www.bcn.cl/leychile/navegar?idNorma=61438) — *Establece normas sobre protección de los derechos de los consumidores* (Ministerio de Economía, Fomento y Reconstrucción), y su reglamento de comercio electrónico, [Decreto 6/2021](https://www.bcn.cl/leychile/navegar?idNorma=1165504) — *Aprueba reglamento de comercio electrónico* (Ministerio de Economía, Fomento y Turismo).
- **Datos personales.** [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales* (Ministerio Secretaría General de la Presidencia), que sustituye progresivamente a [Ley 19.628](https://www.bcn.cl/leychile/navegar?idNorma=141599) — *Sobre protección de la vida privada* (Ministerio Secretaría General de la Presidencia).
- **Derecho a retracto.** [Decreto 52/2024](https://www.bcn.cl/leychile/navegar?idNorma=1206144) — *Aprueba reglamento que regula la forma y condiciones en que los proveedores deberán comunicar la exclusión del derecho a retracto y los bienes en que excepcionalmente y por su naturaleza procederá tal exclusión* (Ministerio de Economía, Fomento y Turismo).

Dentro del repositorio, el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) ordena qué norma aplica a cada decisión comercial, [datos personales y ética](../../docs/DATOS-PERSONALES-Y-ETICA.md) desarrolla el tratamiento de datos y [fuentes oficiales](../../docs/FUENTES-OFICIALES.md) lista los organismos con su fecha de consulta. Ninguno de esos documentos reemplaza al texto legal.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P07-C04-value-based-pricing/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **valor diferencial verificado**, **tasa de aceptación al nuevo precio** y **proporción de valor capturado** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **arquitectura de monetización con métrica de cobro, planes, price fences y política de descuentos**.

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

- Thomas T. Nagle y Georg Müller — [*The Strategy and Tactics of Pricing*](https://openlibrary.org/isbn/9781138737501) (2018, 6.ª ed.) · ISBN 9781138737501 — **aporta a esta clase:** el valor económico: precio de referencia de la alternativa más el valor diferencial cuantificado. **Dónde buscarlo:** el capítulo sobre estimación del valor económico. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Madhavan Ramanujam y Georg Tacke — [*Monetizing Innovation*](https://openlibrary.org/isbn/9781119240877) (2016) · ISBN 9781119240877 — **aporta a esta clase:** las técnicas de conversación sobre disposición a pagar con clientes reales. **Dónde buscarlo:** el capítulo sobre cómo preguntar por el precio. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Hermann Simon — [*Confessions of the Pricing Man*](https://openlibrary.org/isbn/9783319204000) (2015) · ISBN 9783319204000 — **aporta a esta clase:** el precio como reflejo del valor percibido y la tarea de comunicarlo. **Dónde buscarlo:** los capítulos sobre valor y precio. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Douglas W. Hubbard — [*How to Measure Anything*](https://openlibrary.org/isbn/9781118836446) (2014, 3.ª ed.) · ISBN 9781118836446 — **aporta a esta clase:** medir es reducir incertidumbre, no eliminarla. **Dónde buscarlo:** los capítulos que redefinen la medición. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 03 · Pricing por competencia](class-03-competitor-based-pricing.md) · [Índice de la parte](README.md) · [Clase 05 · Disposición a pagar](class-05-willingness-to-pay.md) →
