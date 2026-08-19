---
title: "Proyección de resultados"
type: class
language: es
standard: clase-profunda-v3
part: 20
class: 11
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["wheeler-dv", "provost", "hubbard", "croll-yoskovitz"]
updated: 2026-08-18
---

# Clase 20.11 — Proyección de resultados

**Parte 20 · Analítica comercial y marketing science** · Nivel: Crecimiento y analítica · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v3`

## 🎯 Propósito

Proyectar resultados comerciales exige distinguir tendencia, estacionalidad y ruido. El error habitual es extrapolar el último trimestre, que confunde variación aleatoria con dirección. Wheeler ofrece el criterio operativo: antes de proyectar, determinar si el proceso es estable; si no lo es, ninguna proyección es válida.

El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta. La parte 20 busca **sostener decisiones de ingreso con métricas correctamente construidas**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **proyección de resultados** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Esta cifra mide lo que creo que mide, y qué decisión cambiaría si estuviera equivocada?

Los conceptos que estructuran la sesión son **tendencia**, **estacionalidad**, **estabilidad del proceso** y **intervalo de proyección**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `tendencia`, `estacionalidad`, `estabilidad del proceso` y `intervalo de proyección` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Analítica comercial y marketing science**.
3. **Aplicar** la secuencia **verificar la estabilidad de la serie histórica → separar tendencia, estacionalidad y ruido → elegir el método de proyección según los datos disponibles → presentar el resultado como intervalo → medir la precisión de las proyecciones anteriores** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **precisión de proyecciones previas**, **amplitud del intervalo** y **estabilidad de la serie** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **tendencia** y **estacionalidad** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **precisión de proyecciones previas**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **tendencia** | dirección sostenida de una serie más allá de la variación aleatoria | Da un hecho compatible con la definición y otro que la refute. |
| **estacionalidad** | patrón recurrente asociado al calendario | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **estabilidad del proceso** | condición en que la variación se mantiene dentro de límites previsibles | Construye un caso límite donde el concepto se confunde con el anterior. |
| **intervalo de proyección** | rango dentro del cual se espera el resultado futuro | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. verificar la estabilidad de la serie histórica → 2. separar tendencia, estacionalidad y ruido → 3. elegir el método de proyección según los datos disponibles → 4. presentar el resultado como intervalo → 5. medir la precisión de las proyecciones anteriores
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Ningún método proyecta cambios estructurales: la entrada de un competidor o un cambio regulatorio invalidan la serie histórica.

## 📖 Desarrollo

### 1. Tendencia: mecanismo central

**tendencia** se entiende aquí como **dirección sostenida de una serie más allá de la variación aleatoria**. Es la pieza desde la que se inicia el análisis de proyección de resultados: antes de «verificar la estabilidad de la serie histórica», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Donald J. Wheeler — *Understanding Variation* (2000). **Lente que aporta:** distinguir variación común de variación especial antes de reaccionar a un KPI. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **precisión de proyecciones previas**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **estacionalidad**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Estacionalidad: frontera conceptual y error de clasificación

**Definición operacional:** patrón recurrente asociado al calendario. Su valor está en distinguirlo de **tendencia**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Foster Provost y Tom Fawcett — *Data Science for Business* (2013) —**lente:** pensamiento analítico: formulación del problema, evaluación y valor esperado—. Formula dos mini-casos: uno que satisface la definición de **estacionalidad** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **amplitud del intervalo** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «separar tendencia, estacionalidad y ruido», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Estabilidad del proceso: operacionalización y medición

**estabilidad del proceso** significa **condición en que la variación se mantiene dentro de límites previsibles**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **precisión de proyecciones previas**: `diferencia entre proyectado y real, por periodo`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) orienta este bloque —**lente:** medir lo que parece inmedible: valor de la información y reducción de incertidumbre—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Intervalo de proyección: trade-offs y efectos de segundo orden

**Definición:** rango dentro del cual se espera el resultado futuro. Este concepto obliga a abandonar la idea de que proyección de resultados tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «presentar el resultado como intervalo», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) —**lente:** una métrica que importa por etapa y por modelo de negocio— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **estabilidad de la serie** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **intervalo de proyección** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «medir la precisión de las proyecciones anteriores», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) sirve para contrastar la recomendación final desde otro lente: una métrica que importa por etapa y por modelo de negocio. La frontera de esta clase es explícita: Ningún método proyecta cambios estructurales: la entrada de un competidor o un cambio regulatorio invalidan la serie histórica. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar proyección de resultados no consiste en sumar definiciones. Empieza por **tendencia**, contrasta **estacionalidad** con **estabilidad del proceso**, incorpora **intervalo de proyección** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Donald J. Wheeler — *Understanding Variation* (2000) | distinguir variación común de variación especial antes de reaccionar a un KPI | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | pensamiento analítico: formulación del problema, evaluación y valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) | medir lo que parece inmedible: valor de la información y reducción de incertidumbre | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | una métrica que importa por etapa y por modelo de negocio | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina proyecta el año extrapolando el mejor trimestre de su historia, que coincidió con una campaña puntual que no se repetirá.

**Paso 1 — Verificar la estabilidad de la serie histórica.** El equipo escribe primero el supuesto asociado a **tendencia** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **precisión de proyecciones previas** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Separar tendencia, estacionalidad y ruido.** El trabajo aquí es separar lo observado de lo inferido sobre **estacionalidad**. La evidencia que ordena la discusión es **amplitud del intervalo**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Elegir el método de proyección según los datos disponibles.** El riesgo de este paso es cerrar demasiado rápido alrededor de **estabilidad del proceso**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **estabilidad de la serie** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Presentar el resultado como intervalo.** Con **intervalo de proyección** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **precisión de proyecciones previas** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Medir la precisión de las proyecciones anteriores.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **tendencia**. **amplitud del intervalo** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **tendencia** | Dirección sostenida de una serie más allá de la variación aleatoria | Cuando **precisión de proyecciones previas** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **estacionalidad** | Patrón recurrente asociado al calendario | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Ningún método proyecta cambios estructurales: la entrada de un competidor o un cambio regulatorio invalidan la serie histórica.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre proyección de resultados |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing analyst, Revenue analyst y Data-driven marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina proyecta el año extrapolando el mejor trimestre de su historia, que coincidió con una campaña puntual que no se repetirá.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **verificar la estabilidad de la serie histórica → separar tendencia, estacionalidad y ruido → elegir el método de proyección según los datos disponibles → presentar el resultado como intervalo → medir la precisión de las proyecciones anteriores** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **precisión de proyecciones previas**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **tendencia** y **estacionalidad** como sinónimos | Se perdió la distinción entre «dirección sostenida de una serie más allá de la variación aleatoria» y «patrón recurrente asociado al calendario» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «medir la precisión de las proyecciones anteriores» | Se saltó «verificar la estabilidad de la serie histórica»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **precisión de proyecciones previas** | La métrica local reemplazó al resultado del sistema | Contrástala con **estabilidad de la serie** y explicita el costo de oportunidad. |
| Extrapolar el último periodo | Error específico de esta clase | Verifica la estabilidad de la serie y presenta la proyección como intervalo con supuestos declarados. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **tendencia** y **estacionalidad** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **estabilidad del proceso** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «verificar la estabilidad de la serie histórica» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **precisión de proyecciones previas** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Ningún método proyecta cambios estructurales: la entrada de un competidor o un cambio regulatorio invalidan la serie histórica»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P20-C11-forecasting/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **precisión de proyecciones previas**, **amplitud del intervalo** y **estabilidad de la serie** con fuente, ventana y lectura prohibida.
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

- Donald J. Wheeler — *Understanding Variation* (2000). **Uso en esta clase:** distinguir variación común de variación especial antes de reaccionar a un KPI. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013). **Uso en esta clase:** pensamiento analítico: formulación del problema, evaluación y valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.). **Uso en esta clase:** medir lo que parece inmedible: valor de la información y reducción de incertidumbre. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013). **Uso en esta clase:** una métrica que importa por etapa y por modelo de negocio. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 10 · A/B testing](class-10-a-b-testing.md) · [Índice de la parte](README.md) · [Clase 12 · Fundamentos de marketing mix modeling](class-12-marketing-mix-modeling-fundamentos.md) →
