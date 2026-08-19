# Clase 14.10 — CPA, CAC y ROAS

Clase 10 de 14 de la parte [14 — Publicidad y performance marketing](README.md), de nivel Adquisición. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 14.09, *CTR, CPC y CPM*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de costo de adquisición completo por canal con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** Los seis modelos de negocio y las métricas que cambian entre ellos — Alistair Croll y Benjamin Yoskovitz. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

El costo por adquisición mide el gasto por conversión de campaña; el costo de adquisición de cliente incluye todo el gasto comercial, incluidos sueldos; el retorno sobre inversión publicitaria compara ingreso atribuido con gasto de medios. Los tres se confunden con frecuencia y esa confusión produce decisiones caras: un retorno publicitario alto puede coexistir con una economía unitaria negativa.

Antes de cualquier herramienta, esta clase obliga a nombrar qué cambiaría si el análisis fuese correcto. La parte 14 busca **invertir en medios pagados con control de costo, calidad y riesgo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **CPA, CAC y ROAS** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué unidad de resultado estoy comprando y a qué costo marginal deja de tener sentido?

Los conceptos que estructuran la sesión son **costo por adquisición**, **costo de adquisición de cliente**, **retorno sobre inversión publicitaria** y **ingreso incremental**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `costo por adquisición`, `costo de adquisición de cliente`, `retorno sobre inversión publicitaria` y `ingreso incremental` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Publicidad y performance marketing**.
3. **Aplicar** la secuencia **definir el alcance de cada métrica por escrito → verificar qué ingreso es incremental y cuál no → calcular el costo de adquisición completo por canal → contrastar con margen y periodo de recuperación → decidir escalamiento sólo con economía verificada** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **costo de adquisición completo por canal**, **proporción de ingreso incremental** y **relación valor de vida a costo de adquisición** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **costo por adquisición** y **costo de adquisición de cliente** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **costo de adquisición completo por canal**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **costo por adquisición** | gasto de medios dividido por conversiones registradas de la campaña | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **costo de adquisición de cliente** | gasto total de marketing y ventas, incluidos sueldos, por cliente nuevo | Da un hecho compatible con la definición y otro que la refute. |
| **retorno sobre inversión publicitaria** | ingreso atribuido dividido por gasto de medios | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **ingreso incremental** | ingreso que no habría ocurrido sin la inversión publicitaria | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir el alcance de cada métrica por escrito → 2. verificar qué ingreso es incremental y cuál no → 3. calcular el costo de adquisición completo por canal → 4. contrastar con margen y periodo de recuperación → 5. decidir escalamiento sólo con economía verificada
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** El ingreso atribuido depende del modelo de atribución y de la ventana. Comparar retornos entre periodos con configuraciones distintas no tiene sentido.

## 📖 Desarrollo

### 1. Costo por adquisición: mecanismo central

**Costo por adquisición** se entiende aquí como **gasto de medios dividido por conversiones registradas de la campaña**.

El costo por adquisición y el costo de adquisición de cliente no son lo mismo, y confundirlos es el error más caro de este bloque. El primero mide el costo de una conversión definida en la plataforma —un formulario, una descarga—; el segundo, el costo de conseguir un cliente que paga, con todos los costos incluidos.

**De dónde viene esta afirmación.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) aporta la idea que sostiene este bloque: los seis modelos de negocio y las métricas que cambian entre ellos. Búscala en la parte sobre modelos de negocio. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «costo de adquisición completo por canal» debería moverse cuando cambie **costo por adquisición**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **costo de adquisición de cliente**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Costo de adquisición de cliente: frontera conceptual y error de clasificación

**Definición operacional:** gasto total de marketing y ventas, incluidos sueldos, por cliente nuevo. Su valor está en distinguirlo de **costo por adquisición**.

El retorno sobre inversión publicitaria mide ingreso sobre gasto en medios y omite el resto de la estructura comercial. Una campaña con retorno aparentemente excelente puede ser deficitaria una vez incorporados sueldos, herramientas y costo de servir. Presentarlo como métrica de rentabilidad es inexacto y frecuente.

**Contraste bibliográfico.** Avinash Kaushik — *Web Analytics 2.0* (2009) aporta aquí una distinción concreta: el plan de medición que va de la decisión a la métrica y no al revés (los capítulos sobre estrategia de medición). Formula dos mini-casos: uno que satisface la definición de **costo de adquisición de cliente** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «verificar qué ingreso es incremental y cuál no», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Retorno sobre inversión publicitaria: operacionalización y medición

**Retorno sobre inversión publicitaria** significa **ingreso atribuido dividido por gasto de medios**.

El ingreso atribuido depende del modelo de atribución elegido, y por eso dos informes pueden reportar cifras distintas del mismo periodo sin que ninguno esté equivocado. La ficha debe declarar el modelo y la ventana, y toda comparación entre periodos debe verificar que ambos usaron la misma convención.

Ficha de medición obligatoria para **costo de adquisición completo por canal**: `gasto total atribuible dividido por clientes nuevos del canal`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) pone una condición sobre la medición: los riesgos de optimizar una métrica sustituta en lugar del resultado (los capítulos sobre selección de métricas). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Ingreso incremental: trade-offs y efectos de segundo orden

**Definición:** ingreso que no habría ocurrido sin la inversión publicitaria.

Optimizar por costo por adquisición inmediato favorece la captura de demanda existente y penaliza la generación de demanda futura, cuyo efecto no aparece en la ventana de atribución. Esa asimetría empuja el presupuesto hacia el corto plazo de forma sistemática, y corregirla exige una decisión explícita de dirección.

**Lo que aporta la fuente.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta el criterio para pesar el intercambio: el marco de valor esperado que combina probabilidad y consecuencia económica (el capítulo sobre valor esperado). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **relación valor de vida a costo de adquisición** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **ingreso incremental** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «decidir escalamiento sólo con economía verificada», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La rentabilidad real de la adquisición sólo se conoce comparando el costo con el valor del cliente en el tiempo, que es una proyección con supuestos. Presentar la relación entre ambos como un hecho establecido oculta esa incertidumbre. La versión honesta muestra el supuesto de permanencia y su sensibilidad.

**Frontera declarada.** El ingreso atribuido depende del modelo de atribución y de la ventana. Comparar retornos entre periodos con configuraciones distintas no tiene sentido. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Atribuirse demanda existente, inflar el retorno y decidir presupuesto sobre una ilusión.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar CPA, CAC y ROAS no consiste en sumar definiciones. Empieza por **costo por adquisición**, contrasta **costo de adquisición de cliente** con **retorno sobre inversión publicitaria**, incorpora **ingreso incremental** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | Los seis modelos de negocio y las métricas que cambian entre ellos | La parte sobre modelos de negocio | ¿Qué debería observarse en **costo por adquisición** si aquí opera «los seis modelos de negocio y las métricas que cambian entre ellos»? ¿Y qué observación lo desmentiría en este caso? |
| Avinash Kaushik — *Web Analytics 2.0* (2009) | El plan de medición que va de la decisión a la métrica y no al revés | Los capítulos sobre estrategia de medición | ¿Qué debería observarse en **costo de adquisición de cliente** si aquí opera «el plan de medición que va de la decisión a la métrica y no al revés»? ¿Y qué observación lo desmentiría en este caso? |
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | Los riesgos de optimizar una métrica sustituta en lugar del resultado | Los capítulos sobre selección de métricas | ¿Qué debería observarse en **retorno sobre inversión publicitaria** si aquí opera «los riesgos de optimizar una métrica sustituta en lugar del resultado»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | El marco de valor esperado que combina probabilidad y consecuencia económica | El capítulo sobre valor esperado | ¿Qué debería observarse en **ingreso incremental** si aquí opera «el marco de valor esperado que combina probabilidad y consecuencia económica»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El retorno publicitario reportado por Ruta Andina es 6,1 e incluye compras de clientes que ya eran clientes y que habrían comprado igual.

**Paso 1 — Definir el alcance de cada métrica por escrito.** El equipo escribe primero el supuesto asociado a **costo por adquisición** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **costo de adquisición completo por canal** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Verificar qué ingreso es incremental y cuál no.** El trabajo aquí es separar lo observado de lo inferido sobre **costo de adquisición de cliente**. La evidencia que ordena la discusión es **proporción de ingreso incremental**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Calcular el costo de adquisición completo por canal.** El riesgo de este paso es cerrar demasiado rápido alrededor de **retorno sobre inversión publicitaria**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **relación valor de vida a costo de adquisición** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Contrastar con margen y periodo de recuperación.** Con **ingreso incremental** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **costo de adquisición completo por canal** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Decidir escalamiento sólo con economía verificada.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **costo por adquisición**. **proporción de ingreso incremental** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **costo por adquisición** | Gasto de medios dividido por conversiones registradas de la campaña | Cuando **costo de adquisición completo por canal** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **costo de adquisición de cliente** | Gasto total de marketing y ventas, incluidos sueldos, por cliente nuevo | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** El ingreso atribuido depende del modelo de atribución y de la ventana. Comparar retornos entre periodos con configuraciones distintas no tiene sentido.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre CPA, CAC y ROAS |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Performance marketer, Media buyer y Growth marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El retorno publicitario reportado por Ruta Andina es 6,1 e incluye compras de clientes que ya eran clientes y que habrían comprado igual.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir el alcance de cada métrica por escrito → verificar qué ingreso es incremental y cuál no → calcular el costo de adquisición completo por canal → contrastar con margen y periodo de recuperación → decidir escalamiento sólo con economía verificada** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **costo de adquisición completo por canal**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Lean Analytics* y la de *Web Analytics 2.0*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **costo por adquisición** y **costo de adquisición de cliente** como sinónimos | Se perdió la distinción entre «gasto de medios dividido por conversiones registradas de la campaña» y «gasto total de marketing y ventas, incluidos sueldos, por cliente nuevo» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «decidir escalamiento sólo con economía verificada» | Se saltó «definir el alcance de cada métrica por escrito»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **costo de adquisición completo por canal** | La métrica local reemplazó al resultado del sistema | Contrástala con **relación valor de vida a costo de adquisición** y explicita el costo de oportunidad. |
| Reportar retorno publicitario incluyendo ingreso no incremental | Error específico de esta clase | Separa clientes nuevos de recurrentes y estima incrementalidad antes de reportar retorno. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **costo por adquisición** y **costo de adquisición de cliente** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **retorno sobre inversión publicitaria** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir el alcance de cada métrica por escrito» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **costo de adquisición completo por canal** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «El ingreso atribuido depende del modelo de atribución y de la ventana. Comparar retornos entre periodos con configuraciones distintas no tiene sentido»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **retorno sobre inversión publicitaria** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **costo de adquisición completo por canal**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Lean Analytics* y *Data Science for Business*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Atribuirse demanda existente, inflar el retorno y decidir presupuesto sobre una ilusión.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, comprueba la norma en su texto vigente. Los enlaces van al texto completo publicado por la Biblioteca del Congreso Nacional; son gratuitos y no hace falta creerle a este material.

- **Consumo y comercio.** [Ley 19.496](https://www.bcn.cl/leychile/navegar?idNorma=61438) — *Establece normas sobre protección de los derechos de los consumidores* (Ministerio de Economía, Fomento y Reconstrucción), y su reglamento de comercio electrónico, [Decreto 6/2021](https://www.bcn.cl/leychile/navegar?idNorma=1165504) — *Aprueba reglamento de comercio electrónico* (Ministerio de Economía, Fomento y Turismo).
- **Datos personales.** [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales* (Ministerio Secretaría General de la Presidencia), que sustituye progresivamente a [Ley 19.628](https://www.bcn.cl/leychile/navegar?idNorma=141599) — *Sobre protección de la vida privada* (Ministerio Secretaría General de la Presidencia).
- **Derecho a retracto.** [Decreto 52/2024](https://www.bcn.cl/leychile/navegar?idNorma=1206144) — *Aprueba reglamento que regula la forma y condiciones en que los proveedores deberán comunicar la exclusión del derecho a retracto y los bienes en que excepcionalmente y por su naturaleza procederá tal exclusión* (Ministerio de Economía, Fomento y Turismo).

Dentro del repositorio, el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) ordena qué norma aplica a cada decisión comercial, [datos personales y ética](../../docs/DATOS-PERSONALES-Y-ETICA.md) desarrolla el tratamiento de datos y [fuentes oficiales](../../docs/FUENTES-OFICIALES.md) lista los organismos con su fecha de consulta. Ninguno de esos documentos reemplaza al texto legal.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P14-C10-cpa-cac-y-roas/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **costo de adquisición completo por canal**, **proporción de ingreso incremental** y **relación valor de vida a costo de adquisición** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **plan de performance con estructura de campañas, presupuestos, medición y salvaguardas**.

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

- Alistair Croll y Benjamin Yoskovitz — [*Lean Analytics*](https://openlibrary.org/isbn/9781449335670) (2013) · ISBN 9781449335670 — **aporta a esta clase:** los seis modelos de negocio y las métricas que cambian entre ellos. **Dónde buscarlo:** la parte sobre modelos de negocio. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Avinash Kaushik — [*Web Analytics 2.0*](https://openlibrary.org/isbn/9780470596425) (2009) · ISBN 9780470596425 — **aporta a esta clase:** el plan de medición que va de la decisión a la métrica y no al revés. **Dónde buscarlo:** los capítulos sobre estrategia de medición. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Ron Kohavi, Diane Tang y Ya Xu — [*Trustworthy Online Controlled Experiments*](https://openlibrary.org/isbn/9781108601375) (2020) · ISBN 9781108601375 — **aporta a esta clase:** los riesgos de optimizar una métrica sustituta en lugar del resultado. **Dónde buscarlo:** los capítulos sobre selección de métricas. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) · ISBN 9781449374280 — **aporta a esta clase:** el marco de valor esperado que combina probabilidad y consecuencia económica. **Dónde buscarlo:** el capítulo sobre valor esperado. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 09 · CTR, CPC y CPM](class-09-ctr-cpc-y-cpm.md) · [Índice de la parte](README.md) · [Clase 11 · Tracking y atribución](class-11-tracking-y-atribucion.md) →
