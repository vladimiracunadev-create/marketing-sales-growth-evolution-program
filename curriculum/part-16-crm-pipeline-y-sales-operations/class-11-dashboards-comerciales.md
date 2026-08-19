---
title: "Dashboards comerciales"
type: class
language: es
standard: clase-profunda-v1
part: 16
class: 11
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["kaushik", "grove", "kaplan-norton", "wheeler-dv"]
updated: 2026-08-19
---

# Clase 16.11 — Dashboards comerciales

**Parte 16 · CRM, pipeline y sales operations** · Nivel: Operación de ingresos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

## 🎯 Propósito

Un tablero comercial debe responder tres preguntas: cómo vamos, qué está en riesgo y qué requiere decisión. Todo lo demás sobra. El error habitual es acumular gráficos hasta que nadie los mira: un tablero con treinta métricas no informa, distrae. La regla de diseño es que cada elemento debe tener una acción asociada cuando se sale de rango.

El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta. La parte 16 busca **convertir el CRM en un sistema de trabajo y de verdad operacional**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **dashboards comerciales** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿El pipeline describe la realidad o solo el optimismo del equipo?

Los conceptos que estructuran la sesión son **métrica accionable**, **jerarquía del tablero**, **rango esperado** y **audiencia del tablero**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `métrica accionable`, `jerarquía del tablero`, `rango esperado` y `audiencia del tablero` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **CRM, pipeline y sales operations**.
3. **Aplicar** la secuencia **definir la audiencia y sus decisiones → elegir las métricas que informan esas decisiones → establecer rangos esperados y acciones asociadas → eliminar todo lo que no tenga acción → revisar el uso real del tablero cada trimestre** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **métricas con acción definida**, **uso del tablero** y **decisiones tomadas con el tablero** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **métrica accionable** y **jerarquía del tablero** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **métricas con acción definida**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **métrica accionable** | indicador con una acción definida cuando se desvía de su rango | Da un hecho compatible con la definición y otro que la refute. |
| **jerarquía del tablero** | orden que refleja la importancia de las decisiones que informa | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **rango esperado** | banda de variación normal que evita reaccionar al ruido | Construye un caso límite donde el concepto se confunde con el anterior. |
| **audiencia del tablero** | rol específico para el que se diseña el conjunto de indicadores | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir la audiencia y sus decisiones → 2. elegir las métricas que informan esas decisiones → 3. establecer rangos esperados y acciones asociadas → 4. eliminar todo lo que no tenga acción → 5. revisar el uso real del tablero cada trimestre
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un tablero no reemplaza la conversación de gestión. Su función es enfocar la discusión, no sustituir el juicio sobre casos particulares.

## 📖 Desarrollo

### 1. Métrica accionable: mecanismo central

**métrica accionable** se entiende aquí como **indicador con una acción definida cuando se desvía de su rango**. Es la pieza desde la que se inicia el análisis de dashboards comerciales: antes de «definir la audiencia y sus decisiones», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Avinash Kaushik — *Web Analytics 2.0* (2009). **Lente que aporta:** medición orientada a decisión, segmentación y crítica del dato de vanidad. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **métricas con acción definida**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **jerarquía del tablero**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Jerarquía del tablero: frontera conceptual y error de clasificación

**Definición operacional:** orden que refleja la importancia de las decisiones que informa. Su valor está en distinguirlo de **métrica accionable**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Andrew S. Grove — *High Output Management* (1983) —**lente:** output gerencial, indicadores adelantados y reuniones como herramienta de producción—. Formula dos mini-casos: uno que satisface la definición de **jerarquía del tablero** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **uso del tablero** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «elegir las métricas que informan esas decisiones», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Rango esperado: operacionalización y medición

**rango esperado** significa **banda de variación normal que evita reaccionar al ruido**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **métricas con acción definida**: `indicadores con acción asociada, sobre indicadores del tablero`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) orienta este bloque —**lente:** traducción de la estrategia en indicadores causalmente conectados—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Audiencia del tablero: trade-offs y efectos de segundo orden

**Definición:** rol específico para el que se diseña el conjunto de indicadores. Este concepto obliga a abandonar la idea de que dashboards comerciales tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «eliminar todo lo que no tenga acción», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Donald J. Wheeler — *Understanding Variation* (2000) —**lente:** distinguir variación común de variación especial antes de reaccionar a un KPI— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **decisiones tomadas con el tablero** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **audiencia del tablero** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar el uso real del tablero cada trimestre», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Donald J. Wheeler — *Understanding Variation* (2000) sirve para contrastar la recomendación final desde otro lente: distinguir variación común de variación especial antes de reaccionar a un KPI. La frontera de esta clase es explícita: Un tablero no reemplaza la conversación de gestión. Su función es enfocar la discusión, no sustituir el juicio sobre casos particulares. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Tomar decisiones de contratación y presupuesto sobre un pipeline que no representa la realidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar dashboards comerciales no consiste en sumar definiciones. Empieza por **métrica accionable**, contrasta **jerarquía del tablero** con **rango esperado**, incorpora **audiencia del tablero** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Avinash Kaushik — *Web Analytics 2.0* (2009) | medición orientada a decisión, segmentación y crítica del dato de vanidad | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Andrew S. Grove — *High Output Management* (1983) | output gerencial, indicadores adelantados y reuniones como herramienta de producción | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) | traducción de la estrategia en indicadores causalmente conectados | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Donald J. Wheeler — *Understanding Variation* (2000) | distinguir variación común de variación especial antes de reaccionar a un KPI | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El tablero comercial de Ruta Andina tiene 22 gráficos. En la reunión semanal se revisan dos y las decisiones se toman con una planilla aparte.

**Paso 1 — Definir la audiencia y sus decisiones.** El equipo escribe primero el supuesto asociado a **métrica accionable** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **métricas con acción definida** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Elegir las métricas que informan esas decisiones.** El trabajo aquí es separar lo observado de lo inferido sobre **jerarquía del tablero**. La evidencia que ordena la discusión es **uso del tablero**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Establecer rangos esperados y acciones asociadas.** El riesgo de este paso es cerrar demasiado rápido alrededor de **rango esperado**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **decisiones tomadas con el tablero** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Eliminar todo lo que no tenga acción.** Con **audiencia del tablero** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **métricas con acción definida** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar el uso real del tablero cada trimestre.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **métrica accionable**. **uso del tablero** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **métrica accionable** | Indicador con una acción definida cuando se desvía de su rango | Cuando **métricas con acción definida** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **jerarquía del tablero** | Orden que refleja la importancia de las decisiones que informa | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un tablero no reemplaza la conversación de gestión. Su función es enfocar la discusión, no sustituir el juicio sobre casos particulares.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre dashboards comerciales |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Sales operations, RevOps analyst y Jefe de ventas. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El tablero comercial de Ruta Andina tiene 22 gráficos. En la reunión semanal se revisan dos y las decisiones se toman con una planilla aparte.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **definir la audiencia y sus decisiones → elegir las métricas que informan esas decisiones → establecer rangos esperados y acciones asociadas → eliminar todo lo que no tenga acción → revisar el uso real del tablero cada trimestre** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **métricas con acción definida**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **métrica accionable** y **jerarquía del tablero** como sinónimos | Se perdió la distinción entre «indicador con una acción definida cuando se desvía de su rango» y «orden que refleja la importancia de las decisiones que informa» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar el uso real del tablero cada trimestre» | Se saltó «definir la audiencia y sus decisiones»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **métricas con acción definida** | La métrica local reemplazó al resultado del sistema | Contrástala con **decisiones tomadas con el tablero** y explicita el costo de oportunidad. |
| Acumular métricas sin acción asociada | Error específico de esta clase | Elimina del tablero toda métrica que no tenga una acción definida cuando se sale de rango. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **métrica accionable** y **jerarquía del tablero** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **rango esperado** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir la audiencia y sus decisiones» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **métricas con acción definida** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un tablero no reemplaza la conversación de gestión. Su función es enfocar la discusión, no sustituir el juicio sobre casos particulares»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Tomar decisiones de contratación y presupuesto sobre un pipeline que no representa la realidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P16-C11-dashboards-comerciales/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **métricas con acción definida**, **uso del tablero** y **decisiones tomadas con el tablero** con fuente, ventana y lectura prohibida.
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

- Avinash Kaushik — *Web Analytics 2.0* (2009). **Uso en esta clase:** medición orientada a decisión, segmentación y crítica del dato de vanidad. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Andrew S. Grove — *High Output Management* (1983). **Uso en esta clase:** output gerencial, indicadores adelantados y reuniones como herramienta de producción. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996). **Uso en esta clase:** traducción de la estrategia en indicadores causalmente conectados. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Donald J. Wheeler — *Understanding Variation* (2000). **Uso en esta clase:** distinguir variación común de variación especial antes de reaccionar a un KPI. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 10 · Velocidad comercial](class-10-sales-velocity.md) · [Índice de la parte](README.md) · [Clase 12 · Revisión de pipeline](class-12-revision-de-pipeline.md) →
