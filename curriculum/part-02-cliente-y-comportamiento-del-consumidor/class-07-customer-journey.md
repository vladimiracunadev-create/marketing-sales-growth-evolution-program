---
title: "Customer journey"
type: class
language: es
standard: clase-profunda-v2
part: 02
class: 07
level: Fundamentos
mastery_threshold: 80
estimated_minutes: 150
sources: ["dixon-effort", "krug", "solomon", "kotler"]
anchors: {"dixon-effort": "canal-preferido", "kotler": "canales", "krug": "escaneo", "solomon": "proceso-decision"}
updated: 2026-08-19
---

# Clase 02.07 — Customer journey

**Parte 02 · Cliente y comportamiento del consumidor** · Nivel: Fundamentos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 02.06 — *Unidad de decisión en B2B*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de esfuerzo percibido por etapa para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El traslado forzado de canal como fuente principal de esfuerzo percibido — Matthew Dixon, Nick Toman y Rick DeLisi. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Un mapa de journey útil describe lo que hace y siente el cliente, no lo que hace la empresa. Su valor aparece cuando cada etapa registra: qué intenta lograr, qué información busca, con quién conversa, qué fricción encuentra y qué evidencia necesita para avanzar. Un mapa que sólo enumera canales propios es un organigrama disfrazado. El journey además no termina en la compra: la experiencia posterior determina renovación, referencia y reputación.

Esta sesión distingue lo que se sabe, lo que se supone y lo que todavía no se ha medido. La parte 02 busca **construir un expediente de cliente accionable basado en evidencia y no en estereotipos**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **customer journey** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Quién decide, quién usa, quién paga y qué progreso intenta lograr cada uno?

Los conceptos que estructuran la sesión son **etapa del journey**, **punto de dolor**, **momento de la verdad** y **brecha de expectativa**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `etapa del journey`, `punto de dolor`, `momento de la verdad` y `brecha de expectativa` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Cliente y comportamiento del consumidor**.
3. **Aplicar** la secuencia **definir las etapas desde la perspectiva del cliente → documentar objetivo, información buscada y fricción por etapa → identificar los momentos de la verdad → medir esfuerzo o abandono en cada uno → priorizar intervenciones por costo y efecto** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **esfuerzo percibido por etapa**, **abandono por etapa** y **brecha de expectativa en onboarding** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **etapa del journey** y **punto de dolor** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **esfuerzo percibido por etapa**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **etapa del journey** | momento definido por el objetivo del cliente y no por el canal que la empresa usa | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **punto de dolor** | fricción concreta que aumenta esfuerzo, riesgo o tiempo del cliente en una etapa | Construye un caso límite donde el concepto se confunde con el anterior. |
| **momento de la verdad** | interacción que define desproporcionadamente la percepción de toda la relación | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **brecha de expectativa** | diferencia entre lo que el cliente esperaba y lo que efectivamente recibió | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir las etapas desde la perspectiva del cliente → 2. documentar objetivo, información buscada y fricción por etapa → 3. identificar los momentos de la verdad → 4. medir esfuerzo o abandono en cada uno → 5. priorizar intervenciones por costo y efecto
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** El journey promedio puede no existir: si el mapa mezcla segmentos con recorridos distintos, producirá intervenciones que no sirven a ninguno.

## 📖 Desarrollo

### 1. Etapa del journey: mecanismo central

**Etapa del journey** se entiende aquí como **momento definido por el objetivo del cliente y no por el canal que la empresa usa**.

El journey no es el proceso interno de la empresa dibujado desde afuera. Es la secuencia de situaciones que atraviesa el cliente, incluidas las que ocurren fuera de todo contacto: cuando compara en silencio, cuando consulta a un colega, cuando pospone. Los mapas que sólo contienen interacciones con la empresa describen el CRM y no la experiencia, y por eso nunca explican dónde se pierden las oportunidades.

**De dónde viene esta afirmación.** Matthew Dixon, Nick Toman y Rick DeLisi — *The Effortless Experience* (2013) aporta la idea que sostiene este bloque: el traslado forzado de canal como fuente principal de esfuerzo percibido. Búscala en los capítulos sobre experiencia de canal. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «esfuerzo percibido por etapa» debería moverse cuando cambie **etapa del journey**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **punto de dolor**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Punto de dolor: frontera conceptual y error de clasificación

**Definición operacional:** fricción concreta que aumenta esfuerzo, riesgo o tiempo del cliente en una etapa. Su valor está en distinguirlo de **etapa del journey**.

Un punto de dolor no es cualquier molestia: es un momento donde el cliente considera abandonar o cambiar. El momento de la verdad, en cambio, es aquel donde se forma el juicio duradero sobre la relación, y suele ser un episodio de falla resuelto bien o mal. Distinguirlos evita repartir presupuesto de mejora de forma pareja sobre todo el recorrido en lugar de concentrarlo donde se decide la permanencia.

**Contraste bibliográfico.** Steve Krug — *Don't Make Me Think, Revisited* (2014) aporta aquí una distinción concreta: las personas escanean, no leen: satisfacen en lugar de optimizar (el capítulo sobre cómo usamos realmente la web). Formula dos mini-casos: uno que satisface la definición de **punto de dolor** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «documentar objetivo, información buscada y fricción por etapa», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Momento de la verdad: operacionalización y medición

**Momento de la verdad** significa **interacción que define desproporcionadamente la percepción de toda la relación**.

La brecha de expectativa se mide comparando lo prometido con lo entregado en la misma unidad. Si la promesa comercial dice «implementación en dos semanas», la medición registra el tiempo real hasta el primer uso productivo, por cohorte de venta y con la mediana además del promedio. Esa comparación suele revelar que el problema de experiencia se originó en la conversación de venta y no en la operación.

Ficha de medición obligatoria para **esfuerzo percibido por etapa**: `puntuación de esfuerzo declarada por el cliente al completar la etapa, escala uniforme y muestra mínima definida`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Michael R. Solomon — *Consumer Behavior: Buying, Having, and Being* (2019, 13.ª ed.) pone una condición sobre la medición: el proceso de decisión del consumidor y sus etapas observables (la parte sobre toma de decisiones del consumidor). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Brecha de expectativa: trade-offs y efectos de segundo orden

**Definición:** diferencia entre lo que el cliente esperaba y lo que efectivamente recibió.

Mapear el journey completo con evidencia es caro; hacerlo en un taller de dos horas es barato y produce el mapa que el equipo ya tenía en la cabeza. El intercambio real es entre costo y validez. Lo aceptable es hacer el taller y marcar explícitamente qué tramos están basados en datos, cuáles en conversaciones y cuáles en suposición, para que la inversión posterior se dirija a los últimos.

**Lo que aporta la fuente.** Philip Kotler, Kevin Lane Keller y Alexander Chernev — *Marketing Management* (2021, 16.ª ed.) aporta el criterio para pesar el intercambio: el canal como sistema que cumple funciones de información, transacción y servicio (los capítulos sobre diseño y gestión de canales de marketing). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **brecha de expectativa en onboarding** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **brecha de expectativa** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «priorizar intervenciones por costo y efecto», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El journey es un promedio y ningún cliente lo recorre exactamente. Su utilidad está en priorizar intervenciones, no en predecir la conducta de una cuenta. Cuando un mapa se empieza a usar para justificar decisiones sobre casos individuales, ha dejado de ser una herramienta de diseño y se ha convertido en una regla que nadie verificó.

**Frontera declarada.** El journey promedio puede no existir: si el mapa mezcla segmentos con recorridos distintos, producirá intervenciones que no sirven a ninguno. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Construir personas ficticias sin datos y usarlas para justificar decisiones caras.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar customer journey no consiste en sumar definiciones. Empieza por **etapa del journey**, contrasta **punto de dolor** con **momento de la verdad**, incorpora **brecha de expectativa** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Matthew Dixon, Nick Toman y Rick DeLisi — *The Effortless Experience* (2013) | El traslado forzado de canal como fuente principal de esfuerzo percibido | Los capítulos sobre experiencia de canal | ¿Qué debería observarse en **etapa del journey** si aquí opera «el traslado forzado de canal como fuente principal de esfuerzo percibido»? ¿Y qué observación lo desmentiría en este caso? |
| Steve Krug — *Don't Make Me Think, Revisited* (2014) | Las personas escanean, no leen: satisfacen en lugar de optimizar | El capítulo sobre cómo usamos realmente la web | ¿Qué debería observarse en **punto de dolor** si aquí opera «las personas escanean, no leen: satisfacen en lugar de optimizar»? ¿Y qué observación lo desmentiría en este caso? |
| Michael R. Solomon — *Consumer Behavior: Buying, Having, and Being* (2019, 13.ª ed.) | El proceso de decisión del consumidor y sus etapas observables | La parte sobre toma de decisiones del consumidor | ¿Qué debería observarse en **momento de la verdad** si aquí opera «el proceso de decisión del consumidor y sus etapas observables»? ¿Y qué observación lo desmentiría en este caso? |
| Philip Kotler, Kevin Lane Keller y Alexander Chernev — *Marketing Management* (2021, 16.ª ed.) | El canal como sistema que cumple funciones de información, transacción y servicio | Los capítulos sobre diseño y gestión de canales de marketing | ¿Qué debería observarse en **brecha de expectativa** si aquí opera «el canal como sistema que cumple funciones de información, transacción y servicio»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El journey documentado de Ruta Andina tiene cinco etapas y todas describen acciones internas: «enviar propuesta», «agendar demo». Ninguna describe qué intenta lograr el cliente.

**Paso 1 — Definir las etapas desde la perspectiva del cliente.** El equipo escribe primero el supuesto asociado a **etapa del journey** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **esfuerzo percibido por etapa** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Documentar objetivo, información buscada y fricción por etapa.** El trabajo aquí es separar lo observado de lo inferido sobre **punto de dolor**. La evidencia que ordena la discusión es **abandono por etapa**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Identificar los momentos de la verdad.** El riesgo de este paso es cerrar demasiado rápido alrededor de **momento de la verdad**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **brecha de expectativa en onboarding** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Medir esfuerzo o abandono en cada uno.** Con **brecha de expectativa** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **esfuerzo percibido por etapa** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Priorizar intervenciones por costo y efecto.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **etapa del journey**. **abandono por etapa** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **etapa del journey** | Momento definido por el objetivo del cliente y no por el canal que la empresa usa | Cuando **esfuerzo percibido por etapa** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **punto de dolor** | Fricción concreta que aumenta esfuerzo, riesgo o tiempo del cliente en una etapa | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** El journey promedio puede no existir: si el mapa mezcla segmentos con recorridos distintos, producirá intervenciones que no sirven a ninguno.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre customer journey |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing manager, Product marketing y Ejecutivo comercial. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El journey documentado de Ruta Andina tiene cinco etapas y todas describen acciones internas: «enviar propuesta», «agendar demo». Ninguna describe qué intenta lograr el cliente.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir las etapas desde la perspectiva del cliente → documentar objetivo, información buscada y fricción por etapa → identificar los momentos de la verdad → medir esfuerzo o abandono en cada uno → priorizar intervenciones por costo y efecto** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **esfuerzo percibido por etapa**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *The Effortless Experience* y la de *Don't Make Me Think, Revisited*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **etapa del journey** y **punto de dolor** como sinónimos | Se perdió la distinción entre «momento definido por el objetivo del cliente y no por el canal que la empresa usa» y «fricción concreta que aumenta esfuerzo, riesgo o tiempo del cliente en una etapa» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «priorizar intervenciones por costo y efecto» | Se saltó «definir las etapas desde la perspectiva del cliente»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **esfuerzo percibido por etapa** | La métrica local reemplazó al resultado del sistema | Contrástala con **brecha de expectativa en onboarding** y explicita el costo de oportunidad. |
| Mapear el proceso interno y llamarlo journey | Error específico de esta clase | Reescribe cada etapa empezando por el verbo del cliente, no por el de la empresa. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **etapa del journey** y **punto de dolor** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **momento de la verdad** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir las etapas desde la perspectiva del cliente» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **esfuerzo percibido por etapa** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «El journey promedio puede no existir: si el mapa mezcla segmentos con recorridos distintos, producirá intervenciones que no sirven a ninguno»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **momento de la verdad** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **esfuerzo percibido por etapa**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *The Effortless Experience* y *Marketing Management*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Construir personas ficticias sin datos y usarlas para justificar decisiones caras.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P02-C07-customer-journey/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **esfuerzo percibido por etapa**, **abandono por etapa** y **brecha de expectativa en onboarding** con fuente, ventana y lectura prohibida.
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

- Matthew Dixon, Nick Toman y Rick DeLisi — *The Effortless Experience* (2013) — **aporta a esta clase:** el traslado forzado de canal como fuente principal de esfuerzo percibido. **Dónde buscarlo:** los capítulos sobre experiencia de canal. Registra edición y páginas consultadas en tu nota de lectura.
- Steve Krug — *Don't Make Me Think, Revisited* (2014) — **aporta a esta clase:** las personas escanean, no leen: satisfacen en lugar de optimizar. **Dónde buscarlo:** el capítulo sobre cómo usamos realmente la web. Registra edición y páginas consultadas en tu nota de lectura.
- Michael R. Solomon — *Consumer Behavior: Buying, Having, and Being* (2019, 13.ª ed.) — **aporta a esta clase:** el proceso de decisión del consumidor y sus etapas observables. **Dónde buscarlo:** la parte sobre toma de decisiones del consumidor. Registra edición y páginas consultadas en tu nota de lectura.
- Philip Kotler, Kevin Lane Keller y Alexander Chernev — *Marketing Management* (2021, 16.ª ed.) — **aporta a esta clase:** el canal como sistema que cumple funciones de información, transacción y servicio. **Dónde buscarlo:** los capítulos sobre diseño y gestión de canales de marketing. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 06 · Unidad de decisión en B2B](class-06-unidad-de-decision-en-b2b.md) · [Índice de la parte](README.md) · [Clase 08 · Motivaciones y fricciones](class-08-motivaciones-y-fricciones.md) →
