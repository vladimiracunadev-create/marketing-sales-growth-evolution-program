# Clase 18.09 — Análisis de cohortes

Clase 9 de 14 de la parte [18 — Customer experience, success y fidelización](README.md), de nivel Operación de ingresos. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 18.08, *Retención*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de retención por cohorte en el mismo hito con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El análisis de cohortes como corrección al promedio que esconde la mezcla — Alistair Croll y Benjamin Yoskovitz. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

El análisis de cohortes agrupa clientes por periodo de incorporación y sigue su comportamiento en el tiempo. Es la herramienta que revela si la empresa está mejorando: si cada cohorte nueva retiene mejor que la anterior, algo está funcionando. Los promedios agregados esconden exactamente esa información, porque mezclan clientes con antigüedades distintas.

Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales. La parte 18 busca **sostener y expandir el ingreso existente con un sistema de valor entregado**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **análisis de cohortes** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿En qué momento el cliente obtiene valor y qué lo hace quedarse o irse?

Los conceptos que estructuran la sesión son **cohorte**, **seguimiento longitudinal**, **efecto de mezcla** y **mejora entre cohortes**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `cohorte`, `seguimiento longitudinal`, `efecto de mezcla` y `mejora entre cohortes` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Customer experience, success y fidelización**.
3. **Aplicar** la secuencia **definir el criterio de cohorte y la métrica a seguir → construir la tabla de cohortes con datos propios → comparar cohortes sucesivas en el mismo hito → atribuir las diferencias a cambios conocidos → usar el análisis para evaluar intervenciones** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **retención por cohorte en el mismo hito**, **ingreso acumulado por cohorte** y **tendencia entre cohortes** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **cohorte** y **seguimiento longitudinal** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **retención por cohorte en el mismo hito**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **cohorte** | grupo de clientes que comparte el periodo de incorporación | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **seguimiento longitudinal** | observación del mismo grupo a lo largo de varios periodos | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **efecto de mezcla** | distorsión del promedio provocada por la combinación de cohortes distintas | Da un hecho compatible con la definición y otro que la refute. |
| **mejora entre cohortes** | diferencia de comportamiento entre grupos incorporados en periodos sucesivos | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir el criterio de cohorte y la métrica a seguir → 2. construir la tabla de cohortes con datos propios → 3. comparar cohortes sucesivas en el mismo hito → 4. atribuir las diferencias a cambios conocidos → 5. usar el análisis para evaluar intervenciones
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Las cohortes recientes tienen poca historia y sus proyecciones son inciertas. Comparar sólo en hitos con datos completos evita conclusiones falsas.

## 📖 Desarrollo

### 1. Cohorte: mecanismo central

**Cohorte** se entiende aquí como **grupo de clientes que comparte el periodo de incorporación**.

El análisis por cohortes agrupa a los clientes según cuándo empezaron y sigue a cada grupo en el tiempo. Es la técnica que corrige el efecto de mezcla, que es la principal fuente de conclusiones erróneas en métricas agregadas: un promedio puede mejorar mientras cada grupo empeora, si cambia la proporción entre grupos.

**De dónde viene esta afirmación.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) aporta la idea que sostiene este bloque: el análisis de cohortes como corrección al promedio que esconde la mezcla. Búscala en el capítulo sobre cohortes y segmentación. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «retención por cohorte en el mismo hito» debería moverse cuando cambie **cohorte**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **seguimiento longitudinal**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Seguimiento longitudinal: frontera conceptual y error de clasificación

**Definición operacional:** observación del mismo grupo a lo largo de varios periodos. Su valor está en distinguirlo de **cohorte**.

El seguimiento longitudinal permite comparar cohortes en el mismo punto de su vida, que es la única comparación válida. Comparar una cohorte de tres meses con una de dos años no informa sobre mejora; comparar cada una a los tres meses sí lo hace. Esa disciplina es simple y frecuentemente se incumple.

**Contraste bibliográfico.** Peter Fader — *Customer Centricity* (2020, 2.ª ed.) aporta aquí una distinción concreta: recencia, frecuencia y valor como base de segmentación conductual (los capítulos sobre segmentación por comportamiento). Formula dos mini-casos: uno que satisface la definición de **seguimiento longitudinal** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «construir la tabla de cohortes con datos propios», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Efecto de mezcla: operacionalización y medición

**Efecto de mezcla** significa **distorsión del promedio provocada por la combinación de cohortes distintas**.

La mejora entre cohortes es la evidencia de que una intervención funcionó: si las cohortes posteriores al cambio retienen mejor en el mismo punto de vida, hay señal. Ese es el diseño de evaluación más accesible para cambios de producto o de proceso que no admiten experimento controlado.

Ficha de medición obligatoria para **retención por cohorte en el mismo hito**: `retención al mes N, comparada entre cohortes sucesivas`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) pone una condición sobre la medición: la distinción entre correlación observada y causalidad y qué exige cada una (los capítulos sobre inferencia y sesgo). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Mejora entre cohortes: trade-offs y efectos de segundo orden

**Definición:** diferencia de comportamiento entre grupos incorporados en periodos sucesivos.

Cohortes más finas —por mes, por canal, por segmento— entregan más resolución y reducen el tamaño de cada grupo hasta que el ruido domina. La granularidad debe corresponder al volumen: con pocos clientes por mes, las cohortes trimestrales o semestrales son más informativas aunque parezcan menos precisas.

**Lo que aporta la fuente.** Avinash Kaushik — *Web Analytics 2.0* (2009) aporta el criterio para pesar el intercambio: la segmentación como condición para que un promedio signifique algo (el capítulo sobre segmentación de datos). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **tendencia entre cohortes** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **mejora entre cohortes** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «usar el análisis para evaluar intervenciones», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El análisis por cohortes describe lo que ocurrió con grupos que ya existieron y su capacidad predictiva depende de que las condiciones se mantengan. Un cambio de precio, de segmento objetivo o de producto rompe la comparabilidad. Registrar esos cambios junto con las cohortes es lo que permite interpretar después las diferencias.

**Frontera declarada.** Las cohortes recientes tienen poca historia y sus proyecciones son inciertas. Comparar sólo en hitos con datos completos evita conclusiones falsas. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Retener con castigos contractuales en lugar de valor entregado y dañar reputación.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar análisis de cohortes no consiste en sumar definiciones. Empieza por **cohorte**, contrasta **seguimiento longitudinal** con **efecto de mezcla**, incorpora **mejora entre cohortes** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | El análisis de cohortes como corrección al promedio que esconde la mezcla | El capítulo sobre cohortes y segmentación | ¿Qué debería observarse en **cohorte** si aquí opera «el análisis de cohortes como corrección al promedio que esconde la mezcla»? ¿Y qué observación lo desmentiría en este caso? |
| Peter Fader — *Customer Centricity* (2020, 2.ª ed.) | Recencia, frecuencia y valor como base de segmentación conductual | Los capítulos sobre segmentación por comportamiento | ¿Qué debería observarse en **seguimiento longitudinal** si aquí opera «recencia, frecuencia y valor como base de segmentación conductual»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La distinción entre correlación observada y causalidad y qué exige cada una | Los capítulos sobre inferencia y sesgo | ¿Qué debería observarse en **efecto de mezcla** si aquí opera «la distinción entre correlación observada y causalidad y qué exige cada una»? ¿Y qué observación lo desmentiría en este caso? |
| Avinash Kaushik — *Web Analytics 2.0* (2009) | La segmentación como condición para que un promedio signifique algo | El capítulo sobre segmentación de datos | ¿Qué debería observarse en **mejora entre cohortes** si aquí opera «la segmentación como condición para que un promedio signifique algo»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El promedio de retención de Ruta Andina se mantiene estable. Al analizar por cohorte se ve que las cohortes recientes retienen peor y el promedio se sostiene por las antiguas.

**Paso 1 — Definir el criterio de cohorte y la métrica a seguir.** El equipo escribe primero el supuesto asociado a **cohorte** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **retención por cohorte en el mismo hito** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Construir la tabla de cohortes con datos propios.** El trabajo aquí es separar lo observado de lo inferido sobre **seguimiento longitudinal**. La evidencia que ordena la discusión es **ingreso acumulado por cohorte**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Comparar cohortes sucesivas en el mismo hito.** El riesgo de este paso es cerrar demasiado rápido alrededor de **efecto de mezcla**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **tendencia entre cohortes** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Atribuir las diferencias a cambios conocidos.** Con **mejora entre cohortes** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **retención por cohorte en el mismo hito** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Usar el análisis para evaluar intervenciones.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **cohorte**. **ingreso acumulado por cohorte** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **cohorte** | Grupo de clientes que comparte el periodo de incorporación | Cuando **retención por cohorte en el mismo hito** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **seguimiento longitudinal** | Observación del mismo grupo a lo largo de varios periodos | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Las cohortes recientes tienen poca historia y sus proyecciones son inciertas. Comparar sólo en hitos con datos completos evita conclusiones falsas.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre análisis de cohortes |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Customer success manager, Account manager y Head of CS. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El promedio de retención de Ruta Andina se mantiene estable. Al analizar por cohorte se ve que las cohortes recientes retienen peor y el promedio se sostiene por las antiguas.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir el criterio de cohorte y la métrica a seguir → construir la tabla de cohortes con datos propios → comparar cohortes sucesivas en el mismo hito → atribuir las diferencias a cambios conocidos → usar el análisis para evaluar intervenciones** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **retención por cohorte en el mismo hito**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Lean Analytics* y la de *Customer Centricity*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **cohorte** y **seguimiento longitudinal** como sinónimos | Se perdió la distinción entre «grupo de clientes que comparte el periodo de incorporación» y «observación del mismo grupo a lo largo de varios periodos» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «usar el análisis para evaluar intervenciones» | Se saltó «definir el criterio de cohorte y la métrica a seguir»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **retención por cohorte en el mismo hito** | La métrica local reemplazó al resultado del sistema | Contrástala con **tendencia entre cohortes** y explicita el costo de oportunidad. |
| Evaluar retención con promedios agregados | Error específico de esta clase | Compara cohortes sucesivas en el mismo hito de antigüedad. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **cohorte** y **seguimiento longitudinal** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **efecto de mezcla** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir el criterio de cohorte y la métrica a seguir» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **retención por cohorte en el mismo hito** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Las cohortes recientes tienen poca historia y sus proyecciones son inciertas. Comparar sólo en hitos con datos completos evita conclusiones falsas»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **efecto de mezcla** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **retención por cohorte en el mismo hito**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Lean Analytics* y *Web Analytics 2.0*. |
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

Guarda en `evidence/P18-C09-cohortes/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **retención por cohorte en el mismo hito**, **ingreso acumulado por cohorte** y **tendencia entre cohortes** con fuente, ventana y lectura prohibida.
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

- Alistair Croll y Benjamin Yoskovitz — [*Lean Analytics*](https://openlibrary.org/isbn/9781449335670) (2013) · ISBN 9781449335670 — **aporta a esta clase:** el análisis de cohortes como corrección al promedio que esconde la mezcla. **Dónde buscarlo:** el capítulo sobre cohortes y segmentación. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Peter Fader — [*Customer Centricity*](https://openlibrary.org/isbn/9781613631447) (2020, 2.ª ed.) · ISBN 9781613631447 — **aporta a esta clase:** recencia, frecuencia y valor como base de segmentación conductual. **Dónde buscarlo:** los capítulos sobre segmentación por comportamiento. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) · ISBN 9781449374280 — **aporta a esta clase:** la distinción entre correlación observada y causalidad y qué exige cada una. **Dónde buscarlo:** los capítulos sobre inferencia y sesgo. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Avinash Kaushik — [*Web Analytics 2.0*](https://openlibrary.org/isbn/9780470596425) (2009) · ISBN 9780470596425 — **aporta a esta clase:** la segmentación como condición para que un promedio signifique algo. **Dónde buscarlo:** el capítulo sobre segmentación de datos. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 08 · Retención](class-08-retention.md) · [Índice de la parte](README.md) · [Clase 10 · Renovación](class-10-renewal.md) →
