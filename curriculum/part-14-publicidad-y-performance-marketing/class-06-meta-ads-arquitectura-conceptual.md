---
title: "Meta Ads: arquitectura conceptual"
type: class
language: es
standard: clase-profunda-v2
part: 14
class: 06
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["geddes", "sharp2", "kaushik", "binet-field"]
anchors: {"binet-field": "60-40", "geddes": "subasta", "kaushik": "multiplicidad", "sharp2": "situaciones-compra"}
updated: 2026-08-19
---

# Clase 14.06 — Meta Ads: arquitectura conceptual

Clase 6 de 14 de la parte [14 — Publicidad y performance marketing](README.md), de nivel Adquisición. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 14.05, *Google Ads: arquitectura conceptual*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de conversiones semanales por conjunto con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La mecánica de la subasta: no gana quien más paga sino quien combina oferta y relevancia — Brad Geddes. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

En plataformas sociales la demanda no está declarada: se interrumpe a personas que no buscaban nada. Eso cambia la lógica: la creatividad y la propuesta hacen el trabajo que en búsqueda hacía la intención. La estructura tiende a ser más simple y el aprendizaje del sistema requiere volumen de señal; fragmentar demasiado impide que la optimización funcione.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 14 busca **invertir en medios pagados con control de costo, calidad y riesgo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **meta Ads: arquitectura conceptual** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué unidad de resultado estoy comprando y a qué costo marginal deja de tener sentido?

Los conceptos que estructuran la sesión son **demanda no declarada**, **fase de aprendizaje**, **fragmentación excesiva** y **gancho inicial**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `demanda no declarada`, `fase de aprendizaje`, `fragmentación excesiva` y `gancho inicial` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Publicidad y performance marketing**.
3. **Aplicar** la secuencia **definir la propuesta que justifica interrumpir → consolidar conjuntos para alcanzar volumen de señal → priorizar el gancho inicial en la creatividad → esperar a superar la fase de aprendizaje antes de juzgar → evaluar por costo por resultado de negocio** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **conversiones semanales por conjunto**, **tasa de retención de atención** y **costo por oportunidad calificada** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **demanda no declarada** y **fase de aprendizaje** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **conversiones semanales por conjunto**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **demanda no declarada** | situación en que la audiencia no está buscando activamente la solución | Da un hecho compatible con la definición y otro que la refute. |
| **fase de aprendizaje** | periodo en que el sistema necesita señal suficiente para optimizar | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **fragmentación excesiva** | división del presupuesto en demasiados conjuntos que impide el aprendizaje | Construye un caso límite donde el concepto se confunde con el anterior. |
| **gancho inicial** | primer segundo o primera línea que determina si la persona detiene el desplazamiento | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir la propuesta que justifica interrumpir → 2. consolidar conjuntos para alcanzar volumen de señal → 3. priorizar el gancho inicial en la creatividad → 4. esperar a superar la fase de aprendizaje antes de juzgar → 5. evaluar por costo por resultado de negocio
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Los cambios de privacidad afectan la medición y la optimización en estas plataformas. Los resultados reportados pueden diferir de los registrados internamente.

## 📖 Desarrollo

### 1. Demanda no declarada: mecanismo central

**Demanda no declarada** se entiende aquí como **situación en que la audiencia no está buscando activamente la solución**.

Las plataformas sociales operan sobre demanda no declarada: la persona no está buscando resolver el problema en ese momento. Eso cambia el trabajo del anuncio, que debe primero establecer relevancia y sólo después proponer una acción. Aplicar la lógica de búsqueda —anuncio directo con llamada a la acción inmediata— produce costos altos y conclusiones equivocadas.

**De dónde viene esta afirmación.** Brad Geddes — *Advanced Google AdWords* (2014, 3.ª ed.) aporta la idea que sostiene este bloque: la mecánica de la subasta: no gana quien más paga sino quien combina oferta y relevancia. Búscala en los capítulos sobre funcionamiento de la subasta. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «conversiones semanales por conjunto» debería moverse cuando cambie **demanda no declarada**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **fase de aprendizaje**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Fase de aprendizaje: frontera conceptual y error de clasificación

**Definición operacional:** periodo en que el sistema necesita señal suficiente para optimizar. Su valor está en distinguirlo de **demanda no declarada**.

El gancho inicial es la restricción operativa: los primeros segundos o la primera línea deciden si el resto se ve. No es un asunto de producción sino de mensaje: qué situación reconocible se plantea de inmediato. Un anuncio que empieza presentando la empresa desperdicia exactamente el momento en que tenía atención.

**Contraste bibliográfico.** Jenni Romaniuk y Byron Sharp — *How Brands Grow: Part 2* (2015) aporta aquí una distinción concreta: las situaciones de compra como puntos de entrada a la memoria de categoría (el capítulo sobre puntos de entrada de categoría). Formula dos mini-casos: uno que satisface la definición de **fase de aprendizaje** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «consolidar conjuntos para alcanzar volumen de señal», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Fragmentación excesiva: operacionalización y medición

**Fragmentación excesiva** significa **división del presupuesto en demasiados conjuntos que impide el aprendizaje**.

La fase de aprendizaje de los sistemas automatizados requiere un volumen mínimo de eventos para estabilizar. Intervenir durante esa fase —cambiar presupuesto, audiencia o creatividad— reinicia el proceso y produce resultados erráticos. Definir un periodo de no intervención antes de lanzar evita la reacción impulsiva ante los primeros números.

Ficha de medición obligatoria para **conversiones semanales por conjunto**: `conversiones registradas por conjunto, comparadas con el mínimo de aprendizaje`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Avinash Kaushik — *Web Analytics 2.0* (2009) pone una condición sobre la medición: la multiplicidad: combinar clics, resultados, experiencia y competencia (los capítulos sobre analítica multicanal). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Gancho inicial: trade-offs y efectos de segundo orden

**Definición:** primer segundo o primera línea que determina si la persona detiene el desplazamiento.

Fragmentar en muchas campañas y conjuntos permite control y reparte el volumen de eventos, con lo que ninguno alcanza a salir de la fase de aprendizaje. Consolidar mejora el aprendizaje y reduce el control granular. Con presupuestos moderados, la consolidación suele ser la decisión correcta aunque resulte contraintuitiva.

**Lo que aporta la fuente.** Les Binet y Peter Field — *The Long and the Short of It* (2013) aporta el criterio para pesar el intercambio: la proporción entre inversión en construcción de marca y en activación de ventas (la sección sobre asignación óptima del presupuesto). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **costo por oportunidad calificada** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **gancho inicial** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «evaluar por costo por resultado de negocio», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Las plataformas sociales son especialmente sensibles a cambios de política de privacidad y de medición, que han reducido la precisión de la atribución. Evaluar su contribución sólo con los datos de la plataforma sobreestima o subestima según el caso. Contrastar con datos propios de origen declarado es una verificación necesaria.

**Frontera declarada.** Los cambios de privacidad afectan la medición y la optimización en estas plataformas. Los resultados reportados pueden diferir de los registrados internamente. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Atribuirse demanda existente, inflar el retorno y decidir presupuesto sobre una ilusión.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar meta Ads: arquitectura conceptual no consiste en sumar definiciones. Empieza por **demanda no declarada**, contrasta **fase de aprendizaje** con **fragmentación excesiva**, incorpora **gancho inicial** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Brad Geddes — *Advanced Google AdWords* (2014, 3.ª ed.) | La mecánica de la subasta: no gana quien más paga sino quien combina oferta y relevancia | Los capítulos sobre funcionamiento de la subasta | ¿Qué debería observarse en **demanda no declarada** si aquí opera «la mecánica de la subasta: no gana quien más paga sino quien combina oferta y relevancia»? ¿Y qué observación lo desmentiría en este caso? |
| Jenni Romaniuk y Byron Sharp — *How Brands Grow: Part 2* (2015) | Las situaciones de compra como puntos de entrada a la memoria de categoría | El capítulo sobre puntos de entrada de categoría | ¿Qué debería observarse en **fase de aprendizaje** si aquí opera «las situaciones de compra como puntos de entrada a la memoria de categoría»? ¿Y qué observación lo desmentiría en este caso? |
| Avinash Kaushik — *Web Analytics 2.0* (2009) | La multiplicidad: combinar clics, resultados, experiencia y competencia | Los capítulos sobre analítica multicanal | ¿Qué debería observarse en **fragmentación excesiva** si aquí opera «la multiplicidad: combinar clics, resultados, experiencia y competencia»? ¿Y qué observación lo desmentiría en este caso? |
| Les Binet y Peter Field — *The Long and the Short of It* (2013) | La proporción entre inversión en construcción de marca y en activación de ventas | La sección sobre asignación óptima del presupuesto | ¿Qué debería observarse en **gancho inicial** si aquí opera «la proporción entre inversión en construcción de marca y en activación de ventas»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina dividió CLP 900.000 mensuales en 14 conjuntos de anuncios. Ninguno acumula señal suficiente y el sistema no logra optimizar.

**Paso 1 — Definir la propuesta que justifica interrumpir.** El equipo escribe primero el supuesto asociado a **demanda no declarada** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **conversiones semanales por conjunto** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Consolidar conjuntos para alcanzar volumen de señal.** El trabajo aquí es separar lo observado de lo inferido sobre **fase de aprendizaje**. La evidencia que ordena la discusión es **tasa de retención de atención**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Priorizar el gancho inicial en la creatividad.** El riesgo de este paso es cerrar demasiado rápido alrededor de **fragmentación excesiva**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **costo por oportunidad calificada** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Esperar a superar la fase de aprendizaje antes de juzgar.** Con **gancho inicial** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **conversiones semanales por conjunto** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Evaluar por costo por resultado de negocio.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **demanda no declarada**. **tasa de retención de atención** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **demanda no declarada** | Situación en que la audiencia no está buscando activamente la solución | Cuando **conversiones semanales por conjunto** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **fase de aprendizaje** | Periodo en que el sistema necesita señal suficiente para optimizar | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Los cambios de privacidad afectan la medición y la optimización en estas plataformas. Los resultados reportados pueden diferir de los registrados internamente.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre meta Ads: arquitectura conceptual |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Performance marketer, Media buyer y Growth marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina dividió CLP 900.000 mensuales en 14 conjuntos de anuncios. Ninguno acumula señal suficiente y el sistema no logra optimizar.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir la propuesta que justifica interrumpir → consolidar conjuntos para alcanzar volumen de señal → priorizar el gancho inicial en la creatividad → esperar a superar la fase de aprendizaje antes de juzgar → evaluar por costo por resultado de negocio** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **conversiones semanales por conjunto**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Advanced Google AdWords* y la de *How Brands Grow: Part 2*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **demanda no declarada** y **fase de aprendizaje** como sinónimos | Se perdió la distinción entre «situación en que la audiencia no está buscando activamente la solución» y «periodo en que el sistema necesita señal suficiente para optimizar» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «evaluar por costo por resultado de negocio» | Se saltó «definir la propuesta que justifica interrumpir»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **conversiones semanales por conjunto** | La métrica local reemplazó al resultado del sistema | Contrástala con **costo por oportunidad calificada** y explicita el costo de oportunidad. |
| Fragmentar el presupuesto en demasiados conjuntos | Error específico de esta clase | Consolida hasta alcanzar el volumen de señal que la optimización requiere. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **demanda no declarada** y **fase de aprendizaje** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **fragmentación excesiva** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir la propuesta que justifica interrumpir» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **conversiones semanales por conjunto** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Los cambios de privacidad afectan la medición y la optimización en estas plataformas. Los resultados reportados pueden diferir de los registrados internamente»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **fragmentación excesiva** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **conversiones semanales por conjunto**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Advanced Google AdWords* y *The Long and the Short of It*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Atribuirse demanda existente, inflar el retorno y decidir presupuesto sobre una ilusión.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P14-C06-meta-ads-arquitectura-conceptual/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **conversiones semanales por conjunto**, **tasa de retención de atención** y **costo por oportunidad calificada** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **plan de performance con estructura de campañas, presupuestos, medición y salvaguardas**.

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

- Brad Geddes — [*Advanced Google AdWords*](https://openlibrary.org/isbn/9781118819647) (2014, 3.ª ed.) · ISBN 9781118819647 — **aporta a esta clase:** la mecánica de la subasta: no gana quien más paga sino quien combina oferta y relevancia. **Dónde buscarlo:** los capítulos sobre funcionamiento de la subasta. Registra edición y páginas consultadas en tu nota de lectura.
- Jenni Romaniuk y Byron Sharp — [*How Brands Grow: Part 2*](https://openlibrary.org/isbn/9780195596267) (2015) · ISBN 9780195596267 — **aporta a esta clase:** las situaciones de compra como puntos de entrada a la memoria de categoría. **Dónde buscarlo:** el capítulo sobre puntos de entrada de categoría. Registra edición y páginas consultadas en tu nota de lectura.
- Avinash Kaushik — [*Web Analytics 2.0*](https://openlibrary.org/isbn/9780470596425) (2009) · ISBN 9780470596425 — **aporta a esta clase:** la multiplicidad: combinar clics, resultados, experiencia y competencia. **Dónde buscarlo:** los capítulos sobre analítica multicanal. Registra edición y páginas consultadas en tu nota de lectura.
- Les Binet y Peter Field — [*The Long and the Short of It*](https://openlibrary.org/isbn/9780852941348) (2013) · ISBN 9780852941348 — **aporta a esta clase:** la proporción entre inversión en construcción de marca y en activación de ventas. **Dónde buscarlo:** la sección sobre asignación óptima del presupuesto. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 05 · Google Ads: arquitectura conceptual](class-05-google-ads-arquitectura-conceptual.md) · [Índice de la parte](README.md) · [Clase 07 · LinkedIn Ads: arquitectura conceptual](class-07-linkedin-ads-arquitectura-conceptual.md) →
