---
title: "Etapas de ciclo de vida"
type: class
language: es
standard: clase-profunda-v2
part: 17
class: 02
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["diorio", "roberge", "croll-yoskovitz", "provost"]
anchors: {"croll-yoskovitz": "etapas", "diorio": "definiciones", "provost": "formulacion", "roberge": "demanda"}
updated: 2026-08-19
---

# Clase 17.02 — Etapas de ciclo de vida

Clase 2 de 14 de la parte [17 — Marketing automation y revenue operations](README.md), de nivel Operación de ingresos. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 17.01, *Automatización con propósito*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de distribución por etapa con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La definición única por indicador como acuerdo previo a cualquier tablero — Stephen G. Diorio y Chris K. Hummel. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Las etapas de ciclo de vida clasifican a cada contacto según su relación con la empresa: desconocido, suscriptor, lead, oportunidad, cliente, cliente en riesgo, ex cliente. Su valor está en permitir tratamientos distintos y medir el flujo entre estados. Su condición es la misma que en el pipeline: definiciones compartidas y criterios verificables de transición.

Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales. La parte 17 busca **integrar marketing, ventas y servicio en un solo modelo de datos y de proceso**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **etapas de ciclo de vida** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué automatizo porque mejora el sistema y qué estaría solo escalando un desorden?

Los conceptos que estructuran la sesión son **etapa de ciclo de vida**, **criterio de transición**, **flujo entre etapas** y **estado terminal**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `etapa de ciclo de vida`, `criterio de transición`, `flujo entre etapas` y `estado terminal` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Marketing automation y revenue operations**.
3. **Aplicar** la secuencia **definir las etapas y sus criterios de transición → instrumentar el registro automático de transiciones → medir volumen y velocidad de flujo entre etapas → diseñar tratamiento diferenciado por etapa → revisar las definiciones cada semestre** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **distribución por etapa**, **velocidad de transición** y **contactos sin etapa asignada** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **etapa de ciclo de vida** y **criterio de transición** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **distribución por etapa**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **etapa de ciclo de vida** | estado que describe la relación actual del contacto con la empresa | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **criterio de transición** | condición verificable que mueve a un contacto de una etapa a otra | Construye un caso límite donde el concepto se confunde con el anterior. |
| **flujo entre etapas** | volumen de contactos que se mueve entre estados en un periodo | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **estado terminal** | etapa desde la cual el contacto sale del ciclo activo | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir las etapas y sus criterios de transición → 2. instrumentar el registro automático de transiciones → 3. medir volumen y velocidad de flujo entre etapas → 4. diseñar tratamiento diferenciado por etapa → 5. revisar las definiciones cada semestre
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Demasiadas etapas producen una taxonomía que nadie mantiene. Seis o siete estados suelen bastar para operar.

## 📖 Desarrollo

### 1. Etapa de ciclo de vida: mecanismo central

**Etapa de ciclo de vida** se entiende aquí como **estado que describe la relación actual del contacto con la empresa**.

Las etapas de ciclo de vida describen la relación con una persona u organización a lo largo del tiempo, más allá de una oportunidad puntual. Su función es permitir que cada área sepa en qué estado está cada registro y qué corresponde hacer. Sin ellas, marketing y ventas operan sobre la misma base con criterios distintos.

**De dónde viene esta afirmación.** Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) aporta la idea que sostiene este bloque: la definición única por indicador como acuerdo previo a cualquier tablero. Búscala en los capítulos sobre gobierno de métricas. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «distribución por etapa» debería moverse cuando cambie **etapa de ciclo de vida**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **criterio de transición**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Criterio de transición: frontera conceptual y error de clasificación

**Definición operacional:** condición verificable que mueve a un contacto de una etapa a otra. Su valor está en distinguirlo de **etapa de ciclo de vida**.

El criterio de transición entre etapas debe ser explícito y automatizable, o no se aplicará de forma consistente. «Cuando muestra interés» no es un criterio; «cuando solicita una demostración o descarga el documento de precios» sí lo es. La precisión aquí determina la utilidad de todos los informes de embudo.

**Contraste bibliográfico.** Mark Roberge — *The Sales Acceleration Formula* (2015) aporta aquí una distinción concreta: la generación de demanda medida por conversión a oportunidad y no por volumen (los capítulos sobre la fórmula de generación de demanda). Formula dos mini-casos: uno que satisface la definición de **criterio de transición** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «instrumentar el registro automático de transiciones», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Flujo entre etapas: operacionalización y medición

**Flujo entre etapas** significa **volumen de contactos que se mueve entre estados en un periodo**.

El estado terminal —qué pasa con quien no avanza— es la parte que suele faltar. Sin él, los registros se acumulan indefinidamente en etapas intermedias y las métricas de conversión se deterioran sin que nadie entienda por qué. Definir cuándo un registro sale del ciclo y a dónde va es parte del diseño.

Ficha de medición obligatoria para **distribución por etapa**: `contactos en cada etapa, sobre contactos totales de la base`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) pone una condición sobre la medición: las cinco etapas —empatía, adherencia, viralidad, ingreso y escala— con su métrica propia (la parte sobre etapas del negocio). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Estado terminal: trade-offs y efectos de segundo orden

**Definición:** etapa desde la cual el contacto sale del ciclo activo.

Más etapas entregan visibilidad y aumentan el mantenimiento y la probabilidad de inconsistencia; menos etapas simplifican y ocultan transiciones relevantes. La cantidad debe responder a qué decisiones se toman en cada punto: una etapa que no dispara ninguna acción distinta no justifica existir.

**Lo que aporta la fuente.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta el criterio para pesar el intercambio: la formulación del problema de negocio como problema de datos antes de elegir técnica (los capítulos iniciales sobre pensamiento analítico). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **contactos sin etapa asignada** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **estado terminal** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar las definiciones cada semestre», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El modelo de ciclo de vida describe un recorrido idealizado. Las personas retroceden, se van y vuelven, cambian de organización. Forzar un avance lineal produce datos que no reflejan la realidad. El diseño debe permitir retrocesos y registrarlos, porque esa información es diagnóstica.

**Frontera declarada.** Demasiadas etapas producen una taxonomía que nadie mantiene. Seis o siete estados suelen bastar para operar. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar etapas de ciclo de vida no consiste en sumar definiciones. Empieza por **etapa de ciclo de vida**, contrasta **criterio de transición** con **flujo entre etapas**, incorpora **estado terminal** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) | La definición única por indicador como acuerdo previo a cualquier tablero | Los capítulos sobre gobierno de métricas | ¿Qué debería observarse en **etapa de ciclo de vida** si aquí opera «la definición única por indicador como acuerdo previo a cualquier tablero»? ¿Y qué observación lo desmentiría en este caso? |
| Mark Roberge — *The Sales Acceleration Formula* (2015) | La generación de demanda medida por conversión a oportunidad y no por volumen | Los capítulos sobre la fórmula de generación de demanda | ¿Qué debería observarse en **criterio de transición** si aquí opera «la generación de demanda medida por conversión a oportunidad y no por volumen»? ¿Y qué observación lo desmentiría en este caso? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | Las cinco etapas —empatía, adherencia, viralidad, ingreso y escala— con su métrica propia | La parte sobre etapas del negocio | ¿Qué debería observarse en **flujo entre etapas** si aquí opera «las cinco etapas —empatía, adherencia, viralidad, ingreso y escala— con su métrica propia»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La formulación del problema de negocio como problema de datos antes de elegir técnica | Los capítulos iniciales sobre pensamiento analítico | ¿Qué debería observarse en **estado terminal** si aquí opera «la formulación del problema de negocio como problema de datos antes de elegir técnica»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** En Ruta Andina un mismo contacto aparece como lead en marketing y como cliente en soporte porque cada área usa su propia clasificación.

**Paso 1 — Definir las etapas y sus criterios de transición.** El equipo escribe primero el supuesto asociado a **etapa de ciclo de vida** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **distribución por etapa** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Instrumentar el registro automático de transiciones.** El trabajo aquí es separar lo observado de lo inferido sobre **criterio de transición**. La evidencia que ordena la discusión es **velocidad de transición**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Medir volumen y velocidad de flujo entre etapas.** El riesgo de este paso es cerrar demasiado rápido alrededor de **flujo entre etapas**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **contactos sin etapa asignada** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Diseñar tratamiento diferenciado por etapa.** Con **estado terminal** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **distribución por etapa** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar las definiciones cada semestre.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **etapa de ciclo de vida**. **velocidad de transición** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **etapa de ciclo de vida** | Estado que describe la relación actual del contacto con la empresa | Cuando **distribución por etapa** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **criterio de transición** | Condición verificable que mueve a un contacto de una etapa a otra | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Demasiadas etapas producen una taxonomía que nadie mantiene. Seis o siete estados suelen bastar para operar.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre etapas de ciclo de vida |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing ops, RevOps manager y Sales ops. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

En Ruta Andina un mismo contacto aparece como lead en marketing y como cliente en soporte porque cada área usa su propia clasificación.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir las etapas y sus criterios de transición → instrumentar el registro automático de transiciones → medir volumen y velocidad de flujo entre etapas → diseñar tratamiento diferenciado por etapa → revisar las definiciones cada semestre** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **distribución por etapa**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Revenue Operations* y la de *The Sales Acceleration Formula*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **etapa de ciclo de vida** y **criterio de transición** como sinónimos | Se perdió la distinción entre «estado que describe la relación actual del contacto con la empresa» y «condición verificable que mueve a un contacto de una etapa a otra» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar las definiciones cada semestre» | Se saltó «definir las etapas y sus criterios de transición»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **distribución por etapa** | La métrica local reemplazó al resultado del sistema | Contrástala con **contactos sin etapa asignada** y explicita el costo de oportunidad. |
| Mantener clasificaciones distintas por área | Error específico de esta clase | Acuerda una taxonomía única con criterios verificables y aplícala en todos los sistemas. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **etapa de ciclo de vida** y **criterio de transición** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **flujo entre etapas** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir las etapas y sus criterios de transición» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **distribución por etapa** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Demasiadas etapas producen una taxonomía que nadie mantiene. Seis o siete estados suelen bastar para operar»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **flujo entre etapas** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **distribución por etapa**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Revenue Operations* y *Data Science for Business*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P17-C02-lifecycle-stages/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **distribución por etapa**, **velocidad de transición** y **contactos sin etapa asignada** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **operating model de RevOps con lifecycle, scoring, SLA, integraciones y observabilidad**.

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

- Stephen G. Diorio y Chris K. Hummel — [*Revenue Operations*](https://openlibrary.org/isbn/9781119871132) (2022) · ISBN 9781119871132 — **aporta a esta clase:** la definición única por indicador como acuerdo previo a cualquier tablero. **Dónde buscarlo:** los capítulos sobre gobierno de métricas. Registra edición y páginas consultadas en tu nota de lectura.
- Mark Roberge — [*The Sales Acceleration Formula*](https://openlibrary.org/isbn/9781119047018) (2015) · ISBN 9781119047018 — **aporta a esta clase:** la generación de demanda medida por conversión a oportunidad y no por volumen. **Dónde buscarlo:** los capítulos sobre la fórmula de generación de demanda. Registra edición y páginas consultadas en tu nota de lectura.
- Alistair Croll y Benjamin Yoskovitz — [*Lean Analytics*](https://openlibrary.org/isbn/9781449335670) (2013) · ISBN 9781449335670 — **aporta a esta clase:** las cinco etapas —empatía, adherencia, viralidad, ingreso y escala— con su métrica propia. **Dónde buscarlo:** la parte sobre etapas del negocio. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) · ISBN 9781449374280 — **aporta a esta clase:** la formulación del problema de negocio como problema de datos antes de elegir técnica. **Dónde buscarlo:** los capítulos iniciales sobre pensamiento analítico. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 01 · Automatización con propósito](class-01-automatizacion-con-proposito.md) · [Índice de la parte](README.md) · [Clase 03 · Lead scoring](class-03-lead-scoring.md) →
