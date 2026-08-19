---
title: "Métricas de go-to-market"
type: class
language: es
standard: clase-profunda-v3
part: 22
class: 13
level: IA y expansión
mastery_threshold: 80
estimated_minutes: 150
sources: ["croll-yoskovitz", "ross", "bush-plg", "kaplan-norton"]
updated: 2026-08-18
---

# Clase 22.13 — Métricas de go-to-market

**Parte 22 · Go-to-market, canales y expansión** · Nivel: IA y expansión · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v3`

## 🎯 Propósito

Evaluar una estrategia de salida al mercado exige métricas que capturen eficiencia y no sólo crecimiento: costo de adquisición por movimiento, periodo de recuperación, productividad por persona, contribución por canal y velocidad de escalamiento. Crecer perdiendo eficiencia no es un éxito comercial: es una apuesta financiera que alguien deberá pagar.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 22 busca **diseñar el modo en que la oferta llega al mercado y decide crecer**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **métricas de go-to-market** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué movimiento comercial corresponde al valor del contrato, al ciclo y al comprador?

Los conceptos que estructuran la sesión son **eficiencia del crecimiento**, **productividad por movimiento**, **contribución por canal** y **velocidad de escalamiento**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `eficiencia del crecimiento`, `productividad por movimiento`, `contribución por canal` y `velocidad de escalamiento` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Go-to-market, canales y expansión**.
3. **Aplicar** la secuencia **definir las métricas por movimiento y por canal → medir eficiencia además de crecimiento → comparar la eficiencia entre movimientos → identificar dónde la eficiencia se deteriora al escalar → ajustar la asignación según el resultado** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **eficiencia del crecimiento**, **periodo de recuperación por movimiento** y **deterioro de eficiencia al escalar** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **eficiencia del crecimiento** y **productividad por movimiento** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **eficiencia del crecimiento**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **eficiencia del crecimiento** | relación entre el ingreso incremental y el gasto necesario para producirlo | Construye un caso límite donde el concepto se confunde con el anterior. |
| **productividad por movimiento** | resultado obtenido por unidad de capacidad en cada movimiento comercial | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **contribución por canal** | margen que aporta cada canal después de sus costos | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **velocidad de escalamiento** | rapidez con que el movimiento puede aumentar su producción | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir las métricas por movimiento y por canal → 2. medir eficiencia además de crecimiento → 3. comparar la eficiencia entre movimientos → 4. identificar dónde la eficiencia se deteriora al escalar → 5. ajustar la asignación según el resultado
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** En etapas tempranas puede ser racional sacrificar eficiencia para ganar posición. Lo que no es racional es hacerlo sin declararlo ni medirlo.

## 📖 Desarrollo

### 1. Eficiencia del crecimiento: mecanismo central

**eficiencia del crecimiento** se entiende aquí como **relación entre el ingreso incremental y el gasto necesario para producirlo**. Es la pieza desde la que se inicia el análisis de métricas de go-to-market: antes de «definir las métricas por movimiento y por canal», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013). **Lente que aporta:** una métrica que importa por etapa y por modelo de negocio. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **eficiencia del crecimiento**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **productividad por movimiento**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Productividad por movimiento: frontera conceptual y error de clasificación

**Definición operacional:** resultado obtenido por unidad de capacidad en cada movimiento comercial. Su valor está en distinguirlo de **eficiencia del crecimiento**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Aaron Ross y Marylou Tyler — *Predictable Revenue* (2011) —**lente:** especialización de roles comerciales y generación de pipeline predecible—. Formula dos mini-casos: uno que satisface la definición de **productividad por movimiento** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **periodo de recuperación por movimiento** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «medir eficiencia además de crecimiento», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Contribución por canal: operacionalización y medición

**contribución por canal** significa **margen que aporta cada canal después de sus costos**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **eficiencia del crecimiento**: `ingreso incremental del periodo, sobre gasto comercial incremental`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Wes Bush — *Product-Led Growth* (2019) orienta este bloque —**lente:** el producto como principal vehículo de adquisición, activación y expansión—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Velocidad de escalamiento: trade-offs y efectos de segundo orden

**Definición:** rapidez con que el movimiento puede aumentar su producción. Este concepto obliga a abandonar la idea de que métricas de go-to-market tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «identificar dónde la eficiencia se deteriora al escalar», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) —**lente:** traducción de la estrategia en indicadores causalmente conectados— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **deterioro de eficiencia al escalar** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **velocidad de escalamiento** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «ajustar la asignación según el resultado», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) sirve para contrastar la recomendación final desde otro lente: traducción de la estrategia en indicadores causalmente conectados. La frontera de esta clase es explícita: En etapas tempranas puede ser racional sacrificar eficiencia para ganar posición. Lo que no es racional es hacerlo sin declararlo ni medirlo. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Abrir frentes simultáneos sin capacidad, diluir foco y llegar tarde a todos.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar métricas de go-to-market no consiste en sumar definiciones. Empieza por **eficiencia del crecimiento**, contrasta **productividad por movimiento** con **contribución por canal**, incorpora **velocidad de escalamiento** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | una métrica que importa por etapa y por modelo de negocio | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Aaron Ross y Marylou Tyler — *Predictable Revenue* (2011) | especialización de roles comerciales y generación de pipeline predecible | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Wes Bush — *Product-Led Growth* (2019) | el producto como principal vehículo de adquisición, activación y expansión | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) | traducción de la estrategia en indicadores causalmente conectados | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina creció 40 % en ingreso y su gasto comercial creció 78 %. El plan celebra el crecimiento y no menciona el deterioro de eficiencia.

**Paso 1 — Definir las métricas por movimiento y por canal.** El equipo escribe primero el supuesto asociado a **eficiencia del crecimiento** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **eficiencia del crecimiento** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Medir eficiencia además de crecimiento.** El trabajo aquí es separar lo observado de lo inferido sobre **productividad por movimiento**. La evidencia que ordena la discusión es **periodo de recuperación por movimiento**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Comparar la eficiencia entre movimientos.** El riesgo de este paso es cerrar demasiado rápido alrededor de **contribución por canal**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **deterioro de eficiencia al escalar** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Identificar dónde la eficiencia se deteriora al escalar.** Con **velocidad de escalamiento** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **eficiencia del crecimiento** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Ajustar la asignación según el resultado.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **eficiencia del crecimiento**. **periodo de recuperación por movimiento** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **eficiencia del crecimiento** | Relación entre el ingreso incremental y el gasto necesario para producirlo | Cuando **eficiencia del crecimiento** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **productividad por movimiento** | Resultado obtenido por unidad de capacidad en cada movimiento comercial | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** En etapas tempranas puede ser racional sacrificar eficiencia para ganar posición. Lo que no es racional es hacerlo sin declararlo ni medirlo.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre métricas de go-to-market |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Head of GTM, Partnerships, Product marketing y Founder. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina creció 40 % en ingreso y su gasto comercial creció 78 %. El plan celebra el crecimiento y no menciona el deterioro de eficiencia.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **definir las métricas por movimiento y por canal → medir eficiencia además de crecimiento → comparar la eficiencia entre movimientos → identificar dónde la eficiencia se deteriora al escalar → ajustar la asignación según el resultado** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **eficiencia del crecimiento**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **eficiencia del crecimiento** y **productividad por movimiento** como sinónimos | Se perdió la distinción entre «relación entre el ingreso incremental y el gasto necesario para producirlo» y «resultado obtenido por unidad de capacidad en cada movimiento comercial» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «ajustar la asignación según el resultado» | Se saltó «definir las métricas por movimiento y por canal»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **eficiencia del crecimiento** | La métrica local reemplazó al resultado del sistema | Contrástala con **deterioro de eficiencia al escalar** y explicita el costo de oportunidad. |
| Reportar crecimiento sin reportar eficiencia | Error específico de esta clase | Presenta el ingreso incremental junto al gasto incremental que lo produjo. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **eficiencia del crecimiento** y **productividad por movimiento** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **contribución por canal** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir las métricas por movimiento y por canal» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **eficiencia del crecimiento** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «En etapas tempranas puede ser racional sacrificar eficiencia para ganar posición. Lo que no es racional es hacerlo sin declararlo ni medirlo»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Abrir frentes simultáneos sin capacidad, diluir foco y llegar tarde a todos.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P22-C13-gtm-metrics/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **eficiencia del crecimiento**, **periodo de recuperación por movimiento** y **deterioro de eficiencia al escalar** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **plan GTM completo con beachhead, movimiento comercial, canales, economía y plan de lanzamiento**.

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
- Aaron Ross y Marylou Tyler — *Predictable Revenue* (2011). **Uso en esta clase:** especialización de roles comerciales y generación de pipeline predecible. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Wes Bush — *Product-Led Growth* (2019). **Uso en esta clase:** el producto como principal vehículo de adquisición, activación y expansión. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996). **Uso en esta clase:** traducción de la estrategia en indicadores causalmente conectados. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 12 · Internacionalización](class-12-internacionalizacion.md) · [Índice de la parte](README.md) · [Clase 14 · Plan go-to-market completo](class-14-plan-gtm-completo.md) →
