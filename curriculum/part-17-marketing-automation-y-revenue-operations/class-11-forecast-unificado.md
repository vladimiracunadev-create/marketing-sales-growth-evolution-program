---
title: "Forecast unificado"
type: class
language: es
standard: clase-profunda-v2
part: 17
class: 11
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["mehta", "diorio", "croll-yoskovitz", "provost"]
anchors: {"croll-yoskovitz": "cohortes", "diorio": "definiciones", "mehta": "expansion", "provost": "evaluacion"}
updated: 2026-08-19
---

# Clase 17.11 — Forecast unificado

**Parte 17 · Marketing automation y revenue operations** · Nivel: Operación de ingresos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 17.10 — *Embudo de ingresos*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de precisión por componente para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La expansión condicionada al resultado inicial acreditado — Nick Mehta, Dan Steinman y Lincoln Murphy. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Un forecast unificado proyecta ingreso nuevo, renovaciones, expansión y contracción en un mismo modelo. Sin esa vista, la empresa puede celebrar un trimestre récord de ventas nuevas mientras pierde más ingreso por bajas del que incorpora. La proyección debe declarar sus supuestos por componente y medir la precisión de cada uno por separado.

El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta. La parte 17 busca **integrar marketing, ventas y servicio en un solo modelo de datos y de proceso**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **forecast unificado** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué automatizo porque mejora el sistema y qué estaría solo escalando un desorden?

Los conceptos que estructuran la sesión son **ingreso nuevo**, **renovación**, **expansión y contracción** y **precisión por componente**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `ingreso nuevo`, `renovación`, `expansión y contracción` y `precisión por componente` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Marketing automation y revenue operations**.
3. **Aplicar** la secuencia **modelar cada componente por separado → declarar los supuestos de cada uno → consolidar la proyección de ingreso neto → medir la precisión por componente → corregir los supuestos con el sesgo observado** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **precisión por componente**, **ingreso neto proyectado** y **cobertura de renovaciones** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **ingreso nuevo** y **renovación** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **precisión por componente**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **ingreso nuevo** | ingreso incorporado por clientes que no existían al inicio del periodo | Da un hecho compatible con la definición y otro que la refute. |
| **renovación** | ingreso conservado de clientes existentes al vencer su contrato | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **expansión y contracción** | aumento o reducción de ingreso en clientes que permanecen | Construye un caso límite donde el concepto se confunde con el anterior. |
| **precisión por componente** | medición separada de la exactitud de cada parte de la proyección | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. modelar cada componente por separado → 2. declarar los supuestos de cada uno → 3. consolidar la proyección de ingreso neto → 4. medir la precisión por componente → 5. corregir los supuestos con el sesgo observado
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** La proyección de renovaciones requiere cohortes maduras. En empresas jóvenes el error es alto y debe declararse como rango.

## 📖 Desarrollo

### 1. Ingreso nuevo: mecanismo central

**Ingreso nuevo** se entiende aquí como **ingreso incorporado por clientes que no existían al inicio del periodo**.

Un pronóstico unificado separa los componentes del ingreso porque cada uno se comporta distinto: ingreso nuevo, renovación, expansión y contracción tienen predictibilidad y responsables diferentes. Sumarlos en una sola cifra oculta que el error de pronóstico puede venir de un solo componente.

**De dónde viene esta afirmación.** Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) aporta la idea que sostiene este bloque: la expansión condicionada al resultado inicial acreditado. Búscala en los capítulos sobre crecimiento en la base instalada. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «precisión por componente» debería moverse cuando cambie **ingreso nuevo**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **renovación**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Renovación: frontera conceptual y error de clasificación

**Definición operacional:** ingreso conservado de clientes existentes al vencer su contrato. Su valor está en distinguirlo de **ingreso nuevo**.

La renovación es el componente más predecible y el que menos atención recibe en el proceso de pronóstico, porque suele darse por supuesta. Modelarla explícitamente —con tasa histórica por segmento y por antigüedad— mejora la precisión total más que refinar el pronóstico de ingreso nuevo.

**Contraste bibliográfico.** Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) aporta aquí una distinción concreta: la definición única por indicador como acuerdo previo a cualquier tablero (los capítulos sobre gobierno de métricas). Formula dos mini-casos: uno que satisface la definición de **renovación** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «declarar los supuestos de cada uno», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Expansión y contracción: operacionalización y medición

**Expansión y contracción** significa **aumento o reducción de ingreso en clientes que permanecen**.

La precisión por componente debe medirse por separado. Un pronóstico global con error aceptable puede estar compensando una sobreestimación de nuevo con una subestimación de renovación, y esa compensación no se repetirá. Medir por componente permite corregir donde está el problema.

Ficha de medición obligatoria para **precisión por componente**: `diferencia entre proyección y resultado, por componente y trimestre`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) pone una condición sobre la medición: el análisis de cohortes como corrección al promedio que esconde la mezcla (el capítulo sobre cohortes y segmentación). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Precisión por componente: trade-offs y efectos de segundo orden

**Definición:** medición separada de la exactitud de cada parte de la proyección.

Un proceso de pronóstico detallado mejora la precisión y consume tiempo de muchas personas cada periodo. La inversión se justifica cuando las decisiones dependen del pronóstico —contratación, inversión, compromisos financieros— y no cuando el pronóstico sólo se reporta.

**Lo que aporta la fuente.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta el criterio para pesar el intercambio: la evaluación contra una línea base y no contra la nada (los capítulos sobre evaluación de modelos). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **cobertura de renovaciones** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **precisión por componente** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «corregir los supuestos con el sesgo observado», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La contracción —clientes que reducen su consumo sin irse— es el componente que más se omite y que puede explicar una parte relevante de la desviación. Su medición exige comparar el mismo cliente consigo mismo en el tiempo, no comparar totales. Incorporarla al pronóstico suele revelar un deterioro que el ingreso agregado ocultaba.

**Frontera declarada.** La proyección de renovaciones requiere cohortes maduras. En empresas jóvenes el error es alto y debe declararse como rango. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar forecast unificado no consiste en sumar definiciones. Empieza por **ingreso nuevo**, contrasta **renovación** con **expansión y contracción**, incorpora **precisión por componente** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) | La expansión condicionada al resultado inicial acreditado | Los capítulos sobre crecimiento en la base instalada | ¿Qué debería observarse en **ingreso nuevo** si aquí opera «la expansión condicionada al resultado inicial acreditado»? ¿Y qué observación lo desmentiría en este caso? |
| Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) | La definición única por indicador como acuerdo previo a cualquier tablero | Los capítulos sobre gobierno de métricas | ¿Qué debería observarse en **renovación** si aquí opera «la definición única por indicador como acuerdo previo a cualquier tablero»? ¿Y qué observación lo desmentiría en este caso? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | El análisis de cohortes como corrección al promedio que esconde la mezcla | El capítulo sobre cohortes y segmentación | ¿Qué debería observarse en **expansión y contracción** si aquí opera «el análisis de cohortes como corrección al promedio que esconde la mezcla»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La evaluación contra una línea base y no contra la nada | Los capítulos sobre evaluación de modelos | ¿Qué debería observarse en **precisión por componente** si aquí opera «la evaluación contra una línea base y no contra la nada»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina proyecta ventas nuevas con detalle y estima renovaciones con un porcentaje fijo heredado de 2025 que nadie ha vuelto a validar.

**Paso 1 — Modelar cada componente por separado.** El equipo escribe primero el supuesto asociado a **ingreso nuevo** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **precisión por componente** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Declarar los supuestos de cada uno.** El trabajo aquí es separar lo observado de lo inferido sobre **renovación**. La evidencia que ordena la discusión es **ingreso neto proyectado**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Consolidar la proyección de ingreso neto.** El riesgo de este paso es cerrar demasiado rápido alrededor de **expansión y contracción**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **cobertura de renovaciones** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Medir la precisión por componente.** Con **precisión por componente** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **precisión por componente** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Corregir los supuestos con el sesgo observado.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **ingreso nuevo**. **ingreso neto proyectado** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **ingreso nuevo** | Ingreso incorporado por clientes que no existían al inicio del periodo | Cuando **precisión por componente** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **renovación** | Ingreso conservado de clientes existentes al vencer su contrato | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** La proyección de renovaciones requiere cohortes maduras. En empresas jóvenes el error es alto y debe declararse como rango.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre forecast unificado |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing ops, RevOps manager y Sales ops. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina proyecta ventas nuevas con detalle y estima renovaciones con un porcentaje fijo heredado de 2025 que nadie ha vuelto a validar.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **modelar cada componente por separado → declarar los supuestos de cada uno → consolidar la proyección de ingreso neto → medir la precisión por componente → corregir los supuestos con el sesgo observado** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **precisión por componente**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Customer Success* y la de *Revenue Operations*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **ingreso nuevo** y **renovación** como sinónimos | Se perdió la distinción entre «ingreso incorporado por clientes que no existían al inicio del periodo» y «ingreso conservado de clientes existentes al vencer su contrato» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «corregir los supuestos con el sesgo observado» | Se saltó «modelar cada componente por separado»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **precisión por componente** | La métrica local reemplazó al resultado del sistema | Contrástala con **cobertura de renovaciones** y explicita el costo de oportunidad. |
| Proyectar renovaciones con un porcentaje fijo | Error específico de esta clase | Modela renovación por cohorte y segmento, y mide su precisión cada trimestre. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **ingreso nuevo** y **renovación** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **expansión y contracción** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «modelar cada componente por separado» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **precisión por componente** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «La proyección de renovaciones requiere cohortes maduras. En empresas jóvenes el error es alto y debe declararse como rango»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **expansión y contracción** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **precisión por componente**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Customer Success* y *Data Science for Business*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P17-C11-forecast-unificado/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **precisión por componente**, **ingreso neto proyectado** y **cobertura de renovaciones** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **operating model de RevOps con lifecycle, scoring, SLA, integraciones y observabilidad**.

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

- Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) — **aporta a esta clase:** la expansión condicionada al resultado inicial acreditado. **Dónde buscarlo:** los capítulos sobre crecimiento en la base instalada. Registra edición y páginas consultadas en tu nota de lectura.
- Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) — **aporta a esta clase:** la definición única por indicador como acuerdo previo a cualquier tablero. **Dónde buscarlo:** los capítulos sobre gobierno de métricas. Registra edición y páginas consultadas en tu nota de lectura.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — **aporta a esta clase:** el análisis de cohortes como corrección al promedio que esconde la mezcla. **Dónde buscarlo:** el capítulo sobre cohortes y segmentación. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — **aporta a esta clase:** la evaluación contra una línea base y no contra la nada. **Dónde buscarlo:** los capítulos sobre evaluación de modelos. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 10 · Embudo de ingresos](class-10-revenue-funnel.md) · [Índice de la parte](README.md) · [Clase 12 · Calidad y observabilidad](class-12-calidad-y-observabilidad.md) →
