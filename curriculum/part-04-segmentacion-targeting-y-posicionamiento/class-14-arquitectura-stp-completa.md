---
title: "Arquitectura STP completa"
type: class
language: es
standard: clase-profunda-v3
part: 04
class: 14
level: Fundamentos
mastery_threshold: 80
estimated_minutes: 150
sources: ["kotler", "rumelt", "ries-trout", "moore"]
updated: 2026-08-18
---

# Clase 04.14 — Arquitectura STP completa

**Parte 04 · Segmentación, targeting y posicionamiento** · Nivel: Fundamentos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v3`

## 🎯 Propósito

Esta clase integra segmentación, targeting y posicionamiento en un documento único y coherente: quién es el segmento prioritario, por qué se eligió, qué se descartó, cuál es la promesa y qué evidencia la sostiene. La prueba de coherencia es que la arquitectura permita rechazar decisiones concretas: un canal, una funcionalidad, una campaña que no correspondan al foco elegido.

Esta sesión distingue lo que se sabe, lo que se supone y lo que todavía no se ha medido. La parte 04 busca **elegir a quién servir y ocupar un lugar defendible en la mente del cliente**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **arquitectura STP completa** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué segmento puedo servir mejor que nadie y con qué diferencia comprobable?

Los conceptos que estructuran la sesión son **arquitectura STP**, **coherencia interna**, **decisión descartada** y **indicador de seguimiento**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `arquitectura STP`, `coherencia interna`, `decisión descartada` y `indicador de seguimiento` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Segmentación, targeting y posicionamiento**.
3. **Aplicar** la secuencia **consolidar la segmentación con sus criterios y evidencia → declarar el foco y los descartes con su justificación → fijar la declaración de posicionamiento y su prueba → verificar coherencia entre promesa, precio, canal y operación → definir los indicadores de seguimiento y su periodicidad** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **coherencia auditada**, **evolución de participación en el segmento prioritario** y **costo de adquisición en el foco** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **arquitectura STP** y **coherencia interna** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **coherencia auditada**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **arquitectura STP** | documento que conecta segmentación, elección de objetivo y posicionamiento con sus fundamentos | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **coherencia interna** | ausencia de contradicción entre segmento elegido, promesa, precio y canal | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **decisión descartada** | opción explícitamente rechazada con su razón, que impide reabrir la discusión sin datos nuevos | Da un hecho compatible con la definición y otro que la refute. |
| **indicador de seguimiento** | métrica que informa si la estrategia elegida está produciendo el efecto esperado | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. consolidar la segmentación con sus criterios y evidencia → 2. declarar el foco y los descartes con su justificación → 3. fijar la declaración de posicionamiento y su prueba → 4. verificar coherencia entre promesa, precio, canal y operación → 5. definir los indicadores de seguimiento y su periodicidad
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** La arquitectura es una hipótesis estratégica, no una verdad. Debe revisarse con datos de resultado y no defenderse por costo hundido.

## 📖 Desarrollo

### 1. Arquitectura STP: mecanismo central

**arquitectura STP** se entiende aquí como **documento que conecta segmentación, elección de objetivo y posicionamiento con sus fundamentos**. Es la pieza desde la que se inicia el análisis de arquitectura STP completa: antes de «consolidar la segmentación con sus criterios y evidencia», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Philip Kotler, Kevin Lane Keller y Alexander Chernev — *Marketing Management* (2021, 16.ª ed.). **Lente que aporta:** estructura canónica del marketing: análisis, STP, mezcla comercial y gestión de la demanda. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **coherencia auditada**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **coherencia interna**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Coherencia interna: frontera conceptual y error de clasificación

**Definición operacional:** ausencia de contradicción entre segmento elegido, promesa, precio y canal. Su valor está en distinguirlo de **arquitectura STP**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Richard Rumelt — *Good Strategy / Bad Strategy* (2011) —**lente:** diagnóstico, política rectora y acción coherente frente a la estrategia decorativa—. Formula dos mini-casos: uno que satisface la definición de **coherencia interna** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **evolución de participación en el segmento prioritario** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «declarar el foco y los descartes con su justificación», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Decisión descartada: operacionalización y medición

**decisión descartada** significa **opción explícitamente rechazada con su razón, que impide reabrir la discusión sin datos nuevos**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **coherencia auditada**: `decisiones comerciales del trimestre compatibles con la arquitectura, sobre decisiones revisadas`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Al Ries y Jack Trout — *Positioning: The Battle for Your Mind* (2001, ed. revisada) orienta este bloque —**lente:** posicionamiento como lugar en la mente del cliente y no como declaración interna—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Indicador de seguimiento: trade-offs y efectos de segundo orden

**Definición:** métrica que informa si la estrategia elegida está produciendo el efecto esperado. Este concepto obliga a abandonar la idea de que arquitectura STP completa tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «verificar coherencia entre promesa, precio, canal y operación», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Geoffrey A. Moore — *Crossing the Chasm* (2014, 3.ª ed.) —**lente:** adopción tecnológica, beachhead market y el abismo entre visionarios y pragmáticos— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **costo de adquisición en el foco** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **indicador de seguimiento** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «definir los indicadores de seguimiento y su periodicidad», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Geoffrey A. Moore — *Crossing the Chasm* (2014, 3.ª ed.) sirve para contrastar la recomendación final desde otro lente: adopción tecnológica, beachhead market y el abismo entre visionarios y pragmáticos. La frontera de esta clase es explícita: La arquitectura es una hipótesis estratégica, no una verdad. Debe revisarse con datos de resultado y no defenderse por costo hundido. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Segmentar con variables decorativas que no cambian oferta, canal ni mensaje.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar arquitectura STP completa no consiste en sumar definiciones. Empieza por **arquitectura STP**, contrasta **coherencia interna** con **decisión descartada**, incorpora **indicador de seguimiento** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Philip Kotler, Kevin Lane Keller y Alexander Chernev — *Marketing Management* (2021, 16.ª ed.) | estructura canónica del marketing: análisis, STP, mezcla comercial y gestión de la demanda | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Richard Rumelt — *Good Strategy / Bad Strategy* (2011) | diagnóstico, política rectora y acción coherente frente a la estrategia decorativa | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Al Ries y Jack Trout — *Positioning: The Battle for Your Mind* (2001, ed. revisada) | posicionamiento como lugar en la mente del cliente y no como declaración interna | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Geoffrey A. Moore — *Crossing the Chasm* (2014, 3.ª ed.) | adopción tecnológica, beachhead market y el abismo entre visionarios y pragmáticos | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina debe presentar su arquitectura STP al directorio como base del presupuesto anual. Hoy conviven tres focos declarados en documentos distintos.

**Paso 1 — Consolidar la segmentación con sus criterios y evidencia.** El equipo escribe primero el supuesto asociado a **arquitectura STP** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **coherencia auditada** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Declarar el foco y los descartes con su justificación.** El trabajo aquí es separar lo observado de lo inferido sobre **coherencia interna**. La evidencia que ordena la discusión es **evolución de participación en el segmento prioritario**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Fijar la declaración de posicionamiento y su prueba.** El riesgo de este paso es cerrar demasiado rápido alrededor de **decisión descartada**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **costo de adquisición en el foco** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Verificar coherencia entre promesa, precio, canal y operación.** Con **indicador de seguimiento** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **coherencia auditada** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Definir los indicadores de seguimiento y su periodicidad.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **arquitectura STP**. **evolución de participación en el segmento prioritario** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **arquitectura STP** | Documento que conecta segmentación, elección de objetivo y posicionamiento con sus fundamentos | Cuando **coherencia auditada** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **coherencia interna** | Ausencia de contradicción entre segmento elegido, promesa, precio y canal | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** La arquitectura es una hipótesis estratégica, no una verdad. Debe revisarse con datos de resultado y no defenderse por costo hundido.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre arquitectura STP completa |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing manager, Product marketing y Head of Growth. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina debe presentar su arquitectura STP al directorio como base del presupuesto anual. Hoy conviven tres focos declarados en documentos distintos.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **consolidar la segmentación con sus criterios y evidencia → declarar el foco y los descartes con su justificación → fijar la declaración de posicionamiento y su prueba → verificar coherencia entre promesa, precio, canal y operación → definir los indicadores de seguimiento y su periodicidad** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **coherencia auditada**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **arquitectura STP** y **coherencia interna** como sinónimos | Se perdió la distinción entre «documento que conecta segmentación, elección de objetivo y posicionamiento con sus fundamentos» y «ausencia de contradicción entre segmento elegido, promesa, precio y canal» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «definir los indicadores de seguimiento y su periodicidad» | Se saltó «consolidar la segmentación con sus criterios y evidencia»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **coherencia auditada** | La métrica local reemplazó al resultado del sistema | Contrástala con **costo de adquisición en el foco** y explicita el costo de oportunidad. |
| Mantener varios focos declarados simultáneamente | Error específico de esta clase | Consolida en un documento único y archiva formalmente las versiones anteriores. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **arquitectura STP** y **coherencia interna** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **decisión descartada** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «consolidar la segmentación con sus criterios y evidencia» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **coherencia auditada** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «La arquitectura es una hipótesis estratégica, no una verdad. Debe revisarse con datos de resultado y no defenderse por costo hundido»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Segmentar con variables decorativas que no cambian oferta, canal ni mensaje.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P04-C14-arquitectura-stp-completa/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **coherencia auditada**, **evolución de participación en el segmento prioritario** y **costo de adquisición en el foco** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **arquitectura STP con criterios de atractivo, accesibilidad y declaración de posicionamiento probada**.

## ✅ Evaluación de la clase

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables entre los conceptos de la clase. |
| Diagnóstico y evidencia | 30 % | Datos pertinentes, línea base, supuestos explícitos y límites del dato. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas y argumento ejecutivo trazable. |

**Aprobación:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambios a otra clase se considera insuficiente.

## 📗 Fuentes y verificación

- Philip Kotler, Kevin Lane Keller y Alexander Chernev — *Marketing Management* (2021, 16.ª ed.). **Uso en esta clase:** estructura canónica del marketing: análisis, STP, mezcla comercial y gestión de la demanda. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Richard Rumelt — *Good Strategy / Bad Strategy* (2011). **Uso en esta clase:** diagnóstico, política rectora y acción coherente frente a la estrategia decorativa. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Al Ries y Jack Trout — *Positioning: The Battle for Your Mind* (2001, ed. revisada). **Uso en esta clase:** posicionamiento como lugar en la mente del cliente y no como declaración interna. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Geoffrey A. Moore — *Crossing the Chasm* (2014, 3.ª ed.). **Uso en esta clase:** adopción tecnológica, beachhead market y el abismo entre visionarios y pragmáticos. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 13 · Prueba de posicionamiento](class-13-prueba-de-posicionamiento.md) · [Índice de la parte](README.md)
