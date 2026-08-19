---
title: "Higiene de datos"
type: class
language: es
standard: clase-profunda-v2
part: 16
class: 05
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["diorio", "provost", "roberge", "oneil"]
anchors: {"diorio": "modelo-datos", "oneil": "proxy", "provost": "fuga-datos", "roberge": "metricas-coaching"}
updated: 2026-08-19
---

# Clase 16.05 — Higiene de datos

Clase 5 de 14 de la parte [16 — CRM, pipeline y sales operations](README.md), de nivel Operación de ingresos. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 16.04, *Lead, contacto, cuenta y oportunidad*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de tasa de datos obsoletos con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El modelo de datos común como condición para que las áreas discutan sobre lo mismo — Stephen G. Diorio y Chris K. Hummel. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Los datos comerciales se degradan de forma continua: personas cambian de trabajo, empresas cierran, correos rebotan. Sin un proceso de higiene, la base pierde valor cada mes y las decisiones se toman sobre información obsoleta. La higiene incluye además una obligación legal: mantener datos exactos y eliminarlos cuando ya no son necesarios para la finalidad declarada.

La clase trata el tema como un problema de evidencia y de consecuencia, no como vocabulario. La parte 16 busca **convertir el CRM en un sistema de trabajo y de verdad operacional**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **higiene de datos** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿El pipeline describe la realidad o solo el optimismo del equipo?

Los conceptos que estructuran la sesión son **degradación de datos**, **deduplicación**, **exactitud** y **retención de datos**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `degradación de datos`, `deduplicación`, `exactitud` y `retención de datos` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **CRM, pipeline y sales operations**.
3. **Aplicar** la secuencia **medir el estado actual de completitud y exactitud → establecer rutinas de deduplicación y verificación → definir la política de retención y eliminación → asignar responsables por tipo de dato → reportar el estado de la base cada trimestre** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **tasa de datos obsoletos**, **duplicados por trimestre** y **cumplimiento de la política de retención** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **degradación de datos** y **deduplicación** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **tasa de datos obsoletos**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **degradación de datos** | pérdida progresiva de vigencia de la información de contacto | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **deduplicación** | proceso de identificar y consolidar registros repetidos | Da un hecho compatible con la definición y otro que la refute. |
| **exactitud** | correspondencia entre el dato registrado y la realidad actual | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **retención de datos** | periodo durante el cual se conserva la información según su finalidad | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. medir el estado actual de completitud y exactitud → 2. establecer rutinas de deduplicación y verificación → 3. definir la política de retención y eliminación → 4. asignar responsables por tipo de dato → 5. reportar el estado de la base cada trimestre
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** La eliminación de datos puede entrar en tensión con obligaciones de conservación tributaria o contractual. La política debe distinguir tipos de dato y finalidad.

## 📖 Desarrollo

### 1. Degradación de datos: mecanismo central

**Degradación de datos** se entiende aquí como **pérdida progresiva de vigencia de la información de contacto**.

Los datos comerciales se degradan de forma continua: las personas cambian de cargo, las empresas cambian de nombre, los correos dejan de existir. Una base sin mantenimiento pierde una proporción significativa de su validez cada año. Ese deterioro es predecible y por lo tanto planificable, aunque casi nunca se planifica.

**De dónde viene esta afirmación.** Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) aporta la idea que sostiene este bloque: el modelo de datos común como condición para que las áreas discutan sobre lo mismo. Búscala en los capítulos sobre infraestructura de datos comercial. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «tasa de datos obsoletos» debería moverse cuando cambie **degradación de datos**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **deduplicación**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Deduplicación: frontera conceptual y error de clasificación

**Definición operacional:** proceso de identificar y consolidar registros repetidos. Su valor está en distinguirlo de **degradación de datos**.

La deduplicación es un problema técnico con consecuencias comerciales: dos registros de la misma cuenta producen contactos duplicados, atribuciones erróneas y la impresión de desorganización ante el cliente. Su prevención está en las reglas de creación de registros, no en las limpiezas periódicas, que sólo corrigen el síntoma.

**Contraste bibliográfico.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta aquí una distinción concreta: la fuga de información: un modelo que predice demasiado bien suele estar mal construido (los capítulos sobre problemas de datos). Formula dos mini-casos: uno que satisface la definición de **deduplicación** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «establecer rutinas de deduplicación y verificación», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Exactitud: operacionalización y medición

**Exactitud** significa **correspondencia entre el dato registrado y la realidad actual**.

La exactitud se mide con muestreo: tomar un conjunto de registros al azar y verificar campo por campo contra la realidad. Es un trabajo manual y acotado que entrega una tasa de error por campo. Esa tasa permite decidir qué campos merecen inversión en corrección y cuáles ya no son confiables para decidir.

Ficha de medición obligatoria para **tasa de datos obsoletos**: `registros con rebote o contacto fallido, sobre registros contactados`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Mark Roberge — *The Sales Acceleration Formula* (2015) pone una condición sobre la medición: el acompañamiento dirigido por una métrica diagnóstica por vendedor (los capítulos sobre la fórmula de gestión). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Retención de datos: trade-offs y efectos de segundo orden

**Definición:** periodo durante el cual se conserva la información según su finalidad.

Mantener la calidad exige tiempo que compite con la actividad comercial. Automatizar ayuda y también introduce errores sistemáticos cuando las reglas están mal definidas. La combinación razonable automatiza la detección y deja la corrección de casos ambiguos a una persona, con un tiempo asignado explícito.

**Lo que aporta la fuente.** Cathy O'Neil — *Weapons of Math Destruction* (2016) aporta el criterio para pesar el intercambio: las variables sustitutas que codifican prejuicio sin nombrarlo (los capítulos sobre selección de variables). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **cumplimiento de la política de retención** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **retención de datos** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «reportar el estado de la base cada trimestre», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La conservación de datos personales tiene límites de plazo y de finalidad. Mantener indefinidamente registros de contactos que nunca avanzaron no sólo deteriora la base: puede incumplir obligaciones de conservación. Definir políticas de retención y aplicarlas técnicamente es parte de la higiene, no un asunto separado.

**Frontera declarada.** La eliminación de datos puede entrar en tensión con obligaciones de conservación tributaria o contractual. La política debe distinguir tipos de dato y finalidad. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Tomar decisiones de contratación y presupuesto sobre un pipeline que no representa la realidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar higiene de datos no consiste en sumar definiciones. Empieza por **degradación de datos**, contrasta **deduplicación** con **exactitud**, incorpora **retención de datos** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) | El modelo de datos común como condición para que las áreas discutan sobre lo mismo | Los capítulos sobre infraestructura de datos comercial | ¿Qué debería observarse en **degradación de datos** si aquí opera «el modelo de datos común como condición para que las áreas discutan sobre lo mismo»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La fuga de información: un modelo que predice demasiado bien suele estar mal construido | Los capítulos sobre problemas de datos | ¿Qué debería observarse en **deduplicación** si aquí opera «la fuga de información: un modelo que predice demasiado bien suele estar mal construido»? ¿Y qué observación lo desmentiría en este caso? |
| Mark Roberge — *The Sales Acceleration Formula* (2015) | El acompañamiento dirigido por una métrica diagnóstica por vendedor | Los capítulos sobre la fórmula de gestión | ¿Qué debería observarse en **exactitud** si aquí opera «el acompañamiento dirigido por una métrica diagnóstica por vendedor»? ¿Y qué observación lo desmentiría en este caso? |
| Cathy O'Neil — *Weapons of Math Destruction* (2016) | Las variables sustitutas que codifican prejuicio sin nombrarlo | Los capítulos sobre selección de variables | ¿Qué debería observarse en **retención de datos** si aquí opera «las variables sustitutas que codifican prejuicio sin nombrarlo»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** La base de Ruta Andina tiene 12.400 contactos, 31 % con rebote y registros de personas que solicitaron eliminación hace ocho meses.

**Paso 1 — Medir el estado actual de completitud y exactitud.** El equipo escribe primero el supuesto asociado a **degradación de datos** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **tasa de datos obsoletos** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Establecer rutinas de deduplicación y verificación.** El trabajo aquí es separar lo observado de lo inferido sobre **deduplicación**. La evidencia que ordena la discusión es **duplicados por trimestre**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Definir la política de retención y eliminación.** El riesgo de este paso es cerrar demasiado rápido alrededor de **exactitud**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **cumplimiento de la política de retención** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Asignar responsables por tipo de dato.** Con **retención de datos** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **tasa de datos obsoletos** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Reportar el estado de la base cada trimestre.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **degradación de datos**. **duplicados por trimestre** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **degradación de datos** | Pérdida progresiva de vigencia de la información de contacto | Cuando **tasa de datos obsoletos** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **deduplicación** | Proceso de identificar y consolidar registros repetidos | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** La eliminación de datos puede entrar en tensión con obligaciones de conservación tributaria o contractual. La política debe distinguir tipos de dato y finalidad.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre higiene de datos |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Sales operations, RevOps analyst y Jefe de ventas. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

La base de Ruta Andina tiene 12.400 contactos, 31 % con rebote y registros de personas que solicitaron eliminación hace ocho meses.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **medir el estado actual de completitud y exactitud → establecer rutinas de deduplicación y verificación → definir la política de retención y eliminación → asignar responsables por tipo de dato → reportar el estado de la base cada trimestre** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **tasa de datos obsoletos**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Revenue Operations* y la de *Data Science for Business*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **degradación de datos** y **deduplicación** como sinónimos | Se perdió la distinción entre «pérdida progresiva de vigencia de la información de contacto» y «proceso de identificar y consolidar registros repetidos» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «reportar el estado de la base cada trimestre» | Se saltó «medir el estado actual de completitud y exactitud»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **tasa de datos obsoletos** | La métrica local reemplazó al resultado del sistema | Contrástala con **cumplimiento de la política de retención** y explicita el costo de oportunidad. |
| No eliminar datos tras una solicitud del titular | Error específico de esta clase | Implementa un procedimiento verificable de eliminación con plazo y registro de cumplimiento. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **degradación de datos** y **deduplicación** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **exactitud** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «medir el estado actual de completitud y exactitud» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **tasa de datos obsoletos** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «La eliminación de datos puede entrar en tensión con obligaciones de conservación tributaria o contractual. La política debe distinguir tipos de dato y finalidad»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **exactitud** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **tasa de datos obsoletos**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Revenue Operations* y *Weapons of Math Destruction*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Tomar decisiones de contratación y presupuesto sobre un pipeline que no representa la realidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, comprueba la norma en su texto vigente. Los enlaces van al texto completo publicado por la Biblioteca del Congreso Nacional; son gratuitos y no hace falta creerle a este material.

- **Consumo y comercio.** [Ley 19.496](https://www.bcn.cl/leychile/navegar?idNorma=61438) — *Establece normas sobre protección de los derechos de los consumidores* (Ministerio de Economía, Fomento y Reconstrucción), y su reglamento de comercio electrónico, [Decreto 6/2021](https://www.bcn.cl/leychile/navegar?idNorma=1165504) — *Aprueba reglamento de comercio electrónico* (Ministerio de Economía, Fomento y Turismo).
- **Datos personales.** [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales* (Ministerio Secretaría General de la Presidencia), que sustituye progresivamente a [Ley 19.628](https://www.bcn.cl/leychile/navegar?idNorma=141599) — *Sobre protección de la vida privada* (Ministerio Secretaría General de la Presidencia).
- **Derecho a retracto.** [Decreto 52/2024](https://www.bcn.cl/leychile/navegar?idNorma=1206144) — *Aprueba reglamento que regula la forma y condiciones en que los proveedores deberán comunicar la exclusión del derecho a retracto y los bienes en que excepcionalmente y por su naturaleza procederá tal exclusión* (Ministerio de Economía, Fomento y Turismo).

Dentro del repositorio, el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) ordena qué norma aplica a cada decisión comercial, [datos personales y ética](../../docs/DATOS-PERSONALES-Y-ETICA.md) desarrolla el tratamiento de datos y [fuentes oficiales](../../docs/FUENTES-OFICIALES.md) lista los organismos con su fecha de consulta. Ninguno de esos documentos reemplaza al texto legal.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P16-C05-higiene-de-datos/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **tasa de datos obsoletos**, **duplicados por trimestre** y **cumplimiento de la política de retención** con fuente, ventana y lectura prohibida.
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

Aquí conviene separar dos cosas que suelen ir juntas y no son lo mismo.

**Lo que está comprobado.** Que cada obra existe y cuál es exactamente la edición: el enlace resuelve su ISBN contra el catálogo de OpenLibrary, y eso se revalida periódicamente. Las normas chilenas citadas más arriba enlazan su texto completo y gratuito.

**Lo que es atribución del programa.** Que la idea señalada esté en el capítulo que se indica. Eso es la lectura que este material hace de cada obra, no una cita textual cotejada frase por frase, y se declara así de explícito para que puedas contrastarlo: si abres la obra y no encuentras la idea donde se dice, la cita está mal puesta y **corresponde reportarlo como error del material**. No se citan números de página porque cambian entre ediciones.

- Stephen G. Diorio y Chris K. Hummel — [*Revenue Operations*](https://openlibrary.org/isbn/9781119871132) (2022) · ISBN 9781119871132 — **aporta a esta clase:** el modelo de datos común como condición para que las áreas discutan sobre lo mismo. **Dónde buscarlo:** los capítulos sobre infraestructura de datos comercial. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) · ISBN 9781449374280 — **aporta a esta clase:** la fuga de información: un modelo que predice demasiado bien suele estar mal construido. **Dónde buscarlo:** los capítulos sobre problemas de datos. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Mark Roberge — [*The Sales Acceleration Formula*](https://openlibrary.org/isbn/9781119047018) (2015) · ISBN 9781119047018 — **aporta a esta clase:** el acompañamiento dirigido por una métrica diagnóstica por vendedor. **Dónde buscarlo:** los capítulos sobre la fórmula de gestión. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Cathy O'Neil — [*Weapons of Math Destruction*](https://openlibrary.org/isbn/9780141985428) (2016) · ISBN 9780141985428 — **aporta a esta clase:** las variables sustitutas que codifican prejuicio sin nombrarlo. **Dónde buscarlo:** los capítulos sobre selección de variables. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 04 · Lead, contacto, cuenta y oportunidad](class-04-lead-contact-account-y-opportunity.md) · [Índice de la parte](README.md) · [Clase 06 · Actividades comerciales](class-06-actividades-comerciales.md) →
