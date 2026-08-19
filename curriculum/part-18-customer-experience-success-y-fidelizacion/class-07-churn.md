# Clase 18.07 — Churn

Clase 7 de 14 de la parte [18 — Customer experience, success y fidelización](README.md), de nivel Operación de ingresos. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 18.06, *NPS, CSAT y CES*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de churn de ingreso mensual con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** Las leyes del éxito de cliente, entre ellas que vender al cliente equivocado destruye la retención — Nick Mehta, Dan Steinman y Lincoln Murphy. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

El churn se mide de varias formas —de clientes, de ingreso, bruto y neto— y cada una responde una pregunta distinta. Confundirlas produce diagnósticos falsos: una empresa puede perder pocas cuentas y mucho ingreso si las que se van son las grandes. Además, el motivo declarado rara vez es el real: la causa suele estar meses antes, en la venta o en el onboarding.

Esta sesión distingue lo que se sabe, lo que se supone y lo que todavía no se ha medido. La parte 18 busca **sostener y expandir el ingreso existente con un sistema de valor entregado**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **churn** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿En qué momento el cliente obtiene valor y qué lo hace quedarse o irse?

Los conceptos que estructuran la sesión son **churn de clientes**, **churn de ingreso**, **motivo declarado frente a causa raíz** y **cohorte de baja**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `churn de clientes`, `churn de ingreso`, `motivo declarado frente a causa raíz` y `cohorte de baja` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Customer experience, success y fidelización**.
3. **Aplicar** la secuencia **definir y calcular cada tipo de churn por separado → analizar por cohorte de incorporación y por segmento → recoger motivo declarado y buscar la causa raíz → identificar el momento del proceso donde se originó → intervenir en el origen y no en el síntoma** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **churn de ingreso mensual**, **churn por cohorte** y **concentración de bajas por segmento** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **churn de clientes** y **churn de ingreso** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **churn de ingreso mensual**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **churn de clientes** | cuentas perdidas sobre cuentas activas al inicio del periodo | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **churn de ingreso** | ingreso recurrente perdido sobre ingreso recurrente al inicio del periodo | Construye un caso límite donde el concepto se confunde con el anterior. |
| **motivo declarado frente a causa raíz** | distinción entre lo que el cliente dice y lo que originó la baja | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **cohorte de baja** | grupo de clientes que se dio de baja en el mismo periodo de incorporación | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir y calcular cada tipo de churn por separado → 2. analizar por cohorte de incorporación y por segmento → 3. recoger motivo declarado y buscar la causa raíz → 4. identificar el momento del proceso donde se originó → 5. intervenir en el origen y no en el síntoma
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Reducir el churn a cero no es un objetivo razonable: algunos clientes nunca debieron ser vendidos. La meta correcta considera la calidad del cliente ganado.

## 📖 Desarrollo

### 1. Churn de clientes: mecanismo central

**Churn de clientes** se entiende aquí como **cuentas perdidas sobre cuentas activas al inicio del periodo**.

El abandono de clientes se analiza mal cuando se mira sólo la tasa agregada. Distinguir churn de clientes de churn de ingreso es imprescindible: perder muchas cuentas pequeñas y perder una grande producen la misma cifra en un indicador y consecuencias muy distintas en el otro.

**De dónde viene esta afirmación.** Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) aporta la idea que sostiene este bloque: las leyes del éxito de cliente, entre ellas que vender al cliente equivocado destruye la retención. Búscala en la parte que enuncia las diez leyes. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «churn de ingreso mensual» debería moverse cuando cambie **churn de clientes**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **churn de ingreso**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Churn de ingreso: frontera conceptual y error de clasificación

**Definición operacional:** ingreso recurrente perdido sobre ingreso recurrente al inicio del periodo. Su valor está en distinguirlo de **churn de clientes**.

El motivo declarado y la causa raíz rara vez coinciden. Quien se va suele dar una razón cómoda —presupuesto, reorganización— porque es más fácil que explicar una insatisfacción. La entrevista de salida bien conducida, hecha por alguien que no era el responsable de la cuenta, obtiene información distinta y más útil.

**Contraste bibliográfico.** Peter Fader — *Customer Centricity* (2020, 2.ª ed.) aporta aquí una distinción concreta: la heterogeneidad del valor del cliente: no todos valen lo mismo ni deben tratarse igual (los capítulos sobre centricidad en el cliente). Formula dos mini-casos: uno que satisface la definición de **churn de ingreso** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «analizar por cohorte de incorporación y por segmento», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Motivo declarado frente a causa raíz: operacionalización y medición

**Motivo declarado frente a causa raíz** significa **distinción entre lo que el cliente dice y lo que originó la baja**.

La cohorte de baja es la unidad de análisis correcta: cuándo entraron las cuentas que se fueron y cuánto duraron. Ese análisis revela si el problema está en la venta —cuentas mal calificadas que duran poco— o en el servicio —cuentas que duran y luego se van—, y esas dos causas tienen soluciones opuestas.

Ficha de medición obligatoria para **churn de ingreso mensual**: `ingreso recurrente perdido, sobre ingreso recurrente al inicio del mes`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) pone una condición sobre la medición: el análisis de cohortes como corrección al promedio que esconde la mezcla (el capítulo sobre cohortes y segmentación). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Cohorte de baja: trade-offs y efectos de segundo orden

**Definición:** grupo de clientes que se dio de baja en el mismo periodo de incorporación.

Reducir el abandono puede lograrse mejorando el producto, mejorando el servicio o dejando de vender a quien no encaja. La tercera opción es la más rápida y la más resistida, porque reduce el ingreso del trimestre. Esa decisión corresponde a la dirección y debe tomarse con el cálculo del valor destruido por esas cuentas.

**Lo que aporta la fuente.** Fred Reichheld, Darci Darnell y Maureen Burns — *Winning on Purpose* (2021) aporta el criterio para pesar el intercambio: el cierre del circuito con quien respondió como parte del sistema (los capítulos sobre el proceso de retroalimentación). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **concentración de bajas por segmento** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **cohorte de baja** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «intervenir en el origen y no en el síntoma», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La tasa de abandono es un indicador rezagado: informa sobre decisiones tomadas meses antes. Gestionar sólo con ella equivale a conducir mirando el retrovisor. Los indicadores adelantados —activación, uso, salud, esfuerzo— son los que permiten intervenir, y el abandono sirve para verificar si la intervención funcionó.

**Frontera declarada.** Reducir el churn a cero no es un objetivo razonable: algunos clientes nunca debieron ser vendidos. La meta correcta considera la calidad del cliente ganado. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Retener con castigos contractuales en lugar de valor entregado y dañar reputación.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar churn no consiste en sumar definiciones. Empieza por **churn de clientes**, contrasta **churn de ingreso** con **motivo declarado frente a causa raíz**, incorpora **cohorte de baja** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) | Las leyes del éxito de cliente, entre ellas que vender al cliente equivocado destruye la retención | La parte que enuncia las diez leyes | ¿Qué debería observarse en **churn de clientes** si aquí opera «las leyes del éxito de cliente, entre ellas que vender al cliente equivocado destruye la retención»? ¿Y qué observación lo desmentiría en este caso? |
| Peter Fader — *Customer Centricity* (2020, 2.ª ed.) | La heterogeneidad del valor del cliente: no todos valen lo mismo ni deben tratarse igual | Los capítulos sobre centricidad en el cliente | ¿Qué debería observarse en **churn de ingreso** si aquí opera «la heterogeneidad del valor del cliente: no todos valen lo mismo ni deben tratarse igual»? ¿Y qué observación lo desmentiría en este caso? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | El análisis de cohortes como corrección al promedio que esconde la mezcla | El capítulo sobre cohortes y segmentación | ¿Qué debería observarse en **motivo declarado frente a causa raíz** si aquí opera «el análisis de cohortes como corrección al promedio que esconde la mezcla»? ¿Y qué observación lo desmentiría en este caso? |
| Fred Reichheld, Darci Darnell y Maureen Burns — *Winning on Purpose* (2021) | El cierre del circuito con quien respondió como parte del sistema | Los capítulos sobre el proceso de retroalimentación | ¿Qué debería observarse en **cohorte de baja** si aquí opera «el cierre del circuito con quien respondió como parte del sistema»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina pierde 3,4 % de cuentas al mes. El churn de ingreso es 5,1 % porque las cuentas que se van son las de mayor facturación.

**Paso 1 — Definir y calcular cada tipo de churn por separado.** El equipo escribe primero el supuesto asociado a **churn de clientes** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **churn de ingreso mensual** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Analizar por cohorte de incorporación y por segmento.** El trabajo aquí es separar lo observado de lo inferido sobre **churn de ingreso**. La evidencia que ordena la discusión es **churn por cohorte**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Recoger motivo declarado y buscar la causa raíz.** El riesgo de este paso es cerrar demasiado rápido alrededor de **motivo declarado frente a causa raíz**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **concentración de bajas por segmento** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Identificar el momento del proceso donde se originó.** Con **cohorte de baja** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **churn de ingreso mensual** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Intervenir en el origen y no en el síntoma.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **churn de clientes**. **churn por cohorte** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **churn de clientes** | Cuentas perdidas sobre cuentas activas al inicio del periodo | Cuando **churn de ingreso mensual** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **churn de ingreso** | Ingreso recurrente perdido sobre ingreso recurrente al inicio del periodo | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Reducir el churn a cero no es un objetivo razonable: algunos clientes nunca debieron ser vendidos. La meta correcta considera la calidad del cliente ganado.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre churn |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Customer success manager, Account manager y Head of CS. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina pierde 3,4 % de cuentas al mes. El churn de ingreso es 5,1 % porque las cuentas que se van son las de mayor facturación.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir y calcular cada tipo de churn por separado → analizar por cohorte de incorporación y por segmento → recoger motivo declarado y buscar la causa raíz → identificar el momento del proceso donde se originó → intervenir en el origen y no en el síntoma** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **churn de ingreso mensual**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Customer Success* y la de *Customer Centricity*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **churn de clientes** y **churn de ingreso** como sinónimos | Se perdió la distinción entre «cuentas perdidas sobre cuentas activas al inicio del periodo» y «ingreso recurrente perdido sobre ingreso recurrente al inicio del periodo» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «intervenir en el origen y no en el síntoma» | Se saltó «definir y calcular cada tipo de churn por separado»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **churn de ingreso mensual** | La métrica local reemplazó al resultado del sistema | Contrástala con **concentración de bajas por segmento** y explicita el costo de oportunidad. |
| Reportar sólo churn de clientes | Error específico de esta clase | Calcula churn de clientes y de ingreso por separado y analiza por cohorte y segmento. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **churn de clientes** y **churn de ingreso** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **motivo declarado frente a causa raíz** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir y calcular cada tipo de churn por separado» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **churn de ingreso mensual** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Reducir el churn a cero no es un objetivo razonable: algunos clientes nunca debieron ser vendidos. La meta correcta considera la calidad del cliente ganado»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **motivo declarado frente a causa raíz** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **churn de ingreso mensual**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Customer Success* y *Winning on Purpose*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Retener con castigos contractuales en lugar de valor entregado y dañar reputación.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, comprueba la norma en su texto vigente. Los enlaces van al texto completo publicado por la Biblioteca del Congreso Nacional; son gratuitos y no hace falta creerle a este material.

- **Consumo y comercio.** [Ley 19.496](https://www.bcn.cl/leychile/navegar?idNorma=61438) — *Establece normas sobre protección de los derechos de los consumidores* (Ministerio de Economía, Fomento y Reconstrucción), y su reglamento de comercio electrónico, [Decreto 6/2021](https://www.bcn.cl/leychile/navegar?idNorma=1165504) — *Aprueba reglamento de comercio electrónico* (Ministerio de Economía, Fomento y Turismo).
- **Datos personales.** [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales* (Ministerio Secretaría General de la Presidencia), que sustituye progresivamente a [Ley 19.628](https://www.bcn.cl/leychile/navegar?idNorma=141599) — *Sobre protección de la vida privada* (Ministerio Secretaría General de la Presidencia).
- **Derecho a retracto.** [Decreto 52/2024](https://www.bcn.cl/leychile/navegar?idNorma=1206144) — *Aprueba reglamento que regula la forma y condiciones en que los proveedores deberán comunicar la exclusión del derecho a retracto y los bienes en que excepcionalmente y por su naturaleza procederá tal exclusión* (Ministerio de Economía, Fomento y Turismo).

Dentro del repositorio, el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) ordena qué norma aplica a cada decisión comercial, [datos personales y ética](../../docs/DATOS-PERSONALES-Y-ETICA.md) desarrolla el tratamiento de datos y [fuentes oficiales](../../docs/FUENTES-OFICIALES.md) lista los organismos con su fecha de consulta. Ninguno de esos documentos reemplaza al texto legal.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P18-C07-churn/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **churn de ingreso mensual**, **churn por cohorte** y **concentración de bajas por segmento** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **sistema de retención y expansión con onboarding, health score, renovación y advocacy**.

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

- Nick Mehta, Dan Steinman y Lincoln Murphy — [*Customer Success*](https://openlibrary.org/isbn/9781119168294) (2016) · ISBN 9781119168294 — **aporta a esta clase:** las leyes del éxito de cliente, entre ellas que vender al cliente equivocado destruye la retención. **Dónde buscarlo:** la parte que enuncia las diez leyes. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Peter Fader — [*Customer Centricity*](https://openlibrary.org/isbn/9781613631447) (2020, 2.ª ed.) · ISBN 9781613631447 — **aporta a esta clase:** la heterogeneidad del valor del cliente: no todos valen lo mismo ni deben tratarse igual. **Dónde buscarlo:** los capítulos sobre centricidad en el cliente. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Alistair Croll y Benjamin Yoskovitz — [*Lean Analytics*](https://openlibrary.org/isbn/9781449335670) (2013) · ISBN 9781449335670 — **aporta a esta clase:** el análisis de cohortes como corrección al promedio que esconde la mezcla. **Dónde buscarlo:** el capítulo sobre cohortes y segmentación. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Fred Reichheld, Darci Darnell y Maureen Burns — [*Winning on Purpose*](https://openlibrary.org/isbn/9781647821784) (2021) · ISBN 9781647821784 — **aporta a esta clase:** el cierre del circuito con quien respondió como parte del sistema. **Dónde buscarlo:** los capítulos sobre el proceso de retroalimentación. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 06 · NPS, CSAT y CES](class-06-nps-csat-y-ces.md) · [Índice de la parte](README.md) · [Clase 08 · Retención](class-08-retention.md) →
