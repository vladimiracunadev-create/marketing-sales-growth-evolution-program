---
title: "Diseño de experimentos"
type: class
language: es
standard: clase-profunda-v1
part: 19
class: 11
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["kohavi", "provost", "laja", "wheeler-dv"]
updated: 2026-08-19
---

# Clase 19.11 — Diseño de experimentos

**Parte 19 · Growth marketing y growth engineering** · Nivel: Crecimiento y analítica · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

## 🎯 Propósito

Un experimento válido requiere hipótesis previa, asignación comparable, tamaño suficiente, duración que cubra el ciclo y métricas guardarraíl. Kohavi documenta las trampas más comunes: detención temprana, comparaciones múltiples sin corrección y contaminación entre grupos. Un experimento mal diseñado no es neutro: produce conclusiones falsas con apariencia de rigor.

El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta. La parte 19 busca **instalar un motor de experimentación que produzca aprendizaje acumulativo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **diseño de experimentos** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué bucle hace que el crecimiento se retroalimente en lugar de depender del gasto?

Los conceptos que estructuran la sesión son **asignación comparable**, **tamaño mínimo detectable**, **métrica guardarraíl** y **contaminación**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `asignación comparable`, `tamaño mínimo detectable`, `métrica guardarraíl` y `contaminación` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Growth marketing y growth engineering**.
3. **Aplicar** la secuencia **formular la hipótesis y las métricas antes de iniciar → calcular tamaño y duración necesarios → verificar la comparabilidad de los grupos → ejecutar sin detener anticipadamente → analizar con el criterio previo y documentar** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **potencia del experimento**, **experimentos detenidos anticipadamente** y **resultados replicados** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **asignación comparable** y **tamaño mínimo detectable** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **potencia del experimento**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **asignación comparable** | distribución de sujetos que hace equivalentes a los grupos | Da un hecho compatible con la definición y otro que la refute. |
| **tamaño mínimo detectable** | efecto más pequeño que el experimento puede identificar con la muestra | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **métrica guardarraíl** | indicador que no debe deteriorarse aunque mejore la métrica principal | Construye un caso límite donde el concepto se confunde con el anterior. |
| **contaminación** | situación en que el tratamiento afecta también al grupo de control | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. formular la hipótesis y las métricas antes de iniciar → 2. calcular tamaño y duración necesarios → 3. verificar la comparabilidad de los grupos → 4. ejecutar sin detener anticipadamente → 5. analizar con el criterio previo y documentar
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** En volúmenes bajos, la experimentación rigurosa es inviable. La alternativa honesta es decidir con investigación cualitativa y declarar la incertidumbre.

## 📖 Desarrollo

### 1. Asignación comparable: mecanismo central

**asignación comparable** se entiende aquí como **distribución de sujetos que hace equivalentes a los grupos**. Es la pieza desde la que se inicia el análisis de diseño de experimentos: antes de «formular la hipótesis y las métricas antes de iniciar», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020). **Lente que aporta:** diseño estadístico de experimentos, métricas guardrail y trampas de interpretación. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **potencia del experimento**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **tamaño mínimo detectable**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Tamaño mínimo detectable: frontera conceptual y error de clasificación

**Definición operacional:** efecto más pequeño que el experimento puede identificar con la muestra. Su valor está en distinguirlo de **asignación comparable**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Foster Provost y Tom Fawcett — *Data Science for Business* (2013) —**lente:** pensamiento analítico: formulación del problema, evaluación y valor esperado—. Formula dos mini-casos: uno que satisface la definición de **tamaño mínimo detectable** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **experimentos detenidos anticipadamente** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «calcular tamaño y duración necesarios», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Métrica guardarraíl: operacionalización y medición

**métrica guardarraíl** significa **indicador que no debe deteriorarse aunque mejore la métrica principal**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **potencia del experimento**: `probabilidad de detectar el efecto mínimo relevante con la muestra disponible, calculada antes de iniciar`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Peep Laja y el equipo de CXL — *Conversion Optimization Playbooks (CXL)* (2024) orienta este bloque —**lente:** método CRO basado en investigación previa al test y validez estadística—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Contaminación: trade-offs y efectos de segundo orden

**Definición:** situación en que el tratamiento afecta también al grupo de control. Este concepto obliga a abandonar la idea de que diseño de experimentos tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «ejecutar sin detener anticipadamente», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Donald J. Wheeler — *Understanding Variation* (2000) —**lente:** distinguir variación común de variación especial antes de reaccionar a un KPI— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **resultados replicados** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **contaminación** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «analizar con el criterio previo y documentar», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Donald J. Wheeler — *Understanding Variation* (2000) sirve para contrastar la recomendación final desde otro lente: distinguir variación común de variación especial antes de reaccionar a un KPI. La frontera de esta clase es explícita: En volúmenes bajos, la experimentación rigurosa es inviable. La alternativa honesta es decidir con investigación cualitativa y declarar la incertidumbre. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar diseño de experimentos no consiste en sumar definiciones. Empieza por **asignación comparable**, contrasta **tamaño mínimo detectable** con **métrica guardarraíl**, incorpora **contaminación** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | diseño estadístico de experimentos, métricas guardrail y trampas de interpretación | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | pensamiento analítico: formulación del problema, evaluación y valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Peep Laja y el equipo de CXL — *Conversion Optimization Playbooks (CXL)* (2024) | método CRO basado en investigación previa al test y validez estadística | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Donald J. Wheeler — *Understanding Variation* (2000) | distinguir variación común de variación especial antes de reaccionar a un KPI | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina declaró ganadora una variante tras cuatro días con 120 usuarios por grupo. El efecto desapareció al mes siguiente.

**Paso 1 — Formular la hipótesis y las métricas antes de iniciar.** El equipo escribe primero el supuesto asociado a **asignación comparable** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **potencia del experimento** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Calcular tamaño y duración necesarios.** El trabajo aquí es separar lo observado de lo inferido sobre **tamaño mínimo detectable**. La evidencia que ordena la discusión es **experimentos detenidos anticipadamente**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Verificar la comparabilidad de los grupos.** El riesgo de este paso es cerrar demasiado rápido alrededor de **métrica guardarraíl**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **resultados replicados** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Ejecutar sin detener anticipadamente.** Con **contaminación** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **potencia del experimento** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Analizar con el criterio previo y documentar.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **asignación comparable**. **experimentos detenidos anticipadamente** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **asignación comparable** | Distribución de sujetos que hace equivalentes a los grupos | Cuando **potencia del experimento** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **tamaño mínimo detectable** | Efecto más pequeño que el experimento puede identificar con la muestra | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** En volúmenes bajos, la experimentación rigurosa es inviable. La alternativa honesta es decidir con investigación cualitativa y declarar la incertidumbre.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre diseño de experimentos |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager, Growth engineer y Head of Growth. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina declaró ganadora una variante tras cuatro días con 120 usuarios por grupo. El efecto desapareció al mes siguiente.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **formular la hipótesis y las métricas antes de iniciar → calcular tamaño y duración necesarios → verificar la comparabilidad de los grupos → ejecutar sin detener anticipadamente → analizar con el criterio previo y documentar** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **potencia del experimento**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **asignación comparable** y **tamaño mínimo detectable** como sinónimos | Se perdió la distinción entre «distribución de sujetos que hace equivalentes a los grupos» y «efecto más pequeño que el experimento puede identificar con la muestra» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «analizar con el criterio previo y documentar» | Se saltó «formular la hipótesis y las métricas antes de iniciar»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **potencia del experimento** | La métrica local reemplazó al resultado del sistema | Contrástala con **resultados replicados** y explicita el costo de oportunidad. |
| Detener el experimento al ver un resultado favorable | Error específico de esta clase | Fija duración y tamaño antes de iniciar y analiza sólo al finalizar el plazo definido. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **asignación comparable** y **tamaño mínimo detectable** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **métrica guardarraíl** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «formular la hipótesis y las métricas antes de iniciar» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **potencia del experimento** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «En volúmenes bajos, la experimentación rigurosa es inviable. La alternativa honesta es decidir con investigación cualitativa y declarar la incertidumbre»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P19-C11-experiment-design/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **potencia del experimento**, **experimentos detenidos anticipadamente** y **resultados replicados** con fuente, ventana y lectura prohibida.
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

- Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020). **Uso en esta clase:** diseño estadístico de experimentos, métricas guardrail y trampas de interpretación. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013). **Uso en esta clase:** pensamiento analítico: formulación del problema, evaluación y valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Peep Laja y el equipo de CXL — *Conversion Optimization Playbooks (CXL)* (2024). **Uso en esta clase:** método CRO basado en investigación previa al test y validez estadística. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Donald J. Wheeler — *Understanding Variation* (2000). **Uso en esta clase:** distinguir variación común de variación especial antes de reaccionar a un KPI. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 10 · ICE, RICE y priorización](class-10-ice-rice-y-priorizacion.md) · [Índice de la parte](README.md) · [Clase 12 · Growth engineering](class-12-growth-engineering.md) →
