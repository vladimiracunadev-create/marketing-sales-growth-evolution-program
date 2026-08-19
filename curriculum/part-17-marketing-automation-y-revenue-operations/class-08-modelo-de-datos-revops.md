---
title: "Modelo de datos de RevOps"
type: class
language: es
standard: clase-profunda-v3
part: 17
class: 08
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["diorio", "provost", "roberge", "kaplan-norton"]
updated: 2026-08-18
---

# Clase 17.08 — Modelo de datos de RevOps

**Parte 17 · Marketing automation y revenue operations** · Nivel: Operación de ingresos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v3`

## 🎯 Propósito

El modelo de datos es la infraestructura invisible de las decisiones comerciales. Define qué entidades existen, cómo se relacionan, qué estados son válidos y de dónde proviene cada dato. Cuando no está diseñado, cada informe requiere reconciliación manual y cada pregunta nueva exige un proyecto. Diseñarlo es más barato que rehacerlo después de tres años de deuda.

El punto de partida de esta clase no es la definición sino la decisión que la definición debe mejorar. La parte 17 busca **integrar marketing, ventas y servicio en un solo modelo de datos y de proceso**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **modelo de datos de RevOps** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué automatizo porque mejora el sistema y qué estaría solo escalando un desorden?

Los conceptos que estructuran la sesión son **entidad**, **fuente autoritativa**, **estado válido** y **deuda de datos**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `entidad`, `fuente autoritativa`, `estado válido` y `deuda de datos` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Marketing automation y revenue operations**.
3. **Aplicar** la secuencia **inventariar entidades y sistemas actuales → definir la fuente autoritativa de cada dato → documentar estados válidos y transiciones → resolver las inconsistencias más costosas primero → establecer el proceso de cambio del modelo** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **datos con fuente autoritativa definida**, **inconsistencias entre sistemas** y **tiempo de respuesta a preguntas nuevas** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **entidad** y **fuente autoritativa** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **datos con fuente autoritativa definida**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **entidad** | objeto del modelo que representa algo real: cuenta, contacto, oportunidad, suscripción | Construye un caso límite donde el concepto se confunde con el anterior. |
| **fuente autoritativa** | sistema que contiene la versión válida de cada dato | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **estado válido** | conjunto de valores permitidos para un campo y sus transiciones posibles | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **deuda de datos** | acumulación de inconsistencias que encarece cada análisis futuro | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. inventariar entidades y sistemas actuales → 2. definir la fuente autoritativa de cada dato → 3. documentar estados válidos y transiciones → 4. resolver las inconsistencias más costosas primero → 5. establecer el proceso de cambio del modelo
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un modelo perfecto que exige rehacer todos los sistemas no se implementa. El diseño debe priorizar lo que produce más valor con menos disrupción.

## 📖 Desarrollo

### 1. Entidad: mecanismo central

**entidad** se entiende aquí como **objeto del modelo que representa algo real: cuenta, contacto, oportunidad, suscripción**. Es la pieza desde la que se inicia el análisis de modelo de datos de RevOps: antes de «inventariar entidades y sistemas actuales», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022). **Lente que aporta:** integración de datos, procesos y equipos que producen ingreso como un solo sistema. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **datos con fuente autoritativa definida**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **fuente autoritativa**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Fuente autoritativa: frontera conceptual y error de clasificación

**Definición operacional:** sistema que contiene la versión válida de cada dato. Su valor está en distinguirlo de **entidad**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Foster Provost y Tom Fawcett — *Data Science for Business* (2013) —**lente:** pensamiento analítico: formulación del problema, evaluación y valor esperado—. Formula dos mini-casos: uno que satisface la definición de **fuente autoritativa** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **inconsistencias entre sistemas** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «definir la fuente autoritativa de cada dato», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Estado válido: operacionalización y medición

**estado válido** significa **conjunto de valores permitidos para un campo y sus transiciones posibles**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **datos con fuente autoritativa definida**: `campos críticos con fuente única declarada, sobre campos críticos`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Mark Roberge — *The Sales Acceleration Formula* (2015) orienta este bloque —**lente:** contratación, formación, gestión y demanda comercial gobernadas por datos—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Deuda de datos: trade-offs y efectos de segundo orden

**Definición:** acumulación de inconsistencias que encarece cada análisis futuro. Este concepto obliga a abandonar la idea de que modelo de datos de RevOps tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «resolver las inconsistencias más costosas primero», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) —**lente:** traducción de la estrategia en indicadores causalmente conectados— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **tiempo de respuesta a preguntas nuevas** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **deuda de datos** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «establecer el proceso de cambio del modelo», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) sirve para contrastar la recomendación final desde otro lente: traducción de la estrategia en indicadores causalmente conectados. La frontera de esta clase es explícita: Un modelo perfecto que exige rehacer todos los sistemas no se implementa. El diseño debe priorizar lo que produce más valor con menos disrupción. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar modelo de datos de RevOps no consiste en sumar definiciones. Empieza por **entidad**, contrasta **fuente autoritativa** con **estado válido**, incorpora **deuda de datos** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) | integración de datos, procesos y equipos que producen ingreso como un solo sistema | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | pensamiento analítico: formulación del problema, evaluación y valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Mark Roberge — *The Sales Acceleration Formula* (2015) | contratación, formación, gestión y demanda comercial gobernadas por datos | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) | traducción de la estrategia en indicadores causalmente conectados | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El ingreso recurrente de Ruta Andina existe en el CRM, en la plataforma de facturación y en una planilla. Los tres números difieren y ninguno está declarado como autoritativo.

**Paso 1 — Inventariar entidades y sistemas actuales.** El equipo escribe primero el supuesto asociado a **entidad** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **datos con fuente autoritativa definida** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Definir la fuente autoritativa de cada dato.** El trabajo aquí es separar lo observado de lo inferido sobre **fuente autoritativa**. La evidencia que ordena la discusión es **inconsistencias entre sistemas**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Documentar estados válidos y transiciones.** El riesgo de este paso es cerrar demasiado rápido alrededor de **estado válido**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **tiempo de respuesta a preguntas nuevas** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Resolver las inconsistencias más costosas primero.** Con **deuda de datos** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **datos con fuente autoritativa definida** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Establecer el proceso de cambio del modelo.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **entidad**. **inconsistencias entre sistemas** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **entidad** | Objeto del modelo que representa algo real: cuenta, contacto, oportunidad, suscripción | Cuando **datos con fuente autoritativa definida** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **fuente autoritativa** | Sistema que contiene la versión válida de cada dato | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un modelo perfecto que exige rehacer todos los sistemas no se implementa. El diseño debe priorizar lo que produce más valor con menos disrupción.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre modelo de datos de RevOps |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing ops, RevOps manager y Sales ops. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El ingreso recurrente de Ruta Andina existe en el CRM, en la plataforma de facturación y en una planilla. Los tres números difieren y ninguno está declarado como autoritativo.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **inventariar entidades y sistemas actuales → definir la fuente autoritativa de cada dato → documentar estados válidos y transiciones → resolver las inconsistencias más costosas primero → establecer el proceso de cambio del modelo** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **datos con fuente autoritativa definida**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **entidad** y **fuente autoritativa** como sinónimos | Se perdió la distinción entre «objeto del modelo que representa algo real: cuenta, contacto, oportunidad, suscripción» y «sistema que contiene la versión válida de cada dato» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «establecer el proceso de cambio del modelo» | Se saltó «inventariar entidades y sistemas actuales»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **datos con fuente autoritativa definida** | La métrica local reemplazó al resultado del sistema | Contrástala con **tiempo de respuesta a preguntas nuevas** y explicita el costo de oportunidad. |
| Operar sin fuente autoritativa declarada | Error específico de esta clase | Define para cada dato crítico cuál sistema manda y documenta la regla de reconciliación. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **entidad** y **fuente autoritativa** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **estado válido** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «inventariar entidades y sistemas actuales» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **datos con fuente autoritativa definida** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un modelo perfecto que exige rehacer todos los sistemas no se implementa. El diseño debe priorizar lo que produce más valor con menos disrupción»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P17-C08-modelo-de-datos-revops/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **datos con fuente autoritativa definida**, **inconsistencias entre sistemas** y **tiempo de respuesta a preguntas nuevas** con fuente, ventana y lectura prohibida.
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

- Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022). **Uso en esta clase:** integración de datos, procesos y equipos que producen ingreso como un solo sistema. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013). **Uso en esta clase:** pensamiento analítico: formulación del problema, evaluación y valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Mark Roberge — *The Sales Acceleration Formula* (2015). **Uso en esta clase:** contratación, formación, gestión y demanda comercial gobernadas por datos. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996). **Uso en esta clase:** traducción de la estrategia en indicadores causalmente conectados. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 07 · Acuerdo de servicio entre marketing y ventas](class-07-sla-marketing-ventas.md) · [Índice de la parte](README.md) · [Clase 09 · Integraciones](class-09-integraciones.md) →
