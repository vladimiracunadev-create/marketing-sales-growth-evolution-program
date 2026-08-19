---
title: "Conversión y embudos"
type: class
language: es
standard: clase-profunda-v1
part: 20
class: 02
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["kaushik", "croll-yoskovitz", "provost", "wheeler-dv"]
updated: 2026-08-19
---

# Clase 20.02 — Conversión y embudos

**Parte 20 · Analítica comercial y marketing science** · Nivel: Crecimiento y analítica · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

## 🎯 Propósito

Una tasa de conversión sin numerador, denominador y ventana definidos es un número sin significado. La misma etapa puede reportar 12 % o 34 % según se cuente sobre visitas, sesiones o personas únicas. La disciplina de definición operacional es lo que permite comparar entre periodos, entre canales y entre equipos sin discutir de qué se está hablando.

Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales. La parte 20 busca **sostener decisiones de ingreso con métricas correctamente construidas**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **conversión y embudos** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Esta cifra mide lo que creo que mide, y qué decisión cambiaría si estuviera equivocada?

Los conceptos que estructuran la sesión son **definición operacional**, **unidad de análisis**, **ventana de conversión** y **comparabilidad**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `definición operacional`, `unidad de análisis`, `ventana de conversión` y `comparabilidad` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Analítica comercial y marketing science**.
3. **Aplicar** la secuencia **definir la unidad de análisis y justificarla → especificar numerador, denominador y ventana → documentar la fuente de cada componente → verificar la comparabilidad antes de contrastar → publicar las definiciones junto con las cifras** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **conversión con definición documentada**, **diferencia entre unidades de análisis** y **consistencia entre informes** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **definición operacional** y **unidad de análisis** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **conversión con definición documentada**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **definición operacional** | especificación de numerador, denominador, ventana y fuente | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **unidad de análisis** | elección entre visitas, sesiones, personas o cuentas como base del cálculo | Construye un caso límite donde el concepto se confunde con el anterior. |
| **ventana de conversión** | periodo dentro del cual se considera que la conversión ocurrió | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **comparabilidad** | condición que permite contrastar cifras entre periodos o canales | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir la unidad de análisis y justificarla → 2. especificar numerador, denominador y ventana → 3. documentar la fuente de cada componente → 4. verificar la comparabilidad antes de contrastar → 5. publicar las definiciones junto con las cifras
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Las definiciones no pueden cambiarse retroactivamente sin recalcular la serie. Un cambio de definición rompe la comparabilidad histórica y debe declararse.

## 📖 Desarrollo

### 1. Definición operacional: mecanismo central

**definición operacional** se entiende aquí como **especificación de numerador, denominador, ventana y fuente**. Es la pieza desde la que se inicia el análisis de conversión y embudos: antes de «definir la unidad de análisis y justificarla», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Avinash Kaushik — *Web Analytics 2.0* (2009). **Lente que aporta:** medición orientada a decisión, segmentación y crítica del dato de vanidad. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **conversión con definición documentada**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **unidad de análisis**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Unidad de análisis: frontera conceptual y error de clasificación

**Definición operacional:** elección entre visitas, sesiones, personas o cuentas como base del cálculo. Su valor está en distinguirlo de **definición operacional**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) —**lente:** una métrica que importa por etapa y por modelo de negocio—. Formula dos mini-casos: uno que satisface la definición de **unidad de análisis** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **diferencia entre unidades de análisis** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «especificar numerador, denominador y ventana», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Ventana de conversión: operacionalización y medición

**ventana de conversión** significa **periodo dentro del cual se considera que la conversión ocurrió**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **conversión con definición documentada**: `métricas con definición publicada, sobre métricas reportadas`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Foster Provost y Tom Fawcett — *Data Science for Business* (2013) orienta este bloque —**lente:** pensamiento analítico: formulación del problema, evaluación y valor esperado—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Comparabilidad: trade-offs y efectos de segundo orden

**Definición:** condición que permite contrastar cifras entre periodos o canales. Este concepto obliga a abandonar la idea de que conversión y embudos tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «verificar la comparabilidad antes de contrastar», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Donald J. Wheeler — *Understanding Variation* (2000) —**lente:** distinguir variación común de variación especial antes de reaccionar a un KPI— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **consistencia entre informes** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **comparabilidad** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «publicar las definiciones junto con las cifras», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Donald J. Wheeler — *Understanding Variation* (2000) sirve para contrastar la recomendación final desde otro lente: distinguir variación común de variación especial antes de reaccionar a un KPI. La frontera de esta clase es explícita: Las definiciones no pueden cambiarse retroactivamente sin recalcular la serie. Un cambio de definición rompe la comparabilidad histórica y debe declararse. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar conversión y embudos no consiste en sumar definiciones. Empieza por **definición operacional**, contrasta **unidad de análisis** con **ventana de conversión**, incorpora **comparabilidad** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Avinash Kaushik — *Web Analytics 2.0* (2009) | medición orientada a decisión, segmentación y crítica del dato de vanidad | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | una métrica que importa por etapa y por modelo de negocio | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | pensamiento analítico: formulación del problema, evaluación y valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Donald J. Wheeler — *Understanding Variation* (2000) | distinguir variación común de variación especial antes de reaccionar a un KPI | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Marketing reporta 3,2 % de conversión sobre sesiones y ventas calcula 0,9 % sobre personas únicas. Ambos hablan del mismo embudo en la misma reunión.

**Paso 1 — Definir la unidad de análisis y justificarla.** El equipo escribe primero el supuesto asociado a **definición operacional** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **conversión con definición documentada** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Especificar numerador, denominador y ventana.** El trabajo aquí es separar lo observado de lo inferido sobre **unidad de análisis**. La evidencia que ordena la discusión es **diferencia entre unidades de análisis**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Documentar la fuente de cada componente.** El riesgo de este paso es cerrar demasiado rápido alrededor de **ventana de conversión**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **consistencia entre informes** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Verificar la comparabilidad antes de contrastar.** Con **comparabilidad** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **conversión con definición documentada** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Publicar las definiciones junto con las cifras.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **definición operacional**. **diferencia entre unidades de análisis** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **definición operacional** | Especificación de numerador, denominador, ventana y fuente | Cuando **conversión con definición documentada** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **unidad de análisis** | Elección entre visitas, sesiones, personas o cuentas como base del cálculo | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Las definiciones no pueden cambiarse retroactivamente sin recalcular la serie. Un cambio de definición rompe la comparabilidad histórica y debe declararse.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre conversión y embudos |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing analyst, Revenue analyst y Data-driven marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Marketing reporta 3,2 % de conversión sobre sesiones y ventas calcula 0,9 % sobre personas únicas. Ambos hablan del mismo embudo en la misma reunión.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **definir la unidad de análisis y justificarla → especificar numerador, denominador y ventana → documentar la fuente de cada componente → verificar la comparabilidad antes de contrastar → publicar las definiciones junto con las cifras** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **conversión con definición documentada**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **definición operacional** y **unidad de análisis** como sinónimos | Se perdió la distinción entre «especificación de numerador, denominador, ventana y fuente» y «elección entre visitas, sesiones, personas o cuentas como base del cálculo» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «publicar las definiciones junto con las cifras» | Se saltó «definir la unidad de análisis y justificarla»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **conversión con definición documentada** | La métrica local reemplazó al resultado del sistema | Contrástala con **consistencia entre informes** y explicita el costo de oportunidad. |
| Reportar tasas sin unidad de análisis declarada | Error específico de esta clase | Publica numerador, denominador, ventana y fuente junto a cada tasa. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **definición operacional** y **unidad de análisis** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **ventana de conversión** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir la unidad de análisis y justificarla» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **conversión con definición documentada** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Las definiciones no pueden cambiarse retroactivamente sin recalcular la serie. Un cambio de definición rompe la comparabilidad histórica y debe declararse»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P20-C02-conversion-y-funnels/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **conversión con definición documentada**, **diferencia entre unidades de análisis** y **consistencia entre informes** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **caso analítico integral con árbol de métricas, cohortes, incrementalidad y dashboard ejecutivo**.

## ✅ Evaluación de la clase

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables entre los conceptos de la clase. |
| Diagnóstico y evidencia | 30 % | Datos pertinentes, línea base, supuestos explícitos y límites del dato. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas y argumento ejecutivo trazable. |

**Aprobación:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambios a otra clase se considera insuficiente.

## 📗 Fuentes y verificación

- Avinash Kaushik — *Web Analytics 2.0* (2009). **Uso en esta clase:** medición orientada a decisión, segmentación y crítica del dato de vanidad. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013). **Uso en esta clase:** una métrica que importa por etapa y por modelo de negocio. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013). **Uso en esta clase:** pensamiento analítico: formulación del problema, evaluación y valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Donald J. Wheeler — *Understanding Variation* (2000). **Uso en esta clase:** distinguir variación común de variación especial antes de reaccionar a un KPI. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 01 · Árbol de métricas](class-01-arbol-de-metricas.md) · [Índice de la parte](README.md) · [Clase 03 · Costo de adquisición de cliente](class-03-cac.md) →
