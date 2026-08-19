---
title: "Gobernanza de automatizaciones"
type: class
language: es
standard: clase-profunda-v2
part: 17
class: 13
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["nist-airmf", "diorio", "iso-31000", "oneil"]
anchors: {"diorio": "definiciones", "iso-31000": "proceso", "nist-airmf": "gobernar", "oneil": "auditoria"}
updated: 2026-08-19
---

# Clase 17.13 — Gobernanza de automatizaciones

**Parte 17 · Marketing automation y revenue operations** · Nivel: Operación de ingresos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 17.12 — *Calidad y observabilidad*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de flujos con base legal documentada para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La función de gobierno como condición transversal a las demás — NIST. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La gobernanza define quién puede crear, modificar y desactivar automatizaciones, con qué aprobación y con qué registro. Su ausencia produce sistemas donde nadie puede explicar por qué un cliente recibió un mensaje, lo que además es un problema de cumplimiento: la normativa de datos exige poder acreditar el tratamiento realizado.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 17 busca **integrar marketing, ventas y servicio en un solo modelo de datos y de proceso**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **gobernanza de automatizaciones** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué automatizo porque mejora el sistema y qué estaría solo escalando un desorden?

Los conceptos que estructuran la sesión son **autoridad de cambio**, **registro de tratamiento**, **revisión periódica** y **retiro de automatizaciones**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `autoridad de cambio`, `registro de tratamiento`, `revisión periódica` y `retiro de automatizaciones` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Marketing automation y revenue operations**.
3. **Aplicar** la secuencia **definir autoridad de cambio por tipo de automatización → documentar propósito y base legal de cada flujo → establecer la revisión periódica y su alcance → retirar los flujos obsoletos → mantener el registro de tratamiento actualizado** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **flujos con base legal documentada**, **flujos retirados por revisión** y **cambios con aprobación registrada** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **autoridad de cambio** y **registro de tratamiento** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **flujos con base legal documentada**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **autoridad de cambio** | definición de quién puede modificar qué en el sistema automatizado | Construye un caso límite donde el concepto se confunde con el anterior. |
| **registro de tratamiento** | documentación de qué datos se usaron, con qué finalidad y bajo qué base | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **revisión periódica** | auditoría programada de las automatizaciones activas | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **retiro de automatizaciones** | proceso de desactivar flujos que ya no cumplen función | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir autoridad de cambio por tipo de automatización → 2. documentar propósito y base legal de cada flujo → 3. establecer la revisión periódica y su alcance → 4. retirar los flujos obsoletos → 5. mantener el registro de tratamiento actualizado
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Una gobernanza pesada frena la operación. El nivel de control debe ser proporcional al riesgo: mayor para flujos que tratan datos personales o comprometen a la empresa.

## 📖 Desarrollo

### 1. Autoridad de cambio: mecanismo central

**Autoridad de cambio** se entiende aquí como **definición de quién puede modificar qué en el sistema automatizado**.

La gobernanza de las automatizaciones responde a una pregunta que se vuelve urgente con el tiempo: quién puede crear, modificar o apagar un proceso que se comunica con clientes. Sin autoridad definida, las automatizaciones se multiplican y nadie tiene la visión del conjunto ni la capacidad de detenerlas.

**De dónde viene esta afirmación.** NIST — *AI Risk Management Framework 1.0* (2023) aporta la idea que sostiene este bloque: la función de gobierno como condición transversal a las demás. Búscala en la sección sobre la función gobernar. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «flujos con base legal documentada» debería moverse cuando cambie **autoridad de cambio**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **registro de tratamiento**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Registro de tratamiento: frontera conceptual y error de clasificación

**Definición operacional:** documentación de qué datos se usaron, con qué finalidad y bajo qué base. Su valor está en distinguirlo de **autoridad de cambio**.

El registro de tratamiento —qué datos se usan, para qué finalidad, durante cuánto tiempo, con qué base de licitud— es una obligación normativa y también una herramienta de gestión. Mantenerlo actualizado obliga a saber qué automatizaciones existen, lo que resuelve indirectamente el problema del inventario.

**Contraste bibliográfico.** Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) aporta aquí una distinción concreta: la definición única por indicador como acuerdo previo a cualquier tablero (los capítulos sobre gobierno de métricas). Formula dos mini-casos: uno que satisface la definición de **registro de tratamiento** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «documentar propósito y base legal de cada flujo», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Revisión periódica: operacionalización y medición

**Revisión periódica** significa **auditoría programada de las automatizaciones activas**.

La revisión periódica debe cubrir tres preguntas por cada automatización activa: sigue siendo necesaria, sigue funcionando como se diseñó, sigue cumpliendo el marco normativo. Sin esa revisión, el sistema acumula procesos que hacen cosas que nadie recuerda haber decidido.

Ficha de medición obligatoria para **flujos con base legal documentada**: `automatizaciones con finalidad y base registradas, sobre automatizaciones activas`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** ISO — *ISO 31000: Gestión del riesgo* (2018) pone una condición sobre la medición: el proceso de gestión del riesgo: identificar, analizar, evaluar y tratar (la cláusula sobre el proceso). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Retiro de automatizaciones: trade-offs y efectos de segundo orden

**Definición:** proceso de desactivar flujos que ya no cumplen función.

Controles estrictos reducen el riesgo y ralentizan la operación, empujando a las áreas a construir soluciones fuera del sistema gobernado, que es el peor resultado. El diseño equilibrado define niveles: cambios de bajo riesgo con registro posterior, cambios que afectan comunicación con clientes con aprobación previa.

**Lo que aporta la fuente.** Cathy O'Neil — *Weapons of Math Destruction* (2016) aporta el criterio para pesar el intercambio: la exigencia de auditabilidad en modelos que afectan a personas (el capítulo final sobre desarme). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **cambios con aprobación registrada** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **retiro de automatizaciones** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «mantener el registro de tratamiento actualizado», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El retiro de automatizaciones es tan importante como su creación y casi nunca se planifica. Una automatización creada para una campaña terminada que sigue activa puede producir comunicaciones incoherentes durante años. Incluir una fecha de revisión obligatoria al momento de crear resuelve buena parte del problema.

**Frontera declarada.** Una gobernanza pesada frena la operación. El nivel de control debe ser proporcional al riesgo: mayor para flujos que tratan datos personales o comprometen a la empresa. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar gobernanza de automatizaciones no consiste en sumar definiciones. Empieza por **autoridad de cambio**, contrasta **registro de tratamiento** con **revisión periódica**, incorpora **retiro de automatizaciones** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| NIST — *AI Risk Management Framework 1.0* (2023) | La función de gobierno como condición transversal a las demás | La sección sobre la función gobernar | ¿Qué debería observarse en **autoridad de cambio** si aquí opera «la función de gobierno como condición transversal a las demás»? ¿Y qué observación lo desmentiría en este caso? |
| Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) | La definición única por indicador como acuerdo previo a cualquier tablero | Los capítulos sobre gobierno de métricas | ¿Qué debería observarse en **registro de tratamiento** si aquí opera «la definición única por indicador como acuerdo previo a cualquier tablero»? ¿Y qué observación lo desmentiría en este caso? |
| ISO — *ISO 31000: Gestión del riesgo* (2018) | El proceso de gestión del riesgo: identificar, analizar, evaluar y tratar | La cláusula sobre el proceso | ¿Qué debería observarse en **revisión periódica** si aquí opera «el proceso de gestión del riesgo: identificar, analizar, evaluar y tratar»? ¿Y qué observación lo desmentiría en este caso? |
| Cathy O'Neil — *Weapons of Math Destruction* (2016) | La exigencia de auditabilidad en modelos que afectan a personas | El capítulo final sobre desarme | ¿Qué debería observarse en **retiro de automatizaciones** si aquí opera «la exigencia de auditabilidad en modelos que afectan a personas»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina no puede explicar por qué un cliente recibió una comunicación de una campaña que terminó hace ocho meses, ni con qué base de datos se envió.

**Paso 1 — Definir autoridad de cambio por tipo de automatización.** El equipo escribe primero el supuesto asociado a **autoridad de cambio** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **flujos con base legal documentada** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Documentar propósito y base legal de cada flujo.** El trabajo aquí es separar lo observado de lo inferido sobre **registro de tratamiento**. La evidencia que ordena la discusión es **flujos retirados por revisión**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Establecer la revisión periódica y su alcance.** El riesgo de este paso es cerrar demasiado rápido alrededor de **revisión periódica**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **cambios con aprobación registrada** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Retirar los flujos obsoletos.** Con **retiro de automatizaciones** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **flujos con base legal documentada** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Mantener el registro de tratamiento actualizado.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **autoridad de cambio**. **flujos retirados por revisión** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **autoridad de cambio** | Definición de quién puede modificar qué en el sistema automatizado | Cuando **flujos con base legal documentada** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **registro de tratamiento** | Documentación de qué datos se usaron, con qué finalidad y bajo qué base | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Una gobernanza pesada frena la operación. El nivel de control debe ser proporcional al riesgo: mayor para flujos que tratan datos personales o comprometen a la empresa.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre gobernanza de automatizaciones |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing ops, RevOps manager y Sales ops. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina no puede explicar por qué un cliente recibió una comunicación de una campaña que terminó hace ocho meses, ni con qué base de datos se envió.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir autoridad de cambio por tipo de automatización → documentar propósito y base legal de cada flujo → establecer la revisión periódica y su alcance → retirar los flujos obsoletos → mantener el registro de tratamiento actualizado** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **flujos con base legal documentada**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *AI Risk Management Framework 1.0* y la de *Revenue Operations*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **autoridad de cambio** y **registro de tratamiento** como sinónimos | Se perdió la distinción entre «definición de quién puede modificar qué en el sistema automatizado» y «documentación de qué datos se usaron, con qué finalidad y bajo qué base» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «mantener el registro de tratamiento actualizado» | Se saltó «definir autoridad de cambio por tipo de automatización»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **flujos con base legal documentada** | La métrica local reemplazó al resultado del sistema | Contrástala con **cambios con aprobación registrada** y explicita el costo de oportunidad. |
| Mantener flujos activos sin propósito ni base documentada | Error específico de esta clase | Audita las automatizaciones cada semestre y retira las que no tengan finalidad vigente. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **autoridad de cambio** y **registro de tratamiento** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **revisión periódica** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir autoridad de cambio por tipo de automatización» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **flujos con base legal documentada** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Una gobernanza pesada frena la operación. El nivel de control debe ser proporcional al riesgo: mayor para flujos que tratan datos personales o comprometen a la empresa»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **revisión periódica** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **flujos con base legal documentada**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *AI Risk Management Framework 1.0* y *Weapons of Math Destruction*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P17-C13-gobernanza-de-automatizaciones/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **flujos con base legal documentada**, **flujos retirados por revisión** y **cambios con aprobación registrada** con fuente, ventana y lectura prohibida.
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

Cada obra aparece con la idea concreta que aporta a esta clase. Si al leer no encuentras esa idea, la cita está mal puesta y corresponde reportarlo como error del material.

- NIST — *AI Risk Management Framework 1.0* (2023) — **aporta a esta clase:** la función de gobierno como condición transversal a las demás. **Dónde buscarlo:** la sección sobre la función gobernar. Registra edición y páginas consultadas en tu nota de lectura.
- Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) — **aporta a esta clase:** la definición única por indicador como acuerdo previo a cualquier tablero. **Dónde buscarlo:** los capítulos sobre gobierno de métricas. Registra edición y páginas consultadas en tu nota de lectura.
- ISO — *ISO 31000: Gestión del riesgo* (2018) — **aporta a esta clase:** el proceso de gestión del riesgo: identificar, analizar, evaluar y tratar. **Dónde buscarlo:** la cláusula sobre el proceso. Registra edición y páginas consultadas en tu nota de lectura.
- Cathy O'Neil — *Weapons of Math Destruction* (2016) — **aporta a esta clase:** la exigencia de auditabilidad en modelos que afectan a personas. **Dónde buscarlo:** el capítulo final sobre desarme. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 12 · Calidad y observabilidad](class-12-calidad-y-observabilidad.md) · [Índice de la parte](README.md) · [Clase 14 · Operating model de RevOps](class-14-operating-model-revops.md) →
