---
title: "Calidad y observabilidad"
type: class
language: es
standard: clase-profunda-v2
part: 17
class: 12
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["grove", "nist-airmf", "diorio", "wheeler-dv"]
anchors: {"diorio": "friccion", "grove": "indicadores-adelantados", "nist-airmf": "caracteristicas", "wheeler-dv": "variacion-comun"}
updated: 2026-08-19
---

# Clase 17.12 — Calidad y observabilidad

Clase 12 de 14 de la parte [17 — Marketing automation y revenue operations](README.md), de nivel Operación de ingresos. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 17.11, *Forecast unificado*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de proporción de incidentes detectados por monitoreo con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** Los indicadores adelantados y pareados que permiten corregir a tiempo — Andrew S. Grove. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La observabilidad es la capacidad de saber que algo se rompió antes de que lo note un cliente. En operaciones de ingreso eso significa monitorear flujos, integraciones, completitud de datos y coherencia entre sistemas. Sin observabilidad, los problemas se descubren por reclamo, que es la forma más cara y dañina de enterarse.

La clase trata el tema como un problema de evidencia y de consecuencia, no como vocabulario. La parte 17 busca **integrar marketing, ventas y servicio en un solo modelo de datos y de proceso**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **calidad y observabilidad** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué automatizo porque mejora el sistema y qué estaría solo escalando un desorden?

Los conceptos que estructuran la sesión son **indicador de salud del sistema**, **alerta accionable**, **detección por reclamo** y **tiempo medio de recuperación**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `indicador de salud del sistema`, `alerta accionable`, `detección por reclamo` y `tiempo medio de recuperación` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Marketing automation y revenue operations**.
3. **Aplicar** la secuencia **identificar los procesos críticos y sus modos de falla → definir indicadores de salud por proceso → configurar alertas accionables con responsable → medir tiempo de detección y de recuperación → revisar incidentes y corregir causas raíz** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **proporción de incidentes detectados por monitoreo**, **tiempo medio de detección** y **tiempo medio de recuperación** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **indicador de salud del sistema** y **alerta accionable** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **proporción de incidentes detectados por monitoreo**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **indicador de salud del sistema** | métrica que refleja el correcto funcionamiento de un proceso automatizado | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **alerta accionable** | aviso que indica qué se rompió y qué hacer | Construye un caso límite donde el concepto se confunde con el anterior. |
| **detección por reclamo** | situación en que el problema se conoce porque un cliente lo informa | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **tiempo medio de recuperación** | duración entre la detección del problema y su resolución | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. identificar los procesos críticos y sus modos de falla → 2. definir indicadores de salud por proceso → 3. configurar alertas accionables con responsable → 4. medir tiempo de detección y de recuperación → 5. revisar incidentes y corregir causas raíz
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Demasiadas alertas producen desatención. El diseño debe priorizar pocas alertas realmente accionables sobre muchas informativas.

## 📖 Desarrollo

### 1. Indicador de salud del sistema: mecanismo central

**Indicador de salud del sistema** se entiende aquí como **métrica que refleja el correcto funcionamiento de un proceso automatizado**.

La observabilidad del sistema comercial consiste en poder detectar que algo dejó de funcionar antes de que lo note el cliente. Sin ella, los problemas se descubren por reclamo, que además de ser la vía más costosa es la que más daña la relación.

**De dónde viene esta afirmación.** Andrew S. Grove — *High Output Management* (1983) aporta la idea que sostiene este bloque: los indicadores adelantados y pareados que permiten corregir a tiempo. Búscala en los capítulos sobre medición en la producción. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «proporción de incidentes detectados por monitoreo» debería moverse cuando cambie **indicador de salud del sistema**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **alerta accionable**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Alerta accionable: frontera conceptual y error de clasificación

**Definición operacional:** aviso que indica qué se rompió y qué hacer. Su valor está en distinguirlo de **indicador de salud del sistema**.

El indicador de salud del sistema debe medir el flujo y no sólo el estado: cuántos registros se procesaron, cuántos correos se enviaron, cuántas asignaciones ocurrieron. Un descenso abrupto en esos volúmenes es la señal más temprana de una falla, y detectarlo requiere conocer el rango normal.

**Contraste bibliográfico.** NIST — *AI Risk Management Framework 1.0* (2023) aporta aquí una distinción concreta: las características de un sistema de IA confiable, incluidas trazabilidad y responsabilidad (la sección sobre confiabilidad). Formula dos mini-casos: uno que satisface la definición de **alerta accionable** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «definir indicadores de salud por proceso», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Detección por reclamo: operacionalización y medición

**Detección por reclamo** significa **situación en que el problema se conoce porque un cliente lo informa**.

La alerta accionable se distingue del ruido por una condición: quien la recibe sabe qué hacer. Un sistema que emite muchas alertas de bajo valor entrena al equipo a ignorarlas, y entonces la alerta importante también se ignora. Menos alertas y mejor calibradas es casi siempre la configuración correcta.

Ficha de medición obligatoria para **proporción de incidentes detectados por monitoreo**: `incidentes detectados por alerta, sobre incidentes totales`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) pone una condición sobre la medición: la fricción en los traspasos entre áreas como pérdida medible de ingreso (los capítulos sobre procesos de ingreso). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Tiempo medio de recuperación: trade-offs y efectos de segundo orden

**Definición:** duración entre la detección del problema y su resolución.

Monitorear más entrega mayor cobertura y aumenta el ruido y el costo de mantenimiento del propio monitoreo. La regla práctica es monitorear aquello cuya falla tiene consecuencia para el cliente o para el ingreso, y aceptar que lo demás se detectará por revisión periódica.

**Lo que aporta la fuente.** Donald J. Wheeler — *Understanding Variation* (2000) aporta el criterio para pesar el intercambio: la distinción entre variación común y variación especial antes de reaccionar (los capítulos que introducen la distinción). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **tiempo medio de recuperación** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **tiempo medio de recuperación** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar incidentes y corregir causas raíz», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El tiempo medio de recuperación es la métrica que resume la capacidad de respuesta: cuánto pasa entre que algo falla y que vuelve a funcionar. Medirlo obliga a registrar los incidentes, y ese registro es lo que permite identificar fallas recurrentes que merecen una corrección estructural en lugar de una reparación repetida.

**Frontera declarada.** Demasiadas alertas producen desatención. El diseño debe priorizar pocas alertas realmente accionables sobre muchas informativas. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar calidad y observabilidad no consiste en sumar definiciones. Empieza por **indicador de salud del sistema**, contrasta **alerta accionable** con **detección por reclamo**, incorpora **tiempo medio de recuperación** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Andrew S. Grove — *High Output Management* (1983) | Los indicadores adelantados y pareados que permiten corregir a tiempo | Los capítulos sobre medición en la producción | ¿Qué debería observarse en **indicador de salud del sistema** si aquí opera «los indicadores adelantados y pareados que permiten corregir a tiempo»? ¿Y qué observación lo desmentiría en este caso? |
| NIST — *AI Risk Management Framework 1.0* (2023) | Las características de un sistema de IA confiable, incluidas trazabilidad y responsabilidad | La sección sobre confiabilidad | ¿Qué debería observarse en **alerta accionable** si aquí opera «las características de un sistema de IA confiable, incluidas trazabilidad y responsabilidad»? ¿Y qué observación lo desmentiría en este caso? |
| Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) | La fricción en los traspasos entre áreas como pérdida medible de ingreso | Los capítulos sobre procesos de ingreso | ¿Qué debería observarse en **detección por reclamo** si aquí opera «la fricción en los traspasos entre áreas como pérdida medible de ingreso»? ¿Y qué observación lo desmentiría en este caso? |
| Donald J. Wheeler — *Understanding Variation* (2000) | La distinción entre variación común y variación especial antes de reaccionar | Los capítulos que introducen la distinción | ¿Qué debería observarse en **tiempo medio de recuperación** si aquí opera «la distinción entre variación común y variación especial antes de reaccionar»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El 80 % de los incidentes de Ruta Andina se descubre por reclamo de clientes. El tiempo medio de detección es cuatro días.

**Paso 1 — Identificar los procesos críticos y sus modos de falla.** El equipo escribe primero el supuesto asociado a **indicador de salud del sistema** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **proporción de incidentes detectados por monitoreo** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Definir indicadores de salud por proceso.** El trabajo aquí es separar lo observado de lo inferido sobre **alerta accionable**. La evidencia que ordena la discusión es **tiempo medio de detección**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Configurar alertas accionables con responsable.** El riesgo de este paso es cerrar demasiado rápido alrededor de **detección por reclamo**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **tiempo medio de recuperación** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Medir tiempo de detección y de recuperación.** Con **tiempo medio de recuperación** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **proporción de incidentes detectados por monitoreo** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar incidentes y corregir causas raíz.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **indicador de salud del sistema**. **tiempo medio de detección** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **indicador de salud del sistema** | Métrica que refleja el correcto funcionamiento de un proceso automatizado | Cuando **proporción de incidentes detectados por monitoreo** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **alerta accionable** | Aviso que indica qué se rompió y qué hacer | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Demasiadas alertas producen desatención. El diseño debe priorizar pocas alertas realmente accionables sobre muchas informativas.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre calidad y observabilidad |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing ops, RevOps manager y Sales ops. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El 80 % de los incidentes de Ruta Andina se descubre por reclamo de clientes. El tiempo medio de detección es cuatro días.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **identificar los procesos críticos y sus modos de falla → definir indicadores de salud por proceso → configurar alertas accionables con responsable → medir tiempo de detección y de recuperación → revisar incidentes y corregir causas raíz** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **proporción de incidentes detectados por monitoreo**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *High Output Management* y la de *AI Risk Management Framework 1.0*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **indicador de salud del sistema** y **alerta accionable** como sinónimos | Se perdió la distinción entre «métrica que refleja el correcto funcionamiento de un proceso automatizado» y «aviso que indica qué se rompió y qué hacer» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar incidentes y corregir causas raíz» | Se saltó «identificar los procesos críticos y sus modos de falla»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **proporción de incidentes detectados por monitoreo** | La métrica local reemplazó al resultado del sistema | Contrástala con **tiempo medio de recuperación** y explicita el costo de oportunidad. |
| Enterarse de las fallas por reclamo del cliente | Error específico de esta clase | Instala indicadores de salud por proceso crítico y mide el tiempo de detección. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **indicador de salud del sistema** y **alerta accionable** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **detección por reclamo** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «identificar los procesos críticos y sus modos de falla» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **proporción de incidentes detectados por monitoreo** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Demasiadas alertas producen desatención. El diseño debe priorizar pocas alertas realmente accionables sobre muchas informativas»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **detección por reclamo** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **proporción de incidentes detectados por monitoreo**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *High Output Management* y *Understanding Variation*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P17-C12-calidad-y-observabilidad/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **proporción de incidentes detectados por monitoreo**, **tiempo medio de detección** y **tiempo medio de recuperación** con fuente, ventana y lectura prohibida.
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

Estas son las obras sobre las que se apoya lo que acabas de leer. Cada una aparece con la idea concreta que aporta a esta clase, dónde buscarla dentro del libro y el enlace donde se resuelve la edición exacta. Si al leer no encuentras esa idea, la cita está mal puesta y corresponde reportarlo como error del material.

- Andrew S. Grove — [*High Output Management*](https://openlibrary.org/isbn/9780394532349) (1983) · ISBN 9780394532349 — **aporta a esta clase:** los indicadores adelantados y pareados que permiten corregir a tiempo. **Dónde buscarlo:** los capítulos sobre medición en la producción. Registra edición y páginas consultadas en tu nota de lectura.
- NIST — [*AI Risk Management Framework 1.0*](https://doi.org/10.6028/NIST.AI.100-1) (2023) · DOI 10.6028/NIST.AI.100-1 — **aporta a esta clase:** las características de un sistema de IA confiable, incluidas trazabilidad y responsabilidad. **Dónde buscarlo:** la sección sobre confiabilidad. Registra edición y páginas consultadas en tu nota de lectura.
- Stephen G. Diorio y Chris K. Hummel — [*Revenue Operations*](https://openlibrary.org/isbn/9781119871132) (2022) · ISBN 9781119871132 — **aporta a esta clase:** la fricción en los traspasos entre áreas como pérdida medible de ingreso. **Dónde buscarlo:** los capítulos sobre procesos de ingreso. Registra edición y páginas consultadas en tu nota de lectura.
- Donald J. Wheeler — [*Understanding Variation*](https://openlibrary.org/isbn/9780945320531) (2000) · ISBN 9780945320531 — **aporta a esta clase:** la distinción entre variación común y variación especial antes de reaccionar. **Dónde buscarlo:** los capítulos que introducen la distinción. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 11 · Forecast unificado](class-11-forecast-unificado.md) · [Índice de la parte](README.md) · [Clase 13 · Gobernanza de automatizaciones](class-13-gobernanza-de-automatizaciones.md) →
