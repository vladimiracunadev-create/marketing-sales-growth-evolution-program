---
title: "Modelo operativo de e-commerce"
type: class
language: es
standard: clase-profunda-v3
part: 15
class: 01
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["flint", "croll-yoskovitz", "chaffey", "fader"]
updated: 2026-08-18
---

# Clase 15.01 — Modelo operativo de e-commerce

**Parte 15 · E-commerce y marketplaces** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v3`

## 🎯 Propósito

Vender en línea es una operación logística y financiera antes que una vitrina. El modelo operativo define quién almacena, quién despacha, quién cobra, quién responde por una devolución y cuánto cuesta cada uno de esos pasos. La mayoría de los emprendimientos digitales que fracasan no tenía un problema de tráfico: tenía un costo por pedido superior a su margen y no lo sabía.

El punto de partida de esta clase no es la definición sino la decisión que la definición debe mejorar. La parte 15 busca **operar una tienda y un canal de marketplace con economía verificable**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **modelo operativo de e-commerce** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Dónde se pierde el pedido y cuánto queda después de comisión, envío y devolución?

Los conceptos que estructuran la sesión son **costo por pedido**, **modelo de cumplimiento**, **margen por pedido** y **punto de equilibrio operativo**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `costo por pedido`, `modelo de cumplimiento`, `margen por pedido` y `punto de equilibrio operativo` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **E-commerce y marketplaces**.
3. **Aplicar** la secuencia **mapear el flujo completo desde el pedido hasta la entrega → costear cada paso con datos reales → calcular el margen por pedido y por categoría → identificar el punto de equilibrio operativo → decidir qué pasos internalizar o externalizar** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **margen por pedido**, **costo logístico sobre ingreso** y **pedidos bajo el punto de equilibrio** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **costo por pedido** y **modelo de cumplimiento** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **margen por pedido**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **costo por pedido** | suma de costos de producto, empaque, despacho, pasarela y atención por cada pedido | Da un hecho compatible con la definición y otro que la refute. |
| **modelo de cumplimiento** | forma en que se almacena, prepara y entrega el producto | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **margen por pedido** | ingreso del pedido menos todos los costos variables asociados | Construye un caso límite donde el concepto se confunde con el anterior. |
| **punto de equilibrio operativo** | volumen a partir del cual la operación cubre sus costos fijos | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. mapear el flujo completo desde el pedido hasta la entrega → 2. costear cada paso con datos reales → 3. calcular el margen por pedido y por categoría → 4. identificar el punto de equilibrio operativo → 5. decidir qué pasos internalizar o externalizar
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** El costo por pedido varía con el volumen y con la mezcla de productos. Un cálculo promedio esconde categorías que pierden dinero en cada venta.

## 📖 Desarrollo

### 1. Costo por pedido: mecanismo central

**costo por pedido** se entiende aquí como **suma de costos de producto, empaque, despacho, pasarela y atención por cada pedido**. Es la pieza desde la que se inicia el análisis de modelo operativo de e-commerce: antes de «mapear el flujo completo desde el pedido hasta la entrega», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007). **Lente que aporta:** diagnóstico de comportamiento de compra multicanal y migración de clientes. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **margen por pedido**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **modelo de cumplimiento**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Modelo de cumplimiento: frontera conceptual y error de clasificación

**Definición operacional:** forma en que se almacena, prepara y entrega el producto. Su valor está en distinguirlo de **costo por pedido**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) —**lente:** una métrica que importa por etapa y por modelo de negocio—. Formula dos mini-casos: uno que satisface la definición de **modelo de cumplimiento** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **costo logístico sobre ingreso** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «costear cada paso con datos reales», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Margen por pedido: operacionalización y medición

**margen por pedido** significa **ingreso del pedido menos todos los costos variables asociados**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **margen por pedido**: `ingreso menos costos variables, dividido por ingreso, por categoría`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) orienta este bloque —**lente:** planificación digital integrada: canales, medición y gobierno—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Punto de equilibrio operativo: trade-offs y efectos de segundo orden

**Definición:** volumen a partir del cual la operación cubre sus costos fijos. Este concepto obliga a abandonar la idea de que modelo operativo de e-commerce tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «identificar el punto de equilibrio operativo», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Peter Fader — *Customer Centricity* (2020, 2.ª ed.) —**lente:** valor heterogéneo del cliente y asignación de recursos por valor esperado— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **pedidos bajo el punto de equilibrio** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **punto de equilibrio operativo** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «decidir qué pasos internalizar o externalizar», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Peter Fader — *Customer Centricity* (2020, 2.ª ed.) sirve para contrastar la recomendación final desde otro lente: valor heterogéneo del cliente y asignación de recursos por valor esperado. La frontera de esta clase es explícita: El costo por pedido varía con el volumen y con la mezcla de productos. Un cálculo promedio esconde categorías que pierden dinero en cada venta. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar modelo operativo de e-commerce no consiste en sumar definiciones. Empieza por **costo por pedido**, contrasta **modelo de cumplimiento** con **margen por pedido**, incorpora **punto de equilibrio operativo** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) | diagnóstico de comportamiento de compra multicanal y migración de clientes | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | una métrica que importa por etapa y por modelo de negocio | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) | planificación digital integrada: canales, medición y gobierno | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Peter Fader — *Customer Centricity* (2020, 2.ª ed.) | valor heterogéneo del cliente y asignación de recursos por valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** La línea de hardware de Ruta Andina vende bien y pierde dinero: 16 % de comisión de marketplace, despacho subsidiado y 9 % de devoluciones que nadie costeó.

**Paso 1 — Mapear el flujo completo desde el pedido hasta la entrega.** El equipo escribe primero el supuesto asociado a **costo por pedido** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **margen por pedido** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Costear cada paso con datos reales.** El trabajo aquí es separar lo observado de lo inferido sobre **modelo de cumplimiento**. La evidencia que ordena la discusión es **costo logístico sobre ingreso**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Calcular el margen por pedido y por categoría.** El riesgo de este paso es cerrar demasiado rápido alrededor de **margen por pedido**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **pedidos bajo el punto de equilibrio** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Identificar el punto de equilibrio operativo.** Con **punto de equilibrio operativo** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **margen por pedido** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Decidir qué pasos internalizar o externalizar.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **costo por pedido**. **costo logístico sobre ingreso** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **costo por pedido** | Suma de costos de producto, empaque, despacho, pasarela y atención por cada pedido | Cuando **margen por pedido** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **modelo de cumplimiento** | Forma en que se almacena, prepara y entrega el producto | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** El costo por pedido varía con el volumen y con la mezcla de productos. Un cálculo promedio esconde categorías que pierden dinero en cada venta.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre modelo operativo de e-commerce |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como E-commerce manager, Marketplace specialist y Emprendedor. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

La línea de hardware de Ruta Andina vende bien y pierde dinero: 16 % de comisión de marketplace, despacho subsidiado y 9 % de devoluciones que nadie costeó.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **mapear el flujo completo desde el pedido hasta la entrega → costear cada paso con datos reales → calcular el margen por pedido y por categoría → identificar el punto de equilibrio operativo → decidir qué pasos internalizar o externalizar** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **margen por pedido**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **costo por pedido** y **modelo de cumplimiento** como sinónimos | Se perdió la distinción entre «suma de costos de producto, empaque, despacho, pasarela y atención por cada pedido» y «forma en que se almacena, prepara y entrega el producto» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «decidir qué pasos internalizar o externalizar» | Se saltó «mapear el flujo completo desde el pedido hasta la entrega»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **margen por pedido** | La métrica local reemplazó al resultado del sistema | Contrástala con **pedidos bajo el punto de equilibrio** y explicita el costo de oportunidad. |
| Evaluar el canal por ingreso y no por margen por pedido | Error específico de esta clase | Costea despacho, comisión y devoluciones antes de declarar rentable una categoría. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **costo por pedido** y **modelo de cumplimiento** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **margen por pedido** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «mapear el flujo completo desde el pedido hasta la entrega» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **margen por pedido** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «El costo por pedido varía con el volumen y con la mezcla de productos. Un cálculo promedio esconde categorías que pierden dinero en cada venta»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P15-C01-modelo-operativo-e-commerce/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **margen por pedido**, **costo logístico sobre ingreso** y **pedidos bajo el punto de equilibrio** con fuente, ventana y lectura prohibida.
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

- Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007). **Uso en esta clase:** diagnóstico de comportamiento de compra multicanal y migración de clientes. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013). **Uso en esta clase:** una métrica que importa por etapa y por modelo de negocio. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.). **Uso en esta clase:** planificación digital integrada: canales, medición y gobierno. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Peter Fader — *Customer Centricity* (2020, 2.ª ed.). **Uso en esta clase:** valor heterogéneo del cliente y asignación de recursos por valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

[Índice de la parte](README.md) · [Clase 02 · Catálogo y merchandising digital](class-02-catalogo-y-merchandising-digital.md) →
