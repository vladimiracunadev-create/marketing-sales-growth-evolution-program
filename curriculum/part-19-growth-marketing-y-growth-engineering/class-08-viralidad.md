---
title: "Viralidad"
type: class
language: es
standard: clase-profunda-v3
part: 19
class: 08
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["ellis-brown", "bush-plg", "weinberg-traction", "godin"]
updated: 2026-08-18
---

# Clase 19.08 — Viralidad

**Parte 19 · Growth marketing y growth engineering** · Nivel: Crecimiento y analítica · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v3`

## 🎯 Propósito

La viralidad ocurre cuando cada usuario trae en promedio más de uno nuevo dentro de un ciclo, produciendo crecimiento exponencial. Es rara y suele ser mal entendida: la mayoría de los productos tiene un coeficiente muy por debajo de uno, lo que no impide que la viralidad parcial reduzca el costo de adquisición. El error frecuente es diseñar mecanismos virales en productos donde el uso no es visible para terceros.

El punto de partida de esta clase no es la definición sino la decisión que la definición debe mejorar. La parte 19 busca **instalar un motor de experimentación que produzca aprendizaje acumulativo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **viralidad** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué bucle hace que el crecimiento se retroalimente en lugar de depender del gasto?

Los conceptos que estructuran la sesión son **coeficiente viral**, **tiempo de ciclo viral**, **viralidad parcial** y **visibilidad del uso**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `coeficiente viral`, `tiempo de ciclo viral`, `viralidad parcial` y `visibilidad del uso` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Growth marketing y growth engineering**.
3. **Aplicar** la secuencia **medir el coeficiente y el tiempo de ciclo actuales → evaluar la visibilidad del uso para terceros → diseñar el mecanismo sólo si esa visibilidad existe → medir el efecto sobre el costo de adquisición → evitar mecanismos que degraden la experiencia** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **coeficiente viral**, **tiempo de ciclo** y **efecto en costo de adquisición** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **coeficiente viral** y **tiempo de ciclo viral** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **coeficiente viral**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **coeficiente viral** | número promedio de usuarios nuevos que genera cada usuario existente | Construye un caso límite donde el concepto se confunde con el anterior. |
| **tiempo de ciclo viral** | días entre la incorporación de un usuario y la de quienes trae | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **viralidad parcial** | contribución del mecanismo que reduce el costo de adquisición sin ser exponencial | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **visibilidad del uso** | grado en que terceros observan que alguien usa el producto | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. medir el coeficiente y el tiempo de ciclo actuales → 2. evaluar la visibilidad del uso para terceros → 3. diseñar el mecanismo sólo si esa visibilidad existe → 4. medir el efecto sobre el costo de adquisición → 5. evitar mecanismos que degraden la experiencia
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Los mecanismos virales intrusivos —acceso a contactos, envíos automáticos— dañan la reputación y pueden infringir normas de datos personales.

## 📖 Desarrollo

### 1. Coeficiente viral: mecanismo central

**coeficiente viral** se entiende aquí como **número promedio de usuarios nuevos que genera cada usuario existente**. Es la pieza desde la que se inicia el análisis de viralidad: antes de «medir el coeficiente y el tiempo de ciclo actuales», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Sean Ellis y Morgan Brown — *Hacking Growth* (2017). **Lente que aporta:** equipo multifuncional, ciclo de experimentación y aha moment. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **coeficiente viral**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **tiempo de ciclo viral**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Tiempo de ciclo viral: frontera conceptual y error de clasificación

**Definición operacional:** días entre la incorporación de un usuario y la de quienes trae. Su valor está en distinguirlo de **coeficiente viral**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Wes Bush — *Product-Led Growth* (2019) —**lente:** el producto como principal vehículo de adquisición, activación y expansión—. Formula dos mini-casos: uno que satisface la definición de **tiempo de ciclo viral** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **tiempo de ciclo** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «evaluar la visibilidad del uso para terceros», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Viralidad parcial: operacionalización y medición

**viralidad parcial** significa **contribución del mecanismo que reduce el costo de adquisición sin ser exponencial**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **coeficiente viral**: `usuarios nuevos generados por usuario existente, por ciclo`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Gabriel Weinberg y Justin Mares — *Traction* (2015) orienta este bloque —**lente:** diecinueve canales de tracción y el método bullseye de priorización—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Visibilidad del uso: trade-offs y efectos de segundo orden

**Definición:** grado en que terceros observan que alguien usa el producto. Este concepto obliga a abandonar la idea de que viralidad tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «medir el efecto sobre el costo de adquisición», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Seth Godin — *This Is Marketing* (2018) —**lente:** marketing como servicio a un público mínimo viable y construcción de confianza— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **efecto en costo de adquisición** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **visibilidad del uso** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «evitar mecanismos que degraden la experiencia», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Seth Godin — *This Is Marketing* (2018) sirve para contrastar la recomendación final desde otro lente: marketing como servicio a un público mínimo viable y construcción de confianza. La frontera de esta clase es explícita: Los mecanismos virales intrusivos —acceso a contactos, envíos automáticos— dañan la reputación y pueden infringir normas de datos personales. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar viralidad no consiste en sumar definiciones. Empieza por **coeficiente viral**, contrasta **tiempo de ciclo viral** con **viralidad parcial**, incorpora **visibilidad del uso** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Sean Ellis y Morgan Brown — *Hacking Growth* (2017) | equipo multifuncional, ciclo de experimentación y aha moment | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Wes Bush — *Product-Led Growth* (2019) | el producto como principal vehículo de adquisición, activación y expansión | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Gabriel Weinberg y Justin Mares — *Traction* (2015) | diecinueve canales de tracción y el método bullseye de priorización | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Seth Godin — *This Is Marketing* (2018) | marketing como servicio a un público mínimo viable y construcción de confianza | ¿Qué supuesto de esta clase ayuda a desafiar? |

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Los recordatorios que Ruta Andina envía a los clientes finales de cada taller son vistos por miles de personas al mes: allí existe visibilidad real, a diferencia del panel de administración.

**Paso 1 — Medir el coeficiente y el tiempo de ciclo actuales.** El equipo escribe primero el supuesto asociado a **coeficiente viral** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **coeficiente viral** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Evaluar la visibilidad del uso para terceros.** El trabajo aquí es separar lo observado de lo inferido sobre **tiempo de ciclo viral**. La evidencia que ordena la discusión es **tiempo de ciclo**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Diseñar el mecanismo sólo si esa visibilidad existe.** El riesgo de este paso es cerrar demasiado rápido alrededor de **viralidad parcial**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **efecto en costo de adquisición** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Medir el efecto sobre el costo de adquisición.** Con **visibilidad del uso** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **coeficiente viral** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Evitar mecanismos que degraden la experiencia.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **coeficiente viral**. **tiempo de ciclo** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **coeficiente viral** | Número promedio de usuarios nuevos que genera cada usuario existente | Cuando **coeficiente viral** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **tiempo de ciclo viral** | Días entre la incorporación de un usuario y la de quienes trae | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Los mecanismos virales intrusivos —acceso a contactos, envíos automáticos— dañan la reputación y pueden infringir normas de datos personales.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre viralidad |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager, Growth engineer y Head of Growth. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Los recordatorios que Ruta Andina envía a los clientes finales de cada taller son vistos por miles de personas al mes: allí existe visibilidad real, a diferencia del panel de administración.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **medir el coeficiente y el tiempo de ciclo actuales → evaluar la visibilidad del uso para terceros → diseñar el mecanismo sólo si esa visibilidad existe → medir el efecto sobre el costo de adquisición → evitar mecanismos que degraden la experiencia** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **coeficiente viral**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **coeficiente viral** y **tiempo de ciclo viral** como sinónimos | Se perdió la distinción entre «número promedio de usuarios nuevos que genera cada usuario existente» y «días entre la incorporación de un usuario y la de quienes trae» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «evitar mecanismos que degraden la experiencia» | Se saltó «medir el coeficiente y el tiempo de ciclo actuales»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **coeficiente viral** | La métrica local reemplazó al resultado del sistema | Contrástala con **efecto en costo de adquisición** y explicita el costo de oportunidad. |
| Diseñar mecanismos virales sin visibilidad del uso | Error específico de esta clase | Verifica que terceros puedan observar el uso antes de invertir en el mecanismo. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **coeficiente viral** y **tiempo de ciclo viral** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **viralidad parcial** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «medir el coeficiente y el tiempo de ciclo actuales» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **coeficiente viral** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Los mecanismos virales intrusivos —acceso a contactos, envíos automáticos— dañan la reputación y pueden infringir normas de datos personales»?

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P19-C08-viralidad/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **coeficiente viral**, **tiempo de ciclo** y **efecto en costo de adquisición** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **growth model con North Star, bucles, backlog priorizado y resultados de experimentos**.

## ✅ Evaluación de la clase

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables entre los conceptos de la clase. |
| Diagnóstico y evidencia | 30 % | Datos pertinentes, línea base, supuestos explícitos y límites del dato. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas y argumento ejecutivo trazable. |

**Aprobación:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambios a otra clase se considera insuficiente.

## 📗 Fuentes y verificación

- Sean Ellis y Morgan Brown — *Hacking Growth* (2017). **Uso en esta clase:** equipo multifuncional, ciclo de experimentación y aha moment. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Wes Bush — *Product-Led Growth* (2019). **Uso en esta clase:** el producto como principal vehículo de adquisición, activación y expansión. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Gabriel Weinberg y Justin Mares — *Traction* (2015). **Uso en esta clase:** diecinueve canales de tracción y el método bullseye de priorización. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Seth Godin — *This Is Marketing* (2018). **Uso en esta clase:** marketing como servicio a un público mínimo viable y construcción de confianza. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 07 · Bucles de referencia](class-07-referral-loops.md) · [Índice de la parte](README.md) · [Clase 09 · Backlog de experimentos](class-09-experiment-backlog.md) →
