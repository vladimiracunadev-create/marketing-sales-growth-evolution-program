# Clase 16.13 — Gobierno del CRM

Clase 13 de 14 de la parte [16 — CRM, pipeline y sales operations](README.md), de nivel Operación de ingresos. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 16.12, *Revisión de pipeline*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de cambios documentados con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La definición única por indicador como acuerdo previo a cualquier tablero — Stephen G. Diorio y Chris K. Hummel. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Sin gobierno, un CRM acumula campos, automatizaciones y excepciones hasta volverse inmanejable. El gobierno define quién puede cambiar qué, cómo se solicitan modificaciones, cómo se documentan y con qué frecuencia se revisa el conjunto. También define la responsabilidad sobre datos personales: quién accede, para qué y con qué registro.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 16 busca **convertir el CRM en un sistema de trabajo y de verdad operacional**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **gobierno del CRM** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿El pipeline describe la realidad o solo el optimismo del equipo?

Los conceptos que estructuran la sesión son **responsable del sistema**, **procedimiento de cambio**, **control de acceso** y **deuda de configuración**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `responsable del sistema`, `procedimiento de cambio`, `control de acceso` y `deuda de configuración` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **CRM, pipeline y sales operations**.
3. **Aplicar** la secuencia **designar responsable y procedimiento de cambio → documentar la configuración vigente → definir el control de acceso por rol → revisar y eliminar la deuda de configuración cada semestre → auditar accesos y registro de tratamiento de datos** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **cambios documentados**, **campos y reglas sin uso** y **accesos revisados** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **responsable del sistema** y **procedimiento de cambio** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **cambios documentados**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **responsable del sistema** | persona que decide sobre configuración y cambios | Construye un caso límite donde el concepto se confunde con el anterior. |
| **procedimiento de cambio** | regla que ordena cómo se solicitan y aprueban modificaciones | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **control de acceso** | definición de quién puede ver y modificar cada tipo de dato | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **deuda de configuración** | acumulación de campos y reglas sin uso que degradan el sistema | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. designar responsable y procedimiento de cambio → 2. documentar la configuración vigente → 3. definir el control de acceso por rol → 4. revisar y eliminar la deuda de configuración cada semestre → 5. auditar accesos y registro de tratamiento de datos
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un gobierno demasiado rígido frena mejoras necesarias. El procedimiento debe ser proporcional al riesgo del cambio solicitado.

## 📖 Desarrollo

### 1. Responsable del sistema: mecanismo central

**Responsable del sistema** se entiende aquí como **persona que decide sobre configuración y cambios**.

El gobierno del CRM define quién puede cambiar qué y con qué procedimiento. Su ausencia produce un sistema que crece por acumulación: campos agregados por proyectos terminados, automatizaciones que nadie recuerda haber creado, reglas que se contradicen. Ese desorden tiene un costo operativo real y difícil de revertir.

**De dónde viene esta afirmación.** Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) aporta la idea que sostiene este bloque: la definición única por indicador como acuerdo previo a cualquier tablero. Búscala en los capítulos sobre gobierno de métricas. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «cambios documentados» debería moverse cuando cambie **responsable del sistema**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **procedimiento de cambio**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Procedimiento de cambio: frontera conceptual y error de clasificación

**Definición operacional:** regla que ordena cómo se solicitan y aprueban modificaciones. Su valor está en distinguirlo de **responsable del sistema**.

El responsable del sistema debe estar nombrado y tener tiempo asignado. Cuando la administración del CRM es una tarea adicional de alguien con otras prioridades, se atienden las urgencias y no el mantenimiento. Esa configuración produce, en dos o tres años, un sistema que nadie entiende completo.

**Contraste bibliográfico.** Andrew S. Grove — *High Output Management* (1983) aporta aquí una distinción concreta: la delegación con nivel de supervisión ajustado a la madurez de la tarea (los capítulos sobre madurez relevante a la tarea). Formula dos mini-casos: uno que satisface la definición de **procedimiento de cambio** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «documentar la configuración vigente», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Control de acceso: operacionalización y medición

**Control de acceso** significa **definición de quién puede ver y modificar cada tipo de dato**.

El procedimiento de cambio debe distinguir entre modificaciones locales de bajo impacto y cambios que afectan definiciones, reportes o integraciones. Los primeros deben poder hacerse rápido; los segundos requieren revisión. Sin esa distinción, o todo se traba o todo se cambia sin control.

Ficha de medición obligatoria para **cambios documentados**: `modificaciones con solicitud y aprobación registradas, sobre cambios realizados`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** NIST — *AI Risk Management Framework 1.0* (2023) pone una condición sobre la medición: la función de gobierno como condición transversal a las demás (la sección sobre la función gobernar). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Deuda de configuración: trade-offs y efectos de segundo orden

**Definición:** acumulación de campos y reglas sin uso que degradan el sistema.

Un gobierno estricto protege la integridad y ralentiza la adaptación, lo que empuja a las áreas a construir soluciones paralelas fuera del sistema. Uno laxo permite agilidad y produce deuda de configuración. El equilibrio pasa por definir qué es de bajo riesgo y delegarlo explícitamente.

**Lo que aporta la fuente.** Mark Roberge — *The Sales Acceleration Formula* (2015) aporta el criterio para pesar el intercambio: la formación estandarizada con certificación por componente (los capítulos sobre la fórmula de entrenamiento). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **accesos revisados** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **deuda de configuración** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «auditar accesos y registro de tratamiento de datos», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El control de acceso es una obligación además de una buena práctica: los datos comerciales incluyen información personal y, en algunos casos, información sensible del cliente. Los permisos deben revisarse periódicamente, especialmente tras cambios de rol y salidas, y esa revisión debe quedar registrada.

**Frontera declarada.** Un gobierno demasiado rígido frena mejoras necesarias. El procedimiento debe ser proporcional al riesgo del cambio solicitado. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Tomar decisiones de contratación y presupuesto sobre un pipeline que no representa la realidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar gobierno del CRM no consiste en sumar definiciones. Empieza por **responsable del sistema**, contrasta **procedimiento de cambio** con **control de acceso**, incorpora **deuda de configuración** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) | La definición única por indicador como acuerdo previo a cualquier tablero | Los capítulos sobre gobierno de métricas | ¿Qué debería observarse en **responsable del sistema** si aquí opera «la definición única por indicador como acuerdo previo a cualquier tablero»? ¿Y qué observación lo desmentiría en este caso? |
| Andrew S. Grove — *High Output Management* (1983) | La delegación con nivel de supervisión ajustado a la madurez de la tarea | Los capítulos sobre madurez relevante a la tarea | ¿Qué debería observarse en **procedimiento de cambio** si aquí opera «la delegación con nivel de supervisión ajustado a la madurez de la tarea»? ¿Y qué observación lo desmentiría en este caso? |
| NIST — *AI Risk Management Framework 1.0* (2023) | La función de gobierno como condición transversal a las demás | La sección sobre la función gobernar | ¿Qué debería observarse en **control de acceso** si aquí opera «la función de gobierno como condición transversal a las demás»? ¿Y qué observación lo desmentiría en este caso? |
| Mark Roberge — *The Sales Acceleration Formula* (2015) | La formación estandarizada con certificación por componente | Los capítulos sobre la fórmula de entrenamiento | ¿Qué debería observarse en **deuda de configuración** si aquí opera «la formación estandarizada con certificación por componente»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El CRM de Ruta Andina tiene 14 automatizaciones creadas por tres personas distintas. Dos se contradicen y nadie sabe quién las creó ni por qué.

**Paso 1 — Designar responsable y procedimiento de cambio.** El equipo escribe primero el supuesto asociado a **responsable del sistema** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **cambios documentados** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Documentar la configuración vigente.** El trabajo aquí es separar lo observado de lo inferido sobre **procedimiento de cambio**. La evidencia que ordena la discusión es **campos y reglas sin uso**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Definir el control de acceso por rol.** El riesgo de este paso es cerrar demasiado rápido alrededor de **control de acceso**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **accesos revisados** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Revisar y eliminar la deuda de configuración cada semestre.** Con **deuda de configuración** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **cambios documentados** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Auditar accesos y registro de tratamiento de datos.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **responsable del sistema**. **campos y reglas sin uso** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **responsable del sistema** | Persona que decide sobre configuración y cambios | Cuando **cambios documentados** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **procedimiento de cambio** | Regla que ordena cómo se solicitan y aprueban modificaciones | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un gobierno demasiado rígido frena mejoras necesarias. El procedimiento debe ser proporcional al riesgo del cambio solicitado.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre gobierno del CRM |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Sales operations, RevOps analyst y Jefe de ventas. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El CRM de Ruta Andina tiene 14 automatizaciones creadas por tres personas distintas. Dos se contradicen y nadie sabe quién las creó ni por qué.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **designar responsable y procedimiento de cambio → documentar la configuración vigente → definir el control de acceso por rol → revisar y eliminar la deuda de configuración cada semestre → auditar accesos y registro de tratamiento de datos** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **cambios documentados**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Revenue Operations* y la de *High Output Management*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **responsable del sistema** y **procedimiento de cambio** como sinónimos | Se perdió la distinción entre «persona que decide sobre configuración y cambios» y «regla que ordena cómo se solicitan y aprueban modificaciones» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «auditar accesos y registro de tratamiento de datos» | Se saltó «designar responsable y procedimiento de cambio»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **cambios documentados** | La métrica local reemplazó al resultado del sistema | Contrástala con **accesos revisados** y explicita el costo de oportunidad. |
| Permitir cambios sin registro ni responsable | Error específico de esta clase | Designa un responsable del sistema y exige solicitud documentada para cada cambio de configuración. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **responsable del sistema** y **procedimiento de cambio** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **control de acceso** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «designar responsable y procedimiento de cambio» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **cambios documentados** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un gobierno demasiado rígido frena mejoras necesarias. El procedimiento debe ser proporcional al riesgo del cambio solicitado»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **control de acceso** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **cambios documentados**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Revenue Operations* y *The Sales Acceleration Formula*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Tomar decisiones de contratación y presupuesto sobre un pipeline que no representa la realidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, comprueba la norma en su texto vigente. Los enlaces van al texto completo publicado por la Biblioteca del Congreso Nacional; son gratuitos y no hace falta creerle a este material.

- **Consumo y comercio.** [Ley 19.496](https://www.bcn.cl/leychile/navegar?idNorma=61438) — *Establece normas sobre protección de los derechos de los consumidores* (Ministerio de Economía, Fomento y Reconstrucción), y su reglamento de comercio electrónico, [Decreto 6/2021](https://www.bcn.cl/leychile/navegar?idNorma=1165504) — *Aprueba reglamento de comercio electrónico* (Ministerio de Economía, Fomento y Turismo).
- **Datos personales.** [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales* (Ministerio Secretaría General de la Presidencia), que sustituye progresivamente a [Ley 19.628](https://www.bcn.cl/leychile/navegar?idNorma=141599) — *Sobre protección de la vida privada* (Ministerio Secretaría General de la Presidencia).
- **Derecho a retracto.** [Decreto 52/2024](https://www.bcn.cl/leychile/navegar?idNorma=1206144) — *Aprueba reglamento que regula la forma y condiciones en que los proveedores deberán comunicar la exclusión del derecho a retracto y los bienes en que excepcionalmente y por su naturaleza procederá tal exclusión* (Ministerio de Economía, Fomento y Turismo).

Dentro del repositorio, el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) ordena qué norma aplica a cada decisión comercial, [datos personales y ética](../../docs/DATOS-PERSONALES-Y-ETICA.md) desarrolla el tratamiento de datos y [fuentes oficiales](../../docs/FUENTES-OFICIALES.md) lista los organismos con su fecha de consulta. Ninguno de esos documentos reemplaza al texto legal.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P16-C13-gobierno-del-crm/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **cambios documentados**, **campos y reglas sin uso** y **accesos revisados** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **diseño de sales operations con pipeline, criterios de etapa, forecast y gobierno de datos**.

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

- Stephen G. Diorio y Chris K. Hummel — [*Revenue Operations*](https://openlibrary.org/isbn/9781119871132) (2022) · ISBN 9781119871132 — **aporta a esta clase:** la definición única por indicador como acuerdo previo a cualquier tablero. **Dónde buscarlo:** los capítulos sobre gobierno de métricas. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Andrew S. Grove — [*High Output Management*](https://openlibrary.org/isbn/9780394532349) (1983) · ISBN 9780394532349 — **aporta a esta clase:** la delegación con nivel de supervisión ajustado a la madurez de la tarea. **Dónde buscarlo:** los capítulos sobre madurez relevante a la tarea. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- NIST — [*AI Risk Management Framework 1.0*](https://doi.org/10.6028/NIST.AI.100-1) (2023) · DOI 10.6028/NIST.AI.100-1 — **aporta a esta clase:** la función de gobierno como condición transversal a las demás. **Dónde buscarlo:** la sección sobre la función gobernar. **Acceso:** gratis. Registra edición y páginas consultadas en tu nota de lectura.
- Mark Roberge — [*The Sales Acceleration Formula*](https://openlibrary.org/isbn/9781119047018) (2015) · ISBN 9781119047018 — **aporta a esta clase:** la formación estandarizada con certificación por componente. **Dónde buscarlo:** los capítulos sobre la fórmula de entrenamiento. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 12 · Revisión de pipeline](class-12-revision-de-pipeline.md) · [Índice de la parte](README.md) · [Clase 14 · Diseño de sales operations](class-14-diseno-de-sales-operations.md) →
