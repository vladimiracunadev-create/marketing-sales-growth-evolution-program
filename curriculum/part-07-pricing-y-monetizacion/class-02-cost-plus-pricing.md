---
title: "Pricing por costo"
type: class
language: es
standard: clase-profunda-v1
part: 07
class: 02
level: Oferta comercial
mastery_threshold: 80
estimated_minutes: 150
sources: ["nagle", "simon", "smith-pricing", "croll-yoskovitz"]
updated: 2026-08-19
---

# Clase 07.02 — Pricing por costo

**Parte 07 · Pricing y monetización** · Nivel: Oferta comercial · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

## 🎯 Propósito

Fijar precio sumando un margen al costo es simple, defendible internamente y sistemáticamente subóptimo: ignora al cliente y a la competencia. Su único mérito es garantizar que no se venda bajo costo, lo que es necesario pero insuficiente. Además tiene una trampa lógica: el costo unitario depende del volumen, y el volumen depende del precio, por lo que el método razona en círculo. Su lugar correcto es como piso, no como método.

Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales. La parte 07 busca **diseñar una arquitectura de precios que capture valor sin destruir demanda ni confianza**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **pricing por costo** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Cuánto vale esto para quién, y qué estructura de cobro alinea precio con valor entregado?

Los conceptos que estructuran la sesión son **costo variable unitario**, **costo de servir completo**, **margen objetivo** y **circularidad costo-volumen**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `costo variable unitario`, `costo de servir completo`, `margen objetivo` y `circularidad costo-volumen` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Pricing y monetización**.
3. **Aplicar** la secuencia **identificar todos los costos atribuibles al cliente → separar costos fijos de variables → calcular el piso de precio por segmento → contrastar el piso con la disposición a pagar → usar el resultado como restricción y no como decisión** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **costo de servir por segmento**, **proporción de ventas bajo el piso** y **margen de contribución real** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **costo variable unitario** y **costo de servir completo** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **costo de servir por segmento**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **costo variable unitario** | costo que se incurre por cada unidad adicional vendida o servida | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **costo de servir completo** | suma de costos directos, soporte, implementación y comisiones atribuibles al cliente | Construye un caso límite donde el concepto se confunde con el anterior. |
| **margen objetivo** | porcentaje que la empresa decide agregar sobre el costo | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **circularidad costo-volumen** | dependencia mutua entre costo unitario y volumen que invalida el cálculo ingenuo | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. identificar todos los costos atribuibles al cliente → 2. separar costos fijos de variables → 3. calcular el piso de precio por segmento → 4. contrastar el piso con la disposición a pagar → 5. usar el resultado como restricción y no como decisión
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Sin un costeo que incluya implementación y soporte, el piso calculado es ficticio y puede llevar a vender con pérdida creyendo que hay margen.

## 📖 Desarrollo

### 1. Costo variable unitario: mecanismo central

**costo variable unitario** se entiende aquí como **costo que se incurre por cada unidad adicional vendida o servida**. Es la pieza desde la que se inicia el análisis de pricing por costo: antes de «identificar todos los costos atribuibles al cliente», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.). **Lente que aporta:** pricing basado en valor, estructura de precios, métrica de cobro y política de descuentos. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **costo de servir por segmento**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **costo de servir completo**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Costo de servir completo: frontera conceptual y error de clasificación

**Definición operacional:** suma de costos directos, soporte, implementación y comisiones atribuibles al cliente. Su valor está en distinguirlo de **costo variable unitario**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Hermann Simon — *Confessions of the Pricing Man* (2015) —**lente:** el precio como la palanca de utilidad más rápida y su relación con el valor percibido—. Formula dos mini-casos: uno que satisface la definición de **costo de servir completo** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **proporción de ventas bajo el piso** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «separar costos fijos de variables», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Margen objetivo: operacionalización y medición

**margen objetivo** significa **porcentaje que la empresa decide agregar sobre el costo**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **costo de servir por segmento**: `costos directos e indirectos atribuibles, dividido por clientes del segmento`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Tim J. Smith — *Pricing Strategy* (2011) orienta este bloque —**lente:** segmentación de precios, price fences y decisiones de estructura—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Circularidad costo-volumen: trade-offs y efectos de segundo orden

**Definición:** dependencia mutua entre costo unitario y volumen que invalida el cálculo ingenuo. Este concepto obliga a abandonar la idea de que pricing por costo tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «contrastar el piso con la disposición a pagar», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) —**lente:** una métrica que importa por etapa y por modelo de negocio— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **margen de contribución real** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **circularidad costo-volumen** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «usar el resultado como restricción y no como decisión», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) sirve para contrastar la recomendación final desde otro lente: una métrica que importa por etapa y por modelo de negocio. La frontera de esta clase es explícita: Sin un costeo que incluya implementación y soporte, el piso calculado es ficticio y puede llevar a vender con pérdida creyendo que hay margen. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar pricing por costo no consiste en sumar definiciones. Empieza por **costo variable unitario**, contrasta **costo de servir completo** con **margen objetivo**, incorpora **circularidad costo-volumen** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) | pricing basado en valor, estructura de precios, métrica de cobro y política de descuentos | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Hermann Simon — *Confessions of the Pricing Man* (2015) | el precio como la palanca de utilidad más rápida y su relación con el valor percibido | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Tim J. Smith — *Pricing Strategy* (2011) | segmentación de precios, price fences y decisiones de estructura | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | una métrica que importa por etapa y por modelo de negocio | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El plan básico de Ruta Andina se fijó con 40 % de margen sobre costos de infraestructura. Al incluir las 9 horas de migración, el margen real es negativo.

**Paso 1 — Identificar todos los costos atribuibles al cliente.** El equipo escribe primero el supuesto asociado a **costo variable unitario** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **costo de servir por segmento** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Separar costos fijos de variables.** El trabajo aquí es separar lo observado de lo inferido sobre **costo de servir completo**. La evidencia que ordena la discusión es **proporción de ventas bajo el piso**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Calcular el piso de precio por segmento.** El riesgo de este paso es cerrar demasiado rápido alrededor de **margen objetivo**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **margen de contribución real** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Contrastar el piso con la disposición a pagar.** Con **circularidad costo-volumen** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **costo de servir por segmento** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Usar el resultado como restricción y no como decisión.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **costo variable unitario**. **proporción de ventas bajo el piso** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **costo variable unitario** | Costo que se incurre por cada unidad adicional vendida o servida | Cuando **costo de servir por segmento** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **costo de servir completo** | Suma de costos directos, soporte, implementación y comisiones atribuibles al cliente | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Sin un costeo que incluya implementación y soporte, el piso calculado es ficticio y puede llevar a vender con pérdida creyendo que hay margen.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre pricing por costo |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Pricing manager, Product marketing, CFO comercial y Founder. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El plan básico de Ruta Andina se fijó con 40 % de margen sobre costos de infraestructura. Al incluir las 9 horas de migración, el margen real es negativo.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **identificar todos los costos atribuibles al cliente → separar costos fijos de variables → calcular el piso de precio por segmento → contrastar el piso con la disposición a pagar → usar el resultado como restricción y no como decisión** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **costo de servir por segmento**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **costo variable unitario** y **costo de servir completo** como sinónimos | Se perdió la distinción entre «costo que se incurre por cada unidad adicional vendida o servida» y «suma de costos directos, soporte, implementación y comisiones atribuibles al cliente» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «usar el resultado como restricción y no como decisión» | Se saltó «identificar todos los costos atribuibles al cliente»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **costo de servir por segmento** | La métrica local reemplazó al resultado del sistema | Contrástala con **margen de contribución real** y explicita el costo de oportunidad. |
| Calcular el piso sin costo de servir completo | Error específico de esta clase | Incorpora horas de implementación, soporte y comisiones antes de declarar el margen. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **costo variable unitario** y **costo de servir completo** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **margen objetivo** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «identificar todos los costos atribuibles al cliente» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **costo de servir por segmento** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Sin un costeo que incluya implementación y soporte, el piso calculado es ficticio y puede llevar a vender con pérdida creyendo que hay margen»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P07-C02-cost-plus-pricing/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **costo de servir por segmento**, **proporción de ventas bajo el piso** y **margen de contribución real** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **arquitectura de monetización con métrica de cobro, planes, price fences y política de descuentos**.

## ✅ Evaluación de la clase

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables entre los conceptos de la clase. |
| Diagnóstico y evidencia | 30 % | Datos pertinentes, línea base, supuestos explícitos y límites del dato. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas y argumento ejecutivo trazable. |

**Aprobación:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambios a otra clase se considera insuficiente.

## 📗 Fuentes y verificación

- Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.). **Uso en esta clase:** pricing basado en valor, estructura de precios, métrica de cobro y política de descuentos. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Hermann Simon — *Confessions of the Pricing Man* (2015). **Uso en esta clase:** el precio como la palanca de utilidad más rápida y su relación con el valor percibido. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Tim J. Smith — *Pricing Strategy* (2011). **Uso en esta clase:** segmentación de precios, price fences y decisiones de estructura. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013). **Uso en esta clase:** una métrica que importa por etapa y por modelo de negocio. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 01 · El precio como decisión estratégica](class-01-precio-como-decision-estrategica.md) · [Índice de la parte](README.md) · [Clase 03 · Pricing por competencia](class-03-competitor-based-pricing.md) →
