---
title: "Disposición a pagar"
type: class
language: es
standard: clase-profunda-v2
part: 07
class: 05
level: Oferta comercial
mastery_threshold: 80
estimated_minutes: 150
sources: ["ramanujam", "nagle", "hubbard", "malhotra"]
anchors: {"hubbard": "calibracion", "malhotra": "cuestionario", "nagle": "sensibilidad", "ramanujam": "disposicion-pagar"}
updated: 2026-08-19
---

# Clase 07.05 — Disposición a pagar

**Parte 07 · Pricing y monetización** · Nivel: Oferta comercial · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 07.04 — *Pricing basado en valor*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de dispersión de la disposición declarada para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** Las técnicas de conversación sobre disposición a pagar con clientes reales — Madhavan Ramanujam y Georg Tacke. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La disposición a pagar es una distribución, no un número. Ramanujam sostiene que preguntarla temprano —antes de construir— evita el error más caro de la innovación: desarrollar algo que nadie pagará. Las técnicas van desde preguntas directas calibradas hasta análisis de compensación; todas tienen sesgos y ninguna reemplaza la observación de decisiones reales con precio real.

La clase trata el tema como un problema de evidencia y de consecuencia, no como vocabulario. La parte 07 busca **diseñar una arquitectura de precios que capture valor sin destruir demanda ni confianza**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **disposición a pagar** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Cuánto vale esto para quién, y qué estructura de cobro alinea precio con valor entregado?

Los conceptos que estructuran la sesión son **distribución de disposición a pagar**, **sesgo de declaración**, **análisis de compensación** y **validación con decisión real**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `distribución de disposición a pagar`, `sesgo de declaración`, `análisis de compensación` y `validación con decisión real` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Pricing y monetización**.
3. **Aplicar** la secuencia **definir el segmento y la configuración a evaluar → elegir la técnica según presupuesto y precisión requerida → recoger la distribución y no sólo el promedio → corregir por sesgo de declaración → validar con una prueba de decisión real** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **dispersión de la disposición declarada**, **diferencia declaración-comportamiento** y **tasa de aceptación por nivel de precio** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **distribución de disposición a pagar** y **sesgo de declaración** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **dispersión de la disposición declarada**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **distribución de disposición a pagar** | rango de montos que distintos clientes del segmento pagarían | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **sesgo de declaración** | diferencia entre lo que el cliente dice que pagaría y lo que efectivamente paga | Da un hecho compatible con la definición y otro que la refute. |
| **análisis de compensación** | técnica que fuerza a elegir entre combinaciones de atributos y precio | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **validación con decisión real** | observación de compra efectiva con precio real como prueba final | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir el segmento y la configuración a evaluar → 2. elegir la técnica según presupuesto y precisión requerida → 3. recoger la distribución y no sólo el promedio → 4. corregir por sesgo de declaración → 5. validar con una prueba de decisión real
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Las técnicas declarativas sobreestiman sistemáticamente. Sirven para ordenar preferencias entre configuraciones, no para fijar el precio final.

## 📖 Desarrollo

### 1. Distribución de disposición a pagar: mecanismo central

**Distribución de disposición a pagar** se entiende aquí como **rango de montos que distintos clientes del segmento pagarían**.

La disposición a pagar no es un número por cliente sino una distribución en el mercado, y esa distribución es lo que justifica tener más de un plan. Pensarla como valor único lleva a buscar «el precio correcto», que no existe, en lugar de diseñar una estructura que capture distintos tramos de la distribución.

**De dónde viene esta afirmación.** Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) aporta la idea que sostiene este bloque: las técnicas de conversación sobre disposición a pagar con clientes reales. Búscala en el capítulo sobre cómo preguntar por el precio. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «dispersión de la disposición declarada» debería moverse cuando cambie **distribución de disposición a pagar**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **sesgo de declaración**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Sesgo de declaración: frontera conceptual y error de clasificación

**Definición operacional:** diferencia entre lo que el cliente dice que pagaría y lo que efectivamente paga. Su valor está en distinguirlo de **distribución de disposición a pagar**.

El sesgo de declaración es el problema central de cualquier medición directa: la gente subestima lo que pagaría cuando cree que eso influirá en el precio, y sobreestima cuando quiere ser amable. Por eso las preguntas directas sobre precio se usan como orientación gruesa y nunca como base de decisión sin contrastar con conducta.

**Contraste bibliográfico.** Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) aporta aquí una distinción concreta: los factores que aumentan o reducen la sensibilidad al precio y su gestión deliberada (el capítulo sobre sensibilidad al precio). Formula dos mini-casos: uno que satisface la definición de **sesgo de declaración** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «elegir la técnica según presupuesto y precisión requerida», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Análisis de compensación: operacionalización y medición

**Análisis de compensación** significa **técnica que fuerza a elegir entre combinaciones de atributos y precio**.

El análisis de compensación —pedir que elijan entre combinaciones de atributos y precio— evita el sesgo de la pregunta directa porque obliga a renunciar a algo. Requiere diseño cuidadoso y una muestra suficiente, y entrega la valoración relativa de los atributos, que suele ser más útil que el nivel absoluto de precio.

Ficha de medición obligatoria para **dispersión de la disposición declarada**: `rango intercuartil de los montos declarados por el segmento`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) pone una condición sobre la medición: la calibración de estimaciones subjetivas como habilidad entrenable (los capítulos sobre estimación calibrada). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Validación con decisión real: trade-offs y efectos de segundo orden

**Definición:** observación de compra efectiva con precio real como prueba final.

Investigar la disposición a pagar con rigor cuesta tiempo y dinero, y en mercados B2B pequeños puede ser inviable por tamaño de muestra. La alternativa practicable es la conversación estructurada con clientes reales sobre presupuestos y comparaciones, aceptando que entrega orientación y no precisión. Lo indefendible es no hacer ninguna de las dos y fijar precio por intuición.

**Lo que aporta la fuente.** Naresh K. Malhotra — *Marketing Research: An Applied Orientation* (2019, 7.ª ed.) aporta el criterio para pesar el intercambio: el diseño del cuestionario: orden, formulación y sesgo de respuesta (el capítulo sobre diseño de cuestionarios). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **tasa de aceptación por nivel de precio** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **validación con decisión real** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «validar con una prueba de decisión real», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La validación definitiva es la decisión de compra con precio real. Toda medición previa es una estimación cuya utilidad está en reducir el rango de prueba, no en reemplazarla. Un plan de pricing que no contempla cómo se validará en el mercado está confiando en la investigación más allá de lo que la investigación puede sostener.

**Frontera declarada.** Las técnicas declarativas sobreestiman sistemáticamente. Sirven para ordenar preferencias entre configuraciones, no para fijar el precio final. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar disposición a pagar no consiste en sumar definiciones. Empieza por **distribución de disposición a pagar**, contrasta **sesgo de declaración** con **análisis de compensación**, incorpora **validación con decisión real** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) | Las técnicas de conversación sobre disposición a pagar con clientes reales | El capítulo sobre cómo preguntar por el precio | ¿Qué debería observarse en **distribución de disposición a pagar** si aquí opera «las técnicas de conversación sobre disposición a pagar con clientes reales»? ¿Y qué observación lo desmentiría en este caso? |
| Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) | Los factores que aumentan o reducen la sensibilidad al precio y su gestión deliberada | El capítulo sobre sensibilidad al precio | ¿Qué debería observarse en **sesgo de declaración** si aquí opera «los factores que aumentan o reducen la sensibilidad al precio y su gestión deliberada»? ¿Y qué observación lo desmentiría en este caso? |
| Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) | La calibración de estimaciones subjetivas como habilidad entrenable | Los capítulos sobre estimación calibrada | ¿Qué debería observarse en **análisis de compensación** si aquí opera «la calibración de estimaciones subjetivas como habilidad entrenable»? ¿Y qué observación lo desmentiría en este caso? |
| Naresh K. Malhotra — *Marketing Research: An Applied Orientation* (2019, 7.ª ed.) | El diseño del cuestionario: orden, formulación y sesgo de respuesta | El capítulo sobre diseño de cuestionarios | ¿Qué debería observarse en **validación con decisión real** si aquí opera «el diseño del cuestionario: orden, formulación y sesgo de respuesta»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina preguntó «¿cuánto pagarías?» y obtuvo un promedio de CLP 120.000. Al presentar una propuesta real a ese precio, la aceptación fue de 6 %.

**Paso 1 — Definir el segmento y la configuración a evaluar.** El equipo escribe primero el supuesto asociado a **distribución de disposición a pagar** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **dispersión de la disposición declarada** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Elegir la técnica según presupuesto y precisión requerida.** El trabajo aquí es separar lo observado de lo inferido sobre **sesgo de declaración**. La evidencia que ordena la discusión es **diferencia declaración-comportamiento**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Recoger la distribución y no sólo el promedio.** El riesgo de este paso es cerrar demasiado rápido alrededor de **análisis de compensación**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **tasa de aceptación por nivel de precio** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Corregir por sesgo de declaración.** Con **validación con decisión real** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **dispersión de la disposición declarada** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Validar con una prueba de decisión real.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **distribución de disposición a pagar**. **diferencia declaración-comportamiento** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **distribución de disposición a pagar** | Rango de montos que distintos clientes del segmento pagarían | Cuando **dispersión de la disposición declarada** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **sesgo de declaración** | Diferencia entre lo que el cliente dice que pagaría y lo que efectivamente paga | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Las técnicas declarativas sobreestiman sistemáticamente. Sirven para ordenar preferencias entre configuraciones, no para fijar el precio final.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre disposición a pagar |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Pricing manager, Product marketing, CFO comercial y Founder. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina preguntó «¿cuánto pagarías?» y obtuvo un promedio de CLP 120.000. Al presentar una propuesta real a ese precio, la aceptación fue de 6 %.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir el segmento y la configuración a evaluar → elegir la técnica según presupuesto y precisión requerida → recoger la distribución y no sólo el promedio → corregir por sesgo de declaración → validar con una prueba de decisión real** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **dispersión de la disposición declarada**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Monetizing Innovation* y la de *The Strategy and Tactics of Pricing*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **distribución de disposición a pagar** y **sesgo de declaración** como sinónimos | Se perdió la distinción entre «rango de montos que distintos clientes del segmento pagarían» y «diferencia entre lo que el cliente dice que pagaría y lo que efectivamente paga» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «validar con una prueba de decisión real» | Se saltó «definir el segmento y la configuración a evaluar»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **dispersión de la disposición declarada** | La métrica local reemplazó al resultado del sistema | Contrástala con **tasa de aceptación por nivel de precio** y explicita el costo de oportunidad. |
| Fijar precio con el promedio de lo declarado | Error específico de esta clase | Usa la distribución completa y valida con una prueba de decisión real antes de publicar el precio. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **distribución de disposición a pagar** y **sesgo de declaración** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **análisis de compensación** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir el segmento y la configuración a evaluar» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **dispersión de la disposición declarada** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Las técnicas declarativas sobreestiman sistemáticamente. Sirven para ordenar preferencias entre configuraciones, no para fijar el precio final»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **análisis de compensación** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **dispersión de la disposición declarada**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Monetizing Innovation* y *Marketing Research: An Applied Orientation*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P07-C05-willingness-to-pay/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **dispersión de la disposición declarada**, **diferencia declaración-comportamiento** y **tasa de aceptación por nivel de precio** con fuente, ventana y lectura prohibida.
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

Cada obra aparece con la idea concreta que aporta a esta clase. Si al leer no encuentras esa idea, la cita está mal puesta y corresponde reportarlo como error del material.

- Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) — **aporta a esta clase:** las técnicas de conversación sobre disposición a pagar con clientes reales. **Dónde buscarlo:** el capítulo sobre cómo preguntar por el precio. Registra edición y páginas consultadas en tu nota de lectura.
- Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) — **aporta a esta clase:** los factores que aumentan o reducen la sensibilidad al precio y su gestión deliberada. **Dónde buscarlo:** el capítulo sobre sensibilidad al precio. Registra edición y páginas consultadas en tu nota de lectura.
- Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) — **aporta a esta clase:** la calibración de estimaciones subjetivas como habilidad entrenable. **Dónde buscarlo:** los capítulos sobre estimación calibrada. Registra edición y páginas consultadas en tu nota de lectura.
- Naresh K. Malhotra — *Marketing Research: An Applied Orientation* (2019, 7.ª ed.) — **aporta a esta clase:** el diseño del cuestionario: orden, formulación y sesgo de respuesta. **Dónde buscarlo:** el capítulo sobre diseño de cuestionarios. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 04 · Pricing basado en valor](class-04-value-based-pricing.md) · [Índice de la parte](README.md) · [Clase 06 · Elasticidad y sensibilidad al precio](class-06-elasticidad-y-sensibilidad.md) →
