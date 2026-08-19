---
title: "Mapa de IA comercial"
type: class
language: es
standard: clase-profunda-v2
part: 21
class: 01
level: IA y expansión
mastery_threshold: 80
estimated_minutes: 150
sources: ["russell-norvig", "nist-airmf", "provost", "ng-mlyearning"]
anchors: {"ng-mlyearning": "metrica-unica", "nist-airmf": "funciones", "provost": "formulacion", "russell-norvig": "agente-racional"}
updated: 2026-08-19
---

# Clase 21.01 — Mapa de IA comercial

**Parte 21 · IA aplicada a marketing, ventas y servicio** · Nivel: IA y expansión · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | Ninguna clase previa dentro de esta parte. Si vienes de otra parte, ten a la vista su artefacto final; si empiezas el programa aquí, lee antes `docs/RUTA-DE-APRENDIZAJE.md`. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de casos de uso con criterio de éxito para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El agente racional definido por su medida de desempeño, entorno, actuadores y sensores — Stuart Russell y Peter Norvig. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La inteligencia artificial aplicada a lo comercial cubre tareas muy distintas: generación de texto, clasificación, predicción, recuperación de información y automatización de acciones. Cada una tiene requisitos, riesgos y formas de evaluación propias. Tratar todo como «usar IA» impide decidir: la pregunta correcta es qué tarea concreta mejora, con qué evidencia y quién responde cuando falla.

El punto de partida de esta clase no es la definición sino la decisión que la definición debe mejorar. La parte 21 busca **usar IA como capacidad operativa con evaluación, control y responsabilidad humana**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **mapa de IA comercial** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué tarea mejora con IA, cómo sé que mejora y quién responde cuando falla?

Los conceptos que estructuran la sesión son **tarea automatizable**, **tipo de sistema**, **criterio de éxito** y **responsabilidad humana**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `tarea automatizable`, `tipo de sistema`, `criterio de éxito` y `responsabilidad humana` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **IA aplicada a marketing, ventas y servicio**.
3. **Aplicar** la secuencia **inventariar tareas comerciales candidatas → clasificar cada una por tipo de sistema requerido → definir el criterio de éxito y el costo del error → asignar responsable humano por cada uso → priorizar por valor y por riesgo controlable** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **casos de uso con criterio de éxito**, **costo del error por caso** y **usos con responsable asignado** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **tarea automatizable** y **tipo de sistema** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **casos de uso con criterio de éxito**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **tarea automatizable** | actividad concreta con entrada y salida definidas que un sistema puede ejecutar | Da un hecho compatible con la definición y otro que la refute. |
| **tipo de sistema** | clasificación según lo que hace: genera, clasifica, predice, recupera o actúa | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **criterio de éxito** | definición operacional de qué significa que el sistema funcione bien | Construye un caso límite donde el concepto se confunde con el anterior. |
| **responsabilidad humana** | persona que responde por el resultado con independencia de la automatización | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. inventariar tareas comerciales candidatas → 2. clasificar cada una por tipo de sistema requerido → 3. definir el criterio de éxito y el costo del error → 4. asignar responsable humano por cada uso → 5. priorizar por valor y por riesgo controlable
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** La IA no resuelve problemas de proceso ni de datos: los amplifica. Automatizar sobre información de mala calidad produce errores más rápido.

## 📖 Desarrollo

### 1. Tarea automatizable: mecanismo central

**Tarea automatizable** se entiende aquí como **actividad concreta con entrada y salida definidas que un sistema puede ejecutar**.

Antes de decidir qué automatizar con inteligencia artificial hay que describir la tarea con precisión: qué entra, qué sale, cómo se sabe si el resultado es correcto y quién responde si no lo es. Stuart Russell y Peter Norvig plantean esa descripción como definición de agente racional, y su utilidad práctica es que obliga a explicitar la medida de desempeño antes de elegir tecnología.

**De dónde viene esta afirmación.** Stuart Russell y Peter Norvig — *Artificial Intelligence: A Modern Approach* (2021, 4.ª ed.) aporta la idea que sostiene este bloque: el agente racional definido por su medida de desempeño, entorno, actuadores y sensores. Búscala en los capítulos sobre agentes inteligentes. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «casos de uso con criterio de éxito» debería moverse cuando cambie **tarea automatizable**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **tipo de sistema**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Tipo de sistema: frontera conceptual y error de clasificación

**Definición operacional:** clasificación según lo que hace: genera, clasifica, predice, recupera o actúa. Su valor está en distinguirlo de **tarea automatizable**.

El tipo de sistema importa: no es lo mismo un modelo que clasifica, uno que genera texto y uno que ejecuta acciones. Cada uno tiene modos de falla distintos y exige controles distintos. Tratar todos los usos bajo la misma categoría produce políticas que son excesivas para unos e insuficientes para otros.

**Contraste bibliográfico.** NIST — *AI Risk Management Framework 1.0* (2023) aporta aquí una distinción concreta: las cuatro funciones: mapear, medir, gestionar y gobernar el riesgo de IA (el núcleo del marco). Formula dos mini-casos: uno que satisface la definición de **tipo de sistema** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «clasificar cada una por tipo de sistema requerido», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Criterio de éxito: operacionalización y medición

**Criterio de éxito** significa **definición operacional de qué significa que el sistema funcione bien**.

El criterio de éxito debe definirse antes y ser medible con datos que existan. «Mejorar la productividad» no es un criterio; «reducir el tiempo de preparación de una propuesta manteniendo la tasa de errores por debajo del nivel actual» sí lo es. Sin criterio previo, cualquier resultado se interpretará como éxito.

Ficha de medición obligatoria para **casos de uso con criterio de éxito**: `usos con métrica de evaluación definida, sobre usos activos`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) pone una condición sobre la medición: la formulación del problema de negocio como problema de datos antes de elegir técnica (los capítulos iniciales sobre pensamiento analítico). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Responsabilidad humana: trade-offs y efectos de segundo orden

**Definición:** persona que responde por el resultado con independencia de la automatización.

Automatizar más libera tiempo y traslada el error a un lugar menos visible: un sistema que se equivoca de forma consistente produce daño a escala antes de que alguien lo note. La decisión debe considerar el costo del error multiplicado por el volumen, no sólo el ahorro de tiempo.

**Lo que aporta la fuente.** Andrew Ng — *Machine Learning Yearning* (2018) aporta el criterio para pesar el intercambio: una métrica de evaluación única para poder comparar alternativas (los capítulos sobre métricas de evaluación). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **usos con responsable asignado** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **responsabilidad humana** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «priorizar por valor y por riesgo controlable», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La responsabilidad humana no se transfiere al sistema. Quien despliega una herramienta responde por sus resultados frente al cliente y frente al regulador. Esa asignación debe ser explícita y nominal antes del despliegue, porque después del incidente la discusión sobre quién respondía se vuelve estéril.

**Frontera declarada.** La IA no resuelve problemas de proceso ni de datos: los amplifica. Automatizar sobre información de mala calidad produce errores más rápido. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar mapa de IA comercial no consiste en sumar definiciones. Empieza por **tarea automatizable**, contrasta **tipo de sistema** con **criterio de éxito**, incorpora **responsabilidad humana** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Stuart Russell y Peter Norvig — *Artificial Intelligence: A Modern Approach* (2021, 4.ª ed.) | El agente racional definido por su medida de desempeño, entorno, actuadores y sensores | Los capítulos sobre agentes inteligentes | ¿Qué debería observarse en **tarea automatizable** si aquí opera «el agente racional definido por su medida de desempeño, entorno, actuadores y sensores»? ¿Y qué observación lo desmentiría en este caso? |
| NIST — *AI Risk Management Framework 1.0* (2023) | Las cuatro funciones: mapear, medir, gestionar y gobernar el riesgo de IA | El núcleo del marco | ¿Qué debería observarse en **tipo de sistema** si aquí opera «las cuatro funciones: mapear, medir, gestionar y gobernar el riesgo de IA»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La formulación del problema de negocio como problema de datos antes de elegir técnica | Los capítulos iniciales sobre pensamiento analítico | ¿Qué debería observarse en **criterio de éxito** si aquí opera «la formulación del problema de negocio como problema de datos antes de elegir técnica»? ¿Y qué observación lo desmentiría en este caso? |
| Andrew Ng — *Machine Learning Yearning* (2018) | Una métrica de evaluación única para poder comparar alternativas | Los capítulos sobre métricas de evaluación | ¿Qué debería observarse en **responsabilidad humana** si aquí opera «una métrica de evaluación única para poder comparar alternativas»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina «adoptó IA» activando un asistente en soporte, un generador de textos y un modelo de puntuación. Ninguno tiene criterio de éxito ni responsable definido.

**Paso 1 — Inventariar tareas comerciales candidatas.** El equipo escribe primero el supuesto asociado a **tarea automatizable** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **casos de uso con criterio de éxito** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Clasificar cada una por tipo de sistema requerido.** El trabajo aquí es separar lo observado de lo inferido sobre **tipo de sistema**. La evidencia que ordena la discusión es **costo del error por caso**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Definir el criterio de éxito y el costo del error.** El riesgo de este paso es cerrar demasiado rápido alrededor de **criterio de éxito**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **usos con responsable asignado** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Asignar responsable humano por cada uso.** Con **responsabilidad humana** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **casos de uso con criterio de éxito** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Priorizar por valor y por riesgo controlable.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **tarea automatizable**. **costo del error por caso** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **tarea automatizable** | Actividad concreta con entrada y salida definidas que un sistema puede ejecutar | Cuando **casos de uso con criterio de éxito** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **tipo de sistema** | Clasificación según lo que hace: genera, clasifica, predice, recupera o actúa | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** La IA no resuelve problemas de proceso ni de datos: los amplifica. Automatizar sobre información de mala calidad produce errores más rápido.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre mapa de IA comercial |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager con IA, RevOps, Marketing manager y Sales enablement. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina «adoptó IA» activando un asistente en soporte, un generador de textos y un modelo de puntuación. Ninguno tiene criterio de éxito ni responsable definido.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **inventariar tareas comerciales candidatas → clasificar cada una por tipo de sistema requerido → definir el criterio de éxito y el costo del error → asignar responsable humano por cada uso → priorizar por valor y por riesgo controlable** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **casos de uso con criterio de éxito**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Artificial Intelligence: A Modern Approach* y la de *AI Risk Management Framework 1.0*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **tarea automatizable** y **tipo de sistema** como sinónimos | Se perdió la distinción entre «actividad concreta con entrada y salida definidas que un sistema puede ejecutar» y «clasificación según lo que hace: genera, clasifica, predice, recupera o actúa» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «priorizar por valor y por riesgo controlable» | Se saltó «inventariar tareas comerciales candidatas»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **casos de uso con criterio de éxito** | La métrica local reemplazó al resultado del sistema | Contrástala con **usos con responsable asignado** y explicita el costo de oportunidad. |
| Adoptar herramientas sin definir la tarea ni el criterio de éxito | Error específico de esta clase | Declara la tarea, su métrica de evaluación y su responsable antes de activar cualquier sistema. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **tarea automatizable** y **tipo de sistema** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **criterio de éxito** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «inventariar tareas comerciales candidatas» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **casos de uso con criterio de éxito** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «La IA no resuelve problemas de proceso ni de datos: los amplifica. Automatizar sobre información de mala calidad produce errores más rápido»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **criterio de éxito** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **casos de uso con criterio de éxito**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Artificial Intelligence: A Modern Approach* y *Machine Learning Yearning*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P21-C01-mapa-de-ia-comercial/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **casos de uso con criterio de éxito**, **costo del error por caso** y **usos con responsable asignado** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **operating model humano-IA con casos de uso, evaluaciones, guardrails y registro de incidentes**.

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

- Stuart Russell y Peter Norvig — *Artificial Intelligence: A Modern Approach* (2021, 4.ª ed.) — **aporta a esta clase:** el agente racional definido por su medida de desempeño, entorno, actuadores y sensores. **Dónde buscarlo:** los capítulos sobre agentes inteligentes. Registra edición y páginas consultadas en tu nota de lectura.
- NIST — *AI Risk Management Framework 1.0* (2023) — **aporta a esta clase:** las cuatro funciones: mapear, medir, gestionar y gobernar el riesgo de IA. **Dónde buscarlo:** el núcleo del marco. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — **aporta a esta clase:** la formulación del problema de negocio como problema de datos antes de elegir técnica. **Dónde buscarlo:** los capítulos iniciales sobre pensamiento analítico. Registra edición y páginas consultadas en tu nota de lectura.
- Andrew Ng — *Machine Learning Yearning* (2018) — **aporta a esta clase:** una métrica de evaluación única para poder comparar alternativas. **Dónde buscarlo:** los capítulos sobre métricas de evaluación. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

[Índice de la parte](README.md) · [Clase 02 · Prompting con contexto comercial](class-02-prompting-con-contexto-comercial.md) →
