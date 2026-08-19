---
title: "Pagos"
type: class
language: es
standard: clase-profunda-v1
part: 15
class: 05
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["flint", "chaffey", "croll-yoskovitz", "krug"]
updated: 2026-08-19
---

# Clase 15.05 — Pagos

**Parte 15 · E-commerce y marketplaces** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

## 🎯 Propósito

Los medios de pago determinan quién puede comprar y cuánto cuesta cada transacción. En Chile conviven débito, crédito, transferencia y billeteras, con costos y tasas de aprobación distintos. Las decisiones relevantes son tres: qué medios ofrecer según el segmento, cómo manejar los rechazos y cómo prevenir el fraude sin bloquear compras legítimas.

La clase trata el tema como un problema de evidencia y de consecuencia, no como vocabulario. La parte 15 busca **operar una tienda y un canal de marketplace con economía verificable**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **pagos** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Dónde se pierde el pedido y cuánto queda después de comisión, envío y devolución?

Los conceptos que estructuran la sesión son **tasa de aprobación**, **costo de la transacción**, **contracargo** y **falso rechazo**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `tasa de aprobación`, `costo de la transacción`, `contracargo` y `falso rechazo` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **E-commerce y marketplaces**.
3. **Aplicar** la secuencia **identificar los medios que usa el segmento → medir aprobación y costo por medio → analizar las causas de rechazo → calibrar las reglas antifraude con datos de contracargos → revisar la mezcla de medios cada semestre** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **tasa de aprobación por medio**, **costo de pagos sobre ingreso** y **tasa de contracargos** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **tasa de aprobación** y **costo de la transacción** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **tasa de aprobación por medio**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **tasa de aprobación** | transacciones aprobadas sobre transacciones intentadas, por medio de pago | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **costo de la transacción** | comisión y costos asociados a cada medio de pago | Da un hecho compatible con la definición y otro que la refute. |
| **contracargo** | reversión de un pago solicitada por el titular, con su costo asociado | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **falso rechazo** | transacción legítima bloqueada por reglas de prevención de fraude | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. identificar los medios que usa el segmento → 2. medir aprobación y costo por medio → 3. analizar las causas de rechazo → 4. calibrar las reglas antifraude con datos de contracargos → 5. revisar la mezcla de medios cada semestre
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Ampliar medios de pago aumenta el costo de conciliación y de operación. La decisión debe considerar el costo administrativo, no sólo la comisión.

## 📖 Desarrollo

### 1. Tasa de aprobación: mecanismo central

**tasa de aprobación** se entiende aquí como **transacciones aprobadas sobre transacciones intentadas, por medio de pago**. Es la pieza desde la que se inicia el análisis de pagos: antes de «identificar los medios que usa el segmento», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007). **Lente que aporta:** diagnóstico de comportamiento de compra multicanal y migración de clientes. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **tasa de aprobación por medio**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **costo de la transacción**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Costo de la transacción: frontera conceptual y error de clasificación

**Definición operacional:** comisión y costos asociados a cada medio de pago. Su valor está en distinguirlo de **tasa de aprobación**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) —**lente:** planificación digital integrada: canales, medición y gobierno—. Formula dos mini-casos: uno que satisface la definición de **costo de la transacción** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **costo de pagos sobre ingreso** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «medir aprobación y costo por medio», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Contracargo: operacionalización y medición

**contracargo** significa **reversión de un pago solicitada por el titular, con su costo asociado**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **tasa de aprobación por medio**: `transacciones aprobadas, sobre intentadas, por medio de pago`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) orienta este bloque —**lente:** una métrica que importa por etapa y por modelo de negocio—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Falso rechazo: trade-offs y efectos de segundo orden

**Definición:** transacción legítima bloqueada por reglas de prevención de fraude. Este concepto obliga a abandonar la idea de que pagos tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «calibrar las reglas antifraude con datos de contracargos», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Steve Krug — *Don't Make Me Think, Revisited* (2014) —**lente:** usabilidad, claridad y pruebas baratas con usuarios reales— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **tasa de contracargos** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **falso rechazo** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar la mezcla de medios cada semestre», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Steve Krug — *Don't Make Me Think, Revisited* (2014) sirve para contrastar la recomendación final desde otro lente: usabilidad, claridad y pruebas baratas con usuarios reales. La frontera de esta clase es explícita: Ampliar medios de pago aumenta el costo de conciliación y de operación. La decisión debe considerar el costo administrativo, no sólo la comisión. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar pagos no consiste en sumar definiciones. Empieza por **tasa de aprobación**, contrasta **costo de la transacción** con **contracargo**, incorpora **falso rechazo** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) | diagnóstico de comportamiento de compra multicanal y migración de clientes | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) | planificación digital integrada: canales, medición y gobierno | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | una métrica que importa por etapa y por modelo de negocio | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Steve Krug — *Don't Make Me Think, Revisited* (2014) | usabilidad, claridad y pruebas baratas con usuarios reales | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El 22 % de las transacciones de Ruta Andina se rechaza. La causa principal es una regla antifraude que bloquea compras de regiones distintas a la de facturación.

**Paso 1 — Identificar los medios que usa el segmento.** El equipo escribe primero el supuesto asociado a **tasa de aprobación** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **tasa de aprobación por medio** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Medir aprobación y costo por medio.** El trabajo aquí es separar lo observado de lo inferido sobre **costo de la transacción**. La evidencia que ordena la discusión es **costo de pagos sobre ingreso**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Analizar las causas de rechazo.** El riesgo de este paso es cerrar demasiado rápido alrededor de **contracargo**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **tasa de contracargos** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Calibrar las reglas antifraude con datos de contracargos.** Con **falso rechazo** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **tasa de aprobación por medio** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar la mezcla de medios cada semestre.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **tasa de aprobación**. **costo de pagos sobre ingreso** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **tasa de aprobación** | Transacciones aprobadas sobre transacciones intentadas, por medio de pago | Cuando **tasa de aprobación por medio** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **costo de la transacción** | Comisión y costos asociados a cada medio de pago | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Ampliar medios de pago aumenta el costo de conciliación y de operación. La decisión debe considerar el costo administrativo, no sólo la comisión.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre pagos |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como E-commerce manager, Marketplace specialist y Emprendedor. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El 22 % de las transacciones de Ruta Andina se rechaza. La causa principal es una regla antifraude que bloquea compras de regiones distintas a la de facturación.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **identificar los medios que usa el segmento → medir aprobación y costo por medio → analizar las causas de rechazo → calibrar las reglas antifraude con datos de contracargos → revisar la mezcla de medios cada semestre** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **tasa de aprobación por medio**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **tasa de aprobación** y **costo de la transacción** como sinónimos | Se perdió la distinción entre «transacciones aprobadas sobre transacciones intentadas, por medio de pago» y «comisión y costos asociados a cada medio de pago» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar la mezcla de medios cada semestre» | Se saltó «identificar los medios que usa el segmento»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **tasa de aprobación por medio** | La métrica local reemplazó al resultado del sistema | Contrástala con **tasa de contracargos** y explicita el costo de oportunidad. |
| Calibrar reglas antifraude sin medir falsos rechazos | Error específico de esta clase | Compara contracargos evitados contra ventas legítimas bloqueadas antes de endurecer las reglas. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **tasa de aprobación** y **costo de la transacción** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **contracargo** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «identificar los medios que usa el segmento» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **tasa de aprobación por medio** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Ampliar medios de pago aumenta el costo de conciliación y de operación. La decisión debe considerar el costo administrativo, no sólo la comisión»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P15-C05-pagos/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **tasa de aprobación por medio**, **costo de pagos sobre ingreso** y **tasa de contracargos** con fuente, ventana y lectura prohibida.
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
- Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.). **Uso en esta clase:** planificación digital integrada: canales, medición y gobierno. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013). **Uso en esta clase:** una métrica que importa por etapa y por modelo de negocio. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Steve Krug — *Don't Make Me Think, Revisited* (2014). **Uso en esta clase:** usabilidad, claridad y pruebas baratas con usuarios reales. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 04 · Checkout](class-04-checkout.md) · [Índice de la parte](README.md) · [Clase 06 · Fulfillment](class-06-fulfillment.md) →
