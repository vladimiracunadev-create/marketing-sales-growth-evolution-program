---
title: "Workflows"
type: class
language: es
standard: clase-profunda-v1
part: 17
class: 06
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["diorio", "grove", "nist-airmf", "provost"]
updated: 2026-08-19
---

# Clase 17.06 — Workflows

**Parte 17 · Marketing automation y revenue operations** · Nivel: Operación de ingresos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

## 🎯 Propósito

Un flujo automatizado es código que actúa sobre clientes. Como todo código, necesita documentación, control de versiones, pruebas y un responsable. La práctica habitual —crear flujos sin registro, sin pruebas y sin dueño— produce sistemas donde nadie sabe por qué un cliente recibió un mensaje y nadie puede corregirlo con seguridad.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 17 busca **integrar marketing, ventas y servicio en un solo modelo de datos y de proceso**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **workflows** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué automatizo porque mejora el sistema y qué estaría solo escalando un desorden?

Los conceptos que estructuran la sesión son **condición de entrada**, **condición de salida**, **prueba en ambiente controlado** y **documentación del flujo**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `condición de entrada`, `condición de salida`, `prueba en ambiente controlado` y `documentación del flujo` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Marketing automation y revenue operations**.
3. **Aplicar** la secuencia **documentar propósito y condiciones antes de construir → probar con registros de prueba → activar con volumen limitado y monitoreo → registrar responsable y fecha de revisión → auditar flujos activos cada semestre y retirar los obsoletos** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **flujos documentados**, **flujos sin responsable** y **errores detectados en pruebas** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **condición de entrada** y **condición de salida** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **flujos documentados**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **condición de entrada** | criterio que determina qué registros ingresan al flujo | Da un hecho compatible con la definición y otro que la refute. |
| **condición de salida** | criterio que retira al registro del flujo | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **prueba en ambiente controlado** | verificación del comportamiento antes de activar sobre datos reales | Construye un caso límite donde el concepto se confunde con el anterior. |
| **documentación del flujo** | registro de propósito, condiciones, responsable y fecha de revisión | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. documentar propósito y condiciones antes de construir → 2. probar con registros de prueba → 3. activar con volumen limitado y monitoreo → 4. registrar responsable y fecha de revisión → 5. auditar flujos activos cada semestre y retirar los obsoletos
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Probar todos los casos límite es imposible. El control complementario es el monitoreo posterior y la capacidad de detener el flujo rápidamente.

## 📖 Desarrollo

### 1. Condición de entrada: mecanismo central

**condición de entrada** se entiende aquí como **criterio que determina qué registros ingresan al flujo**. Es la pieza desde la que se inicia el análisis de workflows: antes de «documentar propósito y condiciones antes de construir», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022). **Lente que aporta:** integración de datos, procesos y equipos que producen ingreso como un solo sistema. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **flujos documentados**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **condición de salida**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Condición de salida: frontera conceptual y error de clasificación

**Definición operacional:** criterio que retira al registro del flujo. Su valor está en distinguirlo de **condición de entrada**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Andrew S. Grove — *High Output Management* (1983) —**lente:** output gerencial, indicadores adelantados y reuniones como herramienta de producción—. Formula dos mini-casos: uno que satisface la definición de **condición de salida** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **flujos sin responsable** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «probar con registros de prueba», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Prueba en ambiente controlado: operacionalización y medición

**prueba en ambiente controlado** significa **verificación del comportamiento antes de activar sobre datos reales**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **flujos documentados**: `automatizaciones con documentación completa, sobre automatizaciones activas`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

NIST — *AI Risk Management Framework 1.0* (2023) orienta este bloque —**lente:** gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Documentación del flujo: trade-offs y efectos de segundo orden

**Definición:** registro de propósito, condiciones, responsable y fecha de revisión. Este concepto obliga a abandonar la idea de que workflows tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «registrar responsable y fecha de revisión», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Foster Provost y Tom Fawcett — *Data Science for Business* (2013) —**lente:** pensamiento analítico: formulación del problema, evaluación y valor esperado— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **errores detectados en pruebas** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **documentación del flujo** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «auditar flujos activos cada semestre y retirar los obsoletos», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Foster Provost y Tom Fawcett — *Data Science for Business* (2013) sirve para contrastar la recomendación final desde otro lente: pensamiento analítico: formulación del problema, evaluación y valor esperado. La frontera de esta clase es explícita: Probar todos los casos límite es imposible. El control complementario es el monitoreo posterior y la capacidad de detener el flujo rápidamente. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar workflows no consiste en sumar definiciones. Empieza por **condición de entrada**, contrasta **condición de salida** con **prueba en ambiente controlado**, incorpora **documentación del flujo** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) | integración de datos, procesos y equipos que producen ingreso como un solo sistema | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Andrew S. Grove — *High Output Management* (1983) | output gerencial, indicadores adelantados y reuniones como herramienta de producción | ¿Qué supuesto de esta clase ayuda a desafiar? |
| NIST — *AI Risk Management Framework 1.0* (2023) | gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | pensamiento analítico: formulación del problema, evaluación y valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina tiene 14 automatizaciones activas. Dos envían el mismo correo, una nunca se desactivó tras una campaña de 2025 y ninguna tiene responsable.

**Paso 1 — Documentar propósito y condiciones antes de construir.** El equipo escribe primero el supuesto asociado a **condición de entrada** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **flujos documentados** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Probar con registros de prueba.** El trabajo aquí es separar lo observado de lo inferido sobre **condición de salida**. La evidencia que ordena la discusión es **flujos sin responsable**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Activar con volumen limitado y monitoreo.** El riesgo de este paso es cerrar demasiado rápido alrededor de **prueba en ambiente controlado**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **errores detectados en pruebas** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Registrar responsable y fecha de revisión.** Con **documentación del flujo** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **flujos documentados** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Auditar flujos activos cada semestre y retirar los obsoletos.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **condición de entrada**. **flujos sin responsable** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **condición de entrada** | Criterio que determina qué registros ingresan al flujo | Cuando **flujos documentados** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **condición de salida** | Criterio que retira al registro del flujo | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Probar todos los casos límite es imposible. El control complementario es el monitoreo posterior y la capacidad de detener el flujo rápidamente.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre workflows |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing ops, RevOps manager y Sales ops. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina tiene 14 automatizaciones activas. Dos envían el mismo correo, una nunca se desactivó tras una campaña de 2025 y ninguna tiene responsable.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **documentar propósito y condiciones antes de construir → probar con registros de prueba → activar con volumen limitado y monitoreo → registrar responsable y fecha de revisión → auditar flujos activos cada semestre y retirar los obsoletos** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **flujos documentados**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **condición de entrada** y **condición de salida** como sinónimos | Se perdió la distinción entre «criterio que determina qué registros ingresan al flujo» y «criterio que retira al registro del flujo» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «auditar flujos activos cada semestre y retirar los obsoletos» | Se saltó «documentar propósito y condiciones antes de construir»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **flujos documentados** | La métrica local reemplazó al resultado del sistema | Contrástala con **errores detectados en pruebas** y explicita el costo de oportunidad. |
| Activar flujos sin prueba ni responsable | Error específico de esta clase | Exige documentación, prueba controlada y dueño asignado antes de activar cualquier flujo. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **condición de entrada** y **condición de salida** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **prueba en ambiente controlado** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «documentar propósito y condiciones antes de construir» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **flujos documentados** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Probar todos los casos límite es imposible. El control complementario es el monitoreo posterior y la capacidad de detener el flujo rápidamente»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P17-C06-workflows/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **flujos documentados**, **flujos sin responsable** y **errores detectados en pruebas** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **operating model de RevOps con lifecycle, scoring, SLA, integraciones y observabilidad**.

## ✅ Evaluación de la clase

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables entre los conceptos de la clase. |
| Diagnóstico y evidencia | 30 % | Datos pertinentes, línea base, supuestos explícitos y límites del dato. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas y argumento ejecutivo trazable. |

**Aprobación:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambios a otra clase se considera insuficiente.

## 📗 Fuentes y verificación

- Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022). **Uso en esta clase:** integración de datos, procesos y equipos que producen ingreso como un solo sistema. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Andrew S. Grove — *High Output Management* (1983). **Uso en esta clase:** output gerencial, indicadores adelantados y reuniones como herramienta de producción. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- NIST — *AI Risk Management Framework 1.0* (2023). **Uso en esta clase:** gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013). **Uso en esta clase:** pensamiento analítico: formulación del problema, evaluación y valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 05 · Nurturing](class-05-nurturing.md) · [Índice de la parte](README.md) · [Clase 07 · Acuerdo de servicio entre marketing y ventas](class-07-sla-marketing-ventas.md) →
