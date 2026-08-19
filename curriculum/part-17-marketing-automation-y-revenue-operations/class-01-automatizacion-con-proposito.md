# Clase 17.01 — Automatización con propósito

Clase 1 de 14 de la parte [17 — Marketing automation y revenue operations](README.md), de nivel Operación de ingresos. Dura unos 150 minutos.

## 🚦 Antes de empezar

Esta es la primera clase de la parte, así que no arrastras entregables de las anteriores. Si llegas desde otra parte, ten a la vista su artefacto final; si el programa empieza aquí para ti, lee antes [la ruta de aprendizaje](../../docs/RUTA-DE-APRENDIZAJE.md).

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de flujos con detección de falla con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La fricción en los traspasos entre áreas como pérdida medible de ingreso — Stephen G. Diorio y Chris K. Hummel. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Automatizar un proceso desordenado produce desorden a escala. La secuencia correcta es estandarizar, simplificar y sólo entonces automatizar. Antes de configurar cualquier flujo hay que responder tres preguntas: qué problema resuelve, qué pasa si falla y quién se entera. La automatización comercial tiene consecuencias directas sobre personas reales, y un flujo mal configurado envía mensajes equivocados a clientes reales.

El punto de partida de esta clase no es la definición sino la decisión que la definición debe mejorar. La parte 17 busca **integrar marketing, ventas y servicio en un solo modelo de datos y de proceso**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **automatización con propósito** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué automatizo porque mejora el sistema y qué estaría solo escalando un desorden?

Los conceptos que estructuran la sesión son **proceso estandarizado**, **modo de falla**, **detección de falla** y **reversibilidad**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `proceso estandarizado`, `modo de falla`, `detección de falla` y `reversibilidad` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Marketing automation y revenue operations**.
3. **Aplicar** la secuencia **documentar el proceso manual y estandarizarlo → eliminar pasos innecesarios antes de automatizar → identificar los modos de falla y su consecuencia → instalar detección y alerta antes de activar → medir el efecto sobre el resultado y no sólo el ahorro de tiempo** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **flujos con detección de falla**, **incidentes por automatización** y **tiempo ahorrado verificado** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **proceso estandarizado** y **modo de falla** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **flujos con detección de falla**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **proceso estandarizado** | flujo con pasos definidos y resultado consistente antes de ser automatizado | Da un hecho compatible con la definición y otro que la refute. |
| **modo de falla** | forma en que la automatización puede producir un resultado incorrecto | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **detección de falla** | mecanismo que avisa cuando el flujo deja de funcionar como se esperaba | Construye un caso límite donde el concepto se confunde con el anterior. |
| **reversibilidad** | capacidad de deshacer o corregir el efecto de una automatización errónea | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. documentar el proceso manual y estandarizarlo → 2. eliminar pasos innecesarios antes de automatizar → 3. identificar los modos de falla y su consecuencia → 4. instalar detección y alerta antes de activar → 5. medir el efecto sobre el resultado y no sólo el ahorro de tiempo
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** No todo lo automatizable debe automatizarse: hay interacciones donde el contacto humano es parte del valor y su reemplazo destruye la relación.

## 📖 Desarrollo

### 1. Proceso estandarizado: mecanismo central

**Proceso estandarizado** se entiende aquí como **flujo con pasos definidos y resultado consistente antes de ser automatizado**.

Automatizar un proceso desordenado produce desorden a mayor velocidad. La condición previa a cualquier automatización es que el proceso esté estandarizado: que se sepa qué pasos existen, quién los ejecuta y qué se hace con las excepciones. Saltarse ese paso es la causa más frecuente de automatizaciones que hay que desactivar meses después.

**De dónde viene esta afirmación.** Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) aporta la idea que sostiene este bloque: la fricción en los traspasos entre áreas como pérdida medible de ingreso. Búscala en los capítulos sobre procesos de ingreso. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «flujos con detección de falla» debería moverse cuando cambie **proceso estandarizado**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **modo de falla**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Modo de falla: frontera conceptual y error de clasificación

**Definición operacional:** forma en que la automatización puede producir un resultado incorrecto. Su valor está en distinguirlo de **proceso estandarizado**.

El modo de falla debe anticiparse antes de implementar: qué ocurre si el dato de entrada está incompleto, si el sistema externo no responde, si la condición se cumple dos veces. Un flujo sin manejo de excepciones no falla ruidosamente: falla en silencio, y el problema se detecta cuando alguien nota que algo no ocurrió durante semanas.

**Contraste bibliográfico.** Andrew S. Grove — *High Output Management* (1983) aporta aquí una distinción concreta: el apalancamiento gerencial: qué actividades multiplican el output (los capítulos sobre apalancamiento). Formula dos mini-casos: uno que satisface la definición de **modo de falla** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «eliminar pasos innecesarios antes de automatizar», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Detección de falla: operacionalización y medición

**Detección de falla** significa **mecanismo que avisa cuando el flujo deja de funcionar como se esperaba**.

La detección de falla exige un mecanismo activo. Confiar en que alguien lo notará equivale a descubrir los problemas por reclamo del cliente, que es la forma más cara. Un control mínimo verifica periódicamente que los volúmenes procesados estén dentro de un rango esperado y alerta cuando no lo están.

Ficha de medición obligatoria para **flujos con detección de falla**: `automatizaciones con alerta configurada, sobre automatizaciones activas`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** NIST — *AI Risk Management Framework 1.0* (2023) pone una condición sobre la medición: las cuatro funciones: mapear, medir, gestionar y gobernar el riesgo de IA (el núcleo del marco). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Reversibilidad: trade-offs y efectos de segundo orden

**Definición:** capacidad de deshacer o corregir el efecto de una automatización errónea.

Automatizar más libera tiempo y aumenta la superficie de fallas silenciosas y la dependencia de configuraciones que pocos entienden. Automatizar menos conserva control y consume tiempo en tareas repetitivas. El criterio razonable automatiza lo repetitivo y de bajo riesgo, y mantiene revisión humana donde el error tiene consecuencias para el cliente.

**Lo que aporta la fuente.** Mark Roberge — *The Sales Acceleration Formula* (2015) aporta el criterio para pesar el intercambio: el proceso comercial construido sobre el proceso de compra del cliente (los capítulos sobre alineación con el comprador). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **tiempo ahorrado verificado** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **reversibilidad** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «medir el efecto sobre el resultado y no sólo el ahorro de tiempo», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La reversibilidad debe estar contemplada: cómo se detiene un flujo, cómo se corrige lo que ya ejecutó, quién tiene autoridad para hacerlo. Una automatización que envió mil comunicaciones erróneas necesita un procedimiento de contención definido antes del incidente, no improvisado durante.

**Frontera declarada.** No todo lo automatizable debe automatizarse: hay interacciones donde el contacto humano es parte del valor y su reemplazo destruye la relación. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar automatización con propósito no consiste en sumar definiciones. Empieza por **proceso estandarizado**, contrasta **modo de falla** con **detección de falla**, incorpora **reversibilidad** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) | La fricción en los traspasos entre áreas como pérdida medible de ingreso | Los capítulos sobre procesos de ingreso | ¿Qué debería observarse en **proceso estandarizado** si aquí opera «la fricción en los traspasos entre áreas como pérdida medible de ingreso»? ¿Y qué observación lo desmentiría en este caso? |
| Andrew S. Grove — *High Output Management* (1983) | El apalancamiento gerencial: qué actividades multiplican el output | Los capítulos sobre apalancamiento | ¿Qué debería observarse en **modo de falla** si aquí opera «el apalancamiento gerencial: qué actividades multiplican el output»? ¿Y qué observación lo desmentiría en este caso? |
| NIST — *AI Risk Management Framework 1.0* (2023) | Las cuatro funciones: mapear, medir, gestionar y gobernar el riesgo de IA | El núcleo del marco | ¿Qué debería observarse en **detección de falla** si aquí opera «las cuatro funciones: mapear, medir, gestionar y gobernar el riesgo de IA»? ¿Y qué observación lo desmentiría en este caso? |
| Mark Roberge — *The Sales Acceleration Formula* (2015) | El proceso comercial construido sobre el proceso de compra del cliente | Los capítulos sobre alineación con el comprador | ¿Qué debería observarse en **reversibilidad** si aquí opera «el proceso comercial construido sobre el proceso de compra del cliente»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina automatizó el envío de bienvenida sin filtrar clientes que ya estaban en implementación. Cuarenta clientes recibieron instrucciones de un proceso que ya habían completado.

**Paso 1 — Documentar el proceso manual y estandarizarlo.** El equipo escribe primero el supuesto asociado a **proceso estandarizado** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **flujos con detección de falla** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Eliminar pasos innecesarios antes de automatizar.** El trabajo aquí es separar lo observado de lo inferido sobre **modo de falla**. La evidencia que ordena la discusión es **incidentes por automatización**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Identificar los modos de falla y su consecuencia.** El riesgo de este paso es cerrar demasiado rápido alrededor de **detección de falla**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **tiempo ahorrado verificado** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Instalar detección y alerta antes de activar.** Con **reversibilidad** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **flujos con detección de falla** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Medir el efecto sobre el resultado y no sólo el ahorro de tiempo.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **proceso estandarizado**. **incidentes por automatización** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **proceso estandarizado** | Flujo con pasos definidos y resultado consistente antes de ser automatizado | Cuando **flujos con detección de falla** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **modo de falla** | Forma en que la automatización puede producir un resultado incorrecto | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** No todo lo automatizable debe automatizarse: hay interacciones donde el contacto humano es parte del valor y su reemplazo destruye la relación.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre automatización con propósito |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing ops, RevOps manager y Sales ops. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina automatizó el envío de bienvenida sin filtrar clientes que ya estaban en implementación. Cuarenta clientes recibieron instrucciones de un proceso que ya habían completado.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **documentar el proceso manual y estandarizarlo → eliminar pasos innecesarios antes de automatizar → identificar los modos de falla y su consecuencia → instalar detección y alerta antes de activar → medir el efecto sobre el resultado y no sólo el ahorro de tiempo** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **flujos con detección de falla**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Revenue Operations* y la de *High Output Management*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **proceso estandarizado** y **modo de falla** como sinónimos | Se perdió la distinción entre «flujo con pasos definidos y resultado consistente antes de ser automatizado» y «forma en que la automatización puede producir un resultado incorrecto» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «medir el efecto sobre el resultado y no sólo el ahorro de tiempo» | Se saltó «documentar el proceso manual y estandarizarlo»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **flujos con detección de falla** | La métrica local reemplazó al resultado del sistema | Contrástala con **tiempo ahorrado verificado** y explicita el costo de oportunidad. |
| Automatizar un proceso sin estandarizarlo antes | Error específico de esta clase | Documenta y simplifica el flujo manual; automatiza sólo cuando el resultado ya es consistente. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **proceso estandarizado** y **modo de falla** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **detección de falla** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «documentar el proceso manual y estandarizarlo» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **flujos con detección de falla** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «No todo lo automatizable debe automatizarse: hay interacciones donde el contacto humano es parte del valor y su reemplazo destruye la relación»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **detección de falla** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **flujos con detección de falla**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Revenue Operations* y *The Sales Acceleration Formula*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, comprueba la norma en su texto vigente. Los enlaces van al texto completo publicado por la Biblioteca del Congreso Nacional; son gratuitos y no hace falta creerle a este material.

- **Consumo y comercio.** [Ley 19.496](https://www.bcn.cl/leychile/navegar?idNorma=61438) — *Establece normas sobre protección de los derechos de los consumidores* (Ministerio de Economía, Fomento y Reconstrucción), y su reglamento de comercio electrónico, [Decreto 6/2021](https://www.bcn.cl/leychile/navegar?idNorma=1165504) — *Aprueba reglamento de comercio electrónico* (Ministerio de Economía, Fomento y Turismo).
- **Datos personales.** [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales* (Ministerio Secretaría General de la Presidencia), que sustituye progresivamente a [Ley 19.628](https://www.bcn.cl/leychile/navegar?idNorma=141599) — *Sobre protección de la vida privada* (Ministerio Secretaría General de la Presidencia).
- **Derecho a retracto.** [Decreto 52/2024](https://www.bcn.cl/leychile/navegar?idNorma=1206144) — *Aprueba reglamento que regula la forma y condiciones en que los proveedores deberán comunicar la exclusión del derecho a retracto y los bienes en que excepcionalmente y por su naturaleza procederá tal exclusión* (Ministerio de Economía, Fomento y Turismo).

Dentro del repositorio, el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) ordena qué norma aplica a cada decisión comercial, [datos personales y ética](../../docs/DATOS-PERSONALES-Y-ETICA.md) desarrolla el tratamiento de datos y [fuentes oficiales](../../docs/FUENTES-OFICIALES.md) lista los organismos con su fecha de consulta. Ninguno de esos documentos reemplaza al texto legal.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P17-C01-automatizacion-con-proposito/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **flujos con detección de falla**, **incidentes por automatización** y **tiempo ahorrado verificado** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **operating model de RevOps con lifecycle, scoring, SLA, integraciones y observabilidad**.

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

- Stephen G. Diorio y Chris K. Hummel — [*Revenue Operations*](https://openlibrary.org/isbn/9781119871132) (2022) · ISBN 9781119871132 — **aporta a esta clase:** la fricción en los traspasos entre áreas como pérdida medible de ingreso. **Dónde buscarlo:** los capítulos sobre procesos de ingreso. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Andrew S. Grove — [*High Output Management*](https://openlibrary.org/isbn/9780394532349) (1983) · ISBN 9780394532349 — **aporta a esta clase:** el apalancamiento gerencial: qué actividades multiplican el output. **Dónde buscarlo:** los capítulos sobre apalancamiento. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- NIST — [*AI Risk Management Framework 1.0*](https://doi.org/10.6028/NIST.AI.100-1) (2023) · DOI 10.6028/NIST.AI.100-1 — **aporta a esta clase:** las cuatro funciones: mapear, medir, gestionar y gobernar el riesgo de IA. **Dónde buscarlo:** el núcleo del marco. **Acceso:** gratis. Registra edición y páginas consultadas en tu nota de lectura.
- Mark Roberge — [*The Sales Acceleration Formula*](https://openlibrary.org/isbn/9781119047018) (2015) · ISBN 9781119047018 — **aporta a esta clase:** el proceso comercial construido sobre el proceso de compra del cliente. **Dónde buscarlo:** los capítulos sobre alineación con el comprador. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

[Índice de la parte](README.md) · [Clase 02 · Etapas de ciclo de vida](class-02-lifecycle-stages.md) →
