---
title: "Fulfillment"
type: class
language: es
standard: clase-profunda-v2
part: 15
class: 06
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["dixon-effort", "flint", "chaffey", "grove"]
anchors: {"chaffey": "omnicanal", "dixon-effort": "resolucion-siguiente", "flint": "recompra", "grove": "indicadores-adelantados"}
updated: 2026-08-19
---

# Clase 15.06 — Fulfillment

**Parte 15 · E-commerce y marketplaces** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 15.05 — *Pagos*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de cumplimiento del plazo prometido para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La resolución del siguiente problema previsible en el mismo contacto — Matthew Dixon, Nick Toman y Rick DeLisi. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

El cumplimiento es la promesa que el cliente experimenta. Un plazo incumplido daña más que un precio alto porque afecta la confianza y genera contacto con soporte. La decisión central es entre operar la logística propia o externalizarla, y depende del volumen, del margen y de la capacidad de sostener el estándar prometido.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 15 busca **operar una tienda y un canal de marketplace con economía verificable**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **fulfillment** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Dónde se pierde el pedido y cuánto queda después de comisión, envío y devolución?

Los conceptos que estructuran la sesión son **promesa de entrega**, **cumplimiento del plazo**, **costo de cumplimiento** y **incidencia logística**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `promesa de entrega`, `cumplimiento del plazo`, `costo de cumplimiento` y `incidencia logística` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **E-commerce y marketplaces**.
3. **Aplicar** la secuencia **medir el cumplimiento real antes de prometer → definir la promesa con margen de seguridad → costear el cumplimiento por zona y por tamaño → monitorear incidencias y sus causas → revisar la decisión de operar o externalizar con datos** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **cumplimiento del plazo prometido**, **costo de cumplimiento por pedido** y **tasa de incidencias** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **promesa de entrega** y **cumplimiento del plazo** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **cumplimiento del plazo prometido**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **promesa de entrega** | plazo comunicado al cliente al momento de la compra | Da un hecho compatible con la definición y otro que la refute. |
| **cumplimiento del plazo** | proporción de pedidos entregados dentro de lo prometido | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **costo de cumplimiento** | gasto de preparación, empaque y despacho por pedido | Construye un caso límite donde el concepto se confunde con el anterior. |
| **incidencia logística** | pedido con problema de entrega que genera contacto y costo adicional | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. medir el cumplimiento real antes de prometer → 2. definir la promesa con margen de seguridad → 3. costear el cumplimiento por zona y por tamaño → 4. monitorear incidencias y sus causas → 5. revisar la decisión de operar o externalizar con datos
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Prometer plazos amplios reduce incumplimientos y también conversión. El punto óptimo se encuentra midiendo ambos efectos, no eligiendo uno.

## 📖 Desarrollo

### 1. Promesa de entrega: mecanismo central

**Promesa de entrega** se entiende aquí como **plazo comunicado al cliente al momento de la compra**.

El cumplimiento de la promesa de entrega es el momento donde la experiencia de compra se confirma o se rompe. Todo el trabajo comercial previo se juega en si el paquete llega cuando se dijo. Y a diferencia de otras variables, esta es verificable por el cliente sin ambigüedad: llegó o no llegó en la fecha.

**De dónde viene esta afirmación.** Matthew Dixon, Nick Toman y Rick DeLisi — *The Effortless Experience* (2013) aporta la idea que sostiene este bloque: la resolución del siguiente problema previsible en el mismo contacto. Búscala en los capítulos sobre resolución anticipada. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «cumplimiento del plazo prometido» debería moverse cuando cambie **promesa de entrega**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **cumplimiento del plazo**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Cumplimiento del plazo: frontera conceptual y error de clasificación

**Definición operacional:** proporción de pedidos entregados dentro de lo prometido. Su valor está en distinguirlo de **promesa de entrega**.

La promesa de entrega debe construirse con datos de desempeño real y no con el plazo teórico del operador logístico. Prometer el plazo óptimo produce incumplimientos sistemáticos; prometer el plazo que se cumple en la gran mayoría de los casos produce confianza. La diferencia entre ambos suele ser de uno o dos días y de mucho reclamo.

**Contraste bibliográfico.** Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) aporta aquí una distinción concreta: los patrones de recompra que distinguen un negocio de compra única de uno recurrente (los capítulos sobre ciclos de compra). Formula dos mini-casos: uno que satisface la definición de **cumplimiento del plazo** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «definir la promesa con margen de seguridad», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Costo de cumplimiento: operacionalización y medición

**Costo de cumplimiento** significa **gasto de preparación, empaque y despacho por pedido**.

El cumplimiento del plazo se mide por proporción de pedidos entregados dentro de lo prometido, segmentado por zona y por operador. El promedio nacional oculta que ciertas regiones tienen desempeño muy distinto, y esa segmentación permite ajustar la promesa por zona en lugar de degradar la promesa general.

Ficha de medición obligatoria para **cumplimiento del plazo prometido**: `pedidos entregados en plazo, sobre pedidos despachados`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) pone una condición sobre la medición: la integración de la experiencia entre canales digitales y físicos (los capítulos sobre multicanalidad). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Incidencia logística: trade-offs y efectos de segundo orden

**Definición:** pedido con problema de entrega que genera contacto y costo adicional.

Prometer plazos cortos mejora la conversión y aumenta el incumplimiento, que se paga en reclamos, costo de atención y bajas. Prometer plazos holgados reduce la conversión y protege la experiencia. El cálculo correcto compara la ganancia en conversión con el costo total del incumplimiento, incluido el de reputación.

**Lo que aporta la fuente.** Andrew S. Grove — *High Output Management* (1983) aporta el criterio para pesar el intercambio: los indicadores adelantados y pareados que permiten corregir a tiempo (los capítulos sobre medición en la producción). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **tasa de incidencias** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **incidencia logística** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar la decisión de operar o externalizar con datos», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La incidencia logística es inevitable a cierta escala y lo que se controla es la respuesta. Un procedimiento definido —cómo se detecta, en qué plazo se avisa al cliente, qué se ofrece— convierte un problema en una demostración de servicio. Sin ese procedimiento, cada incidencia se resuelve improvisando y el resultado depende de quién atienda.

**Frontera declarada.** Prometer plazos amplios reduce incumplimientos y también conversión. El punto óptimo se encuentra midiendo ambos efectos, no eligiendo uno. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar fulfillment no consiste en sumar definiciones. Empieza por **promesa de entrega**, contrasta **cumplimiento del plazo** con **costo de cumplimiento**, incorpora **incidencia logística** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Matthew Dixon, Nick Toman y Rick DeLisi — *The Effortless Experience* (2013) | La resolución del siguiente problema previsible en el mismo contacto | Los capítulos sobre resolución anticipada | ¿Qué debería observarse en **promesa de entrega** si aquí opera «la resolución del siguiente problema previsible en el mismo contacto»? ¿Y qué observación lo desmentiría en este caso? |
| Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) | Los patrones de recompra que distinguen un negocio de compra única de uno recurrente | Los capítulos sobre ciclos de compra | ¿Qué debería observarse en **cumplimiento del plazo** si aquí opera «los patrones de recompra que distinguen un negocio de compra única de uno recurrente»? ¿Y qué observación lo desmentiría en este caso? |
| Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) | La integración de la experiencia entre canales digitales y físicos | Los capítulos sobre multicanalidad | ¿Qué debería observarse en **costo de cumplimiento** si aquí opera «la integración de la experiencia entre canales digitales y físicos»? ¿Y qué observación lo desmentiría en este caso? |
| Andrew S. Grove — *High Output Management* (1983) | Los indicadores adelantados y pareados que permiten corregir a tiempo | Los capítulos sobre medición en la producción | ¿Qué debería observarse en **incidencia logística** si aquí opera «los indicadores adelantados y pareados que permiten corregir a tiempo»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina promete entrega en 48 horas y cumple en 61 % de los casos. Cada incumplimiento genera en promedio 2,3 contactos con soporte.

**Paso 1 — Medir el cumplimiento real antes de prometer.** El equipo escribe primero el supuesto asociado a **promesa de entrega** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **cumplimiento del plazo prometido** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Definir la promesa con margen de seguridad.** El trabajo aquí es separar lo observado de lo inferido sobre **cumplimiento del plazo**. La evidencia que ordena la discusión es **costo de cumplimiento por pedido**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Costear el cumplimiento por zona y por tamaño.** El riesgo de este paso es cerrar demasiado rápido alrededor de **costo de cumplimiento**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **tasa de incidencias** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Monitorear incidencias y sus causas.** Con **incidencia logística** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **cumplimiento del plazo prometido** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar la decisión de operar o externalizar con datos.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **promesa de entrega**. **costo de cumplimiento por pedido** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **promesa de entrega** | Plazo comunicado al cliente al momento de la compra | Cuando **cumplimiento del plazo prometido** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **cumplimiento del plazo** | Proporción de pedidos entregados dentro de lo prometido | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Prometer plazos amplios reduce incumplimientos y también conversión. El punto óptimo se encuentra midiendo ambos efectos, no eligiendo uno.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre fulfillment |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como E-commerce manager, Marketplace specialist y Emprendedor. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina promete entrega en 48 horas y cumple en 61 % de los casos. Cada incumplimiento genera en promedio 2,3 contactos con soporte.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **medir el cumplimiento real antes de prometer → definir la promesa con margen de seguridad → costear el cumplimiento por zona y por tamaño → monitorear incidencias y sus causas → revisar la decisión de operar o externalizar con datos** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **cumplimiento del plazo prometido**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *The Effortless Experience* y la de *Hillstrom's Multichannel Forensics*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **promesa de entrega** y **cumplimiento del plazo** como sinónimos | Se perdió la distinción entre «plazo comunicado al cliente al momento de la compra» y «proporción de pedidos entregados dentro de lo prometido» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar la decisión de operar o externalizar con datos» | Se saltó «medir el cumplimiento real antes de prometer»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **cumplimiento del plazo prometido** | La métrica local reemplazó al resultado del sistema | Contrástala con **tasa de incidencias** y explicita el costo de oportunidad. |
| Prometer plazos que la operación no cumple | Error específico de esta clase | Calcula el plazo que se cumple en el 95 % de los casos y comunica ese, no el mejor caso. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **promesa de entrega** y **cumplimiento del plazo** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **costo de cumplimiento** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «medir el cumplimiento real antes de prometer» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **cumplimiento del plazo prometido** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Prometer plazos amplios reduce incumplimientos y también conversión. El punto óptimo se encuentra midiendo ambos efectos, no eligiendo uno»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **costo de cumplimiento** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **cumplimiento del plazo prometido**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *The Effortless Experience* y *High Output Management*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P15-C06-fulfillment/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **cumplimiento del plazo prometido**, **costo de cumplimiento por pedido** y **tasa de incidencias** con fuente, ventana y lectura prohibida.
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

Cada obra aparece con la idea concreta que aporta a esta clase. Si al leer no encuentras esa idea, la cita está mal puesta y corresponde reportarlo como error del material.

- Matthew Dixon, Nick Toman y Rick DeLisi — *The Effortless Experience* (2013) — **aporta a esta clase:** la resolución del siguiente problema previsible en el mismo contacto. **Dónde buscarlo:** los capítulos sobre resolución anticipada. Registra edición y páginas consultadas en tu nota de lectura.
- Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) — **aporta a esta clase:** los patrones de recompra que distinguen un negocio de compra única de uno recurrente. **Dónde buscarlo:** los capítulos sobre ciclos de compra. Registra edición y páginas consultadas en tu nota de lectura.
- Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) — **aporta a esta clase:** la integración de la experiencia entre canales digitales y físicos. **Dónde buscarlo:** los capítulos sobre multicanalidad. Registra edición y páginas consultadas en tu nota de lectura.
- Andrew S. Grove — *High Output Management* (1983) — **aporta a esta clase:** los indicadores adelantados y pareados que permiten corregir a tiempo. **Dónde buscarlo:** los capítulos sobre medición en la producción. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 05 · Pagos](class-05-pagos.md) · [Índice de la parte](README.md) · [Clase 07 · Conversión en comercio digital](class-07-conversion.md) →
