---
title: "Motivaciones y fricciones"
type: class
language: es
standard: clase-profunda-v2
part: 02
class: 08
level: Fundamentos
mastery_threshold: 80
estimated_minutes: 150
sources: ["krug", "laja", "eisenberg", "thaler"]
anchors: {"eisenberg": "friccion-formulario", "krug": "no-pensar", "laja": "jerarquia-mensaje", "thaler": "arquitectura-decision"}
updated: 2026-08-19
---

# Clase 02.08 — Motivaciones y fricciones

**Parte 02 · Cliente y comportamiento del consumidor** · Nivel: Fundamentos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 02.07 — *Customer journey*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de tasa de finalización por paso para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La primera ley: la página no debe obligar a pensar dónde está uno ni qué hacer — Steve Krug. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Toda conversión es el resultado de una competencia entre motivación y fricción. Aumentar la motivación suele ser caro y lento; reducir fricción suele ser barato y rápido, pero tiene un límite: sin motivación suficiente, ninguna reducción de fricción produce acción. El diagnóstico correcto empieza determinando cuál de las dos domina. Confundirlas lleva a rediseñar un formulario cuando el problema era que la oferta no le importaba a nadie.

El punto de partida de esta clase no es la definición sino la decisión que la definición debe mejorar. La parte 02 busca **construir un expediente de cliente accionable basado en evidencia y no en estereotipos**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **motivaciones y fricciones** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Quién decide, quién usa, quién paga y qué progreso intenta lograr cada uno?

Los conceptos que estructuran la sesión son **motivación**, **fricción**, **umbral de acción** y **fricción productiva**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `motivación`, `fricción`, `umbral de acción` y `fricción productiva` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Cliente y comportamiento del consumidor**.
3. **Aplicar** la secuencia **medir dónde se produce el abandono con datos y no con supuestos → distinguir si el abandono se explica por motivación o por fricción → listar fricciones por costo de remoción → eliminar la fricción de mayor efecto y menor costo → verificar que la remoción no degradó la calidad del cliente ganado** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **tasa de finalización por paso**, **tiempo de finalización** y **calidad del cliente ganado tras remover fricción** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **motivación** y **fricción** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **tasa de finalización por paso**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **motivación** | fuerza que impulsa a actuar, proveniente del valor esperado y de la urgencia del problema | Construye un caso límite donde el concepto se confunde con el anterior. |
| **fricción** | costo de esfuerzo, tiempo, riesgo o confusión que impone el proceso | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **umbral de acción** | punto en que la motivación supera a la fricción y el cliente avanza | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **fricción productiva** | obstáculo deliberado que filtra clientes que no serán rentables o que protege al cliente | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. medir dónde se produce el abandono con datos y no con supuestos → 2. distinguir si el abandono se explica por motivación o por fricción → 3. listar fricciones por costo de remoción → 4. eliminar la fricción de mayor efecto y menor costo → 5. verificar que la remoción no degradó la calidad del cliente ganado
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** No toda fricción debe eliminarse: hay fricción que protege al cliente —confirmaciones, verificaciones— y fricción que protege la economía del negocio.

## 📖 Desarrollo

### 1. Motivación: mecanismo central

**Motivación** se entiende aquí como **fuerza que impulsa a actuar, proveniente del valor esperado y de la urgencia del problema**.

Toda acción del cliente ocurre cuando la motivación supera a la fricción. Es una relación y no dos variables independientes: una fricción tolerable para quien tiene urgencia es un obstáculo definitivo para quien está explorando. Por eso las mismas cinco preguntas de un formulario funcionan bien en una solicitud de cotización y destruyen la conversión en una descarga de contenido introductorio.

**De dónde viene esta afirmación.** Steve Krug — *Don't Make Me Think, Revisited* (2014) aporta la idea que sostiene este bloque: la primera ley: la página no debe obligar a pensar dónde está uno ni qué hacer. Búscala en los capítulos iniciales sobre usabilidad. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «tasa de finalización por paso» debería moverse cuando cambie **motivación**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **fricción**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Fricción: frontera conceptual y error de clasificación

**Definición operacional:** costo de esfuerzo, tiempo, riesgo o confusión que impone el proceso. Su valor está en distinguirlo de **motivación**.

El umbral de acción explica por qué las mejoras de conversión son discontinuas. Reducir la fricción un poco no mueve nada hasta que se cruza el punto donde la balanza se invierte, y entonces el movimiento es abrupto. Esa dinámica hace que las pruebas con cambios muy pequeños den resultados nulos que se interpretan mal: no es que la fricción no importe, es que la reducción fue insuficiente para cruzar el umbral.

**Contraste bibliográfico.** Peep Laja y el equipo de CXL — *Conversion Optimization Playbooks (CXL)* (2024) aporta aquí una distinción concreta: la jerarquía del mensaje según las preguntas reales del visitante (las guías sobre estructura de páginas). Formula dos mini-casos: uno que satisface la definición de **fricción** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «distinguir si el abandono se explica por motivación o por fricción», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Umbral de acción: operacionalización y medición

**Umbral de acción** significa **punto en que la motivación supera a la fricción y el cliente avanza**.

La fricción productiva es la que filtra deliberadamente. Un formulario con una pregunta de calificación reduce el volumen de contactos y mejora la calidad; medirlo sólo con la tasa de envío lleva a eliminarlo. La ficha correcta mide el resultado final —contactos que llegan a oportunidad calificada— y no el resultado intermedio, y declara explícitamente que la caída del volumen es un efecto buscado.

Ficha de medición obligatoria para **tasa de finalización por paso**: `usuarios que completan el paso, sobre usuarios que lo iniciaron, por dispositivo y por origen`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Bryan Eisenberg y Jeffrey Eisenberg — *Call to Action* (2005) pone una condición sobre la medición: la fricción del formulario y su efecto medible sobre el abandono (los capítulos sobre puntos de conversión). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Fricción productiva: trade-offs y efectos de segundo orden

**Definición:** obstáculo deliberado que filtra clientes que no serán rentables o que protege al cliente.

Reducir toda fricción posible acelera la entrada y traslada el trabajo de calificación al equipo comercial, que es el recurso más caro del sistema. Aumentarla protege ese tiempo y deja fuera a clientes legítimos que aún no confían. La decisión depende de dónde está el cuello: si sobra capacidad comercial, conviene abrir; si falta, conviene filtrar. No hay respuesta universal.

**Lo que aporta la fuente.** Richard H. Thaler y Cass R. Sunstein — *Nudge: The Final Edition* (2021) aporta el criterio para pesar el intercambio: la arquitectura de la decisión: no existe presentación neutra de las opciones (los capítulos sobre arquitectura de elección). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **calidad del cliente ganado tras remover fricción** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **fricción productiva** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «verificar que la remoción no degradó la calidad del cliente ganado», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El análisis de motivación y fricción supone que el usuario quiere avanzar y algo se lo impide. Cuando el problema es que la oferta no le interesa, ninguna reducción de fricción lo resuelve, y todas las pruebas de optimización darán resultados marginales. Antes de optimizar el flujo conviene verificar que el mensaje esté encontrando a la persona correcta.

**Frontera declarada.** No toda fricción debe eliminarse: hay fricción que protege al cliente —confirmaciones, verificaciones— y fricción que protege la economía del negocio. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Construir personas ficticias sin datos y usarlas para justificar decisiones caras.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar motivaciones y fricciones no consiste en sumar definiciones. Empieza por **motivación**, contrasta **fricción** con **umbral de acción**, incorpora **fricción productiva** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Steve Krug — *Don't Make Me Think, Revisited* (2014) | La primera ley: la página no debe obligar a pensar dónde está uno ni qué hacer | Los capítulos iniciales sobre usabilidad | ¿Qué debería observarse en **motivación** si aquí opera «la primera ley: la página no debe obligar a pensar dónde está uno ni qué hacer»? ¿Y qué observación lo desmentiría en este caso? |
| Peep Laja y el equipo de CXL — *Conversion Optimization Playbooks (CXL)* (2024) | La jerarquía del mensaje según las preguntas reales del visitante | Las guías sobre estructura de páginas | ¿Qué debería observarse en **fricción** si aquí opera «la jerarquía del mensaje según las preguntas reales del visitante»? ¿Y qué observación lo desmentiría en este caso? |
| Bryan Eisenberg y Jeffrey Eisenberg — *Call to Action* (2005) | La fricción del formulario y su efecto medible sobre el abandono | Los capítulos sobre puntos de conversión | ¿Qué debería observarse en **umbral de acción** si aquí opera «la fricción del formulario y su efecto medible sobre el abandono»? ¿Y qué observación lo desmentiría en este caso? |
| Richard H. Thaler y Cass R. Sunstein — *Nudge: The Final Edition* (2021) | La arquitectura de la decisión: no existe presentación neutra de las opciones | Los capítulos sobre arquitectura de elección | ¿Qué debería observarse en **fricción productiva** si aquí opera «la arquitectura de la decisión: no existe presentación neutra de las opciones»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina eliminó el registro de tarjeta en la prueba gratuita y triplicó los registros. A los 90 días, la conversión a pago cayó de 18 % a 4 % y el equipo de soporte se saturó.

**Paso 1 — Medir dónde se produce el abandono con datos y no con supuestos.** El equipo escribe primero el supuesto asociado a **motivación** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **tasa de finalización por paso** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Distinguir si el abandono se explica por motivación o por fricción.** El trabajo aquí es separar lo observado de lo inferido sobre **fricción**. La evidencia que ordena la discusión es **tiempo de finalización**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Listar fricciones por costo de remoción.** El riesgo de este paso es cerrar demasiado rápido alrededor de **umbral de acción**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **calidad del cliente ganado tras remover fricción** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Eliminar la fricción de mayor efecto y menor costo.** Con **fricción productiva** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **tasa de finalización por paso** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Verificar que la remoción no degradó la calidad del cliente ganado.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **motivación**. **tiempo de finalización** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **motivación** | Fuerza que impulsa a actuar, proveniente del valor esperado y de la urgencia del problema | Cuando **tasa de finalización por paso** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **fricción** | Costo de esfuerzo, tiempo, riesgo o confusión que impone el proceso | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** No toda fricción debe eliminarse: hay fricción que protege al cliente —confirmaciones, verificaciones— y fricción que protege la economía del negocio.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre motivaciones y fricciones |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing manager, Product marketing y Ejecutivo comercial. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina eliminó el registro de tarjeta en la prueba gratuita y triplicó los registros. A los 90 días, la conversión a pago cayó de 18 % a 4 % y el equipo de soporte se saturó.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **medir dónde se produce el abandono con datos y no con supuestos → distinguir si el abandono se explica por motivación o por fricción → listar fricciones por costo de remoción → eliminar la fricción de mayor efecto y menor costo → verificar que la remoción no degradó la calidad del cliente ganado** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **tasa de finalización por paso**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Don't Make Me Think, Revisited* y la de *Conversion Optimization Playbooks (CXL)*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **motivación** y **fricción** como sinónimos | Se perdió la distinción entre «fuerza que impulsa a actuar, proveniente del valor esperado y de la urgencia del problema» y «costo de esfuerzo, tiempo, riesgo o confusión que impone el proceso» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «verificar que la remoción no degradó la calidad del cliente ganado» | Se saltó «medir dónde se produce el abandono con datos y no con supuestos»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **tasa de finalización por paso** | La métrica local reemplazó al resultado del sistema | Contrástala con **calidad del cliente ganado tras remover fricción** y explicita el costo de oportunidad. |
| Eliminar fricción sin medir la calidad posterior | Error específico de esta clase | Compara retención y conversión a pago de la cohorte nueva antes de declarar la mejora. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **motivación** y **fricción** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **umbral de acción** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «medir dónde se produce el abandono con datos y no con supuestos» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **tasa de finalización por paso** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «No toda fricción debe eliminarse: hay fricción que protege al cliente —confirmaciones, verificaciones— y fricción que protege la economía del negocio»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **umbral de acción** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **tasa de finalización por paso**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Don't Make Me Think, Revisited* y *Nudge: The Final Edition*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Construir personas ficticias sin datos y usarlas para justificar decisiones caras.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P02-C08-motivaciones-y-fricciones/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **tasa de finalización por paso**, **tiempo de finalización** y **calidad del cliente ganado tras remover fricción** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **expediente de cliente con ICP, unidad de decisión, journey y fricciones priorizadas**.

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

- Steve Krug — *Don't Make Me Think, Revisited* (2014) — **aporta a esta clase:** la primera ley: la página no debe obligar a pensar dónde está uno ni qué hacer. **Dónde buscarlo:** los capítulos iniciales sobre usabilidad. Registra edición y páginas consultadas en tu nota de lectura.
- Peep Laja y el equipo de CXL — *Conversion Optimization Playbooks (CXL)* (2024) — **aporta a esta clase:** la jerarquía del mensaje según las preguntas reales del visitante. **Dónde buscarlo:** las guías sobre estructura de páginas. Registra edición y páginas consultadas en tu nota de lectura.
- Bryan Eisenberg y Jeffrey Eisenberg — *Call to Action* (2005) — **aporta a esta clase:** la fricción del formulario y su efecto medible sobre el abandono. **Dónde buscarlo:** los capítulos sobre puntos de conversión. Registra edición y páginas consultadas en tu nota de lectura.
- Richard H. Thaler y Cass R. Sunstein — *Nudge: The Final Edition* (2021) — **aporta a esta clase:** la arquitectura de la decisión: no existe presentación neutra de las opciones. **Dónde buscarlo:** los capítulos sobre arquitectura de elección. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 07 · Customer journey](class-07-customer-journey.md) · [Índice de la parte](README.md) · [Clase 09 · Sesgos cognitivos y decisiones](class-09-sesgos-cognitivos-y-decisiones.md) →
