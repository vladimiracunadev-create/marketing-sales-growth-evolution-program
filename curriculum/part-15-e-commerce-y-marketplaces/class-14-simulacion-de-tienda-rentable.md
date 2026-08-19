---
title: "Simulación de tienda rentable"
type: class
language: es
standard: clase-profunda-v2
part: 15
class: 14
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["croll-yoskovitz", "flint", "provost", "hubbard"]
anchors: {"croll-yoskovitz": "linea-trazada", "flint": "valor-canal", "hubbard": "calibracion", "provost": "valor-esperado"}
updated: 2026-08-19
---

# Clase 15.14 — Simulación de tienda rentable

**Parte 15 · E-commerce y marketplaces** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 15.13 — *Economía del e-commerce*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de contribución total del modelo para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La línea trazada de antemano: qué valor haría considerar exitoso el experimento — Alistair Croll y Benjamin Yoskovitz. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Esta clase integra la parte en una simulación completa: catálogo, precios, costos de cumplimiento, comisiones, devoluciones, conversión y recompra. El resultado no es una tienda bonita sino un modelo económico que muestra bajo qué condiciones el negocio gana dinero y bajo cuáles no. La prueba de calidad es la sensibilidad: qué variable, al moverse 10 %, cambia el resultado de signo.

Esta sesión distingue lo que se sabe, lo que se supone y lo que todavía no se ha medido. La parte 15 busca **operar una tienda y un canal de marketplace con economía verificable**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **simulación de tienda rentable** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Dónde se pierde el pedido y cuánto queda después de comisión, envío y devolución?

Los conceptos que estructuran la sesión son **modelo económico de la tienda**, **análisis de sensibilidad**, **variable crítica** y **escenario de estrés**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `modelo económico de la tienda`, `análisis de sensibilidad`, `variable crítica` y `escenario de estrés` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **E-commerce y marketplaces**.
3. **Aplicar** la secuencia **construir el modelo con supuestos documentados → calcular contribución y punto de equilibrio → ejecutar el análisis de sensibilidad → identificar las variables críticas → definir los controles que vigilarán esas variables** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **contribución total del modelo**, **variables críticas identificadas** y **resultado en escenario de estrés** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **modelo económico de la tienda** y **análisis de sensibilidad** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **contribución total del modelo**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **modelo económico de la tienda** | representación de ingresos, costos y volúmenes con sus supuestos | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **análisis de sensibilidad** | evaluación del efecto de variar cada supuesto sobre el resultado | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **variable crítica** | supuesto cuyo cambio moderado altera la viabilidad del negocio | Da un hecho compatible con la definición y otro que la refute. |
| **escenario de estrés** | combinación adversa de supuestos usada para probar la resistencia del modelo | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. construir el modelo con supuestos documentados → 2. calcular contribución y punto de equilibrio → 3. ejecutar el análisis de sensibilidad → 4. identificar las variables críticas → 5. definir los controles que vigilarán esas variables
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un modelo es tan bueno como sus supuestos. Sin datos reales de conversión, devoluciones y costo logístico, la simulación sólo ordena la ignorancia.

## 📖 Desarrollo

### 1. Modelo económico de la tienda: mecanismo central

**Modelo económico de la tienda** se entiende aquí como **representación de ingresos, costos y volúmenes con sus supuestos**.

Modelar la rentabilidad de una tienda consiste en construir la cadena completa desde el tráfico hasta la contribución, con cada supuesto explícito y verificable. El valor del ejercicio no está en el número final sino en descubrir qué variable domina el resultado, porque ahí es donde conviene concentrar el esfuerzo.

**De dónde viene esta afirmación.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) aporta la idea que sostiene este bloque: la línea trazada de antemano: qué valor haría considerar exitoso el experimento. Búscala en los capítulos sobre definir el éxito. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «contribución total del modelo» debería moverse cuando cambie **modelo económico de la tienda**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **análisis de sensibilidad**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Análisis de sensibilidad: frontera conceptual y error de clasificación

**Definición operacional:** evaluación del efecto de variar cada supuesto sobre el resultado. Su valor está en distinguirlo de **modelo económico de la tienda**.

El análisis de sensibilidad se hace moviendo cada supuesto en un rango razonable y observando el efecto sobre el resultado. Casi siempre una o dos variables explican la mayor parte de la variación, y esas son las que hay que medir mejor. Las demás pueden estimarse con menos precisión sin afectar la decisión.

**Contraste bibliográfico.** Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) aporta aquí una distinción concreta: la contribución real de cada canal descontando lo que habría ocurrido igual (los capítulos sobre análisis forense de canales). Formula dos mini-casos: uno que satisface la definición de **análisis de sensibilidad** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «calcular contribución y punto de equilibrio», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Variable crítica: operacionalización y medición

**Variable crítica** significa **supuesto cuyo cambio moderado altera la viabilidad del negocio**.

La variable crítica en comercio digital suele ser la tasa de recompra o el margen por pedido, no el tráfico, que es donde se concentra la atención. Descubrirlo cambia la asignación de esfuerzo: invertir en mejorar la variable crítica rinde más que optimizar las demás, aunque sea menos visible.

Ficha de medición obligatoria para **contribución total del modelo**: `ingreso menos costos variables, proyectado por escenario`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) pone una condición sobre la medición: el marco de valor esperado que combina probabilidad y consecuencia económica (el capítulo sobre valor esperado). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Escenario de estrés: trade-offs y efectos de segundo orden

**Definición:** combinación adversa de supuestos usada para probar la resistencia del modelo.

Un modelo detallado captura más matices y se vuelve difícil de auditar y de mantener; uno simple se revisa y omite interacciones. Para decidir, un modelo simple con supuestos declarados suele ser superior a uno complejo cuyos supuestos están enterrados en fórmulas que nadie revisa.

**Lo que aporta la fuente.** Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) aporta el criterio para pesar el intercambio: la calibración de estimaciones subjetivas como habilidad entrenable (los capítulos sobre estimación calibrada). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **resultado en escenario de estrés** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **escenario de estrés** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «definir los controles que vigilarán esas variables», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El escenario de estrés —qué pasa si el costo de adquisición sube, si la conversión baja, si un canal se encarece— debe formar parte del modelo y no ser un ejercicio opcional. Su función es identificar en qué punto la operación deja de ser viable y con cuánta anticipación se podría detectar, que es una información de gestión y no un pesimismo.

**Frontera declarada.** Un modelo es tan bueno como sus supuestos. Sin datos reales de conversión, devoluciones y costo logístico, la simulación sólo ordena la ignorancia. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar simulación de tienda rentable no consiste en sumar definiciones. Empieza por **modelo económico de la tienda**, contrasta **análisis de sensibilidad** con **variable crítica**, incorpora **escenario de estrés** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | La línea trazada de antemano: qué valor haría considerar exitoso el experimento | Los capítulos sobre definir el éxito | ¿Qué debería observarse en **modelo económico de la tienda** si aquí opera «la línea trazada de antemano: qué valor haría considerar exitoso el experimento»? ¿Y qué observación lo desmentiría en este caso? |
| Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) | La contribución real de cada canal descontando lo que habría ocurrido igual | Los capítulos sobre análisis forense de canales | ¿Qué debería observarse en **análisis de sensibilidad** si aquí opera «la contribución real de cada canal descontando lo que habría ocurrido igual»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | El marco de valor esperado que combina probabilidad y consecuencia económica | El capítulo sobre valor esperado | ¿Qué debería observarse en **variable crítica** si aquí opera «el marco de valor esperado que combina probabilidad y consecuencia económica»? ¿Y qué observación lo desmentiría en este caso? |
| Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) | La calibración de estimaciones subjetivas como habilidad entrenable | Los capítulos sobre estimación calibrada | ¿Qué debería observarse en **escenario de estrés** si aquí opera «la calibración de estimaciones subjetivas como habilidad entrenable»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina debe decidir si mantiene, rediseña o cierra su línea de hardware. La decisión requiere un modelo económico con sensibilidad, no una opinión.

**Paso 1 — Construir el modelo con supuestos documentados.** El equipo escribe primero el supuesto asociado a **modelo económico de la tienda** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **contribución total del modelo** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Calcular contribución y punto de equilibrio.** El trabajo aquí es separar lo observado de lo inferido sobre **análisis de sensibilidad**. La evidencia que ordena la discusión es **variables críticas identificadas**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Ejecutar el análisis de sensibilidad.** El riesgo de este paso es cerrar demasiado rápido alrededor de **variable crítica**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **resultado en escenario de estrés** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Identificar las variables críticas.** Con **escenario de estrés** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **contribución total del modelo** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Definir los controles que vigilarán esas variables.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **modelo económico de la tienda**. **variables críticas identificadas** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **modelo económico de la tienda** | Representación de ingresos, costos y volúmenes con sus supuestos | Cuando **contribución total del modelo** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **análisis de sensibilidad** | Evaluación del efecto de variar cada supuesto sobre el resultado | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un modelo es tan bueno como sus supuestos. Sin datos reales de conversión, devoluciones y costo logístico, la simulación sólo ordena la ignorancia.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre simulación de tienda rentable |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como E-commerce manager, Marketplace specialist y Emprendedor. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina debe decidir si mantiene, rediseña o cierra su línea de hardware. La decisión requiere un modelo económico con sensibilidad, no una opinión.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **construir el modelo con supuestos documentados → calcular contribución y punto de equilibrio → ejecutar el análisis de sensibilidad → identificar las variables críticas → definir los controles que vigilarán esas variables** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **contribución total del modelo**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Lean Analytics* y la de *Hillstrom's Multichannel Forensics*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **modelo económico de la tienda** y **análisis de sensibilidad** como sinónimos | Se perdió la distinción entre «representación de ingresos, costos y volúmenes con sus supuestos» y «evaluación del efecto de variar cada supuesto sobre el resultado» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «definir los controles que vigilarán esas variables» | Se saltó «construir el modelo con supuestos documentados»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **contribución total del modelo** | La métrica local reemplazó al resultado del sistema | Contrástala con **resultado en escenario de estrés** y explicita el costo de oportunidad. |
| Presentar el modelo sin análisis de sensibilidad | Error específico de esta clase | Identifica las variables críticas y muestra el resultado bajo escenario adverso. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **modelo económico de la tienda** y **análisis de sensibilidad** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **variable crítica** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «construir el modelo con supuestos documentados» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **contribución total del modelo** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un modelo es tan bueno como sus supuestos. Sin datos reales de conversión, devoluciones y costo logístico, la simulación sólo ordena la ignorancia»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **variable crítica** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **contribución total del modelo**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Lean Analytics* y *How to Measure Anything*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P15-C14-simulacion-de-tienda-rentable/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **contribución total del modelo**, **variables críticas identificadas** y **resultado en escenario de estrés** con fuente, ventana y lectura prohibida.
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

- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — **aporta a esta clase:** la línea trazada de antemano: qué valor haría considerar exitoso el experimento. **Dónde buscarlo:** los capítulos sobre definir el éxito. Registra edición y páginas consultadas en tu nota de lectura.
- Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) — **aporta a esta clase:** la contribución real de cada canal descontando lo que habría ocurrido igual. **Dónde buscarlo:** los capítulos sobre análisis forense de canales. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — **aporta a esta clase:** el marco de valor esperado que combina probabilidad y consecuencia económica. **Dónde buscarlo:** el capítulo sobre valor esperado. Registra edición y páginas consultadas en tu nota de lectura.
- Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) — **aporta a esta clase:** la calibración de estimaciones subjetivas como habilidad entrenable. **Dónde buscarlo:** los capítulos sobre estimación calibrada. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 13 · Economía del e-commerce](class-13-economia-del-e-commerce.md) · [Índice de la parte](README.md)
