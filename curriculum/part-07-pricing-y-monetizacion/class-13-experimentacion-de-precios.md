---
title: "Experimentación de precios"
type: class
language: es
standard: clase-profunda-v2
part: 07
class: 13
level: Oferta comercial
mastery_threshold: 80
estimated_minutes: 150
sources: ["kohavi", "nagle", "provost", "simon"]
anchors: {"kohavi": "guardarrailes", "nagle": "politica", "provost": "evaluacion", "simon": "psicologia-precio"}
updated: 2026-08-19
---

# Clase 07.13 — Experimentación de precios

Clase 13 de 14 de la parte [07 — Pricing y monetización](README.md), de nivel Oferta comercial. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 07.12, *Unit economics*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de efecto en conversión con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** Las métricas guardarraíl que impiden ganar en lo local perdiendo en el sistema — Ron Kohavi, Diane Tang y Ya Xu. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Experimentar con precios es la forma más directa de reducir incertidumbre y la que más consecuencias tiene sobre clientes reales. Un experimento válido requiere grupos comparables, tamaño suficiente, duración que cubra el ciclo de compra y métricas guardrail sobre churn y reclamos. Kohavi advierte sobre las trampas: detener la prueba al ver un resultado favorable o cambiar el criterio a mitad de camino invalida la conclusión.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 07 busca **diseñar una arquitectura de precios que capture valor sin destruir demanda ni confianza**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **experimentación de precios** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Cuánto vale esto para quién, y qué estructura de cobro alinea precio con valor entregado?

Los conceptos que estructuran la sesión son **grupo de comparación**, **métrica guardrail**, **duración mínima** y **detención prematura**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `grupo de comparación`, `métrica guardrail`, `duración mínima` y `detención prematura` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Pricing y monetización**.
3. **Aplicar** la secuencia **definir hipótesis, métrica principal y guardarraíles → calcular tamaño y duración mínima antes de iniciar → asignar grupos de forma comparable y documentada → no modificar criterios durante la ejecución → decidir con el criterio previo y registrar el aprendizaje** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **efecto en conversión**, **efecto en ingreso por visitante** y **guardarraíl de reclamos** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **grupo de comparación** y **métrica guardrail** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **efecto en conversión**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **grupo de comparación** | conjunto equivalente que no recibe el cambio y permite estimar el efecto | Construye un caso límite donde el concepto se confunde con el anterior. |
| **métrica guardrail** | indicador que no debe deteriorarse aunque mejore la métrica principal | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **duración mínima** | tiempo necesario para cubrir el ciclo completo de decisión del segmento | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **detención prematura** | interrupción del experimento al observar un resultado favorable transitorio | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir hipótesis, métrica principal y guardarraíles → 2. calcular tamaño y duración mínima antes de iniciar → 3. asignar grupos de forma comparable y documentada → 4. no modificar criterios durante la ejecución → 5. decidir con el criterio previo y registrar el aprendizaje
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Cobrar precios distintos a clientes equivalentes por asignación aleatoria plantea un problema ético y de trato justo. Los experimentos deben tener criterio de equidad y compensación definida.

## 📖 Desarrollo

### 1. Grupo de comparación: mecanismo central

**Grupo de comparación** se entiende aquí como **conjunto equivalente que no recibe el cambio y permite estimar el efecto**.

Experimentar con precios es distinto de experimentar con una página: el precio afecta a clientes reales, deja precedentes y puede tener implicancias contractuales. Por eso el diseño exige más cuidado que un test de conversión habitual, y por eso muchas empresas terminan cambiando precio sin medir, que es el peor de los mundos.

**De dónde viene esta afirmación.** Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) aporta la idea que sostiene este bloque: las métricas guardarraíl que impiden ganar en lo local perdiendo en el sistema. Búscala en los capítulos sobre métricas y guardarraíles. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «efecto en conversión» debería moverse cuando cambie **grupo de comparación**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **métrica guardrail**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Métrica guardrail: frontera conceptual y error de clasificación

**Definición operacional:** indicador que no debe deteriorarse aunque mejore la métrica principal. Su valor está en distinguirlo de **grupo de comparación**.

El grupo de comparación es lo que convierte un cambio en un experimento. Sin él, la variación observada puede deberse a estacionalidad, a una campaña o al mercado. En pricing, construir el grupo de comparación suele requerir separar por cohorte de ingreso o por mercado geográfico, y esa decisión debe documentarse antes de empezar.

**Contraste bibliográfico.** Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) aporta aquí una distinción concreta: la política de precios como sistema de reglas que evita negociar cada caso (el capítulo sobre política y disciplina de precios). Formula dos mini-casos: uno que satisface la definición de **métrica guardrail** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «calcular tamaño y duración mínima antes de iniciar», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Duración mínima: operacionalización y medición

**Duración mínima** significa **tiempo necesario para cubrir el ciclo completo de decisión del segmento**.

Las métricas guardarraíl son obligatorias en pruebas de precio: además del ingreso, hay que vigilar tasa de conversión, mezcla de planes, volumen de reclamos y bajas. Un alza que mejora el ingreso del mes y dispara las bajas del trimestre siguiente aparece como éxito si sólo se mira la primera métrica. La ventana de evaluación debe cubrir el efecto rezagado.

Ficha de medición obligatoria para **efecto en conversión**: `diferencia de conversión entre grupos, con intervalo de confianza`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) pone una condición sobre la medición: la evaluación contra una línea base y no contra la nada (los capítulos sobre evaluación de modelos). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Detención prematura: trade-offs y efectos de segundo orden

**Definición:** interrupción del experimento al observar un resultado favorable transitorio.

Detener un experimento cuando el resultado es favorable es el error más frecuente y el más costoso, porque garantiza quedarse con los falsos positivos. La disciplina exige fijar la duración y el tamaño antes de empezar y respetarlos. En pricing esa disciplina cuesta más porque la presión por consolidar un buen número es alta.

**Lo que aporta la fuente.** Hermann Simon — *Confessions of the Pricing Man* (2015) aporta el criterio para pesar el intercambio: los efectos psicológicos del precio y su uso responsable (los capítulos sobre psicología del precio). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **guardarraíl de reclamos** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **detención prematura** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «decidir con el criterio previo y registrar el aprendizaje», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Un resultado de experimento de precio vale para el segmento, el momento y el contexto competitivo en que se obtuvo. Extenderlo a toda la base o a otro mercado es una nueva hipótesis. Además, si el experimento implicó condiciones distintas para clientes comparables, corresponde revisar su legitimidad antes de repetirlo a escala.

**Frontera declarada.** Cobrar precios distintos a clientes equivalentes por asignación aleatoria plantea un problema ético y de trato justo. Los experimentos deben tener criterio de equidad y compensación definida. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar experimentación de precios no consiste en sumar definiciones. Empieza por **grupo de comparación**, contrasta **métrica guardrail** con **duración mínima**, incorpora **detención prematura** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | Las métricas guardarraíl que impiden ganar en lo local perdiendo en el sistema | Los capítulos sobre métricas y guardarraíles | ¿Qué debería observarse en **grupo de comparación** si aquí opera «las métricas guardarraíl que impiden ganar en lo local perdiendo en el sistema»? ¿Y qué observación lo desmentiría en este caso? |
| Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) | La política de precios como sistema de reglas que evita negociar cada caso | El capítulo sobre política y disciplina de precios | ¿Qué debería observarse en **métrica guardrail** si aquí opera «la política de precios como sistema de reglas que evita negociar cada caso»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La evaluación contra una línea base y no contra la nada | Los capítulos sobre evaluación de modelos | ¿Qué debería observarse en **duración mínima** si aquí opera «la evaluación contra una línea base y no contra la nada»? ¿Y qué observación lo desmentiría en este caso? |
| Hermann Simon — *Confessions of the Pricing Man* (2015) | Los efectos psicológicos del precio y su uso responsable | Los capítulos sobre psicología del precio | ¿Qué debería observarse en **detención prematura** si aquí opera «los efectos psicológicos del precio y su uso responsable»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina probó un alza de 15 % durante nueve días y observó mejora en ingreso. Su ciclo mediano de decisión es 34 días, por lo que la prueba midió sólo a los compradores más rápidos.

**Paso 1 — Definir hipótesis, métrica principal y guardarraíles.** El equipo escribe primero el supuesto asociado a **grupo de comparación** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **efecto en conversión** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Calcular tamaño y duración mínima antes de iniciar.** El trabajo aquí es separar lo observado de lo inferido sobre **métrica guardrail**. La evidencia que ordena la discusión es **efecto en ingreso por visitante**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Asignar grupos de forma comparable y documentada.** El riesgo de este paso es cerrar demasiado rápido alrededor de **duración mínima**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **guardarraíl de reclamos** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — No modificar criterios durante la ejecución.** Con **detención prematura** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **efecto en conversión** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Decidir con el criterio previo y registrar el aprendizaje.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **grupo de comparación**. **efecto en ingreso por visitante** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **grupo de comparación** | Conjunto equivalente que no recibe el cambio y permite estimar el efecto | Cuando **efecto en conversión** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **métrica guardrail** | Indicador que no debe deteriorarse aunque mejore la métrica principal | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Cobrar precios distintos a clientes equivalentes por asignación aleatoria plantea un problema ético y de trato justo. Los experimentos deben tener criterio de equidad y compensación definida.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre experimentación de precios |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Pricing manager, Product marketing, CFO comercial y Founder. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina probó un alza de 15 % durante nueve días y observó mejora en ingreso. Su ciclo mediano de decisión es 34 días, por lo que la prueba midió sólo a los compradores más rápidos.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir hipótesis, métrica principal y guardarraíles → calcular tamaño y duración mínima antes de iniciar → asignar grupos de forma comparable y documentada → no modificar criterios durante la ejecución → decidir con el criterio previo y registrar el aprendizaje** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **efecto en conversión**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Trustworthy Online Controlled Experiments* y la de *The Strategy and Tactics of Pricing*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **grupo de comparación** y **métrica guardrail** como sinónimos | Se perdió la distinción entre «conjunto equivalente que no recibe el cambio y permite estimar el efecto» y «indicador que no debe deteriorarse aunque mejore la métrica principal» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «decidir con el criterio previo y registrar el aprendizaje» | Se saltó «definir hipótesis, métrica principal y guardarraíles»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **efecto en conversión** | La métrica local reemplazó al resultado del sistema | Contrástala con **guardarraíl de reclamos** y explicita el costo de oportunidad. |
| Detener el experimento al ver un resultado favorable | Error específico de esta clase | Fija duración y tamaño antes de iniciar y no evalúes resultados parciales como definitivos. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **grupo de comparación** y **métrica guardrail** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **duración mínima** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir hipótesis, métrica principal y guardarraíles» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **efecto en conversión** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Cobrar precios distintos a clientes equivalentes por asignación aleatoria plantea un problema ético y de trato justo. Los experimentos deben tener criterio de equidad y compensación definida»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **duración mínima** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **efecto en conversión**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Trustworthy Online Controlled Experiments* y *Confessions of the Pricing Man*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P07-C13-experimentacion-de-precios/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **efecto en conversión**, **efecto en ingreso por visitante** y **guardarraíl de reclamos** con fuente, ventana y lectura prohibida.
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

Estas son las obras sobre las que se apoya lo que acabas de leer. Cada una aparece con la idea concreta que aporta a esta clase, dónde buscarla dentro del libro y el enlace donde se resuelve la edición exacta. Si al leer no encuentras esa idea, la cita está mal puesta y corresponde reportarlo como error del material.

- Ron Kohavi, Diane Tang y Ya Xu — [*Trustworthy Online Controlled Experiments*](https://openlibrary.org/isbn/9781108601375) (2020) · ISBN 9781108601375 — **aporta a esta clase:** las métricas guardarraíl que impiden ganar en lo local perdiendo en el sistema. **Dónde buscarlo:** los capítulos sobre métricas y guardarraíles. Registra edición y páginas consultadas en tu nota de lectura.
- Thomas T. Nagle y Georg Müller — [*The Strategy and Tactics of Pricing*](https://openlibrary.org/isbn/9781138737501) (2018, 6.ª ed.) · ISBN 9781138737501 — **aporta a esta clase:** la política de precios como sistema de reglas que evita negociar cada caso. **Dónde buscarlo:** el capítulo sobre política y disciplina de precios. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) · ISBN 9781449374280 — **aporta a esta clase:** la evaluación contra una línea base y no contra la nada. **Dónde buscarlo:** los capítulos sobre evaluación de modelos. Registra edición y páginas consultadas en tu nota de lectura.
- Hermann Simon — [*Confessions of the Pricing Man*](https://openlibrary.org/isbn/9783319204000) (2015) · ISBN 9783319204000 — **aporta a esta clase:** los efectos psicológicos del precio y su uso responsable. **Dónde buscarlo:** los capítulos sobre psicología del precio. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 12 · Unit economics](class-12-unit-economics.md) · [Índice de la parte](README.md) · [Clase 14 · Arquitectura de monetización](class-14-arquitectura-de-monetizacion.md) →
