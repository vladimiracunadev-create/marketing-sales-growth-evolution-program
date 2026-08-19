# Clase 22.05 — Crecimiento liderado por producto

Clase 5 de 14 de la parte [22 — Go-to-market, canales y expansión](README.md), de nivel IA y expansión. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 22.04, *Crecimiento liderado por ventas*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de conversión autoservicio con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El momento de valor y su distancia respecto del registro — Wes Bush. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

En el modelo liderado por producto, el propio producto adquiere, activa y expande sin intervención comercial. Su economía es atractiva: costo marginal bajo y escalamiento rápido. Sus condiciones son estrictas: valor perceptible sin ayuda, contratación autónoma y un producto que soporte el uso sin implementación asistida. Sin esas condiciones, el modelo produce una base grande que no convierte.

La clase trata el tema como un problema de evidencia y de consecuencia, no como vocabulario. La parte 22 busca **diseñar el modo en que la oferta llega al mercado y decide crecer**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **crecimiento liderado por producto** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué movimiento comercial corresponde al valor del contrato, al ciclo y al comprador?

Los conceptos que estructuran la sesión son **adopción autónoma**, **expansión por uso**, **costo de servir en autoservicio** y **condición de viabilidad**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `adopción autónoma`, `expansión por uso`, `costo de servir en autoservicio` y `condición de viabilidad` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Go-to-market, canales y expansión**.
3. **Aplicar** la secuencia **verificar que el producto permite adopción autónoma → medir el tiempo hasta el valor sin asistencia → definir los gatillos de conversión y de expansión → calcular el costo de servir en autoservicio → evaluar la economía completa antes de escalar** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **conversión autoservicio**, **costo de servir por usuario** y **expansión por uso** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **adopción autónoma** y **expansión por uso** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **conversión autoservicio**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **adopción autónoma** | capacidad del usuario de contratar y obtener valor sin asistencia | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **expansión por uso** | aumento de ingreso derivado del crecimiento natural del uso | Da un hecho compatible con la definición y otro que la refute. |
| **costo de servir en autoservicio** | gasto de producto y soporte por usuario del modelo | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **condición de viabilidad** | requisitos que hacen posible el modelo en un producto concreto | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. verificar que el producto permite adopción autónoma → 2. medir el tiempo hasta el valor sin asistencia → 3. definir los gatillos de conversión y de expansión → 4. calcular el costo de servir en autoservicio → 5. evaluar la economía completa antes de escalar
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** El modelo traslada costo de ventas a producto y soporte. La economía total puede no mejorar si el producto exige inversión constante para sostener la autonomía.

## 📖 Desarrollo

### 1. Adopción autónoma: mecanismo central

**Adopción autónoma** se entiende aquí como **capacidad del usuario de contratar y obtener valor sin asistencia**.

El crecimiento liderado por producto traslada la adquisición y la activación al propio producto. Su condición es que el usuario pueda llegar solo al valor, y esa condición es del producto y del caso de uso, no de la voluntad de la empresa. Verificarla con usuarios reales es previo a reorganizar la operación alrededor del modelo.

**De dónde viene esta afirmación.** Wes Bush — *Product-Led Growth* (2019) aporta la idea que sostiene este bloque: el momento de valor y su distancia respecto del registro. Búscala en los capítulos sobre tiempo hasta el valor. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «conversión autoservicio» debería moverse cuando cambie **adopción autónoma**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **expansión por uso**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Expansión por uso: frontera conceptual y error de clasificación

**Definición operacional:** aumento de ingreso derivado del crecimiento natural del uso. Su valor está en distinguirlo de **adopción autónoma**.

El momento de valor y su distancia respecto del registro son las variables centrales. Cuanto mayor la distancia, más usuarios se pierden en el camino y menos viable es el autoservicio. Medir esa distancia y trabajar deliberadamente en acortarla es el trabajo principal de este modelo.

**Contraste bibliográfico.** Marty Cagan — *Inspired* (2017, 2.ª ed.) aporta aquí una distinción concreta: la orientación a resultado en lugar de a entrega de funcionalidades (los capítulos sobre equipos de producto). Formula dos mini-casos: uno que satisface la definición de **expansión por uso** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «medir el tiempo hasta el valor sin asistencia», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Costo de servir en autoservicio: operacionalización y medición

**Costo de servir en autoservicio** significa **gasto de producto y soporte por usuario del modelo**.

La expansión por uso es el mecanismo de monetización característico: el cliente crece dentro del producto y el ingreso lo sigue. Requiere que la métrica de cobro corresponda al valor y que los límites se alcancen de forma natural. Cuando el límite es artificial, produce frustración en lugar de conversión.

Ficha de medición obligatoria para **conversión autoservicio**: `cuentas que pagan sin intervención, sobre cuentas registradas`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Sean Ellis y Morgan Brown — *Hacking Growth* (2017) pone una condición sobre la medición: la prueba de imprescindibilidad antes de acelerar la adquisición (los capítulos sobre encaje producto-mercado). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Condición de viabilidad: trade-offs y efectos de segundo orden

**Definición:** requisitos que hacen posible el modelo en un producto concreto.

El autoservicio reduce el costo de adquisición y limita el ticket alcanzable, además de dificultar la venta a organizaciones que exigen proceso formal. La mayoría de las empresas termina combinando modelos, y esa combinación exige definir dónde está la frontera antes de que los equipos la disputen caso a caso.

**Lo que aporta la fuente.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) aporta el criterio para pesar el intercambio: los seis modelos de negocio y las métricas que cambian entre ellos (la parte sobre modelos de negocio). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **expansión por uso** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **condición de viabilidad** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «evaluar la economía completa antes de escalar», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El modelo exige inversión sostenida en producto para sostener la adquisición, y esa inversión compite con las funcionalidades que piden los clientes actuales. Reconocer ese conflicto y asignarle capacidad explícita es lo que impide que el mecanismo de crecimiento se degrade silenciosamente mientras el equipo atiende solicitudes.

**Frontera declarada.** El modelo traslada costo de ventas a producto y soporte. La economía total puede no mejorar si el producto exige inversión constante para sostener la autonomía. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Abrir frentes simultáneos sin capacidad, diluir foco y llegar tarde a todos.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar crecimiento liderado por producto no consiste en sumar definiciones. Empieza por **adopción autónoma**, contrasta **expansión por uso** con **costo de servir en autoservicio**, incorpora **condición de viabilidad** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Wes Bush — *Product-Led Growth* (2019) | El momento de valor y su distancia respecto del registro | Los capítulos sobre tiempo hasta el valor | ¿Qué debería observarse en **adopción autónoma** si aquí opera «el momento de valor y su distancia respecto del registro»? ¿Y qué observación lo desmentiría en este caso? |
| Marty Cagan — *Inspired* (2017, 2.ª ed.) | La orientación a resultado en lugar de a entrega de funcionalidades | Los capítulos sobre equipos de producto | ¿Qué debería observarse en **expansión por uso** si aquí opera «la orientación a resultado en lugar de a entrega de funcionalidades»? ¿Y qué observación lo desmentiría en este caso? |
| Sean Ellis y Morgan Brown — *Hacking Growth* (2017) | La prueba de imprescindibilidad antes de acelerar la adquisición | Los capítulos sobre encaje producto-mercado | ¿Qué debería observarse en **costo de servir en autoservicio** si aquí opera «la prueba de imprescindibilidad antes de acelerar la adquisición»? ¿Y qué observación lo desmentiría en este caso? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | Los seis modelos de negocio y las métricas que cambian entre ellos | La parte sobre modelos de negocio | ¿Qué debería observarse en **condición de viabilidad** si aquí opera «los seis modelos de negocio y las métricas que cambian entre ellos»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El plan self-service de Ruta Andina exige migrar datos históricos, tarea que hoy realiza una persona en cada cuenta. El modelo no es viable sin resolver eso.

**Paso 1 — Verificar que el producto permite adopción autónoma.** El equipo escribe primero el supuesto asociado a **adopción autónoma** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **conversión autoservicio** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Medir el tiempo hasta el valor sin asistencia.** El trabajo aquí es separar lo observado de lo inferido sobre **expansión por uso**. La evidencia que ordena la discusión es **costo de servir por usuario**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Definir los gatillos de conversión y de expansión.** El riesgo de este paso es cerrar demasiado rápido alrededor de **costo de servir en autoservicio**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **expansión por uso** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Calcular el costo de servir en autoservicio.** Con **condición de viabilidad** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **conversión autoservicio** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Evaluar la economía completa antes de escalar.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **adopción autónoma**. **costo de servir por usuario** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **adopción autónoma** | Capacidad del usuario de contratar y obtener valor sin asistencia | Cuando **conversión autoservicio** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **expansión por uso** | Aumento de ingreso derivado del crecimiento natural del uso | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** El modelo traslada costo de ventas a producto y soporte. La economía total puede no mejorar si el producto exige inversión constante para sostener la autonomía.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre crecimiento liderado por producto |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Head of GTM, Partnerships, Product marketing y Founder. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El plan self-service de Ruta Andina exige migrar datos históricos, tarea que hoy realiza una persona en cada cuenta. El modelo no es viable sin resolver eso.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **verificar que el producto permite adopción autónoma → medir el tiempo hasta el valor sin asistencia → definir los gatillos de conversión y de expansión → calcular el costo de servir en autoservicio → evaluar la economía completa antes de escalar** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **conversión autoservicio**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Product-Led Growth* y la de *Inspired*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **adopción autónoma** y **expansión por uso** como sinónimos | Se perdió la distinción entre «capacidad del usuario de contratar y obtener valor sin asistencia» y «aumento de ingreso derivado del crecimiento natural del uso» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «evaluar la economía completa antes de escalar» | Se saltó «verificar que el producto permite adopción autónoma»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **conversión autoservicio** | La métrica local reemplazó al resultado del sistema | Contrástala con **expansión por uso** y explicita el costo de oportunidad. |
| Lanzar autoservicio sin resolver la implementación asistida | Error específico de esta clase | Verifica que el cliente pueda obtener valor sin intervención antes de habilitar el plan. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **adopción autónoma** y **expansión por uso** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **costo de servir en autoservicio** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «verificar que el producto permite adopción autónoma» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **conversión autoservicio** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «El modelo traslada costo de ventas a producto y soporte. La economía total puede no mejorar si el producto exige inversión constante para sostener la autonomía»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **costo de servir en autoservicio** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **conversión autoservicio**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Product-Led Growth* y *Lean Analytics*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Abrir frentes simultáneos sin capacidad, diluir foco y llegar tarde a todos.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, comprueba la norma en su texto vigente. Los enlaces van al texto completo publicado por la Biblioteca del Congreso Nacional; son gratuitos y no hace falta creerle a este material.

- **Consumo y comercio.** [Ley 19.496](https://www.bcn.cl/leychile/navegar?idNorma=61438) — *Establece normas sobre protección de los derechos de los consumidores* (Ministerio de Economía, Fomento y Reconstrucción), y su reglamento de comercio electrónico, [Decreto 6/2021](https://www.bcn.cl/leychile/navegar?idNorma=1165504) — *Aprueba reglamento de comercio electrónico* (Ministerio de Economía, Fomento y Turismo).
- **Datos personales.** [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales* (Ministerio Secretaría General de la Presidencia), que sustituye progresivamente a [Ley 19.628](https://www.bcn.cl/leychile/navegar?idNorma=141599) — *Sobre protección de la vida privada* (Ministerio Secretaría General de la Presidencia).
- **Derecho a retracto.** [Decreto 52/2024](https://www.bcn.cl/leychile/navegar?idNorma=1206144) — *Aprueba reglamento que regula la forma y condiciones en que los proveedores deberán comunicar la exclusión del derecho a retracto y los bienes en que excepcionalmente y por su naturaleza procederá tal exclusión* (Ministerio de Economía, Fomento y Turismo).

Dentro del repositorio, el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) ordena qué norma aplica a cada decisión comercial, [datos personales y ética](../../docs/DATOS-PERSONALES-Y-ETICA.md) desarrolla el tratamiento de datos y [fuentes oficiales](../../docs/FUENTES-OFICIALES.md) lista los organismos con su fecha de consulta. Ninguno de esos documentos reemplaza al texto legal.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P22-C05-product-led-growth/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **conversión autoservicio**, **costo de servir por usuario** y **expansión por uso** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **plan GTM completo con beachhead, movimiento comercial, canales, economía y plan de lanzamiento**.

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

- Wes Bush — [*Product-Led Growth*](https://openlibrary.org/isbn/9781777119317) (2019) · ISBN 9781777119317 — **aporta a esta clase:** el momento de valor y su distancia respecto del registro. **Dónde buscarlo:** los capítulos sobre tiempo hasta el valor. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Marty Cagan — [*Inspired*](https://openlibrary.org/isbn/9781119387541) (2017, 2.ª ed.) · ISBN 9781119387541 — **aporta a esta clase:** la orientación a resultado en lugar de a entrega de funcionalidades. **Dónde buscarlo:** los capítulos sobre equipos de producto. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Sean Ellis y Morgan Brown — [*Hacking Growth*](https://openlibrary.org/isbn/9780451497215) (2017) · ISBN 9780451497215 — **aporta a esta clase:** la prueba de imprescindibilidad antes de acelerar la adquisición. **Dónde buscarlo:** los capítulos sobre encaje producto-mercado. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Alistair Croll y Benjamin Yoskovitz — [*Lean Analytics*](https://openlibrary.org/isbn/9781449335670) (2013) · ISBN 9781449335670 — **aporta a esta clase:** los seis modelos de negocio y las métricas que cambian entre ellos. **Dónde buscarlo:** la parte sobre modelos de negocio. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 04 · Crecimiento liderado por ventas](class-04-sales-led-growth.md) · [Índice de la parte](README.md) · [Clase 06 · Crecimiento liderado por socios](class-06-partner-led-growth.md) →
