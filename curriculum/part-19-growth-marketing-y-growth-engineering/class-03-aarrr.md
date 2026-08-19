---
title: "AARRR"
type: class
language: es
standard: clase-profunda-v2
part: 19
class: 03
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["croll-yoskovitz", "ellis-brown", "kaushik", "bush-plg"]
anchors: {"bush-plg": "moment-value", "croll-yoskovitz": "etapas", "ellis-brown": "ciclo", "kaushik": "segmentacion"}
updated: 2026-08-19
---

# Clase 19.03 — AARRR

**Parte 19 · Growth marketing y growth engineering** · Nivel: Crecimiento y analítica · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 19.02 — *North Star Metric*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de conversión por etapa del marco para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** Las cinco etapas —empatía, adherencia, viralidad, ingreso y escala— con su métrica propia — Alistair Croll y Benjamin Yoskovitz. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

El marco de adquisición, activación, retención, referencia e ingreso ordena el recorrido en etapas medibles y facilita localizar el cuello de botella. Su riesgo es tratarlo como secuencia obligatoria y trabajar la adquisición primero por costumbre. La regla práctica es la contraria: en la mayoría de los negocios, trabajar retención y activación antes que adquisición produce más efecto por peso invertido.

Antes de cualquier herramienta, esta clase obliga a nombrar qué cambiaría si el análisis fuese correcto. La parte 19 busca **instalar un motor de experimentación que produzca aprendizaje acumulativo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **AARRR** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué bucle hace que el crecimiento se retroalimente en lugar de depender del gasto?

Los conceptos que estructuran la sesión son **etapa del marco**, **cuello de botella**, **orden de intervención** y **métrica por etapa**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `etapa del marco`, `cuello de botella`, `orden de intervención` y `métrica por etapa` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Growth marketing y growth engineering**.
3. **Aplicar** la secuencia **instrumentar una métrica por etapa → medir volumen y conversión en cada una → identificar el cuello de botella con datos → estimar el efecto de mejorar cada etapa → intervenir donde el efecto por peso invertido es mayor** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **conversión por etapa del marco**, **efecto simulado por etapa** y **cobertura de instrumentación** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **etapa del marco** y **cuello de botella** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **conversión por etapa del marco**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **etapa del marco** | estado medible del recorrido del cliente dentro del modelo | Construye un caso límite donde el concepto se confunde con el anterior. |
| **cuello de botella** | etapa que limita el resultado agregado del sistema | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **orden de intervención** | secuencia de trabajo derivada del diagnóstico y no de la costumbre | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **métrica por etapa** | indicador con definición operacional propio de cada estado | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. instrumentar una métrica por etapa → 2. medir volumen y conversión en cada una → 3. identificar el cuello de botella con datos → 4. estimar el efecto de mejorar cada etapa → 5. intervenir donde el efecto por peso invertido es mayor
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** El marco supone un recorrido lineal que no siempre existe. En negocios con compra por comité o ciclos largos, algunas etapas se superponen.

## 📖 Desarrollo

### 1. Etapa del marco: mecanismo central

**Etapa del marco** se entiende aquí como **estado medible del recorrido del cliente dentro del modelo**.

El marco de adquisición, activación, retención, ingreso y recomendación ordena el recorrido en etapas medibles. Su utilidad principal es diagnóstica: permite localizar dónde está el cuello de botella antes de decidir dónde invertir. Aplicarlo como lista de iniciativas —una por etapa— desaprovecha exactamente lo que aporta.

**De dónde viene esta afirmación.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) aporta la idea que sostiene este bloque: las cinco etapas —empatía, adherencia, viralidad, ingreso y escala— con su métrica propia. Búscala en la parte sobre etapas del negocio. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «conversión por etapa del marco» debería moverse cuando cambie **etapa del marco**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **cuello de botella**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Cuello de botella: frontera conceptual y error de clasificación

**Definición operacional:** etapa que limita el resultado agregado del sistema. Su valor está en distinguirlo de **etapa del marco**.

El cuello de botella es la etapa cuya mejora produce el mayor efecto sobre el resultado final, y rara vez es la de peor porcentaje. Identificarlo exige calcular el efecto de una mejora equivalente en cada etapa sobre el resultado, y ese cálculo suele contradecir la intuición del equipo.

**Contraste bibliográfico.** Sean Ellis y Morgan Brown — *Hacking Growth* (2017) aporta aquí una distinción concreta: el ciclo de crecimiento: analizar, idear, priorizar y probar, ejecutado con ritmo fijo (los capítulos sobre el proceso de experimentación). Formula dos mini-casos: uno que satisface la definición de **cuello de botella** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «medir volumen y conversión en cada una», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Orden de intervención: operacionalización y medición

**Orden de intervención** significa **secuencia de trabajo derivada del diagnóstico y no de la costumbre**.

El orden de intervención importa: mejorar la adquisición cuando la activación falla amplifica la pérdida. La regla práctica es trabajar de atrás hacia adelante —retención antes que adquisición— salvo que el volumen sea tan bajo que no permita medir nada, que es la excepción legítima.

Ficha de medición obligatoria para **conversión por etapa del marco**: `unidades que avanzan, sobre unidades que ingresaron a la etapa`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Avinash Kaushik — *Web Analytics 2.0* (2009) pone una condición sobre la medición: la segmentación como condición para que un promedio signifique algo (el capítulo sobre segmentación de datos). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Métrica por etapa: trade-offs y efectos de segundo orden

**Definición:** indicador con definición operacional propio de cada estado.

Optimizar una etapa puede deteriorar la siguiente: facilitar el registro puede traer usuarios que no activan. Por eso las métricas por etapa deben leerse en cadena y no de forma aislada. Un tablero que muestra cada etapa por separado, sin la conversión entre ellas, induce exactamente ese error.

**Lo que aporta la fuente.** Wes Bush — *Product-Led Growth* (2019) aporta el criterio para pesar el intercambio: el momento de valor y su distancia respecto del registro (los capítulos sobre tiempo hasta el valor). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **cobertura de instrumentación** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **métrica por etapa** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «intervenir donde el efecto por peso invertido es mayor», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El marco supone un recorrido secuencial que muchos negocios no siguen: hay clientes que recomiendan antes de pagar, o que pagan antes de activar. Forzar la secuencia produce categorías artificiales. Su valor está en la disciplina de medir cada transición, no en la literalidad del orden.

**Frontera declarada.** El marco supone un recorrido lineal que no siempre existe. En negocios con compra por comité o ciclos largos, algunas etapas se superponen. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar AARRR no consiste en sumar definiciones. Empieza por **etapa del marco**, contrasta **cuello de botella** con **orden de intervención**, incorpora **métrica por etapa** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | Las cinco etapas —empatía, adherencia, viralidad, ingreso y escala— con su métrica propia | La parte sobre etapas del negocio | ¿Qué debería observarse en **etapa del marco** si aquí opera «las cinco etapas —empatía, adherencia, viralidad, ingreso y escala— con su métrica propia»? ¿Y qué observación lo desmentiría en este caso? |
| Sean Ellis y Morgan Brown — *Hacking Growth* (2017) | El ciclo de crecimiento: analizar, idear, priorizar y probar, ejecutado con ritmo fijo | Los capítulos sobre el proceso de experimentación | ¿Qué debería observarse en **cuello de botella** si aquí opera «el ciclo de crecimiento: analizar, idear, priorizar y probar, ejecutado con ritmo fijo»? ¿Y qué observación lo desmentiría en este caso? |
| Avinash Kaushik — *Web Analytics 2.0* (2009) | La segmentación como condición para que un promedio signifique algo | El capítulo sobre segmentación de datos | ¿Qué debería observarse en **orden de intervención** si aquí opera «la segmentación como condición para que un promedio signifique algo»? ¿Y qué observación lo desmentiría en este caso? |
| Wes Bush — *Product-Led Growth* (2019) | El momento de valor y su distancia respecto del registro | Los capítulos sobre tiempo hasta el valor | ¿Qué debería observarse en **métrica por etapa** si aquí opera «el momento de valor y su distancia respecto del registro»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** La activación de Ruta Andina es 39 % y su conversión de visita a registro es 2,1 %. Duplicar la activación produce más clientes activos que duplicar el tráfico, a un costo menor.

**Paso 1 — Instrumentar una métrica por etapa.** El equipo escribe primero el supuesto asociado a **etapa del marco** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **conversión por etapa del marco** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Medir volumen y conversión en cada una.** El trabajo aquí es separar lo observado de lo inferido sobre **cuello de botella**. La evidencia que ordena la discusión es **efecto simulado por etapa**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Identificar el cuello de botella con datos.** El riesgo de este paso es cerrar demasiado rápido alrededor de **orden de intervención**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **cobertura de instrumentación** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Estimar el efecto de mejorar cada etapa.** Con **métrica por etapa** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **conversión por etapa del marco** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Intervenir donde el efecto por peso invertido es mayor.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **etapa del marco**. **efecto simulado por etapa** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **etapa del marco** | Estado medible del recorrido del cliente dentro del modelo | Cuando **conversión por etapa del marco** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **cuello de botella** | Etapa que limita el resultado agregado del sistema | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** El marco supone un recorrido lineal que no siempre existe. En negocios con compra por comité o ciclos largos, algunas etapas se superponen.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre AARRR |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager, Growth engineer y Head of Growth. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

La activación de Ruta Andina es 39 % y su conversión de visita a registro es 2,1 %. Duplicar la activación produce más clientes activos que duplicar el tráfico, a un costo menor.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **instrumentar una métrica por etapa → medir volumen y conversión en cada una → identificar el cuello de botella con datos → estimar el efecto de mejorar cada etapa → intervenir donde el efecto por peso invertido es mayor** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **conversión por etapa del marco**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Lean Analytics* y la de *Hacking Growth*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **etapa del marco** y **cuello de botella** como sinónimos | Se perdió la distinción entre «estado medible del recorrido del cliente dentro del modelo» y «etapa que limita el resultado agregado del sistema» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «intervenir donde el efecto por peso invertido es mayor» | Se saltó «instrumentar una métrica por etapa»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **conversión por etapa del marco** | La métrica local reemplazó al resultado del sistema | Contrástala con **cobertura de instrumentación** y explicita el costo de oportunidad. |
| Trabajar adquisición por costumbre | Error específico de esta clase | Simula el efecto de mejorar cada etapa y prioriza por resultado esperado sobre costo. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **etapa del marco** y **cuello de botella** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **orden de intervención** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «instrumentar una métrica por etapa» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **conversión por etapa del marco** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «El marco supone un recorrido lineal que no siempre existe. En negocios con compra por comité o ciclos largos, algunas etapas se superponen»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **orden de intervención** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **conversión por etapa del marco**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Lean Analytics* y *Product-Led Growth*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P19-C03-aarrr/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **conversión por etapa del marco**, **efecto simulado por etapa** y **cobertura de instrumentación** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **growth model con North Star, bucles, backlog priorizado y resultados de experimentos**.

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

- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — **aporta a esta clase:** las cinco etapas —empatía, adherencia, viralidad, ingreso y escala— con su métrica propia. **Dónde buscarlo:** la parte sobre etapas del negocio. Registra edición y páginas consultadas en tu nota de lectura.
- Sean Ellis y Morgan Brown — *Hacking Growth* (2017) — **aporta a esta clase:** el ciclo de crecimiento: analizar, idear, priorizar y probar, ejecutado con ritmo fijo. **Dónde buscarlo:** los capítulos sobre el proceso de experimentación. Registra edición y páginas consultadas en tu nota de lectura.
- Avinash Kaushik — *Web Analytics 2.0* (2009) — **aporta a esta clase:** la segmentación como condición para que un promedio signifique algo. **Dónde buscarlo:** el capítulo sobre segmentación de datos. Registra edición y páginas consultadas en tu nota de lectura.
- Wes Bush — *Product-Led Growth* (2019) — **aporta a esta clase:** el momento de valor y su distancia respecto del registro. **Dónde buscarlo:** los capítulos sobre tiempo hasta el valor. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 02 · North Star Metric](class-02-north-star-metric.md) · [Índice de la parte](README.md) · [Clase 04 · Growth loops](class-04-growth-loops.md) →
