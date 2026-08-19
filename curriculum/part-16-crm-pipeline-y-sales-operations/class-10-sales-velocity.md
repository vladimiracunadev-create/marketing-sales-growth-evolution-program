---
title: "Velocidad comercial"
type: class
language: es
standard: clase-profunda-v2
part: 16
class: 10
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["roberge", "grove", "croll-yoskovitz", "miller-heiman"]
anchors: {"croll-yoskovitz": "una-metrica", "grove": "apalancamiento", "miller-heiman": "plan-cuenta", "roberge": "proceso-comprador"}
updated: 2026-08-19
---

# Clase 16.10 — Velocidad comercial

Clase 10 de 14 de la parte [16 — CRM, pipeline y sales operations](README.md), de nivel Operación de ingresos. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 16.09, *Capacidad comercial*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de duración mediana del ciclo con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El proceso comercial construido sobre el proceso de compra del cliente — Mark Roberge. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La velocidad comercial combina cuatro variables: número de oportunidades, valor promedio, tasa de cierre y duración del ciclo. Su utilidad no está en el número final sino en el diagnóstico: muestra qué palanca produce más efecto. Reducir el ciclo un 20 % suele ser más barato que aumentar el número de oportunidades en la misma proporción, y casi nunca se intenta.

Antes de cualquier herramienta, esta clase obliga a nombrar qué cambiaría si el análisis fuese correcto. La parte 16 busca **convertir el CRM en un sistema de trabajo y de verdad operacional**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **velocidad comercial** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿El pipeline describe la realidad o solo el optimismo del equipo?

Los conceptos que estructuran la sesión son **velocidad comercial**, **palanca dominante**, **duración del ciclo** y **efecto compuesto**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `velocidad comercial`, `palanca dominante`, `duración del ciclo` y `efecto compuesto` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **CRM, pipeline y sales operations**.
3. **Aplicar** la secuencia **calcular las cuatro variables con datos propios → simular el efecto de mejorar cada una por separado → identificar la palanca dominante y su costo → intervenir sobre esa palanca → medir el efecto y recalcular** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **duración mediana del ciclo**, **valor promedio de oportunidad** y **velocidad comercial calculada** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **velocidad comercial** y **palanca dominante** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **duración mediana del ciclo**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **velocidad comercial** | resultado de combinar oportunidades, valor, tasa de cierre y duración del ciclo | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **palanca dominante** | variable cuya mejora produce mayor efecto sobre el resultado | Da un hecho compatible con la definición y otro que la refute. |
| **duración del ciclo** | tiempo entre la creación de la oportunidad y su cierre | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **efecto compuesto** | resultado de mejorar varias variables simultáneamente | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. calcular las cuatro variables con datos propios → 2. simular el efecto de mejorar cada una por separado → 3. identificar la palanca dominante y su costo → 4. intervenir sobre esa palanca → 5. medir el efecto y recalcular
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Acelerar el ciclo puede reducir la calidad del diagnóstico y aumentar el churn posterior. La velocidad debe evaluarse junto con la retención.

## 📖 Desarrollo

### 1. Velocidad comercial: mecanismo central

**Velocidad comercial** se entiende aquí como **resultado de combinar oportunidades, valor, tasa de cierre y duración del ciclo**.

La velocidad comercial combina número de oportunidades, valor medio, tasa de cierre y duración del ciclo en una sola expresión. Su utilidad no está en el número resultante sino en la descomposición: permite ver cuál de los cuatro factores explica un cambio y cuál ofrece más margen de mejora.

**De dónde viene esta afirmación.** Mark Roberge — *The Sales Acceleration Formula* (2015) aporta la idea que sostiene este bloque: el proceso comercial construido sobre el proceso de compra del cliente. Búscala en los capítulos sobre alineación con el comprador. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «duración mediana del ciclo» debería moverse cuando cambie **velocidad comercial**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **palanca dominante**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Palanca dominante: frontera conceptual y error de clasificación

**Definición operacional:** variable cuya mejora produce mayor efecto sobre el resultado. Su valor está en distinguirlo de **velocidad comercial**.

La palanca dominante rara vez es la que el equipo intuye. Reducir el ciclo suele tener un efecto mayor que aumentar el volumen, y es más barato. Identificarla exige calcular el efecto de una mejora porcentual equivalente en cada factor, ejercicio simple que cambia la prioridad de las iniciativas.

**Contraste bibliográfico.** Andrew S. Grove — *High Output Management* (1983) aporta aquí una distinción concreta: el apalancamiento gerencial: qué actividades multiplican el output (los capítulos sobre apalancamiento). Formula dos mini-casos: uno que satisface la definición de **palanca dominante** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «simular el efecto de mejorar cada una por separado», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Duración del ciclo: operacionalización y medición

**Duración del ciclo** significa **tiempo entre la creación de la oportunidad y su cierre**.

La duración del ciclo debe medirse con la mediana y por segmento, porque el promedio se distorsiona con pocos negocios muy largos. Además, medirla sólo sobre negocios ganados produce un sesgo: los perdidos también consumieron tiempo, y ese consumo es parte del costo del sistema.

Ficha de medición obligatoria para **duración mediana del ciclo**: `días entre creación y cierre de la oportunidad, mediana por segmento`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) pone una condición sobre la medición: la métrica que importa ahora: una sola, según etapa y modelo de negocio (los capítulos sobre la métrica única). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Efecto compuesto: trade-offs y efectos de segundo orden

**Definición:** resultado de mejorar varias variables simultáneamente.

Acelerar el ciclo puede lograrse presionando, lo que deteriora la calidad de la decisión del cliente y aumenta las bajas posteriores. La aceleración legítima viene de eliminar esperas del proceso propio: tiempos de respuesta, aprobaciones internas, generación de propuestas. Esa distinción es importante y suele omitirse.

**Lo que aporta la fuente.** Robert B. Miller y Stephen E. Heiman — *The New Strategic Selling* (2005) aporta el criterio para pesar el intercambio: el plan de cuenta como documento vivo con posición, riesgos y siguiente acción (los capítulos sobre planificación estratégica de cuentas). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **velocidad comercial calculada** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **efecto compuesto** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «medir el efecto y recalcular», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La velocidad comercial es un indicador agregado y su mejora puede deberse a un cambio de mezcla y no a una mejora real. Un aumento por mayor proporción de negocios pequeños y rápidos no significa que el sistema mejoró. Toda lectura debe acompañarse de la evolución de la mezcla.

**Frontera declarada.** Acelerar el ciclo puede reducir la calidad del diagnóstico y aumentar el churn posterior. La velocidad debe evaluarse junto con la retención. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Tomar decisiones de contratación y presupuesto sobre un pipeline que no representa la realidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar velocidad comercial no consiste en sumar definiciones. Empieza por **velocidad comercial**, contrasta **palanca dominante** con **duración del ciclo**, incorpora **efecto compuesto** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Mark Roberge — *The Sales Acceleration Formula* (2015) | El proceso comercial construido sobre el proceso de compra del cliente | Los capítulos sobre alineación con el comprador | ¿Qué debería observarse en **velocidad comercial** si aquí opera «el proceso comercial construido sobre el proceso de compra del cliente»? ¿Y qué observación lo desmentiría en este caso? |
| Andrew S. Grove — *High Output Management* (1983) | El apalancamiento gerencial: qué actividades multiplican el output | Los capítulos sobre apalancamiento | ¿Qué debería observarse en **palanca dominante** si aquí opera «el apalancamiento gerencial: qué actividades multiplican el output»? ¿Y qué observación lo desmentiría en este caso? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | La métrica que importa ahora: una sola, según etapa y modelo de negocio | Los capítulos sobre la métrica única | ¿Qué debería observarse en **duración del ciclo** si aquí opera «la métrica que importa ahora: una sola, según etapa y modelo de negocio»? ¿Y qué observación lo desmentiría en este caso? |
| Robert B. Miller y Stephen E. Heiman — *The New Strategic Selling* (2005) | El plan de cuenta como documento vivo con posición, riesgos y siguiente acción | Los capítulos sobre planificación estratégica de cuentas | ¿Qué debería observarse en **efecto compuesto** si aquí opera «el plan de cuenta como documento vivo con posición, riesgos y siguiente acción»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El ciclo mediano de Ruta Andina es 71 días y el 44 % de ese tiempo transcurre entre el envío de la propuesta y la primera respuesta del cliente.

**Paso 1 — Calcular las cuatro variables con datos propios.** El equipo escribe primero el supuesto asociado a **velocidad comercial** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **duración mediana del ciclo** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Simular el efecto de mejorar cada una por separado.** El trabajo aquí es separar lo observado de lo inferido sobre **palanca dominante**. La evidencia que ordena la discusión es **valor promedio de oportunidad**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Identificar la palanca dominante y su costo.** El riesgo de este paso es cerrar demasiado rápido alrededor de **duración del ciclo**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **velocidad comercial calculada** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Intervenir sobre esa palanca.** Con **efecto compuesto** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **duración mediana del ciclo** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Medir el efecto y recalcular.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **velocidad comercial**. **valor promedio de oportunidad** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **velocidad comercial** | Resultado de combinar oportunidades, valor, tasa de cierre y duración del ciclo | Cuando **duración mediana del ciclo** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **palanca dominante** | Variable cuya mejora produce mayor efecto sobre el resultado | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Acelerar el ciclo puede reducir la calidad del diagnóstico y aumentar el churn posterior. La velocidad debe evaluarse junto con la retención.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre velocidad comercial |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Sales operations, RevOps analyst y Jefe de ventas. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El ciclo mediano de Ruta Andina es 71 días y el 44 % de ese tiempo transcurre entre el envío de la propuesta y la primera respuesta del cliente.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **calcular las cuatro variables con datos propios → simular el efecto de mejorar cada una por separado → identificar la palanca dominante y su costo → intervenir sobre esa palanca → medir el efecto y recalcular** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **duración mediana del ciclo**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *The Sales Acceleration Formula* y la de *High Output Management*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **velocidad comercial** y **palanca dominante** como sinónimos | Se perdió la distinción entre «resultado de combinar oportunidades, valor, tasa de cierre y duración del ciclo» y «variable cuya mejora produce mayor efecto sobre el resultado» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «medir el efecto y recalcular» | Se saltó «calcular las cuatro variables con datos propios»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **duración mediana del ciclo** | La métrica local reemplazó al resultado del sistema | Contrástala con **velocidad comercial calculada** y explicita el costo de oportunidad. |
| Buscar sólo más oportunidades | Error específico de esta clase | Simula el efecto de reducir el ciclo y de mejorar la tasa de cierre antes de aumentar la generación. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **velocidad comercial** y **palanca dominante** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **duración del ciclo** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «calcular las cuatro variables con datos propios» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **duración mediana del ciclo** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Acelerar el ciclo puede reducir la calidad del diagnóstico y aumentar el churn posterior. La velocidad debe evaluarse junto con la retención»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **duración del ciclo** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **duración mediana del ciclo**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *The Sales Acceleration Formula* y *The New Strategic Selling*. |
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

Guarda en `evidence/P16-C10-sales-velocity/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **duración mediana del ciclo**, **valor promedio de oportunidad** y **velocidad comercial calculada** con fuente, ventana y lectura prohibida.
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

- Mark Roberge — [*The Sales Acceleration Formula*](https://openlibrary.org/isbn/9781119047018) (2015) · ISBN 9781119047018 — **aporta a esta clase:** el proceso comercial construido sobre el proceso de compra del cliente. **Dónde buscarlo:** los capítulos sobre alineación con el comprador. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Andrew S. Grove — [*High Output Management*](https://openlibrary.org/isbn/9780394532349) (1983) · ISBN 9780394532349 — **aporta a esta clase:** el apalancamiento gerencial: qué actividades multiplican el output. **Dónde buscarlo:** los capítulos sobre apalancamiento. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Alistair Croll y Benjamin Yoskovitz — [*Lean Analytics*](https://openlibrary.org/isbn/9781449335670) (2013) · ISBN 9781449335670 — **aporta a esta clase:** la métrica que importa ahora: una sola, según etapa y modelo de negocio. **Dónde buscarlo:** los capítulos sobre la métrica única. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Robert B. Miller y Stephen E. Heiman — [*The New Strategic Selling*](https://openlibrary.org/isbn/9780446695190) (2005) · ISBN 9780446695190 — **aporta a esta clase:** el plan de cuenta como documento vivo con posición, riesgos y siguiente acción. **Dónde buscarlo:** los capítulos sobre planificación estratégica de cuentas. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 09 · Capacidad comercial](class-09-sales-capacity.md) · [Índice de la parte](README.md) · [Clase 11 · Dashboards comerciales](class-11-dashboards-comerciales.md) →
