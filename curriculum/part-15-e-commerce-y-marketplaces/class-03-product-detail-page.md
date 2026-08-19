# Clase 15.03 — Página de producto

Clase 3 de 14 de la parte [15 — E-commerce y marketplaces](README.md), de nivel Adquisición. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 15.02, *Catálogo y merchandising digital*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de consultas previas a la compra con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La primera ley: la página no debe obligar a pensar dónde está uno ni qué hacer — Steve Krug. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La página de producto debe responder todo lo que el cliente necesita para decidir sin contactar a nadie: qué es, si sirve para su caso, cuánto cuesta con despacho, cuándo llega, qué pasa si no funciona. En Chile la información al consumidor no es opcional: precio total, condiciones, garantía legal y derecho a retracto cuando corresponde deben estar disponibles antes de la compra.

Antes de cualquier herramienta, esta clase obliga a nombrar qué cambiaría si el análisis fuese correcto. La parte 15 busca **operar una tienda y un canal de marketplace con economía verificable**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **página de producto** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Dónde se pierde el pedido y cuánto queda después de comisión, envío y devolución?

Los conceptos que estructuran la sesión son **información suficiente**, **precio total**, **garantía legal** y **compatibilidad declarada**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `información suficiente`, `precio total`, `garantía legal` y `compatibilidad declarada` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **E-commerce y marketplaces**.
3. **Aplicar** la secuencia **listar las preguntas que llegan a soporte antes de comprar → responderlas en la página → mostrar precio total y plazo de entrega → declarar garantía y condiciones de devolución → medir consultas previas a la compra y reducirlas** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **consultas previas a la compra**, **tasa de conversión de la página** y **devoluciones por información deficiente** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **información suficiente** y **precio total** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **consultas previas a la compra**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **información suficiente** | conjunto de datos que permite decidir sin consultar | Construye un caso límite donde el concepto se confunde con el anterior. |
| **precio total** | monto final incluyendo impuestos y costos de despacho conocidos | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **garantía legal** | derecho del consumidor que existe con independencia de la garantía comercial | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **compatibilidad declarada** | información que permite verificar si el producto sirve para el caso del cliente | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. listar las preguntas que llegan a soporte antes de comprar → 2. responderlas en la página → 3. mostrar precio total y plazo de entrega → 4. declarar garantía y condiciones de devolución → 5. medir consultas previas a la compra y reducirlas
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Demasiada información dificulta la lectura. La solución es jerarquía y secciones desplegables, no omitir datos que la ley exige o que el cliente necesita.

## 📖 Desarrollo

### 1. Información suficiente: mecanismo central

**Información suficiente** se entiende aquí como **conjunto de datos que permite decidir sin consultar**.

La página de producto tiene que responder todas las preguntas que impiden comprar, y esas preguntas son conocidas: qué es exactamente, si sirve para mi caso, cuánto cuesta en total, cuándo llega, qué pasa si no me sirve. Una página que responde cuatro de las cinco pierde a quien tenía la duda restante.

**De dónde viene esta afirmación.** Steve Krug — *Don't Make Me Think, Revisited* (2014) aporta la idea que sostiene este bloque: la primera ley: la página no debe obligar a pensar dónde está uno ni qué hacer. Búscala en los capítulos iniciales sobre usabilidad. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «consultas previas a la compra» debería moverse cuando cambie **información suficiente**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **precio total**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Precio total: frontera conceptual y error de clasificación

**Definición operacional:** monto final incluyendo impuestos y costos de despacho conocidos. Su valor está en distinguirlo de **información suficiente**.

La información suficiente varía por categoría y se determina observando las consultas de preventa. Si soporte responde repetidamente la misma pregunta sobre un producto, esa pregunta debería estar respondida en la ficha. Ese circuito —de las consultas al contenido— es barato y casi nunca está sistematizado.

**Contraste bibliográfico.** Bryan Eisenberg y Jeffrey Eisenberg — *Call to Action* (2005) aporta aquí una distinción concreta: la hipótesis explícita antes del test y su relación con la persuasión (los capítulos sobre proceso de optimización). Formula dos mini-casos: uno que satisface la definición de **precio total** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «responderlas en la página», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Garantía legal: operacionalización y medición

**Garantía legal** significa **derecho del consumidor que existe con independencia de la garantía comercial**.

El precio total incluye despacho e impuestos, y mostrarlo tarde es la causa principal del abandono en el paso final. Estimar el costo de envío antes del checkout, aunque sea de forma aproximada, reduce ese abandono. Además, en operaciones con consumidores existen obligaciones de información de precio que deben verificarse en la normativa vigente.

Ficha de medición obligatoria para **consultas previas a la compra**: `consultas sobre información que la página debería contener, sobre pedidos`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Peep Laja y el equipo de CXL — *Conversion Optimization Playbooks (CXL)* (2024) pone una condición sobre la medición: la jerarquía del mensaje según las preguntas reales del visitante (las guías sobre estructura de páginas). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Compatibilidad declarada: trade-offs y efectos de segundo orden

**Definición:** información que permite verificar si el producto sirve para el caso del cliente.

Más información responde más dudas y alarga la página, con lo que lo esencial se diluye. La estructura que funciona presenta lo decisivo arriba y organiza el detalle en secciones consultables. La decisión sobre qué va arriba debe basarse en las preguntas reales y no en la importancia que el equipo interno atribuye a cada atributo.

**Lo que aporta la fuente.** Matthew Dixon, Nick Toman y Rick DeLisi — *The Effortless Experience* (2013) aporta el criterio para pesar el intercambio: la reducción del esfuerzo del cliente predice lealtad mejor que el deleite (los capítulos que presentan la evidencia). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **devoluciones por información deficiente** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **compatibilidad declarada** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «medir consultas previas a la compra y reducirlas», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La garantía legal existe con independencia de lo que la página declare, y la información sobre devoluciones y retracto debe corresponder a lo que la ley establece y a lo que la operación puede cumplir. Publicar condiciones más restrictivas que las legales no las hace aplicables y sí genera exposición.

**Frontera declarada.** Demasiada información dificulta la lectura. La solución es jerarquía y secciones desplegables, no omitir datos que la ley exige o que el cliente necesita. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar página de producto no consiste en sumar definiciones. Empieza por **información suficiente**, contrasta **precio total** con **garantía legal**, incorpora **compatibilidad declarada** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Steve Krug — *Don't Make Me Think, Revisited* (2014) | La primera ley: la página no debe obligar a pensar dónde está uno ni qué hacer | Los capítulos iniciales sobre usabilidad | ¿Qué debería observarse en **información suficiente** si aquí opera «la primera ley: la página no debe obligar a pensar dónde está uno ni qué hacer»? ¿Y qué observación lo desmentiría en este caso? |
| Bryan Eisenberg y Jeffrey Eisenberg — *Call to Action* (2005) | La hipótesis explícita antes del test y su relación con la persuasión | Los capítulos sobre proceso de optimización | ¿Qué debería observarse en **precio total** si aquí opera «la hipótesis explícita antes del test y su relación con la persuasión»? ¿Y qué observación lo desmentiría en este caso? |
| Peep Laja y el equipo de CXL — *Conversion Optimization Playbooks (CXL)* (2024) | La jerarquía del mensaje según las preguntas reales del visitante | Las guías sobre estructura de páginas | ¿Qué debería observarse en **garantía legal** si aquí opera «la jerarquía del mensaje según las preguntas reales del visitante»? ¿Y qué observación lo desmentiría en este caso? |
| Matthew Dixon, Nick Toman y Rick DeLisi — *The Effortless Experience* (2013) | La reducción del esfuerzo del cliente predice lealtad mejor que el deleite | Los capítulos que presentan la evidencia | ¿Qué debería observarse en **compatibilidad declarada** si aquí opera «la reducción del esfuerzo del cliente predice lealtad mejor que el deleite»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El lector de tarjetas de Ruta Andina no indica con qué modelos de teléfono es compatible. El 41 % de las devoluciones se debe a incompatibilidad.

**Paso 1 — Listar las preguntas que llegan a soporte antes de comprar.** El equipo escribe primero el supuesto asociado a **información suficiente** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **consultas previas a la compra** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Responderlas en la página.** El trabajo aquí es separar lo observado de lo inferido sobre **precio total**. La evidencia que ordena la discusión es **tasa de conversión de la página**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Mostrar precio total y plazo de entrega.** El riesgo de este paso es cerrar demasiado rápido alrededor de **garantía legal**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **devoluciones por información deficiente** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Declarar garantía y condiciones de devolución.** Con **compatibilidad declarada** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **consultas previas a la compra** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Medir consultas previas a la compra y reducirlas.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **información suficiente**. **tasa de conversión de la página** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **información suficiente** | Conjunto de datos que permite decidir sin consultar | Cuando **consultas previas a la compra** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **precio total** | Monto final incluyendo impuestos y costos de despacho conocidos | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Demasiada información dificulta la lectura. La solución es jerarquía y secciones desplegables, no omitir datos que la ley exige o que el cliente necesita.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre página de producto |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como E-commerce manager, Marketplace specialist y Emprendedor. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El lector de tarjetas de Ruta Andina no indica con qué modelos de teléfono es compatible. El 41 % de las devoluciones se debe a incompatibilidad.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **listar las preguntas que llegan a soporte antes de comprar → responderlas en la página → mostrar precio total y plazo de entrega → declarar garantía y condiciones de devolución → medir consultas previas a la compra y reducirlas** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **consultas previas a la compra**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Don't Make Me Think, Revisited* y la de *Call to Action*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **información suficiente** y **precio total** como sinónimos | Se perdió la distinción entre «conjunto de datos que permite decidir sin consultar» y «monto final incluyendo impuestos y costos de despacho conocidos» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «medir consultas previas a la compra y reducirlas» | Se saltó «listar las preguntas que llegan a soporte antes de comprar»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **consultas previas a la compra** | La métrica local reemplazó al resultado del sistema | Contrástala con **devoluciones por información deficiente** y explicita el costo de oportunidad. |
| Omitir información de compatibilidad o de costo total | Error específico de esta clase | Publica precio total, plazo de entrega, compatibilidad y condiciones de devolución en la propia página. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **información suficiente** y **precio total** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **garantía legal** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «listar las preguntas que llegan a soporte antes de comprar» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **consultas previas a la compra** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Demasiada información dificulta la lectura. La solución es jerarquía y secciones desplegables, no omitir datos que la ley exige o que el cliente necesita»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **garantía legal** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **consultas previas a la compra**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Don't Make Me Think, Revisited* y *The Effortless Experience*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, comprueba la norma en su texto vigente. Los enlaces van al texto completo publicado por la Biblioteca del Congreso Nacional; son gratuitos y no hace falta creerle a este material.

- **Consumo y comercio.** [Ley 19.496](https://www.bcn.cl/leychile/navegar?idNorma=61438) — *Establece normas sobre protección de los derechos de los consumidores* (Ministerio de Economía, Fomento y Reconstrucción), y su reglamento de comercio electrónico, [Decreto 6/2021](https://www.bcn.cl/leychile/navegar?idNorma=1165504) — *Aprueba reglamento de comercio electrónico* (Ministerio de Economía, Fomento y Turismo).
- **Datos personales.** [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales* (Ministerio Secretaría General de la Presidencia), que sustituye progresivamente a [Ley 19.628](https://www.bcn.cl/leychile/navegar?idNorma=141599) — *Sobre protección de la vida privada* (Ministerio Secretaría General de la Presidencia).
- **Derecho a retracto.** [Decreto 52/2024](https://www.bcn.cl/leychile/navegar?idNorma=1206144) — *Aprueba reglamento que regula la forma y condiciones en que los proveedores deberán comunicar la exclusión del derecho a retracto y los bienes en que excepcionalmente y por su naturaleza procederá tal exclusión* (Ministerio de Economía, Fomento y Turismo).

Dentro del repositorio, el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) ordena qué norma aplica a cada decisión comercial, [datos personales y ética](../../docs/DATOS-PERSONALES-Y-ETICA.md) desarrolla el tratamiento de datos y [fuentes oficiales](../../docs/FUENTES-OFICIALES.md) lista los organismos con su fecha de consulta. Ninguno de esos documentos reemplaza al texto legal.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P15-C03-product-detail-page/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **consultas previas a la compra**, **tasa de conversión de la página** y **devoluciones por información deficiente** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **simulación de tienda rentable con catálogo, checkout, costos y plan postventa**.

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

- Steve Krug — [*Don't Make Me Think, Revisited*](https://openlibrary.org/isbn/9780321965516) (2014) · ISBN 9780321965516 — **aporta a esta clase:** la primera ley: la página no debe obligar a pensar dónde está uno ni qué hacer. **Dónde buscarlo:** los capítulos iniciales sobre usabilidad. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Bryan Eisenberg y Jeffrey Eisenberg — [*Call to Action*](https://openlibrary.org/isbn/9781932226393) (2005) · ISBN 9781932226393 — **aporta a esta clase:** la hipótesis explícita antes del test y su relación con la persuasión. **Dónde buscarlo:** los capítulos sobre proceso de optimización. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Peep Laja y el equipo de CXL — [*Conversion Optimization Playbooks (CXL)*](https://cxl.com/institute/) (2024) · fuente primaria — **aporta a esta clase:** la jerarquía del mensaje según las preguntas reales del visitante. **Dónde buscarlo:** las guías sobre estructura de páginas. **Acceso:** acceso limitado. Registra edición y páginas consultadas en tu nota de lectura.
- Matthew Dixon, Nick Toman y Rick DeLisi — [*The Effortless Experience*](https://openlibrary.org/isbn/9780241003305) (2013) · ISBN 9780241003305 — **aporta a esta clase:** la reducción del esfuerzo del cliente predice lealtad mejor que el deleite. **Dónde buscarlo:** los capítulos que presentan la evidencia. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 02 · Catálogo y merchandising digital](class-02-catalogo-y-merchandising-digital.md) · [Índice de la parte](README.md) · [Clase 04 · Checkout](class-04-checkout.md) →
