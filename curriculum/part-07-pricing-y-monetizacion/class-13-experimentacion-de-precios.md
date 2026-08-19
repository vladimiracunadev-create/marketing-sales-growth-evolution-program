---
title: "Experimentación de precios"
type: class
language: es
standard: clase-profunda-v3
part: 07
class: 13
level: Oferta comercial
mastery_threshold: 80
estimated_minutes: 150
sources: ["kohavi", "nagle", "provost", "simon"]
updated: 2026-08-18
---

# Clase 07.13 — Experimentación de precios

**Parte 07 · Pricing y monetización** · Nivel: Oferta comercial · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v3`

## 🎯 Propósito

Experimentar con precios es la forma más directa de reducir incertidumbre y la que más consecuencias tiene sobre clientes reales. Un experimento válido requiere grupos comparables, tamaño suficiente, duración que cubra el ciclo de compra y métricas guardrail sobre churn y reclamos. Kohavi advierte sobre las trampas: detener la prueba al ver un resultado favorable o cambiar el criterio a mitad de camino invalida la conclusión.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 07 busca **diseñar una arquitectura de precios que capture valor sin destruir demanda ni confianza**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **experimentación de precios** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Cuánto vale esto para quién, y qué estructura de cobro alinea precio con valor entregado?

Los conceptos que estructuran la sesión son **grupo de comparación**, **métrica guardrail**, **duración mínima** y **detención prematura**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `grupo de comparación`, `métrica guardrail`, `duración mínima` y `detención prematura` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Pricing y monetización**.
3. **Aplicar** la secuencia **definir hipótesis, métrica principal y guardarraíles → calcular tamaño y duración mínima antes de iniciar → asignar grupos de forma comparable y documentada → no modificar criterios durante la ejecución → decidir con el criterio previo y registrar el aprendizaje** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **efecto en conversión**, **efecto en ingreso por visitante** y **guardarraíl de reclamos** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **grupo de comparación** y **métrica guardrail** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **efecto en conversión**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **grupo de comparación** | conjunto equivalente que no recibe el cambio y permite estimar el efecto | Construye un caso límite donde el concepto se confunde con el anterior. |
| **métrica guardrail** | indicador que no debe deteriorarse aunque mejore la métrica principal | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **duración mínima** | tiempo necesario para cubrir el ciclo completo de decisión del segmento | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **detención prematura** | interrupción del experimento al observar un resultado favorable transitorio | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir hipótesis, métrica principal y guardarraíles → 2. calcular tamaño y duración mínima antes de iniciar → 3. asignar grupos de forma comparable y documentada → 4. no modificar criterios durante la ejecución → 5. decidir con el criterio previo y registrar el aprendizaje
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Cobrar precios distintos a clientes equivalentes por asignación aleatoria plantea un problema ético y de trato justo. Los experimentos deben tener criterio de equidad y compensación definida.

## 📖 Desarrollo

### 1. Grupo de comparación: mecanismo central

**grupo de comparación** se entiende aquí como **conjunto equivalente que no recibe el cambio y permite estimar el efecto**. Es la pieza desde la que se inicia el análisis de experimentación de precios: antes de «definir hipótesis, métrica principal y guardarraíles», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020). **Lente que aporta:** diseño estadístico de experimentos, métricas guardrail y trampas de interpretación. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **efecto en conversión**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **métrica guardrail**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Métrica guardrail: frontera conceptual y error de clasificación

**Definición operacional:** indicador que no debe deteriorarse aunque mejore la métrica principal. Su valor está en distinguirlo de **grupo de comparación**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) —**lente:** pricing basado en valor, estructura de precios, métrica de cobro y política de descuentos—. Formula dos mini-casos: uno que satisface la definición de **métrica guardrail** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **efecto en ingreso por visitante** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «calcular tamaño y duración mínima antes de iniciar», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Duración mínima: operacionalización y medición

**duración mínima** significa **tiempo necesario para cubrir el ciclo completo de decisión del segmento**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **efecto en conversión**: `diferencia de conversión entre grupos, con intervalo de confianza`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Foster Provost y Tom Fawcett — *Data Science for Business* (2013) orienta este bloque —**lente:** pensamiento analítico: formulación del problema, evaluación y valor esperado—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Detención prematura: trade-offs y efectos de segundo orden

**Definición:** interrupción del experimento al observar un resultado favorable transitorio. Este concepto obliga a abandonar la idea de que experimentación de precios tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «no modificar criterios durante la ejecución», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Hermann Simon — *Confessions of the Pricing Man* (2015) —**lente:** el precio como la palanca de utilidad más rápida y su relación con el valor percibido— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **guardarraíl de reclamos** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **detención prematura** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «decidir con el criterio previo y registrar el aprendizaje», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Hermann Simon — *Confessions of the Pricing Man* (2015) sirve para contrastar la recomendación final desde otro lente: el precio como la palanca de utilidad más rápida y su relación con el valor percibido. La frontera de esta clase es explícita: Cobrar precios distintos a clientes equivalentes por asignación aleatoria plantea un problema ético y de trato justo. Los experimentos deben tener criterio de equidad y compensación definida. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar experimentación de precios no consiste en sumar definiciones. Empieza por **grupo de comparación**, contrasta **métrica guardrail** con **duración mínima**, incorpora **detención prematura** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | diseño estadístico de experimentos, métricas guardrail y trampas de interpretación | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) | pricing basado en valor, estructura de precios, métrica de cobro y política de descuentos | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | pensamiento analítico: formulación del problema, evaluación y valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Hermann Simon — *Confessions of the Pricing Man* (2015) | el precio como la palanca de utilidad más rápida y su relación con el valor percibido | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina probó un alza de 15 % durante nueve días y observó mejora en ingreso. Su ciclo mediano de decisión es 34 días, por lo que la prueba midió sólo a los compradores más rápidos.

**Paso 1 — Definir hipótesis, métrica principal y guardarraíles.** El equipo escribe primero el supuesto asociado a **grupo de comparación** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **efecto en conversión** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Calcular tamaño y duración mínima antes de iniciar.** El trabajo aquí es separar lo observado de lo inferido sobre **métrica guardrail**. La evidencia que ordena la discusión es **efecto en ingreso por visitante**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Asignar grupos de forma comparable y documentada.** El riesgo de este paso es cerrar demasiado rápido alrededor de **duración mínima**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **guardarraíl de reclamos** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — No modificar criterios durante la ejecución.** Con **detención prematura** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **efecto en conversión** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Decidir con el criterio previo y registrar el aprendizaje.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **grupo de comparación**. **efecto en ingreso por visitante** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **grupo de comparación** | Conjunto equivalente que no recibe el cambio y permite estimar el efecto | Cuando **efecto en conversión** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **métrica guardrail** | Indicador que no debe deteriorarse aunque mejore la métrica principal | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Cobrar precios distintos a clientes equivalentes por asignación aleatoria plantea un problema ético y de trato justo. Los experimentos deben tener criterio de equidad y compensación definida.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre experimentación de precios |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Pricing manager, Product marketing, CFO comercial y Founder. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina probó un alza de 15 % durante nueve días y observó mejora en ingreso. Su ciclo mediano de decisión es 34 días, por lo que la prueba midió sólo a los compradores más rápidos.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **definir hipótesis, métrica principal y guardarraíles → calcular tamaño y duración mínima antes de iniciar → asignar grupos de forma comparable y documentada → no modificar criterios durante la ejecución → decidir con el criterio previo y registrar el aprendizaje** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **efecto en conversión**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **grupo de comparación** y **métrica guardrail** como sinónimos | Se perdió la distinción entre «conjunto equivalente que no recibe el cambio y permite estimar el efecto» y «indicador que no debe deteriorarse aunque mejore la métrica principal» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «decidir con el criterio previo y registrar el aprendizaje» | Se saltó «definir hipótesis, métrica principal y guardarraíles»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **efecto en conversión** | La métrica local reemplazó al resultado del sistema | Contrástala con **guardarraíl de reclamos** y explicita el costo de oportunidad. |
| Detener el experimento al ver un resultado favorable | Error específico de esta clase | Fija duración y tamaño antes de iniciar y no evalúes resultados parciales como definitivos. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **grupo de comparación** y **métrica guardrail** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **duración mínima** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir hipótesis, métrica principal y guardarraíles» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **efecto en conversión** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Cobrar precios distintos a clientes equivalentes por asignación aleatoria plantea un problema ético y de trato justo. Los experimentos deben tener criterio de equidad y compensación definida»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P07-C13-experimentacion-de-precios/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **efecto en conversión**, **efecto en ingreso por visitante** y **guardarraíl de reclamos** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **arquitectura de monetización con métrica de cobro, planes, price fences y política de descuentos**.

## ✅ Evaluación de la clase

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables entre los conceptos de la clase. |
| Diagnóstico y evidencia | 30 % | Datos pertinentes, línea base, supuestos explícitos y límites del dato. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas y argumento ejecutivo trazable. |

**Aprobación:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambios a otra clase se considera insuficiente.

## 📗 Fuentes y verificación

- Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020). **Uso en esta clase:** diseño estadístico de experimentos, métricas guardrail y trampas de interpretación. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.). **Uso en esta clase:** pricing basado en valor, estructura de precios, métrica de cobro y política de descuentos. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013). **Uso en esta clase:** pensamiento analítico: formulación del problema, evaluación y valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Hermann Simon — *Confessions of the Pricing Man* (2015). **Uso en esta clase:** el precio como la palanca de utilidad más rápida y su relación con el valor percibido. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 12 · Unit economics](class-12-unit-economics.md) · [Índice de la parte](README.md) · [Clase 14 · Arquitectura de monetización](class-14-arquitectura-de-monetizacion.md) →
