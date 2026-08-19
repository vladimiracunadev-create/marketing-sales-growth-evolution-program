---
title: "Ticket promedio y paquetes"
type: class
language: es
standard: clase-profunda-v1
part: 15
class: 09
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["ramanujam", "flint", "fader", "nagle"]
updated: 2026-08-19
---

# Clase 15.09 — Ticket promedio y paquetes

**Parte 15 · E-commerce y marketplaces** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

## 🎯 Propósito

Aumentar el ticket promedio suele ser más barato que aumentar el tráfico, porque opera sobre personas que ya decidieron comprar. Las palancas son conocidas: paquetes, umbrales de despacho gratis, complementos pertinentes. Su límite también: un paquete que obliga a comprar lo que no se necesita reduce la conversión y aumenta las devoluciones.

Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales. La parte 15 busca **operar una tienda y un canal de marketplace con economía verificable**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **ticket promedio y paquetes** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Dónde se pierde el pedido y cuánto queda después de comisión, envío y devolución?

Los conceptos que estructuran la sesión son **ticket promedio**, **paquete pertinente**, **umbral de beneficio** y **efecto sobre conversión**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `ticket promedio`, `paquete pertinente`, `umbral de beneficio` y `efecto sobre conversión` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **E-commerce y marketplaces**.
3. **Aplicar** la secuencia **analizar qué productos se compran juntos → diseñar paquetes con lógica de uso real → definir umbrales de beneficio con margen verificado → medir efecto conjunto en ticket y en conversión → revisar devoluciones asociadas a los paquetes** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **ticket promedio por segmento**, **efecto en conversión** y **devoluciones de productos en paquete** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **ticket promedio** y **paquete pertinente** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **ticket promedio por segmento**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **ticket promedio** | ingreso del periodo dividido por número de pedidos | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **paquete pertinente** | combinación que el cliente usaría efectivamente en conjunto | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **umbral de beneficio** | monto que activa un incentivo como despacho sin costo | Da un hecho compatible con la definición y otro que la refute. |
| **efecto sobre conversión** | cambio en la tasa de compra provocado por la intervención de ticket | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. analizar qué productos se compran juntos → 2. diseñar paquetes con lógica de uso real → 3. definir umbrales de beneficio con margen verificado → 4. medir efecto conjunto en ticket y en conversión → 5. revisar devoluciones asociadas a los paquetes
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Subir el ticket puede reducir la frecuencia de compra. La evaluación debe considerar el ingreso por cliente en el periodo, no sólo el ticket por pedido.

## 📖 Desarrollo

### 1. Ticket promedio: mecanismo central

**ticket promedio** se entiende aquí como **ingreso del periodo dividido por número de pedidos**. Es la pieza desde la que se inicia el análisis de ticket promedio y paquetes: antes de «analizar qué productos se compran juntos», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016). **Lente que aporta:** diseñar el producto alrededor del precio: disposición a pagar antes de construir. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **ticket promedio por segmento**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **paquete pertinente**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Paquete pertinente: frontera conceptual y error de clasificación

**Definición operacional:** combinación que el cliente usaría efectivamente en conjunto. Su valor está en distinguirlo de **ticket promedio**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) —**lente:** diagnóstico de comportamiento de compra multicanal y migración de clientes—. Formula dos mini-casos: uno que satisface la definición de **paquete pertinente** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **efecto en conversión** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «diseñar paquetes con lógica de uso real», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Umbral de beneficio: operacionalización y medición

**umbral de beneficio** significa **monto que activa un incentivo como despacho sin costo**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **ticket promedio por segmento**: `ingreso, sobre pedidos, por segmento y periodo`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Peter Fader — *Customer Centricity* (2020, 2.ª ed.) orienta este bloque —**lente:** valor heterogéneo del cliente y asignación de recursos por valor esperado—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Efecto sobre conversión: trade-offs y efectos de segundo orden

**Definición:** cambio en la tasa de compra provocado por la intervención de ticket. Este concepto obliga a abandonar la idea de que ticket promedio y paquetes tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «medir efecto conjunto en ticket y en conversión», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) —**lente:** pricing basado en valor, estructura de precios, métrica de cobro y política de descuentos— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **devoluciones de productos en paquete** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **efecto sobre conversión** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar devoluciones asociadas a los paquetes», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) sirve para contrastar la recomendación final desde otro lente: pricing basado en valor, estructura de precios, métrica de cobro y política de descuentos. La frontera de esta clase es explícita: Subir el ticket puede reducir la frecuencia de compra. La evaluación debe considerar el ingreso por cliente en el periodo, no sólo el ticket por pedido. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar ticket promedio y paquetes no consiste en sumar definiciones. Empieza por **ticket promedio**, contrasta **paquete pertinente** con **umbral de beneficio**, incorpora **efecto sobre conversión** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) | diseñar el producto alrededor del precio: disposición a pagar antes de construir | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) | diagnóstico de comportamiento de compra multicanal y migración de clientes | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Peter Fader — *Customer Centricity* (2020, 2.ª ed.) | valor heterogéneo del cliente y asignación de recursos por valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) | pricing basado en valor, estructura de precios, métrica de cobro y política de descuentos | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El umbral de despacho gratis de Ruta Andina es CLP 60.000 y su ticket promedio es CLP 89.000: el incentivo se entrega a casi todos sin cambiar comportamiento.

**Paso 1 — Analizar qué productos se compran juntos.** El equipo escribe primero el supuesto asociado a **ticket promedio** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **ticket promedio por segmento** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Diseñar paquetes con lógica de uso real.** El trabajo aquí es separar lo observado de lo inferido sobre **paquete pertinente**. La evidencia que ordena la discusión es **efecto en conversión**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Definir umbrales de beneficio con margen verificado.** El riesgo de este paso es cerrar demasiado rápido alrededor de **umbral de beneficio**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **devoluciones de productos en paquete** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Medir efecto conjunto en ticket y en conversión.** Con **efecto sobre conversión** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **ticket promedio por segmento** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar devoluciones asociadas a los paquetes.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **ticket promedio**. **efecto en conversión** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **ticket promedio** | Ingreso del periodo dividido por número de pedidos | Cuando **ticket promedio por segmento** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **paquete pertinente** | Combinación que el cliente usaría efectivamente en conjunto | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Subir el ticket puede reducir la frecuencia de compra. La evaluación debe considerar el ingreso por cliente en el periodo, no sólo el ticket por pedido.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre ticket promedio y paquetes |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como E-commerce manager, Marketplace specialist y Emprendedor. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El umbral de despacho gratis de Ruta Andina es CLP 60.000 y su ticket promedio es CLP 89.000: el incentivo se entrega a casi todos sin cambiar comportamiento.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **analizar qué productos se compran juntos → diseñar paquetes con lógica de uso real → definir umbrales de beneficio con margen verificado → medir efecto conjunto en ticket y en conversión → revisar devoluciones asociadas a los paquetes** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **ticket promedio por segmento**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **ticket promedio** y **paquete pertinente** como sinónimos | Se perdió la distinción entre «ingreso del periodo dividido por número de pedidos» y «combinación que el cliente usaría efectivamente en conjunto» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar devoluciones asociadas a los paquetes» | Se saltó «analizar qué productos se compran juntos»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **ticket promedio por segmento** | La métrica local reemplazó al resultado del sistema | Contrástala con **devoluciones de productos en paquete** y explicita el costo de oportunidad. |
| Fijar umbrales de beneficio bajo el ticket promedio | Error específico de esta clase | Ubica el umbral por sobre el ticket actual y verifica el efecto en margen y conversión. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **ticket promedio** y **paquete pertinente** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **umbral de beneficio** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «analizar qué productos se compran juntos» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **ticket promedio por segmento** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Subir el ticket puede reducir la frecuencia de compra. La evaluación debe considerar el ingreso por cliente en el periodo, no sólo el ticket por pedido»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P15-C09-aov-y-bundles/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **ticket promedio por segmento**, **efecto en conversión** y **devoluciones de productos en paquete** con fuente, ventana y lectura prohibida.
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

- Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016). **Uso en esta clase:** diseñar el producto alrededor del precio: disposición a pagar antes de construir. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007). **Uso en esta clase:** diagnóstico de comportamiento de compra multicanal y migración de clientes. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Peter Fader — *Customer Centricity* (2020, 2.ª ed.). **Uso en esta clase:** valor heterogéneo del cliente y asignación de recursos por valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.). **Uso en esta clase:** pricing basado en valor, estructura de precios, métrica de cobro y política de descuentos. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 08 · Abandono de carrito](class-08-abandono-de-carrito.md) · [Índice de la parte](README.md) · [Clase 10 · Venta cruzada y venta incremental](class-10-cross-sell-y-upsell.md) →
