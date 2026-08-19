---
title: "Backlog de experimentos"
type: class
language: es
standard: clase-profunda-v3
part: 19
class: 09
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["ellis-brown", "kohavi", "ries-lean", "cagan"]
updated: 2026-08-18
---

# Clase 19.09 — Backlog de experimentos

**Parte 19 · Growth marketing y growth engineering** · Nivel: Crecimiento y analítica · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v3`

## 🎯 Propósito

Un backlog de experimentos convierte las ideas dispersas en una cola priorizada con hipótesis explícitas. Su valor está en la disciplina de formulación: cada entrada debe declarar qué se cree, por qué, qué se medirá y qué resultado la refutaría. Un backlog de ideas sin hipótesis es una lista de deseos que se ejecuta por simpatía.

Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales. La parte 19 busca **instalar un motor de experimentación que produzca aprendizaje acumulativo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **backlog de experimentos** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué bucle hace que el crecimiento se retroalimente en lugar de depender del gasto?

Los conceptos que estructuran la sesión son **entrada del backlog**, **fundamento de la hipótesis**, **esfuerzo estimado** y **aprendizaje esperado**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `entrada del backlog`, `fundamento de la hipótesis`, `esfuerzo estimado` y `aprendizaje esperado` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Growth marketing y growth engineering**.
3. **Aplicar** la secuencia **formular cada idea como hipótesis con fundamento → estimar esfuerzo y aprendizaje esperado → priorizar con un criterio explícito → ejecutar en orden y documentar el resultado → revisar el backlog con los aprendizajes acumulados** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **entradas con hipótesis completa**, **tasa de ejecución** y **aprendizajes por experimento** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **entrada del backlog** y **fundamento de la hipótesis** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **entradas con hipótesis completa**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **entrada del backlog** | experimento formulado con hipótesis, métrica y criterio de decisión | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **fundamento de la hipótesis** | evidencia o razonamiento que sostiene la expectativa | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **esfuerzo estimado** | recursos necesarios para ejecutar el experimento | Da un hecho compatible con la definición y otro que la refute. |
| **aprendizaje esperado** | valor de la información que producirá el resultado, gane o pierda | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. formular cada idea como hipótesis con fundamento → 2. estimar esfuerzo y aprendizaje esperado → 3. priorizar con un criterio explícito → 4. ejecutar en orden y documentar el resultado → 5. revisar el backlog con los aprendizajes acumulados
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un backlog muy formalizado puede frenar pruebas baratas y rápidas. El nivel de formalidad debe ser proporcional al costo del experimento.

## 📖 Desarrollo

### 1. Entrada del backlog: mecanismo central

**entrada del backlog** se entiende aquí como **experimento formulado con hipótesis, métrica y criterio de decisión**. Es la pieza desde la que se inicia el análisis de backlog de experimentos: antes de «formular cada idea como hipótesis con fundamento», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Sean Ellis y Morgan Brown — *Hacking Growth* (2017). **Lente que aporta:** equipo multifuncional, ciclo de experimentación y aha moment. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **entradas con hipótesis completa**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **fundamento de la hipótesis**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Fundamento de la hipótesis: frontera conceptual y error de clasificación

**Definición operacional:** evidencia o razonamiento que sostiene la expectativa. Su valor está en distinguirlo de **entrada del backlog**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) —**lente:** diseño estadístico de experimentos, métricas guardrail y trampas de interpretación—. Formula dos mini-casos: uno que satisface la definición de **fundamento de la hipótesis** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **tasa de ejecución** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «estimar esfuerzo y aprendizaje esperado», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Esfuerzo estimado: operacionalización y medición

**esfuerzo estimado** significa **recursos necesarios para ejecutar el experimento**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **entradas con hipótesis completa**: `entradas con hipótesis, métrica y criterio, sobre entradas del backlog`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Eric Ries — *The Lean Startup* (2011) orienta este bloque —**lente:** construir-medir-aprender, MVP y decisión de perseverar o pivotar—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Aprendizaje esperado: trade-offs y efectos de segundo orden

**Definición:** valor de la información que producirá el resultado, gane o pierda. Este concepto obliga a abandonar la idea de que backlog de experimentos tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «ejecutar en orden y documentar el resultado», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Marty Cagan — *Inspired* (2017, 2.ª ed.) —**lente:** descubrimiento de producto y riesgos de valor, usabilidad, viabilidad y factibilidad— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **aprendizajes por experimento** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **aprendizaje esperado** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar el backlog con los aprendizajes acumulados», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Marty Cagan — *Inspired* (2017, 2.ª ed.) sirve para contrastar la recomendación final desde otro lente: descubrimiento de producto y riesgos de valor, usabilidad, viabilidad y factibilidad. La frontera de esta clase es explícita: Un backlog muy formalizado puede frenar pruebas baratas y rápidas. El nivel de formalidad debe ser proporcional al costo del experimento. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar backlog de experimentos no consiste en sumar definiciones. Empieza por **entrada del backlog**, contrasta **fundamento de la hipótesis** con **esfuerzo estimado**, incorpora **aprendizaje esperado** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Sean Ellis y Morgan Brown — *Hacking Growth* (2017) | equipo multifuncional, ciclo de experimentación y aha moment | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | diseño estadístico de experimentos, métricas guardrail y trampas de interpretación | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Eric Ries — *The Lean Startup* (2011) | construir-medir-aprender, MVP y decisión de perseverar o pivotar | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Marty Cagan — *Inspired* (2017, 2.ª ed.) | descubrimiento de producto y riesgos de valor, usabilidad, viabilidad y factibilidad | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El backlog de Ruta Andina tiene 62 ideas sin hipótesis. Se ejecuta lo que propone quien tiene más influencia en la reunión.

**Paso 1 — Formular cada idea como hipótesis con fundamento.** El equipo escribe primero el supuesto asociado a **entrada del backlog** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **entradas con hipótesis completa** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Estimar esfuerzo y aprendizaje esperado.** El trabajo aquí es separar lo observado de lo inferido sobre **fundamento de la hipótesis**. La evidencia que ordena la discusión es **tasa de ejecución**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Priorizar con un criterio explícito.** El riesgo de este paso es cerrar demasiado rápido alrededor de **esfuerzo estimado**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **aprendizajes por experimento** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Ejecutar en orden y documentar el resultado.** Con **aprendizaje esperado** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **entradas con hipótesis completa** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar el backlog con los aprendizajes acumulados.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **entrada del backlog**. **tasa de ejecución** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **entrada del backlog** | Experimento formulado con hipótesis, métrica y criterio de decisión | Cuando **entradas con hipótesis completa** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **fundamento de la hipótesis** | Evidencia o razonamiento que sostiene la expectativa | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un backlog muy formalizado puede frenar pruebas baratas y rápidas. El nivel de formalidad debe ser proporcional al costo del experimento.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre backlog de experimentos |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager, Growth engineer y Head of Growth. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El backlog de Ruta Andina tiene 62 ideas sin hipótesis. Se ejecuta lo que propone quien tiene más influencia en la reunión.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **formular cada idea como hipótesis con fundamento → estimar esfuerzo y aprendizaje esperado → priorizar con un criterio explícito → ejecutar en orden y documentar el resultado → revisar el backlog con los aprendizajes acumulados** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **entradas con hipótesis completa**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **entrada del backlog** y **fundamento de la hipótesis** como sinónimos | Se perdió la distinción entre «experimento formulado con hipótesis, métrica y criterio de decisión» y «evidencia o razonamiento que sostiene la expectativa» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar el backlog con los aprendizajes acumulados» | Se saltó «formular cada idea como hipótesis con fundamento»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **entradas con hipótesis completa** | La métrica local reemplazó al resultado del sistema | Contrástala con **aprendizajes por experimento** y explicita el costo de oportunidad. |
| Mantener ideas sin hipótesis en el backlog | Error específico de esta clase | Exige hipótesis, métrica y criterio de refutación para cada entrada priorizada. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **entrada del backlog** y **fundamento de la hipótesis** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **esfuerzo estimado** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «formular cada idea como hipótesis con fundamento» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **entradas con hipótesis completa** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un backlog muy formalizado puede frenar pruebas baratas y rápidas. El nivel de formalidad debe ser proporcional al costo del experimento»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P19-C09-experiment-backlog/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **entradas con hipótesis completa**, **tasa de ejecución** y **aprendizajes por experimento** con fuente, ventana y lectura prohibida.
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
- Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020). **Uso en esta clase:** diseño estadístico de experimentos, métricas guardrail y trampas de interpretación. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Eric Ries — *The Lean Startup* (2011). **Uso en esta clase:** construir-medir-aprender, MVP y decisión de perseverar o pivotar. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Marty Cagan — *Inspired* (2017, 2.ª ed.). **Uso en esta clase:** descubrimiento de producto y riesgos de valor, usabilidad, viabilidad y factibilidad. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 08 · Viralidad](class-08-viralidad.md) · [Índice de la parte](README.md) · [Clase 10 · ICE, RICE y priorización](class-10-ice-rice-y-priorizacion.md) →
