---
title: "Suscripción e ingreso recurrente"
type: class
language: es
standard: clase-profunda-v2
part: 07
class: 09
level: Oferta comercial
mastery_threshold: 80
estimated_minutes: 150
sources: ["croll-yoskovitz", "mehta", "ramanujam", "fader-ltv"]
anchors: {"croll-yoskovitz": "modelos", "fader-ltv": "ltv-modelo", "mehta": "expansion", "ramanujam": "modelo-monetizacion"}
updated: 2026-08-19
---

# Clase 07.09 — Suscripción e ingreso recurrente

Clase 9 de 14 de la parte [07 — Pricing y monetización](README.md), de nivel Oferta comercial. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 07.08, *Versionado y price fences*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de ingreso recurrente mensual con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** Los seis modelos de negocio y las métricas que cambian entre ellos — Alistair Croll y Benjamin Yoskovitz. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La suscripción cambia la economía del negocio: el ingreso se reconoce en el tiempo, el costo de adquisición se recupera en meses y la retención pasa a ser la variable dominante. Ese modelo obliga a decisiones nuevas: métrica de cobro, ciclo de facturación, política de renovación y tratamiento de la baja. La renovación automática es legítima cuando se informa con claridad y permite cancelar sin fricción indebida.

Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales. La parte 07 busca **diseñar una arquitectura de precios que capture valor sin destruir demanda ni confianza**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **suscripción e ingreso recurrente** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Cuánto vale esto para quién, y qué estructura de cobro alinea precio con valor entregado?

Los conceptos que estructuran la sesión son **ingreso recurrente**, **periodo de recuperación**, **renovación automática** y **contracción**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `ingreso recurrente`, `periodo de recuperación`, `renovación automática` y `contracción` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Pricing y monetización**.
3. **Aplicar** la secuencia **elegir la métrica de cobro que sigue al valor → calcular el periodo de recuperación por segmento → definir la política de renovación y de cancelación → verificar el cumplimiento del deber de información → seguir expansión, contracción y baja por cohorte** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **ingreso recurrente mensual**, **periodo de recuperación** y **tasa de contracción** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **ingreso recurrente** y **periodo de recuperación** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **ingreso recurrente mensual**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **ingreso recurrente** | ingreso comprometido que se repite en periodos sucesivos bajo un contrato vigente | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **periodo de recuperación** | tiempo necesario para recuperar el costo de adquisición con el margen del cliente | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **renovación automática** | continuidad del contrato sin acción del cliente, sujeta a deber de información | Da un hecho compatible con la definición y otro que la refute. |
| **contracción** | reducción del ingreso de un cliente que permanece activo | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. elegir la métrica de cobro que sigue al valor → 2. calcular el periodo de recuperación por segmento → 3. definir la política de renovación y de cancelación → 4. verificar el cumplimiento del deber de información → 5. seguir expansión, contracción y baja por cohorte
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** La renovación automática exige información oportuna y un mecanismo de cancelación equivalente al de contratación. Dificultar la baja expone a sanción y destruye reputación.

## 📖 Desarrollo

### 1. Ingreso recurrente: mecanismo central

**Ingreso recurrente** se entiende aquí como **ingreso comprometido que se repite en periodos sucesivos bajo un contrato vigente**.

El ingreso recurrente cambia la economía del negocio: el valor de un cliente ya no está en la venta sino en la permanencia, y eso justifica invertir en adquisición más de lo que el primer pago recupera. La condición para que esa lógica funcione es que la permanencia sea real y medida, no supuesta por el modelo de contrato.

**De dónde viene esta afirmación.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) aporta la idea que sostiene este bloque: los seis modelos de negocio y las métricas que cambian entre ellos. Búscala en la parte sobre modelos de negocio. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «ingreso recurrente mensual» debería moverse cuando cambie **ingreso recurrente**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **periodo de recuperación**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Periodo de recuperación: frontera conceptual y error de clasificación

**Definición operacional:** tiempo necesario para recuperar el costo de adquisición con el margen del cliente. Su valor está en distinguirlo de **ingreso recurrente**.

El periodo de recuperación es el indicador que gobierna la velocidad de crecimiento sostenible: cuántos meses tarda el margen del cliente en cubrir lo que costó adquirirlo. Un periodo mayor que la permanencia media significa que cada cliente nuevo destruye valor, y ese diagnóstico —como en el caso de Ruta Andina— puede convivir con un crecimiento aparente de ingresos.

**Contraste bibliográfico.** Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) aporta aquí una distinción concreta: la expansión condicionada al resultado inicial acreditado (los capítulos sobre crecimiento en la base instalada). Formula dos mini-casos: uno que satisface la definición de **periodo de recuperación** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «calcular el periodo de recuperación por segmento», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Renovación automática: operacionalización y medición

**Renovación automática** significa **continuidad del contrato sin acción del cliente, sujeta a deber de información**.

La contracción es la reducción de ingreso de clientes que permanecen, y suele medirse mal o no medirse. Un negocio puede tener baja tasa de bajas y perder ingreso porque los clientes reducen su consumo. Por eso la medición correcta separa churn de clientes, churn de ingreso y contracción, y reporta las tres.

Ficha de medición obligatoria para **ingreso recurrente mensual**: `suma del ingreso comprometido de contratos vigentes, al cierre de cada mes`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) pone una condición sobre la medición: los modelos de monetización disponibles y el criterio para elegir la métrica de cobro (el capítulo sobre modelos de monetización). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Contracción: trade-offs y efectos de segundo orden

**Definición:** reducción del ingreso de un cliente que permanece activo.

La renovación automática mejora la retención declarada y traslada el costo de la decisión al cliente, que puede sentirse atrapado. En Chile, además, las condiciones de renovación automática están reguladas en relaciones de consumo. La decisión de usarla exige verificar el marco aplicable y diseñar un aviso previo genuino, no un cumplimiento formal.

**Lo que aporta la fuente.** Peter Fader y Sarah Toms — *The Customer Centricity Playbook* (2018) aporta el criterio para pesar el intercambio: el valor de vida como proyección con supuestos declarados y no como cifra única (los capítulos sobre cálculo del valor de vida). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **tasa de contracción** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **contracción** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «seguir expansión, contracción y baja por cohorte», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El modelo recurrente supone que el cliente obtiene valor de forma continua. Cuando el valor es episódico —se usa dos veces al año— el modelo genera resentimiento y bajas. En esos casos, un esquema por uso o por proyecto se alinea mejor con la percepción, aunque produzca ingresos menos predecibles.

**Frontera declarada.** La renovación automática exige información oportuna y un mecanismo de cancelación equivalente al de contratación. Dificultar la baja expone a sanción y destruye reputación. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar suscripción e ingreso recurrente no consiste en sumar definiciones. Empieza por **ingreso recurrente**, contrasta **periodo de recuperación** con **renovación automática**, incorpora **contracción** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | Los seis modelos de negocio y las métricas que cambian entre ellos | La parte sobre modelos de negocio | ¿Qué debería observarse en **ingreso recurrente** si aquí opera «los seis modelos de negocio y las métricas que cambian entre ellos»? ¿Y qué observación lo desmentiría en este caso? |
| Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) | La expansión condicionada al resultado inicial acreditado | Los capítulos sobre crecimiento en la base instalada | ¿Qué debería observarse en **periodo de recuperación** si aquí opera «la expansión condicionada al resultado inicial acreditado»? ¿Y qué observación lo desmentiría en este caso? |
| Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) | Los modelos de monetización disponibles y el criterio para elegir la métrica de cobro | El capítulo sobre modelos de monetización | ¿Qué debería observarse en **renovación automática** si aquí opera «los modelos de monetización disponibles y el criterio para elegir la métrica de cobro»? ¿Y qué observación lo desmentiría en este caso? |
| Peter Fader y Sarah Toms — *The Customer Centricity Playbook* (2018) | El valor de vida como proyección con supuestos declarados y no como cifra única | Los capítulos sobre cálculo del valor de vida | ¿Qué debería observarse en **contracción** si aquí opera «el valor de vida como proyección con supuestos declarados y no como cifra única»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina recupera su costo de adquisición en 14 meses y su churn mensual es 3,4 %: la vida media del cliente es menor que el periodo de recuperación.

**Paso 1 — Elegir la métrica de cobro que sigue al valor.** El equipo escribe primero el supuesto asociado a **ingreso recurrente** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **ingreso recurrente mensual** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Calcular el periodo de recuperación por segmento.** El trabajo aquí es separar lo observado de lo inferido sobre **periodo de recuperación**. La evidencia que ordena la discusión es **periodo de recuperación**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Definir la política de renovación y de cancelación.** El riesgo de este paso es cerrar demasiado rápido alrededor de **renovación automática**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **tasa de contracción** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Verificar el cumplimiento del deber de información.** Con **contracción** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **ingreso recurrente mensual** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Seguir expansión, contracción y baja por cohorte.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **ingreso recurrente**. **periodo de recuperación** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **ingreso recurrente** | Ingreso comprometido que se repite en periodos sucesivos bajo un contrato vigente | Cuando **ingreso recurrente mensual** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **periodo de recuperación** | Tiempo necesario para recuperar el costo de adquisición con el margen del cliente | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** La renovación automática exige información oportuna y un mecanismo de cancelación equivalente al de contratación. Dificultar la baja expone a sanción y destruye reputación.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre suscripción e ingreso recurrente |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Pricing manager, Product marketing, CFO comercial y Founder. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina recupera su costo de adquisición en 14 meses y su churn mensual es 3,4 %: la vida media del cliente es menor que el periodo de recuperación.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **elegir la métrica de cobro que sigue al valor → calcular el periodo de recuperación por segmento → definir la política de renovación y de cancelación → verificar el cumplimiento del deber de información → seguir expansión, contracción y baja por cohorte** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **ingreso recurrente mensual**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Lean Analytics* y la de *Customer Success*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **ingreso recurrente** y **periodo de recuperación** como sinónimos | Se perdió la distinción entre «ingreso comprometido que se repite en periodos sucesivos bajo un contrato vigente» y «tiempo necesario para recuperar el costo de adquisición con el margen del cliente» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «seguir expansión, contracción y baja por cohorte» | Se saltó «elegir la métrica de cobro que sigue al valor»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **ingreso recurrente mensual** | La métrica local reemplazó al resultado del sistema | Contrástala con **tasa de contracción** y explicita el costo de oportunidad. |
| Escalar adquisición con periodo de recuperación mayor que la vida del cliente | Error específico de esta clase | Compara periodo de recuperación con vida media antes de aumentar el gasto comercial. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **ingreso recurrente** y **periodo de recuperación** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **renovación automática** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «elegir la métrica de cobro que sigue al valor» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **ingreso recurrente mensual** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «La renovación automática exige información oportuna y un mecanismo de cancelación equivalente al de contratación. Dificultar la baja expone a sanción y destruye reputación»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **renovación automática** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **ingreso recurrente mensual**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Lean Analytics* y *The Customer Centricity Playbook*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P07-C09-suscripcion-y-recurring-revenue/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **ingreso recurrente mensual**, **periodo de recuperación** y **tasa de contracción** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **arquitectura de monetización con métrica de cobro, planes, price fences y política de descuentos**.

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

- Alistair Croll y Benjamin Yoskovitz — [*Lean Analytics*](https://openlibrary.org/isbn/9781449335670) (2013) · ISBN 9781449335670 — **aporta a esta clase:** los seis modelos de negocio y las métricas que cambian entre ellos. **Dónde buscarlo:** la parte sobre modelos de negocio. Registra edición y páginas consultadas en tu nota de lectura.
- Nick Mehta, Dan Steinman y Lincoln Murphy — [*Customer Success*](https://openlibrary.org/isbn/9781119168294) (2016) · ISBN 9781119168294 — **aporta a esta clase:** la expansión condicionada al resultado inicial acreditado. **Dónde buscarlo:** los capítulos sobre crecimiento en la base instalada. Registra edición y páginas consultadas en tu nota de lectura.
- Madhavan Ramanujam y Georg Tacke — [*Monetizing Innovation*](https://openlibrary.org/isbn/9781119240877) (2016) · ISBN 9781119240877 — **aporta a esta clase:** los modelos de monetización disponibles y el criterio para elegir la métrica de cobro. **Dónde buscarlo:** el capítulo sobre modelos de monetización. Registra edición y páginas consultadas en tu nota de lectura.
- Peter Fader y Sarah Toms — [*The Customer Centricity Playbook*](https://openlibrary.org/isbn/9781613630914) (2018) · ISBN 9781613630914 — **aporta a esta clase:** el valor de vida como proyección con supuestos declarados y no como cifra única. **Dónde buscarlo:** los capítulos sobre cálculo del valor de vida. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 08 · Versionado y price fences](class-08-versionado-y-price-fences.md) · [Índice de la parte](README.md) · [Clase 10 · Freemium y pruebas gratuitas](class-10-freemium-y-pruebas-gratuitas.md) →
