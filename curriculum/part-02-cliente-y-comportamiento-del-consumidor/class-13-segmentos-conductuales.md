---
title: "Segmentos conductuales"
type: class
language: es
standard: clase-profunda-v3
part: 02
class: 13
level: Fundamentos
mastery_threshold: 80
estimated_minutes: 150
sources: ["fader", "croll-yoskovitz", "kaushik", "flint"]
updated: 2026-08-18
---

# Clase 02.13 — Segmentos conductuales

**Parte 02 · Cliente y comportamiento del consumidor** · Nivel: Fundamentos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v3`

## 🎯 Propósito

Segmentar por comportamiento observado —frecuencia, recencia, gasto, uso de funcionalidades, canal de origen— suele predecir mejor que segmentar por atributos declarados. La razón es simple: el comportamiento ya ocurrió y está registrado, mientras que la intención declarada es una promesa. La segmentación conductual permite además accionar: se puede construir una lista, medir un efecto y comparar cohortes.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 02 busca **construir un expediente de cliente accionable basado en evidencia y no en estereotipos**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **segmentos conductuales** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Quién decide, quién usa, quién paga y qué progreso intenta lograr cada uno?

Los conceptos que estructuran la sesión son **segmento conductual**, **recencia, frecuencia y valor**, **cohorte** y **accionabilidad del segmento**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `segmento conductual`, `recencia, frecuencia y valor`, `cohorte` y `accionabilidad del segmento` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Cliente y comportamiento del consumidor**.
3. **Aplicar** la secuencia **definir las acciones que se registrarán como señal → construir los segmentos con datos existentes → verificar que cada segmento sea alcanzable y suficientemente grande → diseñar un tratamiento distinto por segmento → medir el efecto diferencial y descartar segmentos sin respuesta** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **tamaño y estabilidad del segmento**, **diferencial de respuesta** y **valor promedio por segmento** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **segmento conductual** y **recencia, frecuencia y valor** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **tamaño y estabilidad del segmento**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **segmento conductual** | grupo definido por acciones registradas y no por características declaradas | Construye un caso límite donde el concepto se confunde con el anterior. |
| **recencia, frecuencia y valor** | tres dimensiones básicas de comportamiento de compra que ordenan la base de clientes | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **cohorte** | conjunto de clientes que comparten el mismo periodo de inicio y que se sigue en el tiempo | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **accionabilidad del segmento** | posibilidad real de alcanzar y tratar de forma distinta a ese grupo | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir las acciones que se registrarán como señal → 2. construir los segmentos con datos existentes → 3. verificar que cada segmento sea alcanzable y suficientemente grande → 4. diseñar un tratamiento distinto por segmento → 5. medir el efecto diferencial y descartar segmentos sin respuesta
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Los segmentos conductuales cambian con el producto: cada cambio relevante de funcionalidad puede invalidar la segmentación y obliga a recalcularla.

## 📖 Desarrollo

### 1. Segmento conductual: mecanismo central

**segmento conductual** se entiende aquí como **grupo definido por acciones registradas y no por características declaradas**. Es la pieza desde la que se inicia el análisis de segmentos conductuales: antes de «definir las acciones que se registrarán como señal», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Peter Fader — *Customer Centricity* (2020, 2.ª ed.). **Lente que aporta:** valor heterogéneo del cliente y asignación de recursos por valor esperado. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **tamaño y estabilidad del segmento**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **recencia, frecuencia y valor**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Recencia, frecuencia y valor: frontera conceptual y error de clasificación

**Definición operacional:** tres dimensiones básicas de comportamiento de compra que ordenan la base de clientes. Su valor está en distinguirlo de **segmento conductual**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) —**lente:** una métrica que importa por etapa y por modelo de negocio—. Formula dos mini-casos: uno que satisface la definición de **recencia, frecuencia y valor** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **diferencial de respuesta** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «construir los segmentos con datos existentes», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Cohorte: operacionalización y medición

**cohorte** significa **conjunto de clientes que comparten el mismo periodo de inicio y que se sigue en el tiempo**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **tamaño y estabilidad del segmento**: `clientes en el segmento y porcentaje que permanece en él entre dos periodos consecutivos`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Avinash Kaushik — *Web Analytics 2.0* (2009) orienta este bloque —**lente:** medición orientada a decisión, segmentación y crítica del dato de vanidad—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Accionabilidad del segmento: trade-offs y efectos de segundo orden

**Definición:** posibilidad real de alcanzar y tratar de forma distinta a ese grupo. Este concepto obliga a abandonar la idea de que segmentos conductuales tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «diseñar un tratamiento distinto por segmento», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) —**lente:** diagnóstico de comportamiento de compra multicanal y migración de clientes— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **valor promedio por segmento** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **accionabilidad del segmento** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «medir el efecto diferencial y descartar segmentos sin respuesta», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) sirve para contrastar la recomendación final desde otro lente: diagnóstico de comportamiento de compra multicanal y migración de clientes. La frontera de esta clase es explícita: Los segmentos conductuales cambian con el producto: cada cambio relevante de funcionalidad puede invalidar la segmentación y obliga a recalcularla. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Construir personas ficticias sin datos y usarlas para justificar decisiones caras.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar segmentos conductuales no consiste en sumar definiciones. Empieza por **segmento conductual**, contrasta **recencia, frecuencia y valor** con **cohorte**, incorpora **accionabilidad del segmento** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Peter Fader — *Customer Centricity* (2020, 2.ª ed.) | valor heterogéneo del cliente y asignación de recursos por valor esperado | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | una métrica que importa por etapa y por modelo de negocio | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Avinash Kaushik — *Web Analytics 2.0* (2009) | medición orientada a decisión, segmentación y crítica del dato de vanidad | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) | diagnóstico de comportamiento de compra multicanal y migración de clientes | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina segmenta por rubro. Al segmentar por uso del módulo de pagos aparece una división más predictiva: quienes lo activan en las dos primeras semanas retienen 3,2 veces más.

**Paso 1 — Definir las acciones que se registrarán como señal.** El equipo escribe primero el supuesto asociado a **segmento conductual** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **tamaño y estabilidad del segmento** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Construir los segmentos con datos existentes.** El trabajo aquí es separar lo observado de lo inferido sobre **recencia, frecuencia y valor**. La evidencia que ordena la discusión es **diferencial de respuesta**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Verificar que cada segmento sea alcanzable y suficientemente grande.** El riesgo de este paso es cerrar demasiado rápido alrededor de **cohorte**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **valor promedio por segmento** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Diseñar un tratamiento distinto por segmento.** Con **accionabilidad del segmento** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **tamaño y estabilidad del segmento** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Medir el efecto diferencial y descartar segmentos sin respuesta.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **segmento conductual**. **diferencial de respuesta** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **segmento conductual** | Grupo definido por acciones registradas y no por características declaradas | Cuando **tamaño y estabilidad del segmento** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **recencia, frecuencia y valor** | Tres dimensiones básicas de comportamiento de compra que ordenan la base de clientes | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Los segmentos conductuales cambian con el producto: cada cambio relevante de funcionalidad puede invalidar la segmentación y obliga a recalcularla.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre segmentos conductuales |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing manager, Product marketing y Ejecutivo comercial. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina segmenta por rubro. Al segmentar por uso del módulo de pagos aparece una división más predictiva: quienes lo activan en las dos primeras semanas retienen 3,2 veces más.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **definir las acciones que se registrarán como señal → construir los segmentos con datos existentes → verificar que cada segmento sea alcanzable y suficientemente grande → diseñar un tratamiento distinto por segmento → medir el efecto diferencial y descartar segmentos sin respuesta** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **tamaño y estabilidad del segmento**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **segmento conductual** y **recencia, frecuencia y valor** como sinónimos | Se perdió la distinción entre «grupo definido por acciones registradas y no por características declaradas» y «tres dimensiones básicas de comportamiento de compra que ordenan la base de clientes» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «medir el efecto diferencial y descartar segmentos sin respuesta» | Se saltó «definir las acciones que se registrarán como señal»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **tamaño y estabilidad del segmento** | La métrica local reemplazó al resultado del sistema | Contrástala con **valor promedio por segmento** y explicita el costo de oportunidad. |
| Crear segmentos que no se pueden alcanzar | Error específico de esta clase | Verifica que exista un canal y un dato de contacto para tratar al segmento de forma distinta. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **segmento conductual** y **recencia, frecuencia y valor** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **cohorte** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir las acciones que se registrarán como señal» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **tamaño y estabilidad del segmento** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Los segmentos conductuales cambian con el producto: cada cambio relevante de funcionalidad puede invalidar la segmentación y obliga a recalcularla»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Construir personas ficticias sin datos y usarlas para justificar decisiones caras.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P02-C13-segmentos-conductuales/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **tamaño y estabilidad del segmento**, **diferencial de respuesta** y **valor promedio por segmento** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **expediente de cliente con ICP, unidad de decisión, journey y fricciones priorizadas**.

## ✅ Evaluación de la clase

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables entre los conceptos de la clase. |
| Diagnóstico y evidencia | 30 % | Datos pertinentes, línea base, supuestos explícitos y límites del dato. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas y argumento ejecutivo trazable. |

**Aprobación:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambios a otra clase se considera insuficiente.

## 📗 Fuentes y verificación

- Peter Fader — *Customer Centricity* (2020, 2.ª ed.). **Uso en esta clase:** valor heterogéneo del cliente y asignación de recursos por valor esperado. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013). **Uso en esta clase:** una métrica que importa por etapa y por modelo de negocio. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Avinash Kaushik — *Web Analytics 2.0* (2009). **Uso en esta clase:** medición orientada a decisión, segmentación y crítica del dato de vanidad. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007). **Uso en esta clase:** diagnóstico de comportamiento de compra multicanal y migración de clientes. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 12 · Contexto cultural y social](class-12-contexto-cultural-y-social.md) · [Índice de la parte](README.md) · [Clase 14 · Síntesis: expediente de cliente accionable](class-14-sintesis-expediente-de-cliente-accionable.md) →
