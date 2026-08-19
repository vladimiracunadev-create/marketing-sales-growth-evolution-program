---
title: "Analítica digital"
type: class
language: es
standard: clase-profunda-v1
part: 12
class: 10
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["kaushik", "provost", "croll-yoskovitz", "wheeler-dv"]
updated: 2026-08-19
---

# Clase 12.10 — Analítica digital

**Parte 12 · Marketing digital y adquisición** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

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

**plan de medición** se entiende aquí como **documento que vincula decisiones, preguntas, métricas y eventos a registrar**. Es la pieza desde la que se inicia el análisis de analítica digital: antes de «definir las decisiones que la analítica debe informar», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Avinash Kaushik — *Web Analytics 2.0* (2009). **Lente que aporta:** medición orientada a decisión, segmentación y crítica del dato de vanidad. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **decisiones informadas por analítica**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **métrica de vanidad**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Métrica de vanidad: frontera conceptual y error de clasificación

**Definición operacional:** indicador que sube sin relación con el resultado de negocio. Su valor está en distinguirlo de **plan de medición**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Foster Provost y Tom Fawcett — *Data Science for Business* (2013) —**lente:** pensamiento analítico: formulación del problema, evaluación y valor esperado—. Formula dos mini-casos: uno que satisface la definición de **métrica de vanidad** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **calidad de la instrumentación** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «traducirlas a preguntas y métricas con definición operacional», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Segmentación analítica: operacionalización y medición

**segmentación analítica** significa **análisis por grupos que revela diferencias ocultas en el promedio**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **decisiones informadas por analítica**: `decisiones documentadas que citan un análisis, por trimestre`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) orienta este bloque —**lente:** una métrica que importa por etapa y por modelo de negocio—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Calidad del dato: trade-offs y efectos de segundo orden

**Definición:** grado en que la instrumentación registra correctamente lo que ocurre. Este concepto obliga a abandonar la idea de que analítica digital tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «analizar por segmento y no sólo el agregado», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Donald J. Wheeler — *Understanding Variation* (2000) —**lente:** distinguir variación común de variación especial antes de reaccionar a un KPI— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **métricas activas sin uso** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **calidad del dato** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar el plan cada semestre y eliminar lo que no se usa», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Donald J. Wheeler — *Understanding Variation* (2000) sirve para contrastar la recomendación final desde otro lente: distinguir variación común de variación especial antes de reaccionar a un KPI. La frontera de esta clase es explícita: Las restricciones de privacidad y el bloqueo de rastreadores reducen la cobertura de la analítica digital. Los datos deben leerse como muestra sesgada y no como censo. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Optimizar métricas de vanidad y desatender consentimiento, cookies y datos personales.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar analítica digital no consiste en sumar definiciones. Empieza por **plan de medición**, contrasta **métrica de vanidad** con **segmentación analítica**, incorpora **calidad del dato** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Avinash Kaushik — *Web Analytics 2.0* (2009) | medición orientada a decisión, segmentación y crítica del dato de vanidad | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | pensamiento analítico: formulación del problema, evaluación y valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | una métrica que importa por etapa y por modelo de negocio | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Donald J. Wheeler — *Understanding Variation* (2000) | distinguir variación común de variación especial antes de reaccionar a un KPI | ¿Qué supuesto de esta clase ayuda a desafiar? |

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

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **definir las decisiones que la analítica debe informar → traducirlas a preguntas y métricas con definición operacional → instrumentar sólo lo necesario y verificar la calidad → analizar por segmento y no sólo el agregado → revisar el plan cada semestre y eliminar lo que no se usa** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **decisiones informadas por analítica**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

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

- Avinash Kaushik — *Web Analytics 2.0* (2009). **Uso en esta clase:** medición orientada a decisión, segmentación y crítica del dato de vanidad. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013). **Uso en esta clase:** pensamiento analítico: formulación del problema, evaluación y valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013). **Uso en esta clase:** una métrica que importa por etapa y por modelo de negocio. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Donald J. Wheeler — *Understanding Variation* (2000). **Uso en esta clase:** distinguir variación común de variación especial antes de reaccionar a un KPI. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 09 · Conversión web](class-09-conversion-web.md) · [Índice de la parte](README.md) · [Clase 11 · Atribución básica](class-11-atribucion-basica.md) →
