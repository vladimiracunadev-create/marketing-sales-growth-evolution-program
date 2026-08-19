# Clase 14.07 — LinkedIn Ads: arquitectura conceptual

Clase 7 de 14 de la parte [14 — Publicidad y performance marketing](README.md), de nivel Adquisición. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 14.06, *Meta Ads: arquitectura conceptual*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de costo por oportunidad calificada con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** Los tipos de coincidencia y las exclusiones como control del gasto — Brad Geddes. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La publicidad profesional permite segmentar por cargo, industria y tamaño, lo que la hace atractiva para B2B y también cara por impresión. Su uso racional exige tickets que sostengan ese costo y una propuesta pertinente para el rol. Usarla para captar leads con un recurso genérico produce el costo por lead más alto del mercado sin mejor calidad.

Esta sesión distingue lo que se sabe, lo que se supone y lo que todavía no se ha medido. La parte 14 busca **invertir en medios pagados con control de costo, calidad y riesgo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **linkedIn Ads: arquitectura conceptual** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué unidad de resultado estoy comprando y a qué costo marginal deja de tener sentido?

Los conceptos que estructuran la sesión son **segmentación profesional**, **costo por impresión elevado**, **pertinencia por rol** y **umbral de viabilidad**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `segmentación profesional`, `costo por impresión elevado`, `pertinencia por rol` y `umbral de viabilidad` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Publicidad y performance marketing**.
3. **Aplicar** la secuencia **verificar que el ticket sostiene el costo del canal → segmentar por rol con criterios verificables → construir el mensaje desde la preocupación del cargo → medir hasta oportunidad calificada y no hasta lead → comparar con canales alternativos antes de escalar** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **costo por oportunidad calificada**, **precisión de la segmentación** y **comparación con canales alternativos** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **segmentación profesional** y **costo por impresión elevado** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **costo por oportunidad calificada**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **segmentación profesional** | selección por cargo, función, industria y tamaño de organización | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **costo por impresión elevado** | precio característico del canal que exige tickets altos para ser rentable | Construye un caso límite donde el concepto se confunde con el anterior. |
| **pertinencia por rol** | correspondencia entre el mensaje y las preocupaciones del cargo seleccionado | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **umbral de viabilidad** | ticket mínimo que hace rentable el canal dada su estructura de costo | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. verificar que el ticket sostiene el costo del canal → 2. segmentar por rol con criterios verificables → 3. construir el mensaje desde la preocupación del cargo → 4. medir hasta oportunidad calificada y no hasta lead → 5. comparar con canales alternativos antes de escalar
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Los datos de perfil profesional son declarados por los usuarios y pueden estar desactualizados. La segmentación no garantiza que la persona ocupe hoy ese cargo.

## 📖 Desarrollo

### 1. Segmentación profesional: mecanismo central

**Segmentación profesional** se entiende aquí como **selección por cargo, función, industria y tamaño de organización**.

La publicidad en redes profesionales tiene un costo por impresión considerablemente mayor y una segmentación por rol y organización que ninguna otra ofrece. Esa combinación define su uso correcto: campañas dirigidas a públicos pequeños y de alto valor, donde el costo por contacto se justifica por el tamaño potencial del negocio.

**De dónde viene esta afirmación.** Brad Geddes — *Advanced Google AdWords* (2014, 3.ª ed.) aporta la idea que sostiene este bloque: los tipos de coincidencia y las exclusiones como control del gasto. Búscala en los capítulos sobre palabras clave y concordancias. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «costo por oportunidad calificada» debería moverse cuando cambie **segmentación profesional**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **costo por impresión elevado**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Costo por impresión elevado: frontera conceptual y error de clasificación

**Definición operacional:** precio característico del canal que exige tickets altos para ser rentable. Su valor está en distinguirlo de **segmentación profesional**.

La pertinencia por rol es la ventaja del canal y también su trampa: se puede segmentar con tanta precisión que la audiencia resultante es demasiado pequeña para sostener una campaña. Existe un umbral mínimo de audiencia por debajo del cual el sistema no puede optimizar y el costo se dispara.

**Contraste bibliográfico.** Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) aporta aquí una distinción concreta: el modelo de contribución de canal a la conversión (los capítulos sobre estrategia de canales). Formula dos mini-casos: uno que satisface la definición de **costo por impresión elevado** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «segmentar por rol con criterios verificables», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Pertinencia por rol: operacionalización y medición

**Pertinencia por rol** significa **correspondencia entre el mensaje y las preocupaciones del cargo seleccionado**.

El costo por oportunidad, y no el costo por clic, es la métrica que decide si el canal funciona. Comparar su costo por clic con el de otras plataformas siempre lo hará ver mal. La comparación válida es contra el valor del negocio que produce, y esa comparación exige conectar la campaña con el sistema comercial.

Ficha de medición obligatoria para **costo por oportunidad calificada**: `gasto del canal dividido por oportunidades calificadas originadas`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Brent Adamson y Matthew Dixon — *The Challenger Customer* (2015) pone una condición sobre la medición: el consenso interno como principal obstáculo, por encima de la persuasión individual (los capítulos iniciales sobre el problema del consenso). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Umbral de viabilidad: trade-offs y efectos de segundo orden

**Definición:** ticket mínimo que hace rentable el canal dada su estructura de costo.

Ampliar la segmentación reduce el costo unitario y diluye la pertinencia que justificaba usar este canal en particular. Restringirla mantiene la precisión y encarece. La decisión debe considerar que la ventaja competitiva del canal está en la precisión: si se renuncia a ella, existen alternativas más baratas.

**Lo que aporta la fuente.** Avinash Kaushik — *Web Analytics 2.0* (2009) aporta el criterio para pesar el intercambio: la distinción entre métricas de vanidad y métricas accionables (los capítulos sobre selección de métricas). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **comparación con canales alternativos** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **umbral de viabilidad** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «comparar con canales alternativos antes de escalar», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

En decisiones con comité, un contacto individual generado por publicidad es apenas el inicio de un proceso largo. Evaluar la campaña con la conversión inmediata subestima su contribución; atribuirle todo el negocio la sobreestima. La lectura razonable la trata como generación de conversaciones y no como canal de cierre.

**Frontera declarada.** Los datos de perfil profesional son declarados por los usuarios y pueden estar desactualizados. La segmentación no garantiza que la persona ocupe hoy ese cargo. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Atribuirse demanda existente, inflar el retorno y decidir presupuesto sobre una ilusión.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar linkedIn Ads: arquitectura conceptual no consiste en sumar definiciones. Empieza por **segmentación profesional**, contrasta **costo por impresión elevado** con **pertinencia por rol**, incorpora **umbral de viabilidad** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Brad Geddes — *Advanced Google AdWords* (2014, 3.ª ed.) | Los tipos de coincidencia y las exclusiones como control del gasto | Los capítulos sobre palabras clave y concordancias | ¿Qué debería observarse en **segmentación profesional** si aquí opera «los tipos de coincidencia y las exclusiones como control del gasto»? ¿Y qué observación lo desmentiría en este caso? |
| Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) | El modelo de contribución de canal a la conversión | Los capítulos sobre estrategia de canales | ¿Qué debería observarse en **costo por impresión elevado** si aquí opera «el modelo de contribución de canal a la conversión»? ¿Y qué observación lo desmentiría en este caso? |
| Brent Adamson y Matthew Dixon — *The Challenger Customer* (2015) | El consenso interno como principal obstáculo, por encima de la persuasión individual | Los capítulos iniciales sobre el problema del consenso | ¿Qué debería observarse en **pertinencia por rol** si aquí opera «el consenso interno como principal obstáculo, por encima de la persuasión individual»? ¿Y qué observación lo desmentiría en este caso? |
| Avinash Kaushik — *Web Analytics 2.0* (2009) | La distinción entre métricas de vanidad y métricas accionables | Los capítulos sobre selección de métricas | ¿Qué debería observarse en **umbral de viabilidad** si aquí opera «la distinción entre métricas de vanidad y métricas accionables»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina gastó CLP 1,2 millones en el canal para promocionar un ebook genérico. Obtuvo 22 leads a CLP 54.000 cada uno y ninguna oportunidad calificada.

**Paso 1 — Verificar que el ticket sostiene el costo del canal.** El equipo escribe primero el supuesto asociado a **segmentación profesional** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **costo por oportunidad calificada** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Segmentar por rol con criterios verificables.** El trabajo aquí es separar lo observado de lo inferido sobre **costo por impresión elevado**. La evidencia que ordena la discusión es **precisión de la segmentación**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Construir el mensaje desde la preocupación del cargo.** El riesgo de este paso es cerrar demasiado rápido alrededor de **pertinencia por rol**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **comparación con canales alternativos** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Medir hasta oportunidad calificada y no hasta lead.** Con **umbral de viabilidad** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **costo por oportunidad calificada** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Comparar con canales alternativos antes de escalar.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **segmentación profesional**. **precisión de la segmentación** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **segmentación profesional** | Selección por cargo, función, industria y tamaño de organización | Cuando **costo por oportunidad calificada** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **costo por impresión elevado** | Precio característico del canal que exige tickets altos para ser rentable | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Los datos de perfil profesional son declarados por los usuarios y pueden estar desactualizados. La segmentación no garantiza que la persona ocupe hoy ese cargo.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre linkedIn Ads: arquitectura conceptual |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Performance marketer, Media buyer y Growth marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina gastó CLP 1,2 millones en el canal para promocionar un ebook genérico. Obtuvo 22 leads a CLP 54.000 cada uno y ninguna oportunidad calificada.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **verificar que el ticket sostiene el costo del canal → segmentar por rol con criterios verificables → construir el mensaje desde la preocupación del cargo → medir hasta oportunidad calificada y no hasta lead → comparar con canales alternativos antes de escalar** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **costo por oportunidad calificada**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Advanced Google AdWords* y la de *Digital Marketing*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **segmentación profesional** y **costo por impresión elevado** como sinónimos | Se perdió la distinción entre «selección por cargo, función, industria y tamaño de organización» y «precio característico del canal que exige tickets altos para ser rentable» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «comparar con canales alternativos antes de escalar» | Se saltó «verificar que el ticket sostiene el costo del canal»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **costo por oportunidad calificada** | La métrica local reemplazó al resultado del sistema | Contrástala con **comparación con canales alternativos** y explicita el costo de oportunidad. |
| Usar canales caros para captar leads genéricos | Error específico de esta clase | Reserva el canal para propuestas pertinentes al rol y tickets que sostengan su costo. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **segmentación profesional** y **costo por impresión elevado** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **pertinencia por rol** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «verificar que el ticket sostiene el costo del canal» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **costo por oportunidad calificada** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Los datos de perfil profesional son declarados por los usuarios y pueden estar desactualizados. La segmentación no garantiza que la persona ocupe hoy ese cargo»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **pertinencia por rol** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **costo por oportunidad calificada**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Advanced Google AdWords* y *Web Analytics 2.0*. |
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

Guarda en `evidence/P14-C07-linkedin-ads-arquitectura-conceptual/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **costo por oportunidad calificada**, **precisión de la segmentación** y **comparación con canales alternativos** con fuente, ventana y lectura prohibida.
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

- Brad Geddes — [*Advanced Google AdWords*](https://openlibrary.org/isbn/9781118819647) (2014, 3.ª ed.) · ISBN 9781118819647 — **aporta a esta clase:** los tipos de coincidencia y las exclusiones como control del gasto. **Dónde buscarlo:** los capítulos sobre palabras clave y concordancias. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Dave Chaffey y Fiona Ellis-Chadwick — [*Digital Marketing*](https://openlibrary.org/isbn/9781292400990) (2022, 8.ª ed.) · ISBN 9781292400990 — **aporta a esta clase:** el modelo de contribución de canal a la conversión. **Dónde buscarlo:** los capítulos sobre estrategia de canales. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Brent Adamson y Matthew Dixon — [*The Challenger Customer*](https://openlibrary.org/isbn/9780241196564) (2015) · ISBN 9780241196564 — **aporta a esta clase:** el consenso interno como principal obstáculo, por encima de la persuasión individual. **Dónde buscarlo:** los capítulos iniciales sobre el problema del consenso. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Avinash Kaushik — [*Web Analytics 2.0*](https://openlibrary.org/isbn/9780470596425) (2009) · ISBN 9780470596425 — **aporta a esta clase:** la distinción entre métricas de vanidad y métricas accionables. **Dónde buscarlo:** los capítulos sobre selección de métricas. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 06 · Meta Ads: arquitectura conceptual](class-06-meta-ads-arquitectura-conceptual.md) · [Índice de la parte](README.md) · [Clase 08 · Presupuesto y ritmo de gasto](class-08-presupuesto-y-pacing.md) →
