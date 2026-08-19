---
title: "Pricing basado en valor"
type: class
language: es
standard: clase-profunda-v1
part: 07
class: 04
level: Oferta comercial
mastery_threshold: 80
estimated_minutes: 150
sources: ["nagle", "ramanujam", "simon", "hubbard"]
updated: 2026-08-19
---

# Clase 07.04 — Pricing basado en valor

**Parte 07 · Pricing y monetización** · Nivel: Oferta comercial · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

## 🎯 Propósito

El pricing basado en valor parte del beneficio económico que la oferta produce para un segmento y captura una fracción de él. Requiere tres piezas: una alternativa de referencia clara, el valor diferencial cuantificado en la unidad del cliente y una regla de captura explícita. Nagle advierte que el método no consiste en cobrar todo el valor: dejar excedente al cliente es lo que sostiene la relación y hace defendible el precio.

El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta. La parte 07 busca **diseñar una arquitectura de precios que capture valor sin destruir demanda ni confianza**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **pricing basado en valor** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Cuánto vale esto para quién, y qué estructura de cobro alinea precio con valor entregado?

Los conceptos que estructuran la sesión son **valor de referencia**, **valor diferencial**, **regla de captura** y **excedente para el cliente**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `valor de referencia`, `valor diferencial`, `regla de captura` y `excedente para el cliente` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Pricing y monetización**.
3. **Aplicar** la secuencia **identificar la alternativa de referencia del segmento → cuantificar el valor diferencial en unidades del cliente → verificar la cuantificación con clientes reales → definir la regla de captura y justificarla → probar el precio resultante antes de generalizarlo** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **valor diferencial verificado**, **tasa de aceptación al nuevo precio** y **proporción de valor capturado** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **valor de referencia** y **valor diferencial** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **valor diferencial verificado**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **valor de referencia** | costo de la mejor alternativa disponible para el cliente | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **valor diferencial** | beneficio adicional que la oferta produce frente a esa alternativa, cuantificado | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **regla de captura** | proporción del valor diferencial que la empresa decide cobrar | Da un hecho compatible con la definición y otro que la refute. |
| **excedente para el cliente** | parte del valor diferencial que queda en manos del cliente y sostiene la elección | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. identificar la alternativa de referencia del segmento → 2. cuantificar el valor diferencial en unidades del cliente → 3. verificar la cuantificación con clientes reales → 4. definir la regla de captura y justificarla → 5. probar el precio resultante antes de generalizarlo
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** El valor no es uniforme dentro de un segmento: el mismo cálculo puede sobreestimar el beneficio para clientes con menor volumen. La estimación debe declarar su rango.

## 📖 Desarrollo

### 1. Valor de referencia: mecanismo central

**valor de referencia** se entiende aquí como **costo de la mejor alternativa disponible para el cliente**. Es la pieza desde la que se inicia el análisis de pricing basado en valor: antes de «identificar la alternativa de referencia del segmento», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.). **Lente que aporta:** pricing basado en valor, estructura de precios, métrica de cobro y política de descuentos. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **valor diferencial verificado**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **valor diferencial**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Valor diferencial: frontera conceptual y error de clasificación

**Definición operacional:** beneficio adicional que la oferta produce frente a esa alternativa, cuantificado. Su valor está en distinguirlo de **valor de referencia**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) —**lente:** diseñar el producto alrededor del precio: disposición a pagar antes de construir—. Formula dos mini-casos: uno que satisface la definición de **valor diferencial** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **tasa de aceptación al nuevo precio** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «cuantificar el valor diferencial en unidades del cliente», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Regla de captura: operacionalización y medición

**regla de captura** significa **proporción del valor diferencial que la empresa decide cobrar**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **valor diferencial verificado**: `clientes que confirman la magnitud estimada, sobre clientes consultados`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Hermann Simon — *Confessions of the Pricing Man* (2015) orienta este bloque —**lente:** el precio como la palanca de utilidad más rápida y su relación con el valor percibido—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Excedente para el cliente: trade-offs y efectos de segundo orden

**Definición:** parte del valor diferencial que queda en manos del cliente y sostiene la elección. Este concepto obliga a abandonar la idea de que pricing basado en valor tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «definir la regla de captura y justificarla», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) —**lente:** medir lo que parece inmedible: valor de la información y reducción de incertidumbre— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **proporción de valor capturado** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **excedente para el cliente** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «probar el precio resultante antes de generalizarlo», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) sirve para contrastar la recomendación final desde otro lente: medir lo que parece inmedible: valor de la información y reducción de incertidumbre. La frontera de esta clase es explícita: El valor no es uniforme dentro de un segmento: el mismo cálculo puede sobreestimar el beneficio para clientes con menor volumen. La estimación debe declarar su rango. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar pricing basado en valor no consiste en sumar definiciones. Empieza por **valor de referencia**, contrasta **valor diferencial** con **regla de captura**, incorpora **excedente para el cliente** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) | pricing basado en valor, estructura de precios, métrica de cobro y política de descuentos | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) | diseñar el producto alrededor del precio: disposición a pagar antes de construir | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Hermann Simon — *Confessions of the Pricing Man* (2015) | el precio como la palanca de utilidad más rápida y su relación con el valor percibido | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) | medir lo que parece inmedible: valor de la información y reducción de incertidumbre | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Para un taller que pierde 6 citas semanales a CLP 45.000 cada una, el valor diferencial de reducir inasistencias a la mitad es del orden de CLP 540.000 mensuales. El plan cuesta CLP 79.000.

**Paso 1 — Identificar la alternativa de referencia del segmento.** El equipo escribe primero el supuesto asociado a **valor de referencia** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **valor diferencial verificado** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Cuantificar el valor diferencial en unidades del cliente.** El trabajo aquí es separar lo observado de lo inferido sobre **valor diferencial**. La evidencia que ordena la discusión es **tasa de aceptación al nuevo precio**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Verificar la cuantificación con clientes reales.** El riesgo de este paso es cerrar demasiado rápido alrededor de **regla de captura**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **proporción de valor capturado** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Definir la regla de captura y justificarla.** Con **excedente para el cliente** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **valor diferencial verificado** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Probar el precio resultante antes de generalizarlo.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **valor de referencia**. **tasa de aceptación al nuevo precio** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **valor de referencia** | Costo de la mejor alternativa disponible para el cliente | Cuando **valor diferencial verificado** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **valor diferencial** | Beneficio adicional que la oferta produce frente a esa alternativa, cuantificado | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** El valor no es uniforme dentro de un segmento: el mismo cálculo puede sobreestimar el beneficio para clientes con menor volumen. La estimación debe declarar su rango.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre pricing basado en valor |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Pricing manager, Product marketing, CFO comercial y Founder. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Para un taller que pierde 6 citas semanales a CLP 45.000 cada una, el valor diferencial de reducir inasistencias a la mitad es del orden de CLP 540.000 mensuales. El plan cuesta CLP 79.000.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **identificar la alternativa de referencia del segmento → cuantificar el valor diferencial en unidades del cliente → verificar la cuantificación con clientes reales → definir la regla de captura y justificarla → probar el precio resultante antes de generalizarlo** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **valor diferencial verificado**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **valor de referencia** y **valor diferencial** como sinónimos | Se perdió la distinción entre «costo de la mejor alternativa disponible para el cliente» y «beneficio adicional que la oferta produce frente a esa alternativa, cuantificado» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «probar el precio resultante antes de generalizarlo» | Se saltó «identificar la alternativa de referencia del segmento»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **valor diferencial verificado** | La métrica local reemplazó al resultado del sistema | Contrástala con **proporción de valor capturado** y explicita el costo de oportunidad. |
| Cuantificar el valor sin verificarlo con clientes | Error específico de esta clase | Presenta el cálculo a cinco clientes y ajusta los supuestos que rechacen. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **valor de referencia** y **valor diferencial** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **regla de captura** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «identificar la alternativa de referencia del segmento» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **valor diferencial verificado** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «El valor no es uniforme dentro de un segmento: el mismo cálculo puede sobreestimar el beneficio para clientes con menor volumen. La estimación debe declarar su rango»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P07-C04-value-based-pricing/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **valor diferencial verificado**, **tasa de aceptación al nuevo precio** y **proporción de valor capturado** con fuente, ventana y lectura prohibida.
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
- Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016). **Uso en esta clase:** diseñar el producto alrededor del precio: disposición a pagar antes de construir. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Hermann Simon — *Confessions of the Pricing Man* (2015). **Uso en esta clase:** el precio como la palanca de utilidad más rápida y su relación con el valor percibido. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.). **Uso en esta clase:** medir lo que parece inmedible: valor de la información y reducción de incertidumbre. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 03 · Pricing por competencia](class-03-competitor-based-pricing.md) · [Índice de la parte](README.md) · [Clase 05 · Disposición a pagar](class-05-willingness-to-pay.md) →
