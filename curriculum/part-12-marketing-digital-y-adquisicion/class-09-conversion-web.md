---
title: "Conversión web"
type: class
language: es
standard: clase-profunda-v2
part: 12
class: 09
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["laja", "kohavi", "eisenberg", "krug"]
anchors: {"eisenberg": "hipotesis-cro", "kohavi": "detencion-temprana", "krug": "prueba-usabilidad", "laja": "investigacion-previa"}
updated: 2026-08-19
---

# Clase 12.09 — Conversión web

**Parte 12 · Marketing digital y adquisición** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 12.08 — *Community marketing*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de tasa de conversión por paso para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La investigación previa al test: sin diagnóstico, el experimento es una apuesta — Peep Laja y el equipo de CXL. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La optimización de conversión seria empieza con investigación, no con tests: analítica para saber dónde se pierde, grabaciones y encuestas para saber por qué, y sólo entonces hipótesis y experimentos. Laja insiste en que la mayoría de los tests fracasan por falta de investigación previa y por muestras insuficientes que producen conclusiones falsas.

Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales. La parte 12 busca **operar un sistema digital de adquisición medible de punta a punta**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **conversión web** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué activo digital genera demanda propia y qué parte del resultado es alquilada?

Los conceptos que estructuran la sesión son **investigación previa**, **hipótesis de conversión**, **potencia estadística** y **falso positivo**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `investigación previa`, `hipótesis de conversión`, `potencia estadística` y `falso positivo` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Marketing digital y adquisición**.
3. **Aplicar** la secuencia **identificar la mayor pérdida con analítica → investigar la causa con evidencia cualitativa → formular la hipótesis con mecanismo explícito → calcular muestra y duración antes de iniciar → validar el resultado antes de implementarlo de forma permanente** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **tasa de conversión por paso**, **potencia del test** y **tasa de replicación** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **investigación previa** y **hipótesis de conversión** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **tasa de conversión por paso**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **investigación previa** | análisis cuantitativo y cualitativo que precede a la formulación de hipótesis | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **hipótesis de conversión** | afirmación sobre qué cambio producirá qué efecto y por qué | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **potencia estadística** | capacidad del test de detectar el efecto mínimo relevante con la muestra disponible | Da un hecho compatible con la definición y otro que la refute. |
| **falso positivo** | conclusión de mejora que no se sostiene al repetir la medición | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. identificar la mayor pérdida con analítica → 2. investigar la causa con evidencia cualitativa → 3. formular la hipótesis con mecanismo explícito → 4. calcular muestra y duración antes de iniciar → 5. validar el resultado antes de implementarlo de forma permanente
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** En sitios con poco tráfico los tests A/B rara vez alcanzan potencia suficiente. La alternativa correcta es investigación cualitativa y cambios fundamentados, no tests sin potencia.

## 📖 Desarrollo

### 1. Investigación previa: mecanismo central

**Investigación previa** se entiende aquí como **análisis cuantitativo y cualitativo que precede a la formulación de hipótesis**.

Optimizar la conversión empieza por investigar y no por probar. Peep Laja lo plantea con claridad: sin diagnóstico previo, un experimento es una apuesta con vestimenta científica. La investigación combina datos de comportamiento, revisión de usabilidad, encuestas breves y análisis de las objeciones que ya conoce el equipo comercial.

**De dónde viene esta afirmación.** Peep Laja y el equipo de CXL — *Conversion Optimization Playbooks (CXL)* (2024) aporta la idea que sostiene este bloque: la investigación previa al test: sin diagnóstico, el experimento es una apuesta. Búscala en el método de investigación de conversión. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «tasa de conversión por paso» debería moverse cuando cambie **investigación previa**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **hipótesis de conversión**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Hipótesis de conversión: frontera conceptual y error de clasificación

**Definición operacional:** afirmación sobre qué cambio producirá qué efecto y por qué. Su valor está en distinguirlo de **investigación previa**.

La hipótesis de conversión debe nombrar el mecanismo y no sólo el cambio: no «cambiar el botón a verde», sino «la duda sobre el compromiso frena la acción; explicitar que no requiere tarjeta debería aumentar los envíos». La segunda formulación es refutable y, gane o pierda, enseña algo transferible.

**Contraste bibliográfico.** Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) aporta aquí una distinción concreta: la detención temprana y el espionaje de resultados como fuente de falsos positivos (los capítulos sobre errores comunes). Formula dos mini-casos: uno que satisface la definición de **hipótesis de conversión** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «investigar la causa con evidencia cualitativa», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Potencia estadística: operacionalización y medición

**Potencia estadística** significa **capacidad del test de detectar el efecto mínimo relevante con la muestra disponible**.

La potencia estadística determina si el experimento podrá detectar el efecto que interesa. Con tráfico bajo, buscar mejoras de dos puntos es imposible y el resultado será ruido interpretado como señal. El cálculo del tamaño necesario se hace antes de lanzar y, si el tráfico no alcanza, la decisión correcta es probar cambios grandes o no probar.

Ficha de medición obligatoria para **tasa de conversión por paso**: `avances, sobre entradas al paso, en el recorrido de conversión`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Bryan Eisenberg y Jeffrey Eisenberg — *Call to Action* (2005) pone una condición sobre la medición: la hipótesis explícita antes del test y su relación con la persuasión (los capítulos sobre proceso de optimización). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Falso positivo: trade-offs y efectos de segundo orden

**Definición:** conclusión de mejora que no se sostiene al repetir la medición.

Probar muchas variantes acelera la exploración y aumenta la probabilidad de falsos positivos por comparaciones múltiples. Probar pocas y grandes reduce ese riesgo y explora menos. En sitios con tráfico moderado —la mayoría en mercados como el chileno— la segunda opción es casi siempre la correcta.

**Lo que aporta la fuente.** Steve Krug — *Don't Make Me Think, Revisited* (2014) aporta el criterio para pesar el intercambio: la prueba de usabilidad barata con pocos usuarios como práctica regular (los capítulos sobre pruebas de usabilidad). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **tasa de replicación** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **falso positivo** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «validar el resultado antes de implementarlo de forma permanente», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Un resultado positivo no replicado es una hipótesis, no un hallazgo. La proporción de resultados que no se sostienen al repetirse es alta, y las organizaciones que documentan sólo los éxitos construyen un catálogo de creencias falsas. Registrar todos los experimentos, incluidos los nulos, es lo que hace que el programa acumule conocimiento.

**Frontera declarada.** En sitios con poco tráfico los tests A/B rara vez alcanzan potencia suficiente. La alternativa correcta es investigación cualitativa y cambios fundamentados, no tests sin potencia. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Optimizar métricas de vanidad y desatender consentimiento, cookies y datos personales.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar conversión web no consiste en sumar definiciones. Empieza por **investigación previa**, contrasta **hipótesis de conversión** con **potencia estadística**, incorpora **falso positivo** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Peep Laja y el equipo de CXL — *Conversion Optimization Playbooks (CXL)* (2024) | La investigación previa al test: sin diagnóstico, el experimento es una apuesta | El método de investigación de conversión | ¿Qué debería observarse en **investigación previa** si aquí opera «la investigación previa al test: sin diagnóstico, el experimento es una apuesta»? ¿Y qué observación lo desmentiría en este caso? |
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | La detención temprana y el espionaje de resultados como fuente de falsos positivos | Los capítulos sobre errores comunes | ¿Qué debería observarse en **hipótesis de conversión** si aquí opera «la detención temprana y el espionaje de resultados como fuente de falsos positivos»? ¿Y qué observación lo desmentiría en este caso? |
| Bryan Eisenberg y Jeffrey Eisenberg — *Call to Action* (2005) | La hipótesis explícita antes del test y su relación con la persuasión | Los capítulos sobre proceso de optimización | ¿Qué debería observarse en **potencia estadística** si aquí opera «la hipótesis explícita antes del test y su relación con la persuasión»? ¿Y qué observación lo desmentiría en este caso? |
| Steve Krug — *Don't Make Me Think, Revisited* (2014) | La prueba de usabilidad barata con pocos usuarios como práctica regular | Los capítulos sobre pruebas de usabilidad | ¿Qué debería observarse en **falso positivo** si aquí opera «la prueba de usabilidad barata con pocos usuarios como práctica regular»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina cambió el color del botón y declaró 18 % de mejora con 120 visitantes por variante durante cuatro días. Al mes siguiente la conversión volvió al nivel anterior.

**Paso 1 — Identificar la mayor pérdida con analítica.** El equipo escribe primero el supuesto asociado a **investigación previa** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **tasa de conversión por paso** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Investigar la causa con evidencia cualitativa.** El trabajo aquí es separar lo observado de lo inferido sobre **hipótesis de conversión**. La evidencia que ordena la discusión es **potencia del test**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Formular la hipótesis con mecanismo explícito.** El riesgo de este paso es cerrar demasiado rápido alrededor de **potencia estadística**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **tasa de replicación** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Calcular muestra y duración antes de iniciar.** Con **falso positivo** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **tasa de conversión por paso** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Validar el resultado antes de implementarlo de forma permanente.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **investigación previa**. **potencia del test** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **investigación previa** | Análisis cuantitativo y cualitativo que precede a la formulación de hipótesis | Cuando **tasa de conversión por paso** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **hipótesis de conversión** | Afirmación sobre qué cambio producirá qué efecto y por qué | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** En sitios con poco tráfico los tests A/B rara vez alcanzan potencia suficiente. La alternativa correcta es investigación cualitativa y cambios fundamentados, no tests sin potencia.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre conversión web |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Digital marketing manager, Growth marketer y Especialista SEO/SEM. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina cambió el color del botón y declaró 18 % de mejora con 120 visitantes por variante durante cuatro días. Al mes siguiente la conversión volvió al nivel anterior.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **identificar la mayor pérdida con analítica → investigar la causa con evidencia cualitativa → formular la hipótesis con mecanismo explícito → calcular muestra y duración antes de iniciar → validar el resultado antes de implementarlo de forma permanente** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **tasa de conversión por paso**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Conversion Optimization Playbooks (CXL)* y la de *Trustworthy Online Controlled Experiments*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **investigación previa** y **hipótesis de conversión** como sinónimos | Se perdió la distinción entre «análisis cuantitativo y cualitativo que precede a la formulación de hipótesis» y «afirmación sobre qué cambio producirá qué efecto y por qué» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «validar el resultado antes de implementarlo de forma permanente» | Se saltó «identificar la mayor pérdida con analítica»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **tasa de conversión por paso** | La métrica local reemplazó al resultado del sistema | Contrástala con **tasa de replicación** y explicita el costo de oportunidad. |
| Testear sin calcular muestra ni duración | Error específico de esta clase | Calcula el tamaño necesario antes de iniciar; si el tráfico no alcanza, decide con investigación cualitativa. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **investigación previa** y **hipótesis de conversión** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **potencia estadística** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «identificar la mayor pérdida con analítica» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **tasa de conversión por paso** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «En sitios con poco tráfico los tests A/B rara vez alcanzan potencia suficiente. La alternativa correcta es investigación cualitativa y cambios fundamentados, no tests sin potencia»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **potencia estadística** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **tasa de conversión por paso**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Conversion Optimization Playbooks (CXL)* y *Don't Make Me Think, Revisited*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Optimizar métricas de vanidad y desatender consentimiento, cookies y datos personales.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P12-C09-conversion-web/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **tasa de conversión por paso**, **potencia del test** y **tasa de replicación** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **plan de adquisición digital con arquitectura de sitio, canales, medición y auditoría inicial**.

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

- Peep Laja y el equipo de CXL — *Conversion Optimization Playbooks (CXL)* (2024) — **aporta a esta clase:** la investigación previa al test: sin diagnóstico, el experimento es una apuesta. **Dónde buscarlo:** el método de investigación de conversión. Registra edición y páginas consultadas en tu nota de lectura.
- Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) — **aporta a esta clase:** la detención temprana y el espionaje de resultados como fuente de falsos positivos. **Dónde buscarlo:** los capítulos sobre errores comunes. Registra edición y páginas consultadas en tu nota de lectura.
- Bryan Eisenberg y Jeffrey Eisenberg — *Call to Action* (2005) — **aporta a esta clase:** la hipótesis explícita antes del test y su relación con la persuasión. **Dónde buscarlo:** los capítulos sobre proceso de optimización. Registra edición y páginas consultadas en tu nota de lectura.
- Steve Krug — *Don't Make Me Think, Revisited* (2014) — **aporta a esta clase:** la prueba de usabilidad barata con pocos usuarios como práctica regular. **Dónde buscarlo:** los capítulos sobre pruebas de usabilidad. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 08 · Community marketing](class-08-community-marketing.md) · [Índice de la parte](README.md) · [Clase 10 · Analítica digital](class-10-analitica-digital.md) →
