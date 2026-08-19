---
title: "Periodo de recuperación"
type: class
language: es
standard: clase-profunda-v2
part: 20
class: 05
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["croll-yoskovitz", "fader-ltv", "provost", "simon"]
anchors: {"croll-yoskovitz": "linea-trazada", "fader-ltv": "inversion-diferencial", "provost": "valor-esperado", "simon": "palanca-precio"}
updated: 2026-08-19
---

# Clase 20.05 — Periodo de recuperación

**Parte 20 · Analítica comercial y marketing science** · Nivel: Crecimiento y analítica · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 20.04 — *Valor de vida del cliente*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de periodo de recuperación por segmento para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La línea trazada de antemano: qué valor haría considerar exitoso el experimento — Alistair Croll y Benjamin Yoskovitz. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

El periodo de recuperación indica cuántos meses tarda el margen de un cliente en cubrir su costo de adquisición. Es más útil que la relación entre valor de vida y costo para decidir ritmo de inversión, porque habla directamente de caja. Una empresa con recuperación de 18 meses y caja para 6 no puede escalar aunque su valor de vida sea excelente.

La clase trata el tema como un problema de evidencia y de consecuencia, no como vocabulario. La parte 20 busca **sostener decisiones de ingreso con métricas correctamente construidas**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **periodo de recuperación** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Esta cifra mide lo que creo que mide, y qué decisión cambiaría si estuviera equivocada?

Los conceptos que estructuran la sesión son **periodo de recuperación**, **restricción de caja**, **ritmo sostenible de adquisición** y **relación con la vida del cliente**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `periodo de recuperación`, `restricción de caja`, `ritmo sostenible de adquisición` y `relación con la vida del cliente` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Analítica comercial y marketing science**.
3. **Aplicar** la secuencia **calcular el margen mensual por cliente → determinar el periodo de recuperación por segmento → compararlo con la vida media observada → estimar el ritmo sostenible según la caja disponible → ajustar la meta de adquisición a esa restricción** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **periodo de recuperación por segmento**, **relación recuperación-permanencia** y **clientes financiables por periodo** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **periodo de recuperación** y **restricción de caja** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **periodo de recuperación por segmento**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **periodo de recuperación** | meses hasta que el margen acumulado iguala el costo de adquisición | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **restricción de caja** | límite de inversión impuesto por la liquidez disponible | Da un hecho compatible con la definición y otro que la refute. |
| **ritmo sostenible de adquisición** | volumen de clientes nuevos que la caja permite financiar | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **relación con la vida del cliente** | comparación entre recuperación y permanencia esperada | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. calcular el margen mensual por cliente → 2. determinar el periodo de recuperación por segmento → 3. compararlo con la vida media observada → 4. estimar el ritmo sostenible según la caja disponible → 5. ajustar la meta de adquisición a esa restricción
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** El periodo de recuperación ignora el valor posterior. Un negocio con recuperación larga puede ser excelente si la permanencia es muy alta y hay financiamiento.

## 📖 Desarrollo

### 1. Periodo de recuperación: mecanismo central

**Periodo de recuperación** se entiende aquí como **meses hasta que el margen acumulado iguala el costo de adquisición**.

El periodo de recuperación —cuánto tarda el margen de un cliente en cubrir lo que costó adquirirlo— es la métrica que gobierna la velocidad sostenible de crecimiento. Un negocio puede tener una relación favorable entre valor y costo y aun así quebrar, si el dinero tarda demasiado en volver.

**De dónde viene esta afirmación.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) aporta la idea que sostiene este bloque: la línea trazada de antemano: qué valor haría considerar exitoso el experimento. Búscala en los capítulos sobre definir el éxito. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «periodo de recuperación por segmento» debería moverse cuando cambie **periodo de recuperación**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **restricción de caja**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Restricción de caja: frontera conceptual y error de clasificación

**Definición operacional:** límite de inversión impuesto por la liquidez disponible. Su valor está en distinguirlo de **periodo de recuperación**.

La restricción de caja es lo que hace de esta métrica una decisión y no un dato: con recursos limitados, el periodo de recuperación determina cuántos clientes nuevos se pueden financiar por periodo. En el caso de Ruta Andina, catorce meses de recuperación contra once de permanencia describe un sistema que consume caja con cada venta.

**Contraste bibliográfico.** Peter Fader y Sarah Toms — *The Customer Centricity Playbook* (2018) aporta aquí una distinción concreta: la inversión diferenciada por valor esperado del cliente (los capítulos sobre decisiones de inversión). Formula dos mini-casos: uno que satisface la definición de **restricción de caja** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «determinar el periodo de recuperación por segmento», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Ritmo sostenible de adquisición: operacionalización y medición

**Ritmo sostenible de adquisición** significa **volumen de clientes nuevos que la caja permite financiar**.

El cálculo debe usar margen de contribución y no ingreso, e incluir el costo de servir. Usar ingreso produce un periodo aparentemente corto que no corresponde a la realidad de la caja. La ficha debe declarar qué se incluyó, porque la diferencia entre ambas versiones puede ser de varios meses.

Ficha de medición obligatoria para **periodo de recuperación por segmento**: `meses hasta recuperar el costo de adquisición, por segmento`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) pone una condición sobre la medición: el marco de valor esperado que combina probabilidad y consecuencia económica (el capítulo sobre valor esperado). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Relación con la vida del cliente: trade-offs y efectos de segundo orden

**Definición:** comparación entre recuperación y permanencia esperada.

Reducir el periodo de recuperación puede lograrse subiendo precio, cobrando por adelantado o bajando el costo de adquisición. Cada opción tiene efectos secundarios: el cobro anticipado mejora la caja y puede reducir la conversión. Modelar ese intercambio antes de decidir evita resolver un problema creando otro.

**Lo que aporta la fuente.** Hermann Simon — *Confessions of the Pricing Man* (2015) aporta el criterio para pesar el intercambio: el precio como la palanca de utilidad más rápida frente a volumen y costo (los capítulos sobre el poder del precio). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **clientes financiables por periodo** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **relación con la vida del cliente** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «ajustar la meta de adquisición a esa restricción», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La métrica supone que la permanencia se mantiene durante el periodo de recuperación, y ese supuesto hay que verificarlo. Cuando el periodo excede la permanencia mediana, el negocio está estructurado para perder dinero con cada cliente, y ninguna optimización de canal lo corrige.

**Frontera declarada.** El periodo de recuperación ignora el valor posterior. Un negocio con recuperación larga puede ser excelente si la permanencia es muy alta y hay financiamiento. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar periodo de recuperación no consiste en sumar definiciones. Empieza por **periodo de recuperación**, contrasta **restricción de caja** con **ritmo sostenible de adquisición**, incorpora **relación con la vida del cliente** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | La línea trazada de antemano: qué valor haría considerar exitoso el experimento | Los capítulos sobre definir el éxito | ¿Qué debería observarse en **periodo de recuperación** si aquí opera «la línea trazada de antemano: qué valor haría considerar exitoso el experimento»? ¿Y qué observación lo desmentiría en este caso? |
| Peter Fader y Sarah Toms — *The Customer Centricity Playbook* (2018) | La inversión diferenciada por valor esperado del cliente | Los capítulos sobre decisiones de inversión | ¿Qué debería observarse en **restricción de caja** si aquí opera «la inversión diferenciada por valor esperado del cliente»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | El marco de valor esperado que combina probabilidad y consecuencia económica | El capítulo sobre valor esperado | ¿Qué debería observarse en **ritmo sostenible de adquisición** si aquí opera «el marco de valor esperado que combina probabilidad y consecuencia económica»? ¿Y qué observación lo desmentiría en este caso? |
| Hermann Simon — *Confessions of the Pricing Man* (2015) | El precio como la palanca de utilidad más rápida frente a volumen y costo | Los capítulos sobre el poder del precio | ¿Qué debería observarse en **relación con la vida del cliente** si aquí opera «el precio como la palanca de utilidad más rápida frente a volumen y costo»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina recupera su inversión en 14 meses y su vida media de cliente es 11. Cada cliente nuevo destruye caja antes de aportar.

**Paso 1 — Calcular el margen mensual por cliente.** El equipo escribe primero el supuesto asociado a **periodo de recuperación** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **periodo de recuperación por segmento** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Determinar el periodo de recuperación por segmento.** El trabajo aquí es separar lo observado de lo inferido sobre **restricción de caja**. La evidencia que ordena la discusión es **relación recuperación-permanencia**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Compararlo con la vida media observada.** El riesgo de este paso es cerrar demasiado rápido alrededor de **ritmo sostenible de adquisición**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **clientes financiables por periodo** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Estimar el ritmo sostenible según la caja disponible.** Con **relación con la vida del cliente** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **periodo de recuperación por segmento** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Ajustar la meta de adquisición a esa restricción.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **periodo de recuperación**. **relación recuperación-permanencia** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **periodo de recuperación** | Meses hasta que el margen acumulado iguala el costo de adquisición | Cuando **periodo de recuperación por segmento** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **restricción de caja** | Límite de inversión impuesto por la liquidez disponible | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** El periodo de recuperación ignora el valor posterior. Un negocio con recuperación larga puede ser excelente si la permanencia es muy alta y hay financiamiento.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre periodo de recuperación |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing analyst, Revenue analyst y Data-driven marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina recupera su inversión en 14 meses y su vida media de cliente es 11. Cada cliente nuevo destruye caja antes de aportar.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **calcular el margen mensual por cliente → determinar el periodo de recuperación por segmento → compararlo con la vida media observada → estimar el ritmo sostenible según la caja disponible → ajustar la meta de adquisición a esa restricción** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **periodo de recuperación por segmento**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Lean Analytics* y la de *The Customer Centricity Playbook*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **periodo de recuperación** y **restricción de caja** como sinónimos | Se perdió la distinción entre «meses hasta que el margen acumulado iguala el costo de adquisición» y «límite de inversión impuesto por la liquidez disponible» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «ajustar la meta de adquisición a esa restricción» | Se saltó «calcular el margen mensual por cliente»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **periodo de recuperación por segmento** | La métrica local reemplazó al resultado del sistema | Contrástala con **clientes financiables por periodo** y explicita el costo de oportunidad. |
| Escalar con recuperación mayor que la vida del cliente | Error específico de esta clase | Compara ambos indicadores por segmento antes de aumentar la inversión en adquisición. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **periodo de recuperación** y **restricción de caja** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **ritmo sostenible de adquisición** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «calcular el margen mensual por cliente» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **periodo de recuperación por segmento** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «El periodo de recuperación ignora el valor posterior. Un negocio con recuperación larga puede ser excelente si la permanencia es muy alta y hay financiamiento»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **ritmo sostenible de adquisición** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **periodo de recuperación por segmento**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Lean Analytics* y *Confessions of the Pricing Man*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P20-C05-payback/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **periodo de recuperación por segmento**, **relación recuperación-permanencia** y **clientes financiables por periodo** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **caso analítico integral con árbol de métricas, cohortes, incrementalidad y dashboard ejecutivo**.

## ✅ Evaluación de la clase

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables entre los conceptos de la clase. |
| Diagnóstico y evidencia | 30 % | Datos pertinentes, línea base, supuestos explícitos y límites del dato. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas y argumento ejecutivo trazable. |

**Aprobación:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambios a otra clase se considera insuficiente.

## 📗 Fuentes y verificación

Cada obra aparece con la idea concreta que aporta a esta clase. Si al leer no encuentras esa idea, la cita está mal puesta y corresponde reportarlo como error del material.

- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — **aporta a esta clase:** la línea trazada de antemano: qué valor haría considerar exitoso el experimento. **Dónde buscarlo:** los capítulos sobre definir el éxito. Registra edición y páginas consultadas en tu nota de lectura.
- Peter Fader y Sarah Toms — *The Customer Centricity Playbook* (2018) — **aporta a esta clase:** la inversión diferenciada por valor esperado del cliente. **Dónde buscarlo:** los capítulos sobre decisiones de inversión. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — **aporta a esta clase:** el marco de valor esperado que combina probabilidad y consecuencia económica. **Dónde buscarlo:** el capítulo sobre valor esperado. Registra edición y páginas consultadas en tu nota de lectura.
- Hermann Simon — *Confessions of the Pricing Man* (2015) — **aporta a esta clase:** el precio como la palanca de utilidad más rápida frente a volumen y costo. **Dónde buscarlo:** los capítulos sobre el poder del precio. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 04 · Valor de vida del cliente](class-04-ltv.md) · [Índice de la parte](README.md) · [Clase 06 · Margen de contribución](class-06-contribution-margin.md) →
