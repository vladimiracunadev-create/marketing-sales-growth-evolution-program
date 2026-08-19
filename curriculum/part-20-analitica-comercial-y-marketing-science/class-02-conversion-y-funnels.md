---
title: "Conversión y embudos"
type: class
language: es
standard: clase-profunda-v2
part: 20
class: 02
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["kaushik", "croll-yoskovitz", "provost", "wheeler-dv"]
anchors: {"croll-yoskovitz": "etapas", "kaushik": "segmentacion", "provost": "evaluacion", "wheeler-dv": "comparar-dos-puntos"}
updated: 2026-08-19
---

# Clase 20.02 — Conversión y embudos

**Parte 20 · Analítica comercial y marketing science** · Nivel: Crecimiento y analítica · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 20.01 — *Árbol de métricas*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de conversión con definición documentada para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La segmentación como condición para que un promedio signifique algo — Avinash Kaushik. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Una tasa de conversión sin numerador, denominador y ventana definidos es un número sin significado. La misma etapa puede reportar 12 % o 34 % según se cuente sobre visitas, sesiones o personas únicas. La disciplina de definición operacional es lo que permite comparar entre periodos, entre canales y entre equipos sin discutir de qué se está hablando.

Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales. La parte 20 busca **sostener decisiones de ingreso con métricas correctamente construidas**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **conversión y embudos** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Esta cifra mide lo que creo que mide, y qué decisión cambiaría si estuviera equivocada?

Los conceptos que estructuran la sesión son **definición operacional**, **unidad de análisis**, **ventana de conversión** y **comparabilidad**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `definición operacional`, `unidad de análisis`, `ventana de conversión` y `comparabilidad` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Analítica comercial y marketing science**.
3. **Aplicar** la secuencia **definir la unidad de análisis y justificarla → especificar numerador, denominador y ventana → documentar la fuente de cada componente → verificar la comparabilidad antes de contrastar → publicar las definiciones junto con las cifras** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **conversión con definición documentada**, **diferencia entre unidades de análisis** y **consistencia entre informes** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **definición operacional** y **unidad de análisis** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **conversión con definición documentada**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **definición operacional** | especificación de numerador, denominador, ventana y fuente | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **unidad de análisis** | elección entre visitas, sesiones, personas o cuentas como base del cálculo | Construye un caso límite donde el concepto se confunde con el anterior. |
| **ventana de conversión** | periodo dentro del cual se considera que la conversión ocurrió | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **comparabilidad** | condición que permite contrastar cifras entre periodos o canales | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir la unidad de análisis y justificarla → 2. especificar numerador, denominador y ventana → 3. documentar la fuente de cada componente → 4. verificar la comparabilidad antes de contrastar → 5. publicar las definiciones junto con las cifras
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Las definiciones no pueden cambiarse retroactivamente sin recalcular la serie. Un cambio de definición rompe la comparabilidad histórica y debe declararse.

## 📖 Desarrollo

### 1. Definición operacional: mecanismo central

**Definición operacional** se entiende aquí como **especificación de numerador, denominador, ventana y fuente**.

Medir conversión exige tres definiciones previas: qué cuenta como entrada, qué cuenta como conversión y en qué ventana. Sin las tres, dos personas calculan cifras distintas de la misma operación y ambas tienen razón. La mayoría de las discusiones sobre tasas de conversión son en realidad discusiones sobre definiciones no explicitadas.

**De dónde viene esta afirmación.** Avinash Kaushik — *Web Analytics 2.0* (2009) aporta la idea que sostiene este bloque: la segmentación como condición para que un promedio signifique algo. Búscala en el capítulo sobre segmentación de datos. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «conversión con definición documentada» debería moverse cuando cambie **definición operacional**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **unidad de análisis**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Unidad de análisis: frontera conceptual y error de clasificación

**Definición operacional:** elección entre visitas, sesiones, personas o cuentas como base del cálculo. Su valor está en distinguirlo de **definición operacional**.

La unidad de análisis determina qué significa el número: conversión por visita, por visitante o por sesión son métricas distintas que pueden moverse en direcciones opuestas. Elegir la unidad corresponde a la decisión que se quiere tomar, y esa elección debe declararse en la ficha junto con el resto.

**Contraste bibliográfico.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) aporta aquí una distinción concreta: las cinco etapas —empatía, adherencia, viralidad, ingreso y escala— con su métrica propia (la parte sobre etapas del negocio). Formula dos mini-casos: uno que satisface la definición de **unidad de análisis** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «especificar numerador, denominador y ventana», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Ventana de conversión: operacionalización y medición

**Ventana de conversión** significa **periodo dentro del cual se considera que la conversión ocurrió**.

La comparabilidad entre periodos exige que la mezcla de tráfico sea similar. Una tasa que mejora porque aumentó la proporción de visitantes recurrentes no indica que la página mejorara. Segmentar por origen antes de comparar es lo que evita atribuir a la gestión lo que produjo el cambio de composición.

Ficha de medición obligatoria para **conversión con definición documentada**: `métricas con definición publicada, sobre métricas reportadas`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) pone una condición sobre la medición: la evaluación contra una línea base y no contra la nada (los capítulos sobre evaluación de modelos). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Comparabilidad: trade-offs y efectos de segundo orden

**Definición:** condición que permite contrastar cifras entre periodos o canales.

Ventanas de conversión largas capturan más conversiones y atribuyen a un contacto efectos que pudieron tener otras causas; ventanas cortas subestiman. La elección debe corresponder al ciclo de compra observado, y ese dato hay que medirlo en lugar de adoptar el valor por defecto de la herramienta.

**Lo que aporta la fuente.** Donald J. Wheeler — *Understanding Variation* (2000) aporta el criterio para pesar el intercambio: el error de comparar dos puntos consecutivos y llamarlo tendencia (los capítulos sobre interpretación de series). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **consistencia entre informes** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **comparabilidad** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «publicar las definiciones junto con las cifras», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Una tasa de conversión describe una relación entre dos conteos y no explica nada por sí sola. Su valor aparece en la comparación —con periodos anteriores, entre segmentos, contra una línea base— y siempre acompañada del volumen absoluto, porque una tasa excelente sobre pocas unidades puede ser irrelevante para el negocio.

**Frontera declarada.** Las definiciones no pueden cambiarse retroactivamente sin recalcular la serie. Un cambio de definición rompe la comparabilidad histórica y debe declararse. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar conversión y embudos no consiste en sumar definiciones. Empieza por **definición operacional**, contrasta **unidad de análisis** con **ventana de conversión**, incorpora **comparabilidad** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Avinash Kaushik — *Web Analytics 2.0* (2009) | La segmentación como condición para que un promedio signifique algo | El capítulo sobre segmentación de datos | ¿Qué debería observarse en **definición operacional** si aquí opera «la segmentación como condición para que un promedio signifique algo»? ¿Y qué observación lo desmentiría en este caso? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | Las cinco etapas —empatía, adherencia, viralidad, ingreso y escala— con su métrica propia | La parte sobre etapas del negocio | ¿Qué debería observarse en **unidad de análisis** si aquí opera «las cinco etapas —empatía, adherencia, viralidad, ingreso y escala— con su métrica propia»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La evaluación contra una línea base y no contra la nada | Los capítulos sobre evaluación de modelos | ¿Qué debería observarse en **ventana de conversión** si aquí opera «la evaluación contra una línea base y no contra la nada»? ¿Y qué observación lo desmentiría en este caso? |
| Donald J. Wheeler — *Understanding Variation* (2000) | El error de comparar dos puntos consecutivos y llamarlo tendencia | Los capítulos sobre interpretación de series | ¿Qué debería observarse en **comparabilidad** si aquí opera «el error de comparar dos puntos consecutivos y llamarlo tendencia»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Marketing reporta 3,2 % de conversión sobre sesiones y ventas calcula 0,9 % sobre personas únicas. Ambos hablan del mismo embudo en la misma reunión.

**Paso 1 — Definir la unidad de análisis y justificarla.** El equipo escribe primero el supuesto asociado a **definición operacional** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **conversión con definición documentada** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Especificar numerador, denominador y ventana.** El trabajo aquí es separar lo observado de lo inferido sobre **unidad de análisis**. La evidencia que ordena la discusión es **diferencia entre unidades de análisis**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Documentar la fuente de cada componente.** El riesgo de este paso es cerrar demasiado rápido alrededor de **ventana de conversión**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **consistencia entre informes** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Verificar la comparabilidad antes de contrastar.** Con **comparabilidad** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **conversión con definición documentada** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Publicar las definiciones junto con las cifras.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **definición operacional**. **diferencia entre unidades de análisis** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **definición operacional** | Especificación de numerador, denominador, ventana y fuente | Cuando **conversión con definición documentada** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **unidad de análisis** | Elección entre visitas, sesiones, personas o cuentas como base del cálculo | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Las definiciones no pueden cambiarse retroactivamente sin recalcular la serie. Un cambio de definición rompe la comparabilidad histórica y debe declararse.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre conversión y embudos |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing analyst, Revenue analyst y Data-driven marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Marketing reporta 3,2 % de conversión sobre sesiones y ventas calcula 0,9 % sobre personas únicas. Ambos hablan del mismo embudo en la misma reunión.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir la unidad de análisis y justificarla → especificar numerador, denominador y ventana → documentar la fuente de cada componente → verificar la comparabilidad antes de contrastar → publicar las definiciones junto con las cifras** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **conversión con definición documentada**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Web Analytics 2.0* y la de *Lean Analytics*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **definición operacional** y **unidad de análisis** como sinónimos | Se perdió la distinción entre «especificación de numerador, denominador, ventana y fuente» y «elección entre visitas, sesiones, personas o cuentas como base del cálculo» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «publicar las definiciones junto con las cifras» | Se saltó «definir la unidad de análisis y justificarla»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **conversión con definición documentada** | La métrica local reemplazó al resultado del sistema | Contrástala con **consistencia entre informes** y explicita el costo de oportunidad. |
| Reportar tasas sin unidad de análisis declarada | Error específico de esta clase | Publica numerador, denominador, ventana y fuente junto a cada tasa. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **definición operacional** y **unidad de análisis** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **ventana de conversión** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir la unidad de análisis y justificarla» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **conversión con definición documentada** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Las definiciones no pueden cambiarse retroactivamente sin recalcular la serie. Un cambio de definición rompe la comparabilidad histórica y debe declararse»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **ventana de conversión** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **conversión con definición documentada**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Web Analytics 2.0* y *Understanding Variation*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P20-C02-conversion-y-funnels/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **conversión con definición documentada**, **diferencia entre unidades de análisis** y **consistencia entre informes** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **caso analítico integral con árbol de métricas, cohortes, incrementalidad y dashboard ejecutivo**.

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

- Avinash Kaushik — *Web Analytics 2.0* (2009) — **aporta a esta clase:** la segmentación como condición para que un promedio signifique algo. **Dónde buscarlo:** el capítulo sobre segmentación de datos. Registra edición y páginas consultadas en tu nota de lectura.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — **aporta a esta clase:** las cinco etapas —empatía, adherencia, viralidad, ingreso y escala— con su métrica propia. **Dónde buscarlo:** la parte sobre etapas del negocio. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — **aporta a esta clase:** la evaluación contra una línea base y no contra la nada. **Dónde buscarlo:** los capítulos sobre evaluación de modelos. Registra edición y páginas consultadas en tu nota de lectura.
- Donald J. Wheeler — *Understanding Variation* (2000) — **aporta a esta clase:** el error de comparar dos puntos consecutivos y llamarlo tendencia. **Dónde buscarlo:** los capítulos sobre interpretación de series. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 01 · Árbol de métricas](class-01-arbol-de-metricas.md) · [Índice de la parte](README.md) · [Clase 03 · Costo de adquisición de cliente](class-03-cac.md) →
