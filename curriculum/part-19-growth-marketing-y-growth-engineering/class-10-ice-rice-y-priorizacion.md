---
title: "ICE, RICE y priorización"
type: class
language: es
standard: clase-profunda-v2
part: 19
class: 10
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["ellis-brown", "hubbard", "cagan", "provost"]
anchors: {"cagan": "resultado-output", "ellis-brown": "ciclo", "hubbard": "calibracion", "provost": "valor-esperado"}
updated: 2026-08-19
---

# Clase 19.10 — ICE, RICE y priorización

Clase 10 de 14 de la parte [19 — Growth marketing y growth engineering](README.md), de nivel Crecimiento y analítica. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 19.09, *Backlog de experimentos*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de calibración de estimaciones con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El ciclo de crecimiento: analizar, idear, priorizar y probar, ejecutado con ritmo fijo — Sean Ellis y Morgan Brown. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Los marcos de priorización convierten juicios en números comparables: impacto, confianza, esfuerzo y alcance. Su valor no está en la precisión —los puntajes son estimaciones— sino en hacer explícito el razonamiento y permitir la discusión. Su riesgo es la falsa objetividad: un número inventado con dos decimales sigue siendo una opinión.

Antes de cualquier herramienta, esta clase obliga a nombrar qué cambiaría si el análisis fuese correcto. La parte 19 busca **instalar un motor de experimentación que produzca aprendizaje acumulativo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **ICE, RICE y priorización** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué bucle hace que el crecimiento se retroalimente en lugar de depender del gasto?

Los conceptos que estructuran la sesión son **impacto estimado**, **confianza**, **esfuerzo** y **falsa objetividad**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `impacto estimado`, `confianza`, `esfuerzo` y `falsa objetividad` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Growth marketing y growth engineering**.
3. **Aplicar** la secuencia **definir la escala de cada componente con criterios → puntuar con participación de más de una persona → revisar los casos donde el puntaje contradice la intuición → ejecutar en orden y registrar el resultado → calibrar las estimaciones con los resultados observados** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **calibración de estimaciones**, **dispersión entre evaluadores** y **orden de ejecución respetado** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **impacto estimado** y **confianza** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **calibración de estimaciones**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **impacto estimado** | efecto esperado sobre la métrica objetivo si la hipótesis es correcta | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **confianza** | grado de evidencia que respalda la expectativa de impacto | Da un hecho compatible con la definición y otro que la refute. |
| **esfuerzo** | recursos necesarios para ejecutar, expresados en una unidad comparable | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **falsa objetividad** | apariencia de rigor que produce un puntaje basado en estimaciones subjetivas | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir la escala de cada componente con criterios → 2. puntuar con participación de más de una persona → 3. revisar los casos donde el puntaje contradice la intuición → 4. ejecutar en orden y registrar el resultado → 5. calibrar las estimaciones con los resultados observados
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Ningún marco reemplaza el juicio estratégico. Iniciativas de alto valor y alto esfuerzo pueden quedar postergadas indefinidamente por un puntaje.

## 📖 Desarrollo

### 1. Impacto estimado: mecanismo central

**Impacto estimado** se entiende aquí como **efecto esperado sobre la métrica objetivo si la hipótesis es correcta**.

Los métodos de priorización que combinan impacto, confianza y esfuerzo tienen una virtud y un riesgo. La virtud es forzar a explicitar los tres componentes; el riesgo es que la suma de estimaciones subjetivas produce un número que parece objetivo. Douglas Hubbard mostró que las estimaciones se pueden calibrar, y esa calibración es lo que salva al método.

**De dónde viene esta afirmación.** Sean Ellis y Morgan Brown — *Hacking Growth* (2017) aporta la idea que sostiene este bloque: el ciclo de crecimiento: analizar, idear, priorizar y probar, ejecutado con ritmo fijo. Búscala en los capítulos sobre el proceso de experimentación. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «calibración de estimaciones» debería moverse cuando cambie **impacto estimado**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **confianza**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Confianza: frontera conceptual y error de clasificación

**Definición operacional:** grado de evidencia que respalda la expectativa de impacto. Su valor está en distinguirlo de **impacto estimado**.

La confianza es el componente más informativo y el peor usado. Debe reflejar qué evidencia sustenta la estimación de impacto: un dato propio, un resultado previo, una referencia externa o nada. Registrar esa fuente junto al puntaje permite después revisar si el equipo sobreestima sistemáticamente.

**Contraste bibliográfico.** Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) aporta aquí una distinción concreta: la calibración de estimaciones subjetivas como habilidad entrenable (los capítulos sobre estimación calibrada). Formula dos mini-casos: uno que satisface la definición de **confianza** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «puntuar con participación de más de una persona», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Esfuerzo: operacionalización y medición

**Esfuerzo** significa **recursos necesarios para ejecutar, expresados en una unidad comparable**.

El esfuerzo debe estimarse con quien va a ejecutar y no por quien propone. Las estimaciones de esfuerzo hechas por quien tiene interés en que la idea se priorice son consistentemente optimistas. Ese sesgo es predecible y se corrige con el procedimiento, no con advertencias.

Ficha de medición obligatoria para **calibración de estimaciones**: `diferencia entre impacto estimado y observado, por experimento`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Marty Cagan — *Inspired* (2017, 2.ª ed.) pone una condición sobre la medición: la orientación a resultado en lugar de a entrega de funcionalidades (los capítulos sobre equipos de producto). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Falsa objetividad: trade-offs y efectos de segundo orden

**Definición:** apariencia de rigor que produce un puntaje basado en estimaciones subjetivas.

Un sistema de puntuación acelera la decisión y puede sustituir el juicio: ideas de alto potencial y alta incertidumbre siempre puntúan bajo, y por lo tanto nunca se prueban. Reservar una proporción explícita de la capacidad para apuestas fuera del ranking evita que el método elimine la exploración.

**Lo que aporta la fuente.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta el criterio para pesar el intercambio: el marco de valor esperado que combina probabilidad y consecuencia económica (el capítulo sobre valor esperado). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **orden de ejecución respetado** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **falsa objetividad** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «calibrar las estimaciones con los resultados observados», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La falsa objetividad es el riesgo central: presentar el resultado del cálculo como una conclusión cuando es una suma de opiniones. La forma honesta de usarlo es como estructura de discusión —qué supone cada quien— y no como veredicto. Cuando el puntaje decide sin conversación, el método está siendo mal usado.

**Frontera declarada.** Ningún marco reemplaza el juicio estratégico. Iniciativas de alto valor y alto esfuerzo pueden quedar postergadas indefinidamente por un puntaje. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar ICE, RICE y priorización no consiste en sumar definiciones. Empieza por **impacto estimado**, contrasta **confianza** con **esfuerzo**, incorpora **falsa objetividad** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Sean Ellis y Morgan Brown — *Hacking Growth* (2017) | El ciclo de crecimiento: analizar, idear, priorizar y probar, ejecutado con ritmo fijo | Los capítulos sobre el proceso de experimentación | ¿Qué debería observarse en **impacto estimado** si aquí opera «el ciclo de crecimiento: analizar, idear, priorizar y probar, ejecutado con ritmo fijo»? ¿Y qué observación lo desmentiría en este caso? |
| Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) | La calibración de estimaciones subjetivas como habilidad entrenable | Los capítulos sobre estimación calibrada | ¿Qué debería observarse en **confianza** si aquí opera «la calibración de estimaciones subjetivas como habilidad entrenable»? ¿Y qué observación lo desmentiría en este caso? |
| Marty Cagan — *Inspired* (2017, 2.ª ed.) | La orientación a resultado en lugar de a entrega de funcionalidades | Los capítulos sobre equipos de producto | ¿Qué debería observarse en **esfuerzo** si aquí opera «la orientación a resultado en lugar de a entrega de funcionalidades»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | El marco de valor esperado que combina probabilidad y consecuencia económica | El capítulo sobre valor esperado | ¿Qué debería observarse en **falsa objetividad** si aquí opera «el marco de valor esperado que combina probabilidad y consecuencia económica»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El equipo de Ruta Andina puntúa el impacto con una escala sin criterios. La misma iniciativa recibe 8 y 3 de dos personas distintas.

**Paso 1 — Definir la escala de cada componente con criterios.** El equipo escribe primero el supuesto asociado a **impacto estimado** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **calibración de estimaciones** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Puntuar con participación de más de una persona.** El trabajo aquí es separar lo observado de lo inferido sobre **confianza**. La evidencia que ordena la discusión es **dispersión entre evaluadores**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Revisar los casos donde el puntaje contradice la intuición.** El riesgo de este paso es cerrar demasiado rápido alrededor de **esfuerzo**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **orden de ejecución respetado** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Ejecutar en orden y registrar el resultado.** Con **falsa objetividad** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **calibración de estimaciones** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Calibrar las estimaciones con los resultados observados.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **impacto estimado**. **dispersión entre evaluadores** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **impacto estimado** | Efecto esperado sobre la métrica objetivo si la hipótesis es correcta | Cuando **calibración de estimaciones** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **confianza** | Grado de evidencia que respalda la expectativa de impacto | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Ningún marco reemplaza el juicio estratégico. Iniciativas de alto valor y alto esfuerzo pueden quedar postergadas indefinidamente por un puntaje.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre ICE, RICE y priorización |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager, Growth engineer y Head of Growth. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El equipo de Ruta Andina puntúa el impacto con una escala sin criterios. La misma iniciativa recibe 8 y 3 de dos personas distintas.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir la escala de cada componente con criterios → puntuar con participación de más de una persona → revisar los casos donde el puntaje contradice la intuición → ejecutar en orden y registrar el resultado → calibrar las estimaciones con los resultados observados** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **calibración de estimaciones**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Hacking Growth* y la de *How to Measure Anything*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **impacto estimado** y **confianza** como sinónimos | Se perdió la distinción entre «efecto esperado sobre la métrica objetivo si la hipótesis es correcta» y «grado de evidencia que respalda la expectativa de impacto» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «calibrar las estimaciones con los resultados observados» | Se saltó «definir la escala de cada componente con criterios»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **calibración de estimaciones** | La métrica local reemplazó al resultado del sistema | Contrástala con **orden de ejecución respetado** y explicita el costo de oportunidad. |
| Puntuar sin criterios definidos por escala | Error específico de esta clase | Define qué significa cada valor de la escala y calibra las estimaciones con resultados reales. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **impacto estimado** y **confianza** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **esfuerzo** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir la escala de cada componente con criterios» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **calibración de estimaciones** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Ningún marco reemplaza el juicio estratégico. Iniciativas de alto valor y alto esfuerzo pueden quedar postergadas indefinidamente por un puntaje»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **esfuerzo** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **calibración de estimaciones**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Hacking Growth* y *Data Science for Business*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, comprueba la norma en su texto vigente. Los enlaces van al texto completo publicado por la Biblioteca del Congreso Nacional; son gratuitos y no hace falta creerle a este material.

- **Consumo y comercio.** [Ley 19.496](https://www.bcn.cl/leychile/navegar?idNorma=61438) — *Establece normas sobre protección de los derechos de los consumidores* (Ministerio de Economía, Fomento y Reconstrucción), y su reglamento de comercio electrónico, [Decreto 6/2021](https://www.bcn.cl/leychile/navegar?idNorma=1165504) — *Aprueba reglamento de comercio electrónico* (Ministerio de Economía, Fomento y Turismo).
- **Datos personales.** [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales* (Ministerio Secretaría General de la Presidencia), que sustituye progresivamente a [Ley 19.628](https://www.bcn.cl/leychile/navegar?idNorma=141599) — *Sobre protección de la vida privada* (Ministerio Secretaría General de la Presidencia).
- **Derecho a retracto.** [Decreto 52/2024](https://www.bcn.cl/leychile/navegar?idNorma=1206144) — *Aprueba reglamento que regula la forma y condiciones en que los proveedores deberán comunicar la exclusión del derecho a retracto y los bienes en que excepcionalmente y por su naturaleza procederá tal exclusión* (Ministerio de Economía, Fomento y Turismo).

Dentro del repositorio, el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) ordena qué norma aplica a cada decisión comercial, [datos personales y ética](../../docs/DATOS-PERSONALES-Y-ETICA.md) desarrolla el tratamiento de datos y [fuentes oficiales](../../docs/FUENTES-OFICIALES.md) lista los organismos con su fecha de consulta. Ninguno de esos documentos reemplaza al texto legal.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P19-C10-ice-rice-y-priorizacion/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **calibración de estimaciones**, **dispersión entre evaluadores** y **orden de ejecución respetado** con fuente, ventana y lectura prohibida.
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

Aquí conviene separar dos cosas que suelen ir juntas y no son lo mismo.

**Lo que está comprobado.** Que cada obra existe y cuál es exactamente la edición: el enlace resuelve su ISBN contra el catálogo de OpenLibrary, y eso se revalida periódicamente. Las normas chilenas citadas más arriba enlazan su texto completo y gratuito.

**Lo que es atribución del programa.** Que la idea señalada esté en el capítulo que se indica. Eso es la lectura que este material hace de cada obra, no una cita textual cotejada frase por frase, y se declara así de explícito para que puedas contrastarlo: si abres la obra y no encuentras la idea donde se dice, la cita está mal puesta y **corresponde reportarlo como error del material**. No se citan números de página porque cambian entre ediciones.

- Sean Ellis y Morgan Brown — [*Hacking Growth*](https://openlibrary.org/isbn/9780451497215) (2017) · ISBN 9780451497215 — **aporta a esta clase:** el ciclo de crecimiento: analizar, idear, priorizar y probar, ejecutado con ritmo fijo. **Dónde buscarlo:** los capítulos sobre el proceso de experimentación. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Douglas W. Hubbard — [*How to Measure Anything*](https://openlibrary.org/isbn/9781118836446) (2014, 3.ª ed.) · ISBN 9781118836446 — **aporta a esta clase:** la calibración de estimaciones subjetivas como habilidad entrenable. **Dónde buscarlo:** los capítulos sobre estimación calibrada. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Marty Cagan — [*Inspired*](https://openlibrary.org/isbn/9781119387541) (2017, 2.ª ed.) · ISBN 9781119387541 — **aporta a esta clase:** la orientación a resultado en lugar de a entrega de funcionalidades. **Dónde buscarlo:** los capítulos sobre equipos de producto. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) · ISBN 9781449374280 — **aporta a esta clase:** el marco de valor esperado que combina probabilidad y consecuencia económica. **Dónde buscarlo:** el capítulo sobre valor esperado. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 09 · Backlog de experimentos](class-09-experiment-backlog.md) · [Índice de la parte](README.md) · [Clase 11 · Diseño de experimentos](class-11-experiment-design.md) →
