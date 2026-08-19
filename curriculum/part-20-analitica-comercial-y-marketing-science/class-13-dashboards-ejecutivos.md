# Clase 20.13 — Dashboards ejecutivos

Clase 13 de 14 de la parte [20 — Analítica comercial y marketing science](README.md), de nivel Crecimiento y analítica. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 20.12, *Fundamentos de marketing mix modeling*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de tiempo de lectura con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** Las cuatro perspectivas: financiera, cliente, procesos y aprendizaje — Robert S. Kaplan y David P. Norton. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Un tablero ejecutivo debe responder en un minuto: cómo vamos frente al plan, qué cambió y qué decisión se requiere. Su diseño exige jerarquía, contexto —comparación con periodo anterior y con meta— y rangos de variación esperada. Un tablero sin contexto convierte cada fluctuación normal en una alarma y agota la capacidad de atención de la dirección.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 20 busca **sostener decisiones de ingreso con métricas correctamente construidas**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **dashboards ejecutivos** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Esta cifra mide lo que creo que mide, y qué decisión cambiaría si estuviera equivocada?

Los conceptos que estructuran la sesión son **contexto comparativo**, **jerarquía visual**, **banda de variación esperada** y **decisión requerida**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `contexto comparativo`, `jerarquía visual`, `banda de variación esperada` y `decisión requerida` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Analítica comercial y marketing science**.
3. **Aplicar** la secuencia **definir las decisiones que el tablero debe habilitar → seleccionar pocos indicadores con contexto → establecer bandas de variación esperada → señalar explícitamente qué requiere decisión → verificar el uso real con la dirección** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **tiempo de lectura**, **indicadores con banda definida** y **decisiones tomadas con el tablero** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **contexto comparativo** y **jerarquía visual** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **tiempo de lectura**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **contexto comparativo** | referencia frente a periodo anterior, meta o límite esperado | Construye un caso límite donde el concepto se confunde con el anterior. |
| **jerarquía visual** | orden que refleja la importancia de las decisiones que informa | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **banda de variación esperada** | rango dentro del cual la fluctuación no requiere acción | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **decisión requerida** | acción que el tablero solicita explícitamente cuando algo se desvía | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir las decisiones que el tablero debe habilitar → 2. seleccionar pocos indicadores con contexto → 3. establecer bandas de variación esperada → 4. señalar explícitamente qué requiere decisión → 5. verificar el uso real con la dirección
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un tablero ejecutivo no reemplaza el análisis: señala dónde mirar. Las decisiones complejas requieren un documento con contexto y alternativas.

## 📖 Desarrollo

### 1. Contexto comparativo: mecanismo central

**Contexto comparativo** se entiende aquí como **referencia frente a periodo anterior, meta o límite esperado**.

Un tablero ejecutivo tiene un propósito distinto del operativo: no sirve para gestionar el día sino para detectar desviaciones que requieren decisión de dirección. Esa diferencia determina qué contiene, con qué frecuencia se actualiza y con qué nivel de agregación se presenta.

**De dónde viene esta afirmación.** Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) aporta la idea que sostiene este bloque: las cuatro perspectivas: financiera, cliente, procesos y aprendizaje. Búscala en los capítulos que presentan el cuadro de mando. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «tiempo de lectura» debería moverse cuando cambie **contexto comparativo**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **jerarquía visual**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Jerarquía visual: frontera conceptual y error de clasificación

**Definición operacional:** orden que refleja la importancia de las decisiones que informa. Su valor está en distinguirlo de **contexto comparativo**.

El contexto comparativo es lo que convierte un número en información: periodo anterior, meta, banda de variación esperada. Un valor solo no permite saber si hay que actuar. Incorporar límites calculados a partir de la propia variación histórica evita que la dirección reaccione ante fluctuaciones normales.

**Contraste bibliográfico.** Donald J. Wheeler — *Understanding Variation* (2000) aporta aquí una distinción concreta: el error de comparar dos puntos consecutivos y llamarlo tendencia (los capítulos sobre interpretación de series). Formula dos mini-casos: uno que satisface la definición de **jerarquía visual** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «seleccionar pocos indicadores con contexto», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Banda de variación esperada: operacionalización y medición

**Banda de variación esperada** significa **rango dentro del cual la fluctuación no requiere acción**.

La decisión requerida debería estar explícita en el tablero: qué se espera que decida quien lo mira. Un tablero que sólo informa produce reuniones de revisión sin acuerdos. Incluir, junto a cada desviación relevante, la decisión pendiente y su responsable transforma el instrumento.

Ficha de medición obligatoria para **tiempo de lectura**: `minutos que tarda un ejecutivo en identificar el estado y las decisiones`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Avinash Kaushik — *Web Analytics 2.0* (2009) pone una condición sobre la medición: la prueba del «¿y entonces qué?» aplicada tres veces a cada informe (los capítulos sobre informes accionables). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Decisión requerida: trade-offs y efectos de segundo orden

**Definición:** acción que el tablero solicita explícitamente cuando algo se desvía.

Más información entrega contexto y diluye la atención de quien tiene poco tiempo; menos concentra y puede ocultar. Para dirección, la regla práctica es una vista que se lea en pocos minutos, con capacidad de profundizar bajo demanda. Un tablero ejecutivo que requiere explicación no cumple su función.

**Lo que aporta la fuente.** Andrew S. Grove — *High Output Management* (1983) aporta el criterio para pesar el intercambio: los indicadores adelantados y pareados que permiten corregir a tiempo (los capítulos sobre medición en la producción). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **decisiones tomadas con el tablero** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **decisión requerida** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «verificar el uso real con la dirección», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Los tableros heredan la calidad de sus fuentes y la de las definiciones. Un indicador construido sobre un campo inconsistente produce una cifra precisa e inexacta que la dirección usará como si fuera confiable. Documentar la definición y la fuente de cada indicador es parte del tablero y no un anexo.

**Frontera declarada.** Un tablero ejecutivo no reemplaza el análisis: señala dónde mirar. Las decisiones complejas requieren un documento con contexto y alternativas. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar dashboards ejecutivos no consiste en sumar definiciones. Empieza por **contexto comparativo**, contrasta **jerarquía visual** con **banda de variación esperada**, incorpora **decisión requerida** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) | Las cuatro perspectivas: financiera, cliente, procesos y aprendizaje | Los capítulos que presentan el cuadro de mando | ¿Qué debería observarse en **contexto comparativo** si aquí opera «las cuatro perspectivas: financiera, cliente, procesos y aprendizaje»? ¿Y qué observación lo desmentiría en este caso? |
| Donald J. Wheeler — *Understanding Variation* (2000) | El error de comparar dos puntos consecutivos y llamarlo tendencia | Los capítulos sobre interpretación de series | ¿Qué debería observarse en **jerarquía visual** si aquí opera «el error de comparar dos puntos consecutivos y llamarlo tendencia»? ¿Y qué observación lo desmentiría en este caso? |
| Avinash Kaushik — *Web Analytics 2.0* (2009) | La prueba del «¿y entonces qué?» aplicada tres veces a cada informe | Los capítulos sobre informes accionables | ¿Qué debería observarse en **banda de variación esperada** si aquí opera «la prueba del «¿y entonces qué?» aplicada tres veces a cada informe»? ¿Y qué observación lo desmentiría en este caso? |
| Andrew S. Grove — *High Output Management* (1983) | Los indicadores adelantados y pareados que permiten corregir a tiempo | Los capítulos sobre medición en la producción | ¿Qué debería observarse en **decisión requerida** si aquí opera «los indicadores adelantados y pareados que permiten corregir a tiempo»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El tablero que Ruta Andina presenta al directorio tiene 18 gráficos sin metas ni comparaciones. La reunión se consume preguntando si cada variación es buena o mala.

**Paso 1 — Definir las decisiones que el tablero debe habilitar.** El equipo escribe primero el supuesto asociado a **contexto comparativo** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **tiempo de lectura** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Seleccionar pocos indicadores con contexto.** El trabajo aquí es separar lo observado de lo inferido sobre **jerarquía visual**. La evidencia que ordena la discusión es **indicadores con banda definida**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Establecer bandas de variación esperada.** El riesgo de este paso es cerrar demasiado rápido alrededor de **banda de variación esperada**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **decisiones tomadas con el tablero** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Señalar explícitamente qué requiere decisión.** Con **decisión requerida** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **tiempo de lectura** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Verificar el uso real con la dirección.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **contexto comparativo**. **indicadores con banda definida** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **contexto comparativo** | Referencia frente a periodo anterior, meta o límite esperado | Cuando **tiempo de lectura** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **jerarquía visual** | Orden que refleja la importancia de las decisiones que informa | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un tablero ejecutivo no reemplaza el análisis: señala dónde mirar. Las decisiones complejas requieren un documento con contexto y alternativas.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre dashboards ejecutivos |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing analyst, Revenue analyst y Data-driven marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El tablero que Ruta Andina presenta al directorio tiene 18 gráficos sin metas ni comparaciones. La reunión se consume preguntando si cada variación es buena o mala.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir las decisiones que el tablero debe habilitar → seleccionar pocos indicadores con contexto → establecer bandas de variación esperada → señalar explícitamente qué requiere decisión → verificar el uso real con la dirección** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **tiempo de lectura**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *The Balanced Scorecard* y la de *Understanding Variation*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **contexto comparativo** y **jerarquía visual** como sinónimos | Se perdió la distinción entre «referencia frente a periodo anterior, meta o límite esperado» y «orden que refleja la importancia de las decisiones que informa» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «verificar el uso real con la dirección» | Se saltó «definir las decisiones que el tablero debe habilitar»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **tiempo de lectura** | La métrica local reemplazó al resultado del sistema | Contrástala con **decisiones tomadas con el tablero** y explicita el costo de oportunidad. |
| Presentar cifras sin meta ni comparación | Error específico de esta clase | Agrega contexto comparativo y banda de variación esperada a cada indicador. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **contexto comparativo** y **jerarquía visual** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **banda de variación esperada** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir las decisiones que el tablero debe habilitar» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **tiempo de lectura** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un tablero ejecutivo no reemplaza el análisis: señala dónde mirar. Las decisiones complejas requieren un documento con contexto y alternativas»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **banda de variación esperada** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **tiempo de lectura**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *The Balanced Scorecard* y *High Output Management*. |
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

Guarda en `evidence/P20-C13-dashboards-ejecutivos/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **tiempo de lectura**, **indicadores con banda definida** y **decisiones tomadas con el tablero** con fuente, ventana y lectura prohibida.
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

- Robert S. Kaplan y David P. Norton — [*The Balanced Scorecard*](https://openlibrary.org/isbn/9780875846514) (1996) · ISBN 9780875846514 — **aporta a esta clase:** las cuatro perspectivas: financiera, cliente, procesos y aprendizaje. **Dónde buscarlo:** los capítulos que presentan el cuadro de mando. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Donald J. Wheeler — [*Understanding Variation*](https://openlibrary.org/isbn/9780945320531) (2000) · ISBN 9780945320531 — **aporta a esta clase:** el error de comparar dos puntos consecutivos y llamarlo tendencia. **Dónde buscarlo:** los capítulos sobre interpretación de series. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Avinash Kaushik — [*Web Analytics 2.0*](https://openlibrary.org/isbn/9780470596425) (2009) · ISBN 9780470596425 — **aporta a esta clase:** la prueba del «¿y entonces qué?» aplicada tres veces a cada informe. **Dónde buscarlo:** los capítulos sobre informes accionables. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Andrew S. Grove — [*High Output Management*](https://openlibrary.org/isbn/9780394532349) (1983) · ISBN 9780394532349 — **aporta a esta clase:** los indicadores adelantados y pareados que permiten corregir a tiempo. **Dónde buscarlo:** los capítulos sobre medición en la producción. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 12 · Fundamentos de marketing mix modeling](class-12-marketing-mix-modeling-fundamentos.md) · [Índice de la parte](README.md) · [Clase 14 · Caso analítico integral](class-14-caso-analitico-integral.md) →
