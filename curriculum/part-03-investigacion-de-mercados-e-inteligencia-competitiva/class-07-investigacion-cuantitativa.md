---
title: "Investigación cuantitativa"
type: class
language: es
standard: clase-profunda-v3
part: 03
class: 07
level: Fundamentos
mastery_threshold: 80
estimated_minutes: 150
sources: ["provost", "kohavi", "malhotra", "wheeler-dv"]
updated: 2026-08-18
---

# Clase 03.07 — Investigación cuantitativa

**Parte 03 · Investigación de mercados e inteligencia competitiva** · Nivel: Fundamentos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v3`

## 🎯 Propósito

La investigación cuantitativa responde preguntas de magnitud y de relación: cuántos, con qué frecuencia, qué tan asociado. Su valor depende de tres cosas que suelen omitirse en informes comerciales: definición operacional de la variable, tamaño de muestra suficiente y declaración de incertidumbre. Un número sin intervalo ni denominador es retórica con apariencia de dato.

Esta sesión distingue lo que se sabe, lo que se supone y lo que todavía no se ha medido. La parte 03 busca **producir investigación que cambie una decisión y resista una auditoría metodológica**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **investigación cuantitativa** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué evidencia mínima necesito para decidir, y qué sesgo podría estar produciéndola?

Los conceptos que estructuran la sesión son **variable operacionalizada**, **tamaño de muestra suficiente**, **incertidumbre declarada** y **asociación frente a causalidad**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `variable operacionalizada`, `tamaño de muestra suficiente`, `incertidumbre declarada` y `asociación frente a causalidad` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Investigación de mercados e inteligencia competitiva**.
3. **Aplicar** la secuencia **definir las variables y su forma de medición → calcular el tamaño de muestra según el efecto mínimo relevante → recolectar con procedimiento uniforme → reportar estimación e incertidumbre → distinguir explícitamente asociación de causalidad** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **potencia del estudio**, **proporción de resultados con intervalo reportado** y **consistencia entre olas** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **variable operacionalizada** y **tamaño de muestra suficiente** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **potencia del estudio**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **variable operacionalizada** | concepto traducido en una medición reproducible con unidad y fuente | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **tamaño de muestra suficiente** | número de observaciones necesario para detectar el efecto que importaría | Construye un caso límite donde el concepto se confunde con el anterior. |
| **incertidumbre declarada** | rango dentro del cual se espera que esté el valor real | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **asociación frente a causalidad** | distinción entre variables que se mueven juntas y variables donde una produce la otra | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir las variables y su forma de medición → 2. calcular el tamaño de muestra según el efecto mínimo relevante → 3. recolectar con procedimiento uniforme → 4. reportar estimación e incertidumbre → 5. distinguir explícitamente asociación de causalidad
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Más muestra no arregla una variable mal definida. Precisión sin validez sólo produce error con más decimales.

## 📖 Desarrollo

### 1. Variable operacionalizada: mecanismo central

**variable operacionalizada** se entiende aquí como **concepto traducido en una medición reproducible con unidad y fuente**. Es la pieza desde la que se inicia el análisis de investigación cuantitativa: antes de «definir las variables y su forma de medición», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Foster Provost y Tom Fawcett — *Data Science for Business* (2013). **Lente que aporta:** pensamiento analítico: formulación del problema, evaluación y valor esperado. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **potencia del estudio**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **tamaño de muestra suficiente**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Tamaño de muestra suficiente: frontera conceptual y error de clasificación

**Definición operacional:** número de observaciones necesario para detectar el efecto que importaría. Su valor está en distinguirlo de **variable operacionalizada**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) —**lente:** diseño estadístico de experimentos, métricas guardrail y trampas de interpretación—. Formula dos mini-casos: uno que satisface la definición de **tamaño de muestra suficiente** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **proporción de resultados con intervalo reportado** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «calcular el tamaño de muestra según el efecto mínimo relevante», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Incertidumbre declarada: operacionalización y medición

**incertidumbre declarada** significa **rango dentro del cual se espera que esté el valor real**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **potencia del estudio**: `probabilidad de detectar el efecto mínimo relevante con la muestra disponible, calculada antes de recolectar`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Naresh K. Malhotra — *Marketing Research: An Applied Orientation* (2019, 7.ª ed.) orienta este bloque —**lente:** diseño de investigación, muestreo, medición y análisis con rigor metodológico—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Asociación frente a causalidad: trade-offs y efectos de segundo orden

**Definición:** distinción entre variables que se mueven juntas y variables donde una produce la otra. Este concepto obliga a abandonar la idea de que investigación cuantitativa tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «reportar estimación e incertidumbre», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Donald J. Wheeler — *Understanding Variation* (2000) —**lente:** distinguir variación común de variación especial antes de reaccionar a un KPI— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **consistencia entre olas** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **asociación frente a causalidad** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «distinguir explícitamente asociación de causalidad», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Donald J. Wheeler — *Understanding Variation* (2000) sirve para contrastar la recomendación final desde otro lente: distinguir variación común de variación especial antes de reaccionar a un KPI. La frontera de esta clase es explícita: Más muestra no arregla una variable mal definida. Precisión sin validez sólo produce error con más decimales. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Investigar para confirmar una decisión ya tomada y presentar el resultado como hallazgo.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar investigación cuantitativa no consiste en sumar definiciones. Empieza por **variable operacionalizada**, contrasta **tamaño de muestra suficiente** con **incertidumbre declarada**, incorpora **asociación frente a causalidad** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | pensamiento analítico: formulación del problema, evaluación y valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | diseño estadístico de experimentos, métricas guardrail y trampas de interpretación | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Naresh K. Malhotra — *Marketing Research: An Applied Orientation* (2019, 7.ª ed.) | diseño de investigación, muestreo, medición y análisis con rigor metodológico | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Donald J. Wheeler — *Understanding Variation* (2000) | distinguir variación común de variación especial antes de reaccionar a un KPI | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El informe de Ruta Andina afirma que «los clientes del sur convierten 15 % más». La diferencia proviene de 11 observaciones y ningún intervalo acompaña la cifra.

**Paso 1 — Definir las variables y su forma de medición.** El equipo escribe primero el supuesto asociado a **variable operacionalizada** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **potencia del estudio** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Calcular el tamaño de muestra según el efecto mínimo relevante.** El trabajo aquí es separar lo observado de lo inferido sobre **tamaño de muestra suficiente**. La evidencia que ordena la discusión es **proporción de resultados con intervalo reportado**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Recolectar con procedimiento uniforme.** El riesgo de este paso es cerrar demasiado rápido alrededor de **incertidumbre declarada**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **consistencia entre olas** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Reportar estimación e incertidumbre.** Con **asociación frente a causalidad** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **potencia del estudio** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Distinguir explícitamente asociación de causalidad.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **variable operacionalizada**. **proporción de resultados con intervalo reportado** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **variable operacionalizada** | Concepto traducido en una medición reproducible con unidad y fuente | Cuando **potencia del estudio** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **tamaño de muestra suficiente** | Número de observaciones necesario para detectar el efecto que importaría | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Más muestra no arregla una variable mal definida. Precisión sin validez sólo produce error con más decimales.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre investigación cuantitativa |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Market researcher, Product marketing y Consultor comercial. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El informe de Ruta Andina afirma que «los clientes del sur convierten 15 % más». La diferencia proviene de 11 observaciones y ningún intervalo acompaña la cifra.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **definir las variables y su forma de medición → calcular el tamaño de muestra según el efecto mínimo relevante → recolectar con procedimiento uniforme → reportar estimación e incertidumbre → distinguir explícitamente asociación de causalidad** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **potencia del estudio**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **variable operacionalizada** y **tamaño de muestra suficiente** como sinónimos | Se perdió la distinción entre «concepto traducido en una medición reproducible con unidad y fuente» y «número de observaciones necesario para detectar el efecto que importaría» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «distinguir explícitamente asociación de causalidad» | Se saltó «definir las variables y su forma de medición»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **potencia del estudio** | La métrica local reemplazó al resultado del sistema | Contrástala con **consistencia entre olas** y explicita el costo de oportunidad. |
| Reportar diferencias sin denominador ni incertidumbre | Error específico de esta clase | Acompaña toda comparación con tamaño de muestra e intervalo, o preséntala como observación exploratoria. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **variable operacionalizada** y **tamaño de muestra suficiente** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **incertidumbre declarada** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir las variables y su forma de medición» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **potencia del estudio** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Más muestra no arregla una variable mal definida. Precisión sin validez sólo produce error con más decimales»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Investigar para confirmar una decisión ya tomada y presentar el resultado como hallazgo.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P03-C07-investigacion-cuantitativa/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **potencia del estudio**, **proporción de resultados con intervalo reportado** y **consistencia entre olas** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **informe de oportunidad de mercado con método, muestra, límites y decisión recomendada**.

## ✅ Evaluación de la clase

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables entre los conceptos de la clase. |
| Diagnóstico y evidencia | 30 % | Datos pertinentes, línea base, supuestos explícitos y límites del dato. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas y argumento ejecutivo trazable. |

**Aprobación:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambios a otra clase se considera insuficiente.

## 📗 Fuentes y verificación

- Foster Provost y Tom Fawcett — *Data Science for Business* (2013). **Uso en esta clase:** pensamiento analítico: formulación del problema, evaluación y valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020). **Uso en esta clase:** diseño estadístico de experimentos, métricas guardrail y trampas de interpretación. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Naresh K. Malhotra — *Marketing Research: An Applied Orientation* (2019, 7.ª ed.). **Uso en esta clase:** diseño de investigación, muestreo, medición y análisis con rigor metodológico. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Donald J. Wheeler — *Understanding Variation* (2000). **Uso en esta clase:** distinguir variación común de variación especial antes de reaccionar a un KPI. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 06 · Investigación cualitativa](class-06-investigacion-cualitativa.md) · [Índice de la parte](README.md) · [Clase 08 · TAM, SAM y SOM](class-08-tam-sam-y-som.md) →
