---
title: "Packaging y bundling"
type: class
language: es
standard: clase-profunda-v1
part: 05
class: 07
level: Oferta comercial
mastery_threshold: 80
estimated_minutes: 150
sources: ["ramanujam", "nagle", "smith-pricing", "ariely"]
updated: 2026-08-19
---

# Clase 05.07 — Packaging y bundling

**Parte 05 · Producto, oferta y propuesta de valor** · Nivel: Oferta comercial · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

## 🎯 Propósito

Empaquetar es decidir qué va junto y qué se vende por separado. Un buen empaquetado alinea el precio con el valor recibido y facilita la elección; uno malo obliga a pagar por lo que no se usa o fragmenta tanto que nadie entiende qué comprar. Ramanujam propone diseñar los paquetes desde la disposición a pagar por atributo, y no desde la arquitectura técnica del producto.

Esta sesión distingue lo que se sabe, lo que se supone y lo que todavía no se ha medido. La parte 05 busca **convertir una capacidad técnica en una oferta que alguien quiera comprar hoy**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **packaging y bundling** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué compra realmente el cliente y por qué elegiría esta oferta frente a no hacer nada?

Los conceptos que estructuran la sesión son **paquete**, **componente diferenciador**, **componente de volumen** y **canibalización de planes**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `paquete`, `componente diferenciador`, `componente de volumen` y `canibalización de planes` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Producto, oferta y propuesta de valor**.
3. **Aplicar** la secuencia **medir disposición a pagar por atributo → clasificar atributos en diferenciadores, de volumen y opcionales → construir dos o tres paquetes con lógica clara → simular canibalización y margen por escenario → probar la estructura antes de publicarla** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **distribución de ventas por plan**, **tasa de migración entre planes** y **margen por paquete** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **paquete** y **componente diferenciador** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **distribución de ventas por plan**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **paquete** | combinación de componentes ofrecida como unidad con un precio propio | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **componente diferenciador** | atributo con alta disposición a pagar que justifica un plan superior | Construye un caso límite donde el concepto se confunde con el anterior. |
| **componente de volumen** | atributo de bajo valor incremental que conviene incluir en todos los planes | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **canibalización de planes** | traslado de clientes desde un plan superior a uno inferior por diseño del paquete | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. medir disposición a pagar por atributo → 2. clasificar atributos en diferenciadores, de volumen y opcionales → 3. construir dos o tres paquetes con lógica clara → 4. simular canibalización y margen por escenario → 5. probar la estructura antes de publicarla
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Más paquetes no es mejor: la elección excesiva reduce conversión. Tres alternativas claras suelen superar a siete opciones matizadas.

## 📖 Desarrollo

### 1. Paquete: mecanismo central

**paquete** se entiende aquí como **combinación de componentes ofrecida como unidad con un precio propio**. Es la pieza desde la que se inicia el análisis de packaging y bundling: antes de «medir disposición a pagar por atributo», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016). **Lente que aporta:** diseñar el producto alrededor del precio: disposición a pagar antes de construir. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **distribución de ventas por plan**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **componente diferenciador**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Componente diferenciador: frontera conceptual y error de clasificación

**Definición operacional:** atributo con alta disposición a pagar que justifica un plan superior. Su valor está en distinguirlo de **paquete**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) —**lente:** pricing basado en valor, estructura de precios, métrica de cobro y política de descuentos—. Formula dos mini-casos: uno que satisface la definición de **componente diferenciador** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **tasa de migración entre planes** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «clasificar atributos en diferenciadores, de volumen y opcionales», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Componente de volumen: operacionalización y medición

**componente de volumen** significa **atributo de bajo valor incremental que conviene incluir en todos los planes**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **distribución de ventas por plan**: `unidades y margen por plan, sobre ventas totales del periodo`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Tim J. Smith — *Pricing Strategy* (2011) orienta este bloque —**lente:** segmentación de precios, price fences y decisiones de estructura—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Canibalización de planes: trade-offs y efectos de segundo orden

**Definición:** traslado de clientes desde un plan superior a uno inferior por diseño del paquete. Este concepto obliga a abandonar la idea de que packaging y bundling tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «simular canibalización y margen por escenario», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Dan Ariely — *Predictably Irrational* (2008) —**lente:** efectos de anclaje, gratuidad y comparación en la percepción de valor— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **margen por paquete** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **canibalización de planes** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «probar la estructura antes de publicarla», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Dan Ariely — *Predictably Irrational* (2008) sirve para contrastar la recomendación final desde otro lente: efectos de anclaje, gratuidad y comparación en la percepción de valor. La frontera de esta clase es explícita: Más paquetes no es mejor: la elección excesiva reduce conversión. Tres alternativas claras suelen superar a siete opciones matizadas. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Prometer resultados que la operación no puede sostener y generar churn temprano.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar packaging y bundling no consiste en sumar definiciones. Empieza por **paquete**, contrasta **componente diferenciador** con **componente de volumen**, incorpora **canibalización de planes** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) | diseñar el producto alrededor del precio: disposición a pagar antes de construir | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) | pricing basado en valor, estructura de precios, métrica de cobro y política de descuentos | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Tim J. Smith — *Pricing Strategy* (2011) | segmentación de precios, price fences y decisiones de estructura | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Dan Ariely — *Predictably Irrational* (2008) | efectos de anclaje, gratuidad y comparación en la percepción de valor | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina tiene cinco planes y el 78 % de las ventas se concentra en el más barato porque incluye el módulo de pagos, que es el atributo más valorado.

**Paso 1 — Medir disposición a pagar por atributo.** El equipo escribe primero el supuesto asociado a **paquete** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **distribución de ventas por plan** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Clasificar atributos en diferenciadores, de volumen y opcionales.** El trabajo aquí es separar lo observado de lo inferido sobre **componente diferenciador**. La evidencia que ordena la discusión es **tasa de migración entre planes**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Construir dos o tres paquetes con lógica clara.** El riesgo de este paso es cerrar demasiado rápido alrededor de **componente de volumen**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **margen por paquete** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Simular canibalización y margen por escenario.** Con **canibalización de planes** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **distribución de ventas por plan** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Probar la estructura antes de publicarla.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **paquete**. **tasa de migración entre planes** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **paquete** | Combinación de componentes ofrecida como unidad con un precio propio | Cuando **distribución de ventas por plan** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **componente diferenciador** | Atributo con alta disposición a pagar que justifica un plan superior | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Más paquetes no es mejor: la elección excesiva reduce conversión. Tres alternativas claras suelen superar a siete opciones matizadas.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre packaging y bundling |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Product marketing, Product manager y Founder. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina tiene cinco planes y el 78 % de las ventas se concentra en el más barato porque incluye el módulo de pagos, que es el atributo más valorado.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **medir disposición a pagar por atributo → clasificar atributos en diferenciadores, de volumen y opcionales → construir dos o tres paquetes con lógica clara → simular canibalización y margen por escenario → probar la estructura antes de publicarla** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **distribución de ventas por plan**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **paquete** y **componente diferenciador** como sinónimos | Se perdió la distinción entre «combinación de componentes ofrecida como unidad con un precio propio» y «atributo con alta disposición a pagar que justifica un plan superior» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «probar la estructura antes de publicarla» | Se saltó «medir disposición a pagar por atributo»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **distribución de ventas por plan** | La métrica local reemplazó al resultado del sistema | Contrástala con **margen por paquete** y explicita el costo de oportunidad. |
| Diseñar planes desde la arquitectura técnica | Error específico de esta clase | Construye los paquetes desde la disposición a pagar por atributo, medida en el segmento. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **paquete** y **componente diferenciador** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **componente de volumen** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «medir disposición a pagar por atributo» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **distribución de ventas por plan** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Más paquetes no es mejor: la elección excesiva reduce conversión. Tres alternativas claras suelen superar a siete opciones matizadas»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Prometer resultados que la operación no puede sostener y generar churn temprano.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P05-C07-packaging-y-bundling/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **distribución de ventas por plan**, **tasa de migración entre planes** y **margen por paquete** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **oferta lista para vender con propuesta de valor, alcance, garantía y prueba de concepto**.

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
- Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.). **Uso en esta clase:** pricing basado en valor, estructura de precios, métrica de cobro y política de descuentos. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Tim J. Smith — *Pricing Strategy* (2011). **Uso en esta clase:** segmentación de precios, price fences y decisiones de estructura. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Dan Ariely — *Predictably Irrational* (2008). **Uso en esta clase:** efectos de anclaje, gratuidad y comparación en la percepción de valor. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 06 · Diseño de ofertas](class-06-diseno-de-ofertas.md) · [Índice de la parte](README.md) · [Clase 08 · Garantías y reducción de riesgo](class-08-garantias-y-reduccion-de-riesgo.md) →
