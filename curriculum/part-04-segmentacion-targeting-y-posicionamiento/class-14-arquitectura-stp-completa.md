---
title: "Arquitectura STP completa"
type: class
language: es
standard: clase-profunda-v2
part: 04
class: 14
level: Fundamentos
mastery_threshold: 80
estimated_minutes: 150
sources: ["kotler", "rumelt", "ries-trout", "moore"]
anchors: {"kotler": "stp", "moore": "referencias", "ries-trout": "nombre", "rumelt": "nucleo"}
updated: 2026-08-19
---

# Clase 04.14 — Arquitectura STP completa

**Parte 04 · Segmentación, targeting y posicionamiento** · Nivel: Fundamentos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 04.13 — *Prueba de posicionamiento*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de coherencia auditada para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La secuencia segmentación → targeting → posicionamiento como decisión previa a la mezcla comercial — Philip Kotler, Kevin Lane Keller y Alexander Chernev. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Esta clase integra segmentación, targeting y posicionamiento en un documento único y coherente: quién es el segmento prioritario, por qué se eligió, qué se descartó, cuál es la promesa y qué evidencia la sostiene. La prueba de coherencia es que la arquitectura permita rechazar decisiones concretas: un canal, una funcionalidad, una campaña que no correspondan al foco elegido.

Esta sesión distingue lo que se sabe, lo que se supone y lo que todavía no se ha medido. La parte 04 busca **elegir a quién servir y ocupar un lugar defendible en la mente del cliente**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **arquitectura STP completa** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué segmento puedo servir mejor que nadie y con qué diferencia comprobable?

Los conceptos que estructuran la sesión son **arquitectura STP**, **coherencia interna**, **decisión descartada** y **indicador de seguimiento**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `arquitectura STP`, `coherencia interna`, `decisión descartada` y `indicador de seguimiento` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Segmentación, targeting y posicionamiento**.
3. **Aplicar** la secuencia **consolidar la segmentación con sus criterios y evidencia → declarar el foco y los descartes con su justificación → fijar la declaración de posicionamiento y su prueba → verificar coherencia entre promesa, precio, canal y operación → definir los indicadores de seguimiento y su periodicidad** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **coherencia auditada**, **evolución de participación en el segmento prioritario** y **costo de adquisición en el foco** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **arquitectura STP** y **coherencia interna** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **coherencia auditada**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **arquitectura STP** | documento que conecta segmentación, elección de objetivo y posicionamiento con sus fundamentos | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **coherencia interna** | ausencia de contradicción entre segmento elegido, promesa, precio y canal | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **decisión descartada** | opción explícitamente rechazada con su razón, que impide reabrir la discusión sin datos nuevos | Da un hecho compatible con la definición y otro que la refute. |
| **indicador de seguimiento** | métrica que informa si la estrategia elegida está produciendo el efecto esperado | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. consolidar la segmentación con sus criterios y evidencia → 2. declarar el foco y los descartes con su justificación → 3. fijar la declaración de posicionamiento y su prueba → 4. verificar coherencia entre promesa, precio, canal y operación → 5. definir los indicadores de seguimiento y su periodicidad
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** La arquitectura es una hipótesis estratégica, no una verdad. Debe revisarse con datos de resultado y no defenderse por costo hundido.

## 📖 Desarrollo

### 1. Arquitectura STP: mecanismo central

**Arquitectura STP** se entiende aquí como **documento que conecta segmentación, elección de objetivo y posicionamiento con sus fundamentos**.

La arquitectura STP completa es el documento que conecta las tres decisiones y muestra sus consecuencias: a quién se elige, por qué se descartan los demás, cómo se quiere ser percibido y qué cambia en la operación por eso. Su valor está en la coherencia interna: cada decisión debe poder derivarse de la anterior, y cuando no se puede, hay un salto que conviene hacer visible.

**De dónde viene esta afirmación.** Philip Kotler, Kevin Lane Keller y Alexander Chernev — *Marketing Management* (2021, 16.ª ed.) aporta la idea que sostiene este bloque: la secuencia segmentación → targeting → posicionamiento como decisión previa a la mezcla comercial. Búscala en los capítulos sobre identificación de segmentos y posicionamiento de marca. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «coherencia auditada» debería moverse cuando cambie **arquitectura STP**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **coherencia interna**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Coherencia interna: frontera conceptual y error de clasificación

**Definición operacional:** ausencia de contradicción entre segmento elegido, promesa, precio y canal. Su valor está en distinguirlo de **arquitectura STP**.

La coherencia interna se audita con una revisión simple y desagradable: se toma cada elemento del plan comercial —canal, precio, mensaje, criterio de calificación— y se pregunta si sería el mismo con otro segmento objetivo. Los elementos que no cambian son los que no están respondiendo a la decisión de segmentación, y suelen ser mayoría.

**Contraste bibliográfico.** Richard Rumelt — *Good Strategy / Bad Strategy* (2011) aporta aquí una distinción concreta: el núcleo de una estrategia: diagnóstico, política rectora y acción coherente (la parte sobre el núcleo de la buena estrategia). Formula dos mini-casos: uno que satisface la definición de **coherencia interna** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «declarar el foco y los descartes con su justificación», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Decisión descartada: operacionalización y medición

**Decisión descartada** significa **opción explícitamente rechazada con su razón, que impide reabrir la discusión sin datos nuevos**.

La decisión descartada es parte del documento. Registrar qué segmentos se evaluaron y por qué no se eligieron permite, seis meses después, distinguir un cambio de estrategia de una improvisación. También protege al equipo: cuando alguien proponga volver a un segmento descartado, existirá el registro de por qué se descartó y podrá discutirse si esas razones cambiaron.

Ficha de medición obligatoria para **coherencia auditada**: `decisiones comerciales del trimestre compatibles con la arquitectura, sobre decisiones revisadas`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Al Ries y Jack Trout — *Positioning: The Battle for Your Mind* (2001, ed. revisada) pone una condición sobre la medición: el nombre como primer acto de posicionamiento y su efecto en la extensión futura (los capítulos sobre nombre y trampa de la extensión de línea). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Indicador de seguimiento: trade-offs y efectos de segundo orden

**Definición:** métrica que informa si la estrategia elegida está produciendo el efecto esperado.

Una arquitectura muy definida orienta con precisión y limita la capacidad de aprovechar oportunidades imprevistas. La forma de resolverlo no es dejarla vaga sino definir explícitamente la banda de excepción: qué proporción del esfuerzo puede destinarse a oportunidades fuera del plan y quién autoriza. Sin esa banda, la excepción ocurre igual pero sin control.

**Lo que aporta la fuente.** Geoffrey A. Moore — *Crossing the Chasm* (2014, 3.ª ed.) aporta el criterio para pesar el intercambio: las referencias dentro del mismo segmento como mecanismo de adopción (los capítulos sobre segmentación y referencias). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **costo de adquisición en el foco** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **indicador de seguimiento** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «definir los indicadores de seguimiento y su periodicidad», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El STP es una decisión con horizonte, no una verdad. El documento debe incluir el indicador que se seguirá para evaluarla y la fecha de la primera revisión seria. Una arquitectura sin condición de revisión se defiende por identidad y no por resultados, que es exactamente lo que ocurre en las organizaciones donde el posicionamiento sobrevive a tres cambios de mercado.

**Frontera declarada.** La arquitectura es una hipótesis estratégica, no una verdad. Debe revisarse con datos de resultado y no defenderse por costo hundido. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Segmentar con variables decorativas que no cambian oferta, canal ni mensaje.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar arquitectura STP completa no consiste en sumar definiciones. Empieza por **arquitectura STP**, contrasta **coherencia interna** con **decisión descartada**, incorpora **indicador de seguimiento** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Philip Kotler, Kevin Lane Keller y Alexander Chernev — *Marketing Management* (2021, 16.ª ed.) | La secuencia segmentación → targeting → posicionamiento como decisión previa a la mezcla comercial | Los capítulos sobre identificación de segmentos y posicionamiento de marca | ¿Qué debería observarse en **arquitectura STP** si aquí opera «la secuencia segmentación → targeting → posicionamiento como decisión previa a la mezcla comercial»? ¿Y qué observación lo desmentiría en este caso? |
| Richard Rumelt — *Good Strategy / Bad Strategy* (2011) | El núcleo de una estrategia: diagnóstico, política rectora y acción coherente | La parte sobre el núcleo de la buena estrategia | ¿Qué debería observarse en **coherencia interna** si aquí opera «el núcleo de una estrategia: diagnóstico, política rectora y acción coherente»? ¿Y qué observación lo desmentiría en este caso? |
| Al Ries y Jack Trout — *Positioning: The Battle for Your Mind* (2001, ed. revisada) | El nombre como primer acto de posicionamiento y su efecto en la extensión futura | Los capítulos sobre nombre y trampa de la extensión de línea | ¿Qué debería observarse en **decisión descartada** si aquí opera «el nombre como primer acto de posicionamiento y su efecto en la extensión futura»? ¿Y qué observación lo desmentiría en este caso? |
| Geoffrey A. Moore — *Crossing the Chasm* (2014, 3.ª ed.) | Las referencias dentro del mismo segmento como mecanismo de adopción | Los capítulos sobre segmentación y referencias | ¿Qué debería observarse en **indicador de seguimiento** si aquí opera «las referencias dentro del mismo segmento como mecanismo de adopción»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina debe presentar su arquitectura STP al directorio como base del presupuesto anual. Hoy conviven tres focos declarados en documentos distintos.

**Paso 1 — Consolidar la segmentación con sus criterios y evidencia.** El equipo escribe primero el supuesto asociado a **arquitectura STP** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **coherencia auditada** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Declarar el foco y los descartes con su justificación.** El trabajo aquí es separar lo observado de lo inferido sobre **coherencia interna**. La evidencia que ordena la discusión es **evolución de participación en el segmento prioritario**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Fijar la declaración de posicionamiento y su prueba.** El riesgo de este paso es cerrar demasiado rápido alrededor de **decisión descartada**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **costo de adquisición en el foco** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Verificar coherencia entre promesa, precio, canal y operación.** Con **indicador de seguimiento** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **coherencia auditada** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Definir los indicadores de seguimiento y su periodicidad.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **arquitectura STP**. **evolución de participación en el segmento prioritario** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **arquitectura STP** | Documento que conecta segmentación, elección de objetivo y posicionamiento con sus fundamentos | Cuando **coherencia auditada** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **coherencia interna** | Ausencia de contradicción entre segmento elegido, promesa, precio y canal | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** La arquitectura es una hipótesis estratégica, no una verdad. Debe revisarse con datos de resultado y no defenderse por costo hundido.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre arquitectura STP completa |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing manager, Product marketing y Head of Growth. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina debe presentar su arquitectura STP al directorio como base del presupuesto anual. Hoy conviven tres focos declarados en documentos distintos.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **consolidar la segmentación con sus criterios y evidencia → declarar el foco y los descartes con su justificación → fijar la declaración de posicionamiento y su prueba → verificar coherencia entre promesa, precio, canal y operación → definir los indicadores de seguimiento y su periodicidad** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **coherencia auditada**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Marketing Management* y la de *Good Strategy / Bad Strategy*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **arquitectura STP** y **coherencia interna** como sinónimos | Se perdió la distinción entre «documento que conecta segmentación, elección de objetivo y posicionamiento con sus fundamentos» y «ausencia de contradicción entre segmento elegido, promesa, precio y canal» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «definir los indicadores de seguimiento y su periodicidad» | Se saltó «consolidar la segmentación con sus criterios y evidencia»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **coherencia auditada** | La métrica local reemplazó al resultado del sistema | Contrástala con **costo de adquisición en el foco** y explicita el costo de oportunidad. |
| Mantener varios focos declarados simultáneamente | Error específico de esta clase | Consolida en un documento único y archiva formalmente las versiones anteriores. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **arquitectura STP** y **coherencia interna** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **decisión descartada** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «consolidar la segmentación con sus criterios y evidencia» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **coherencia auditada** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «La arquitectura es una hipótesis estratégica, no una verdad. Debe revisarse con datos de resultado y no defenderse por costo hundido»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **decisión descartada** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **coherencia auditada**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Marketing Management* y *Crossing the Chasm*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Segmentar con variables decorativas que no cambian oferta, canal ni mensaje.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P04-C14-arquitectura-stp-completa/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **coherencia auditada**, **evolución de participación en el segmento prioritario** y **costo de adquisición en el foco** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **arquitectura STP con criterios de atractivo, accesibilidad y declaración de posicionamiento probada**.

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

- Philip Kotler, Kevin Lane Keller y Alexander Chernev — *Marketing Management* (2021, 16.ª ed.) — **aporta a esta clase:** la secuencia segmentación → targeting → posicionamiento como decisión previa a la mezcla comercial. **Dónde buscarlo:** los capítulos sobre identificación de segmentos y posicionamiento de marca. Registra edición y páginas consultadas en tu nota de lectura.
- Richard Rumelt — *Good Strategy / Bad Strategy* (2011) — **aporta a esta clase:** el núcleo de una estrategia: diagnóstico, política rectora y acción coherente. **Dónde buscarlo:** la parte sobre el núcleo de la buena estrategia. Registra edición y páginas consultadas en tu nota de lectura.
- Al Ries y Jack Trout — *Positioning: The Battle for Your Mind* (2001, ed. revisada) — **aporta a esta clase:** el nombre como primer acto de posicionamiento y su efecto en la extensión futura. **Dónde buscarlo:** los capítulos sobre nombre y trampa de la extensión de línea. Registra edición y páginas consultadas en tu nota de lectura.
- Geoffrey A. Moore — *Crossing the Chasm* (2014, 3.ª ed.) — **aporta a esta clase:** las referencias dentro del mismo segmento como mecanismo de adopción. **Dónde buscarlo:** los capítulos sobre segmentación y referencias. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 13 · Prueba de posicionamiento](class-13-prueba-de-posicionamiento.md) · [Índice de la parte](README.md)
