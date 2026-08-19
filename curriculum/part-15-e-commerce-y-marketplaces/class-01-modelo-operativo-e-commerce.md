---
title: "Modelo operativo de e-commerce"
type: class
language: es
standard: clase-profunda-v2
part: 15
class: 01
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["flint", "croll-yoskovitz", "chaffey", "fader"]
anchors: {"chaffey": "planificacion", "croll-yoskovitz": "modelos", "fader": "heterogeneidad", "flint": "valor-canal"}
updated: 2026-08-19
---

# Clase 15.01 — Modelo operativo de e-commerce

Clase 1 de 14 de la parte [15 — E-commerce y marketplaces](README.md), de nivel Adquisición. Dura unos 150 minutos.

## 🚦 Antes de empezar

Esta es la primera clase de la parte, así que no arrastras entregables de las anteriores. Si llegas desde otra parte, ten a la vista su artefacto final; si el programa empieza aquí para ti, lee antes [la ruta de aprendizaje](../../docs/RUTA-DE-APRENDIZAJE.md).

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de margen por pedido con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La contribución real de cada canal descontando lo que habría ocurrido igual — Kevin Hillstrom. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Vender en línea es una operación logística y financiera antes que una vitrina. El modelo operativo define quién almacena, quién despacha, quién cobra, quién responde por una devolución y cuánto cuesta cada uno de esos pasos. La mayoría de los emprendimientos digitales que fracasan no tenía un problema de tráfico: tenía un costo por pedido superior a su margen y no lo sabía.

El punto de partida de esta clase no es la definición sino la decisión que la definición debe mejorar. La parte 15 busca **operar una tienda y un canal de marketplace con economía verificable**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **modelo operativo de e-commerce** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Dónde se pierde el pedido y cuánto queda después de comisión, envío y devolución?

Los conceptos que estructuran la sesión son **costo por pedido**, **modelo de cumplimiento**, **margen por pedido** y **punto de equilibrio operativo**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `costo por pedido`, `modelo de cumplimiento`, `margen por pedido` y `punto de equilibrio operativo` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **E-commerce y marketplaces**.
3. **Aplicar** la secuencia **mapear el flujo completo desde el pedido hasta la entrega → costear cada paso con datos reales → calcular el margen por pedido y por categoría → identificar el punto de equilibrio operativo → decidir qué pasos internalizar o externalizar** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **margen por pedido**, **costo logístico sobre ingreso** y **pedidos bajo el punto de equilibrio** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **costo por pedido** y **modelo de cumplimiento** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **margen por pedido**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **costo por pedido** | suma de costos de producto, empaque, despacho, pasarela y atención por cada pedido | Da un hecho compatible con la definición y otro que la refute. |
| **modelo de cumplimiento** | forma en que se almacena, prepara y entrega el producto | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **margen por pedido** | ingreso del pedido menos todos los costos variables asociados | Construye un caso límite donde el concepto se confunde con el anterior. |
| **punto de equilibrio operativo** | volumen a partir del cual la operación cubre sus costos fijos | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. mapear el flujo completo desde el pedido hasta la entrega → 2. costear cada paso con datos reales → 3. calcular el margen por pedido y por categoría → 4. identificar el punto de equilibrio operativo → 5. decidir qué pasos internalizar o externalizar
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** El costo por pedido varía con el volumen y con la mezcla de productos. Un cálculo promedio esconde categorías que pierden dinero en cada venta.

## 📖 Desarrollo

### 1. Costo por pedido: mecanismo central

**Costo por pedido** se entiende aquí como **suma de costos de producto, empaque, despacho, pasarela y atención por cada pedido**.

El comercio digital se evalúa por pedido y no por venta total. Esa unidad de análisis revela lo que el ingreso agregado oculta: cuánto cuesta procesar, preparar y entregar cada pedido, y cuánto queda después. Un negocio que crece en ventas y pierde margen por pedido está acelerando hacia un problema que el tablero de ingresos no muestra.

**De dónde viene esta afirmación.** Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) aporta la idea que sostiene este bloque: la contribución real de cada canal descontando lo que habría ocurrido igual. Búscala en los capítulos sobre análisis forense de canales. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «margen por pedido» debería moverse cuando cambie **costo por pedido**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **modelo de cumplimiento**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Modelo de cumplimiento: frontera conceptual y error de clasificación

**Definición operacional:** forma en que se almacena, prepara y entrega el producto. Su valor está en distinguirlo de **costo por pedido**.

El modelo de cumplimiento —stock propio, despacho de terceros, cruce directo— determina la estructura de costos y el control sobre la experiencia. Cada modelo tiene un punto de equilibrio distinto y una sensibilidad distinta al volumen. Elegirlo sin ese análisis produce operaciones que funcionan a escala pequeña y se vuelven inviables al crecer, o al revés.

**Contraste bibliográfico.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) aporta aquí una distinción concreta: los seis modelos de negocio y las métricas que cambian entre ellos (la parte sobre modelos de negocio). Formula dos mini-casos: uno que satisface la definición de **modelo de cumplimiento** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «costear cada paso con datos reales», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Margen por pedido: operacionalización y medición

**Margen por pedido** significa **ingreso del pedido menos todos los costos variables asociados**.

El margen por pedido debe calcularse con todos los costos variables dentro: producto, embalaje, picking, despacho, comisión de medio de pago, devoluciones esperadas y atención posventa asociada. Esa cifra, por categoría, suele revelar que parte del catálogo se vende con margen negativo, y esa información cambia decisiones de promoción y de surtido.

Ficha de medición obligatoria para **margen por pedido**: `ingreso menos costos variables, dividido por ingreso, por categoría`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) pone una condición sobre la medición: el marco de planificación digital: situación, objetivos, estrategia, táctica, acción y control (los capítulos sobre planificación de marketing digital). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Punto de equilibrio operativo: trade-offs y efectos de segundo orden

**Definición:** volumen a partir del cual la operación cubre sus costos fijos.

Crecer en volumen mejora el poder de compra y la absorción de costos fijos, y puede deteriorar el margen si el crecimiento viene de categorías de bajo margen o de pedidos pequeños. La decisión de impulsar volumen debe declarar de qué segmento se espera que venga, no tratarlo como un objetivo indiferenciado.

**Lo que aporta la fuente.** Peter Fader — *Customer Centricity* (2020, 2.ª ed.) aporta el criterio para pesar el intercambio: la heterogeneidad del valor del cliente: no todos valen lo mismo ni deben tratarse igual (los capítulos sobre centricidad en el cliente). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **pedidos bajo el punto de equilibrio** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **punto de equilibrio operativo** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «decidir qué pasos internalizar o externalizar», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El punto de equilibrio operativo se mueve con la estacionalidad y con los cambios de tarifa logística. Calcularlo una vez y usarlo todo el año produce decisiones basadas en supuestos obsoletos. Revisarlo trimestralmente, o cuando cambia una tarifa relevante, es parte del mantenimiento de la operación.

**Frontera declarada.** El costo por pedido varía con el volumen y con la mezcla de productos. Un cálculo promedio esconde categorías que pierden dinero en cada venta. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar modelo operativo de e-commerce no consiste en sumar definiciones. Empieza por **costo por pedido**, contrasta **modelo de cumplimiento** con **margen por pedido**, incorpora **punto de equilibrio operativo** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) | La contribución real de cada canal descontando lo que habría ocurrido igual | Los capítulos sobre análisis forense de canales | ¿Qué debería observarse en **costo por pedido** si aquí opera «la contribución real de cada canal descontando lo que habría ocurrido igual»? ¿Y qué observación lo desmentiría en este caso? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | Los seis modelos de negocio y las métricas que cambian entre ellos | La parte sobre modelos de negocio | ¿Qué debería observarse en **modelo de cumplimiento** si aquí opera «los seis modelos de negocio y las métricas que cambian entre ellos»? ¿Y qué observación lo desmentiría en este caso? |
| Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) | El marco de planificación digital: situación, objetivos, estrategia, táctica, acción y control | Los capítulos sobre planificación de marketing digital | ¿Qué debería observarse en **margen por pedido** si aquí opera «el marco de planificación digital: situación, objetivos, estrategia, táctica, acción y control»? ¿Y qué observación lo desmentiría en este caso? |
| Peter Fader — *Customer Centricity* (2020, 2.ª ed.) | La heterogeneidad del valor del cliente: no todos valen lo mismo ni deben tratarse igual | Los capítulos sobre centricidad en el cliente | ¿Qué debería observarse en **punto de equilibrio operativo** si aquí opera «la heterogeneidad del valor del cliente: no todos valen lo mismo ni deben tratarse igual»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** La línea de hardware de Ruta Andina vende bien y pierde dinero: 16 % de comisión de marketplace, despacho subsidiado y 9 % de devoluciones que nadie costeó.

**Paso 1 — Mapear el flujo completo desde el pedido hasta la entrega.** El equipo escribe primero el supuesto asociado a **costo por pedido** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **margen por pedido** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Costear cada paso con datos reales.** El trabajo aquí es separar lo observado de lo inferido sobre **modelo de cumplimiento**. La evidencia que ordena la discusión es **costo logístico sobre ingreso**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Calcular el margen por pedido y por categoría.** El riesgo de este paso es cerrar demasiado rápido alrededor de **margen por pedido**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **pedidos bajo el punto de equilibrio** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Identificar el punto de equilibrio operativo.** Con **punto de equilibrio operativo** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **margen por pedido** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Decidir qué pasos internalizar o externalizar.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **costo por pedido**. **costo logístico sobre ingreso** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **costo por pedido** | Suma de costos de producto, empaque, despacho, pasarela y atención por cada pedido | Cuando **margen por pedido** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **modelo de cumplimiento** | Forma en que se almacena, prepara y entrega el producto | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** El costo por pedido varía con el volumen y con la mezcla de productos. Un cálculo promedio esconde categorías que pierden dinero en cada venta.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre modelo operativo de e-commerce |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como E-commerce manager, Marketplace specialist y Emprendedor. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

La línea de hardware de Ruta Andina vende bien y pierde dinero: 16 % de comisión de marketplace, despacho subsidiado y 9 % de devoluciones que nadie costeó.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **mapear el flujo completo desde el pedido hasta la entrega → costear cada paso con datos reales → calcular el margen por pedido y por categoría → identificar el punto de equilibrio operativo → decidir qué pasos internalizar o externalizar** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **margen por pedido**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Hillstrom's Multichannel Forensics* y la de *Lean Analytics*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **costo por pedido** y **modelo de cumplimiento** como sinónimos | Se perdió la distinción entre «suma de costos de producto, empaque, despacho, pasarela y atención por cada pedido» y «forma en que se almacena, prepara y entrega el producto» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «decidir qué pasos internalizar o externalizar» | Se saltó «mapear el flujo completo desde el pedido hasta la entrega»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **margen por pedido** | La métrica local reemplazó al resultado del sistema | Contrástala con **pedidos bajo el punto de equilibrio** y explicita el costo de oportunidad. |
| Evaluar el canal por ingreso y no por margen por pedido | Error específico de esta clase | Costea despacho, comisión y devoluciones antes de declarar rentable una categoría. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **costo por pedido** y **modelo de cumplimiento** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **margen por pedido** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «mapear el flujo completo desde el pedido hasta la entrega» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **margen por pedido** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «El costo por pedido varía con el volumen y con la mezcla de productos. Un cálculo promedio esconde categorías que pierden dinero en cada venta»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **margen por pedido** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **margen por pedido**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Hillstrom's Multichannel Forensics* y *Customer Centricity*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P15-C01-modelo-operativo-e-commerce/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **margen por pedido**, **costo logístico sobre ingreso** y **pedidos bajo el punto de equilibrio** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **simulación de tienda rentable con catálogo, checkout, costos y plan postventa**.

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

- Kevin Hillstrom — [*Hillstrom's Multichannel Forensics*](https://openlibrary.org/isbn/9780977148950) (2007) · ISBN 9780977148950 — **aporta a esta clase:** la contribución real de cada canal descontando lo que habría ocurrido igual. **Dónde buscarlo:** los capítulos sobre análisis forense de canales. Registra edición y páginas consultadas en tu nota de lectura.
- Alistair Croll y Benjamin Yoskovitz — [*Lean Analytics*](https://openlibrary.org/isbn/9781449335670) (2013) · ISBN 9781449335670 — **aporta a esta clase:** los seis modelos de negocio y las métricas que cambian entre ellos. **Dónde buscarlo:** la parte sobre modelos de negocio. Registra edición y páginas consultadas en tu nota de lectura.
- Dave Chaffey y Fiona Ellis-Chadwick — [*Digital Marketing*](https://openlibrary.org/isbn/9781292400990) (2022, 8.ª ed.) · ISBN 9781292400990 — **aporta a esta clase:** el marco de planificación digital: situación, objetivos, estrategia, táctica, acción y control. **Dónde buscarlo:** los capítulos sobre planificación de marketing digital. Registra edición y páginas consultadas en tu nota de lectura.
- Peter Fader — [*Customer Centricity*](https://openlibrary.org/isbn/9781613631447) (2020, 2.ª ed.) · ISBN 9781613631447 — **aporta a esta clase:** la heterogeneidad del valor del cliente: no todos valen lo mismo ni deben tratarse igual. **Dónde buscarlo:** los capítulos sobre centricidad en el cliente. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

[Índice de la parte](README.md) · [Clase 02 · Catálogo y merchandising digital](class-02-catalogo-y-merchandising-digital.md) →
