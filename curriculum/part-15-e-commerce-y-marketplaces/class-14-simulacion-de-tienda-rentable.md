---
title: "Simulación de tienda rentable"
type: class
language: es
standard: clase-profunda-v3
part: 15
class: 14
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["croll-yoskovitz", "flint", "provost", "hubbard"]
updated: 2026-08-18
---

# Clase 15.14 — Simulación de tienda rentable

**Parte 15 · E-commerce y marketplaces** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v3`

## 🎯 Propósito

Esta clase integra la parte en una simulación completa: catálogo, precios, costos de cumplimiento, comisiones, devoluciones, conversión y recompra. El resultado no es una tienda bonita sino un modelo económico que muestra bajo qué condiciones el negocio gana dinero y bajo cuáles no. La prueba de calidad es la sensibilidad: qué variable, al moverse 10 %, cambia el resultado de signo.

Esta sesión distingue lo que se sabe, lo que se supone y lo que todavía no se ha medido. La parte 15 busca **operar una tienda y un canal de marketplace con economía verificable**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **simulación de tienda rentable** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Dónde se pierde el pedido y cuánto queda después de comisión, envío y devolución?

Los conceptos que estructuran la sesión son **modelo económico de la tienda**, **análisis de sensibilidad**, **variable crítica** y **escenario de estrés**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `modelo económico de la tienda`, `análisis de sensibilidad`, `variable crítica` y `escenario de estrés` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **E-commerce y marketplaces**.
3. **Aplicar** la secuencia **construir el modelo con supuestos documentados → calcular contribución y punto de equilibrio → ejecutar el análisis de sensibilidad → identificar las variables críticas → definir los controles que vigilarán esas variables** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **contribución total del modelo**, **variables críticas identificadas** y **resultado en escenario de estrés** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **modelo económico de la tienda** y **análisis de sensibilidad** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **contribución total del modelo**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **modelo económico de la tienda** | representación de ingresos, costos y volúmenes con sus supuestos | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **análisis de sensibilidad** | evaluación del efecto de variar cada supuesto sobre el resultado | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **variable crítica** | supuesto cuyo cambio moderado altera la viabilidad del negocio | Da un hecho compatible con la definición y otro que la refute. |
| **escenario de estrés** | combinación adversa de supuestos usada para probar la resistencia del modelo | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. construir el modelo con supuestos documentados → 2. calcular contribución y punto de equilibrio → 3. ejecutar el análisis de sensibilidad → 4. identificar las variables críticas → 5. definir los controles que vigilarán esas variables
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un modelo es tan bueno como sus supuestos. Sin datos reales de conversión, devoluciones y costo logístico, la simulación sólo ordena la ignorancia.

## 📖 Desarrollo

### 1. Modelo económico de la tienda: mecanismo central

**modelo económico de la tienda** se entiende aquí como **representación de ingresos, costos y volúmenes con sus supuestos**. Es la pieza desde la que se inicia el análisis de simulación de tienda rentable: antes de «construir el modelo con supuestos documentados», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013). **Lente que aporta:** una métrica que importa por etapa y por modelo de negocio. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **contribución total del modelo**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **análisis de sensibilidad**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Análisis de sensibilidad: frontera conceptual y error de clasificación

**Definición operacional:** evaluación del efecto de variar cada supuesto sobre el resultado. Su valor está en distinguirlo de **modelo económico de la tienda**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) —**lente:** diagnóstico de comportamiento de compra multicanal y migración de clientes—. Formula dos mini-casos: uno que satisface la definición de **análisis de sensibilidad** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **variables críticas identificadas** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «calcular contribución y punto de equilibrio», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Variable crítica: operacionalización y medición

**variable crítica** significa **supuesto cuyo cambio moderado altera la viabilidad del negocio**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **contribución total del modelo**: `ingreso menos costos variables, proyectado por escenario`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Foster Provost y Tom Fawcett — *Data Science for Business* (2013) orienta este bloque —**lente:** pensamiento analítico: formulación del problema, evaluación y valor esperado—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Escenario de estrés: trade-offs y efectos de segundo orden

**Definición:** combinación adversa de supuestos usada para probar la resistencia del modelo. Este concepto obliga a abandonar la idea de que simulación de tienda rentable tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «identificar las variables críticas», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) —**lente:** medir lo que parece inmedible: valor de la información y reducción de incertidumbre— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **resultado en escenario de estrés** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **escenario de estrés** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «definir los controles que vigilarán esas variables», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) sirve para contrastar la recomendación final desde otro lente: medir lo que parece inmedible: valor de la información y reducción de incertidumbre. La frontera de esta clase es explícita: Un modelo es tan bueno como sus supuestos. Sin datos reales de conversión, devoluciones y costo logístico, la simulación sólo ordena la ignorancia. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar simulación de tienda rentable no consiste en sumar definiciones. Empieza por **modelo económico de la tienda**, contrasta **análisis de sensibilidad** con **variable crítica**, incorpora **escenario de estrés** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | una métrica que importa por etapa y por modelo de negocio | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) | diagnóstico de comportamiento de compra multicanal y migración de clientes | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | pensamiento analítico: formulación del problema, evaluación y valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) | medir lo que parece inmedible: valor de la información y reducción de incertidumbre | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina debe decidir si mantiene, rediseña o cierra su línea de hardware. La decisión requiere un modelo económico con sensibilidad, no una opinión.

**Paso 1 — Construir el modelo con supuestos documentados.** El equipo escribe primero el supuesto asociado a **modelo económico de la tienda** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **contribución total del modelo** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Calcular contribución y punto de equilibrio.** El trabajo aquí es separar lo observado de lo inferido sobre **análisis de sensibilidad**. La evidencia que ordena la discusión es **variables críticas identificadas**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Ejecutar el análisis de sensibilidad.** El riesgo de este paso es cerrar demasiado rápido alrededor de **variable crítica**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **resultado en escenario de estrés** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Identificar las variables críticas.** Con **escenario de estrés** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **contribución total del modelo** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Definir los controles que vigilarán esas variables.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **modelo económico de la tienda**. **variables críticas identificadas** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **modelo económico de la tienda** | Representación de ingresos, costos y volúmenes con sus supuestos | Cuando **contribución total del modelo** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **análisis de sensibilidad** | Evaluación del efecto de variar cada supuesto sobre el resultado | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un modelo es tan bueno como sus supuestos. Sin datos reales de conversión, devoluciones y costo logístico, la simulación sólo ordena la ignorancia.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre simulación de tienda rentable |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como E-commerce manager, Marketplace specialist y Emprendedor. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina debe decidir si mantiene, rediseña o cierra su línea de hardware. La decisión requiere un modelo económico con sensibilidad, no una opinión.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **construir el modelo con supuestos documentados → calcular contribución y punto de equilibrio → ejecutar el análisis de sensibilidad → identificar las variables críticas → definir los controles que vigilarán esas variables** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **contribución total del modelo**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **modelo económico de la tienda** y **análisis de sensibilidad** como sinónimos | Se perdió la distinción entre «representación de ingresos, costos y volúmenes con sus supuestos» y «evaluación del efecto de variar cada supuesto sobre el resultado» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «definir los controles que vigilarán esas variables» | Se saltó «construir el modelo con supuestos documentados»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **contribución total del modelo** | La métrica local reemplazó al resultado del sistema | Contrástala con **resultado en escenario de estrés** y explicita el costo de oportunidad. |
| Presentar el modelo sin análisis de sensibilidad | Error específico de esta clase | Identifica las variables críticas y muestra el resultado bajo escenario adverso. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **modelo económico de la tienda** y **análisis de sensibilidad** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **variable crítica** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «construir el modelo con supuestos documentados» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **contribución total del modelo** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un modelo es tan bueno como sus supuestos. Sin datos reales de conversión, devoluciones y costo logístico, la simulación sólo ordena la ignorancia»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P15-C14-simulacion-de-tienda-rentable/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **contribución total del modelo**, **variables críticas identificadas** y **resultado en escenario de estrés** con fuente, ventana y lectura prohibida.
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

- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013). **Uso en esta clase:** una métrica que importa por etapa y por modelo de negocio. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007). **Uso en esta clase:** diagnóstico de comportamiento de compra multicanal y migración de clientes. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013). **Uso en esta clase:** pensamiento analítico: formulación del problema, evaluación y valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.). **Uso en esta clase:** medir lo que parece inmedible: valor de la información y reducción de incertidumbre. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 13 · Economía del e-commerce](class-13-economia-del-e-commerce.md) · [Índice de la parte](README.md)
