---
title: "Lead scoring"
type: class
language: es
standard: clase-profunda-v2
part: 17
class: 03
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["provost", "roberge", "diorio", "oneil"]
anchors: {"diorio": "modelo-datos", "oneil": "proxy", "provost": "evaluacion", "roberge": "metricas-coaching"}
updated: 2026-08-19
---

# Clase 17.03 — Lead scoring

**Parte 17 · Marketing automation y revenue operations** · Nivel: Operación de ingresos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 17.02 — *Etapas de ciclo de vida*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de conversión por tramo de puntaje para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La evaluación contra una línea base y no contra la nada — Foster Provost y Tom Fawcett. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Un modelo de puntuación estima la probabilidad de que un contacto se convierta en cliente. Su utilidad depende de que combine ajuste de perfil y señal de comportamiento, y de que se valide contra resultados reales. Un modelo construido con opiniones del equipo y nunca contrastado produce puntajes que nadie usa y una falsa sensación de rigor.

Antes de cualquier herramienta, esta clase obliga a nombrar qué cambiaría si el análisis fuese correcto. La parte 17 busca **integrar marketing, ventas y servicio en un solo modelo de datos y de proceso**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **lead scoring** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué automatizo porque mejora el sistema y qué estaría solo escalando un desorden?

Los conceptos que estructuran la sesión son **puntaje de ajuste**, **puntaje de comportamiento**, **validación del modelo** y **decaimiento**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `puntaje de ajuste`, `puntaje de comportamiento`, `validación del modelo` y `decaimiento` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Marketing automation y revenue operations**.
3. **Aplicar** la secuencia **definir los componentes de ajuste y de comportamiento → asignar pesos derivados de datos históricos → aplicar decaimiento por inactividad → validar contra conversión real cada trimestre → recalibrar y documentar los cambios** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **conversión por tramo de puntaje**, **capacidad discriminante** y **uso del puntaje por ventas** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **puntaje de ajuste** y **puntaje de comportamiento** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **conversión por tramo de puntaje**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **puntaje de ajuste** | componente que evalúa la correspondencia con el perfil de cliente ideal | Construye un caso límite donde el concepto se confunde con el anterior. |
| **puntaje de comportamiento** | componente que evalúa señales de interés y de intención | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **validación del modelo** | contraste entre el puntaje asignado y la conversión efectiva | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **decaimiento** | reducción del puntaje por inactividad, que evita puntajes eternos | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir los componentes de ajuste y de comportamiento → 2. asignar pesos derivados de datos históricos → 3. aplicar decaimiento por inactividad → 4. validar contra conversión real cada trimestre → 5. recalibrar y documentar los cambios
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Los modelos aprenden del histórico y reproducen sus sesgos. Si la prospección pasada ignoró un segmento, el modelo seguirá subvalorándolo.

## 📖 Desarrollo

### 1. Puntaje de ajuste: mecanismo central

**Puntaje de ajuste** se entiende aquí como **componente que evalúa la correspondencia con el perfil de cliente ideal**.

El puntaje de leads intenta responder a quién atender primero. Su utilidad depende por completo de que se valide contra resultados reales: si los leads con puntaje alto no convierten mejor que los de puntaje bajo, el modelo no está informando nada y su uso es peor que no tener modelo, porque transmite falsa confianza.

**De dónde viene esta afirmación.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta la idea que sostiene este bloque: la evaluación contra una línea base y no contra la nada. Búscala en los capítulos sobre evaluación de modelos. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «conversión por tramo de puntaje» debería moverse cuando cambie **puntaje de ajuste**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **puntaje de comportamiento**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Puntaje de comportamiento: frontera conceptual y error de clasificación

**Definición operacional:** componente que evalúa señales de interés y de intención. Su valor está en distinguirlo de **puntaje de ajuste**.

El puntaje de ajuste y el de comportamiento miden cosas distintas y deben mantenerse separados. El ajuste describe si la organización corresponde al perfil; el comportamiento, si hay señales de interés activo. Una empresa perfecta sin actividad y una empresa fuera de perfil muy activa requieren tratamientos opuestos, y un puntaje único los confunde.

**Contraste bibliográfico.** Mark Roberge — *The Sales Acceleration Formula* (2015) aporta aquí una distinción concreta: el acompañamiento dirigido por una métrica diagnóstica por vendedor (los capítulos sobre la fórmula de gestión). Formula dos mini-casos: uno que satisface la definición de **puntaje de comportamiento** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «asignar pesos derivados de datos históricos», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Validación del modelo: operacionalización y medición

**Validación del modelo** significa **contraste entre el puntaje asignado y la conversión efectiva**.

La validación se hace comparando la tasa de conversión real por tramo de puntaje. Si los tramos no se separan, el modelo no discrimina. Esa verificación debe repetirse periódicamente porque el comportamiento cambia: un modelo validado hace dos años puede haber dejado de funcionar sin que nadie lo note.

Ficha de medición obligatoria para **conversión por tramo de puntaje**: `clientes ganados, sobre leads de cada tramo de puntaje`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) pone una condición sobre la medición: el modelo de datos común como condición para que las áreas discutan sobre lo mismo (los capítulos sobre infraestructura de datos comercial). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Decaimiento: trade-offs y efectos de segundo orden

**Definición:** reducción del puntaje por inactividad, que evita puntajes eternos.

Un modelo más complejo puede capturar mejor las señales y se vuelve imposible de explicar al equipo comercial, que entonces lo ignora. Uno simple se entiende y se usa, aunque discrimine algo menos. En la práctica, un modelo simple que el equipo comprende suele producir mejores resultados que uno sofisticado que nadie cree.

**Lo que aporta la fuente.** Cathy O'Neil — *Weapons of Math Destruction* (2016) aporta el criterio para pesar el intercambio: las variables sustitutas que codifican prejuicio sin nombrarlo (los capítulos sobre selección de variables). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **uso del puntaje por ventas** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **decaimiento** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «recalibrar y documentar los cambios», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Un modelo entrenado con datos históricos reproduce los sesgos de la operación pasada: si históricamente sólo se atendió a cierto tipo de cuenta, el modelo aprenderá que ese tipo convierte. Esa retroalimentación puede cerrar el mercado sin que nadie lo decida. Revisar qué segmentos quedan sistemáticamente con puntaje bajo es un control necesario.

**Frontera declarada.** Los modelos aprenden del histórico y reproducen sus sesgos. Si la prospección pasada ignoró un segmento, el modelo seguirá subvalorándolo. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar lead scoring no consiste en sumar definiciones. Empieza por **puntaje de ajuste**, contrasta **puntaje de comportamiento** con **validación del modelo**, incorpora **decaimiento** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La evaluación contra una línea base y no contra la nada | Los capítulos sobre evaluación de modelos | ¿Qué debería observarse en **puntaje de ajuste** si aquí opera «la evaluación contra una línea base y no contra la nada»? ¿Y qué observación lo desmentiría en este caso? |
| Mark Roberge — *The Sales Acceleration Formula* (2015) | El acompañamiento dirigido por una métrica diagnóstica por vendedor | Los capítulos sobre la fórmula de gestión | ¿Qué debería observarse en **puntaje de comportamiento** si aquí opera «el acompañamiento dirigido por una métrica diagnóstica por vendedor»? ¿Y qué observación lo desmentiría en este caso? |
| Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) | El modelo de datos común como condición para que las áreas discutan sobre lo mismo | Los capítulos sobre infraestructura de datos comercial | ¿Qué debería observarse en **validación del modelo** si aquí opera «el modelo de datos común como condición para que las áreas discutan sobre lo mismo»? ¿Y qué observación lo desmentiría en este caso? |
| Cathy O'Neil — *Weapons of Math Destruction* (2016) | Las variables sustitutas que codifican prejuicio sin nombrarlo | Los capítulos sobre selección de variables | ¿Qué debería observarse en **decaimiento** si aquí opera «las variables sustitutas que codifican prejuicio sin nombrarlo»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El modelo de Ruta Andina asigna 30 puntos por abrir tres correos y 10 por pertenecer al rubro objetivo. Los leads de mayor puntaje convierten igual que el promedio.

**Paso 1 — Definir los componentes de ajuste y de comportamiento.** El equipo escribe primero el supuesto asociado a **puntaje de ajuste** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **conversión por tramo de puntaje** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Asignar pesos derivados de datos históricos.** El trabajo aquí es separar lo observado de lo inferido sobre **puntaje de comportamiento**. La evidencia que ordena la discusión es **capacidad discriminante**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Aplicar decaimiento por inactividad.** El riesgo de este paso es cerrar demasiado rápido alrededor de **validación del modelo**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **uso del puntaje por ventas** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Validar contra conversión real cada trimestre.** Con **decaimiento** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **conversión por tramo de puntaje** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Recalibrar y documentar los cambios.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **puntaje de ajuste**. **capacidad discriminante** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **puntaje de ajuste** | Componente que evalúa la correspondencia con el perfil de cliente ideal | Cuando **conversión por tramo de puntaje** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **puntaje de comportamiento** | Componente que evalúa señales de interés y de intención | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Los modelos aprenden del histórico y reproducen sus sesgos. Si la prospección pasada ignoró un segmento, el modelo seguirá subvalorándolo.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre lead scoring |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing ops, RevOps manager y Sales ops. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El modelo de Ruta Andina asigna 30 puntos por abrir tres correos y 10 por pertenecer al rubro objetivo. Los leads de mayor puntaje convierten igual que el promedio.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir los componentes de ajuste y de comportamiento → asignar pesos derivados de datos históricos → aplicar decaimiento por inactividad → validar contra conversión real cada trimestre → recalibrar y documentar los cambios** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **conversión por tramo de puntaje**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Data Science for Business* y la de *The Sales Acceleration Formula*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **puntaje de ajuste** y **puntaje de comportamiento** como sinónimos | Se perdió la distinción entre «componente que evalúa la correspondencia con el perfil de cliente ideal» y «componente que evalúa señales de interés y de intención» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «recalibrar y documentar los cambios» | Se saltó «definir los componentes de ajuste y de comportamiento»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **conversión por tramo de puntaje** | La métrica local reemplazó al resultado del sistema | Contrástala con **uso del puntaje por ventas** y explicita el costo de oportunidad. |
| No validar el modelo contra conversión real | Error específico de esta clase | Compara la conversión por tramo de puntaje cada trimestre y recalibra los pesos. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **puntaje de ajuste** y **puntaje de comportamiento** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **validación del modelo** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir los componentes de ajuste y de comportamiento» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **conversión por tramo de puntaje** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Los modelos aprenden del histórico y reproducen sus sesgos. Si la prospección pasada ignoró un segmento, el modelo seguirá subvalorándolo»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **validación del modelo** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **conversión por tramo de puntaje**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Data Science for Business* y *Weapons of Math Destruction*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P17-C03-lead-scoring/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **conversión por tramo de puntaje**, **capacidad discriminante** y **uso del puntaje por ventas** con fuente, ventana y lectura prohibida.
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

- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — **aporta a esta clase:** la evaluación contra una línea base y no contra la nada. **Dónde buscarlo:** los capítulos sobre evaluación de modelos. Registra edición y páginas consultadas en tu nota de lectura.
- Mark Roberge — *The Sales Acceleration Formula* (2015) — **aporta a esta clase:** el acompañamiento dirigido por una métrica diagnóstica por vendedor. **Dónde buscarlo:** los capítulos sobre la fórmula de gestión. Registra edición y páginas consultadas en tu nota de lectura.
- Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) — **aporta a esta clase:** el modelo de datos común como condición para que las áreas discutan sobre lo mismo. **Dónde buscarlo:** los capítulos sobre infraestructura de datos comercial. Registra edición y páginas consultadas en tu nota de lectura.
- Cathy O'Neil — *Weapons of Math Destruction* (2016) — **aporta a esta clase:** las variables sustitutas que codifican prejuicio sin nombrarlo. **Dónde buscarlo:** los capítulos sobre selección de variables. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 02 · Etapas de ciclo de vida](class-02-lifecycle-stages.md) · [Índice de la parte](README.md) · [Clase 04 · Enrutamiento de leads](class-04-lead-routing.md) →
