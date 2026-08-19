---
title: "Crecimiento centrado en retención"
type: class
language: es
standard: clase-profunda-v3
part: 19
class: 06
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["ellis-brown", "fader", "croll-yoskovitz", "mehta"]
updated: 2026-08-18
---

# Clase 19.06 — Crecimiento centrado en retención

**Parte 19 · Growth marketing y growth engineering** · Nivel: Crecimiento y analítica · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v3`

## 🎯 Propósito

Invertir en adquisición con retención deficiente es llenar un estanque con fuga. El orden correcto es diagnóstico: si la curva de retención no se estabiliza, el problema es de encaje o de producto y ningún canal lo compensa. Esta es la decisión más contraintuitiva de growth, porque la presión organizacional siempre empuja hacia más leads.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 19 busca **instalar un motor de experimentación que produzca aprendizaje acumulativo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **crecimiento centrado en retención** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué bucle hace que el crecimiento se retroalimente en lugar de depender del gasto?

Los conceptos que estructuran la sesión son **curva estabilizada**, **orden de inversión**, **costo de la fuga** y **umbral de escalamiento**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `curva estabilizada`, `orden de inversión`, `costo de la fuga` y `umbral de escalamiento` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Growth marketing y growth engineering**.
3. **Aplicar** la secuencia **verificar si la curva de retención se estabiliza → definir el umbral que autoriza escalar adquisición → calcular el costo de la fuga actual → priorizar intervenciones de retención → escalar adquisición sólo tras superar el umbral** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **nivel de estabilización de la curva**, **costo de la fuga** y **relación inversión retención-adquisición** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **curva estabilizada** y **orden de inversión** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **nivel de estabilización de la curva**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **curva estabilizada** | retención que deja de caer y se aplana en un nivel positivo | Da un hecho compatible con la definición y otro que la refute. |
| **orden de inversión** | secuencia que prioriza retención antes que adquisición | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **costo de la fuga** | ingreso perdido por invertir en adquisición sobre una base que no retiene | Construye un caso límite donde el concepto se confunde con el anterior. |
| **umbral de escalamiento** | nivel de retención a partir del cual conviene escalar adquisición | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. verificar si la curva de retención se estabiliza → 2. definir el umbral que autoriza escalar adquisición → 3. calcular el costo de la fuga actual → 4. priorizar intervenciones de retención → 5. escalar adquisición sólo tras superar el umbral
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Detener toda adquisición mientras se arregla la retención puede matar la caja. La decisión realista es sostener y no escalar hasta superar el umbral.

## 📖 Desarrollo

### 1. Curva estabilizada: mecanismo central

**curva estabilizada** se entiende aquí como **retención que deja de caer y se aplana en un nivel positivo**. Es la pieza desde la que se inicia el análisis de crecimiento centrado en retención: antes de «verificar si la curva de retención se estabiliza», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Sean Ellis y Morgan Brown — *Hacking Growth* (2017). **Lente que aporta:** equipo multifuncional, ciclo de experimentación y aha moment. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **nivel de estabilización de la curva**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **orden de inversión**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Orden de inversión: frontera conceptual y error de clasificación

**Definición operacional:** secuencia que prioriza retención antes que adquisición. Su valor está en distinguirlo de **curva estabilizada**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Peter Fader — *Customer Centricity* (2020, 2.ª ed.) —**lente:** valor heterogéneo del cliente y asignación de recursos por valor esperado—. Formula dos mini-casos: uno que satisface la definición de **orden de inversión** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **costo de la fuga** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «definir el umbral que autoriza escalar adquisición», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Costo de la fuga: operacionalización y medición

**costo de la fuga** significa **ingreso perdido por invertir en adquisición sobre una base que no retiene**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **nivel de estabilización de la curva**: `porcentaje en que la retención se aplana, por cohorte`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) orienta este bloque —**lente:** una métrica que importa por etapa y por modelo de negocio—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Umbral de escalamiento: trade-offs y efectos de segundo orden

**Definición:** nivel de retención a partir del cual conviene escalar adquisición. Este concepto obliga a abandonar la idea de que crecimiento centrado en retención tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «priorizar intervenciones de retención», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) —**lente:** disciplina operativa de éxito de cliente: salud, renovación y expansión— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **relación inversión retención-adquisición** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **umbral de escalamiento** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «escalar adquisición sólo tras superar el umbral», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) sirve para contrastar la recomendación final desde otro lente: disciplina operativa de éxito de cliente: salud, renovación y expansión. La frontera de esta clase es explícita: Detener toda adquisición mientras se arregla la retención puede matar la caja. La decisión realista es sostener y no escalar hasta superar el umbral. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar crecimiento centrado en retención no consiste en sumar definiciones. Empieza por **curva estabilizada**, contrasta **orden de inversión** con **costo de la fuga**, incorpora **umbral de escalamiento** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Sean Ellis y Morgan Brown — *Hacking Growth* (2017) | equipo multifuncional, ciclo de experimentación y aha moment | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Peter Fader — *Customer Centricity* (2020, 2.ª ed.) | valor heterogéneo del cliente y asignación de recursos por valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | una métrica que importa por etapa y por modelo de negocio | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) | disciplina operativa de éxito de cliente: salud, renovación y expansión | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina planea duplicar su inversión publicitaria. Sus cohortes pierden el 38 % de los clientes antes del día 90 y la curva no se ha estabilizado en ninguna cohorte.

**Paso 1 — Verificar si la curva de retención se estabiliza.** El equipo escribe primero el supuesto asociado a **curva estabilizada** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **nivel de estabilización de la curva** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Definir el umbral que autoriza escalar adquisición.** El trabajo aquí es separar lo observado de lo inferido sobre **orden de inversión**. La evidencia que ordena la discusión es **costo de la fuga**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Calcular el costo de la fuga actual.** El riesgo de este paso es cerrar demasiado rápido alrededor de **costo de la fuga**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **relación inversión retención-adquisición** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Priorizar intervenciones de retención.** Con **umbral de escalamiento** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **nivel de estabilización de la curva** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Escalar adquisición sólo tras superar el umbral.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **curva estabilizada**. **costo de la fuga** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **curva estabilizada** | Retención que deja de caer y se aplana en un nivel positivo | Cuando **nivel de estabilización de la curva** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **orden de inversión** | Secuencia que prioriza retención antes que adquisición | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Detener toda adquisición mientras se arregla la retención puede matar la caja. La decisión realista es sostener y no escalar hasta superar el umbral.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre crecimiento centrado en retención |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager, Growth engineer y Head of Growth. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina planea duplicar su inversión publicitaria. Sus cohortes pierden el 38 % de los clientes antes del día 90 y la curva no se ha estabilizado en ninguna cohorte.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **verificar si la curva de retención se estabiliza → definir el umbral que autoriza escalar adquisición → calcular el costo de la fuga actual → priorizar intervenciones de retención → escalar adquisición sólo tras superar el umbral** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **nivel de estabilización de la curva**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **curva estabilizada** y **orden de inversión** como sinónimos | Se perdió la distinción entre «retención que deja de caer y se aplana en un nivel positivo» y «secuencia que prioriza retención antes que adquisición» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «escalar adquisición sólo tras superar el umbral» | Se saltó «verificar si la curva de retención se estabiliza»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **nivel de estabilización de la curva** | La métrica local reemplazó al resultado del sistema | Contrástala con **relación inversión retención-adquisición** y explicita el costo de oportunidad. |
| Escalar adquisición con retención no estabilizada | Error específico de esta clase | Define el umbral de retención que autoriza escalar y respétalo como regla de inversión. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **curva estabilizada** y **orden de inversión** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **costo de la fuga** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «verificar si la curva de retención se estabiliza» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **nivel de estabilización de la curva** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Detener toda adquisición mientras se arregla la retención puede matar la caja. La decisión realista es sostener y no escalar hasta superar el umbral»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P19-C06-retention-first-growth/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **nivel de estabilización de la curva**, **costo de la fuga** y **relación inversión retención-adquisición** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **growth model con North Star, bucles, backlog priorizado y resultados de experimentos**.

## ✅ Evaluación de la clase

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables entre los conceptos de la clase. |
| Diagnóstico y evidencia | 30 % | Datos pertinentes, línea base, supuestos explícitos y límites del dato. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas y argumento ejecutivo trazable. |

**Aprobación:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambios a otra clase se considera insuficiente.

## 📗 Fuentes y verificación

- Sean Ellis y Morgan Brown — *Hacking Growth* (2017). **Uso en esta clase:** equipo multifuncional, ciclo de experimentación y aha moment. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Peter Fader — *Customer Centricity* (2020, 2.ª ed.). **Uso en esta clase:** valor heterogéneo del cliente y asignación de recursos por valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013). **Uso en esta clase:** una métrica que importa por etapa y por modelo de negocio. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016). **Uso en esta clase:** disciplina operativa de éxito de cliente: salud, renovación y expansión. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 05 · Activación](class-05-activation.md) · [Índice de la parte](README.md) · [Clase 07 · Bucles de referencia](class-07-referral-loops.md) →
