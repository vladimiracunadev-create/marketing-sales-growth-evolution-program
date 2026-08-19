---
title: "Backlog de experimentos"
type: class
language: es
standard: clase-profunda-v2
part: 19
class: 09
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["ellis-brown", "kohavi", "ries-lean", "cagan"]
anchors: {"cagan": "riesgos", "ellis-brown": "backlog", "kohavi": "confianza", "ries-lean": "aprendizaje-validado"}
updated: 2026-08-19
---

# Clase 19.09 — Backlog de experimentos

**Parte 19 · Growth marketing y growth engineering** · Nivel: Crecimiento y analítica · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 19.08 — *Viralidad*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de entradas con hipótesis completa para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El backlog de experimentos con hipótesis y criterio previo — Sean Ellis y Morgan Brown. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Un backlog de experimentos convierte las ideas dispersas en una cola priorizada con hipótesis explícitas. Su valor está en la disciplina de formulación: cada entrada debe declarar qué se cree, por qué, qué se medirá y qué resultado la refutaría. Un backlog de ideas sin hipótesis es una lista de deseos que se ejecuta por simpatía.

Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales. La parte 19 busca **instalar un motor de experimentación que produzca aprendizaje acumulativo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **backlog de experimentos** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué bucle hace que el crecimiento se retroalimente en lugar de depender del gasto?

Los conceptos que estructuran la sesión son **entrada del backlog**, **fundamento de la hipótesis**, **esfuerzo estimado** y **aprendizaje esperado**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `entrada del backlog`, `fundamento de la hipótesis`, `esfuerzo estimado` y `aprendizaje esperado` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Growth marketing y growth engineering**.
3. **Aplicar** la secuencia **formular cada idea como hipótesis con fundamento → estimar esfuerzo y aprendizaje esperado → priorizar con un criterio explícito → ejecutar en orden y documentar el resultado → revisar el backlog con los aprendizajes acumulados** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **entradas con hipótesis completa**, **tasa de ejecución** y **aprendizajes por experimento** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **entrada del backlog** y **fundamento de la hipótesis** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **entradas con hipótesis completa**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **entrada del backlog** | experimento formulado con hipótesis, métrica y criterio de decisión | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **fundamento de la hipótesis** | evidencia o razonamiento que sostiene la expectativa | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **esfuerzo estimado** | recursos necesarios para ejecutar el experimento | Da un hecho compatible con la definición y otro que la refute. |
| **aprendizaje esperado** | valor de la información que producirá el resultado, gane o pierda | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. formular cada idea como hipótesis con fundamento → 2. estimar esfuerzo y aprendizaje esperado → 3. priorizar con un criterio explícito → 4. ejecutar en orden y documentar el resultado → 5. revisar el backlog con los aprendizajes acumulados
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un backlog muy formalizado puede frenar pruebas baratas y rápidas. El nivel de formalidad debe ser proporcional al costo del experimento.

## 📖 Desarrollo

### 1. Entrada del backlog: mecanismo central

**Entrada del backlog** se entiende aquí como **experimento formulado con hipótesis, métrica y criterio de decisión**.

Un backlog de experimentos convierte las ideas dispersas en un flujo gestionable. Cada entrada debe contener la hipótesis, el fundamento que la sustenta, el esfuerzo estimado y el aprendizaje esperado gane o pierda. Sin esos cuatro campos, el backlog es una lista de ocurrencias ordenada por quién insistió más.

**De dónde viene esta afirmación.** Sean Ellis y Morgan Brown — *Hacking Growth* (2017) aporta la idea que sostiene este bloque: el backlog de experimentos con hipótesis y criterio previo. Búscala en los capítulos sobre priorización de pruebas. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «entradas con hipótesis completa» debería moverse cuando cambie **entrada del backlog**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **fundamento de la hipótesis**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Fundamento de la hipótesis: frontera conceptual y error de clasificación

**Definición operacional:** evidencia o razonamiento que sostiene la expectativa. Su valor está en distinguirlo de **entrada del backlog**.

El fundamento de la hipótesis es lo que distingue un experimento de una apuesta. Debe apoyarse en un dato observado, una entrevista, un patrón en el comportamiento o un principio con evidencia. Las entradas sin fundamento pueden existir en el backlog, pero deben marcarse como exploratorias y competir con desventaja.

**Contraste bibliográfico.** Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) aporta aquí una distinción concreta: las condiciones que hacen confiable un experimento en línea (los capítulos sobre experimentos confiables). Formula dos mini-casos: uno que satisface la definición de **fundamento de la hipótesis** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «estimar esfuerzo y aprendizaje esperado», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Esfuerzo estimado: operacionalización y medición

**Esfuerzo estimado** significa **recursos necesarios para ejecutar el experimento**.

El aprendizaje esperado debe declararse para ambos resultados: qué se sabrá si funciona y qué se sabrá si no. Un experimento cuyo resultado negativo no enseña nada suele estar mal diseñado. Ese campo, exigido al escribir la entrada, elimina buena parte de las ideas que sólo confirmarían lo que ya se cree.

Ficha de medición obligatoria para **entradas con hipótesis completa**: `entradas con hipótesis, métrica y criterio, sobre entradas del backlog`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Eric Ries — *The Lean Startup* (2011) pone una condición sobre la medición: el aprendizaje validado como unidad de progreso frente a los hitos de plan (los capítulos sobre aprendizaje validado). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Aprendizaje esperado: trade-offs y efectos de segundo orden

**Definición:** valor de la información que producirá el resultado, gane o pierda.

Un backlog grande ofrece opciones y produce parálisis y trabajo de mantenimiento. Uno pequeño se ejecuta y puede quedarse sin ideas de calidad. La práctica razonable mantiene un número acotado de entradas priorizadas y descarta explícitamente las demás, en lugar de acumularlas indefinidamente.

**Lo que aporta la fuente.** Marty Cagan — *Inspired* (2017, 2.ª ed.) aporta el criterio para pesar el intercambio: los cuatro riesgos de producto: valor, usabilidad, viabilidad y factibilidad (los capítulos sobre riesgos del descubrimiento). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **aprendizajes por experimento** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **aprendizaje esperado** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar el backlog con los aprendizajes acumulados», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El backlog describe lo que se puede probar con la capacidad e instrumentación actuales. Ideas que requieren infraestructura inexistente no son experimentos sino proyectos, y mezclarlas distorsiona la planificación. Separarlas en dos listas distintas evita que la priorización compare cosas incomparables.

**Frontera declarada.** Un backlog muy formalizado puede frenar pruebas baratas y rápidas. El nivel de formalidad debe ser proporcional al costo del experimento. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar backlog de experimentos no consiste en sumar definiciones. Empieza por **entrada del backlog**, contrasta **fundamento de la hipótesis** con **esfuerzo estimado**, incorpora **aprendizaje esperado** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Sean Ellis y Morgan Brown — *Hacking Growth* (2017) | El backlog de experimentos con hipótesis y criterio previo | Los capítulos sobre priorización de pruebas | ¿Qué debería observarse en **entrada del backlog** si aquí opera «el backlog de experimentos con hipótesis y criterio previo»? ¿Y qué observación lo desmentiría en este caso? |
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | Las condiciones que hacen confiable un experimento en línea | Los capítulos sobre experimentos confiables | ¿Qué debería observarse en **fundamento de la hipótesis** si aquí opera «las condiciones que hacen confiable un experimento en línea»? ¿Y qué observación lo desmentiría en este caso? |
| Eric Ries — *The Lean Startup* (2011) | El aprendizaje validado como unidad de progreso frente a los hitos de plan | Los capítulos sobre aprendizaje validado | ¿Qué debería observarse en **esfuerzo estimado** si aquí opera «el aprendizaje validado como unidad de progreso frente a los hitos de plan»? ¿Y qué observación lo desmentiría en este caso? |
| Marty Cagan — *Inspired* (2017, 2.ª ed.) | Los cuatro riesgos de producto: valor, usabilidad, viabilidad y factibilidad | Los capítulos sobre riesgos del descubrimiento | ¿Qué debería observarse en **aprendizaje esperado** si aquí opera «los cuatro riesgos de producto: valor, usabilidad, viabilidad y factibilidad»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El backlog de Ruta Andina tiene 62 ideas sin hipótesis. Se ejecuta lo que propone quien tiene más influencia en la reunión.

**Paso 1 — Formular cada idea como hipótesis con fundamento.** El equipo escribe primero el supuesto asociado a **entrada del backlog** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **entradas con hipótesis completa** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Estimar esfuerzo y aprendizaje esperado.** El trabajo aquí es separar lo observado de lo inferido sobre **fundamento de la hipótesis**. La evidencia que ordena la discusión es **tasa de ejecución**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Priorizar con un criterio explícito.** El riesgo de este paso es cerrar demasiado rápido alrededor de **esfuerzo estimado**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **aprendizajes por experimento** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Ejecutar en orden y documentar el resultado.** Con **aprendizaje esperado** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **entradas con hipótesis completa** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar el backlog con los aprendizajes acumulados.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **entrada del backlog**. **tasa de ejecución** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **entrada del backlog** | Experimento formulado con hipótesis, métrica y criterio de decisión | Cuando **entradas con hipótesis completa** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **fundamento de la hipótesis** | Evidencia o razonamiento que sostiene la expectativa | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un backlog muy formalizado puede frenar pruebas baratas y rápidas. El nivel de formalidad debe ser proporcional al costo del experimento.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre backlog de experimentos |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager, Growth engineer y Head of Growth. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El backlog de Ruta Andina tiene 62 ideas sin hipótesis. Se ejecuta lo que propone quien tiene más influencia en la reunión.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **formular cada idea como hipótesis con fundamento → estimar esfuerzo y aprendizaje esperado → priorizar con un criterio explícito → ejecutar en orden y documentar el resultado → revisar el backlog con los aprendizajes acumulados** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **entradas con hipótesis completa**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Hacking Growth* y la de *Trustworthy Online Controlled Experiments*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **entrada del backlog** y **fundamento de la hipótesis** como sinónimos | Se perdió la distinción entre «experimento formulado con hipótesis, métrica y criterio de decisión» y «evidencia o razonamiento que sostiene la expectativa» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar el backlog con los aprendizajes acumulados» | Se saltó «formular cada idea como hipótesis con fundamento»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **entradas con hipótesis completa** | La métrica local reemplazó al resultado del sistema | Contrástala con **aprendizajes por experimento** y explicita el costo de oportunidad. |
| Mantener ideas sin hipótesis en el backlog | Error específico de esta clase | Exige hipótesis, métrica y criterio de refutación para cada entrada priorizada. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **entrada del backlog** y **fundamento de la hipótesis** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **esfuerzo estimado** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «formular cada idea como hipótesis con fundamento» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **entradas con hipótesis completa** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un backlog muy formalizado puede frenar pruebas baratas y rápidas. El nivel de formalidad debe ser proporcional al costo del experimento»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **esfuerzo estimado** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **entradas con hipótesis completa**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Hacking Growth* y *Inspired*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P19-C09-experiment-backlog/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **entradas con hipótesis completa**, **tasa de ejecución** y **aprendizajes por experimento** con fuente, ventana y lectura prohibida.
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

- Sean Ellis y Morgan Brown — *Hacking Growth* (2017) — **aporta a esta clase:** el backlog de experimentos con hipótesis y criterio previo. **Dónde buscarlo:** los capítulos sobre priorización de pruebas. Registra edición y páginas consultadas en tu nota de lectura.
- Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) — **aporta a esta clase:** las condiciones que hacen confiable un experimento en línea. **Dónde buscarlo:** los capítulos sobre experimentos confiables. Registra edición y páginas consultadas en tu nota de lectura.
- Eric Ries — *The Lean Startup* (2011) — **aporta a esta clase:** el aprendizaje validado como unidad de progreso frente a los hitos de plan. **Dónde buscarlo:** los capítulos sobre aprendizaje validado. Registra edición y páginas consultadas en tu nota de lectura.
- Marty Cagan — *Inspired* (2017, 2.ª ed.) — **aporta a esta clase:** los cuatro riesgos de producto: valor, usabilidad, viabilidad y factibilidad. **Dónde buscarlo:** los capítulos sobre riesgos del descubrimiento. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 08 · Viralidad](class-08-viralidad.md) · [Índice de la parte](README.md) · [Clase 10 · ICE, RICE y priorización](class-10-ice-rice-y-priorizacion.md) →
