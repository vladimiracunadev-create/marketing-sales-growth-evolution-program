---
title: "Health score"
type: class
language: es
standard: clase-profunda-v3
part: 18
class: 05
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["mehta", "provost", "fader", "croll-yoskovitz"]
updated: 2026-08-18
---

# Clase 18.05 — Health score

**Parte 18 · Customer experience, success y fidelización** · Nivel: Operación de ingresos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v3`

## 🎯 Propósito

Un puntaje de salud estima el riesgo de baja combinando uso, resultado, relación y señales comerciales. Su valor depende de la validación: un puntaje que no predice la baja produce falsa tranquilidad. La construcción correcta parte de analizar qué distinguió a las cuentas que se fueron de las que se quedaron, y no de una ponderación inventada en una reunión.

La clase trata el tema como un problema de evidencia y de consecuencia, no como vocabulario. La parte 18 busca **sostener y expandir el ingreso existente con un sistema de valor entregado**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **health score** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿En qué momento el cliente obtiene valor y qué lo hace quedarse o irse?

Los conceptos que estructuran la sesión son **componente de uso**, **componente de resultado**, **validación predictiva** y **umbral de intervención**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `componente de uso`, `componente de resultado`, `validación predictiva` y `umbral de intervención` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Customer experience, success y fidelización**.
3. **Aplicar** la secuencia **analizar qué distinguió a las cuentas perdidas → construir el puntaje con esos componentes → validar su capacidad predictiva con datos históricos → definir umbrales y acciones asociadas → recalibrar cada semestre con datos nuevos** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **capacidad predictiva del puntaje**, **cobertura de la intervención** y **bajas sin señal previa** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **componente de uso** y **componente de resultado** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **capacidad predictiva del puntaje**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **componente de uso** | señal de actividad en el producto que refleja adopción real | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **componente de resultado** | evidencia de que el cliente logra el beneficio comprometido | Da un hecho compatible con la definición y otro que la refute. |
| **validación predictiva** | contraste entre el puntaje asignado y la baja efectiva | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **umbral de intervención** | nivel de puntaje que activa una acción definida | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. analizar qué distinguió a las cuentas perdidas → 2. construir el puntaje con esos componentes → 3. validar su capacidad predictiva con datos históricos → 4. definir umbrales y acciones asociadas → 5. recalibrar cada semestre con datos nuevos
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un puntaje predictivo sin capacidad de intervención sólo anticipa la pérdida. Debe existir una acción posible para cada nivel de riesgo.

## 📖 Desarrollo

### 1. Componente de uso: mecanismo central

**componente de uso** se entiende aquí como **señal de actividad en el producto que refleja adopción real**. Es la pieza desde la que se inicia el análisis de health score: antes de «analizar qué distinguió a las cuentas perdidas», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016). **Lente que aporta:** disciplina operativa de éxito de cliente: salud, renovación y expansión. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **capacidad predictiva del puntaje**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **componente de resultado**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Componente de resultado: frontera conceptual y error de clasificación

**Definición operacional:** evidencia de que el cliente logra el beneficio comprometido. Su valor está en distinguirlo de **componente de uso**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Foster Provost y Tom Fawcett — *Data Science for Business* (2013) —**lente:** pensamiento analítico: formulación del problema, evaluación y valor esperado—. Formula dos mini-casos: uno que satisface la definición de **componente de resultado** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **cobertura de la intervención** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «construir el puntaje con esos componentes», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Validación predictiva: operacionalización y medición

**validación predictiva** significa **contraste entre el puntaje asignado y la baja efectiva**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **capacidad predictiva del puntaje**: `tasa de baja en el tramo de riesgo alto frente al tramo bajo`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Peter Fader — *Customer Centricity* (2020, 2.ª ed.) orienta este bloque —**lente:** valor heterogéneo del cliente y asignación de recursos por valor esperado—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Umbral de intervención: trade-offs y efectos de segundo orden

**Definición:** nivel de puntaje que activa una acción definida. Este concepto obliga a abandonar la idea de que health score tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «definir umbrales y acciones asociadas», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) —**lente:** una métrica que importa por etapa y por modelo de negocio— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **bajas sin señal previa** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **umbral de intervención** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «recalibrar cada semestre con datos nuevos», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) sirve para contrastar la recomendación final desde otro lente: una métrica que importa por etapa y por modelo de negocio. La frontera de esta clase es explícita: Un puntaje predictivo sin capacidad de intervención sólo anticipa la pérdida. Debe existir una acción posible para cada nivel de riesgo. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Retener con castigos contractuales en lugar de valor entregado y dañar reputación.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar health score no consiste en sumar definiciones. Empieza por **componente de uso**, contrasta **componente de resultado** con **validación predictiva**, incorpora **umbral de intervención** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) | disciplina operativa de éxito de cliente: salud, renovación y expansión | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | pensamiento analítico: formulación del problema, evaluación y valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Peter Fader — *Customer Centricity* (2020, 2.ª ed.) | valor heterogéneo del cliente y asignación de recursos por valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | una métrica que importa por etapa y por modelo de negocio | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El puntaje de salud de Ruta Andina se calcula con la percepción del ejecutivo. El 44 % de las bajas del último trimestre estaba clasificado como saludable.

**Paso 1 — Analizar qué distinguió a las cuentas perdidas.** El equipo escribe primero el supuesto asociado a **componente de uso** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **capacidad predictiva del puntaje** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Construir el puntaje con esos componentes.** El trabajo aquí es separar lo observado de lo inferido sobre **componente de resultado**. La evidencia que ordena la discusión es **cobertura de la intervención**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Validar su capacidad predictiva con datos históricos.** El riesgo de este paso es cerrar demasiado rápido alrededor de **validación predictiva**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **bajas sin señal previa** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Definir umbrales y acciones asociadas.** Con **umbral de intervención** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **capacidad predictiva del puntaje** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Recalibrar cada semestre con datos nuevos.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **componente de uso**. **cobertura de la intervención** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **componente de uso** | Señal de actividad en el producto que refleja adopción real | Cuando **capacidad predictiva del puntaje** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **componente de resultado** | Evidencia de que el cliente logra el beneficio comprometido | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un puntaje predictivo sin capacidad de intervención sólo anticipa la pérdida. Debe existir una acción posible para cada nivel de riesgo.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre health score |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Customer success manager, Account manager y Head of CS. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El puntaje de salud de Ruta Andina se calcula con la percepción del ejecutivo. El 44 % de las bajas del último trimestre estaba clasificado como saludable.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **analizar qué distinguió a las cuentas perdidas → construir el puntaje con esos componentes → validar su capacidad predictiva con datos históricos → definir umbrales y acciones asociadas → recalibrar cada semestre con datos nuevos** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **capacidad predictiva del puntaje**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **componente de uso** y **componente de resultado** como sinónimos | Se perdió la distinción entre «señal de actividad en el producto que refleja adopción real» y «evidencia de que el cliente logra el beneficio comprometido» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «recalibrar cada semestre con datos nuevos» | Se saltó «analizar qué distinguió a las cuentas perdidas»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **capacidad predictiva del puntaje** | La métrica local reemplazó al resultado del sistema | Contrástala con **bajas sin señal previa** y explicita el costo de oportunidad. |
| Construir el puntaje con percepciones del equipo | Error específico de esta clase | Deriva los componentes del análisis de cuentas perdidas y valida su capacidad predictiva. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **componente de uso** y **componente de resultado** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **validación predictiva** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «analizar qué distinguió a las cuentas perdidas» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **capacidad predictiva del puntaje** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un puntaje predictivo sin capacidad de intervención sólo anticipa la pérdida. Debe existir una acción posible para cada nivel de riesgo»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Retener con castigos contractuales en lugar de valor entregado y dañar reputación.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P18-C05-health-score/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **capacidad predictiva del puntaje**, **cobertura de la intervención** y **bajas sin señal previa** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **sistema de retención y expansión con onboarding, health score, renovación y advocacy**.

## ✅ Evaluación de la clase

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables entre los conceptos de la clase. |
| Diagnóstico y evidencia | 30 % | Datos pertinentes, línea base, supuestos explícitos y límites del dato. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas y argumento ejecutivo trazable. |

**Aprobación:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambios a otra clase se considera insuficiente.

## 📗 Fuentes y verificación

- Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016). **Uso en esta clase:** disciplina operativa de éxito de cliente: salud, renovación y expansión. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013). **Uso en esta clase:** pensamiento analítico: formulación del problema, evaluación y valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Peter Fader — *Customer Centricity* (2020, 2.ª ed.). **Uso en esta clase:** valor heterogéneo del cliente y asignación de recursos por valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013). **Uso en esta clase:** una métrica que importa por etapa y por modelo de negocio. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 04 · Customer Success](class-04-customer-success.md) · [Índice de la parte](README.md) · [Clase 06 · NPS, CSAT y CES](class-06-nps-csat-y-ces.md) →
