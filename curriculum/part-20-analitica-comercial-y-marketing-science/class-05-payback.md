---
title: "Periodo de recuperación"
type: class
language: es
standard: clase-profunda-v1
part: 20
class: 05
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["croll-yoskovitz", "fader-ltv", "provost", "simon"]
updated: 2026-08-19
---

# Clase 20.05 — Periodo de recuperación

**Parte 20 · Analítica comercial y marketing science** · Nivel: Crecimiento y analítica · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

## 🎯 Propósito

El periodo de recuperación indica cuántos meses tarda el margen de un cliente en cubrir su costo de adquisición. Es más útil que la relación entre valor de vida y costo para decidir ritmo de inversión, porque habla directamente de caja. Una empresa con recuperación de 18 meses y caja para 6 no puede escalar aunque su valor de vida sea excelente.

La clase trata el tema como un problema de evidencia y de consecuencia, no como vocabulario. La parte 20 busca **sostener decisiones de ingreso con métricas correctamente construidas**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **periodo de recuperación** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Esta cifra mide lo que creo que mide, y qué decisión cambiaría si estuviera equivocada?

Los conceptos que estructuran la sesión son **periodo de recuperación**, **restricción de caja**, **ritmo sostenible de adquisición** y **relación con la vida del cliente**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `periodo de recuperación`, `restricción de caja`, `ritmo sostenible de adquisición` y `relación con la vida del cliente` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Analítica comercial y marketing science**.
3. **Aplicar** la secuencia **calcular el margen mensual por cliente → determinar el periodo de recuperación por segmento → compararlo con la vida media observada → estimar el ritmo sostenible según la caja disponible → ajustar la meta de adquisición a esa restricción** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **periodo de recuperación por segmento**, **relación recuperación-permanencia** y **clientes financiables por periodo** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **periodo de recuperación** y **restricción de caja** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **periodo de recuperación por segmento**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **periodo de recuperación** | meses hasta que el margen acumulado iguala el costo de adquisición | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **restricción de caja** | límite de inversión impuesto por la liquidez disponible | Da un hecho compatible con la definición y otro que la refute. |
| **ritmo sostenible de adquisición** | volumen de clientes nuevos que la caja permite financiar | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **relación con la vida del cliente** | comparación entre recuperación y permanencia esperada | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. calcular el margen mensual por cliente → 2. determinar el periodo de recuperación por segmento → 3. compararlo con la vida media observada → 4. estimar el ritmo sostenible según la caja disponible → 5. ajustar la meta de adquisición a esa restricción
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** El periodo de recuperación ignora el valor posterior. Un negocio con recuperación larga puede ser excelente si la permanencia es muy alta y hay financiamiento.

## 📖 Desarrollo

### 1. Periodo de recuperación: mecanismo central

**periodo de recuperación** se entiende aquí como **meses hasta que el margen acumulado iguala el costo de adquisición**. Es la pieza desde la que se inicia el análisis de periodo de recuperación: antes de «calcular el margen mensual por cliente», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013). **Lente que aporta:** una métrica que importa por etapa y por modelo de negocio. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **periodo de recuperación por segmento**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **restricción de caja**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Restricción de caja: frontera conceptual y error de clasificación

**Definición operacional:** límite de inversión impuesto por la liquidez disponible. Su valor está en distinguirlo de **periodo de recuperación**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Peter Fader y Sarah Toms — *The Customer Centricity Playbook* (2018) —**lente:** modelos de valor de vida del cliente y decisiones de inversión por cohorte—. Formula dos mini-casos: uno que satisface la definición de **restricción de caja** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **relación recuperación-permanencia** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «determinar el periodo de recuperación por segmento», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Ritmo sostenible de adquisición: operacionalización y medición

**ritmo sostenible de adquisición** significa **volumen de clientes nuevos que la caja permite financiar**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **periodo de recuperación por segmento**: `meses hasta recuperar el costo de adquisición, por segmento`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Foster Provost y Tom Fawcett — *Data Science for Business* (2013) orienta este bloque —**lente:** pensamiento analítico: formulación del problema, evaluación y valor esperado—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Relación con la vida del cliente: trade-offs y efectos de segundo orden

**Definición:** comparación entre recuperación y permanencia esperada. Este concepto obliga a abandonar la idea de que periodo de recuperación tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «estimar el ritmo sostenible según la caja disponible», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Hermann Simon — *Confessions of the Pricing Man* (2015) —**lente:** el precio como la palanca de utilidad más rápida y su relación con el valor percibido— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **clientes financiables por periodo** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **relación con la vida del cliente** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «ajustar la meta de adquisición a esa restricción», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Hermann Simon — *Confessions of the Pricing Man* (2015) sirve para contrastar la recomendación final desde otro lente: el precio como la palanca de utilidad más rápida y su relación con el valor percibido. La frontera de esta clase es explícita: El periodo de recuperación ignora el valor posterior. Un negocio con recuperación larga puede ser excelente si la permanencia es muy alta y hay financiamiento. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar periodo de recuperación no consiste en sumar definiciones. Empieza por **periodo de recuperación**, contrasta **restricción de caja** con **ritmo sostenible de adquisición**, incorpora **relación con la vida del cliente** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | una métrica que importa por etapa y por modelo de negocio | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Peter Fader y Sarah Toms — *The Customer Centricity Playbook* (2018) | modelos de valor de vida del cliente y decisiones de inversión por cohorte | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | pensamiento analítico: formulación del problema, evaluación y valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Hermann Simon — *Confessions of the Pricing Man* (2015) | el precio como la palanca de utilidad más rápida y su relación con el valor percibido | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina recupera su inversión en 14 meses y su vida media de cliente es 11. Cada cliente nuevo destruye caja antes de aportar.

**Paso 1 — Calcular el margen mensual por cliente.** El equipo escribe primero el supuesto asociado a **periodo de recuperación** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **periodo de recuperación por segmento** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Determinar el periodo de recuperación por segmento.** El trabajo aquí es separar lo observado de lo inferido sobre **restricción de caja**. La evidencia que ordena la discusión es **relación recuperación-permanencia**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Compararlo con la vida media observada.** El riesgo de este paso es cerrar demasiado rápido alrededor de **ritmo sostenible de adquisición**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **clientes financiables por periodo** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Estimar el ritmo sostenible según la caja disponible.** Con **relación con la vida del cliente** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **periodo de recuperación por segmento** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Ajustar la meta de adquisición a esa restricción.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **periodo de recuperación**. **relación recuperación-permanencia** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **periodo de recuperación** | Meses hasta que el margen acumulado iguala el costo de adquisición | Cuando **periodo de recuperación por segmento** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **restricción de caja** | Límite de inversión impuesto por la liquidez disponible | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** El periodo de recuperación ignora el valor posterior. Un negocio con recuperación larga puede ser excelente si la permanencia es muy alta y hay financiamiento.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre periodo de recuperación |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing analyst, Revenue analyst y Data-driven marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina recupera su inversión en 14 meses y su vida media de cliente es 11. Cada cliente nuevo destruye caja antes de aportar.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **calcular el margen mensual por cliente → determinar el periodo de recuperación por segmento → compararlo con la vida media observada → estimar el ritmo sostenible según la caja disponible → ajustar la meta de adquisición a esa restricción** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **periodo de recuperación por segmento**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **periodo de recuperación** y **restricción de caja** como sinónimos | Se perdió la distinción entre «meses hasta que el margen acumulado iguala el costo de adquisición» y «límite de inversión impuesto por la liquidez disponible» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «ajustar la meta de adquisición a esa restricción» | Se saltó «calcular el margen mensual por cliente»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **periodo de recuperación por segmento** | La métrica local reemplazó al resultado del sistema | Contrástala con **clientes financiables por periodo** y explicita el costo de oportunidad. |
| Escalar con recuperación mayor que la vida del cliente | Error específico de esta clase | Compara ambos indicadores por segmento antes de aumentar la inversión en adquisición. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **periodo de recuperación** y **restricción de caja** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **ritmo sostenible de adquisición** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «calcular el margen mensual por cliente» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **periodo de recuperación por segmento** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «El periodo de recuperación ignora el valor posterior. Un negocio con recuperación larga puede ser excelente si la permanencia es muy alta y hay financiamiento»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P20-C05-payback/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **periodo de recuperación por segmento**, **relación recuperación-permanencia** y **clientes financiables por periodo** con fuente, ventana y lectura prohibida.
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

- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013). **Uso en esta clase:** una métrica que importa por etapa y por modelo de negocio. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Peter Fader y Sarah Toms — *The Customer Centricity Playbook* (2018). **Uso en esta clase:** modelos de valor de vida del cliente y decisiones de inversión por cohorte. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013). **Uso en esta clase:** pensamiento analítico: formulación del problema, evaluación y valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Hermann Simon — *Confessions of the Pricing Man* (2015). **Uso en esta clase:** el precio como la palanca de utilidad más rápida y su relación con el valor percibido. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 04 · Valor de vida del cliente](class-04-ltv.md) · [Índice de la parte](README.md) · [Clase 06 · Margen de contribución](class-06-contribution-margin.md) →
