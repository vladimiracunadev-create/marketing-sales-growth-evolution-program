---
title: "Modelos de atribución"
type: class
language: es
standard: clase-profunda-v2
part: 20
class: 08
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["kaushik", "kohavi", "provost", "binet-field"]
anchors: {"binet-field": "corto-largo", "kaushik": "plan-medicion", "kohavi": "confianza", "provost": "asociacion-causalidad"}
updated: 2026-08-19
---

# Clase 20.08 — Modelos de atribución

Clase 8 de 14 de la parte [20 — Analítica comercial y marketing science](README.md), de nivel Crecimiento y analítica. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 20.07, *Análisis de cohortes aplicado*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de variación de crédito entre modelos con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El plan de medición que va de la decisión a la métrica y no al revés — Avinash Kaushik. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Los modelos de atribución reparten el crédito entre puntos de contacto según una regla convencional. Ninguno mide causalidad: describen correlación con una convención declarada. Su uso correcto es comparativo —ver cómo cambia la lectura según el modelo— y su uso incorrecto es tratarlos como verdad para asignar presupuesto sin verificación causal.

El punto de partida de esta clase no es la definición sino la decisión que la definición debe mejorar. La parte 20 busca **sostener decisiones de ingreso con métricas correctamente construidas**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **modelos de atribución** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Esta cifra mide lo que creo que mide, y qué decisión cambiaría si estuviera equivocada?

Los conceptos que estructuran la sesión son **modelo basado en reglas**, **modelo basado en datos**, **ventana de contacto** y **límite causal**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `modelo basado en reglas`, `modelo basado en datos`, `ventana de contacto` y `límite causal` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Analítica comercial y marketing science**.
3. **Aplicar** la secuencia **declarar el modelo y la ventana utilizados → comparar la lectura bajo al menos dos modelos → identificar los canales cuyo crédito varía más → diseñar verificación causal para los casos críticos → publicar las limitaciones junto con los resultados** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **variación de crédito entre modelos**, **cobertura de recorridos completos** y **decisiones respaldadas por verificación causal** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **modelo basado en reglas** y **modelo basado en datos** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **variación de crédito entre modelos**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **modelo basado en reglas** | convención fija que reparte el crédito según posición o decaimiento | Construye un caso límite donde el concepto se confunde con el anterior. |
| **modelo basado en datos** | asignación derivada del análisis de recorridos observados | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **ventana de contacto** | periodo dentro del cual se consideran los puntos de contacto | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **límite causal** | imposibilidad de establecer causalidad con datos observacionales de atribución | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. declarar el modelo y la ventana utilizados → 2. comparar la lectura bajo al menos dos modelos → 3. identificar los canales cuyo crédito varía más → 4. diseñar verificación causal para los casos críticos → 5. publicar las limitaciones junto con los resultados
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** La reducción de cobertura de rastreo por privacidad afecta a todos los modelos. Los recorridos incompletos sesgan sistemáticamente hacia los canales de último contacto.

## 📖 Desarrollo

### 1. Modelo basado en reglas: mecanismo central

**Modelo basado en reglas** se entiende aquí como **convención fija que reparte el crédito según posición o decaimiento**.

Los modelos de atribución reparten el crédito de una conversión entre los contactos que la precedieron. Ninguno es verdadero: son convenciones con supuestos distintos. Elegir uno es aceptar un sesgo determinado, y lo profesional es declararlo en lugar de presentar el resultado como un hecho.

**De dónde viene esta afirmación.** Avinash Kaushik — *Web Analytics 2.0* (2009) aporta la idea que sostiene este bloque: el plan de medición que va de la decisión a la métrica y no al revés. Búscala en los capítulos sobre estrategia de medición. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «variación de crédito entre modelos» debería moverse cuando cambie **modelo basado en reglas**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **modelo basado en datos**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Modelo basado en datos: frontera conceptual y error de clasificación

**Definición operacional:** asignación derivada del análisis de recorridos observados. Su valor está en distinguirlo de **modelo basado en reglas**.

Los modelos basados en reglas —último clic, primero, lineal, con decaimiento— son transparentes y arbitrarios. Los basados en datos son menos arbitrarios y opacos, y requieren volumen suficiente para entrenarse. La elección debe considerar quién usará el resultado: un modelo que nadie puede explicar no sostiene una decisión de presupuesto.

**Contraste bibliográfico.** Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) aporta aquí una distinción concreta: las condiciones que hacen confiable un experimento en línea (los capítulos sobre experimentos confiables). Formula dos mini-casos: uno que satisface la definición de **modelo basado en datos** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «comparar la lectura bajo al menos dos modelos», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Ventana de contacto: operacionalización y medición

**Ventana de contacto** significa **periodo dentro del cual se consideran los puntos de contacto**.

La ventana de contacto define qué interacciones se consideran parte del recorrido. Una ventana corta en un ciclo largo excluye los contactos iniciales y sobreatribuye al cierre. Ajustarla al ciclo observado es un cambio simple que suele modificar sustancialmente la imagen de contribución de los canales.

Ficha de medición obligatoria para **variación de crédito entre modelos**: `diferencia del crédito asignado a cada canal según modelo`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) pone una condición sobre la medición: la distinción entre correlación observada y causalidad y qué exige cada una (los capítulos sobre inferencia y sesgo). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Límite causal: trade-offs y efectos de segundo orden

**Definición:** imposibilidad de establecer causalidad con datos observacionales de atribución.

Modelos más sofisticados reparten mejor y consumen tiempo de implementación y mantenimiento, además de exigir datos de calidad. En operaciones con volúmenes moderados, la sofisticación no compensa: es preferible un modelo simple con la ventana correcta y una prueba de incrementalidad para las decisiones grandes.

**Lo que aporta la fuente.** Les Binet y Peter Field — *The Long and the Short of It* (2013) aporta el criterio para pesar el intercambio: los efectos de corto plazo decaen; los de marca se acumulan y bajan la elasticidad de precio (los capítulos sobre curvas de respuesta en el tiempo). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **decisiones respaldadas por verificación causal** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **límite causal** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «publicar las limitaciones junto con los resultados», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La atribución mide asociación temporal y no causa. Ningún modelo responde qué habría pasado sin esa inversión, que es la pregunta de gestión. Cuando la decisión es significativa, la atribución debe complementarse con un diseño experimental, y ese límite hay que declararlo cada vez que se presenta un informe de atribución.

**Frontera declarada.** La reducción de cobertura de rastreo por privacidad afecta a todos los modelos. Los recorridos incompletos sesgan sistemáticamente hacia los canales de último contacto. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar modelos de atribución no consiste en sumar definiciones. Empieza por **modelo basado en reglas**, contrasta **modelo basado en datos** con **ventana de contacto**, incorpora **límite causal** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Avinash Kaushik — *Web Analytics 2.0* (2009) | El plan de medición que va de la decisión a la métrica y no al revés | Los capítulos sobre estrategia de medición | ¿Qué debería observarse en **modelo basado en reglas** si aquí opera «el plan de medición que va de la decisión a la métrica y no al revés»? ¿Y qué observación lo desmentiría en este caso? |
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | Las condiciones que hacen confiable un experimento en línea | Los capítulos sobre experimentos confiables | ¿Qué debería observarse en **modelo basado en datos** si aquí opera «las condiciones que hacen confiable un experimento en línea»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La distinción entre correlación observada y causalidad y qué exige cada una | Los capítulos sobre inferencia y sesgo | ¿Qué debería observarse en **ventana de contacto** si aquí opera «la distinción entre correlación observada y causalidad y qué exige cada una»? ¿Y qué observación lo desmentiría en este caso? |
| Les Binet y Peter Field — *The Long and the Short of It* (2013) | Los efectos de corto plazo decaen; los de marca se acumulan y bajan la elasticidad de precio | Los capítulos sobre curvas de respuesta en el tiempo | ¿Qué debería observarse en **límite causal** si aquí opera «los efectos de corto plazo decaen; los de marca se acumulan y bajan la elasticidad de precio»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Bajo último clic, la búsqueda de marca de Ruta Andina recibe 61 % del crédito; bajo un modelo lineal, 28 %. El presupuesto se asigna con el primero sin discusión.

**Paso 1 — Declarar el modelo y la ventana utilizados.** El equipo escribe primero el supuesto asociado a **modelo basado en reglas** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **variación de crédito entre modelos** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Comparar la lectura bajo al menos dos modelos.** El trabajo aquí es separar lo observado de lo inferido sobre **modelo basado en datos**. La evidencia que ordena la discusión es **cobertura de recorridos completos**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Identificar los canales cuyo crédito varía más.** El riesgo de este paso es cerrar demasiado rápido alrededor de **ventana de contacto**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **decisiones respaldadas por verificación causal** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Diseñar verificación causal para los casos críticos.** Con **límite causal** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **variación de crédito entre modelos** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Publicar las limitaciones junto con los resultados.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **modelo basado en reglas**. **cobertura de recorridos completos** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **modelo basado en reglas** | Convención fija que reparte el crédito según posición o decaimiento | Cuando **variación de crédito entre modelos** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **modelo basado en datos** | Asignación derivada del análisis de recorridos observados | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** La reducción de cobertura de rastreo por privacidad afecta a todos los modelos. Los recorridos incompletos sesgan sistemáticamente hacia los canales de último contacto.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre modelos de atribución |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing analyst, Revenue analyst y Data-driven marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Bajo último clic, la búsqueda de marca de Ruta Andina recibe 61 % del crédito; bajo un modelo lineal, 28 %. El presupuesto se asigna con el primero sin discusión.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **declarar el modelo y la ventana utilizados → comparar la lectura bajo al menos dos modelos → identificar los canales cuyo crédito varía más → diseñar verificación causal para los casos críticos → publicar las limitaciones junto con los resultados** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **variación de crédito entre modelos**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Web Analytics 2.0* y la de *Trustworthy Online Controlled Experiments*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **modelo basado en reglas** y **modelo basado en datos** como sinónimos | Se perdió la distinción entre «convención fija que reparte el crédito según posición o decaimiento» y «asignación derivada del análisis de recorridos observados» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «publicar las limitaciones junto con los resultados» | Se saltó «declarar el modelo y la ventana utilizados»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **variación de crédito entre modelos** | La métrica local reemplazó al resultado del sistema | Contrástala con **decisiones respaldadas por verificación causal** y explicita el costo de oportunidad. |
| Tratar la atribución como evidencia causal | Error específico de esta clase | Compara modelos y valida con experimentos los canales donde la decisión es costosa. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **modelo basado en reglas** y **modelo basado en datos** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **ventana de contacto** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «declarar el modelo y la ventana utilizados» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **variación de crédito entre modelos** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «La reducción de cobertura de rastreo por privacidad afecta a todos los modelos. Los recorridos incompletos sesgan sistemáticamente hacia los canales de último contacto»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **ventana de contacto** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **variación de crédito entre modelos**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Web Analytics 2.0* y *The Long and the Short of It*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, comprueba la norma en su texto vigente. Los enlaces van al texto completo publicado por la Biblioteca del Congreso Nacional; son gratuitos y no hace falta creerle a este material.

- **Consumo y comercio.** [Ley 19.496](https://www.bcn.cl/leychile/navegar?idNorma=61438) — *Establece normas sobre protección de los derechos de los consumidores* (Ministerio de Economía, Fomento y Reconstrucción), y su reglamento de comercio electrónico, [Decreto 6/2021](https://www.bcn.cl/leychile/navegar?idNorma=1165504) — *Aprueba reglamento de comercio electrónico* (Ministerio de Economía, Fomento y Turismo).
- **Datos personales.** [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales* (Ministerio Secretaría General de la Presidencia), que sustituye progresivamente a [Ley 19.628](https://www.bcn.cl/leychile/navegar?idNorma=141599) — *Sobre protección de la vida privada* (Ministerio Secretaría General de la Presidencia).
- **Derecho a retracto.** [Decreto 52/2024](https://www.bcn.cl/leychile/navegar?idNorma=1206144) — *Aprueba reglamento que regula la forma y condiciones en que los proveedores deberán comunicar la exclusión del derecho a retracto y los bienes en que excepcionalmente y por su naturaleza procederá tal exclusión* (Ministerio de Economía, Fomento y Turismo).

Dentro del repositorio, el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) ordena qué norma aplica a cada decisión comercial, [datos personales y ética](../../docs/DATOS-PERSONALES-Y-ETICA.md) desarrolla el tratamiento de datos y [fuentes oficiales](../../docs/FUENTES-OFICIALES.md) lista los organismos con su fecha de consulta. Ninguno de esos documentos reemplaza al texto legal.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P20-C08-attribution-models/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **variación de crédito entre modelos**, **cobertura de recorridos completos** y **decisiones respaldadas por verificación causal** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **caso analítico integral con árbol de métricas, cohortes, incrementalidad y dashboard ejecutivo**.

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

- Avinash Kaushik — [*Web Analytics 2.0*](https://openlibrary.org/isbn/9780470596425) (2009) · ISBN 9780470596425 — **aporta a esta clase:** el plan de medición que va de la decisión a la métrica y no al revés. **Dónde buscarlo:** los capítulos sobre estrategia de medición. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Ron Kohavi, Diane Tang y Ya Xu — [*Trustworthy Online Controlled Experiments*](https://openlibrary.org/isbn/9781108601375) (2020) · ISBN 9781108601375 — **aporta a esta clase:** las condiciones que hacen confiable un experimento en línea. **Dónde buscarlo:** los capítulos sobre experimentos confiables. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) · ISBN 9781449374280 — **aporta a esta clase:** la distinción entre correlación observada y causalidad y qué exige cada una. **Dónde buscarlo:** los capítulos sobre inferencia y sesgo. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Les Binet y Peter Field — [*The Long and the Short of It*](https://openlibrary.org/isbn/9780852941348) (2013) · ISBN 9780852941348 — **aporta a esta clase:** los efectos de corto plazo decaen; los de marca se acumulan y bajan la elasticidad de precio. **Dónde buscarlo:** los capítulos sobre curvas de respuesta en el tiempo. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 07 · Análisis de cohortes aplicado](class-07-cohort-analysis.md) · [Índice de la parte](README.md) · [Clase 09 · Incrementalidad](class-09-incrementalidad.md) →
