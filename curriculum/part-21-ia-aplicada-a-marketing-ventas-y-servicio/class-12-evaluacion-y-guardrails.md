---
title: "Evaluación y guardrails"
type: class
language: es
standard: clase-profunda-v1
part: 21
class: 12
level: IA y expansión
mastery_threshold: 80
estimated_minutes: 150
sources: ["nist-airmf", "ng-mlyearning", "kohavi", "iso-31000"]
updated: 2026-08-19
---

# Clase 21.12 — Evaluación y guardrails

**Parte 21 · IA aplicada a marketing, ventas y servicio** · Nivel: IA y expansión · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v1`

## 🎯 Propósito

Un sistema de IA sin evaluación es una apuesta. Evaluar significa definir un conjunto de casos representativos con respuesta esperada, medir el desempeño antes de desplegar y monitorearlo después. Los guardarraíles son las restricciones que impiden comportamientos inaceptables aunque el sistema los proponga. El marco de gestión de riesgo del NIST ordena esto en cuatro funciones: mapear, medir, gestionar y gobernar.

La clase trata el tema como un problema de evidencia y de consecuencia, no como vocabulario. La parte 21 busca **usar IA como capacidad operativa con evaluación, control y responsabilidad humana**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **evaluación y guardrails** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué tarea mejora con IA, cómo sé que mejora y quién responde cuando falla?

Los conceptos que estructuran la sesión son **conjunto de evaluación**, **guardarraíl**, **monitoreo posterior** y **umbral de aceptación**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `conjunto de evaluación`, `guardarraíl`, `monitoreo posterior` y `umbral de aceptación` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **IA aplicada a marketing, ventas y servicio**.
3. **Aplicar** la secuencia **construir el conjunto de evaluación con casos reales → definir el umbral de aceptación antes de probar → implementar guardarraíles sobre los riesgos identificados → monitorear el desempeño en producción → documentar incidentes y ajustar el sistema** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **desempeño en el conjunto de evaluación**, **incidentes por guardarraíl activado** y **deriva de desempeño** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **conjunto de evaluación** y **guardarraíl** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **desempeño en el conjunto de evaluación**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **conjunto de evaluación** | casos representativos con resultado esperado que permiten medir el desempeño | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **guardarraíl** | restricción que impide un comportamiento inaceptable del sistema | Construye un caso límite donde el concepto se confunde con el anterior. |
| **monitoreo posterior** | medición continua del desempeño tras el despliegue | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **umbral de aceptación** | nivel de desempeño mínimo que autoriza el uso en producción | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. construir el conjunto de evaluación con casos reales → 2. definir el umbral de aceptación antes de probar → 3. implementar guardarraíles sobre los riesgos identificados → 4. monitorear el desempeño en producción → 5. documentar incidentes y ajustar el sistema
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Ningún conjunto de evaluación cubre todos los casos posibles. Los guardarraíles y el monitoreo son necesarios precisamente porque la evaluación previa es incompleta.

## 📖 Desarrollo

### 1. Conjunto de evaluación: mecanismo central

**conjunto de evaluación** se entiende aquí como **casos representativos con resultado esperado que permiten medir el desempeño**. Es la pieza desde la que se inicia el análisis de evaluación y guardrails: antes de «construir el conjunto de evaluación con casos reales», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es NIST — *AI Risk Management Framework 1.0* (2023). **Lente que aporta:** gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **desempeño en el conjunto de evaluación**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **guardarraíl**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Guardarraíl: frontera conceptual y error de clasificación

**Definición operacional:** restricción que impide un comportamiento inaceptable del sistema. Su valor está en distinguirlo de **conjunto de evaluación**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Andrew Ng — *Machine Learning Yearning* (2018) —**lente:** diagnóstico de sistemas de aprendizaje y priorización de mejoras—. Formula dos mini-casos: uno que satisface la definición de **guardarraíl** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **incidentes por guardarraíl activado** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «definir el umbral de aceptación antes de probar», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Monitoreo posterior: operacionalización y medición

**monitoreo posterior** significa **medición continua del desempeño tras el despliegue**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **desempeño en el conjunto de evaluación**: `casos resueltos correctamente, sobre casos del conjunto`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) orienta este bloque —**lente:** diseño estadístico de experimentos, métricas guardrail y trampas de interpretación—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Umbral de aceptación: trade-offs y efectos de segundo orden

**Definición:** nivel de desempeño mínimo que autoriza el uso en producción. Este concepto obliga a abandonar la idea de que evaluación y guardrails tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «monitorear el desempeño en producción», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

ISO — *ISO 31000: Gestión del riesgo* (2018) —**lente:** vocabulario y proceso de gestión de riesgo aplicable a decisiones comerciales— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **deriva de desempeño** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **umbral de aceptación** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «documentar incidentes y ajustar el sistema», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

ISO — *ISO 31000: Gestión del riesgo* (2018) sirve para contrastar la recomendación final desde otro lente: vocabulario y proceso de gestión de riesgo aplicable a decisiones comerciales. La frontera de esta clase es explícita: Ningún conjunto de evaluación cubre todos los casos posibles. Los guardarraíles y el monitoreo son necesarios precisamente porque la evaluación previa es incompleta. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar evaluación y guardrails no consiste en sumar definiciones. Empieza por **conjunto de evaluación**, contrasta **guardarraíl** con **monitoreo posterior**, incorpora **umbral de aceptación** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| NIST — *AI Risk Management Framework 1.0* (2023) | gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Andrew Ng — *Machine Learning Yearning* (2018) | diagnóstico de sistemas de aprendizaje y priorización de mejoras | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | diseño estadístico de experimentos, métricas guardrail y trampas de interpretación | ¿Qué supuesto de esta clase ayuda a desafiar? |
| ISO — *ISO 31000: Gestión del riesgo* (2018) | vocabulario y proceso de gestión de riesgo aplicable a decisiones comerciales | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina desplegó su asistente sin conjunto de evaluación. Descubrió que prometía funcionalidades inexistentes cuando un cliente reclamó por escrito.

**Paso 1 — Construir el conjunto de evaluación con casos reales.** El equipo escribe primero el supuesto asociado a **conjunto de evaluación** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **desempeño en el conjunto de evaluación** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Definir el umbral de aceptación antes de probar.** El trabajo aquí es separar lo observado de lo inferido sobre **guardarraíl**. La evidencia que ordena la discusión es **incidentes por guardarraíl activado**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Implementar guardarraíles sobre los riesgos identificados.** El riesgo de este paso es cerrar demasiado rápido alrededor de **monitoreo posterior**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **deriva de desempeño** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Monitorear el desempeño en producción.** Con **umbral de aceptación** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **desempeño en el conjunto de evaluación** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Documentar incidentes y ajustar el sistema.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **conjunto de evaluación**. **incidentes por guardarraíl activado** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **conjunto de evaluación** | Casos representativos con resultado esperado que permiten medir el desempeño | Cuando **desempeño en el conjunto de evaluación** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **guardarraíl** | Restricción que impide un comportamiento inaceptable del sistema | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Ningún conjunto de evaluación cubre todos los casos posibles. Los guardarraíles y el monitoreo son necesarios precisamente porque la evaluación previa es incompleta.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre evaluación y guardrails |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager con IA, RevOps, Marketing manager y Sales enablement. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina desplegó su asistente sin conjunto de evaluación. Descubrió que prometía funcionalidades inexistentes cuando un cliente reclamó por escrito.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **construir el conjunto de evaluación con casos reales → definir el umbral de aceptación antes de probar → implementar guardarraíles sobre los riesgos identificados → monitorear el desempeño en producción → documentar incidentes y ajustar el sistema** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **desempeño en el conjunto de evaluación**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **conjunto de evaluación** y **guardarraíl** como sinónimos | Se perdió la distinción entre «casos representativos con resultado esperado que permiten medir el desempeño» y «restricción que impide un comportamiento inaceptable del sistema» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «documentar incidentes y ajustar el sistema» | Se saltó «construir el conjunto de evaluación con casos reales»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **desempeño en el conjunto de evaluación** | La métrica local reemplazó al resultado del sistema | Contrástala con **deriva de desempeño** y explicita el costo de oportunidad. |
| Desplegar sin conjunto de evaluación ni umbral | Error específico de esta clase | Construye casos representativos con respuesta esperada y define el umbral antes del despliegue. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **conjunto de evaluación** y **guardarraíl** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **monitoreo posterior** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «construir el conjunto de evaluación con casos reales» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **desempeño en el conjunto de evaluación** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Ningún conjunto de evaluación cubre todos los casos posibles. Los guardarraíles y el monitoreo son necesarios precisamente porque la evaluación previa es incompleta»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P21-C12-evaluacion-y-guardrails/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **desempeño en el conjunto de evaluación**, **incidentes por guardarraíl activado** y **deriva de desempeño** con fuente, ventana y lectura prohibida.
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

- NIST — *AI Risk Management Framework 1.0* (2023). **Uso en esta clase:** gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Andrew Ng — *Machine Learning Yearning* (2018). **Uso en esta clase:** diagnóstico de sistemas de aprendizaje y priorización de mejoras. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020). **Uso en esta clase:** diseño estadístico de experimentos, métricas guardrail y trampas de interpretación. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- ISO — *ISO 31000: Gestión del riesgo* (2018). **Uso en esta clase:** vocabulario y proceso de gestión de riesgo aplicable a decisiones comerciales. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 11 · IA en customer success](class-11-ia-en-customer-success.md) · [Índice de la parte](README.md) · [Clase 13 · Privacidad y propiedad intelectual](class-13-privacidad-y-propiedad-intelectual.md) →
