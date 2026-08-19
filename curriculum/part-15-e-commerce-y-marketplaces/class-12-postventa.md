---
title: "Postventa"
type: class
language: es
standard: clase-profunda-v2
part: 15
class: 12
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["dixon-effort", "reichheld", "flint", "mehta"]
anchors: {"dixon-effort": "esfuerzo", "flint": "recompra", "mehta": "resultado-cliente", "reichheld": "cierre-circuito"}
updated: 2026-08-19
---

# Clase 15.12 — Postventa

Clase 12 de 14 de la parte [15 — E-commerce y marketplaces](README.md), de nivel Adquisición. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 15.11, *Marketplaces*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de tiempo de resolución con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La reducción del esfuerzo del cliente predice lealtad mejor que el deleite — Matthew Dixon, Nick Toman y Rick DeLisi. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La postventa es donde se define si el cliente vuelve. Incluye seguimiento del pedido, gestión de incidencias, devoluciones y garantía. En Chile, el derecho a retracto en compras a distancia y la garantía legal son obligaciones, no gestos comerciales: el proveedor debe informarlas y cumplirlas. Una postventa bien operada convierte un problema en una razón para volver.

La clase trata el tema como un problema de evidencia y de consecuencia, no como vocabulario. La parte 15 busca **operar una tienda y un canal de marketplace con economía verificable**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **postventa** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Dónde se pierde el pedido y cuánto queda después de comisión, envío y devolución?

Los conceptos que estructuran la sesión son **derecho a retracto**, **garantía legal**, **esfuerzo del cliente** y **recuperación de servicio**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `derecho a retracto`, `garantía legal`, `esfuerzo del cliente` y `recuperación de servicio` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **E-commerce y marketplaces**.
3. **Aplicar** la secuencia **documentar el proceso de devolución y garantía → informar los derechos de forma clara y accesible → reducir el esfuerzo del cliente en la resolución → medir tiempo de resolución e insatisfacción → analizar causas raíz y corregir el origen** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **tiempo de resolución**, **esfuerzo declarado del cliente** y **recompra tras incidencia resuelta** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **derecho a retracto** y **garantía legal** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **tiempo de resolución**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **derecho a retracto** | facultad del consumidor de terminar la compra a distancia dentro del plazo legal | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **garantía legal** | derecho a reparación, cambio o devolución que existe con independencia de la voluntad del proveedor | Construye un caso límite donde el concepto se confunde con el anterior. |
| **esfuerzo del cliente** | cantidad de pasos y tiempo que exige resolver un problema | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **recuperación de servicio** | gestión que convierte una experiencia negativa en confianza recuperada | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. documentar el proceso de devolución y garantía → 2. informar los derechos de forma clara y accesible → 3. reducir el esfuerzo del cliente en la resolución → 4. medir tiempo de resolución e insatisfacción → 5. analizar causas raíz y corregir el origen
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un proceso de devolución muy laxo puede ser abusado. El equilibrio se gestiona con verificación proporcional, nunca restringiendo derechos legales.

## 📖 Desarrollo

### 1. Derecho a retracto: mecanismo central

**Derecho a retracto** se entiende aquí como **facultad del consumidor de terminar la compra a distancia dentro del plazo legal**.

La posventa es donde se decide si habrá segunda compra, y en comercio digital la segunda compra es lo que hace viable el costo de adquisición. Una operación que trata la posventa como centro de costo está optimizando el gasto de la actividad que sostiene su economía.

**De dónde viene esta afirmación.** Matthew Dixon, Nick Toman y Rick DeLisi — *The Effortless Experience* (2013) aporta la idea que sostiene este bloque: la reducción del esfuerzo del cliente predice lealtad mejor que el deleite. Búscala en los capítulos que presentan la evidencia. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «tiempo de resolución» debería moverse cuando cambie **derecho a retracto**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **garantía legal**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Garantía legal: frontera conceptual y error de clasificación

**Definición operacional:** derecho a reparación, cambio o devolución que existe con independencia de la voluntad del proveedor. Su valor está en distinguirlo de **derecho a retracto**.

El esfuerzo del cliente es el mejor predictor de deterioro de la relación: cuántos contactos necesitó, cuántas veces repitió su información, cuánto esperó. Reducir ese esfuerzo tiene más efecto sobre la lealtad que superar expectativas en casos aislados, según la evidencia recogida por Matthew Dixon y su equipo.

**Contraste bibliográfico.** Fred Reichheld, Darci Darnell y Maureen Burns — *Winning on Purpose* (2021) aporta aquí una distinción concreta: el cierre del circuito con quien respondió como parte del sistema (los capítulos sobre el proceso de retroalimentación). Formula dos mini-casos: uno que satisface la definición de **garantía legal** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «informar los derechos de forma clara y accesible», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Esfuerzo del cliente: operacionalización y medición

**Esfuerzo del cliente** significa **cantidad de pasos y tiempo que exige resolver un problema**.

La recuperación de servicio bien ejecutada puede dejar una relación más fuerte que la ausencia de problemas. Sus condiciones son concretas: reconocer rápido, resolver sin que el cliente tenga que insistir y compensar de forma proporcional. Medir el resultado de las recuperaciones —qué proporción de esos clientes vuelve a comprar— indica si el procedimiento funciona.

Ficha de medición obligatoria para **tiempo de resolución**: `días entre la solicitud y la resolución efectiva, mediana`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) pone una condición sobre la medición: los patrones de recompra que distinguen un negocio de compra única de uno recurrente (los capítulos sobre ciclos de compra). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Recuperación de servicio: trade-offs y efectos de segundo orden

**Definición:** gestión que convierte una experiencia negativa en confianza recuperada.

Una política de devoluciones amplia mejora la conversión y aumenta el costo operativo y el abuso. Una restrictiva protege el costo y frena la compra, especialmente en categorías donde el cliente no puede evaluar antes. El cálculo debe comparar el aumento de conversión con el costo total de las devoluciones adicionales.

**Lo que aporta la fuente.** Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) aporta el criterio para pesar el intercambio: el resultado deseado del cliente más la experiencia apropiada como definición de éxito (los capítulos sobre la definición de customer success). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **recompra tras incidencia resuelta** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **recuperación de servicio** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «analizar causas raíz y corregir el origen», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El derecho a retracto y la garantía legal existen con independencia de la política comercial y no pueden restringirse. En Chile, la normativa de consumo establece condiciones específicas para el comercio a distancia. La política publicada debe cumplirlas como piso y su redacción debe verificarse con la norma vigente.

**Frontera declarada.** Un proceso de devolución muy laxo puede ser abusado. El equilibrio se gestiona con verificación proporcional, nunca restringiendo derechos legales. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar postventa no consiste en sumar definiciones. Empieza por **derecho a retracto**, contrasta **garantía legal** con **esfuerzo del cliente**, incorpora **recuperación de servicio** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Matthew Dixon, Nick Toman y Rick DeLisi — *The Effortless Experience* (2013) | La reducción del esfuerzo del cliente predice lealtad mejor que el deleite | Los capítulos que presentan la evidencia | ¿Qué debería observarse en **derecho a retracto** si aquí opera «la reducción del esfuerzo del cliente predice lealtad mejor que el deleite»? ¿Y qué observación lo desmentiría en este caso? |
| Fred Reichheld, Darci Darnell y Maureen Burns — *Winning on Purpose* (2021) | El cierre del circuito con quien respondió como parte del sistema | Los capítulos sobre el proceso de retroalimentación | ¿Qué debería observarse en **garantía legal** si aquí opera «el cierre del circuito con quien respondió como parte del sistema»? ¿Y qué observación lo desmentiría en este caso? |
| Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) | Los patrones de recompra que distinguen un negocio de compra única de uno recurrente | Los capítulos sobre ciclos de compra | ¿Qué debería observarse en **esfuerzo del cliente** si aquí opera «los patrones de recompra que distinguen un negocio de compra única de uno recurrente»? ¿Y qué observación lo desmentiría en este caso? |
| Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) | El resultado deseado del cliente más la experiencia apropiada como definición de éxito | Los capítulos sobre la definición de customer success | ¿Qué debería observarse en **recuperación de servicio** si aquí opera «el resultado deseado del cliente más la experiencia apropiada como definición de éxito»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina exige que las devoluciones se soliciten por correo, con boleta física y dentro de 5 días. El plazo legal de retracto es mayor y el requisito de boleta física es un obstáculo innecesario.

**Paso 1 — Documentar el proceso de devolución y garantía.** El equipo escribe primero el supuesto asociado a **derecho a retracto** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **tiempo de resolución** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Informar los derechos de forma clara y accesible.** El trabajo aquí es separar lo observado de lo inferido sobre **garantía legal**. La evidencia que ordena la discusión es **esfuerzo declarado del cliente**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Reducir el esfuerzo del cliente en la resolución.** El riesgo de este paso es cerrar demasiado rápido alrededor de **esfuerzo del cliente**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **recompra tras incidencia resuelta** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Medir tiempo de resolución e insatisfacción.** Con **recuperación de servicio** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **tiempo de resolución** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Analizar causas raíz y corregir el origen.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **derecho a retracto**. **esfuerzo declarado del cliente** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **derecho a retracto** | Facultad del consumidor de terminar la compra a distancia dentro del plazo legal | Cuando **tiempo de resolución** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **garantía legal** | Derecho a reparación, cambio o devolución que existe con independencia de la voluntad del proveedor | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un proceso de devolución muy laxo puede ser abusado. El equilibrio se gestiona con verificación proporcional, nunca restringiendo derechos legales.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre postventa |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como E-commerce manager, Marketplace specialist y Emprendedor. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina exige que las devoluciones se soliciten por correo, con boleta física y dentro de 5 días. El plazo legal de retracto es mayor y el requisito de boleta física es un obstáculo innecesario.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **documentar el proceso de devolución y garantía → informar los derechos de forma clara y accesible → reducir el esfuerzo del cliente en la resolución → medir tiempo de resolución e insatisfacción → analizar causas raíz y corregir el origen** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **tiempo de resolución**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *The Effortless Experience* y la de *Winning on Purpose*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **derecho a retracto** y **garantía legal** como sinónimos | Se perdió la distinción entre «facultad del consumidor de terminar la compra a distancia dentro del plazo legal» y «derecho a reparación, cambio o devolución que existe con independencia de la voluntad del proveedor» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «analizar causas raíz y corregir el origen» | Se saltó «documentar el proceso de devolución y garantía»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **tiempo de resolución** | La métrica local reemplazó al resultado del sistema | Contrástala con **recompra tras incidencia resuelta** y explicita el costo de oportunidad. |
| Restringir derechos del consumidor en las condiciones | Error específico de esta clase | Revisa las condiciones publicadas contra la normativa vigente y elimina toda cláusula que limite derechos legales. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **derecho a retracto** y **garantía legal** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **esfuerzo del cliente** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «documentar el proceso de devolución y garantía» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **tiempo de resolución** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un proceso de devolución muy laxo puede ser abusado. El equilibrio se gestiona con verificación proporcional, nunca restringiendo derechos legales»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **esfuerzo del cliente** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **tiempo de resolución**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *The Effortless Experience* y *Customer Success*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, comprueba la norma en su texto vigente. Los enlaces van al texto completo publicado por la Biblioteca del Congreso Nacional; son gratuitos y no hace falta creerle a este material.

- **Consumo y comercio.** [Ley 19.496](https://www.bcn.cl/leychile/navegar?idNorma=61438) — *Establece normas sobre protección de los derechos de los consumidores* (Ministerio de Economía, Fomento y Reconstrucción), y su reglamento de comercio electrónico, [Decreto 6/2021](https://www.bcn.cl/leychile/navegar?idNorma=1165504) — *Aprueba reglamento de comercio electrónico* (Ministerio de Economía, Fomento y Turismo).
- **Datos personales.** [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales* (Ministerio Secretaría General de la Presidencia), que sustituye progresivamente a [Ley 19.628](https://www.bcn.cl/leychile/navegar?idNorma=141599) — *Sobre protección de la vida privada* (Ministerio Secretaría General de la Presidencia).
- **Derecho a retracto.** [Decreto 52/2024](https://www.bcn.cl/leychile/navegar?idNorma=1206144) — *Aprueba reglamento que regula la forma y condiciones en que los proveedores deberán comunicar la exclusión del derecho a retracto y los bienes en que excepcionalmente y por su naturaleza procederá tal exclusión* (Ministerio de Economía, Fomento y Turismo).

Dentro del repositorio, el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) ordena qué norma aplica a cada decisión comercial, [datos personales y ética](../../docs/DATOS-PERSONALES-Y-ETICA.md) desarrolla el tratamiento de datos y [fuentes oficiales](../../docs/FUENTES-OFICIALES.md) lista los organismos con su fecha de consulta. Ninguno de esos documentos reemplaza al texto legal.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P15-C12-postventa/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **tiempo de resolución**, **esfuerzo declarado del cliente** y **recompra tras incidencia resuelta** con fuente, ventana y lectura prohibida.
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

Aquí conviene separar dos cosas que suelen ir juntas y no son lo mismo.

**Lo que está comprobado.** Que cada obra existe y cuál es exactamente la edición: el enlace resuelve su ISBN contra el catálogo de OpenLibrary, y eso se revalida periódicamente. Las normas chilenas citadas más arriba enlazan su texto completo y gratuito.

**Lo que es atribución del programa.** Que la idea señalada esté en el capítulo que se indica. Eso es la lectura que este material hace de cada obra, no una cita textual cotejada frase por frase, y se declara así de explícito para que puedas contrastarlo: si abres la obra y no encuentras la idea donde se dice, la cita está mal puesta y **corresponde reportarlo como error del material**. No se citan números de página porque cambian entre ediciones.

- Matthew Dixon, Nick Toman y Rick DeLisi — [*The Effortless Experience*](https://openlibrary.org/isbn/9780241003305) (2013) · ISBN 9780241003305 — **aporta a esta clase:** la reducción del esfuerzo del cliente predice lealtad mejor que el deleite. **Dónde buscarlo:** los capítulos que presentan la evidencia. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Fred Reichheld, Darci Darnell y Maureen Burns — [*Winning on Purpose*](https://openlibrary.org/isbn/9781647821784) (2021) · ISBN 9781647821784 — **aporta a esta clase:** el cierre del circuito con quien respondió como parte del sistema. **Dónde buscarlo:** los capítulos sobre el proceso de retroalimentación. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Kevin Hillstrom — [*Hillstrom's Multichannel Forensics*](https://openlibrary.org/isbn/9780977148950) (2007) · ISBN 9780977148950 — **aporta a esta clase:** los patrones de recompra que distinguen un negocio de compra única de uno recurrente. **Dónde buscarlo:** los capítulos sobre ciclos de compra. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Nick Mehta, Dan Steinman y Lincoln Murphy — [*Customer Success*](https://openlibrary.org/isbn/9781119168294) (2016) · ISBN 9781119168294 — **aporta a esta clase:** el resultado deseado del cliente más la experiencia apropiada como definición de éxito. **Dónde buscarlo:** los capítulos sobre la definición de customer success. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 11 · Marketplaces](class-11-marketplaces.md) · [Índice de la parte](README.md) · [Clase 13 · Economía del e-commerce](class-13-economia-del-e-commerce.md) →
