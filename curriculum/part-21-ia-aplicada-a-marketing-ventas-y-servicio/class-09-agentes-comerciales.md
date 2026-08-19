---
title: "Agentes comerciales automatizados"
type: class
language: es
standard: clase-profunda-v2
part: 21
class: 09
level: IA y expansión
mastery_threshold: 80
estimated_minutes: 150
sources: ["russell-norvig", "nist-airmf", "iso-31000", "oneil"]
anchors: {"iso-31000": "riesgo-residual", "nist-airmf": "gobernar", "oneil": "auditoria", "russell-norvig": "agente-racional"}
updated: 2026-08-19
---

# Clase 21.09 — Agentes comerciales automatizados

Clase 9 de 14 de la parte [21 — IA aplicada a marketing, ventas y servicio](README.md), de nivel IA y expansión. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 21.08, *Copilotos de ventas*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de acciones ejecutadas por el agente con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El agente racional definido por su medida de desempeño, entorno, actuadores y sensores — Stuart Russell y Peter Norvig. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Un agente no sólo genera texto: ejecuta acciones —enviar correos, actualizar registros, agendar—. Eso cambia el perfil de riesgo: un error ya no produce un borrador malo sino una acción real sobre un cliente real. Su diseño exige límites explícitos de autoridad, registro de acciones, capacidad de detención inmediata y responsable identificado.

Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales. La parte 21 busca **usar IA como capacidad operativa con evaluación, control y responsabilidad humana**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **agentes comerciales automatizados** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué tarea mejora con IA, cómo sé que mejora y quién responde cuando falla?

Los conceptos que estructuran la sesión son **autoridad del agente**, **registro de acciones**, **mecanismo de detención** y **acción irreversible**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `autoridad del agente`, `registro de acciones`, `mecanismo de detención` y `acción irreversible` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **IA aplicada a marketing, ventas y servicio**.
3. **Aplicar** la secuencia **definir la autoridad del agente por tipo de acción → excluir las acciones irreversibles de la autonomía → instrumentar el registro completo de acciones → habilitar la detención inmediata y probarla → revisar el registro periódicamente con responsable** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **acciones ejecutadas por el agente**, **acciones revertidas** y **tiempo de detención** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **autoridad del agente** y **registro de acciones** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **acciones ejecutadas por el agente**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **autoridad del agente** | conjunto de acciones que el sistema puede ejecutar sin aprobación humana | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **registro de acciones** | traza completa de qué hizo el sistema, cuándo y sobre qué registro | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **mecanismo de detención** | capacidad de interrumpir la operación del agente de inmediato | Da un hecho compatible con la definición y otro que la refute. |
| **acción irreversible** | operación cuyo efecto no puede deshacerse, como enviar una comunicación | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir la autoridad del agente por tipo de acción → 2. excluir las acciones irreversibles de la autonomía → 3. instrumentar el registro completo de acciones → 4. habilitar la detención inmediata y probarla → 5. revisar el registro periódicamente con responsable
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** La responsabilidad legal y comercial siempre recae en la empresa, no en el sistema. La automatización no traslada la responsabilidad a nadie más.

## 📖 Desarrollo

### 1. Autoridad del agente: mecanismo central

**Autoridad del agente** se entiende aquí como **conjunto de acciones que el sistema puede ejecutar sin aprobación humana**.

Un agente que ejecuta acciones comerciales de forma autónoma —enviar comunicaciones, actualizar registros, agendar— introduce una categoría de riesgo distinta: los errores no se quedan en una sugerencia, se materializan. Por eso su autoridad debe estar acotada explícitamente y no definirse por lo que técnicamente puede hacer.

**De dónde viene esta afirmación.** Stuart Russell y Peter Norvig — *Artificial Intelligence: A Modern Approach* (2021, 4.ª ed.) aporta la idea que sostiene este bloque: el agente racional definido por su medida de desempeño, entorno, actuadores y sensores. Búscala en los capítulos sobre agentes inteligentes. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «acciones ejecutadas por el agente» debería moverse cuando cambie **autoridad del agente**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **registro de acciones**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Registro de acciones: frontera conceptual y error de clasificación

**Definición operacional:** traza completa de qué hizo el sistema, cuándo y sobre qué registro. Su valor está en distinguirlo de **autoridad del agente**.

La autoridad del agente debe declararse por acción: qué puede hacer sin supervisión, qué requiere confirmación y qué está prohibido. Esa lista debe existir antes del despliegue y revisarse cuando se amplían las capacidades. Un agente cuya autoridad nunca se definió la tiene ilimitada por omisión.

**Contraste bibliográfico.** NIST — *AI Risk Management Framework 1.0* (2023) aporta aquí una distinción concreta: la función de gobierno como condición transversal a las demás (la sección sobre la función gobernar). Formula dos mini-casos: uno que satisface la definición de **registro de acciones** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «excluir las acciones irreversibles de la autonomía», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Mecanismo de detención: operacionalización y medición

**Mecanismo de detención** significa **capacidad de interrumpir la operación del agente de inmediato**.

El registro de acciones es la condición mínima de auditabilidad: qué hizo el agente, cuándo, con qué información y con qué resultado. Sin ese registro, un incidente no puede reconstruirse y la responsabilidad no puede establecerse, lo que expone tanto a la empresa como a las personas involucradas.

Ficha de medición obligatoria para **acciones ejecutadas por el agente**: `operaciones automáticas realizadas, por tipo y periodo`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** ISO — *ISO 31000: Gestión del riesgo* (2018) pone una condición sobre la medición: el riesgo residual aceptado de forma explícita y documentada (la cláusula sobre tratamiento del riesgo). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Acción irreversible: trade-offs y efectos de segundo orden

**Definición:** operación cuyo efecto no puede deshacerse, como enviar una comunicación.

Mayor autonomía produce más eficiencia y reduce los puntos donde un humano puede detectar un error. El equilibrio no es una preferencia sino una función del costo del error: acciones reversibles y de bajo impacto admiten autonomía; las irreversibles o con efecto sobre el cliente exigen confirmación.

**Lo que aporta la fuente.** Cathy O'Neil — *Weapons of Math Destruction* (2016) aporta el criterio para pesar el intercambio: la exigencia de auditabilidad en modelos que afectan a personas (el capítulo final sobre desarme). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **tiempo de detención** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **acción irreversible** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar el registro periódicamente con responsable», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El mecanismo de detención debe existir, ser conocido y estar probado. La pregunta «quién puede apagar esto y en cuánto tiempo» debe tener respuesta antes de activar el sistema, y la respuesta debe verificarse con una prueba real, no suponerse a partir de la documentación.

**Frontera declarada.** La responsabilidad legal y comercial siempre recae en la empresa, no en el sistema. La automatización no traslada la responsabilidad a nadie más. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar agentes comerciales automatizados no consiste en sumar definiciones. Empieza por **autoridad del agente**, contrasta **registro de acciones** con **mecanismo de detención**, incorpora **acción irreversible** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Stuart Russell y Peter Norvig — *Artificial Intelligence: A Modern Approach* (2021, 4.ª ed.) | El agente racional definido por su medida de desempeño, entorno, actuadores y sensores | Los capítulos sobre agentes inteligentes | ¿Qué debería observarse en **autoridad del agente** si aquí opera «el agente racional definido por su medida de desempeño, entorno, actuadores y sensores»? ¿Y qué observación lo desmentiría en este caso? |
| NIST — *AI Risk Management Framework 1.0* (2023) | La función de gobierno como condición transversal a las demás | La sección sobre la función gobernar | ¿Qué debería observarse en **registro de acciones** si aquí opera «la función de gobierno como condición transversal a las demás»? ¿Y qué observación lo desmentiría en este caso? |
| ISO — *ISO 31000: Gestión del riesgo* (2018) | El riesgo residual aceptado de forma explícita y documentada | La cláusula sobre tratamiento del riesgo | ¿Qué debería observarse en **mecanismo de detención** si aquí opera «el riesgo residual aceptado de forma explícita y documentada»? ¿Y qué observación lo desmentiría en este caso? |
| Cathy O'Neil — *Weapons of Math Destruction* (2016) | La exigencia de auditabilidad en modelos que afectan a personas | El capítulo final sobre desarme | ¿Qué debería observarse en **acción irreversible** si aquí opera «la exigencia de auditabilidad en modelos que afectan a personas»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Un agente de Ruta Andina envió 400 correos de reactivación a clientes que habían solicitado no ser contactados, porque la regla de exclusión no estaba implementada.

**Paso 1 — Definir la autoridad del agente por tipo de acción.** El equipo escribe primero el supuesto asociado a **autoridad del agente** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **acciones ejecutadas por el agente** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Excluir las acciones irreversibles de la autonomía.** El trabajo aquí es separar lo observado de lo inferido sobre **registro de acciones**. La evidencia que ordena la discusión es **acciones revertidas**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Instrumentar el registro completo de acciones.** El riesgo de este paso es cerrar demasiado rápido alrededor de **mecanismo de detención**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **tiempo de detención** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Habilitar la detención inmediata y probarla.** Con **acción irreversible** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **acciones ejecutadas por el agente** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar el registro periódicamente con responsable.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **autoridad del agente**. **acciones revertidas** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **autoridad del agente** | Conjunto de acciones que el sistema puede ejecutar sin aprobación humana | Cuando **acciones ejecutadas por el agente** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **registro de acciones** | Traza completa de qué hizo el sistema, cuándo y sobre qué registro | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** La responsabilidad legal y comercial siempre recae en la empresa, no en el sistema. La automatización no traslada la responsabilidad a nadie más.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre agentes comerciales automatizados |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager con IA, RevOps, Marketing manager y Sales enablement. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Un agente de Ruta Andina envió 400 correos de reactivación a clientes que habían solicitado no ser contactados, porque la regla de exclusión no estaba implementada.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir la autoridad del agente por tipo de acción → excluir las acciones irreversibles de la autonomía → instrumentar el registro completo de acciones → habilitar la detención inmediata y probarla → revisar el registro periódicamente con responsable** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **acciones ejecutadas por el agente**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Artificial Intelligence: A Modern Approach* y la de *AI Risk Management Framework 1.0*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **autoridad del agente** y **registro de acciones** como sinónimos | Se perdió la distinción entre «conjunto de acciones que el sistema puede ejecutar sin aprobación humana» y «traza completa de qué hizo el sistema, cuándo y sobre qué registro» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar el registro periódicamente con responsable» | Se saltó «definir la autoridad del agente por tipo de acción»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **acciones ejecutadas por el agente** | La métrica local reemplazó al resultado del sistema | Contrástala con **tiempo de detención** y explicita el costo de oportunidad. |
| Otorgar autoridad sobre acciones irreversibles | Error específico de esta clase | Excluye envíos y compromisos de la autonomía del agente y exige aprobación humana. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **autoridad del agente** y **registro de acciones** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **mecanismo de detención** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir la autoridad del agente por tipo de acción» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **acciones ejecutadas por el agente** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «La responsabilidad legal y comercial siempre recae en la empresa, no en el sistema. La automatización no traslada la responsabilidad a nadie más»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **mecanismo de detención** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **acciones ejecutadas por el agente**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Artificial Intelligence: A Modern Approach* y *Weapons of Math Destruction*. |
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

Guarda en `evidence/P21-C09-agentes-comerciales/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **acciones ejecutadas por el agente**, **acciones revertidas** y **tiempo de detención** con fuente, ventana y lectura prohibida.
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

- Stuart Russell y Peter Norvig — [*Artificial Intelligence: A Modern Approach*](https://openlibrary.org/isbn/9780136958420) (2021, 4.ª ed.) · ISBN 9780136958420 — **aporta a esta clase:** el agente racional definido por su medida de desempeño, entorno, actuadores y sensores. **Dónde buscarlo:** los capítulos sobre agentes inteligentes. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- NIST — [*AI Risk Management Framework 1.0*](https://doi.org/10.6028/NIST.AI.100-1) (2023) · DOI 10.6028/NIST.AI.100-1 — **aporta a esta clase:** la función de gobierno como condición transversal a las demás. **Dónde buscarlo:** la sección sobre la función gobernar. **Acceso:** gratis. Registra edición y páginas consultadas en tu nota de lectura.
- ISO — *ISO 31000: Gestión del riesgo* (2018) · fuente primaria — **aporta a esta clase:** el riesgo residual aceptado de forma explícita y documentada. **Dónde buscarlo:** la cláusula sobre tratamiento del riesgo. **Acceso:** de pago. Registra edición y páginas consultadas en tu nota de lectura.
- Cathy O'Neil — [*Weapons of Math Destruction*](https://openlibrary.org/isbn/9780141985428) (2016) · ISBN 9780141985428 — **aporta a esta clase:** la exigencia de auditabilidad en modelos que afectan a personas. **Dónde buscarlo:** el capítulo final sobre desarme. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 08 · Copilotos de ventas](class-08-copilotos-de-ventas.md) · [Índice de la parte](README.md) · [Clase 10 · Inteligencia de conversaciones](class-10-conversation-intelligence.md) →
