---
title: "Tracking y atribución"
type: class
language: es
standard: clase-profunda-v1
part: 14
class: 11
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["kaushik", "provost", "kohavi", "chaffey"]
updated: 2026-08-19
---

# Clase 14.11 — Tracking y atribución

**Parte 14 · Publicidad y performance marketing** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

## 🎯 Propósito

Medir publicidad exige instrumentación: parámetros de campaña consistentes, eventos de conversión bien definidos y una convención de nomenclatura que permita analizar. Sin eso, cada informe requiere reconstruir manualmente qué significa cada fila. Las restricciones de privacidad reducen la cobertura del rastreo, lo que obliga a combinar medición de plataforma con datos propios del CRM.

El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta. La parte 14 busca **invertir en medios pagados con control de costo, calidad y riesgo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **tracking y atribución** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué unidad de resultado estoy comprando y a qué costo marginal deja de tener sentido?

Los conceptos que estructuran la sesión son **convención de nomenclatura**, **evento de conversión**, **cobertura de medición** y **reconciliación con CRM**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `convención de nomenclatura`, `evento de conversión`, `cobertura de medición` y `reconciliación con CRM` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Publicidad y performance marketing**.
3. **Aplicar** la secuencia **definir la convención de nomenclatura y aplicarla → instrumentar eventos con definición documentada → estimar la cobertura real de la medición → reconciliar con el CRM cada mes → declarar el margen de error en los informes** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **consistencia de etiquetado**, **diferencia plataforma-CRM** y **cobertura de medición estimada** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **convención de nomenclatura** y **evento de conversión** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **consistencia de etiquetado**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **convención de nomenclatura** | regla uniforme para etiquetar campañas, fuentes y medios | Da un hecho compatible con la definición y otro que la refute. |
| **evento de conversión** | acción registrada que representa un resultado relevante | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **cobertura de medición** | proporción de las conversiones reales que el sistema logra registrar | Construye un caso límite donde el concepto se confunde con el anterior. |
| **reconciliación con CRM** | contraste entre lo reportado por plataformas y lo registrado internamente | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir la convención de nomenclatura y aplicarla → 2. instrumentar eventos con definición documentada → 3. estimar la cobertura real de la medición → 4. reconciliar con el CRM cada mes → 5. declarar el margen de error en los informes
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Ninguna instrumentación recupera la cobertura completa bajo las restricciones actuales de privacidad. La medición debe leerse como estimación con error conocido.

## 📖 Desarrollo

### 1. Convención de nomenclatura: mecanismo central

**convención de nomenclatura** se entiende aquí como **regla uniforme para etiquetar campañas, fuentes y medios**. Es la pieza desde la que se inicia el análisis de tracking y atribución: antes de «definir la convención de nomenclatura y aplicarla», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Avinash Kaushik — *Web Analytics 2.0* (2009). **Lente que aporta:** medición orientada a decisión, segmentación y crítica del dato de vanidad. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **consistencia de etiquetado**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **evento de conversión**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Evento de conversión: frontera conceptual y error de clasificación

**Definición operacional:** acción registrada que representa un resultado relevante. Su valor está en distinguirlo de **convención de nomenclatura**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Foster Provost y Tom Fawcett — *Data Science for Business* (2013) —**lente:** pensamiento analítico: formulación del problema, evaluación y valor esperado—. Formula dos mini-casos: uno que satisface la definición de **evento de conversión** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **diferencia plataforma-CRM** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «instrumentar eventos con definición documentada», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Cobertura de medición: operacionalización y medición

**cobertura de medición** significa **proporción de las conversiones reales que el sistema logra registrar**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **consistencia de etiquetado**: `sesiones con parámetros correctos, sobre sesiones de campañas`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) orienta este bloque —**lente:** diseño estadístico de experimentos, métricas guardrail y trampas de interpretación—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Reconciliación con CRM: trade-offs y efectos de segundo orden

**Definición:** contraste entre lo reportado por plataformas y lo registrado internamente. Este concepto obliga a abandonar la idea de que tracking y atribución tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «reconciliar con el CRM cada mes», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) —**lente:** planificación digital integrada: canales, medición y gobierno— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **cobertura de medición estimada** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **reconciliación con CRM** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «declarar el margen de error en los informes», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) sirve para contrastar la recomendación final desde otro lente: planificación digital integrada: canales, medición y gobierno. La frontera de esta clase es explícita: Ninguna instrumentación recupera la cobertura completa bajo las restricciones actuales de privacidad. La medición debe leerse como estimación con error conocido. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Atribuirse demanda existente, inflar el retorno y decidir presupuesto sobre una ilusión.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar tracking y atribución no consiste en sumar definiciones. Empieza por **convención de nomenclatura**, contrasta **evento de conversión** con **cobertura de medición**, incorpora **reconciliación con CRM** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Avinash Kaushik — *Web Analytics 2.0* (2009) | medición orientada a decisión, segmentación y crítica del dato de vanidad | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | pensamiento analítico: formulación del problema, evaluación y valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | diseño estadístico de experimentos, métricas guardrail y trampas de interpretación | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) | planificación digital integrada: canales, medición y gobierno | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Las plataformas reportan 96 conversiones mensuales a Ruta Andina y el CRM registra 41 oportunidades. Nadie ha reconciliado ambas cifras.

**Paso 1 — Definir la convención de nomenclatura y aplicarla.** El equipo escribe primero el supuesto asociado a **convención de nomenclatura** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **consistencia de etiquetado** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Instrumentar eventos con definición documentada.** El trabajo aquí es separar lo observado de lo inferido sobre **evento de conversión**. La evidencia que ordena la discusión es **diferencia plataforma-CRM**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Estimar la cobertura real de la medición.** El riesgo de este paso es cerrar demasiado rápido alrededor de **cobertura de medición**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **cobertura de medición estimada** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Reconciliar con el CRM cada mes.** Con **reconciliación con CRM** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **consistencia de etiquetado** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Declarar el margen de error en los informes.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **convención de nomenclatura**. **diferencia plataforma-CRM** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **convención de nomenclatura** | Regla uniforme para etiquetar campañas, fuentes y medios | Cuando **consistencia de etiquetado** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **evento de conversión** | Acción registrada que representa un resultado relevante | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Ninguna instrumentación recupera la cobertura completa bajo las restricciones actuales de privacidad. La medición debe leerse como estimación con error conocido.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre tracking y atribución |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Performance marketer, Media buyer y Growth marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Las plataformas reportan 96 conversiones mensuales a Ruta Andina y el CRM registra 41 oportunidades. Nadie ha reconciliado ambas cifras.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **definir la convención de nomenclatura y aplicarla → instrumentar eventos con definición documentada → estimar la cobertura real de la medición → reconciliar con el CRM cada mes → declarar el margen de error en los informes** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **consistencia de etiquetado**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **convención de nomenclatura** y **evento de conversión** como sinónimos | Se perdió la distinción entre «regla uniforme para etiquetar campañas, fuentes y medios» y «acción registrada que representa un resultado relevante» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «declarar el margen de error en los informes» | Se saltó «definir la convención de nomenclatura y aplicarla»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **consistencia de etiquetado** | La métrica local reemplazó al resultado del sistema | Contrástala con **cobertura de medición estimada** y explicita el costo de oportunidad. |
| Reportar cifras de plataforma sin reconciliar con el CRM | Error específico de esta clase | Concilia mensualmente y publica la diferencia junto con el informe. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **convención de nomenclatura** y **evento de conversión** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **cobertura de medición** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir la convención de nomenclatura y aplicarla» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **consistencia de etiquetado** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Ninguna instrumentación recupera la cobertura completa bajo las restricciones actuales de privacidad. La medición debe leerse como estimación con error conocido»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Atribuirse demanda existente, inflar el retorno y decidir presupuesto sobre una ilusión.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P14-C11-tracking-y-atribucion/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **consistencia de etiquetado**, **diferencia plataforma-CRM** y **cobertura de medición estimada** con fuente, ventana y lectura prohibida.
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

- Avinash Kaushik — *Web Analytics 2.0* (2009). **Uso en esta clase:** medición orientada a decisión, segmentación y crítica del dato de vanidad. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013). **Uso en esta clase:** pensamiento analítico: formulación del problema, evaluación y valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020). **Uso en esta clase:** diseño estadístico de experimentos, métricas guardrail y trampas de interpretación. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.). **Uso en esta clase:** planificación digital integrada: canales, medición y gobierno. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 10 · CPA, CAC y ROAS](class-10-cpa-cac-y-roas.md) · [Índice de la parte](README.md) · [Clase 12 · Optimización de campañas](class-12-optimizacion-de-campanas.md) →
