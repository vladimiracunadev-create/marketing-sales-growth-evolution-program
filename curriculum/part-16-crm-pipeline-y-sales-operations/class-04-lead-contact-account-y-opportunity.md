---
title: "Lead, contacto, cuenta y oportunidad"
type: class
language: es
standard: clase-profunda-v1
part: 16
class: 04
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["diorio", "roberge", "provost", "ross"]
updated: 2026-08-19
---

# Clase 16.04 — Lead, contacto, cuenta y oportunidad

**Parte 16 · CRM, pipeline y sales operations** · Nivel: Operación de ingresos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

## 🎯 Propósito

El modelo de datos define qué se puede analizar. Confundir un contacto con una cuenta impide ver cuántas oportunidades hay en una misma organización; confundir un lead con una oportunidad infla el pipeline. Las definiciones deben ser explícitas, compartidas entre marketing y ventas, y sostenidas por reglas del sistema y no sólo por acuerdos verbales.

El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta. La parte 16 busca **convertir el CRM en un sistema de trabajo y de verdad operacional**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **lead, contacto, cuenta y oportunidad** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿El pipeline describe la realidad o solo el optimismo del equipo?

Los conceptos que estructuran la sesión son **lead**, **contacto**, **cuenta** y **oportunidad**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `lead`, `contacto`, `cuenta` y `oportunidad` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **CRM, pipeline y sales operations**.
3. **Aplicar** la secuencia **definir cada entidad por escrito y con ejemplos → establecer las reglas de conversión entre entidades → configurar el sistema para impedir duplicaciones → capacitar al equipo con casos límite → auditar la consistencia del modelo cada trimestre** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **duplicados de cuenta**, **oportunidades sin cuenta asociada** y **consistencia de conversión** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **lead** y **contacto** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **duplicados de cuenta**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **lead** | persona o empresa con interés potencial aún no calificada | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **contacto** | persona identificada asociada a una cuenta | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **cuenta** | organización cliente o potencial cliente como entidad única | Da un hecho compatible con la definición y otro que la refute. |
| **oportunidad** | posibilidad de venta calificada con valor, etapa y fecha estimada | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir cada entidad por escrito y con ejemplos → 2. establecer las reglas de conversión entre entidades → 3. configurar el sistema para impedir duplicaciones → 4. capacitar al equipo con casos límite → 5. auditar la consistencia del modelo cada trimestre
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un modelo de datos muy estricto puede no representar estructuras reales como grupos empresariales o franquicias. Debe existir un mecanismo de jerarquía.

## 📖 Desarrollo

### 1. Lead: mecanismo central

**lead** se entiende aquí como **persona o empresa con interés potencial aún no calificada**. Es la pieza desde la que se inicia el análisis de lead, contacto, cuenta y oportunidad: antes de «definir cada entidad por escrito y con ejemplos», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022). **Lente que aporta:** integración de datos, procesos y equipos que producen ingreso como un solo sistema. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **duplicados de cuenta**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **contacto**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Contacto: frontera conceptual y error de clasificación

**Definición operacional:** persona identificada asociada a una cuenta. Su valor está en distinguirlo de **lead**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Mark Roberge — *The Sales Acceleration Formula* (2015) —**lente:** contratación, formación, gestión y demanda comercial gobernadas por datos—. Formula dos mini-casos: uno que satisface la definición de **contacto** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **oportunidades sin cuenta asociada** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «establecer las reglas de conversión entre entidades», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Cuenta: operacionalización y medición

**cuenta** significa **organización cliente o potencial cliente como entidad única**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **duplicados de cuenta**: `cuentas duplicadas detectadas, sobre cuentas totales`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Foster Provost y Tom Fawcett — *Data Science for Business* (2013) orienta este bloque —**lente:** pensamiento analítico: formulación del problema, evaluación y valor esperado—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Oportunidad: trade-offs y efectos de segundo orden

**Definición:** posibilidad de venta calificada con valor, etapa y fecha estimada. Este concepto obliga a abandonar la idea de que lead, contacto, cuenta y oportunidad tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «capacitar al equipo con casos límite», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Aaron Ross y Marylou Tyler — *Predictable Revenue* (2011) —**lente:** especialización de roles comerciales y generación de pipeline predecible— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **consistencia de conversión** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **oportunidad** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «auditar la consistencia del modelo cada trimestre», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Aaron Ross y Marylou Tyler — *Predictable Revenue* (2011) sirve para contrastar la recomendación final desde otro lente: especialización de roles comerciales y generación de pipeline predecible. La frontera de esta clase es explícita: Un modelo de datos muy estricto puede no representar estructuras reales como grupos empresariales o franquicias. Debe existir un mecanismo de jerarquía. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Tomar decisiones de contratación y presupuesto sobre un pipeline que no representa la realidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar lead, contacto, cuenta y oportunidad no consiste en sumar definiciones. Empieza por **lead**, contrasta **contacto** con **cuenta**, incorpora **oportunidad** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) | integración de datos, procesos y equipos que producen ingreso como un solo sistema | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Mark Roberge — *The Sales Acceleration Formula* (2015) | contratación, formación, gestión y demanda comercial gobernadas por datos | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | pensamiento analítico: formulación del problema, evaluación y valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Aaron Ross y Marylou Tyler — *Predictable Revenue* (2011) | especialización de roles comerciales y generación de pipeline predecible | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** La cadena de 14 locales aparece como 14 cuentas distintas en el CRM de Ruta Andina. Nadie puede ver el ingreso total ni el riesgo de concentración.

**Paso 1 — Definir cada entidad por escrito y con ejemplos.** El equipo escribe primero el supuesto asociado a **lead** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **duplicados de cuenta** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Establecer las reglas de conversión entre entidades.** El trabajo aquí es separar lo observado de lo inferido sobre **contacto**. La evidencia que ordena la discusión es **oportunidades sin cuenta asociada**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Configurar el sistema para impedir duplicaciones.** El riesgo de este paso es cerrar demasiado rápido alrededor de **cuenta**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **consistencia de conversión** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Capacitar al equipo con casos límite.** Con **oportunidad** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **duplicados de cuenta** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Auditar la consistencia del modelo cada trimestre.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **lead**. **oportunidades sin cuenta asociada** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **lead** | Persona o empresa con interés potencial aún no calificada | Cuando **duplicados de cuenta** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **contacto** | Persona identificada asociada a una cuenta | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un modelo de datos muy estricto puede no representar estructuras reales como grupos empresariales o franquicias. Debe existir un mecanismo de jerarquía.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre lead, contacto, cuenta y oportunidad |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Sales operations, RevOps analyst y Jefe de ventas. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

La cadena de 14 locales aparece como 14 cuentas distintas en el CRM de Ruta Andina. Nadie puede ver el ingreso total ni el riesgo de concentración.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **definir cada entidad por escrito y con ejemplos → establecer las reglas de conversión entre entidades → configurar el sistema para impedir duplicaciones → capacitar al equipo con casos límite → auditar la consistencia del modelo cada trimestre** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **duplicados de cuenta**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **lead** y **contacto** como sinónimos | Se perdió la distinción entre «persona o empresa con interés potencial aún no calificada» y «persona identificada asociada a una cuenta» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «auditar la consistencia del modelo cada trimestre» | Se saltó «definir cada entidad por escrito y con ejemplos»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **duplicados de cuenta** | La métrica local reemplazó al resultado del sistema | Contrástala con **consistencia de conversión** y explicita el costo de oportunidad. |
| Registrar sucursales como cuentas independientes | Error específico de esta clase | Define la jerarquía de cuentas y consolida las sucursales bajo la organización matriz. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **lead** y **contacto** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **cuenta** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir cada entidad por escrito y con ejemplos» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **duplicados de cuenta** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un modelo de datos muy estricto puede no representar estructuras reales como grupos empresariales o franquicias. Debe existir un mecanismo de jerarquía»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Tomar decisiones de contratación y presupuesto sobre un pipeline que no representa la realidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P16-C04-lead-contact-account-y-opportunity/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **duplicados de cuenta**, **oportunidades sin cuenta asociada** y **consistencia de conversión** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **diseño de sales operations con pipeline, criterios de etapa, forecast y gobierno de datos**.

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
- Mark Roberge — *The Sales Acceleration Formula* (2015). **Uso en esta clase:** contratación, formación, gestión y demanda comercial gobernadas por datos. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013). **Uso en esta clase:** pensamiento analítico: formulación del problema, evaluación y valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Aaron Ross y Marylou Tyler — *Predictable Revenue* (2011). **Uso en esta clase:** especialización de roles comerciales y generación de pipeline predecible. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 03 · Etapas y criterios de salida](class-03-etapas-y-criterios-de-salida.md) · [Índice de la parte](README.md) · [Clase 05 · Higiene de datos](class-05-higiene-de-datos.md) →
