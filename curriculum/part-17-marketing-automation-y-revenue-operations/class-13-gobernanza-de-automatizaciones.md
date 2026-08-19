---
title: "Gobernanza de automatizaciones"
type: class
language: es
standard: clase-profunda-v1
part: 17
class: 13
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["nist-airmf", "diorio", "iso-31000", "oneil"]
updated: 2026-08-19
---

# Clase 17.13 — Gobernanza de automatizaciones

**Parte 17 · Marketing automation y revenue operations** · Nivel: Operación de ingresos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

## 🎯 Propósito

La gobernanza define quién puede crear, modificar y desactivar automatizaciones, con qué aprobación y con qué registro. Su ausencia produce sistemas donde nadie puede explicar por qué un cliente recibió un mensaje, lo que además es un problema de cumplimiento: la normativa de datos exige poder acreditar el tratamiento realizado.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 17 busca **integrar marketing, ventas y servicio en un solo modelo de datos y de proceso**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **gobernanza de automatizaciones** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué automatizo porque mejora el sistema y qué estaría solo escalando un desorden?

Los conceptos que estructuran la sesión son **autoridad de cambio**, **registro de tratamiento**, **revisión periódica** y **retiro de automatizaciones**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `autoridad de cambio`, `registro de tratamiento`, `revisión periódica` y `retiro de automatizaciones` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Marketing automation y revenue operations**.
3. **Aplicar** la secuencia **definir autoridad de cambio por tipo de automatización → documentar propósito y base legal de cada flujo → establecer la revisión periódica y su alcance → retirar los flujos obsoletos → mantener el registro de tratamiento actualizado** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **flujos con base legal documentada**, **flujos retirados por revisión** y **cambios con aprobación registrada** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **autoridad de cambio** y **registro de tratamiento** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **flujos con base legal documentada**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **autoridad de cambio** | definición de quién puede modificar qué en el sistema automatizado | Construye un caso límite donde el concepto se confunde con el anterior. |
| **registro de tratamiento** | documentación de qué datos se usaron, con qué finalidad y bajo qué base | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **revisión periódica** | auditoría programada de las automatizaciones activas | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **retiro de automatizaciones** | proceso de desactivar flujos que ya no cumplen función | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir autoridad de cambio por tipo de automatización → 2. documentar propósito y base legal de cada flujo → 3. establecer la revisión periódica y su alcance → 4. retirar los flujos obsoletos → 5. mantener el registro de tratamiento actualizado
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Una gobernanza pesada frena la operación. El nivel de control debe ser proporcional al riesgo: mayor para flujos que tratan datos personales o comprometen a la empresa.

## 📖 Desarrollo

### 1. Autoridad de cambio: mecanismo central

**autoridad de cambio** se entiende aquí como **definición de quién puede modificar qué en el sistema automatizado**. Es la pieza desde la que se inicia el análisis de gobernanza de automatizaciones: antes de «definir autoridad de cambio por tipo de automatización», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es NIST — *AI Risk Management Framework 1.0* (2023). **Lente que aporta:** gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **flujos con base legal documentada**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **registro de tratamiento**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Registro de tratamiento: frontera conceptual y error de clasificación

**Definición operacional:** documentación de qué datos se usaron, con qué finalidad y bajo qué base. Su valor está en distinguirlo de **autoridad de cambio**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) —**lente:** integración de datos, procesos y equipos que producen ingreso como un solo sistema—. Formula dos mini-casos: uno que satisface la definición de **registro de tratamiento** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **flujos retirados por revisión** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «documentar propósito y base legal de cada flujo», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Revisión periódica: operacionalización y medición

**revisión periódica** significa **auditoría programada de las automatizaciones activas**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **flujos con base legal documentada**: `automatizaciones con finalidad y base registradas, sobre automatizaciones activas`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

ISO — *ISO 31000: Gestión del riesgo* (2018) orienta este bloque —**lente:** vocabulario y proceso de gestión de riesgo aplicable a decisiones comerciales—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Retiro de automatizaciones: trade-offs y efectos de segundo orden

**Definición:** proceso de desactivar flujos que ya no cumplen función. Este concepto obliga a abandonar la idea de que gobernanza de automatizaciones tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «retirar los flujos obsoletos», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Cathy O'Neil — *Weapons of Math Destruction* (2016) —**lente:** daños de los modelos opacos a escala y necesidad de auditoría— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **cambios con aprobación registrada** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **retiro de automatizaciones** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «mantener el registro de tratamiento actualizado», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Cathy O'Neil — *Weapons of Math Destruction* (2016) sirve para contrastar la recomendación final desde otro lente: daños de los modelos opacos a escala y necesidad de auditoría. La frontera de esta clase es explícita: Una gobernanza pesada frena la operación. El nivel de control debe ser proporcional al riesgo: mayor para flujos que tratan datos personales o comprometen a la empresa. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar gobernanza de automatizaciones no consiste en sumar definiciones. Empieza por **autoridad de cambio**, contrasta **registro de tratamiento** con **revisión periódica**, incorpora **retiro de automatizaciones** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| NIST — *AI Risk Management Framework 1.0* (2023) | gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) | integración de datos, procesos y equipos que producen ingreso como un solo sistema | ¿Qué supuesto de esta clase ayuda a desafiar? |
| ISO — *ISO 31000: Gestión del riesgo* (2018) | vocabulario y proceso de gestión de riesgo aplicable a decisiones comerciales | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Cathy O'Neil — *Weapons of Math Destruction* (2016) | daños de los modelos opacos a escala y necesidad de auditoría | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina no puede explicar por qué un cliente recibió una comunicación de una campaña que terminó hace ocho meses, ni con qué base de datos se envió.

**Paso 1 — Definir autoridad de cambio por tipo de automatización.** El equipo escribe primero el supuesto asociado a **autoridad de cambio** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **flujos con base legal documentada** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Documentar propósito y base legal de cada flujo.** El trabajo aquí es separar lo observado de lo inferido sobre **registro de tratamiento**. La evidencia que ordena la discusión es **flujos retirados por revisión**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Establecer la revisión periódica y su alcance.** El riesgo de este paso es cerrar demasiado rápido alrededor de **revisión periódica**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **cambios con aprobación registrada** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Retirar los flujos obsoletos.** Con **retiro de automatizaciones** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **flujos con base legal documentada** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Mantener el registro de tratamiento actualizado.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **autoridad de cambio**. **flujos retirados por revisión** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **autoridad de cambio** | Definición de quién puede modificar qué en el sistema automatizado | Cuando **flujos con base legal documentada** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **registro de tratamiento** | Documentación de qué datos se usaron, con qué finalidad y bajo qué base | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Una gobernanza pesada frena la operación. El nivel de control debe ser proporcional al riesgo: mayor para flujos que tratan datos personales o comprometen a la empresa.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre gobernanza de automatizaciones |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing ops, RevOps manager y Sales ops. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina no puede explicar por qué un cliente recibió una comunicación de una campaña que terminó hace ocho meses, ni con qué base de datos se envió.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **definir autoridad de cambio por tipo de automatización → documentar propósito y base legal de cada flujo → establecer la revisión periódica y su alcance → retirar los flujos obsoletos → mantener el registro de tratamiento actualizado** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **flujos con base legal documentada**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **autoridad de cambio** y **registro de tratamiento** como sinónimos | Se perdió la distinción entre «definición de quién puede modificar qué en el sistema automatizado» y «documentación de qué datos se usaron, con qué finalidad y bajo qué base» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «mantener el registro de tratamiento actualizado» | Se saltó «definir autoridad de cambio por tipo de automatización»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **flujos con base legal documentada** | La métrica local reemplazó al resultado del sistema | Contrástala con **cambios con aprobación registrada** y explicita el costo de oportunidad. |
| Mantener flujos activos sin propósito ni base documentada | Error específico de esta clase | Audita las automatizaciones cada semestre y retira las que no tengan finalidad vigente. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **autoridad de cambio** y **registro de tratamiento** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **revisión periódica** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir autoridad de cambio por tipo de automatización» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **flujos con base legal documentada** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Una gobernanza pesada frena la operación. El nivel de control debe ser proporcional al riesgo: mayor para flujos que tratan datos personales o comprometen a la empresa»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P17-C13-gobernanza-de-automatizaciones/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **flujos con base legal documentada**, **flujos retirados por revisión** y **cambios con aprobación registrada** con fuente, ventana y lectura prohibida.
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

- NIST — *AI Risk Management Framework 1.0* (2023). **Uso en esta clase:** gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022). **Uso en esta clase:** integración de datos, procesos y equipos que producen ingreso como un solo sistema. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- ISO — *ISO 31000: Gestión del riesgo* (2018). **Uso en esta clase:** vocabulario y proceso de gestión de riesgo aplicable a decisiones comerciales. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Cathy O'Neil — *Weapons of Math Destruction* (2016). **Uso en esta clase:** daños de los modelos opacos a escala y necesidad de auditoría. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 12 · Calidad y observabilidad](class-12-calidad-y-observabilidad.md) · [Índice de la parte](README.md) · [Clase 14 · Operating model de RevOps](class-14-operating-model-revops.md) →
