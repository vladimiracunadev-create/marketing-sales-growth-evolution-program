---
title: "Personalización"
type: class
language: es
standard: clase-profunda-v3
part: 21
class: 05
level: IA y expansión
mastery_threshold: 80
estimated_minutes: 150
sources: ["thaler", "oneil", "nist-airmf", "cialdini"]
updated: 2026-08-18
---

# Clase 21.05 — Personalización

**Parte 21 · IA aplicada a marketing, ventas y servicio** · Nivel: IA y expansión · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v3`

## 🎯 Propósito

La personalización mejora la pertinencia y puede cruzar rápidamente hacia lo invasivo. El límite no es técnico sino de expectativa: usar información que el cliente no sabe que la empresa posee produce desconfianza, aunque su obtención haya sido lícita. La regla práctica es personalizar con datos que el cliente entregó conscientemente y para la finalidad que conoce.

La clase trata el tema como un problema de evidencia y de consecuencia, no como vocabulario. La parte 21 busca **usar IA como capacidad operativa con evaluación, control y responsabilidad humana**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **personalización** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué tarea mejora con IA, cómo sé que mejora y quién responde cuando falla?

Los conceptos que estructuran la sesión son **pertinencia percibida**, **expectativa de privacidad**, **finalidad declarada** y **efecto inquietante**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `pertinencia percibida`, `expectativa de privacidad`, `finalidad declarada` y `efecto inquietante` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **IA aplicada a marketing, ventas y servicio**.
3. **Aplicar** la secuencia **identificar qué datos entregó el cliente conscientemente → verificar la finalidad declarada al recogerlos → diseñar la personalización dentro de esa expectativa → probar la reacción con un grupo pequeño → medir efecto en conversión y en bajas** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **efecto en conversión**, **tasa de baja tras personalización** y **consultas sobre uso de datos** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **pertinencia percibida** y **expectativa de privacidad** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **efecto en conversión**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **pertinencia percibida** | grado en que el cliente considera útil la adaptación del mensaje | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **expectativa de privacidad** | supuesto del cliente sobre qué información tiene la empresa y para qué | Da un hecho compatible con la definición y otro que la refute. |
| **finalidad declarada** | uso informado al momento de recoger el dato | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **efecto inquietante** | reacción negativa ante una personalización que revela información inesperada | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. identificar qué datos entregó el cliente conscientemente → 2. verificar la finalidad declarada al recogerlos → 3. diseñar la personalización dentro de esa expectativa → 4. probar la reacción con un grupo pequeño → 5. medir efecto en conversión y en bajas
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** La normativa de datos personales exige finalidad determinada e información al titular. La personalización basada en inferencias no declaradas es especialmente riesgosa.

## 📖 Desarrollo

### 1. Pertinencia percibida: mecanismo central

**pertinencia percibida** se entiende aquí como **grado en que el cliente considera útil la adaptación del mensaje**. Es la pieza desde la que se inicia el análisis de personalización: antes de «identificar qué datos entregó el cliente conscientemente», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Richard H. Thaler y Cass R. Sunstein — *Nudge: The Final Edition* (2021). **Lente que aporta:** arquitectura de decisión y límites éticos de la influencia sobre la elección. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **efecto en conversión**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **expectativa de privacidad**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Expectativa de privacidad: frontera conceptual y error de clasificación

**Definición operacional:** supuesto del cliente sobre qué información tiene la empresa y para qué. Su valor está en distinguirlo de **pertinencia percibida**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Cathy O'Neil — *Weapons of Math Destruction* (2016) —**lente:** daños de los modelos opacos a escala y necesidad de auditoría—. Formula dos mini-casos: uno que satisface la definición de **expectativa de privacidad** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **tasa de baja tras personalización** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «verificar la finalidad declarada al recogerlos», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Finalidad declarada: operacionalización y medición

**finalidad declarada** significa **uso informado al momento de recoger el dato**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **efecto en conversión**: `diferencia de conversión entre versión personalizada y estándar`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

NIST — *AI Risk Management Framework 1.0* (2023) orienta este bloque —**lente:** gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Efecto inquietante: trade-offs y efectos de segundo orden

**Definición:** reacción negativa ante una personalización que revela información inesperada. Este concepto obliga a abandonar la idea de que personalización tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «probar la reacción con un grupo pequeño», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Robert B. Cialdini — *Influence: The Psychology of Persuasion, New and Expanded* (2021) —**lente:** principios de influencia y su uso ético en contextos comerciales— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **consultas sobre uso de datos** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **efecto inquietante** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «medir efecto en conversión y en bajas», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Robert B. Cialdini — *Influence: The Psychology of Persuasion, New and Expanded* (2021) sirve para contrastar la recomendación final desde otro lente: principios de influencia y su uso ético en contextos comerciales. La frontera de esta clase es explícita: La normativa de datos personales exige finalidad determinada e información al titular. La personalización basada en inferencias no declaradas es especialmente riesgosa. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar personalización no consiste en sumar definiciones. Empieza por **pertinencia percibida**, contrasta **expectativa de privacidad** con **finalidad declarada**, incorpora **efecto inquietante** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Richard H. Thaler y Cass R. Sunstein — *Nudge: The Final Edition* (2021) | arquitectura de decisión y límites éticos de la influencia sobre la elección | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Cathy O'Neil — *Weapons of Math Destruction* (2016) | daños de los modelos opacos a escala y necesidad de auditoría | ¿Qué supuesto de esta clase ayuda a desafiar? |
| NIST — *AI Risk Management Framework 1.0* (2023) | gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Robert B. Cialdini — *Influence: The Psychology of Persuasion, New and Expanded* (2021) | principios de influencia y su uso ético en contextos comerciales | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina envió un correo mencionando la cantidad de citas canceladas de cada taller. Varios clientes preguntaron cómo obtuvieron ese dato y dos solicitaron eliminación.

**Paso 1 — Identificar qué datos entregó el cliente conscientemente.** El equipo escribe primero el supuesto asociado a **pertinencia percibida** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **efecto en conversión** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Verificar la finalidad declarada al recogerlos.** El trabajo aquí es separar lo observado de lo inferido sobre **expectativa de privacidad**. La evidencia que ordena la discusión es **tasa de baja tras personalización**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Diseñar la personalización dentro de esa expectativa.** El riesgo de este paso es cerrar demasiado rápido alrededor de **finalidad declarada**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **consultas sobre uso de datos** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Probar la reacción con un grupo pequeño.** Con **efecto inquietante** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **efecto en conversión** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Medir efecto en conversión y en bajas.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **pertinencia percibida**. **tasa de baja tras personalización** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **pertinencia percibida** | Grado en que el cliente considera útil la adaptación del mensaje | Cuando **efecto en conversión** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **expectativa de privacidad** | Supuesto del cliente sobre qué información tiene la empresa y para qué | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** La normativa de datos personales exige finalidad determinada e información al titular. La personalización basada en inferencias no declaradas es especialmente riesgosa.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre personalización |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager con IA, RevOps, Marketing manager y Sales enablement. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina envió un correo mencionando la cantidad de citas canceladas de cada taller. Varios clientes preguntaron cómo obtuvieron ese dato y dos solicitaron eliminación.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **identificar qué datos entregó el cliente conscientemente → verificar la finalidad declarada al recogerlos → diseñar la personalización dentro de esa expectativa → probar la reacción con un grupo pequeño → medir efecto en conversión y en bajas** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **efecto en conversión**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **pertinencia percibida** y **expectativa de privacidad** como sinónimos | Se perdió la distinción entre «grado en que el cliente considera útil la adaptación del mensaje» y «supuesto del cliente sobre qué información tiene la empresa y para qué» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «medir efecto en conversión y en bajas» | Se saltó «identificar qué datos entregó el cliente conscientemente»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **efecto en conversión** | La métrica local reemplazó al resultado del sistema | Contrástala con **consultas sobre uso de datos** y explicita el costo de oportunidad. |
| Personalizar con datos fuera de la finalidad declarada | Error específico de esta clase | Limita la personalización a datos entregados conscientemente y para el uso informado. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **pertinencia percibida** y **expectativa de privacidad** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **finalidad declarada** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «identificar qué datos entregó el cliente conscientemente» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **efecto en conversión** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «La normativa de datos personales exige finalidad determinada e información al titular. La personalización basada en inferencias no declaradas es especialmente riesgosa»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P21-C05-personalizacion/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **efecto en conversión**, **tasa de baja tras personalización** y **consultas sobre uso de datos** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **operating model humano-IA con casos de uso, evaluaciones, guardrails y registro de incidentes**.

## ✅ Evaluación de la clase

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables entre los conceptos de la clase. |
| Diagnóstico y evidencia | 30 % | Datos pertinentes, línea base, supuestos explícitos y límites del dato. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas y argumento ejecutivo trazable. |

**Aprobación:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambios a otra clase se considera insuficiente.

## 📗 Fuentes y verificación

- Richard H. Thaler y Cass R. Sunstein — *Nudge: The Final Edition* (2021). **Uso en esta clase:** arquitectura de decisión y límites éticos de la influencia sobre la elección. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Cathy O'Neil — *Weapons of Math Destruction* (2016). **Uso en esta clase:** daños de los modelos opacos a escala y necesidad de auditoría. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- NIST — *AI Risk Management Framework 1.0* (2023). **Uso en esta clase:** gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Robert B. Cialdini — *Influence: The Psychology of Persuasion, New and Expanded* (2021). **Uso en esta clase:** principios de influencia y su uso ético en contextos comerciales. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 04 · Generación de contenido con controles](class-04-generacion-de-contenido-con-controles.md) · [Índice de la parte](README.md) · [Clase 06 · Investigación de prospectos asistida](class-06-lead-research.md) →
