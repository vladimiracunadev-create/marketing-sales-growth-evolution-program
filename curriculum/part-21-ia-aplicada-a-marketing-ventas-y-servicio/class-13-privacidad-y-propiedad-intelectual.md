# Clase 21.13 — Privacidad y propiedad intelectual

Clase 13 de 14 de la parte [21 — IA aplicada a marketing, ventas y servicio](README.md), de nivel IA y expansión. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 21.12, *Evaluación y guardrails*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de casos de uso con base legal documentada con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La función de gobierno como condición transversal a las demás — NIST. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

El uso comercial de IA plantea dos frentes legales. En datos personales, la Ley 21.719 refuerza obligaciones de finalidad, información, seguridad y derechos del titular, incluidos los casos de decisiones automatizadas. En propiedad intelectual, el contenido generado puede reproducir obras protegidas y su titularidad no siempre es clara. Ambos frentes exigen política escrita, no criterio individual.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 21 busca **usar IA como capacidad operativa con evaluación, control y responsabilidad humana**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **privacidad y propiedad intelectual** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué tarea mejora con IA, cómo sé que mejora y quién responde cuando falla?

Los conceptos que estructuran la sesión son **finalidad del tratamiento**, **decisión automatizada**, **titularidad del contenido** y **política de uso**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `finalidad del tratamiento`, `decisión automatizada`, `titularidad del contenido` y `política de uso` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **IA aplicada a marketing, ventas y servicio**.
3. **Aplicar** la secuencia **inventariar qué datos se tratan en cada caso de uso → verificar finalidad, base de licitud e información al titular → definir la política de uso de contenido generado → documentar las decisiones automatizadas y su supervisión → revisar la política cuando cambia la normativa o las herramientas** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **casos de uso con base legal documentada**, **decisiones automatizadas identificadas** y **incidentes de privacidad** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **finalidad del tratamiento** y **decisión automatizada** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **casos de uso con base legal documentada**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **finalidad del tratamiento** | propósito declarado que legitima el uso de los datos personales | Construye un caso límite donde el concepto se confunde con el anterior. |
| **decisión automatizada** | resolución que afecta a una persona tomada sin intervención humana significativa | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **titularidad del contenido** | definición de quién posee derechos sobre lo generado | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **política de uso** | documento que define qué está permitido, qué no y quién autoriza excepciones | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. inventariar qué datos se tratan en cada caso de uso → 2. verificar finalidad, base de licitud e información al titular → 3. definir la política de uso de contenido generado → 4. documentar las decisiones automatizadas y su supervisión → 5. revisar la política cuando cambia la normativa o las herramientas
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** La normativa evoluciona y las herramientas cambian sus condiciones de servicio. La política debe tener fecha de revisión y responsable, no ser un documento único.

## 📖 Desarrollo

### 1. Finalidad del tratamiento: mecanismo central

**Finalidad del tratamiento** se entiende aquí como **propósito declarado que legitima el uso de los datos personales**.

El uso de estas herramientas en operaciones comerciales toca dos marcos normativos distintos: protección de datos personales y propiedad intelectual. Confundirlos lleva a resolver uno y dejar el otro abierto. Ambos deben revisarse antes de incorporar una herramienta al flujo de trabajo.

**De dónde viene esta afirmación.** NIST — *AI Risk Management Framework 1.0* (2023) aporta la idea que sostiene este bloque: la función de gobierno como condición transversal a las demás. Búscala en la sección sobre la función gobernar. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «casos de uso con base legal documentada» debería moverse cuando cambie **finalidad del tratamiento**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **decisión automatizada**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Decisión automatizada: frontera conceptual y error de clasificación

**Definición operacional:** resolución que afecta a una persona tomada sin intervención humana significativa. Su valor está en distinguirlo de **finalidad del tratamiento**.

La finalidad del tratamiento debe declararse y limitarse. Incorporar datos de clientes a un servicio externo es una transferencia con obligaciones específicas: dónde se procesan, quién más accede, cuánto se conservan, si se usan para entrenar. Esas preguntas deben responderse con el proveedor y documentarse.

**Contraste bibliográfico.** Cathy O'Neil — *Weapons of Math Destruction* (2016) aporta aquí una distinción concreta: la exigencia de auditabilidad en modelos que afectan a personas (el capítulo final sobre desarme). Formula dos mini-casos: uno que satisface la definición de **decisión automatizada** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «verificar finalidad, base de licitud e información al titular», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Titularidad del contenido: operacionalización y medición

**Titularidad del contenido** significa **definición de quién posee derechos sobre lo generado**.

La decisión automatizada que produce efectos jurídicos o significativos sobre una persona tiene regulación propia, incluido el derecho a intervención humana. Un sistema que rechaza solicitudes, asigna condiciones o excluye de una oferta puede caer en esa categoría. Verificarlo antes de desplegar es obligatorio.

Ficha de medición obligatoria para **casos de uso con base legal documentada**: `usos con finalidad y base registradas, sobre usos activos`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** ISO — *ISO 31000: Gestión del riesgo* (2018) pone una condición sobre la medición: el riesgo residual aceptado de forma explícita y documentada (la cláusula sobre tratamiento del riesgo). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Política de uso: trade-offs y efectos de segundo orden

**Definición:** documento que define qué está permitido, qué no y quién autoriza excepciones.

Restringir el uso protege y reduce la productividad; permitirlo ampliamente acelera y expone. La política razonable define categorías de datos —públicos, internos, de cliente, sensibles— y qué puede usarse con qué herramienta, en lugar de una prohibición general que el equipo incumplirá en silencio.

**Lo que aporta la fuente.** Stuart Russell y Peter Norvig — *Artificial Intelligence: A Modern Approach* (2021, 4.ª ed.) aporta el criterio para pesar el intercambio: la caracterización del entorno: observable, determinista, episódico y sus consecuencias (el capítulo sobre propiedades del entorno). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **incidentes de privacidad** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **política de uso** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar la política cuando cambia la normativa o las herramientas», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La titularidad del contenido generado y el riesgo de infringir derechos de terceros dependen de la jurisdicción y de los términos del proveedor, y ambos cambian. Este material entrega la estructura de las preguntas; las respuestas requieren revisión legal actualizada y no pueden darse por sabidas.

**Frontera declarada.** La normativa evoluciona y las herramientas cambian sus condiciones de servicio. La política debe tener fecha de revisión y responsable, no ser un documento único. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar privacidad y propiedad intelectual no consiste en sumar definiciones. Empieza por **finalidad del tratamiento**, contrasta **decisión automatizada** con **titularidad del contenido**, incorpora **política de uso** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| NIST — *AI Risk Management Framework 1.0* (2023) | La función de gobierno como condición transversal a las demás | La sección sobre la función gobernar | ¿Qué debería observarse en **finalidad del tratamiento** si aquí opera «la función de gobierno como condición transversal a las demás»? ¿Y qué observación lo desmentiría en este caso? |
| Cathy O'Neil — *Weapons of Math Destruction* (2016) | La exigencia de auditabilidad en modelos que afectan a personas | El capítulo final sobre desarme | ¿Qué debería observarse en **decisión automatizada** si aquí opera «la exigencia de auditabilidad en modelos que afectan a personas»? ¿Y qué observación lo desmentiría en este caso? |
| ISO — *ISO 31000: Gestión del riesgo* (2018) | El riesgo residual aceptado de forma explícita y documentada | La cláusula sobre tratamiento del riesgo | ¿Qué debería observarse en **titularidad del contenido** si aquí opera «el riesgo residual aceptado de forma explícita y documentada»? ¿Y qué observación lo desmentiría en este caso? |
| Stuart Russell y Peter Norvig — *Artificial Intelligence: A Modern Approach* (2021, 4.ª ed.) | La caracterización del entorno: observable, determinista, episódico y sus consecuencias | El capítulo sobre propiedades del entorno | ¿Qué debería observarse en **política de uso** si aquí opera «la caracterización del entorno: observable, determinista, episódico y sus consecuencias»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina usa un modelo para decidir qué clientes reciben una oferta de retención. Esa decisión automatizada afecta a personas y no está documentada ni supervisada.

**Paso 1 — Inventariar qué datos se tratan en cada caso de uso.** El equipo escribe primero el supuesto asociado a **finalidad del tratamiento** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **casos de uso con base legal documentada** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Verificar finalidad, base de licitud e información al titular.** El trabajo aquí es separar lo observado de lo inferido sobre **decisión automatizada**. La evidencia que ordena la discusión es **decisiones automatizadas identificadas**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Definir la política de uso de contenido generado.** El riesgo de este paso es cerrar demasiado rápido alrededor de **titularidad del contenido**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **incidentes de privacidad** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Documentar las decisiones automatizadas y su supervisión.** Con **política de uso** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **casos de uso con base legal documentada** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar la política cuando cambia la normativa o las herramientas.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **finalidad del tratamiento**. **decisiones automatizadas identificadas** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **finalidad del tratamiento** | Propósito declarado que legitima el uso de los datos personales | Cuando **casos de uso con base legal documentada** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **decisión automatizada** | Resolución que afecta a una persona tomada sin intervención humana significativa | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** La normativa evoluciona y las herramientas cambian sus condiciones de servicio. La política debe tener fecha de revisión y responsable, no ser un documento único.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre privacidad y propiedad intelectual |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager con IA, RevOps, Marketing manager y Sales enablement. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina usa un modelo para decidir qué clientes reciben una oferta de retención. Esa decisión automatizada afecta a personas y no está documentada ni supervisada.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **inventariar qué datos se tratan en cada caso de uso → verificar finalidad, base de licitud e información al titular → definir la política de uso de contenido generado → documentar las decisiones automatizadas y su supervisión → revisar la política cuando cambia la normativa o las herramientas** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **casos de uso con base legal documentada**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *AI Risk Management Framework 1.0* y la de *Weapons of Math Destruction*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **finalidad del tratamiento** y **decisión automatizada** como sinónimos | Se perdió la distinción entre «propósito declarado que legitima el uso de los datos personales» y «resolución que afecta a una persona tomada sin intervención humana significativa» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar la política cuando cambia la normativa o las herramientas» | Se saltó «inventariar qué datos se tratan en cada caso de uso»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **casos de uso con base legal documentada** | La métrica local reemplazó al resultado del sistema | Contrástala con **incidentes de privacidad** y explicita el costo de oportunidad. |
| Operar decisiones automatizadas sin documentación ni supervisión | Error específico de esta clase | Identifica las decisiones automatizadas que afectan a personas y documenta su supervisión humana. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **finalidad del tratamiento** y **decisión automatizada** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **titularidad del contenido** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «inventariar qué datos se tratan en cada caso de uso» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **casos de uso con base legal documentada** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «La normativa evoluciona y las herramientas cambian sus condiciones de servicio. La política debe tener fecha de revisión y responsable, no ser un documento único»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **titularidad del contenido** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **casos de uso con base legal documentada**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *AI Risk Management Framework 1.0* y *Artificial Intelligence: A Modern Approach*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, comprueba la norma en su texto vigente. Los enlaces van al texto completo publicado por la Biblioteca del Congreso Nacional; son gratuitos y no hace falta creerle a este material.

- **Consumo y comercio.** [Ley 19.496](https://www.bcn.cl/leychile/navegar?idNorma=61438) — *Establece normas sobre protección de los derechos de los consumidores* (Ministerio de Economía, Fomento y Reconstrucción), y su reglamento de comercio electrónico, [Decreto 6/2021](https://www.bcn.cl/leychile/navegar?idNorma=1165504) — *Aprueba reglamento de comercio electrónico* (Ministerio de Economía, Fomento y Turismo).
- **Datos personales.** [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales* (Ministerio Secretaría General de la Presidencia), que sustituye progresivamente a [Ley 19.628](https://www.bcn.cl/leychile/navegar?idNorma=141599) — *Sobre protección de la vida privada* (Ministerio Secretaría General de la Presidencia).
- **Derecho a retracto.** [Decreto 52/2024](https://www.bcn.cl/leychile/navegar?idNorma=1206144) — *Aprueba reglamento que regula la forma y condiciones en que los proveedores deberán comunicar la exclusión del derecho a retracto y los bienes en que excepcionalmente y por su naturaleza procederá tal exclusión* (Ministerio de Economía, Fomento y Turismo).

Dentro del repositorio, el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) ordena qué norma aplica a cada decisión comercial, [datos personales y ética](../../docs/DATOS-PERSONALES-Y-ETICA.md) desarrolla el tratamiento de datos y [fuentes oficiales](../../docs/FUENTES-OFICIALES.md) lista los organismos con su fecha de consulta. Ninguno de esos documentos reemplaza al texto legal.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P21-C13-privacidad-y-propiedad-intelectual/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **casos de uso con base legal documentada**, **decisiones automatizadas identificadas** y **incidentes de privacidad** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **operating model humano-IA con casos de uso, evaluaciones, guardrails y registro de incidentes**.

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

- NIST — [*AI Risk Management Framework 1.0*](https://doi.org/10.6028/NIST.AI.100-1) (2023) · DOI 10.6028/NIST.AI.100-1 — **aporta a esta clase:** la función de gobierno como condición transversal a las demás. **Dónde buscarlo:** la sección sobre la función gobernar. **Acceso:** gratis. Registra edición y páginas consultadas en tu nota de lectura.
- Cathy O'Neil — [*Weapons of Math Destruction*](https://openlibrary.org/isbn/9780141985428) (2016) · ISBN 9780141985428 — **aporta a esta clase:** la exigencia de auditabilidad en modelos que afectan a personas. **Dónde buscarlo:** el capítulo final sobre desarme. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- ISO — *ISO 31000: Gestión del riesgo* (2018) · fuente primaria — **aporta a esta clase:** el riesgo residual aceptado de forma explícita y documentada. **Dónde buscarlo:** la cláusula sobre tratamiento del riesgo. **Acceso:** de pago. Registra edición y páginas consultadas en tu nota de lectura.
- Stuart Russell y Peter Norvig — [*Artificial Intelligence: A Modern Approach*](https://openlibrary.org/isbn/9780136958420) (2021, 4.ª ed.) · ISBN 9780136958420 — **aporta a esta clase:** la caracterización del entorno: observable, determinista, episódico y sus consecuencias. **Dónde buscarlo:** el capítulo sobre propiedades del entorno. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 12 · Evaluación y guardrails](class-12-evaluacion-y-guardrails.md) · [Índice de la parte](README.md) · [Clase 14 · Operating model humano-IA](class-14-operating-model-humano-ia.md) →
