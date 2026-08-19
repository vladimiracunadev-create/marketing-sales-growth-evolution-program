---
title: "Lead scoring asistido por modelos"
type: class
language: es
standard: clase-profunda-v2
part: 21
class: 07
level: IA y expansión
mastery_threshold: 80
estimated_minutes: 150
sources: ["provost", "ng-mlyearning", "oneil", "nist-airmf"]
anchors: {"ng-mlyearning": "diagnostico", "nist-airmf": "caracteristicas", "oneil": "retroalimentacion", "provost": "sobreajuste"}
updated: 2026-08-19
---

# Clase 21.07 — Lead scoring asistido por modelos

Clase 7 de 14 de la parte [21 — IA aplicada a marketing, ventas y servicio](README.md), de nivel IA y expansión. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 21.06, *Investigación de prospectos asistida*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de desempeño frente a la regla actual con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El sobreajuste y la validación fuera de muestra — Foster Provost y Tom Fawcett. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Un modelo predictivo puede superar a las reglas manuales cuando hay volumen suficiente y datos de calidad. Sus riesgos son conocidos: aprende de la historia y reproduce sus sesgos; si la prospección pasada ignoró un segmento, el modelo lo seguirá subvalorando. Requiere validación periódica, explicabilidad suficiente para que ventas confíe y supervisión humana.

Esta sesión distingue lo que se sabe, lo que se supone y lo que todavía no se ha medido. La parte 21 busca **usar IA como capacidad operativa con evaluación, control y responsabilidad humana**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **lead scoring asistido por modelos** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué tarea mejora con IA, cómo sé que mejora y quién responde cuando falla?

Los conceptos que estructuran la sesión son **sesgo histórico**, **explicabilidad**, **deriva del modelo** y **supervisión humana**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `sesgo histórico`, `explicabilidad`, `deriva del modelo` y `supervisión humana` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **IA aplicada a marketing, ventas y servicio**.
3. **Aplicar** la secuencia **verificar volumen y calidad de datos antes de modelar → evaluar el desempeño frente a la regla manual actual → revisar el sesgo por segmento → monitorear la deriva y recalibrar → mantener supervisión humana sobre las decisiones** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **desempeño frente a la regla actual**, **desempeño por segmento** y **deriva observada** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **sesgo histórico** y **explicabilidad** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **desempeño frente a la regla actual**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **sesgo histórico** | reproducción de patrones del pasado que pueden ser injustos o subóptimos | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **explicabilidad** | capacidad de indicar qué factores influyeron en la puntuación | Construye un caso límite donde el concepto se confunde con el anterior. |
| **deriva del modelo** | pérdida de precisión por cambios en el mercado o en el proceso | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **supervisión humana** | revisión de decisiones del modelo por una persona responsable | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. verificar volumen y calidad de datos antes de modelar → 2. evaluar el desempeño frente a la regla manual actual → 3. revisar el sesgo por segmento → 4. monitorear la deriva y recalibrar → 5. mantener supervisión humana sobre las decisiones
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un modelo que no puede explicarse no será usado por el equipo comercial. La explicabilidad no es un lujo: determina la adopción.

## 📖 Desarrollo

### 1. Sesgo histórico: mecanismo central

**Sesgo histórico** se entiende aquí como **reproducción de patrones del pasado que pueden ser injustos o subóptimos**.

Un modelo de calificación entrenado con datos propios puede superar a las reglas manuales y arrastra un problema que las reglas no tienen: reproduce lo que la empresa hizo, incluidos sus errores. Si históricamente se descartó un segmento por prejuicio, el modelo aprenderá que ese segmento no convierte porque nunca se le vendió.

**De dónde viene esta afirmación.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta la idea que sostiene este bloque: el sobreajuste y la validación fuera de muestra. Búscala en los capítulos sobre sobreajuste. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «desempeño frente a la regla actual» debería moverse cuando cambie **sesgo histórico**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **explicabilidad**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Explicabilidad: frontera conceptual y error de clasificación

**Definición operacional:** capacidad de indicar qué factores influyeron en la puntuación. Su valor está en distinguirlo de **sesgo histórico**.

El sesgo histórico se detecta comparando la distribución de puntajes por segmento con la distribución de resultados reales en los casos donde sí se intentó. Cuando un segmento tiene puntaje sistemáticamente bajo y pocos intentos, la conclusión no es que no convierte: es que no hay evidencia.

**Contraste bibliográfico.** Andrew Ng — *Machine Learning Yearning* (2018) aporta aquí una distinción concreta: el diagnóstico de errores antes de elegir la siguiente mejora (los capítulos sobre análisis de error). Formula dos mini-casos: uno que satisface la definición de **explicabilidad** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «evaluar el desempeño frente a la regla manual actual», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Deriva del modelo: operacionalización y medición

**Deriva del modelo** significa **pérdida de precisión por cambios en el mercado o en el proceso**.

La explicabilidad no es una preferencia estética: si el equipo comercial no entiende por qué una cuenta tiene puntaje alto, no sabrá cómo aprovechar esa información y terminará ignorándola. Un modelo que entrega los tres factores que más pesaron en cada caso se usa; uno que entrega sólo un número, no.

Ficha de medición obligatoria para **desempeño frente a la regla actual**: `diferencia de precisión entre el modelo y la regla manual`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Cathy O'Neil — *Weapons of Math Destruction* (2016) pone una condición sobre la medición: los bucles de retroalimentación que confirman el sesgo del modelo (los capítulos sobre bucles perniciosos). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Supervisión humana: trade-offs y efectos de segundo orden

**Definición:** revisión de decisiones del modelo por una persona responsable.

Un modelo más preciso puede ser menos explicable y menos adoptado, con lo que su precisión superior no se traduce en resultado. En la práctica comercial, la adopción importa más que la exactitud marginal, y esa consideración debe entrar en la elección del método.

**Lo que aporta la fuente.** NIST — *AI Risk Management Framework 1.0* (2023) aporta el criterio para pesar el intercambio: las características de un sistema de IA confiable, incluidas trazabilidad y responsabilidad (la sección sobre confiabilidad). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **deriva observada** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **supervisión humana** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «mantener supervisión humana sobre las decisiones», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La deriva del modelo —la pérdida de validez a medida que cambian las condiciones— es inevitable y debe monitorearse. Un modelo que funcionó bien puede dejar de discriminar sin aviso. Definir una revisión periódica y un umbral de desempeño que obligue a reentrenar es parte del despliegue, no una tarea posterior.

**Frontera declarada.** Un modelo que no puede explicarse no será usado por el equipo comercial. La explicabilidad no es un lujo: determina la adopción. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar lead scoring asistido por modelos no consiste en sumar definiciones. Empieza por **sesgo histórico**, contrasta **explicabilidad** con **deriva del modelo**, incorpora **supervisión humana** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | El sobreajuste y la validación fuera de muestra | Los capítulos sobre sobreajuste | ¿Qué debería observarse en **sesgo histórico** si aquí opera «el sobreajuste y la validación fuera de muestra»? ¿Y qué observación lo desmentiría en este caso? |
| Andrew Ng — *Machine Learning Yearning* (2018) | El diagnóstico de errores antes de elegir la siguiente mejora | Los capítulos sobre análisis de error | ¿Qué debería observarse en **explicabilidad** si aquí opera «el diagnóstico de errores antes de elegir la siguiente mejora»? ¿Y qué observación lo desmentiría en este caso? |
| Cathy O'Neil — *Weapons of Math Destruction* (2016) | Los bucles de retroalimentación que confirman el sesgo del modelo | Los capítulos sobre bucles perniciosos | ¿Qué debería observarse en **deriva del modelo** si aquí opera «los bucles de retroalimentación que confirman el sesgo del modelo»? ¿Y qué observación lo desmentiría en este caso? |
| NIST — *AI Risk Management Framework 1.0* (2023) | Las características de un sistema de IA confiable, incluidas trazabilidad y responsabilidad | La sección sobre confiabilidad | ¿Qué debería observarse en **supervisión humana** si aquí opera «las características de un sistema de IA confiable, incluidas trazabilidad y responsabilidad»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El modelo de Ruta Andina asigna puntajes bajos a los talleres de regiones porque históricamente se les prospectó menos, no porque conviertan peor.

**Paso 1 — Verificar volumen y calidad de datos antes de modelar.** El equipo escribe primero el supuesto asociado a **sesgo histórico** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **desempeño frente a la regla actual** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Evaluar el desempeño frente a la regla manual actual.** El trabajo aquí es separar lo observado de lo inferido sobre **explicabilidad**. La evidencia que ordena la discusión es **desempeño por segmento**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Revisar el sesgo por segmento.** El riesgo de este paso es cerrar demasiado rápido alrededor de **deriva del modelo**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **deriva observada** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Monitorear la deriva y recalibrar.** Con **supervisión humana** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **desempeño frente a la regla actual** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Mantener supervisión humana sobre las decisiones.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **sesgo histórico**. **desempeño por segmento** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **sesgo histórico** | Reproducción de patrones del pasado que pueden ser injustos o subóptimos | Cuando **desempeño frente a la regla actual** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **explicabilidad** | Capacidad de indicar qué factores influyeron en la puntuación | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un modelo que no puede explicarse no será usado por el equipo comercial. La explicabilidad no es un lujo: determina la adopción.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre lead scoring asistido por modelos |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager con IA, RevOps, Marketing manager y Sales enablement. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El modelo de Ruta Andina asigna puntajes bajos a los talleres de regiones porque históricamente se les prospectó menos, no porque conviertan peor.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **verificar volumen y calidad de datos antes de modelar → evaluar el desempeño frente a la regla manual actual → revisar el sesgo por segmento → monitorear la deriva y recalibrar → mantener supervisión humana sobre las decisiones** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **desempeño frente a la regla actual**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Data Science for Business* y la de *Machine Learning Yearning*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **sesgo histórico** y **explicabilidad** como sinónimos | Se perdió la distinción entre «reproducción de patrones del pasado que pueden ser injustos o subóptimos» y «capacidad de indicar qué factores influyeron en la puntuación» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «mantener supervisión humana sobre las decisiones» | Se saltó «verificar volumen y calidad de datos antes de modelar»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **desempeño frente a la regla actual** | La métrica local reemplazó al resultado del sistema | Contrástala con **deriva observada** y explicita el costo de oportunidad. |
| Desplegar el modelo sin revisar el sesgo por segmento | Error específico de esta clase | Compara el desempeño entre segmentos y corrige antes de usarlo para priorizar. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **sesgo histórico** y **explicabilidad** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **deriva del modelo** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «verificar volumen y calidad de datos antes de modelar» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **desempeño frente a la regla actual** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un modelo que no puede explicarse no será usado por el equipo comercial. La explicabilidad no es un lujo: determina la adopción»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **deriva del modelo** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **desempeño frente a la regla actual**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Data Science for Business* y *AI Risk Management Framework 1.0*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P21-C07-lead-scoring-asistido/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **desempeño frente a la regla actual**, **desempeño por segmento** y **deriva observada** con fuente, ventana y lectura prohibida.
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

Estas son las obras sobre las que se apoya lo que acabas de leer. Cada una aparece con la idea concreta que aporta a esta clase, dónde buscarla dentro del libro y el enlace donde se resuelve la edición exacta. Si al leer no encuentras esa idea, la cita está mal puesta y corresponde reportarlo como error del material.

- Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) · ISBN 9781449374280 — **aporta a esta clase:** el sobreajuste y la validación fuera de muestra. **Dónde buscarlo:** los capítulos sobre sobreajuste. Registra edición y páginas consultadas en tu nota de lectura.
- Andrew Ng — [*Machine Learning Yearning*](https://info.deeplearning.ai/machine-learning-yearning-book) (2018) · fuente primaria — **aporta a esta clase:** el diagnóstico de errores antes de elegir la siguiente mejora. **Dónde buscarlo:** los capítulos sobre análisis de error. Registra edición y páginas consultadas en tu nota de lectura.
- Cathy O'Neil — [*Weapons of Math Destruction*](https://openlibrary.org/isbn/9780141985428) (2016) · ISBN 9780141985428 — **aporta a esta clase:** los bucles de retroalimentación que confirman el sesgo del modelo. **Dónde buscarlo:** los capítulos sobre bucles perniciosos. Registra edición y páginas consultadas en tu nota de lectura.
- NIST — [*AI Risk Management Framework 1.0*](https://doi.org/10.6028/NIST.AI.100-1) (2023) · DOI 10.6028/NIST.AI.100-1 — **aporta a esta clase:** las características de un sistema de IA confiable, incluidas trazabilidad y responsabilidad. **Dónde buscarlo:** la sección sobre confiabilidad. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 06 · Investigación de prospectos asistida](class-06-lead-research.md) · [Índice de la parte](README.md) · [Clase 08 · Copilotos de ventas](class-08-copilotos-de-ventas.md) →
