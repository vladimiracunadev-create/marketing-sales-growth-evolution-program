---
title: "Privacidad y propiedad intelectual"
type: class
language: es
standard: clase-profunda-v1
part: 21
class: 13
level: IA y expansión
mastery_threshold: 80
estimated_minutes: 150
sources: ["nist-airmf", "oneil", "iso-31000", "russell-norvig"]
updated: 2026-08-19
---

# Clase 21.13 — Privacidad y propiedad intelectual

**Parte 21 · IA aplicada a marketing, ventas y servicio** · Nivel: IA y expansión · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

## 🎯 Propósito

El uso comercial de IA plantea dos frentes legales. En datos personales, la Ley 21.719 refuerza obligaciones de finalidad, información, seguridad y derechos del titular, incluidos los casos de decisiones automatizadas. En propiedad intelectual, el contenido generado puede reproducir obras protegidas y su titularidad no siempre es clara. Ambos frentes exigen política escrita, no criterio individual.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 21 busca **usar IA como capacidad operativa con evaluación, control y responsabilidad humana**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **privacidad y propiedad intelectual** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué tarea mejora con IA, cómo sé que mejora y quién responde cuando falla?

Los conceptos que estructuran la sesión son **finalidad del tratamiento**, **decisión automatizada**, **titularidad del contenido** y **política de uso**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `finalidad del tratamiento`, `decisión automatizada`, `titularidad del contenido` y `política de uso` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **IA aplicada a marketing, ventas y servicio**.
3. **Aplicar** la secuencia **inventariar qué datos se tratan en cada caso de uso → verificar finalidad, base de licitud e información al titular → definir la política de uso de contenido generado → documentar las decisiones automatizadas y su supervisión → revisar la política cuando cambia la normativa o las herramientas** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **casos de uso con base legal documentada**, **decisiones automatizadas identificadas** y **incidentes de privacidad** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **finalidad del tratamiento** y **decisión automatizada** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **casos de uso con base legal documentada**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **finalidad del tratamiento** | propósito declarado que legitima el uso de los datos personales | Construye un caso límite donde el concepto se confunde con el anterior. |
| **decisión automatizada** | resolución que afecta a una persona tomada sin intervención humana significativa | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **titularidad del contenido** | definición de quién posee derechos sobre lo generado | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **política de uso** | documento que define qué está permitido, qué no y quién autoriza excepciones | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. inventariar qué datos se tratan en cada caso de uso → 2. verificar finalidad, base de licitud e información al titular → 3. definir la política de uso de contenido generado → 4. documentar las decisiones automatizadas y su supervisión → 5. revisar la política cuando cambia la normativa o las herramientas
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** La normativa evoluciona y las herramientas cambian sus condiciones de servicio. La política debe tener fecha de revisión y responsable, no ser un documento único.

## 📖 Desarrollo

### 1. Finalidad del tratamiento: mecanismo central

**finalidad del tratamiento** se entiende aquí como **propósito declarado que legitima el uso de los datos personales**. Es la pieza desde la que se inicia el análisis de privacidad y propiedad intelectual: antes de «inventariar qué datos se tratan en cada caso de uso», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es NIST — *AI Risk Management Framework 1.0* (2023). **Lente que aporta:** gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **casos de uso con base legal documentada**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **decisión automatizada**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Decisión automatizada: frontera conceptual y error de clasificación

**Definición operacional:** resolución que afecta a una persona tomada sin intervención humana significativa. Su valor está en distinguirlo de **finalidad del tratamiento**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Cathy O'Neil — *Weapons of Math Destruction* (2016) —**lente:** daños de los modelos opacos a escala y necesidad de auditoría—. Formula dos mini-casos: uno que satisface la definición de **decisión automatizada** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **decisiones automatizadas identificadas** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «verificar finalidad, base de licitud e información al titular», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Titularidad del contenido: operacionalización y medición

**titularidad del contenido** significa **definición de quién posee derechos sobre lo generado**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **casos de uso con base legal documentada**: `usos con finalidad y base registradas, sobre usos activos`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

ISO — *ISO 31000: Gestión del riesgo* (2018) orienta este bloque —**lente:** vocabulario y proceso de gestión de riesgo aplicable a decisiones comerciales—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Política de uso: trade-offs y efectos de segundo orden

**Definición:** documento que define qué está permitido, qué no y quién autoriza excepciones. Este concepto obliga a abandonar la idea de que privacidad y propiedad intelectual tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «documentar las decisiones automatizadas y su supervisión», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Stuart Russell y Peter Norvig — *Artificial Intelligence: A Modern Approach* (2021, 4.ª ed.) —**lente:** marco formal de agentes, entornos y medidas de desempeño— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **incidentes de privacidad** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **política de uso** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar la política cuando cambia la normativa o las herramientas», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Stuart Russell y Peter Norvig — *Artificial Intelligence: A Modern Approach* (2021, 4.ª ed.) sirve para contrastar la recomendación final desde otro lente: marco formal de agentes, entornos y medidas de desempeño. La frontera de esta clase es explícita: La normativa evoluciona y las herramientas cambian sus condiciones de servicio. La política debe tener fecha de revisión y responsable, no ser un documento único. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar privacidad y propiedad intelectual no consiste en sumar definiciones. Empieza por **finalidad del tratamiento**, contrasta **decisión automatizada** con **titularidad del contenido**, incorpora **política de uso** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| NIST — *AI Risk Management Framework 1.0* (2023) | gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Cathy O'Neil — *Weapons of Math Destruction* (2016) | daños de los modelos opacos a escala y necesidad de auditoría | ¿Qué supuesto de esta clase ayuda a desafiar? |
| ISO — *ISO 31000: Gestión del riesgo* (2018) | vocabulario y proceso de gestión de riesgo aplicable a decisiones comerciales | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Stuart Russell y Peter Norvig — *Artificial Intelligence: A Modern Approach* (2021, 4.ª ed.) | marco formal de agentes, entornos y medidas de desempeño | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina usa un modelo para decidir qué clientes reciben una oferta de retención. Esa decisión automatizada afecta a personas y no está documentada ni supervisada.

**Paso 1 — Inventariar qué datos se tratan en cada caso de uso.** El equipo escribe primero el supuesto asociado a **finalidad del tratamiento** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **casos de uso con base legal documentada** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Verificar finalidad, base de licitud e información al titular.** El trabajo aquí es separar lo observado de lo inferido sobre **decisión automatizada**. La evidencia que ordena la discusión es **decisiones automatizadas identificadas**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Definir la política de uso de contenido generado.** El riesgo de este paso es cerrar demasiado rápido alrededor de **titularidad del contenido**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **incidentes de privacidad** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Documentar las decisiones automatizadas y su supervisión.** Con **política de uso** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **casos de uso con base legal documentada** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar la política cuando cambia la normativa o las herramientas.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **finalidad del tratamiento**. **decisiones automatizadas identificadas** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **finalidad del tratamiento** | Propósito declarado que legitima el uso de los datos personales | Cuando **casos de uso con base legal documentada** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **decisión automatizada** | Resolución que afecta a una persona tomada sin intervención humana significativa | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** La normativa evoluciona y las herramientas cambian sus condiciones de servicio. La política debe tener fecha de revisión y responsable, no ser un documento único.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre privacidad y propiedad intelectual |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager con IA, RevOps, Marketing manager y Sales enablement. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina usa un modelo para decidir qué clientes reciben una oferta de retención. Esa decisión automatizada afecta a personas y no está documentada ni supervisada.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **inventariar qué datos se tratan en cada caso de uso → verificar finalidad, base de licitud e información al titular → definir la política de uso de contenido generado → documentar las decisiones automatizadas y su supervisión → revisar la política cuando cambia la normativa o las herramientas** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **casos de uso con base legal documentada**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **finalidad del tratamiento** y **decisión automatizada** como sinónimos | Se perdió la distinción entre «propósito declarado que legitima el uso de los datos personales» y «resolución que afecta a una persona tomada sin intervención humana significativa» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar la política cuando cambia la normativa o las herramientas» | Se saltó «inventariar qué datos se tratan en cada caso de uso»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **casos de uso con base legal documentada** | La métrica local reemplazó al resultado del sistema | Contrástala con **incidentes de privacidad** y explicita el costo de oportunidad. |
| Operar decisiones automatizadas sin documentación ni supervisión | Error específico de esta clase | Identifica las decisiones automatizadas que afectan a personas y documenta su supervisión humana. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **finalidad del tratamiento** y **decisión automatizada** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **titularidad del contenido** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «inventariar qué datos se tratan en cada caso de uso» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **casos de uso con base legal documentada** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «La normativa evoluciona y las herramientas cambian sus condiciones de servicio. La política debe tener fecha de revisión y responsable, no ser un documento único»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P21-C13-privacidad-y-propiedad-intelectual/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **casos de uso con base legal documentada**, **decisiones automatizadas identificadas** y **incidentes de privacidad** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **operating model humano-IA con casos de uso, evaluaciones, guardrails y registro de incidentes**.

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
- Cathy O'Neil — *Weapons of Math Destruction* (2016). **Uso en esta clase:** daños de los modelos opacos a escala y necesidad de auditoría. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- ISO — *ISO 31000: Gestión del riesgo* (2018). **Uso en esta clase:** vocabulario y proceso de gestión de riesgo aplicable a decisiones comerciales. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Stuart Russell y Peter Norvig — *Artificial Intelligence: A Modern Approach* (2021, 4.ª ed.). **Uso en esta clase:** marco formal de agentes, entornos y medidas de desempeño. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 12 · Evaluación y guardrails](class-12-evaluacion-y-guardrails.md) · [Índice de la parte](README.md) · [Clase 14 · Operating model humano-IA](class-14-operating-model-humano-ia.md) →
