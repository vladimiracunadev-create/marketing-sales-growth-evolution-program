---
title: "North Star Metric"
type: class
language: es
standard: clase-profunda-v2
part: 19
class: 02
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["ellis-brown", "croll-yoskovitz", "doerr", "kaplan-norton"]
anchors: {"croll-yoskovitz": "una-metrica", "doerr": "foco", "ellis-brown": "aha", "kaplan-norton": "indicadores-causales"}
updated: 2026-08-19
---

# Clase 19.02 — North Star Metric

**Parte 19 · Growth marketing y growth engineering** · Nivel: Crecimiento y analítica · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 19.01 — *Qué es growth*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de valor de la métrica estrella para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El momento «ajá» identificado con datos y no supuesto — Sean Ellis y Morgan Brown. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Una métrica estrella es el indicador que mejor representa el valor entregado al cliente y que, al crecer, arrastra al negocio. Su elección es una decisión estratégica: enfoca al equipo y excluye otras lecturas. Debe cumplir tres condiciones: reflejar valor para el cliente, ser influenciable por el equipo y correlacionar con el ingreso a mediano plazo.

Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales. La parte 19 busca **instalar un motor de experimentación que produzca aprendizaje acumulativo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **north Star Metric** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué bucle hace que el crecimiento se retroalimente en lugar de depender del gasto?

Los conceptos que estructuran la sesión son **métrica estrella**, **métrica de entrada**, **correlación con ingreso** y **efecto de enfoque**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `métrica estrella`, `métrica de entrada`, `correlación con ingreso` y `efecto de enfoque` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Growth marketing y growth engineering**.
3. **Aplicar** la secuencia **identificar el momento en que el cliente obtiene valor → proponer candidatas y verificar su correlación con ingreso → descomponer la métrica en sus entradas → declarar la elección y comunicarla → revisar la elección cuando cambia el modelo de negocio** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **valor de la métrica estrella**, **correlación con ingreso** y **alineación de iniciativas** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **métrica estrella** y **métrica de entrada** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **valor de la métrica estrella**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **métrica estrella** | indicador único que representa el valor entregado y guía las decisiones | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **métrica de entrada** | componente que alimenta la métrica estrella y sobre el que se actúa | Construye un caso límite donde el concepto se confunde con el anterior. |
| **correlación con ingreso** | relación observada entre la métrica y el resultado financiero | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **efecto de enfoque** | concentración del esfuerzo que produce elegir una sola métrica | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. identificar el momento en que el cliente obtiene valor → 2. proponer candidatas y verificar su correlación con ingreso → 3. descomponer la métrica en sus entradas → 4. declarar la elección y comunicarla → 5. revisar la elección cuando cambia el modelo de negocio
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Una sola métrica no describe un negocio completo. Debe acompañarse de guardarraíles que impidan optimizarla dañando margen, retención o reputación.

## 📖 Desarrollo

### 1. Métrica estrella: mecanismo central

**Métrica estrella** se entiende aquí como **indicador único que representa el valor entregado y guía las decisiones**.

La métrica estrella intenta resumir en un número el valor que la empresa entrega. Su función no es medir todo sino alinear: cuando varias áreas optimizan indicadores distintos, el sistema se desordena. Elegirla es una decisión de dirección y su principal efecto es sobre qué se deja de hacer.

**De dónde viene esta afirmación.** Sean Ellis y Morgan Brown — *Hacking Growth* (2017) aporta la idea que sostiene este bloque: el momento «ajá» identificado con datos y no supuesto. Búscala en los capítulos sobre el momento de valor. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «valor de la métrica estrella» debería moverse cuando cambie **métrica estrella**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **métrica de entrada**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Métrica de entrada: frontera conceptual y error de clasificación

**Definición operacional:** componente que alimenta la métrica estrella y sobre el que se actúa. Su valor está en distinguirlo de **métrica estrella**.

Una buena métrica estrella tiene tres propiedades: refleja valor entregado al cliente, se puede influir con las decisiones del equipo y correlaciona con el ingreso en el mediano plazo. Un indicador que cumple sólo las dos primeras produce equipos ocupados y empresas que no crecen.

**Contraste bibliográfico.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) aporta aquí una distinción concreta: la métrica que importa ahora: una sola, según etapa y modelo de negocio (los capítulos sobre la métrica única). Formula dos mini-casos: uno que satisface la definición de **métrica de entrada** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «proponer candidatas y verificar su correlación con ingreso», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Correlación con ingreso: operacionalización y medición

**Correlación con ingreso** significa **relación observada entre la métrica y el resultado financiero**.

La correlación con el ingreso debe verificarse con datos propios y no suponerse. El procedimiento es comparar la evolución de la métrica candidata con la del ingreso en el histórico disponible, reconociendo que la correlación no establece causa. Cuando no hay relación observable, la métrica puede seguir siendo válida pero el supuesto debe declararse.

Ficha de medición obligatoria para **valor de la métrica estrella**: `valor del indicador elegido en el periodo, sobre su valor en el periodo anterior comparable`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** John Doerr — *Measure What Matters* (2018) pone una condición sobre la medición: el foco: pocos objetivos, con lo descartado explícito (los capítulos sobre comprometerse con prioridades). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Efecto de enfoque: trade-offs y efectos de segundo orden

**Definición:** concentración del esfuerzo que produce elegir una sola métrica.

Una métrica única concentra el esfuerzo y crea el riesgo de optimizarla a costa de otras variables. Por eso debe acompañarse de guardarraíles: indicadores que no deben deteriorarse aunque la métrica principal mejore. Sin ellos, el equipo encontrará la forma de mover el número sin crear valor.

**Lo que aporta la fuente.** Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) aporta el criterio para pesar el intercambio: los inductores de actuación frente a los indicadores de resultado (los capítulos sobre tipos de indicador). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **alineación de iniciativas** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **efecto de enfoque** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar la elección cuando cambia el modelo de negocio», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La métrica estrella corresponde a una etapa del negocio y debe revisarse cuando la etapa cambia. Una que sirvió para la fase de adopción puede ser irrelevante en la de monetización. Mantenerla por inercia produce un equipo optimizando algo que ya dejó de ser el problema.

**Frontera declarada.** Una sola métrica no describe un negocio completo. Debe acompañarse de guardarraíles que impidan optimizarla dañando margen, retención o reputación. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar north Star Metric no consiste en sumar definiciones. Empieza por **métrica estrella**, contrasta **métrica de entrada** con **correlación con ingreso**, incorpora **efecto de enfoque** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Sean Ellis y Morgan Brown — *Hacking Growth* (2017) | El momento «ajá» identificado con datos y no supuesto | Los capítulos sobre el momento de valor | ¿Qué debería observarse en **métrica estrella** si aquí opera «el momento «ajá» identificado con datos y no supuesto»? ¿Y qué observación lo desmentiría en este caso? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | La métrica que importa ahora: una sola, según etapa y modelo de negocio | Los capítulos sobre la métrica única | ¿Qué debería observarse en **métrica de entrada** si aquí opera «la métrica que importa ahora: una sola, según etapa y modelo de negocio»? ¿Y qué observación lo desmentiría en este caso? |
| John Doerr — *Measure What Matters* (2018) | El foco: pocos objetivos, con lo descartado explícito | Los capítulos sobre comprometerse con prioridades | ¿Qué debería observarse en **correlación con ingreso** si aquí opera «el foco: pocos objetivos, con lo descartado explícito»? ¿Y qué observación lo desmentiría en este caso? |
| Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) | Los inductores de actuación frente a los indicadores de resultado | Los capítulos sobre tipos de indicador | ¿Qué debería observarse en **efecto de enfoque** si aquí opera «los inductores de actuación frente a los indicadores de resultado»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina usa «cuentas registradas» como métrica principal. Las cuentas que nunca activan el módulo de pagos no producen ingreso ni permanecen.

**Paso 1 — Identificar el momento en que el cliente obtiene valor.** El equipo escribe primero el supuesto asociado a **métrica estrella** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **valor de la métrica estrella** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Proponer candidatas y verificar su correlación con ingreso.** El trabajo aquí es separar lo observado de lo inferido sobre **métrica de entrada**. La evidencia que ordena la discusión es **correlación con ingreso**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Descomponer la métrica en sus entradas.** El riesgo de este paso es cerrar demasiado rápido alrededor de **correlación con ingreso**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **alineación de iniciativas** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Declarar la elección y comunicarla.** Con **efecto de enfoque** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **valor de la métrica estrella** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar la elección cuando cambia el modelo de negocio.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **métrica estrella**. **correlación con ingreso** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **métrica estrella** | Indicador único que representa el valor entregado y guía las decisiones | Cuando **valor de la métrica estrella** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **métrica de entrada** | Componente que alimenta la métrica estrella y sobre el que se actúa | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Una sola métrica no describe un negocio completo. Debe acompañarse de guardarraíles que impidan optimizarla dañando margen, retención o reputación.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre north Star Metric |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager, Growth engineer y Head of Growth. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina usa «cuentas registradas» como métrica principal. Las cuentas que nunca activan el módulo de pagos no producen ingreso ni permanecen.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **identificar el momento en que el cliente obtiene valor → proponer candidatas y verificar su correlación con ingreso → descomponer la métrica en sus entradas → declarar la elección y comunicarla → revisar la elección cuando cambia el modelo de negocio** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **valor de la métrica estrella**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Hacking Growth* y la de *Lean Analytics*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **métrica estrella** y **métrica de entrada** como sinónimos | Se perdió la distinción entre «indicador único que representa el valor entregado y guía las decisiones» y «componente que alimenta la métrica estrella y sobre el que se actúa» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar la elección cuando cambia el modelo de negocio» | Se saltó «identificar el momento en que el cliente obtiene valor»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **valor de la métrica estrella** | La métrica local reemplazó al resultado del sistema | Contrástala con **alineación de iniciativas** y explicita el costo de oportunidad. |
| Elegir una métrica de volumen sin relación con el valor | Error específico de esta clase | Verifica la correlación con ingreso y retención antes de declarar la métrica estrella. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **métrica estrella** y **métrica de entrada** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **correlación con ingreso** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «identificar el momento en que el cliente obtiene valor» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **valor de la métrica estrella** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Una sola métrica no describe un negocio completo. Debe acompañarse de guardarraíles que impidan optimizarla dañando margen, retención o reputación»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **correlación con ingreso** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **valor de la métrica estrella**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Hacking Growth* y *The Balanced Scorecard*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P19-C02-north-star-metric/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **valor de la métrica estrella**, **correlación con ingreso** y **alineación de iniciativas** con fuente, ventana y lectura prohibida.
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

Cada obra aparece con la idea concreta que aporta a esta clase. Si al leer no encuentras esa idea, la cita está mal puesta y corresponde reportarlo como error del material.

- Sean Ellis y Morgan Brown — *Hacking Growth* (2017) — **aporta a esta clase:** el momento «ajá» identificado con datos y no supuesto. **Dónde buscarlo:** los capítulos sobre el momento de valor. Registra edición y páginas consultadas en tu nota de lectura.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — **aporta a esta clase:** la métrica que importa ahora: una sola, según etapa y modelo de negocio. **Dónde buscarlo:** los capítulos sobre la métrica única. Registra edición y páginas consultadas en tu nota de lectura.
- John Doerr — *Measure What Matters* (2018) — **aporta a esta clase:** el foco: pocos objetivos, con lo descartado explícito. **Dónde buscarlo:** los capítulos sobre comprometerse con prioridades. Registra edición y páginas consultadas en tu nota de lectura.
- Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) — **aporta a esta clase:** los inductores de actuación frente a los indicadores de resultado. **Dónde buscarlo:** los capítulos sobre tipos de indicador. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 01 · Qué es growth](class-01-que-es-growth.md) · [Índice de la parte](README.md) · [Clase 03 · AARRR](class-03-aarrr.md) →
