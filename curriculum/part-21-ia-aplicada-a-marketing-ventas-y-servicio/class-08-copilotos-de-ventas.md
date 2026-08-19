# Clase 21.08 — Copilotos de ventas

Clase 8 de 14 de la parte [21 — IA aplicada a marketing, ventas y servicio](README.md), de nivel IA y expansión. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 21.07, *Lead scoring asistido por modelos*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de comunicaciones revisadas antes del envío con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** Las características de un sistema de IA confiable, incluidas trazabilidad y responsabilidad — NIST. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Un copiloto comercial asiste en tareas concretas: preparar reuniones, redactar seguimientos, resumir conversaciones, sugerir siguientes pasos. Su valor es real y su riesgo también: si produce contenido que el vendedor envía sin revisar, la empresa queda comprometida por afirmaciones que nadie verificó. La regla es que el humano responde por lo que envía.

El punto de partida de esta clase no es la definición sino la decisión que la definición debe mejorar. La parte 21 busca **usar IA como capacidad operativa con evaluación, control y responsabilidad humana**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **copilotos de ventas** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué tarea mejora con IA, cómo sé que mejora y quién responde cuando falla?

Los conceptos que estructuran la sesión son **asistencia en tarea**, **revisión obligatoria**, **compromiso derivado** y **registro de la asistencia**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `asistencia en tarea`, `revisión obligatoria`, `compromiso derivado` y `registro de la asistencia` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **IA aplicada a marketing, ventas y servicio**.
3. **Aplicar** la secuencia **definir en qué tareas se permite la asistencia → establecer la revisión humana obligatoria antes del envío → capacitar sobre los errores típicos del sistema → registrar el origen de las comunicaciones → medir tiempo ahorrado y errores evitados** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **comunicaciones revisadas antes del envío**, **errores detectados en revisión** y **tiempo ahorrado verificado** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **asistencia en tarea** y **revisión obligatoria** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **comunicaciones revisadas antes del envío**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **asistencia en tarea** | apoyo en una actividad específica sin sustituir la decisión | Construye un caso límite donde el concepto se confunde con el anterior. |
| **revisión obligatoria** | verificación humana antes de enviar cualquier salida al cliente | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **compromiso derivado** | obligación que nace de lo afirmado en una comunicación comercial | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **registro de la asistencia** | documentación de qué fue generado y quién lo aprobó | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir en qué tareas se permite la asistencia → 2. establecer la revisión humana obligatoria antes del envío → 3. capacitar sobre los errores típicos del sistema → 4. registrar el origen de las comunicaciones → 5. medir tiempo ahorrado y errores evitados
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** La asistencia puede degradar la habilidad del equipo si sustituye la práctica del diagnóstico. Conviene reservar la asistencia para tareas mecánicas.

## 📖 Desarrollo

### 1. Asistencia en tarea: mecanismo central

**Asistencia en tarea** se entiende aquí como **apoyo en una actividad específica sin sustituir la decisión**.

Un asistente de ventas cambia dónde ocurre el error: en lugar de que el vendedor olvide algo, el sistema puede sugerir algo incorrecto con confianza. Esa diferencia exige un control distinto: la revisión obligatoria antes de que cualquier salida llegue al cliente.

**De dónde viene esta afirmación.** NIST — *AI Risk Management Framework 1.0* (2023) aporta la idea que sostiene este bloque: las características de un sistema de IA confiable, incluidas trazabilidad y responsabilidad. Búscala en la sección sobre confiabilidad. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «comunicaciones revisadas antes del envío» debería moverse cuando cambie **asistencia en tarea**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **revisión obligatoria**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Revisión obligatoria: frontera conceptual y error de clasificación

**Definición operacional:** verificación humana antes de enviar cualquier salida al cliente. Su valor está en distinguirlo de **asistencia en tarea**.

La asistencia en tarea funciona mejor que la sustitución: resumir una llamada, preparar un borrador, recordar compromisos previos son usos donde el sistema aporta y el humano decide. Los usos donde el sistema decide —qué precio ofrecer, qué prometer— requieren controles mucho más estrictos y raramente se justifican.

**Contraste bibliográfico.** Mark Roberge — *The Sales Acceleration Formula* (2015) aporta aquí una distinción concreta: la formación estandarizada con certificación por componente (los capítulos sobre la fórmula de entrenamiento). Formula dos mini-casos: uno que satisface la definición de **revisión obligatoria** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «establecer la revisión humana obligatoria antes del envío», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Compromiso derivado: operacionalización y medición

**Compromiso derivado** significa **obligación que nace de lo afirmado en una comunicación comercial**.

El compromiso derivado es el riesgo específico: si el asistente redacta una propuesta con una condición que la operación no puede cumplir y alguien la envía, la empresa queda obligada. La revisión obligatoria debe cubrir específicamente los elementos que generan obligación: plazos, alcances, precios, garantías.

Ficha de medición obligatoria para **comunicaciones revisadas antes del envío**: `salidas verificadas por una persona, sobre salidas enviadas`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Andrew Ng — *Machine Learning Yearning* (2018) pone una condición sobre la medición: el conjunto de evaluación que representa la distribución real de uso (los capítulos sobre conjuntos de desarrollo y prueba). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Registro de la asistencia: trade-offs y efectos de segundo orden

**Definición:** documentación de qué fue generado y quién lo aprobó.

Usar más asistencia aumenta la productividad y puede degradar la habilidad del equipo, que deja de practicar lo que el sistema hace. En funciones donde el criterio se construye con práctica —el descubrimiento, la negociación— esa degradación tiene costo de mediano plazo que conviene considerar.

**Lo que aporta la fuente.** Neil Rackham — *SPIN Selling* (1988) aporta el criterio para pesar el intercambio: el avance frente a la continuación: qué distingue una reunión que progresa (el capítulo sobre los cuatro resultados de una visita). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **tiempo ahorrado verificado** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **registro de la asistencia** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «medir tiempo ahorrado y errores evitados», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El registro de la asistencia —qué produjo el sistema, qué modificó la persona— tiene valor para auditar y para mejorar. Cuando aparece un error en una propuesta, poder distinguir si venía del borrador o se introdujo después determina qué corregir. Ese registro debe existir desde el despliegue.

**Frontera declarada.** La asistencia puede degradar la habilidad del equipo si sustituye la práctica del diagnóstico. Conviene reservar la asistencia para tareas mecánicas. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar copilotos de ventas no consiste en sumar definiciones. Empieza por **asistencia en tarea**, contrasta **revisión obligatoria** con **compromiso derivado**, incorpora **registro de la asistencia** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| NIST — *AI Risk Management Framework 1.0* (2023) | Las características de un sistema de IA confiable, incluidas trazabilidad y responsabilidad | La sección sobre confiabilidad | ¿Qué debería observarse en **asistencia en tarea** si aquí opera «las características de un sistema de IA confiable, incluidas trazabilidad y responsabilidad»? ¿Y qué observación lo desmentiría en este caso? |
| Mark Roberge — *The Sales Acceleration Formula* (2015) | La formación estandarizada con certificación por componente | Los capítulos sobre la fórmula de entrenamiento | ¿Qué debería observarse en **revisión obligatoria** si aquí opera «la formación estandarizada con certificación por componente»? ¿Y qué observación lo desmentiría en este caso? |
| Andrew Ng — *Machine Learning Yearning* (2018) | El conjunto de evaluación que representa la distribución real de uso | Los capítulos sobre conjuntos de desarrollo y prueba | ¿Qué debería observarse en **compromiso derivado** si aquí opera «el conjunto de evaluación que representa la distribución real de uso»? ¿Y qué observación lo desmentiría en este caso? |
| Neil Rackham — *SPIN Selling* (1988) | El avance frente a la continuación: qué distingue una reunión que progresa | El capítulo sobre los cuatro resultados de una visita | ¿Qué debería observarse en **registro de la asistencia** si aquí opera «el avance frente a la continuación: qué distingue una reunión que progresa»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Un vendedor de Ruta Andina envió una propuesta generada que incluía una integración inexistente. El cliente firmó por esa razón.

**Paso 1 — Definir en qué tareas se permite la asistencia.** El equipo escribe primero el supuesto asociado a **asistencia en tarea** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **comunicaciones revisadas antes del envío** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Establecer la revisión humana obligatoria antes del envío.** El trabajo aquí es separar lo observado de lo inferido sobre **revisión obligatoria**. La evidencia que ordena la discusión es **errores detectados en revisión**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Capacitar sobre los errores típicos del sistema.** El riesgo de este paso es cerrar demasiado rápido alrededor de **compromiso derivado**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **tiempo ahorrado verificado** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Registrar el origen de las comunicaciones.** Con **registro de la asistencia** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **comunicaciones revisadas antes del envío** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Medir tiempo ahorrado y errores evitados.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **asistencia en tarea**. **errores detectados en revisión** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **asistencia en tarea** | Apoyo en una actividad específica sin sustituir la decisión | Cuando **comunicaciones revisadas antes del envío** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **revisión obligatoria** | Verificación humana antes de enviar cualquier salida al cliente | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** La asistencia puede degradar la habilidad del equipo si sustituye la práctica del diagnóstico. Conviene reservar la asistencia para tareas mecánicas.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre copilotos de ventas |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager con IA, RevOps, Marketing manager y Sales enablement. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Un vendedor de Ruta Andina envió una propuesta generada que incluía una integración inexistente. El cliente firmó por esa razón.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir en qué tareas se permite la asistencia → establecer la revisión humana obligatoria antes del envío → capacitar sobre los errores típicos del sistema → registrar el origen de las comunicaciones → medir tiempo ahorrado y errores evitados** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **comunicaciones revisadas antes del envío**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *AI Risk Management Framework 1.0* y la de *The Sales Acceleration Formula*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **asistencia en tarea** y **revisión obligatoria** como sinónimos | Se perdió la distinción entre «apoyo en una actividad específica sin sustituir la decisión» y «verificación humana antes de enviar cualquier salida al cliente» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «medir tiempo ahorrado y errores evitados» | Se saltó «definir en qué tareas se permite la asistencia»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **comunicaciones revisadas antes del envío** | La métrica local reemplazó al resultado del sistema | Contrástala con **tiempo ahorrado verificado** y explicita el costo de oportunidad. |
| Enviar salidas generadas sin revisión humana | Error específico de esta clase | Instala la revisión obligatoria antes de cualquier comunicación al cliente. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **asistencia en tarea** y **revisión obligatoria** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **compromiso derivado** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir en qué tareas se permite la asistencia» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **comunicaciones revisadas antes del envío** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «La asistencia puede degradar la habilidad del equipo si sustituye la práctica del diagnóstico. Conviene reservar la asistencia para tareas mecánicas»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **compromiso derivado** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **comunicaciones revisadas antes del envío**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *AI Risk Management Framework 1.0* y *SPIN Selling*. |
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

Guarda en `evidence/P21-C08-copilotos-de-ventas/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **comunicaciones revisadas antes del envío**, **errores detectados en revisión** y **tiempo ahorrado verificado** con fuente, ventana y lectura prohibida.
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

- NIST — [*AI Risk Management Framework 1.0*](https://doi.org/10.6028/NIST.AI.100-1) (2023) · DOI 10.6028/NIST.AI.100-1 — **aporta a esta clase:** las características de un sistema de IA confiable, incluidas trazabilidad y responsabilidad. **Dónde buscarlo:** la sección sobre confiabilidad. **Acceso:** gratis. Registra edición y páginas consultadas en tu nota de lectura.
- Mark Roberge — [*The Sales Acceleration Formula*](https://openlibrary.org/isbn/9781119047018) (2015) · ISBN 9781119047018 — **aporta a esta clase:** la formación estandarizada con certificación por componente. **Dónde buscarlo:** los capítulos sobre la fórmula de entrenamiento. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Andrew Ng — [*Machine Learning Yearning*](https://info.deeplearning.ai/machine-learning-yearning-book) (2018) · fuente primaria — **aporta a esta clase:** el conjunto de evaluación que representa la distribución real de uso. **Dónde buscarlo:** los capítulos sobre conjuntos de desarrollo y prueba. **Acceso:** gratis. Registra edición y páginas consultadas en tu nota de lectura.
- Neil Rackham — [*SPIN Selling*](https://openlibrary.org/isbn/9780070511132) (1988) · ISBN 9780070511132 — **aporta a esta clase:** el avance frente a la continuación: qué distingue una reunión que progresa. **Dónde buscarlo:** el capítulo sobre los cuatro resultados de una visita. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 07 · Lead scoring asistido por modelos](class-07-lead-scoring-asistido.md) · [Índice de la parte](README.md) · [Clase 09 · Agentes comerciales automatizados](class-09-agentes-comerciales.md) →
