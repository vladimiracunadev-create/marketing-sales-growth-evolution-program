---
title: "Analítica digital"
type: class
language: es
standard: clase-profunda-v2
part: 12
class: 10
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["kaushik", "provost", "croll-yoskovitz", "wheeler-dv"]
anchors: {"croll-yoskovitz": "una-metrica", "kaushik": "vanidad", "provost": "formulacion", "wheeler-dv": "graficos-control"}
updated: 2026-08-19
---

# Clase 12.10 — Analítica digital

**Parte 12 · Marketing digital y adquisición** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 12.09 — *Conversión web*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de decisiones informadas por analítica para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La distinción entre métricas de vanidad y métricas accionables — Avinash Kaushik. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La analítica digital sirve para tomar decisiones, no para llenar tableros. Kaushik distingue entre métricas que informan acción y métricas de vanidad que sólo producen sensación de control. La condición previa es un plan de medición: qué decisiones se tomarán, qué preguntas las informan, qué eventos hay que registrar y con qué definición. Sin ese plan, se instrumenta todo y no se usa nada.

Antes de cualquier herramienta, esta clase obliga a nombrar qué cambiaría si el análisis fuese correcto. La parte 12 busca **operar un sistema digital de adquisición medible de punta a punta**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **analítica digital** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué activo digital genera demanda propia y qué parte del resultado es alquilada?

Los conceptos que estructuran la sesión son **plan de medición**, **métrica de vanidad**, **segmentación analítica** y **calidad del dato**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `plan de medición`, `métrica de vanidad`, `segmentación analítica` y `calidad del dato` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Marketing digital y adquisición**.
3. **Aplicar** la secuencia **definir las decisiones que la analítica debe informar → traducirlas a preguntas y métricas con definición operacional → instrumentar sólo lo necesario y verificar la calidad → analizar por segmento y no sólo el agregado → revisar el plan cada semestre y eliminar lo que no se usa** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **decisiones informadas por analítica**, **calidad de la instrumentación** y **métricas activas sin uso** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **plan de medición** y **métrica de vanidad** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **decisiones informadas por analítica**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **plan de medición** | documento que vincula decisiones, preguntas, métricas y eventos a registrar | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **métrica de vanidad** | indicador que sube sin relación con el resultado de negocio | Da un hecho compatible con la definición y otro que la refute. |
| **segmentación analítica** | análisis por grupos que revela diferencias ocultas en el promedio | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **calidad del dato** | grado en que la instrumentación registra correctamente lo que ocurre | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir las decisiones que la analítica debe informar → 2. traducirlas a preguntas y métricas con definición operacional → 3. instrumentar sólo lo necesario y verificar la calidad → 4. analizar por segmento y no sólo el agregado → 5. revisar el plan cada semestre y eliminar lo que no se usa
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Las restricciones de privacidad y el bloqueo de rastreadores reducen la cobertura de la analítica digital. Los datos deben leerse como muestra sesgada y no como censo.

## 📖 Desarrollo

### 1. Plan de medición: mecanismo central

**Plan de medición** se entiende aquí como **documento que vincula decisiones, preguntas, métricas y eventos a registrar**.

La analítica digital es útil cuando parte de la decisión y no del dato disponible. Avinash Kaushik propone una prueba directa para cada informe: preguntar tres veces «¿y entonces qué?». Si al tercer intento no aparece una acción, el informe no debería existir, por más que las cifras sean correctas.

**De dónde viene esta afirmación.** Avinash Kaushik — *Web Analytics 2.0* (2009) aporta la idea que sostiene este bloque: la distinción entre métricas de vanidad y métricas accionables. Búscala en los capítulos sobre selección de métricas. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «decisiones informadas por analítica» debería moverse cuando cambie **plan de medición**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **métrica de vanidad**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Métrica de vanidad: frontera conceptual y error de clasificación

**Definición operacional:** indicador que sube sin relación con el resultado de negocio. Su valor está en distinguirlo de **plan de medición**.

La métrica de vanidad se reconoce porque siempre sube y nunca cambia una decisión: visitas acumuladas, seguidores totales, impresiones. No son falsas; son irrelevantes para la gestión. Sustituirlas por métricas de conversión y de calidad de tráfico suele reducir el tamaño del tablero y aumentar su utilidad.

**Contraste bibliográfico.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta aquí una distinción concreta: la formulación del problema de negocio como problema de datos antes de elegir técnica (los capítulos iniciales sobre pensamiento analítico). Formula dos mini-casos: uno que satisface la definición de **métrica de vanidad** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «traducirlas a preguntas y métricas con definición operacional», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Segmentación analítica: operacionalización y medición

**Segmentación analítica** significa **análisis por grupos que revela diferencias ocultas en el promedio**.

La segmentación es la condición para que un promedio signifique algo. Una tasa de conversión global mezcla tráfico de marca con tráfico frío, móvil con escritorio, clientes con desconocidos. Analizar sin segmentar produce conclusiones sobre un promedio que no describe a nadie, y decisiones que no mejoran a ningún grupo.

Ficha de medición obligatoria para **decisiones informadas por analítica**: `decisiones documentadas que citan un análisis, por trimestre`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) pone una condición sobre la medición: la métrica que importa ahora: una sola, según etapa y modelo de negocio (los capítulos sobre la métrica única). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Calidad del dato: trade-offs y efectos de segundo orden

**Definición:** grado en que la instrumentación registra correctamente lo que ocurre.

Medir más entrega mejor comprensión y aumenta el costo de implementación y mantenimiento, además de las obligaciones sobre datos. Cada evento adicional exige definición, verificación y documentación. Un plan de medición que empieza por la decisión suele necesitar menos eventos de los que el equipo técnico propone.

**Lo que aporta la fuente.** Donald J. Wheeler — *Understanding Variation* (2000) aporta el criterio para pesar el intercambio: los gráficos de comportamiento del proceso como filtro entre señal y ruido (los capítulos sobre gráficos de control). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **métricas activas sin uso** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **calidad del dato** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar el plan cada semestre y eliminar lo que no se usa», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La calidad del dato limita todo lo demás. Bloqueadores, consentimiento, dispositivos múltiples y cambios de plataforma producen huecos que no siempre son visibles. Un análisis riguroso declara qué proporción del tráfico está efectivamente medida y cómo ese hueco podría sesgar la conclusión.

**Frontera declarada.** Las restricciones de privacidad y el bloqueo de rastreadores reducen la cobertura de la analítica digital. Los datos deben leerse como muestra sesgada y no como censo. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Optimizar métricas de vanidad y desatender consentimiento, cookies y datos personales.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar analítica digital no consiste en sumar definiciones. Empieza por **plan de medición**, contrasta **métrica de vanidad** con **segmentación analítica**, incorpora **calidad del dato** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Avinash Kaushik — *Web Analytics 2.0* (2009) | La distinción entre métricas de vanidad y métricas accionables | Los capítulos sobre selección de métricas | ¿Qué debería observarse en **plan de medición** si aquí opera «la distinción entre métricas de vanidad y métricas accionables»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La formulación del problema de negocio como problema de datos antes de elegir técnica | Los capítulos iniciales sobre pensamiento analítico | ¿Qué debería observarse en **métrica de vanidad** si aquí opera «la formulación del problema de negocio como problema de datos antes de elegir técnica»? ¿Y qué observación lo desmentiría en este caso? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | La métrica que importa ahora: una sola, según etapa y modelo de negocio | Los capítulos sobre la métrica única | ¿Qué debería observarse en **segmentación analítica** si aquí opera «la métrica que importa ahora: una sola, según etapa y modelo de negocio»? ¿Y qué observación lo desmentiría en este caso? |
| Donald J. Wheeler — *Understanding Variation* (2000) | Los gráficos de comportamiento del proceso como filtro entre señal y ruido | Los capítulos sobre gráficos de control | ¿Qué debería observarse en **calidad del dato** si aquí opera «los gráficos de comportamiento del proceso como filtro entre señal y ruido»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El tablero de Ruta Andina tiene 34 métricas. En la reunión mensual se revisan tres y ninguna cambia una decisión.

**Paso 1 — Definir las decisiones que la analítica debe informar.** El equipo escribe primero el supuesto asociado a **plan de medición** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **decisiones informadas por analítica** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Traducirlas a preguntas y métricas con definición operacional.** El trabajo aquí es separar lo observado de lo inferido sobre **métrica de vanidad**. La evidencia que ordena la discusión es **calidad de la instrumentación**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Instrumentar sólo lo necesario y verificar la calidad.** El riesgo de este paso es cerrar demasiado rápido alrededor de **segmentación analítica**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **métricas activas sin uso** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Analizar por segmento y no sólo el agregado.** Con **calidad del dato** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **decisiones informadas por analítica** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar el plan cada semestre y eliminar lo que no se usa.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **plan de medición**. **calidad de la instrumentación** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **plan de medición** | Documento que vincula decisiones, preguntas, métricas y eventos a registrar | Cuando **decisiones informadas por analítica** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **métrica de vanidad** | Indicador que sube sin relación con el resultado de negocio | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Las restricciones de privacidad y el bloqueo de rastreadores reducen la cobertura de la analítica digital. Los datos deben leerse como muestra sesgada y no como censo.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre analítica digital |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Digital marketing manager, Growth marketer y Especialista SEO/SEM. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El tablero de Ruta Andina tiene 34 métricas. En la reunión mensual se revisan tres y ninguna cambia una decisión.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir las decisiones que la analítica debe informar → traducirlas a preguntas y métricas con definición operacional → instrumentar sólo lo necesario y verificar la calidad → analizar por segmento y no sólo el agregado → revisar el plan cada semestre y eliminar lo que no se usa** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **decisiones informadas por analítica**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Web Analytics 2.0* y la de *Data Science for Business*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **plan de medición** y **métrica de vanidad** como sinónimos | Se perdió la distinción entre «documento que vincula decisiones, preguntas, métricas y eventos a registrar» y «indicador que sube sin relación con el resultado de negocio» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar el plan cada semestre y eliminar lo que no se usa» | Se saltó «definir las decisiones que la analítica debe informar»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **decisiones informadas por analítica** | La métrica local reemplazó al resultado del sistema | Contrástala con **métricas activas sin uso** y explicita el costo de oportunidad. |
| Instrumentar todo sin plan de medición | Error específico de esta clase | Parte de las decisiones y elimina del tablero toda métrica que no informe una de ellas. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **plan de medición** y **métrica de vanidad** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **segmentación analítica** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir las decisiones que la analítica debe informar» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **decisiones informadas por analítica** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Las restricciones de privacidad y el bloqueo de rastreadores reducen la cobertura de la analítica digital. Los datos deben leerse como muestra sesgada y no como censo»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **segmentación analítica** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **decisiones informadas por analítica**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Web Analytics 2.0* y *Understanding Variation*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Optimizar métricas de vanidad y desatender consentimiento, cookies y datos personales.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P12-C10-analitica-digital/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **decisiones informadas por analítica**, **calidad de la instrumentación** y **métricas activas sin uso** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **plan de adquisición digital con arquitectura de sitio, canales, medición y auditoría inicial**.

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

- Avinash Kaushik — *Web Analytics 2.0* (2009) — **aporta a esta clase:** la distinción entre métricas de vanidad y métricas accionables. **Dónde buscarlo:** los capítulos sobre selección de métricas. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — **aporta a esta clase:** la formulación del problema de negocio como problema de datos antes de elegir técnica. **Dónde buscarlo:** los capítulos iniciales sobre pensamiento analítico. Registra edición y páginas consultadas en tu nota de lectura.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — **aporta a esta clase:** la métrica que importa ahora: una sola, según etapa y modelo de negocio. **Dónde buscarlo:** los capítulos sobre la métrica única. Registra edición y páginas consultadas en tu nota de lectura.
- Donald J. Wheeler — *Understanding Variation* (2000) — **aporta a esta clase:** los gráficos de comportamiento del proceso como filtro entre señal y ruido. **Dónde buscarlo:** los capítulos sobre gráficos de control. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 09 · Conversión web](class-09-conversion-web.md) · [Índice de la parte](README.md) · [Clase 11 · Atribución básica](class-11-atribucion-basica.md) →
