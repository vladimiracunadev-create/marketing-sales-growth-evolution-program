---
title: "Costo de adquisición de cliente"
type: class
language: es
standard: clase-profunda-v2
part: 20
class: 03
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["croll-yoskovitz", "provost", "fader-ltv", "kaushik"]
anchors: {"croll-yoskovitz": "modelos", "fader-ltv": "cohortes-valor", "kaushik": "plan-medicion", "provost": "valor-esperado"}
updated: 2026-08-19
---

# Clase 20.03 — Costo de adquisición de cliente

**Parte 20 · Analítica comercial y marketing science** · Nivel: Crecimiento y analítica · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 20.02 — *Conversión y embudos*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de costo de adquisición por canal para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** Los seis modelos de negocio y las métricas que cambian entre ellos — Alistair Croll y Benjamin Yoskovitz. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

El costo de adquisición debe incluir todo el gasto necesario para conseguir un cliente nuevo: medios, herramientas, sueldos comerciales y de marketing, comisiones. Excluir sueldos es el error más común y el más caro, porque produce una economía aparente que no resiste una revisión financiera. El cálculo debe hacerse por segmento y por canal, no sólo agregado.

Antes de cualquier herramienta, esta clase obliga a nombrar qué cambiaría si el análisis fuese correcto. La parte 20 busca **sostener decisiones de ingreso con métricas correctamente construidas**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **costo de adquisición de cliente** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Esta cifra mide lo que creo que mide, y qué decisión cambiaría si estuviera equivocada?

Los conceptos que estructuran la sesión son **alcance del costo**, **costo por canal**, **periodo de atribución** y **costo mixto**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `alcance del costo`, `costo por canal`, `periodo de atribución` y `costo mixto` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Analítica comercial y marketing science**.
3. **Aplicar** la secuencia **declarar el alcance del cálculo por escrito → atribuir el gasto a canales y segmentos → considerar el desfase entre gasto e incorporación → calcular por canal y por segmento → conciliar el total con la contabilidad** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **costo de adquisición por canal**, **dispersión entre canales** y **conciliación con contabilidad** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **alcance del costo** y **costo por canal** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **costo de adquisición por canal**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **alcance del costo** | conjunto de gastos incluidos en el cálculo, declarado por escrito | Construye un caso límite donde el concepto se confunde con el anterior. |
| **costo por canal** | gasto atribuible dividido por clientes nuevos originados en ese canal | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **periodo de atribución** | desfase entre el gasto y la incorporación del cliente que produce | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **costo mixto** | promedio que combina canales con economías muy distintas | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. declarar el alcance del cálculo por escrito → 2. atribuir el gasto a canales y segmentos → 3. considerar el desfase entre gasto e incorporación → 4. calcular por canal y por segmento → 5. conciliar el total con la contabilidad
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** El costo promedio esconde diferencias entre canales. Escalar sobre el promedio puede significar aumentar el gasto en el canal menos eficiente.

## 📖 Desarrollo

### 1. Alcance del costo: mecanismo central

**Alcance del costo** se entiende aquí como **conjunto de gastos incluidos en el cálculo, declarado por escrito**.

El costo de adquisición de cliente parece simple y es una de las métricas peor calculadas. Su definición exige decidir qué costos se incluyen —sólo medios, o también sueldos, herramientas y comisiones—, qué periodo se considera y cómo se atribuyen los costos compartidos entre canales.

**De dónde viene esta afirmación.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) aporta la idea que sostiene este bloque: los seis modelos de negocio y las métricas que cambian entre ellos. Búscala en la parte sobre modelos de negocio. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «costo de adquisición por canal» debería moverse cuando cambie **alcance del costo**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **costo por canal**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Costo por canal: frontera conceptual y error de clasificación

**Definición operacional:** gasto atribuible dividido por clientes nuevos originados en ese canal. Su valor está en distinguirlo de **alcance del costo**.

El alcance del costo debe ser completo si el número va a compararse con el valor del cliente. Un cálculo que sólo incluye gasto en medios subestima de forma considerable y produce decisiones de inversión equivocadas. La versión completa suele ser incómoda y es la única defendible.

**Contraste bibliográfico.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta aquí una distinción concreta: el marco de valor esperado que combina probabilidad y consecuencia económica (el capítulo sobre valor esperado). Formula dos mini-casos: uno que satisface la definición de **costo por canal** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «atribuir el gasto a canales y segmentos», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Periodo de atribución: operacionalización y medición

**Periodo de atribución** significa **desfase entre el gasto y la incorporación del cliente que produce**.

El costo por canal exige atribuir, y la atribución es imperfecta. Una forma honesta de manejarlo es reportar el costo mixto —total de gasto sobre total de clientes nuevos— junto con las estimaciones por canal, declarando el modelo de atribución usado. El costo mixto no se puede discutir; el por canal siempre es una estimación.

Ficha de medición obligatoria para **costo de adquisición por canal**: `gasto atribuible dividido por clientes nuevos, por canal`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Peter Fader y Sarah Toms — *The Customer Centricity Playbook* (2018) pone una condición sobre la medición: las cohortes como base del cálculo, frente al promedio agregado (los capítulos sobre análisis por cohorte). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Costo mixto: trade-offs y efectos de segundo orden

**Definición:** promedio que combina canales con economías muy distintas.

Optimizar el costo de adquisición favorece los canales de captura de demanda existente y penaliza los que construyen demanda futura, cuyo efecto no aparece en la ventana de medición. Esa asimetría es estructural y debe compensarse con una decisión explícita de asignación, no esperando que los datos la corrijan.

**Lo que aporta la fuente.** Avinash Kaushik — *Web Analytics 2.0* (2009) aporta el criterio para pesar el intercambio: el plan de medición que va de la decisión a la métrica y no al revés (los capítulos sobre estrategia de medición). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **conciliación con contabilidad** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **costo mixto** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «conciliar el total con la contabilidad», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El costo de adquisición sólo significa algo comparado con el valor que ese cliente genera. Un costo alto puede ser excelente si la permanencia es larga, y uno bajo puede ser ruinoso si el cliente se va en tres meses. Presentar el costo sin su contraparte es una de las prácticas más engañosas de los tableros comerciales.

**Frontera declarada.** El costo promedio esconde diferencias entre canales. Escalar sobre el promedio puede significar aumentar el gasto en el canal menos eficiente. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar costo de adquisición de cliente no consiste en sumar definiciones. Empieza por **alcance del costo**, contrasta **costo por canal** con **periodo de atribución**, incorpora **costo mixto** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | Los seis modelos de negocio y las métricas que cambian entre ellos | La parte sobre modelos de negocio | ¿Qué debería observarse en **alcance del costo** si aquí opera «los seis modelos de negocio y las métricas que cambian entre ellos»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | El marco de valor esperado que combina probabilidad y consecuencia económica | El capítulo sobre valor esperado | ¿Qué debería observarse en **costo por canal** si aquí opera «el marco de valor esperado que combina probabilidad y consecuencia económica»? ¿Y qué observación lo desmentiría en este caso? |
| Peter Fader y Sarah Toms — *The Customer Centricity Playbook* (2018) | Las cohortes como base del cálculo, frente al promedio agregado | Los capítulos sobre análisis por cohorte | ¿Qué debería observarse en **periodo de atribución** si aquí opera «las cohortes como base del cálculo, frente al promedio agregado»? ¿Y qué observación lo desmentiría en este caso? |
| Avinash Kaushik — *Web Analytics 2.0* (2009) | El plan de medición que va de la decisión a la métrica y no al revés | Los capítulos sobre estrategia de medición | ¿Qué debería observarse en **costo mixto** si aquí opera «el plan de medición que va de la decisión a la métrica y no al revés»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina reporta un costo de adquisición de CLP 310.000. Al incluir los sueldos del equipo comercial y de marketing, la cifra real supera CLP 700.000.

**Paso 1 — Declarar el alcance del cálculo por escrito.** El equipo escribe primero el supuesto asociado a **alcance del costo** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **costo de adquisición por canal** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Atribuir el gasto a canales y segmentos.** El trabajo aquí es separar lo observado de lo inferido sobre **costo por canal**. La evidencia que ordena la discusión es **dispersión entre canales**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Considerar el desfase entre gasto e incorporación.** El riesgo de este paso es cerrar demasiado rápido alrededor de **periodo de atribución**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **conciliación con contabilidad** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Calcular por canal y por segmento.** Con **costo mixto** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **costo de adquisición por canal** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Conciliar el total con la contabilidad.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **alcance del costo**. **dispersión entre canales** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **alcance del costo** | Conjunto de gastos incluidos en el cálculo, declarado por escrito | Cuando **costo de adquisición por canal** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **costo por canal** | Gasto atribuible dividido por clientes nuevos originados en ese canal | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** El costo promedio esconde diferencias entre canales. Escalar sobre el promedio puede significar aumentar el gasto en el canal menos eficiente.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre costo de adquisición de cliente |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing analyst, Revenue analyst y Data-driven marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina reporta un costo de adquisición de CLP 310.000. Al incluir los sueldos del equipo comercial y de marketing, la cifra real supera CLP 700.000.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **declarar el alcance del cálculo por escrito → atribuir el gasto a canales y segmentos → considerar el desfase entre gasto e incorporación → calcular por canal y por segmento → conciliar el total con la contabilidad** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **costo de adquisición por canal**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Lean Analytics* y la de *Data Science for Business*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **alcance del costo** y **costo por canal** como sinónimos | Se perdió la distinción entre «conjunto de gastos incluidos en el cálculo, declarado por escrito» y «gasto atribuible dividido por clientes nuevos originados en ese canal» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «conciliar el total con la contabilidad» | Se saltó «declarar el alcance del cálculo por escrito»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **costo de adquisición por canal** | La métrica local reemplazó al resultado del sistema | Contrástala con **conciliación con contabilidad** y explicita el costo de oportunidad. |
| Excluir sueldos del cálculo | Error específico de esta clase | Declara el alcance completo, incluye remuneraciones y concilia con contabilidad. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **alcance del costo** y **costo por canal** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **periodo de atribución** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «declarar el alcance del cálculo por escrito» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **costo de adquisición por canal** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «El costo promedio esconde diferencias entre canales. Escalar sobre el promedio puede significar aumentar el gasto en el canal menos eficiente»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **periodo de atribución** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **costo de adquisición por canal**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Lean Analytics* y *Web Analytics 2.0*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P20-C03-cac/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **costo de adquisición por canal**, **dispersión entre canales** y **conciliación con contabilidad** con fuente, ventana y lectura prohibida.
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

Cada obra aparece con la idea concreta que aporta a esta clase. Si al leer no encuentras esa idea, la cita está mal puesta y corresponde reportarlo como error del material.

- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — **aporta a esta clase:** los seis modelos de negocio y las métricas que cambian entre ellos. **Dónde buscarlo:** la parte sobre modelos de negocio. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — **aporta a esta clase:** el marco de valor esperado que combina probabilidad y consecuencia económica. **Dónde buscarlo:** el capítulo sobre valor esperado. Registra edición y páginas consultadas en tu nota de lectura.
- Peter Fader y Sarah Toms — *The Customer Centricity Playbook* (2018) — **aporta a esta clase:** las cohortes como base del cálculo, frente al promedio agregado. **Dónde buscarlo:** los capítulos sobre análisis por cohorte. Registra edición y páginas consultadas en tu nota de lectura.
- Avinash Kaushik — *Web Analytics 2.0* (2009) — **aporta a esta clase:** el plan de medición que va de la decisión a la métrica y no al revés. **Dónde buscarlo:** los capítulos sobre estrategia de medición. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 02 · Conversión y embudos](class-02-conversion-y-funnels.md) · [Índice de la parte](README.md) · [Clase 04 · Valor de vida del cliente](class-04-ltv.md) →
