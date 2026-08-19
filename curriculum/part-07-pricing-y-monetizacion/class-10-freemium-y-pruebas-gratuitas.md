---
title: "Freemium y pruebas gratuitas"
type: class
language: es
standard: clase-profunda-v1
part: 07
class: 10
level: Oferta comercial
mastery_threshold: 80
estimated_minutes: 150
sources: ["bush-plg", "croll-yoskovitz", "ramanujam", "ellis-brown"]
updated: 2026-08-19
---

# Clase 07.10 — Freemium y pruebas gratuitas

**Parte 07 · Pricing y monetización** · Nivel: Oferta comercial · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

## 🎯 Propósito

Gratis no es una estrategia: es un costo con la esperanza de una conversión. Freemium funciona cuando el costo marginal de servir al usuario gratuito es bajo, cuando el plan gratuito produce un activo —datos, red, distribución— y cuando existe una razón clara para migrar. La prueba gratuita, en cambio, funciona cuando el valor se percibe rápido. Elegir mal entre ambos modelos produce bases enormes que no convierten y saturan soporte.

Antes de cualquier herramienta, esta clase obliga a nombrar qué cambiaría si el análisis fuese correcto. La parte 07 busca **diseñar una arquitectura de precios que capture valor sin destruir demanda ni confianza**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **freemium y pruebas gratuitas** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Cuánto vale esto para quién, y qué estructura de cobro alinea precio con valor entregado?

Los conceptos que estructuran la sesión son **freemium**, **prueba gratuita**, **costo marginal de servir gratis** y **gatillo de conversión**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `freemium`, `prueba gratuita`, `costo marginal de servir gratis` y `gatillo de conversión` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Pricing y monetización**.
3. **Aplicar** la secuencia **definir el objetivo del modelo gratuito → estimar el costo marginal de servir → diseñar el gatillo de conversión en torno al valor → medir conversión y calidad de la cohorte gratuita → ajustar límites o abandonar el modelo con criterio previo** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **tasa de conversión a pago**, **costo de soporte por usuario gratuito** y **uso del gatillo de conversión** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **freemium** y **prueba gratuita** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **tasa de conversión a pago**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **freemium** | plan gratuito permanente con limitaciones que motivan la migración a un plan pagado | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **prueba gratuita** | acceso completo por tiempo limitado para que el cliente experimente el valor | Da un hecho compatible con la definición y otro que la refute. |
| **costo marginal de servir gratis** | gasto adicional por cada usuario gratuito, incluido soporte | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **gatillo de conversión** | limitación o momento que hace racional pasar al plan pagado | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir el objetivo del modelo gratuito → 2. estimar el costo marginal de servir → 3. diseñar el gatillo de conversión en torno al valor → 4. medir conversión y calidad de la cohorte gratuita → 5. ajustar límites o abandonar el modelo con criterio previo
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un plan gratuito con costo de soporte alto puede destruir la economía del negocio incluso con buena conversión. El costo marginal debe medirse antes de escalar.

## 📖 Desarrollo

### 1. Freemium: mecanismo central

**freemium** se entiende aquí como **plan gratuito permanente con limitaciones que motivan la migración a un plan pagado**. Es la pieza desde la que se inicia el análisis de freemium y pruebas gratuitas: antes de «definir el objetivo del modelo gratuito», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Wes Bush — *Product-Led Growth* (2019). **Lente que aporta:** el producto como principal vehículo de adquisición, activación y expansión. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **tasa de conversión a pago**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **prueba gratuita**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Prueba gratuita: frontera conceptual y error de clasificación

**Definición operacional:** acceso completo por tiempo limitado para que el cliente experimente el valor. Su valor está en distinguirlo de **freemium**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) —**lente:** una métrica que importa por etapa y por modelo de negocio—. Formula dos mini-casos: uno que satisface la definición de **prueba gratuita** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **costo de soporte por usuario gratuito** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «estimar el costo marginal de servir», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Costo marginal de servir gratis: operacionalización y medición

**costo marginal de servir gratis** significa **gasto adicional por cada usuario gratuito, incluido soporte**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **tasa de conversión a pago**: `usuarios que pasan a plan pagado, sobre usuarios gratuitos de la cohorte, a 90 días`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) orienta este bloque —**lente:** diseñar el producto alrededor del precio: disposición a pagar antes de construir—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Gatillo de conversión: trade-offs y efectos de segundo orden

**Definición:** limitación o momento que hace racional pasar al plan pagado. Este concepto obliga a abandonar la idea de que freemium y pruebas gratuitas tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «medir conversión y calidad de la cohorte gratuita», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Sean Ellis y Morgan Brown — *Hacking Growth* (2017) —**lente:** equipo multifuncional, ciclo de experimentación y aha moment— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **uso del gatillo de conversión** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **gatillo de conversión** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «ajustar límites o abandonar el modelo con criterio previo», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Sean Ellis y Morgan Brown — *Hacking Growth* (2017) sirve para contrastar la recomendación final desde otro lente: equipo multifuncional, ciclo de experimentación y aha moment. La frontera de esta clase es explícita: Un plan gratuito con costo de soporte alto puede destruir la economía del negocio incluso con buena conversión. El costo marginal debe medirse antes de escalar. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar freemium y pruebas gratuitas no consiste en sumar definiciones. Empieza por **freemium**, contrasta **prueba gratuita** con **costo marginal de servir gratis**, incorpora **gatillo de conversión** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Wes Bush — *Product-Led Growth* (2019) | el producto como principal vehículo de adquisición, activación y expansión | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | una métrica que importa por etapa y por modelo de negocio | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) | diseñar el producto alrededor del precio: disposición a pagar antes de construir | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Sean Ellis y Morgan Brown — *Hacking Growth* (2017) | equipo multifuncional, ciclo de experimentación y aha moment | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina abrió un plan gratuito sin límites de uso. Tiene 1.900 cuentas gratuitas, 2 % de conversión y el 44 % de los tickets de soporte proviene de ellas.

**Paso 1 — Definir el objetivo del modelo gratuito.** El equipo escribe primero el supuesto asociado a **freemium** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **tasa de conversión a pago** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Estimar el costo marginal de servir.** El trabajo aquí es separar lo observado de lo inferido sobre **prueba gratuita**. La evidencia que ordena la discusión es **costo de soporte por usuario gratuito**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Diseñar el gatillo de conversión en torno al valor.** El riesgo de este paso es cerrar demasiado rápido alrededor de **costo marginal de servir gratis**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **uso del gatillo de conversión** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Medir conversión y calidad de la cohorte gratuita.** Con **gatillo de conversión** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **tasa de conversión a pago** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Ajustar límites o abandonar el modelo con criterio previo.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **freemium**. **costo de soporte por usuario gratuito** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **freemium** | Plan gratuito permanente con limitaciones que motivan la migración a un plan pagado | Cuando **tasa de conversión a pago** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **prueba gratuita** | Acceso completo por tiempo limitado para que el cliente experimente el valor | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un plan gratuito con costo de soporte alto puede destruir la economía del negocio incluso con buena conversión. El costo marginal debe medirse antes de escalar.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre freemium y pruebas gratuitas |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Pricing manager, Product marketing, CFO comercial y Founder. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina abrió un plan gratuito sin límites de uso. Tiene 1.900 cuentas gratuitas, 2 % de conversión y el 44 % de los tickets de soporte proviene de ellas.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **definir el objetivo del modelo gratuito → estimar el costo marginal de servir → diseñar el gatillo de conversión en torno al valor → medir conversión y calidad de la cohorte gratuita → ajustar límites o abandonar el modelo con criterio previo** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **tasa de conversión a pago**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **freemium** y **prueba gratuita** como sinónimos | Se perdió la distinción entre «plan gratuito permanente con limitaciones que motivan la migración a un plan pagado» y «acceso completo por tiempo limitado para que el cliente experimente el valor» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «ajustar límites o abandonar el modelo con criterio previo» | Se saltó «definir el objetivo del modelo gratuito»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **tasa de conversión a pago** | La métrica local reemplazó al resultado del sistema | Contrástala con **uso del gatillo de conversión** y explicita el costo de oportunidad. |
| Abrir plan gratuito sin límite ni gatillo | Error específico de esta clase | Define el límite que activa la conversión y mide el costo marginal de servir antes de escalar. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **freemium** y **prueba gratuita** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **costo marginal de servir gratis** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir el objetivo del modelo gratuito» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **tasa de conversión a pago** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un plan gratuito con costo de soporte alto puede destruir la economía del negocio incluso con buena conversión. El costo marginal debe medirse antes de escalar»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P07-C10-freemium-y-pruebas-gratuitas/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **tasa de conversión a pago**, **costo de soporte por usuario gratuito** y **uso del gatillo de conversión** con fuente, ventana y lectura prohibida.
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

- Wes Bush — *Product-Led Growth* (2019). **Uso en esta clase:** el producto como principal vehículo de adquisición, activación y expansión. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013). **Uso en esta clase:** una métrica que importa por etapa y por modelo de negocio. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016). **Uso en esta clase:** diseñar el producto alrededor del precio: disposición a pagar antes de construir. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Sean Ellis y Morgan Brown — *Hacking Growth* (2017). **Uso en esta clase:** equipo multifuncional, ciclo de experimentación y aha moment. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 09 · Suscripción e ingreso recurrente](class-09-suscripcion-y-recurring-revenue.md) · [Índice de la parte](README.md) · [Clase 11 · Descuentos sin destruir valor](class-11-descuentos-sin-destruir-valor.md) →
