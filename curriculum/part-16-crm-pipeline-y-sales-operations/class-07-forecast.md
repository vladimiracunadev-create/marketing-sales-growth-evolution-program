---
title: "Forecast"
type: class
language: es
standard: clase-profunda-v2
part: 16
class: 07
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["roberge", "grove", "provost", "wheeler-dv"]
anchors: {"grove": "indicadores-adelantados", "provost": "evaluacion", "roberge": "metricas-coaching", "wheeler-dv": "comparar-dos-puntos"}
updated: 2026-08-19
---

# Clase 16.07 — Forecast

**Parte 16 · CRM, pipeline y sales operations** · Nivel: Operación de ingresos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 16.06 — *Actividades comerciales*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de precisión del forecast para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El acompañamiento dirigido por una métrica diagnóstica por vendedor — Mark Roberge. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Un forecast es un compromiso sobre el futuro con un método declarado. Los tres enfoques habituales —ponderación por etapa, juicio del vendedor y análisis de cohortes históricas— tienen sesgos distintos y conviene contrastarlos. Lo que hace confiable a un forecast no es la sofisticación del cálculo sino la calidad de los criterios de etapa y la honestidad con que se revisan las desviaciones.

Esta sesión distingue lo que se sabe, lo que se supone y lo que todavía no se ha medido. La parte 16 busca **convertir el CRM en un sistema de trabajo y de verdad operacional**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **forecast** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿El pipeline describe la realidad o solo el optimismo del equipo?

Los conceptos que estructuran la sesión son **método de forecast**, **sesgo de optimismo**, **precisión del forecast** y **compromiso frente a mejor caso**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `método de forecast`, `sesgo de optimismo`, `precisión del forecast` y `compromiso frente a mejor caso` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **CRM, pipeline y sales operations**.
3. **Aplicar** la secuencia **declarar el método y su alcance → separar compromiso, probable y mejor caso → contrastar con al menos un método alternativo → medir la precisión de cada ciclo → corregir el método con el sesgo observado** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **precisión del forecast**, **sesgo sistemático** y **cobertura del pipeline** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **método de forecast** y **sesgo de optimismo** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **precisión del forecast**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **método de forecast** | regla explícita que convierte el estado del pipeline en una proyección | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **sesgo de optimismo** | tendencia sistemática a proyectar más de lo que se cierra | Construye un caso límite donde el concepto se confunde con el anterior. |
| **precisión del forecast** | diferencia entre lo proyectado y lo efectivamente cerrado | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **compromiso frente a mejor caso** | distinción entre lo que se asegura y lo que podría ocurrir | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. declarar el método y su alcance → 2. separar compromiso, probable y mejor caso → 3. contrastar con al menos un método alternativo → 4. medir la precisión de cada ciclo → 5. corregir el método con el sesgo observado
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Ningún método corrige un pipeline con criterios de etapa débiles. La precisión del forecast es consecuencia de la disciplina de calificación, no de la fórmula.

## 📖 Desarrollo

### 1. Método de forecast: mecanismo central

**Método de forecast** se entiende aquí como **regla explícita que convierte el estado del pipeline en una proyección**.

El pronóstico comercial es una estimación con incertidumbre y debería presentarse como tal. La práctica habitual de reportar un número único esconde el rango y produce conversaciones sobre precisión que no corresponden. Un pronóstico con rango declarado y supuestos explícitos es más útil y más honesto.

**De dónde viene esta afirmación.** Mark Roberge — *The Sales Acceleration Formula* (2015) aporta la idea que sostiene este bloque: el acompañamiento dirigido por una métrica diagnóstica por vendedor. Búscala en los capítulos sobre la fórmula de gestión. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «precisión del forecast» debería moverse cuando cambie **método de forecast**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **sesgo de optimismo**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Sesgo de optimismo: frontera conceptual y error de clasificación

**Definición operacional:** tendencia sistemática a proyectar más de lo que se cierra. Su valor está en distinguirlo de **método de forecast**.

El sesgo de optimismo está documentado y es sistemático: los pronósticos comerciales tienden a sobreestimar. Corregirlo con un factor derivado del historial propio —cuánto se sobreestimó en los últimos ocho trimestres— es más efectivo que pedir realismo, porque actúa sobre el dato y no sobre la intención.

**Contraste bibliográfico.** Andrew S. Grove — *High Output Management* (1983) aporta aquí una distinción concreta: los indicadores adelantados y pareados que permiten corregir a tiempo (los capítulos sobre medición en la producción). Formula dos mini-casos: uno que satisface la definición de **sesgo de optimismo** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «separar compromiso, probable y mejor caso», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Precisión del forecast: operacionalización y medición

**Precisión del forecast** significa **diferencia entre lo proyectado y lo efectivamente cerrado**.

La precisión del pronóstico se mide y se mejora: error absoluto medio por trimestre, comparado en el tiempo y por vendedor. Sin esa medición, no hay forma de saber si el pronóstico está mejorando ni de identificar quién sistemáticamente sobreestima. Es un dato que casi ninguna organización lleva y que es fácil de construir.

Ficha de medición obligatoria para **precisión del forecast**: `diferencia porcentual entre proyección y cierre real, por trimestre`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) pone una condición sobre la medición: la evaluación contra una línea base y no contra la nada (los capítulos sobre evaluación de modelos). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Compromiso frente a mejor caso: trade-offs y efectos de segundo orden

**Definición:** distinción entre lo que se asegura y lo que podría ocurrir.

Un pronóstico conservador protege de sorpresas y puede producir decisiones de inversión demasiado cautelosas; uno optimista habilita inversión y arriesga compromisos que no se cumplen. La solución es separar el compromiso —lo que se sostiene— del mejor caso, y usar cada uno para decisiones distintas.

**Lo que aporta la fuente.** Donald J. Wheeler — *Understanding Variation* (2000) aporta el criterio para pesar el intercambio: el error de comparar dos puntos consecutivos y llamarlo tendencia (los capítulos sobre interpretación de series). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **cobertura del pipeline** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **compromiso frente a mejor caso** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «corregir el método con el sesgo observado», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El método de pronóstico debe corresponder a la madurez de los datos. Un modelo ponderado por etapa requiere probabilidades históricas confiables; sin ellas, produce precisión aparente sobre supuestos arbitrarios. En operaciones jóvenes, el juicio estructurado con criterios explícitos suele ser superior al modelo.

**Frontera declarada.** Ningún método corrige un pipeline con criterios de etapa débiles. La precisión del forecast es consecuencia de la disciplina de calificación, no de la fórmula. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Tomar decisiones de contratación y presupuesto sobre un pipeline que no representa la realidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar forecast no consiste en sumar definiciones. Empieza por **método de forecast**, contrasta **sesgo de optimismo** con **precisión del forecast**, incorpora **compromiso frente a mejor caso** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Mark Roberge — *The Sales Acceleration Formula* (2015) | El acompañamiento dirigido por una métrica diagnóstica por vendedor | Los capítulos sobre la fórmula de gestión | ¿Qué debería observarse en **método de forecast** si aquí opera «el acompañamiento dirigido por una métrica diagnóstica por vendedor»? ¿Y qué observación lo desmentiría en este caso? |
| Andrew S. Grove — *High Output Management* (1983) | Los indicadores adelantados y pareados que permiten corregir a tiempo | Los capítulos sobre medición en la producción | ¿Qué debería observarse en **sesgo de optimismo** si aquí opera «los indicadores adelantados y pareados que permiten corregir a tiempo»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La evaluación contra una línea base y no contra la nada | Los capítulos sobre evaluación de modelos | ¿Qué debería observarse en **precisión del forecast** si aquí opera «la evaluación contra una línea base y no contra la nada»? ¿Y qué observación lo desmentiría en este caso? |
| Donald J. Wheeler — *Understanding Variation* (2000) | El error de comparar dos puntos consecutivos y llamarlo tendencia | Los capítulos sobre interpretación de series | ¿Qué debería observarse en **compromiso frente a mejor caso** si aquí opera «el error de comparar dos puntos consecutivos y llamarlo tendencia»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El forecast de Ruta Andina proyecta CLP 84 millones y cierra CLP 51 millones. La desviación se repite hace cuatro trimestres y nadie ha ajustado el método.

**Paso 1 — Declarar el método y su alcance.** El equipo escribe primero el supuesto asociado a **método de forecast** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **precisión del forecast** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Separar compromiso, probable y mejor caso.** El trabajo aquí es separar lo observado de lo inferido sobre **sesgo de optimismo**. La evidencia que ordena la discusión es **sesgo sistemático**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Contrastar con al menos un método alternativo.** El riesgo de este paso es cerrar demasiado rápido alrededor de **precisión del forecast**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **cobertura del pipeline** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Medir la precisión de cada ciclo.** Con **compromiso frente a mejor caso** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **precisión del forecast** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Corregir el método con el sesgo observado.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **método de forecast**. **sesgo sistemático** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **método de forecast** | Regla explícita que convierte el estado del pipeline en una proyección | Cuando **precisión del forecast** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **sesgo de optimismo** | Tendencia sistemática a proyectar más de lo que se cierra | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Ningún método corrige un pipeline con criterios de etapa débiles. La precisión del forecast es consecuencia de la disciplina de calificación, no de la fórmula.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre forecast |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Sales operations, RevOps analyst y Jefe de ventas. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El forecast de Ruta Andina proyecta CLP 84 millones y cierra CLP 51 millones. La desviación se repite hace cuatro trimestres y nadie ha ajustado el método.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **declarar el método y su alcance → separar compromiso, probable y mejor caso → contrastar con al menos un método alternativo → medir la precisión de cada ciclo → corregir el método con el sesgo observado** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **precisión del forecast**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *The Sales Acceleration Formula* y la de *High Output Management*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **método de forecast** y **sesgo de optimismo** como sinónimos | Se perdió la distinción entre «regla explícita que convierte el estado del pipeline en una proyección» y «tendencia sistemática a proyectar más de lo que se cierra» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «corregir el método con el sesgo observado» | Se saltó «declarar el método y su alcance»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **precisión del forecast** | La métrica local reemplazó al resultado del sistema | Contrástala con **cobertura del pipeline** y explicita el costo de oportunidad. |
| Mantener el método pese a un sesgo sistemático | Error específico de esta clase | Mide la desviación con signo por trimestre y corrige el método con ese factor. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **método de forecast** y **sesgo de optimismo** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **precisión del forecast** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «declarar el método y su alcance» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **precisión del forecast** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Ningún método corrige un pipeline con criterios de etapa débiles. La precisión del forecast es consecuencia de la disciplina de calificación, no de la fórmula»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **precisión del forecast** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **precisión del forecast**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *The Sales Acceleration Formula* y *Understanding Variation*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Tomar decisiones de contratación y presupuesto sobre un pipeline que no representa la realidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P16-C07-forecast/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **precisión del forecast**, **sesgo sistemático** y **cobertura del pipeline** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **diseño de sales operations con pipeline, criterios de etapa, forecast y gobierno de datos**.

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

- Mark Roberge — *The Sales Acceleration Formula* (2015) — **aporta a esta clase:** el acompañamiento dirigido por una métrica diagnóstica por vendedor. **Dónde buscarlo:** los capítulos sobre la fórmula de gestión. Registra edición y páginas consultadas en tu nota de lectura.
- Andrew S. Grove — *High Output Management* (1983) — **aporta a esta clase:** los indicadores adelantados y pareados que permiten corregir a tiempo. **Dónde buscarlo:** los capítulos sobre medición en la producción. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — **aporta a esta clase:** la evaluación contra una línea base y no contra la nada. **Dónde buscarlo:** los capítulos sobre evaluación de modelos. Registra edición y páginas consultadas en tu nota de lectura.
- Donald J. Wheeler — *Understanding Variation* (2000) — **aporta a esta clase:** el error de comparar dos puntos consecutivos y llamarlo tendencia. **Dónde buscarlo:** los capítulos sobre interpretación de series. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 06 · Actividades comerciales](class-06-actividades-comerciales.md) · [Índice de la parte](README.md) · [Clase 08 · Cuotas y territorios](class-08-cuotas-y-territorios.md) →
