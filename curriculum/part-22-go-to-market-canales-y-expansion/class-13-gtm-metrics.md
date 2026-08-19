---
title: "Métricas de go-to-market"
type: class
language: es
standard: clase-profunda-v2
part: 22
class: 13
level: IA y expansión
mastery_threshold: 80
estimated_minutes: 150
sources: ["croll-yoskovitz", "ross", "bush-plg", "kaplan-norton"]
anchors: {"bush-plg": "ocasion-upgrade", "croll-yoskovitz": "una-metrica", "kaplan-norton": "indicadores-causales", "ross": "pipeline-predecible"}
updated: 2026-08-19
---

# Clase 22.13 — Métricas de go-to-market

Clase 13 de 14 de la parte [22 — Go-to-market, canales y expansión](README.md), de nivel IA y expansión. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 22.12, *Internacionalización*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de eficiencia del crecimiento con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La métrica que importa ahora: una sola, según etapa y modelo de negocio — Alistair Croll y Benjamin Yoskovitz. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Evaluar una estrategia de salida al mercado exige métricas que capturen eficiencia y no sólo crecimiento: costo de adquisición por movimiento, periodo de recuperación, productividad por persona, contribución por canal y velocidad de escalamiento. Crecer perdiendo eficiencia no es un éxito comercial: es una apuesta financiera que alguien deberá pagar.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 22 busca **diseñar el modo en que la oferta llega al mercado y decide crecer**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **métricas de go-to-market** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué movimiento comercial corresponde al valor del contrato, al ciclo y al comprador?

Los conceptos que estructuran la sesión son **eficiencia del crecimiento**, **productividad por movimiento**, **contribución por canal** y **velocidad de escalamiento**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `eficiencia del crecimiento`, `productividad por movimiento`, `contribución por canal` y `velocidad de escalamiento` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Go-to-market, canales y expansión**.
3. **Aplicar** la secuencia **definir las métricas por movimiento y por canal → medir eficiencia además de crecimiento → comparar la eficiencia entre movimientos → identificar dónde la eficiencia se deteriora al escalar → ajustar la asignación según el resultado** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **eficiencia del crecimiento**, **periodo de recuperación por movimiento** y **deterioro de eficiencia al escalar** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **eficiencia del crecimiento** y **productividad por movimiento** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **eficiencia del crecimiento**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **eficiencia del crecimiento** | relación entre el ingreso incremental y el gasto necesario para producirlo | Construye un caso límite donde el concepto se confunde con el anterior. |
| **productividad por movimiento** | resultado obtenido por unidad de capacidad en cada movimiento comercial | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **contribución por canal** | margen que aporta cada canal después de sus costos | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **velocidad de escalamiento** | rapidez con que el movimiento puede aumentar su producción | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir las métricas por movimiento y por canal → 2. medir eficiencia además de crecimiento → 3. comparar la eficiencia entre movimientos → 4. identificar dónde la eficiencia se deteriora al escalar → 5. ajustar la asignación según el resultado
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** En etapas tempranas puede ser racional sacrificar eficiencia para ganar posición. Lo que no es racional es hacerlo sin declararlo ni medirlo.

## 📖 Desarrollo

### 1. Eficiencia del crecimiento: mecanismo central

**Eficiencia del crecimiento** se entiende aquí como **relación entre el ingreso incremental y el gasto necesario para producirlo**.

Las métricas de entrada al mercado deben medir eficiencia y no sólo volumen: cuánto cuesta crecer, cuánto tarda y qué proporción del crecimiento se retiene. Un crecimiento rápido con mala eficiencia es un problema que aparece después, cuando el capital que lo financiaba se agota.

**De dónde viene esta afirmación.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) aporta la idea que sostiene este bloque: la métrica que importa ahora: una sola, según etapa y modelo de negocio. Búscala en los capítulos sobre la métrica única. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «eficiencia del crecimiento» debería moverse cuando cambie **eficiencia del crecimiento**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **productividad por movimiento**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Productividad por movimiento: frontera conceptual y error de clasificación

**Definición operacional:** resultado obtenido por unidad de capacidad en cada movimiento comercial. Su valor está en distinguirlo de **eficiencia del crecimiento**.

La eficiencia del crecimiento relaciona el ingreso nuevo con el gasto que lo produjo, incluyendo todos los costos comerciales. Es la métrica que resume si el motor funciona. Su valor está en la comparación en el tiempo y entre movimientos comerciales, no en un umbral absoluto.

**Contraste bibliográfico.** Aaron Ross y Marylou Tyler — *Predictable Revenue* (2011) aporta aquí una distinción concreta: el pipeline predecible derivado de una relación medida entre actividad y resultado (los capítulos sobre generación predecible). Formula dos mini-casos: uno que satisface la definición de **productividad por movimiento** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «medir eficiencia además de crecimiento», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Contribución por canal: operacionalización y medición

**Contribución por canal** significa **margen que aporta cada canal después de sus costos**.

La productividad por movimiento —cuánto ingreso genera cada tipo de canal por unidad de recurso— permite decidir dónde invertir el próximo peso. Ese análisis exige imputar correctamente los costos, y ahí es donde la mayoría de los cálculos se vuelve discutible. Declarar la imputación es parte del análisis.

Ficha de medición obligatoria para **eficiencia del crecimiento**: `ingreso incremental del periodo, sobre gasto comercial incremental`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Wes Bush — *Product-Led Growth* (2019) pone una condición sobre la medición: el gatillo de conversión construido alrededor del valor y no del tiempo (los capítulos sobre conversión a plan pagado). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Velocidad de escalamiento: trade-offs y efectos de segundo orden

**Definición:** rapidez con que el movimiento puede aumentar su producción.

Optimizar la eficiencia puede frenar el crecimiento en un momento donde la velocidad importa más que el margen; priorizar el crecimiento puede construir una operación que no se sostiene. La decisión depende de la etapa y de la disponibilidad de capital, y debe declararse explícitamente en lugar de oscilar entre ambos objetivos.

**Lo que aporta la fuente.** Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) aporta el criterio para pesar el intercambio: los inductores de actuación frente a los indicadores de resultado (los capítulos sobre tipos de indicador). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **deterioro de eficiencia al escalar** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **velocidad de escalamiento** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «ajustar la asignación según el resultado», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Las métricas de entrada al mercado son indicadores agregados y su movimiento puede deberse a cambios de mezcla. Un aumento de eficiencia por mayor proporción de negocios pequeños y rápidos no significa mejora del sistema. Toda lectura debe acompañarse de la evolución de la composición.

**Frontera declarada.** En etapas tempranas puede ser racional sacrificar eficiencia para ganar posición. Lo que no es racional es hacerlo sin declararlo ni medirlo. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Abrir frentes simultáneos sin capacidad, diluir foco y llegar tarde a todos.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar métricas de go-to-market no consiste en sumar definiciones. Empieza por **eficiencia del crecimiento**, contrasta **productividad por movimiento** con **contribución por canal**, incorpora **velocidad de escalamiento** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | La métrica que importa ahora: una sola, según etapa y modelo de negocio | Los capítulos sobre la métrica única | ¿Qué debería observarse en **eficiencia del crecimiento** si aquí opera «la métrica que importa ahora: una sola, según etapa y modelo de negocio»? ¿Y qué observación lo desmentiría en este caso? |
| Aaron Ross y Marylou Tyler — *Predictable Revenue* (2011) | El pipeline predecible derivado de una relación medida entre actividad y resultado | Los capítulos sobre generación predecible | ¿Qué debería observarse en **productividad por movimiento** si aquí opera «el pipeline predecible derivado de una relación medida entre actividad y resultado»? ¿Y qué observación lo desmentiría en este caso? |
| Wes Bush — *Product-Led Growth* (2019) | El gatillo de conversión construido alrededor del valor y no del tiempo | Los capítulos sobre conversión a plan pagado | ¿Qué debería observarse en **contribución por canal** si aquí opera «el gatillo de conversión construido alrededor del valor y no del tiempo»? ¿Y qué observación lo desmentiría en este caso? |
| Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) | Los inductores de actuación frente a los indicadores de resultado | Los capítulos sobre tipos de indicador | ¿Qué debería observarse en **velocidad de escalamiento** si aquí opera «los inductores de actuación frente a los indicadores de resultado»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina creció 40 % en ingreso y su gasto comercial creció 78 %. El plan celebra el crecimiento y no menciona el deterioro de eficiencia.

**Paso 1 — Definir las métricas por movimiento y por canal.** El equipo escribe primero el supuesto asociado a **eficiencia del crecimiento** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **eficiencia del crecimiento** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Medir eficiencia además de crecimiento.** El trabajo aquí es separar lo observado de lo inferido sobre **productividad por movimiento**. La evidencia que ordena la discusión es **periodo de recuperación por movimiento**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Comparar la eficiencia entre movimientos.** El riesgo de este paso es cerrar demasiado rápido alrededor de **contribución por canal**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **deterioro de eficiencia al escalar** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Identificar dónde la eficiencia se deteriora al escalar.** Con **velocidad de escalamiento** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **eficiencia del crecimiento** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Ajustar la asignación según el resultado.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **eficiencia del crecimiento**. **periodo de recuperación por movimiento** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **eficiencia del crecimiento** | Relación entre el ingreso incremental y el gasto necesario para producirlo | Cuando **eficiencia del crecimiento** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **productividad por movimiento** | Resultado obtenido por unidad de capacidad en cada movimiento comercial | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** En etapas tempranas puede ser racional sacrificar eficiencia para ganar posición. Lo que no es racional es hacerlo sin declararlo ni medirlo.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre métricas de go-to-market |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Head of GTM, Partnerships, Product marketing y Founder. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina creció 40 % en ingreso y su gasto comercial creció 78 %. El plan celebra el crecimiento y no menciona el deterioro de eficiencia.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir las métricas por movimiento y por canal → medir eficiencia además de crecimiento → comparar la eficiencia entre movimientos → identificar dónde la eficiencia se deteriora al escalar → ajustar la asignación según el resultado** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **eficiencia del crecimiento**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Lean Analytics* y la de *Predictable Revenue*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **eficiencia del crecimiento** y **productividad por movimiento** como sinónimos | Se perdió la distinción entre «relación entre el ingreso incremental y el gasto necesario para producirlo» y «resultado obtenido por unidad de capacidad en cada movimiento comercial» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «ajustar la asignación según el resultado» | Se saltó «definir las métricas por movimiento y por canal»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **eficiencia del crecimiento** | La métrica local reemplazó al resultado del sistema | Contrástala con **deterioro de eficiencia al escalar** y explicita el costo de oportunidad. |
| Reportar crecimiento sin reportar eficiencia | Error específico de esta clase | Presenta el ingreso incremental junto al gasto incremental que lo produjo. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **eficiencia del crecimiento** y **productividad por movimiento** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **contribución por canal** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir las métricas por movimiento y por canal» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **eficiencia del crecimiento** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «En etapas tempranas puede ser racional sacrificar eficiencia para ganar posición. Lo que no es racional es hacerlo sin declararlo ni medirlo»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **contribución por canal** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **eficiencia del crecimiento**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Lean Analytics* y *The Balanced Scorecard*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Abrir frentes simultáneos sin capacidad, diluir foco y llegar tarde a todos.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P22-C13-gtm-metrics/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **eficiencia del crecimiento**, **periodo de recuperación por movimiento** y **deterioro de eficiencia al escalar** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **plan GTM completo con beachhead, movimiento comercial, canales, economía y plan de lanzamiento**.

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

- Alistair Croll y Benjamin Yoskovitz — [*Lean Analytics*](https://openlibrary.org/isbn/9781449335670) (2013) · ISBN 9781449335670 — **aporta a esta clase:** la métrica que importa ahora: una sola, según etapa y modelo de negocio. **Dónde buscarlo:** los capítulos sobre la métrica única. Registra edición y páginas consultadas en tu nota de lectura.
- Aaron Ross y Marylou Tyler — [*Predictable Revenue*](https://openlibrary.org/isbn/9780984380213) (2011) · ISBN 9780984380213 — **aporta a esta clase:** el pipeline predecible derivado de una relación medida entre actividad y resultado. **Dónde buscarlo:** los capítulos sobre generación predecible. Registra edición y páginas consultadas en tu nota de lectura.
- Wes Bush — [*Product-Led Growth*](https://openlibrary.org/isbn/9781777119317) (2019) · ISBN 9781777119317 — **aporta a esta clase:** el gatillo de conversión construido alrededor del valor y no del tiempo. **Dónde buscarlo:** los capítulos sobre conversión a plan pagado. Registra edición y páginas consultadas en tu nota de lectura.
- Robert S. Kaplan y David P. Norton — [*The Balanced Scorecard*](https://openlibrary.org/isbn/9780875846514) (1996) · ISBN 9780875846514 — **aporta a esta clase:** los inductores de actuación frente a los indicadores de resultado. **Dónde buscarlo:** los capítulos sobre tipos de indicador. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 12 · Internacionalización](class-12-internacionalizacion.md) · [Índice de la parte](README.md) · [Clase 14 · Plan go-to-market completo](class-14-plan-gtm-completo.md) →
