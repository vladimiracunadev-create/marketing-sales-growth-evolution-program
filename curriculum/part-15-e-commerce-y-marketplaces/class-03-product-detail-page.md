---
title: "Página de producto"
type: class
language: es
standard: clase-profunda-v3
part: 15
class: 03
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["krug", "eisenberg", "laja", "dixon-effort"]
updated: 2026-08-18
---

# Clase 15.03 — Página de producto

**Parte 15 · E-commerce y marketplaces** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v3`

## 🎯 Propósito

La página de producto debe responder todo lo que el cliente necesita para decidir sin contactar a nadie: qué es, si sirve para su caso, cuánto cuesta con despacho, cuándo llega, qué pasa si no funciona. En Chile la información al consumidor no es opcional: precio total, condiciones, garantía legal y derecho a retracto cuando corresponde deben estar disponibles antes de la compra.

Antes de cualquier herramienta, esta clase obliga a nombrar qué cambiaría si el análisis fuese correcto. La parte 15 busca **operar una tienda y un canal de marketplace con economía verificable**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **página de producto** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Dónde se pierde el pedido y cuánto queda después de comisión, envío y devolución?

Los conceptos que estructuran la sesión son **información suficiente**, **precio total**, **garantía legal** y **compatibilidad declarada**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `información suficiente`, `precio total`, `garantía legal` y `compatibilidad declarada` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **E-commerce y marketplaces**.
3. **Aplicar** la secuencia **listar las preguntas que llegan a soporte antes de comprar → responderlas en la página → mostrar precio total y plazo de entrega → declarar garantía y condiciones de devolución → medir consultas previas a la compra y reducirlas** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **consultas previas a la compra**, **tasa de conversión de la página** y **devoluciones por información deficiente** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **información suficiente** y **precio total** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **consultas previas a la compra**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **información suficiente** | conjunto de datos que permite decidir sin consultar | Construye un caso límite donde el concepto se confunde con el anterior. |
| **precio total** | monto final incluyendo impuestos y costos de despacho conocidos | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **garantía legal** | derecho del consumidor que existe con independencia de la garantía comercial | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **compatibilidad declarada** | información que permite verificar si el producto sirve para el caso del cliente | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. listar las preguntas que llegan a soporte antes de comprar → 2. responderlas en la página → 3. mostrar precio total y plazo de entrega → 4. declarar garantía y condiciones de devolución → 5. medir consultas previas a la compra y reducirlas
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Demasiada información dificulta la lectura. La solución es jerarquía y secciones desplegables, no omitir datos que la ley exige o que el cliente necesita.

## 📖 Desarrollo

### 1. Información suficiente: mecanismo central

**información suficiente** se entiende aquí como **conjunto de datos que permite decidir sin consultar**. Es la pieza desde la que se inicia el análisis de página de producto: antes de «listar las preguntas que llegan a soporte antes de comprar», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Steve Krug — *Don't Make Me Think, Revisited* (2014). **Lente que aporta:** usabilidad, claridad y pruebas baratas con usuarios reales. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **consultas previas a la compra**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **precio total**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Precio total: frontera conceptual y error de clasificación

**Definición operacional:** monto final incluyendo impuestos y costos de despacho conocidos. Su valor está en distinguirlo de **información suficiente**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Bryan Eisenberg y Jeffrey Eisenberg — *Call to Action* (2005) —**lente:** optimización de conversión con hipótesis, escenarios y persuasión medible—. Formula dos mini-casos: uno que satisface la definición de **precio total** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **tasa de conversión de la página** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «responderlas en la página», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Garantía legal: operacionalización y medición

**garantía legal** significa **derecho del consumidor que existe con independencia de la garantía comercial**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **consultas previas a la compra**: `consultas sobre información que la página debería contener, sobre pedidos`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Peep Laja y el equipo de CXL — *Conversion Optimization Playbooks (CXL)* (2024) orienta este bloque —**lente:** método CRO basado en investigación previa al test y validez estadística—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Compatibilidad declarada: trade-offs y efectos de segundo orden

**Definición:** información que permite verificar si el producto sirve para el caso del cliente. Este concepto obliga a abandonar la idea de que página de producto tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «declarar garantía y condiciones de devolución», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Matthew Dixon, Nick Toman y Rick DeLisi — *The Effortless Experience* (2013) —**lente:** reducción del esfuerzo del cliente como motor de lealtad frente al deleite— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **devoluciones por información deficiente** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **compatibilidad declarada** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «medir consultas previas a la compra y reducirlas», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Matthew Dixon, Nick Toman y Rick DeLisi — *The Effortless Experience* (2013) sirve para contrastar la recomendación final desde otro lente: reducción del esfuerzo del cliente como motor de lealtad frente al deleite. La frontera de esta clase es explícita: Demasiada información dificulta la lectura. La solución es jerarquía y secciones desplegables, no omitir datos que la ley exige o que el cliente necesita. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar página de producto no consiste en sumar definiciones. Empieza por **información suficiente**, contrasta **precio total** con **garantía legal**, incorpora **compatibilidad declarada** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Steve Krug — *Don't Make Me Think, Revisited* (2014) | usabilidad, claridad y pruebas baratas con usuarios reales | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Bryan Eisenberg y Jeffrey Eisenberg — *Call to Action* (2005) | optimización de conversión con hipótesis, escenarios y persuasión medible | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Peep Laja y el equipo de CXL — *Conversion Optimization Playbooks (CXL)* (2024) | método CRO basado en investigación previa al test y validez estadística | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Matthew Dixon, Nick Toman y Rick DeLisi — *The Effortless Experience* (2013) | reducción del esfuerzo del cliente como motor de lealtad frente al deleite | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El lector de tarjetas de Ruta Andina no indica con qué modelos de teléfono es compatible. El 41 % de las devoluciones se debe a incompatibilidad.

**Paso 1 — Listar las preguntas que llegan a soporte antes de comprar.** El equipo escribe primero el supuesto asociado a **información suficiente** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **consultas previas a la compra** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Responderlas en la página.** El trabajo aquí es separar lo observado de lo inferido sobre **precio total**. La evidencia que ordena la discusión es **tasa de conversión de la página**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Mostrar precio total y plazo de entrega.** El riesgo de este paso es cerrar demasiado rápido alrededor de **garantía legal**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **devoluciones por información deficiente** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Declarar garantía y condiciones de devolución.** Con **compatibilidad declarada** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **consultas previas a la compra** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Medir consultas previas a la compra y reducirlas.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **información suficiente**. **tasa de conversión de la página** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **información suficiente** | Conjunto de datos que permite decidir sin consultar | Cuando **consultas previas a la compra** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **precio total** | Monto final incluyendo impuestos y costos de despacho conocidos | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Demasiada información dificulta la lectura. La solución es jerarquía y secciones desplegables, no omitir datos que la ley exige o que el cliente necesita.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre página de producto |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como E-commerce manager, Marketplace specialist y Emprendedor. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El lector de tarjetas de Ruta Andina no indica con qué modelos de teléfono es compatible. El 41 % de las devoluciones se debe a incompatibilidad.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **listar las preguntas que llegan a soporte antes de comprar → responderlas en la página → mostrar precio total y plazo de entrega → declarar garantía y condiciones de devolución → medir consultas previas a la compra y reducirlas** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **consultas previas a la compra**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **información suficiente** y **precio total** como sinónimos | Se perdió la distinción entre «conjunto de datos que permite decidir sin consultar» y «monto final incluyendo impuestos y costos de despacho conocidos» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «medir consultas previas a la compra y reducirlas» | Se saltó «listar las preguntas que llegan a soporte antes de comprar»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **consultas previas a la compra** | La métrica local reemplazó al resultado del sistema | Contrástala con **devoluciones por información deficiente** y explicita el costo de oportunidad. |
| Omitir información de compatibilidad o de costo total | Error específico de esta clase | Publica precio total, plazo de entrega, compatibilidad y condiciones de devolución en la propia página. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **información suficiente** y **precio total** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **garantía legal** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «listar las preguntas que llegan a soporte antes de comprar» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **consultas previas a la compra** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Demasiada información dificulta la lectura. La solución es jerarquía y secciones desplegables, no omitir datos que la ley exige o que el cliente necesita»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P15-C03-product-detail-page/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **consultas previas a la compra**, **tasa de conversión de la página** y **devoluciones por información deficiente** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **simulación de tienda rentable con catálogo, checkout, costos y plan postventa**.

## ✅ Evaluación de la clase

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables entre los conceptos de la clase. |
| Diagnóstico y evidencia | 30 % | Datos pertinentes, línea base, supuestos explícitos y límites del dato. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas y argumento ejecutivo trazable. |

**Aprobación:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambios a otra clase se considera insuficiente.

## 📗 Fuentes y verificación

- Steve Krug — *Don't Make Me Think, Revisited* (2014). **Uso en esta clase:** usabilidad, claridad y pruebas baratas con usuarios reales. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Bryan Eisenberg y Jeffrey Eisenberg — *Call to Action* (2005). **Uso en esta clase:** optimización de conversión con hipótesis, escenarios y persuasión medible. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Peep Laja y el equipo de CXL — *Conversion Optimization Playbooks (CXL)* (2024). **Uso en esta clase:** método CRO basado en investigación previa al test y validez estadística. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Matthew Dixon, Nick Toman y Rick DeLisi — *The Effortless Experience* (2013). **Uso en esta clase:** reducción del esfuerzo del cliente como motor de lealtad frente al deleite. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 02 · Catálogo y merchandising digital](class-02-catalogo-y-merchandising-digital.md) · [Índice de la parte](README.md) · [Clase 04 · Checkout](class-04-checkout.md) →
