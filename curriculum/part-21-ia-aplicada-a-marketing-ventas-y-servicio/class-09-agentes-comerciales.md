---
title: "Agentes comerciales automatizados"
type: class
language: es
standard: clase-profunda-v1
part: 21
class: 09
level: IA y expansión
mastery_threshold: 80
estimated_minutes: 150
sources: ["russell-norvig", "nist-airmf", "iso-31000", "oneil"]
updated: 2026-08-19
---

# Clase 21.09 — Agentes comerciales automatizados

**Parte 21 · IA aplicada a marketing, ventas y servicio** · Nivel: IA y expansión · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

## 🎯 Propósito

Un agente no sólo genera texto: ejecuta acciones —enviar correos, actualizar registros, agendar—. Eso cambia el perfil de riesgo: un error ya no produce un borrador malo sino una acción real sobre un cliente real. Su diseño exige límites explícitos de autoridad, registro de acciones, capacidad de detención inmediata y responsable identificado.

Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales. La parte 21 busca **usar IA como capacidad operativa con evaluación, control y responsabilidad humana**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **agentes comerciales automatizados** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué tarea mejora con IA, cómo sé que mejora y quién responde cuando falla?

Los conceptos que estructuran la sesión son **autoridad del agente**, **registro de acciones**, **mecanismo de detención** y **acción irreversible**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `autoridad del agente`, `registro de acciones`, `mecanismo de detención` y `acción irreversible` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **IA aplicada a marketing, ventas y servicio**.
3. **Aplicar** la secuencia **definir la autoridad del agente por tipo de acción → excluir las acciones irreversibles de la autonomía → instrumentar el registro completo de acciones → habilitar la detención inmediata y probarla → revisar el registro periódicamente con responsable** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **acciones ejecutadas por el agente**, **acciones revertidas** y **tiempo de detención** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **autoridad del agente** y **registro de acciones** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **acciones ejecutadas por el agente**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **autoridad del agente** | conjunto de acciones que el sistema puede ejecutar sin aprobación humana | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **registro de acciones** | traza completa de qué hizo el sistema, cuándo y sobre qué registro | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **mecanismo de detención** | capacidad de interrumpir la operación del agente de inmediato | Da un hecho compatible con la definición y otro que la refute. |
| **acción irreversible** | operación cuyo efecto no puede deshacerse, como enviar una comunicación | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir la autoridad del agente por tipo de acción → 2. excluir las acciones irreversibles de la autonomía → 3. instrumentar el registro completo de acciones → 4. habilitar la detención inmediata y probarla → 5. revisar el registro periódicamente con responsable
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** La responsabilidad legal y comercial siempre recae en la empresa, no en el sistema. La automatización no traslada la responsabilidad a nadie más.

## 📖 Desarrollo

### 1. Autoridad del agente: mecanismo central

**autoridad del agente** se entiende aquí como **conjunto de acciones que el sistema puede ejecutar sin aprobación humana**. Es la pieza desde la que se inicia el análisis de agentes comerciales automatizados: antes de «definir la autoridad del agente por tipo de acción», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Stuart Russell y Peter Norvig — *Artificial Intelligence: A Modern Approach* (2021, 4.ª ed.). **Lente que aporta:** marco formal de agentes, entornos y medidas de desempeño. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **acciones ejecutadas por el agente**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **registro de acciones**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Registro de acciones: frontera conceptual y error de clasificación

**Definición operacional:** traza completa de qué hizo el sistema, cuándo y sobre qué registro. Su valor está en distinguirlo de **autoridad del agente**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con NIST — *AI Risk Management Framework 1.0* (2023) —**lente:** gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar—. Formula dos mini-casos: uno que satisface la definición de **registro de acciones** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **acciones revertidas** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «excluir las acciones irreversibles de la autonomía», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Mecanismo de detención: operacionalización y medición

**mecanismo de detención** significa **capacidad de interrumpir la operación del agente de inmediato**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **acciones ejecutadas por el agente**: `operaciones automáticas realizadas, por tipo y periodo`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

ISO — *ISO 31000: Gestión del riesgo* (2018) orienta este bloque —**lente:** vocabulario y proceso de gestión de riesgo aplicable a decisiones comerciales—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Acción irreversible: trade-offs y efectos de segundo orden

**Definición:** operación cuyo efecto no puede deshacerse, como enviar una comunicación. Este concepto obliga a abandonar la idea de que agentes comerciales automatizados tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «habilitar la detención inmediata y probarla», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Cathy O'Neil — *Weapons of Math Destruction* (2016) —**lente:** daños de los modelos opacos a escala y necesidad de auditoría— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **tiempo de detención** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **acción irreversible** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar el registro periódicamente con responsable», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Cathy O'Neil — *Weapons of Math Destruction* (2016) sirve para contrastar la recomendación final desde otro lente: daños de los modelos opacos a escala y necesidad de auditoría. La frontera de esta clase es explícita: La responsabilidad legal y comercial siempre recae en la empresa, no en el sistema. La automatización no traslada la responsabilidad a nadie más. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar agentes comerciales automatizados no consiste en sumar definiciones. Empieza por **autoridad del agente**, contrasta **registro de acciones** con **mecanismo de detención**, incorpora **acción irreversible** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Stuart Russell y Peter Norvig — *Artificial Intelligence: A Modern Approach* (2021, 4.ª ed.) | marco formal de agentes, entornos y medidas de desempeño | ¿Qué supuesto de esta clase ayuda a desafiar? |
| NIST — *AI Risk Management Framework 1.0* (2023) | gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar | ¿Qué supuesto de esta clase ayuda a desafiar? |
| ISO — *ISO 31000: Gestión del riesgo* (2018) | vocabulario y proceso de gestión de riesgo aplicable a decisiones comerciales | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Cathy O'Neil — *Weapons of Math Destruction* (2016) | daños de los modelos opacos a escala y necesidad de auditoría | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Un agente de Ruta Andina envió 400 correos de reactivación a clientes que habían solicitado no ser contactados, porque la regla de exclusión no estaba implementada.

**Paso 1 — Definir la autoridad del agente por tipo de acción.** El equipo escribe primero el supuesto asociado a **autoridad del agente** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **acciones ejecutadas por el agente** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Excluir las acciones irreversibles de la autonomía.** El trabajo aquí es separar lo observado de lo inferido sobre **registro de acciones**. La evidencia que ordena la discusión es **acciones revertidas**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Instrumentar el registro completo de acciones.** El riesgo de este paso es cerrar demasiado rápido alrededor de **mecanismo de detención**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **tiempo de detención** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Habilitar la detención inmediata y probarla.** Con **acción irreversible** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **acciones ejecutadas por el agente** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar el registro periódicamente con responsable.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **autoridad del agente**. **acciones revertidas** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **autoridad del agente** | Conjunto de acciones que el sistema puede ejecutar sin aprobación humana | Cuando **acciones ejecutadas por el agente** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **registro de acciones** | Traza completa de qué hizo el sistema, cuándo y sobre qué registro | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** La responsabilidad legal y comercial siempre recae en la empresa, no en el sistema. La automatización no traslada la responsabilidad a nadie más.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre agentes comerciales automatizados |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager con IA, RevOps, Marketing manager y Sales enablement. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Un agente de Ruta Andina envió 400 correos de reactivación a clientes que habían solicitado no ser contactados, porque la regla de exclusión no estaba implementada.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **definir la autoridad del agente por tipo de acción → excluir las acciones irreversibles de la autonomía → instrumentar el registro completo de acciones → habilitar la detención inmediata y probarla → revisar el registro periódicamente con responsable** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **acciones ejecutadas por el agente**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **autoridad del agente** y **registro de acciones** como sinónimos | Se perdió la distinción entre «conjunto de acciones que el sistema puede ejecutar sin aprobación humana» y «traza completa de qué hizo el sistema, cuándo y sobre qué registro» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar el registro periódicamente con responsable» | Se saltó «definir la autoridad del agente por tipo de acción»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **acciones ejecutadas por el agente** | La métrica local reemplazó al resultado del sistema | Contrástala con **tiempo de detención** y explicita el costo de oportunidad. |
| Otorgar autoridad sobre acciones irreversibles | Error específico de esta clase | Excluye envíos y compromisos de la autonomía del agente y exige aprobación humana. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **autoridad del agente** y **registro de acciones** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **mecanismo de detención** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir la autoridad del agente por tipo de acción» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **acciones ejecutadas por el agente** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «La responsabilidad legal y comercial siempre recae en la empresa, no en el sistema. La automatización no traslada la responsabilidad a nadie más»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P21-C09-agentes-comerciales/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **acciones ejecutadas por el agente**, **acciones revertidas** y **tiempo de detención** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **operating model humano-IA con casos de uso, evaluaciones, guardrails y registro de incidentes**.

## ✅ Evaluación de la clase

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables entre los conceptos de la clase. |
| Diagnóstico y evidencia | 30 % | Datos pertinentes, línea base, supuestos explícitos y límites del dato. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas y argumento ejecutivo trazable. |

**Aprobación:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambios a otra clase se considera insuficiente.

## 📗 Fuentes y verificación

- Stuart Russell y Peter Norvig — *Artificial Intelligence: A Modern Approach* (2021, 4.ª ed.). **Uso en esta clase:** marco formal de agentes, entornos y medidas de desempeño. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- NIST — *AI Risk Management Framework 1.0* (2023). **Uso en esta clase:** gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- ISO — *ISO 31000: Gestión del riesgo* (2018). **Uso en esta clase:** vocabulario y proceso de gestión de riesgo aplicable a decisiones comerciales. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Cathy O'Neil — *Weapons of Math Destruction* (2016). **Uso en esta clase:** daños de los modelos opacos a escala y necesidad de auditoría. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 08 · Copilotos de ventas](class-08-copilotos-de-ventas.md) · [Índice de la parte](README.md) · [Clase 10 · Inteligencia de conversaciones](class-10-conversation-intelligence.md) →
