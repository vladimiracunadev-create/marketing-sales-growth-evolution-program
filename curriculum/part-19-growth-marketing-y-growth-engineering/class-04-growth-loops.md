---
title: "Growth loops"
type: class
language: es
standard: clase-profunda-v1
part: 19
class: 04
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["ellis-brown", "bush-plg", "croll-yoskovitz", "weinberg-traction"]
updated: 2026-08-19
---

# Clase 19.04 — Growth loops

**Parte 19 · Growth marketing y growth engineering** · Nivel: Crecimiento y analítica · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

## 🎯 Propósito

Un bucle de crecimiento es un sistema donde el resultado de un ciclo alimenta el siguiente: clientes que producen contenido, referencias o datos que atraen a más clientes. A diferencia del embudo, que se agota, el bucle compone. Su construcción exige identificar qué output del cliente puede convertirse en input de adquisición sin intervención manual.

El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta. La parte 19 busca **instalar un motor de experimentación que produzca aprendizaje acumulativo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **growth loops** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué bucle hace que el crecimiento se retroalimente en lugar de depender del gasto?

Los conceptos que estructuran la sesión son **bucle de crecimiento**, **output del usuario**, **velocidad del bucle** y **factor de amplificación**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `bucle de crecimiento`, `output del usuario`, `velocidad del bucle` y `factor de amplificación` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Growth marketing y growth engineering**.
3. **Aplicar** la secuencia **identificar qué produce el usuario al usar el producto → evaluar si ese output puede atraer a otros → diseñar el mecanismo que cierra el bucle → medir velocidad y factor de amplificación → decidir si conviene invertir en el bucle o en canales directos** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **factor de amplificación**, **velocidad del bucle** y **proporción de adquisición por bucle** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **bucle de crecimiento** y **output del usuario** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **factor de amplificación**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **bucle de crecimiento** | sistema donde el resultado de un ciclo alimenta la entrada del siguiente | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **output del usuario** | producto de la actividad del cliente que puede atraer a otros | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **velocidad del bucle** | tiempo que tarda un ciclo completo en producir nuevos usuarios | Da un hecho compatible con la definición y otro que la refute. |
| **factor de amplificación** | número de nuevos usuarios que genera cada usuario existente por ciclo | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. identificar qué produce el usuario al usar el producto → 2. evaluar si ese output puede atraer a otros → 3. diseñar el mecanismo que cierra el bucle → 4. medir velocidad y factor de amplificación → 5. decidir si conviene invertir en el bucle o en canales directos
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** No todos los negocios admiten bucles: si el output del usuario no es visible para terceros, no hay mecanismo posible y forzarlo produce experiencias intrusivas.

## 📖 Desarrollo

### 1. Bucle de crecimiento: mecanismo central

**bucle de crecimiento** se entiende aquí como **sistema donde el resultado de un ciclo alimenta la entrada del siguiente**. Es la pieza desde la que se inicia el análisis de growth loops: antes de «identificar qué produce el usuario al usar el producto», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Sean Ellis y Morgan Brown — *Hacking Growth* (2017). **Lente que aporta:** equipo multifuncional, ciclo de experimentación y aha moment. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **factor de amplificación**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **output del usuario**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Output del usuario: frontera conceptual y error de clasificación

**Definición operacional:** producto de la actividad del cliente que puede atraer a otros. Su valor está en distinguirlo de **bucle de crecimiento**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Wes Bush — *Product-Led Growth* (2019) —**lente:** el producto como principal vehículo de adquisición, activación y expansión—. Formula dos mini-casos: uno que satisface la definición de **output del usuario** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **velocidad del bucle** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «evaluar si ese output puede atraer a otros», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Velocidad del bucle: operacionalización y medición

**velocidad del bucle** significa **tiempo que tarda un ciclo completo en producir nuevos usuarios**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **factor de amplificación**: `nuevos usuarios generados por usuario existente, por ciclo`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) orienta este bloque —**lente:** una métrica que importa por etapa y por modelo de negocio—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Factor de amplificación: trade-offs y efectos de segundo orden

**Definición:** número de nuevos usuarios que genera cada usuario existente por ciclo. Este concepto obliga a abandonar la idea de que growth loops tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «medir velocidad y factor de amplificación», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Gabriel Weinberg y Justin Mares — *Traction* (2015) —**lente:** diecinueve canales de tracción y el método bullseye de priorización— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **proporción de adquisición por bucle** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **factor de amplificación** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «decidir si conviene invertir en el bucle o en canales directos», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Gabriel Weinberg y Justin Mares — *Traction* (2015) sirve para contrastar la recomendación final desde otro lente: diecinueve canales de tracción y el método bullseye de priorización. La frontera de esta clase es explícita: No todos los negocios admiten bucles: si el output del usuario no es visible para terceros, no hay mecanismo posible y forzarlo produce experiencias intrusivas. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar growth loops no consiste en sumar definiciones. Empieza por **bucle de crecimiento**, contrasta **output del usuario** con **velocidad del bucle**, incorpora **factor de amplificación** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Sean Ellis y Morgan Brown — *Hacking Growth* (2017) | equipo multifuncional, ciclo de experimentación y aha moment | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Wes Bush — *Product-Led Growth* (2019) | el producto como principal vehículo de adquisición, activación y expansión | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | una métrica que importa por etapa y por modelo de negocio | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Gabriel Weinberg y Justin Mares — *Traction* (2015) | diecinueve canales de tracción y el método bullseye de priorización | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Cada cliente de Ruta Andina envía recordatorios de cita a sus propios clientes finales. Ese mensaje podría incluir una referencia visible y convertirse en un bucle.

**Paso 1 — Identificar qué produce el usuario al usar el producto.** El equipo escribe primero el supuesto asociado a **bucle de crecimiento** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **factor de amplificación** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Evaluar si ese output puede atraer a otros.** El trabajo aquí es separar lo observado de lo inferido sobre **output del usuario**. La evidencia que ordena la discusión es **velocidad del bucle**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Diseñar el mecanismo que cierra el bucle.** El riesgo de este paso es cerrar demasiado rápido alrededor de **velocidad del bucle**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **proporción de adquisición por bucle** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Medir velocidad y factor de amplificación.** Con **factor de amplificación** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **factor de amplificación** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Decidir si conviene invertir en el bucle o en canales directos.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **bucle de crecimiento**. **velocidad del bucle** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **bucle de crecimiento** | Sistema donde el resultado de un ciclo alimenta la entrada del siguiente | Cuando **factor de amplificación** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **output del usuario** | Producto de la actividad del cliente que puede atraer a otros | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** No todos los negocios admiten bucles: si el output del usuario no es visible para terceros, no hay mecanismo posible y forzarlo produce experiencias intrusivas.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre growth loops |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager, Growth engineer y Head of Growth. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Cada cliente de Ruta Andina envía recordatorios de cita a sus propios clientes finales. Ese mensaje podría incluir una referencia visible y convertirse en un bucle.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **identificar qué produce el usuario al usar el producto → evaluar si ese output puede atraer a otros → diseñar el mecanismo que cierra el bucle → medir velocidad y factor de amplificación → decidir si conviene invertir en el bucle o en canales directos** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **factor de amplificación**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **bucle de crecimiento** y **output del usuario** como sinónimos | Se perdió la distinción entre «sistema donde el resultado de un ciclo alimenta la entrada del siguiente» y «producto de la actividad del cliente que puede atraer a otros» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «decidir si conviene invertir en el bucle o en canales directos» | Se saltó «identificar qué produce el usuario al usar el producto»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **factor de amplificación** | La métrica local reemplazó al resultado del sistema | Contrástala con **proporción de adquisición por bucle** y explicita el costo de oportunidad. |
| Forzar un bucle donde el producto no lo permite | Error específico de esta clase | Verifica que exista un output visible para terceros antes de invertir en el mecanismo. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **bucle de crecimiento** y **output del usuario** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **velocidad del bucle** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «identificar qué produce el usuario al usar el producto» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **factor de amplificación** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «No todos los negocios admiten bucles: si el output del usuario no es visible para terceros, no hay mecanismo posible y forzarlo produce experiencias intrusivas»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P19-C04-growth-loops/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **factor de amplificación**, **velocidad del bucle** y **proporción de adquisición por bucle** con fuente, ventana y lectura prohibida.
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
- Wes Bush — *Product-Led Growth* (2019). **Uso en esta clase:** el producto como principal vehículo de adquisición, activación y expansión. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013). **Uso en esta clase:** una métrica que importa por etapa y por modelo de negocio. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Gabriel Weinberg y Justin Mares — *Traction* (2015). **Uso en esta clase:** diecinueve canales de tracción y el método bullseye de priorización. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 03 · AARRR](class-03-aarrr.md) · [Índice de la parte](README.md) · [Clase 05 · Activación](class-05-activation.md) →
