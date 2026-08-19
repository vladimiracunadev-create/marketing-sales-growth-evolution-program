---
title: "Activación"
type: class
language: es
standard: clase-profunda-v3
part: 19
class: 05
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["ellis-brown", "hulick", "croll-yoskovitz", "kohavi"]
updated: 2026-08-18
---

# Clase 19.05 — Activación

**Parte 19 · Growth marketing y growth engineering** · Nivel: Crecimiento y analítica · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v3`

## 🎯 Propósito

La activación es el momento en que el usuario experimenta el valor del producto por primera vez. Identificarla con precisión es una tarea analítica: consiste en encontrar qué acción, realizada en qué plazo, predice la permanencia. Una vez identificada, todo el diseño inicial debe orientarse a que ocurra lo antes posible.

La clase trata el tema como un problema de evidencia y de consecuencia, no como vocabulario. La parte 19 busca **instalar un motor de experimentación que produzca aprendizaje acumulativo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **activación** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué bucle hace que el crecimiento se retroalimente en lugar de depender del gasto?

Los conceptos que estructuran la sesión son **evento de activación**, **ventana de activación**, **análisis predictivo de activación** y **tasa de activación**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `evento de activación`, `ventana de activación`, `análisis predictivo de activación` y `tasa de activación` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Growth marketing y growth engineering**.
3. **Aplicar** la secuencia **analizar qué acciones distinguen a quienes permanecen → definir el evento y la ventana de activación → medir la tasa actual por segmento y origen → rediseñar el inicio para producir ese evento antes → verificar el efecto sobre la retención de las cohortes nuevas** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **tasa de activación**, **retención por activación** y **tiempo hasta la activación** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **evento de activación** y **ventana de activación** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **tasa de activación**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **evento de activación** | acción cuya realización predice la permanencia del usuario | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **ventana de activación** | plazo dentro del cual esa acción debe ocurrir para predecir retención | Da un hecho compatible con la definición y otro que la refute. |
| **análisis predictivo de activación** | método que identifica el evento a partir de datos históricos | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **tasa de activación** | usuarios que realizan el evento en la ventana, sobre usuarios incorporados | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. analizar qué acciones distinguen a quienes permanecen → 2. definir el evento y la ventana de activación → 3. medir la tasa actual por segmento y origen → 4. rediseñar el inicio para producir ese evento antes → 5. verificar el efecto sobre la retención de las cohortes nuevas
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** La correlación entre el evento y la retención no prueba causalidad: puede que quienes ya estaban comprometidos hagan ambas cosas. Verificarlo requiere un experimento.

## 📖 Desarrollo

### 1. Evento de activación: mecanismo central

**evento de activación** se entiende aquí como **acción cuya realización predice la permanencia del usuario**. Es la pieza desde la que se inicia el análisis de activación: antes de «analizar qué acciones distinguen a quienes permanecen», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Sean Ellis y Morgan Brown — *Hacking Growth* (2017). **Lente que aporta:** equipo multifuncional, ciclo de experimentación y aha moment. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **tasa de activación**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **ventana de activación**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Ventana de activación: frontera conceptual y error de clasificación

**Definición operacional:** plazo dentro del cual esa acción debe ocurrir para predecir retención. Su valor está en distinguirlo de **evento de activación**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Samuel Hulick — *The Elements of User Onboarding* (2014) —**lente:** diseño del primer valor percibido y reducción del time-to-value—. Formula dos mini-casos: uno que satisface la definición de **ventana de activación** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **retención por activación** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «definir el evento y la ventana de activación», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Análisis predictivo de activación: operacionalización y medición

**análisis predictivo de activación** significa **método que identifica el evento a partir de datos históricos**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **tasa de activación**: `usuarios activados en la ventana, sobre usuarios incorporados`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) orienta este bloque —**lente:** una métrica que importa por etapa y por modelo de negocio—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Tasa de activación: trade-offs y efectos de segundo orden

**Definición:** usuarios que realizan el evento en la ventana, sobre usuarios incorporados. Este concepto obliga a abandonar la idea de que activación tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «rediseñar el inicio para producir ese evento antes», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) —**lente:** diseño estadístico de experimentos, métricas guardrail y trampas de interpretación— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **tiempo hasta la activación** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **tasa de activación** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «verificar el efecto sobre la retención de las cohortes nuevas», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) sirve para contrastar la recomendación final desde otro lente: diseño estadístico de experimentos, métricas guardrail y trampas de interpretación. La frontera de esta clase es explícita: La correlación entre el evento y la retención no prueba causalidad: puede que quienes ya estaban comprometidos hagan ambas cosas. Verificarlo requiere un experimento. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar activación no consiste en sumar definiciones. Empieza por **evento de activación**, contrasta **ventana de activación** con **análisis predictivo de activación**, incorpora **tasa de activación** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Sean Ellis y Morgan Brown — *Hacking Growth* (2017) | equipo multifuncional, ciclo de experimentación y aha moment | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Samuel Hulick — *The Elements of User Onboarding* (2014) | diseño del primer valor percibido y reducción del time-to-value | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | una métrica que importa por etapa y por modelo de negocio | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | diseño estadístico de experimentos, métricas guardrail y trampas de interpretación | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El análisis de Ruta Andina muestra que quienes cargan más de 20 clientes en la primera semana retienen 3,4 veces más. Sólo el 22 % lo hace.

**Paso 1 — Analizar qué acciones distinguen a quienes permanecen.** El equipo escribe primero el supuesto asociado a **evento de activación** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **tasa de activación** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Definir el evento y la ventana de activación.** El trabajo aquí es separar lo observado de lo inferido sobre **ventana de activación**. La evidencia que ordena la discusión es **retención por activación**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Medir la tasa actual por segmento y origen.** El riesgo de este paso es cerrar demasiado rápido alrededor de **análisis predictivo de activación**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **tiempo hasta la activación** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Rediseñar el inicio para producir ese evento antes.** Con **tasa de activación** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **tasa de activación** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Verificar el efecto sobre la retención de las cohortes nuevas.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **evento de activación**. **retención por activación** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **evento de activación** | Acción cuya realización predice la permanencia del usuario | Cuando **tasa de activación** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **ventana de activación** | Plazo dentro del cual esa acción debe ocurrir para predecir retención | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** La correlación entre el evento y la retención no prueba causalidad: puede que quienes ya estaban comprometidos hagan ambas cosas. Verificarlo requiere un experimento.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre activación |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager, Growth engineer y Head of Growth. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El análisis de Ruta Andina muestra que quienes cargan más de 20 clientes en la primera semana retienen 3,4 veces más. Sólo el 22 % lo hace.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **analizar qué acciones distinguen a quienes permanecen → definir el evento y la ventana de activación → medir la tasa actual por segmento y origen → rediseñar el inicio para producir ese evento antes → verificar el efecto sobre la retención de las cohortes nuevas** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **tasa de activación**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **evento de activación** y **ventana de activación** como sinónimos | Se perdió la distinción entre «acción cuya realización predice la permanencia del usuario» y «plazo dentro del cual esa acción debe ocurrir para predecir retención» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «verificar el efecto sobre la retención de las cohortes nuevas» | Se saltó «analizar qué acciones distinguen a quienes permanecen»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **tasa de activación** | La métrica local reemplazó al resultado del sistema | Contrástala con **tiempo hasta la activación** y explicita el costo de oportunidad. |
| Confundir correlación con causalidad en el evento de activación | Error específico de esta clase | Diseña un experimento que induzca el evento y verifica si la retención mejora. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **evento de activación** y **ventana de activación** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **análisis predictivo de activación** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «analizar qué acciones distinguen a quienes permanecen» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **tasa de activación** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «La correlación entre el evento y la retención no prueba causalidad: puede que quienes ya estaban comprometidos hagan ambas cosas. Verificarlo requiere un experimento»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P19-C05-activation/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **tasa de activación**, **retención por activación** y **tiempo hasta la activación** con fuente, ventana y lectura prohibida.
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
- Samuel Hulick — *The Elements of User Onboarding* (2014). **Uso en esta clase:** diseño del primer valor percibido y reducción del time-to-value. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013). **Uso en esta clase:** una métrica que importa por etapa y por modelo de negocio. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020). **Uso en esta clase:** diseño estadístico de experimentos, métricas guardrail y trampas de interpretación. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 04 · Growth loops](class-04-growth-loops.md) · [Índice de la parte](README.md) · [Clase 06 · Crecimiento centrado en retención](class-06-retention-first-growth.md) →
