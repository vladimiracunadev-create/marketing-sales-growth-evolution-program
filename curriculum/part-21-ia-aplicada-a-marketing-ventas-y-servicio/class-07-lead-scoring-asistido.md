---
title: "Lead scoring asistido por modelos"
type: class
language: es
standard: clase-profunda-v1
part: 21
class: 07
level: IA y expansión
mastery_threshold: 80
estimated_minutes: 150
sources: ["provost", "ng-mlyearning", "oneil", "nist-airmf"]
updated: 2026-08-19
---

# Clase 21.07 — Lead scoring asistido por modelos

**Parte 21 · IA aplicada a marketing, ventas y servicio** · Nivel: IA y expansión · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

## 🎯 Propósito

Un modelo predictivo puede superar a las reglas manuales cuando hay volumen suficiente y datos de calidad. Sus riesgos son conocidos: aprende de la historia y reproduce sus sesgos; si la prospección pasada ignoró un segmento, el modelo lo seguirá subvalorando. Requiere validación periódica, explicabilidad suficiente para que ventas confíe y supervisión humana.

Esta sesión distingue lo que se sabe, lo que se supone y lo que todavía no se ha medido. La parte 21 busca **usar IA como capacidad operativa con evaluación, control y responsabilidad humana**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **lead scoring asistido por modelos** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué tarea mejora con IA, cómo sé que mejora y quién responde cuando falla?

Los conceptos que estructuran la sesión son **sesgo histórico**, **explicabilidad**, **deriva del modelo** y **supervisión humana**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `sesgo histórico`, `explicabilidad`, `deriva del modelo` y `supervisión humana` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **IA aplicada a marketing, ventas y servicio**.
3. **Aplicar** la secuencia **verificar volumen y calidad de datos antes de modelar → evaluar el desempeño frente a la regla manual actual → revisar el sesgo por segmento → monitorear la deriva y recalibrar → mantener supervisión humana sobre las decisiones** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **desempeño frente a la regla actual**, **desempeño por segmento** y **deriva observada** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **sesgo histórico** y **explicabilidad** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **desempeño frente a la regla actual**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **sesgo histórico** | reproducción de patrones del pasado que pueden ser injustos o subóptimos | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **explicabilidad** | capacidad de indicar qué factores influyeron en la puntuación | Construye un caso límite donde el concepto se confunde con el anterior. |
| **deriva del modelo** | pérdida de precisión por cambios en el mercado o en el proceso | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **supervisión humana** | revisión de decisiones del modelo por una persona responsable | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. verificar volumen y calidad de datos antes de modelar → 2. evaluar el desempeño frente a la regla manual actual → 3. revisar el sesgo por segmento → 4. monitorear la deriva y recalibrar → 5. mantener supervisión humana sobre las decisiones
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un modelo que no puede explicarse no será usado por el equipo comercial. La explicabilidad no es un lujo: determina la adopción.

## 📖 Desarrollo

### 1. Sesgo histórico: mecanismo central

**sesgo histórico** se entiende aquí como **reproducción de patrones del pasado que pueden ser injustos o subóptimos**. Es la pieza desde la que se inicia el análisis de lead scoring asistido por modelos: antes de «verificar volumen y calidad de datos antes de modelar», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Foster Provost y Tom Fawcett — *Data Science for Business* (2013). **Lente que aporta:** pensamiento analítico: formulación del problema, evaluación y valor esperado. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **desempeño frente a la regla actual**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **explicabilidad**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Explicabilidad: frontera conceptual y error de clasificación

**Definición operacional:** capacidad de indicar qué factores influyeron en la puntuación. Su valor está en distinguirlo de **sesgo histórico**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Andrew Ng — *Machine Learning Yearning* (2018) —**lente:** diagnóstico de sistemas de aprendizaje y priorización de mejoras—. Formula dos mini-casos: uno que satisface la definición de **explicabilidad** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **desempeño por segmento** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «evaluar el desempeño frente a la regla manual actual», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Deriva del modelo: operacionalización y medición

**deriva del modelo** significa **pérdida de precisión por cambios en el mercado o en el proceso**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **desempeño frente a la regla actual**: `diferencia de precisión entre el modelo y la regla manual`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Cathy O'Neil — *Weapons of Math Destruction* (2016) orienta este bloque —**lente:** daños de los modelos opacos a escala y necesidad de auditoría—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Supervisión humana: trade-offs y efectos de segundo orden

**Definición:** revisión de decisiones del modelo por una persona responsable. Este concepto obliga a abandonar la idea de que lead scoring asistido por modelos tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «monitorear la deriva y recalibrar», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

NIST — *AI Risk Management Framework 1.0* (2023) —**lente:** gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **deriva observada** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **supervisión humana** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «mantener supervisión humana sobre las decisiones», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

NIST — *AI Risk Management Framework 1.0* (2023) sirve para contrastar la recomendación final desde otro lente: gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar. La frontera de esta clase es explícita: Un modelo que no puede explicarse no será usado por el equipo comercial. La explicabilidad no es un lujo: determina la adopción. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar lead scoring asistido por modelos no consiste en sumar definiciones. Empieza por **sesgo histórico**, contrasta **explicabilidad** con **deriva del modelo**, incorpora **supervisión humana** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | pensamiento analítico: formulación del problema, evaluación y valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Andrew Ng — *Machine Learning Yearning* (2018) | diagnóstico de sistemas de aprendizaje y priorización de mejoras | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Cathy O'Neil — *Weapons of Math Destruction* (2016) | daños de los modelos opacos a escala y necesidad de auditoría | ¿Qué supuesto de esta clase ayuda a desafiar? |
| NIST — *AI Risk Management Framework 1.0* (2023) | gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El modelo de Ruta Andina asigna puntajes bajos a los talleres de regiones porque históricamente se les prospectó menos, no porque conviertan peor.

**Paso 1 — Verificar volumen y calidad de datos antes de modelar.** El equipo escribe primero el supuesto asociado a **sesgo histórico** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **desempeño frente a la regla actual** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Evaluar el desempeño frente a la regla manual actual.** El trabajo aquí es separar lo observado de lo inferido sobre **explicabilidad**. La evidencia que ordena la discusión es **desempeño por segmento**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Revisar el sesgo por segmento.** El riesgo de este paso es cerrar demasiado rápido alrededor de **deriva del modelo**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **deriva observada** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Monitorear la deriva y recalibrar.** Con **supervisión humana** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **desempeño frente a la regla actual** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Mantener supervisión humana sobre las decisiones.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **sesgo histórico**. **desempeño por segmento** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **sesgo histórico** | Reproducción de patrones del pasado que pueden ser injustos o subóptimos | Cuando **desempeño frente a la regla actual** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **explicabilidad** | Capacidad de indicar qué factores influyeron en la puntuación | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un modelo que no puede explicarse no será usado por el equipo comercial. La explicabilidad no es un lujo: determina la adopción.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre lead scoring asistido por modelos |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager con IA, RevOps, Marketing manager y Sales enablement. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El modelo de Ruta Andina asigna puntajes bajos a los talleres de regiones porque históricamente se les prospectó menos, no porque conviertan peor.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **verificar volumen y calidad de datos antes de modelar → evaluar el desempeño frente a la regla manual actual → revisar el sesgo por segmento → monitorear la deriva y recalibrar → mantener supervisión humana sobre las decisiones** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **desempeño frente a la regla actual**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **sesgo histórico** y **explicabilidad** como sinónimos | Se perdió la distinción entre «reproducción de patrones del pasado que pueden ser injustos o subóptimos» y «capacidad de indicar qué factores influyeron en la puntuación» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «mantener supervisión humana sobre las decisiones» | Se saltó «verificar volumen y calidad de datos antes de modelar»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **desempeño frente a la regla actual** | La métrica local reemplazó al resultado del sistema | Contrástala con **deriva observada** y explicita el costo de oportunidad. |
| Desplegar el modelo sin revisar el sesgo por segmento | Error específico de esta clase | Compara el desempeño entre segmentos y corrige antes de usarlo para priorizar. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **sesgo histórico** y **explicabilidad** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **deriva del modelo** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «verificar volumen y calidad de datos antes de modelar» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **desempeño frente a la regla actual** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un modelo que no puede explicarse no será usado por el equipo comercial. La explicabilidad no es un lujo: determina la adopción»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P21-C07-lead-scoring-asistido/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **desempeño frente a la regla actual**, **desempeño por segmento** y **deriva observada** con fuente, ventana y lectura prohibida.
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

- Foster Provost y Tom Fawcett — *Data Science for Business* (2013). **Uso en esta clase:** pensamiento analítico: formulación del problema, evaluación y valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Andrew Ng — *Machine Learning Yearning* (2018). **Uso en esta clase:** diagnóstico de sistemas de aprendizaje y priorización de mejoras. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Cathy O'Neil — *Weapons of Math Destruction* (2016). **Uso en esta clase:** daños de los modelos opacos a escala y necesidad de auditoría. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- NIST — *AI Risk Management Framework 1.0* (2023). **Uso en esta clase:** gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 06 · Investigación de prospectos asistida](class-06-lead-research.md) · [Índice de la parte](README.md) · [Clase 08 · Copilotos de ventas](class-08-copilotos-de-ventas.md) →
