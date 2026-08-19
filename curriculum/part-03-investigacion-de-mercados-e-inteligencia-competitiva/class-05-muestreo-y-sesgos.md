---
title: "Muestreo y sesgos"
type: class
language: es
standard: clase-profunda-v2
part: 03
class: 05
level: Fundamentos
mastery_threshold: 80
estimated_minutes: 150
sources: ["malhotra", "provost", "hubbard", "kohavi"]
anchors: {"hubbard": "dilema-medicion", "kohavi": "confianza", "malhotra": "muestreo", "provost": "asociacion-causalidad"}
updated: 2026-08-19
---

# Clase 03.05 — Muestreo y sesgos

Clase 5 de 14 de la parte [03 — Investigación de mercados e inteligencia competitiva](README.md), de nivel Fundamentos. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 03.04, *Diseño de encuestas*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de cobertura del marco muestral con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** Los métodos de muestreo probabilístico y no probabilístico y su efecto en la inferencia — Naresh K. Malhotra. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

El error más caro de la investigación comercial no está en el análisis sino en quién quedó dentro de la muestra. Encuestar a la base de clientes actuales para entender por qué el mercado no compra es un ejemplo de sesgo de supervivencia. La muestra por conveniencia no es necesariamente inválida, pero obliga a declarar sus límites y a no extrapolar a la población. Un informe honesto describe a quién representa y a quién no.

La clase trata el tema como un problema de evidencia y de consecuencia, no como vocabulario. La parte 03 busca **producir investigación que cambie una decisión y resista una auditoría metodológica**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **muestreo y sesgos** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué evidencia mínima necesito para decidir, y qué sesgo podría estar produciéndola?

Los conceptos que estructuran la sesión son **marco muestral**, **sesgo de selección**, **sesgo de supervivencia** y **no respuesta informativa**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `marco muestral`, `sesgo de selección`, `sesgo de supervivencia` y `no respuesta informativa` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Investigación de mercados e inteligencia competitiva**.
3. **Aplicar** la secuencia **definir la población objetivo con precisión → describir el marco muestral y sus exclusiones → elegir el método de selección y justificarlo → estimar quién queda fuera y cómo podría diferir → declarar los límites de extrapolación en el informe** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **cobertura del marco muestral**, **diferencia entre respondentes y no respondentes** y **intervalo de confianza declarado** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **marco muestral** y **sesgo de selección** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **cobertura del marco muestral**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **marco muestral** | lista o mecanismo desde el cual se seleccionan los participantes | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **sesgo de selección** | diferencia sistemática entre quienes participan y quienes no, relacionada con la variable estudiada | Da un hecho compatible con la definición y otro que la refute. |
| **sesgo de supervivencia** | error de observar sólo los casos que permanecieron y concluir sobre todos | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **no respuesta informativa** | situación en que quienes no responden difieren sistemáticamente de quienes sí responden | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir la población objetivo con precisión → 2. describir el marco muestral y sus exclusiones → 3. elegir el método de selección y justificarlo → 4. estimar quién queda fuera y cómo podría diferir → 5. declarar los límites de extrapolación en el informe
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** En segmentos B2B pequeños la aleatorización pura suele ser imposible. La alternativa correcta no es fingirla sino documentar el criterio de selección y sus consecuencias.

## 📖 Desarrollo

### 1. Marco muestral: mecanismo central

**Marco muestral** se entiende aquí como **lista o mecanismo desde el cual se seleccionan los participantes**.

El marco muestral es la lista concreta desde la que se extrae la muestra, y casi todos los problemas de representatividad viven ahí y no en el tamaño. Si el marco es la base de clientes actuales, ninguna muestra dirá nada sobre quienes no compraron. Es un error tan común como invisible: se reporta el margen de error del muestreo mientras el sesgo del marco, mucho mayor, queda sin mencionar.

**De dónde viene esta afirmación.** Naresh K. Malhotra — *Marketing Research: An Applied Orientation* (2019, 7.ª ed.) aporta la idea que sostiene este bloque: los métodos de muestreo probabilístico y no probabilístico y su efecto en la inferencia. Búscala en los capítulos sobre diseño y tamaño de muestra. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «cobertura del marco muestral» debería moverse cuando cambie **marco muestral**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **sesgo de selección**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Sesgo de selección: frontera conceptual y error de clasificación

**Definición operacional:** diferencia sistemática entre quienes participan y quienes no, relacionada con la variable estudiada. Su valor está en distinguirlo de **marco muestral**.

El sesgo de supervivencia es la versión más costosa del anterior. Estudiar sólo a los clientes que permanecen para entender qué produce permanencia es circular: los que se fueron tenían justamente la información que falta. En análisis comercial aparece constantemente —se analizan negocios ganados para aprender a ganar— y produce conclusiones seguras y equivocadas.

**Contraste bibliográfico.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta aquí una distinción concreta: la distinción entre correlación observada y causalidad y qué exige cada una (los capítulos sobre inferencia y sesgo). Formula dos mini-casos: uno que satisface la definición de **sesgo de selección** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «describir el marco muestral y sus exclusiones», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Sesgo de supervivencia: operacionalización y medición

**Sesgo de supervivencia** significa **error de observar sólo los casos que permanecieron y concluir sobre todos**.

La no respuesta informativa se detecta comparando a quienes respondieron con la población conocida. Si los clientes con incidencias abiertas responden menos, la satisfacción medida está inflada por construcción. La corrección no siempre es posible, pero la declaración sí lo es: el informe debe indicar quién quedó subrepresentado y en qué dirección eso mueve el resultado.

Ficha de medición obligatoria para **cobertura del marco muestral**: `unidades de la población objetivo presentes en el marco, sobre población estimada`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) pone una condición sobre la medición: lo que parece inmedible suele estar mal definido, no ser inmedible (los capítulos sobre el problema de la medición). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. No respuesta informativa: trade-offs y efectos de segundo orden

**Definición:** situación en que quienes no responden difieren sistemáticamente de quienes sí responden.

Muestras mayores reducen el error aleatorio y no corrigen el sesgo; de hecho, lo vuelven más peligroso, porque un resultado sesgado con intervalo estrecho se presenta con más confianza. Invertir en tamaño cuando el problema es el marco es gastar en precisión sobre una medición inexacta. La prioridad de gasto es siempre marco primero, tamaño después.

**Lo que aporta la fuente.** Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) aporta el criterio para pesar el intercambio: las condiciones que hacen confiable un experimento en línea (los capítulos sobre experimentos confiables). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **intervalo de confianza declarado** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **no respuesta informativa** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «declarar los límites de extrapolación en el informe», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El muestreo probabilístico exige un marco completo y acceso aleatorio, condiciones que rara vez se cumplen en investigación comercial B2B con universos pequeños. En esos casos, la salida honesta es declarar que la muestra es por conveniencia y limitar las conclusiones a descripción, sin presentar márgenes de error que suponen un diseño que no se usó.

**Frontera declarada.** En segmentos B2B pequeños la aleatorización pura suele ser imposible. La alternativa correcta no es fingirla sino documentar el criterio de selección y sus consecuencias. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Investigar para confirmar una decisión ya tomada y presentar el resultado como hallazgo.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar muestreo y sesgos no consiste en sumar definiciones. Empieza por **marco muestral**, contrasta **sesgo de selección** con **sesgo de supervivencia**, incorpora **no respuesta informativa** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Naresh K. Malhotra — *Marketing Research: An Applied Orientation* (2019, 7.ª ed.) | Los métodos de muestreo probabilístico y no probabilístico y su efecto en la inferencia | Los capítulos sobre diseño y tamaño de muestra | ¿Qué debería observarse en **marco muestral** si aquí opera «los métodos de muestreo probabilístico y no probabilístico y su efecto en la inferencia»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La distinción entre correlación observada y causalidad y qué exige cada una | Los capítulos sobre inferencia y sesgo | ¿Qué debería observarse en **sesgo de selección** si aquí opera «la distinción entre correlación observada y causalidad y qué exige cada una»? ¿Y qué observación lo desmentiría en este caso? |
| Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) | Lo que parece inmedible suele estar mal definido, no ser inmedible | Los capítulos sobre el problema de la medición | ¿Qué debería observarse en **sesgo de supervivencia** si aquí opera «lo que parece inmedible suele estar mal definido, no ser inmedible»? ¿Y qué observación lo desmentiría en este caso? |
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | Las condiciones que hacen confiable un experimento en línea | Los capítulos sobre experimentos confiables | ¿Qué debería observarse en **no respuesta informativa** si aquí opera «las condiciones que hacen confiable un experimento en línea»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina concluye que «el precio no es un problema» a partir de una encuesta enviada sólo a clientes activos. Los que se fueron por precio, por definición, no estaban en la lista.

**Paso 1 — Definir la población objetivo con precisión.** El equipo escribe primero el supuesto asociado a **marco muestral** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **cobertura del marco muestral** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Describir el marco muestral y sus exclusiones.** El trabajo aquí es separar lo observado de lo inferido sobre **sesgo de selección**. La evidencia que ordena la discusión es **diferencia entre respondentes y no respondentes**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Elegir el método de selección y justificarlo.** El riesgo de este paso es cerrar demasiado rápido alrededor de **sesgo de supervivencia**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **intervalo de confianza declarado** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Estimar quién queda fuera y cómo podría diferir.** Con **no respuesta informativa** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **cobertura del marco muestral** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Declarar los límites de extrapolación en el informe.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **marco muestral**. **diferencia entre respondentes y no respondentes** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **marco muestral** | Lista o mecanismo desde el cual se seleccionan los participantes | Cuando **cobertura del marco muestral** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **sesgo de selección** | Diferencia sistemática entre quienes participan y quienes no, relacionada con la variable estudiada | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** En segmentos B2B pequeños la aleatorización pura suele ser imposible. La alternativa correcta no es fingirla sino documentar el criterio de selección y sus consecuencias.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre muestreo y sesgos |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Market researcher, Product marketing y Consultor comercial. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina concluye que «el precio no es un problema» a partir de una encuesta enviada sólo a clientes activos. Los que se fueron por precio, por definición, no estaban en la lista.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir la población objetivo con precisión → describir el marco muestral y sus exclusiones → elegir el método de selección y justificarlo → estimar quién queda fuera y cómo podría diferir → declarar los límites de extrapolación en el informe** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **cobertura del marco muestral**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Marketing Research: An Applied Orientation* y la de *Data Science for Business*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **marco muestral** y **sesgo de selección** como sinónimos | Se perdió la distinción entre «lista o mecanismo desde el cual se seleccionan los participantes» y «diferencia sistemática entre quienes participan y quienes no, relacionada con la variable estudiada» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «declarar los límites de extrapolación en el informe» | Se saltó «definir la población objetivo con precisión»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **cobertura del marco muestral** | La métrica local reemplazó al resultado del sistema | Contrástala con **intervalo de confianza declarado** y explicita el costo de oportunidad. |
| Extrapolar desde la base de clientes al mercado | Error específico de esta clase | Incluye no clientes y clientes perdidos en el marco muestral cuando la pregunta es sobre el mercado. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **marco muestral** y **sesgo de selección** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **sesgo de supervivencia** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir la población objetivo con precisión» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **cobertura del marco muestral** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «En segmentos B2B pequeños la aleatorización pura suele ser imposible. La alternativa correcta no es fingirla sino documentar el criterio de selección y sus consecuencias»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **sesgo de supervivencia** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **cobertura del marco muestral**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Marketing Research: An Applied Orientation* y *Trustworthy Online Controlled Experiments*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Investigar para confirmar una decisión ya tomada y presentar el resultado como hallazgo.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P03-C05-muestreo-y-sesgos/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **cobertura del marco muestral**, **diferencia entre respondentes y no respondentes** y **intervalo de confianza declarado** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **informe de oportunidad de mercado con método, muestra, límites y decisión recomendada**.

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

- Naresh K. Malhotra — [*Marketing Research: An Applied Orientation*](https://openlibrary.org/isbn/9781292265636) (2019, 7.ª ed.) · ISBN 9781292265636 — **aporta a esta clase:** los métodos de muestreo probabilístico y no probabilístico y su efecto en la inferencia. **Dónde buscarlo:** los capítulos sobre diseño y tamaño de muestra. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) · ISBN 9781449374280 — **aporta a esta clase:** la distinción entre correlación observada y causalidad y qué exige cada una. **Dónde buscarlo:** los capítulos sobre inferencia y sesgo. Registra edición y páginas consultadas en tu nota de lectura.
- Douglas W. Hubbard — [*How to Measure Anything*](https://openlibrary.org/isbn/9781118836446) (2014, 3.ª ed.) · ISBN 9781118836446 — **aporta a esta clase:** lo que parece inmedible suele estar mal definido, no ser inmedible. **Dónde buscarlo:** los capítulos sobre el problema de la medición. Registra edición y páginas consultadas en tu nota de lectura.
- Ron Kohavi, Diane Tang y Ya Xu — [*Trustworthy Online Controlled Experiments*](https://openlibrary.org/isbn/9781108601375) (2020) · ISBN 9781108601375 — **aporta a esta clase:** las condiciones que hacen confiable un experimento en línea. **Dónde buscarlo:** los capítulos sobre experimentos confiables. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 04 · Diseño de encuestas](class-04-diseno-de-encuestas.md) · [Índice de la parte](README.md) · [Clase 06 · Investigación cualitativa](class-06-investigacion-cualitativa.md) →
