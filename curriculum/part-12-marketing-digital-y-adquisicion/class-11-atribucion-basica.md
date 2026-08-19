---
title: "Atribución básica"
type: class
language: es
standard: clase-profunda-v3
part: 12
class: 11
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["kaushik", "kohavi", "provost", "binet-field"]
updated: 2026-08-18
---

# Clase 12.11 — Atribución básica

**Parte 12 · Marketing digital y adquisición** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v3`

## 🎯 Propósito

La atribución intenta repartir el crédito de una conversión entre los puntos de contacto que la precedieron. Todos los modelos —último clic, primer clic, lineal, decaimiento— son convenciones, no verdades. El último clic sobrevalora los canales de captura de intención y subvalora los que crean demanda. La conclusión práctica es usar la atribución para ordenar la conversación y la incrementalidad para decidir presupuesto.

El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta. La parte 12 busca **operar un sistema digital de adquisición medible de punta a punta**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **atribución básica** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué activo digital genera demanda propia y qué parte del resultado es alquilada?

Los conceptos que estructuran la sesión son **modelo de atribución**, **sesgo del último clic**, **ventana de atribución** y **incrementalidad**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `modelo de atribución`, `sesgo del último clic`, `ventana de atribución` y `incrementalidad` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Marketing digital y adquisición**.
3. **Aplicar** la secuencia **documentar el modelo y la ventana utilizados → comparar resultados bajo dos modelos distintos → identificar los canales cuyo valor cambia según el modelo → diseñar una prueba de incrementalidad para los casos críticos → decidir presupuesto con evidencia causal donde el monto lo justifique** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **diferencia de crédito entre modelos**, **cobertura de la atribución** y **resultado de pruebas de incrementalidad** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **modelo de atribución** y **sesgo del último clic** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **diferencia de crédito entre modelos**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **modelo de atribución** | regla convencional que reparte el crédito de la conversión entre puntos de contacto | Da un hecho compatible con la definición y otro que la refute. |
| **sesgo del último clic** | sobrevaloración del canal más cercano a la conversión | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **ventana de atribución** | periodo dentro del cual un contacto se considera contribuyente | Construye un caso límite donde el concepto se confunde con el anterior. |
| **incrementalidad** | efecto causal real de un canal, estimado con grupo de comparación | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. documentar el modelo y la ventana utilizados → 2. comparar resultados bajo dos modelos distintos → 3. identificar los canales cuyo valor cambia según el modelo → 4. diseñar una prueba de incrementalidad para los casos críticos → 5. decidir presupuesto con evidencia causal donde el monto lo justifique
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Ningún modelo de atribución establece causalidad. Con presupuestos pequeños, el costo de una prueba de incrementalidad puede superar su beneficio.

## 📖 Desarrollo

### 1. Modelo de atribución: mecanismo central

**modelo de atribución** se entiende aquí como **regla convencional que reparte el crédito de la conversión entre puntos de contacto**. Es la pieza desde la que se inicia el análisis de atribución básica: antes de «documentar el modelo y la ventana utilizados», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Avinash Kaushik — *Web Analytics 2.0* (2009). **Lente que aporta:** medición orientada a decisión, segmentación y crítica del dato de vanidad. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **diferencia de crédito entre modelos**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **sesgo del último clic**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Sesgo del último clic: frontera conceptual y error de clasificación

**Definición operacional:** sobrevaloración del canal más cercano a la conversión. Su valor está en distinguirlo de **modelo de atribución**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) —**lente:** diseño estadístico de experimentos, métricas guardrail y trampas de interpretación—. Formula dos mini-casos: uno que satisface la definición de **sesgo del último clic** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **cobertura de la atribución** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «comparar resultados bajo dos modelos distintos», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Ventana de atribución: operacionalización y medición

**ventana de atribución** significa **periodo dentro del cual un contacto se considera contribuyente**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **diferencia de crédito entre modelos**: `variación del crédito asignado a cada canal según el modelo aplicado`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Foster Provost y Tom Fawcett — *Data Science for Business* (2013) orienta este bloque —**lente:** pensamiento analítico: formulación del problema, evaluación y valor esperado—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Incrementalidad: trade-offs y efectos de segundo orden

**Definición:** efecto causal real de un canal, estimado con grupo de comparación. Este concepto obliga a abandonar la idea de que atribución básica tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «diseñar una prueba de incrementalidad para los casos críticos», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Les Binet y Peter Field — *The Long and the Short of It* (2013) —**lente:** equilibrio entre construcción de marca a largo plazo y activación de ventas a corto plazo— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **resultado de pruebas de incrementalidad** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **incrementalidad** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «decidir presupuesto con evidencia causal donde el monto lo justifique», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Les Binet y Peter Field — *The Long and the Short of It* (2013) sirve para contrastar la recomendación final desde otro lente: equilibrio entre construcción de marca a largo plazo y activación de ventas a corto plazo. La frontera de esta clase es explícita: Ningún modelo de atribución establece causalidad. Con presupuestos pequeños, el costo de una prueba de incrementalidad puede superar su beneficio. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Optimizar métricas de vanidad y desatender consentimiento, cookies y datos personales.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar atribución básica no consiste en sumar definiciones. Empieza por **modelo de atribución**, contrasta **sesgo del último clic** con **ventana de atribución**, incorpora **incrementalidad** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Avinash Kaushik — *Web Analytics 2.0* (2009) | medición orientada a decisión, segmentación y crítica del dato de vanidad | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | diseño estadístico de experimentos, métricas guardrail y trampas de interpretación | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | pensamiento analítico: formulación del problema, evaluación y valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Les Binet y Peter Field — *The Long and the Short of It* (2013) | equilibrio entre construcción de marca a largo plazo y activación de ventas a corto plazo | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Bajo último clic, la búsqueda de marca recibe el 61 % del crédito en Ruta Andina. Bajo primer clic, el contenido orgánico recibe el 44 %. El presupuesto se asigna con el primero.

**Paso 1 — Documentar el modelo y la ventana utilizados.** El equipo escribe primero el supuesto asociado a **modelo de atribución** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **diferencia de crédito entre modelos** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Comparar resultados bajo dos modelos distintos.** El trabajo aquí es separar lo observado de lo inferido sobre **sesgo del último clic**. La evidencia que ordena la discusión es **cobertura de la atribución**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Identificar los canales cuyo valor cambia según el modelo.** El riesgo de este paso es cerrar demasiado rápido alrededor de **ventana de atribución**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **resultado de pruebas de incrementalidad** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Diseñar una prueba de incrementalidad para los casos críticos.** Con **incrementalidad** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **diferencia de crédito entre modelos** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Decidir presupuesto con evidencia causal donde el monto lo justifique.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **modelo de atribución**. **cobertura de la atribución** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **modelo de atribución** | Regla convencional que reparte el crédito de la conversión entre puntos de contacto | Cuando **diferencia de crédito entre modelos** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **sesgo del último clic** | Sobrevaloración del canal más cercano a la conversión | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Ningún modelo de atribución establece causalidad. Con presupuestos pequeños, el costo de una prueba de incrementalidad puede superar su beneficio.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre atribución básica |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Digital marketing manager, Growth marketer y Especialista SEO/SEM. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Bajo último clic, la búsqueda de marca recibe el 61 % del crédito en Ruta Andina. Bajo primer clic, el contenido orgánico recibe el 44 %. El presupuesto se asigna con el primero.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **documentar el modelo y la ventana utilizados → comparar resultados bajo dos modelos distintos → identificar los canales cuyo valor cambia según el modelo → diseñar una prueba de incrementalidad para los casos críticos → decidir presupuesto con evidencia causal donde el monto lo justifique** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **diferencia de crédito entre modelos**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **modelo de atribución** y **sesgo del último clic** como sinónimos | Se perdió la distinción entre «regla convencional que reparte el crédito de la conversión entre puntos de contacto» y «sobrevaloración del canal más cercano a la conversión» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «decidir presupuesto con evidencia causal donde el monto lo justifique» | Se saltó «documentar el modelo y la ventana utilizados»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **diferencia de crédito entre modelos** | La métrica local reemplazó al resultado del sistema | Contrástala con **resultado de pruebas de incrementalidad** y explicita el costo de oportunidad. |
| Asignar presupuesto sólo por último clic | Error específico de esta clase | Compara al menos dos modelos y valida los canales críticos con una prueba de incrementalidad. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **modelo de atribución** y **sesgo del último clic** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **ventana de atribución** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «documentar el modelo y la ventana utilizados» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **diferencia de crédito entre modelos** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Ningún modelo de atribución establece causalidad. Con presupuestos pequeños, el costo de una prueba de incrementalidad puede superar su beneficio»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Optimizar métricas de vanidad y desatender consentimiento, cookies y datos personales.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P12-C11-atribucion-basica/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **diferencia de crédito entre modelos**, **cobertura de la atribución** y **resultado de pruebas de incrementalidad** con fuente, ventana y lectura prohibida.
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
- Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020). **Uso en esta clase:** diseño estadístico de experimentos, métricas guardrail y trampas de interpretación. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013). **Uso en esta clase:** pensamiento analítico: formulación del problema, evaluación y valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Les Binet y Peter Field — *The Long and the Short of It* (2013). **Uso en esta clase:** equilibrio entre construcción de marca a largo plazo y activación de ventas a corto plazo. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 10 · Analítica digital](class-10-analitica-digital.md) · [Índice de la parte](README.md) · [Clase 12 · Omnicanalidad](class-12-omnicanalidad.md) →
