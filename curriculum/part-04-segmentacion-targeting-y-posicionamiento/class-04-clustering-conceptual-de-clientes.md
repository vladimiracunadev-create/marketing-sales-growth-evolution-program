---
title: "Clustering conceptual de clientes"
type: class
language: es
standard: clase-profunda-v2
part: 04
class: 04
level: Fundamentos
mastery_threshold: 80
estimated_minutes: 150
sources: ["provost", "fader", "croll-yoskovitz", "kaushik"]
anchors: {"croll-yoskovitz": "cohortes", "fader": "rfm", "kaushik": "segmentacion", "provost": "sobreajuste"}
updated: 2026-08-19
---

# Clase 04.04 — Clustering conceptual de clientes

**Parte 04 · Segmentación, targeting y posicionamiento** · Nivel: Fundamentos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 04.03 — *Variables de segmentación B2B*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de cohesión y separación para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El sobreajuste y la validación fuera de muestra — Foster Provost y Tom Fawcett. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Agrupar clientes por similitud es una técnica poderosa y fácil de mal usar. El algoritmo siempre devuelve grupos, incluso cuando no existen. La utilidad depende de tres decisiones humanas: qué variables entran, cómo se escalan y qué significa cada grupo en términos de negocio. Un cluster que no puede describirse en una frase accionable no sirve, aunque sea estadísticamente impecable.

El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta. La parte 04 busca **elegir a quién servir y ocupar un lugar defendible en la mente del cliente**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **clustering conceptual de clientes** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué segmento puedo servir mejor que nadie y con qué diferencia comprobable?

Los conceptos que estructuran la sesión son **variable de entrada**, **cohesión del grupo**, **interpretabilidad** y **estabilidad temporal**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `variable de entrada`, `cohesión del grupo`, `interpretabilidad` y `estabilidad temporal` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Segmentación, targeting y posicionamiento**.
3. **Aplicar** la secuencia **elegir variables con justificación de negocio → normalizar escalas y documentar el criterio → generar agrupaciones y evaluar cohesión → describir cada grupo con una regla accionable → verificar estabilidad en un periodo distinto** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **cohesión y separación**, **estabilidad entre periodos** y **diferencia de valor entre grupos** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **variable de entrada** y **cohesión del grupo** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **cohesión y separación**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **variable de entrada** | atributo incluido en el agrupamiento, cuya escala condiciona el resultado | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **cohesión del grupo** | grado en que los miembros de un grupo se parecen entre sí más que a los de otros grupos | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **interpretabilidad** | posibilidad de describir el grupo con una regla de negocio comprensible | Da un hecho compatible con la definición y otro que la refute. |
| **estabilidad temporal** | permanencia de la estructura de grupos al repetir el análisis en otro periodo | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. elegir variables con justificación de negocio → 2. normalizar escalas y documentar el criterio → 3. generar agrupaciones y evaluar cohesión → 4. describir cada grupo con una regla accionable → 5. verificar estabilidad en un periodo distinto
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** El agrupamiento describe, no explica. No indica causa ni predice respuesta a un tratamiento: para eso hace falta experimentación.

## 📖 Desarrollo

### 1. Variable de entrada: mecanismo central

**Variable de entrada** se entiende aquí como **atributo incluido en el agrupamiento, cuya escala condiciona el resultado**.

Agrupar clientes por comportamiento es útil cuando el resultado es interpretable. Un algoritmo puede producir cinco grupos matemáticamente óptimos e imposibles de describir en una frase, y un grupo que nadie puede describir es un grupo que nadie puede atender. En análisis comercial, la interpretabilidad no es una concesión: es un requisito de utilidad.

**De dónde viene esta afirmación.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta la idea que sostiene este bloque: el sobreajuste y la validación fuera de muestra. Búscala en los capítulos sobre sobreajuste. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «cohesión y separación» debería moverse cuando cambie **variable de entrada**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **cohesión del grupo**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Cohesión del grupo: frontera conceptual y error de clasificación

**Definición operacional:** grado en que los miembros de un grupo se parecen entre sí más que a los de otros grupos. Su valor está en distinguirlo de **variable de entrada**.

La cohesión del grupo y su separación de los demás son dos propiedades distintas y ambas importan. Un conjunto compacto pero solapado con otro no permite decidir a cuál pertenece un cliente nuevo. Antes de operar la segmentación conviene verificar cuántos clientes quedan en zona ambigua: si son muchos, el modelo describe un continuo que se está partiendo artificialmente.

**Contraste bibliográfico.** Peter Fader — *Customer Centricity* (2020, 2.ª ed.) aporta aquí una distinción concreta: recencia, frecuencia y valor como base de segmentación conductual (los capítulos sobre segmentación por comportamiento). Formula dos mini-casos: uno que satisface la definición de **cohesión del grupo** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «normalizar escalas y documentar el criterio», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Interpretabilidad: operacionalización y medición

**Interpretabilidad** significa **posibilidad de describir el grupo con una regla de negocio comprensible**.

La estabilidad temporal se verifica corriendo el mismo procedimiento sobre dos periodos y midiendo cuántos clientes cambian de grupo. Una rotación alta no invalida el modelo pero cambia su uso: sirve para describir el momento, no para asignar tratamientos de largo plazo. Documentar esa rotación evita que el equipo construya programas anuales sobre grupos que duran un trimestre.

Ficha de medición obligatoria para **cohesión y separación**: `medida de distancia intragrupo frente a distancia entre grupos`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) pone una condición sobre la medición: el análisis de cohortes como corrección al promedio que esconde la mezcla (el capítulo sobre cohortes y segmentación). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Estabilidad temporal: trade-offs y efectos de segundo orden

**Definición:** permanencia de la estructura de grupos al repetir el análisis en otro periodo.

Incluir más variables mejora el ajuste dentro de la muestra y aumenta el riesgo de capturar ruido que no se repetirá. Es el problema clásico del sobreajuste, y en segmentación aparece disfrazado de riqueza analítica. La contención práctica es reservar un periodo de datos que no se usa para construir y comprobar allí si los grupos se sostienen.

**Lo que aporta la fuente.** Avinash Kaushik — *Web Analytics 2.0* (2009) aporta el criterio para pesar el intercambio: la segmentación como condición para que un promedio signifique algo (el capítulo sobre segmentación de datos). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **diferencia de valor entre grupos** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **estabilidad temporal** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «verificar estabilidad en un periodo distinto», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El agrupamiento describe patrones en los datos disponibles, y los datos disponibles reflejan cómo la empresa ha operado hasta ahora. Si históricamente sólo se prospectó un tipo de cliente, ningún algoritmo descubrirá el segmento que nunca se contactó. El método encuentra estructura en lo que hay, no oportunidades en lo que falta.

**Frontera declarada.** El agrupamiento describe, no explica. No indica causa ni predice respuesta a un tratamiento: para eso hace falta experimentación. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Segmentar con variables decorativas que no cambian oferta, canal ni mensaje.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar clustering conceptual de clientes no consiste en sumar definiciones. Empieza por **variable de entrada**, contrasta **cohesión del grupo** con **interpretabilidad**, incorpora **estabilidad temporal** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | El sobreajuste y la validación fuera de muestra | Los capítulos sobre sobreajuste | ¿Qué debería observarse en **variable de entrada** si aquí opera «el sobreajuste y la validación fuera de muestra»? ¿Y qué observación lo desmentiría en este caso? |
| Peter Fader — *Customer Centricity* (2020, 2.ª ed.) | Recencia, frecuencia y valor como base de segmentación conductual | Los capítulos sobre segmentación por comportamiento | ¿Qué debería observarse en **cohesión del grupo** si aquí opera «recencia, frecuencia y valor como base de segmentación conductual»? ¿Y qué observación lo desmentiría en este caso? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | El análisis de cohortes como corrección al promedio que esconde la mezcla | El capítulo sobre cohortes y segmentación | ¿Qué debería observarse en **interpretabilidad** si aquí opera «el análisis de cohortes como corrección al promedio que esconde la mezcla»? ¿Y qué observación lo desmentiría en este caso? |
| Avinash Kaushik — *Web Analytics 2.0* (2009) | La segmentación como condición para que un promedio signifique algo | El capítulo sobre segmentación de datos | ¿Qué debería observarse en **estabilidad temporal** si aquí opera «la segmentación como condición para que un promedio signifique algo»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Un análisis entrega cinco clusters de clientes de Ruta Andina. Tres son indistinguibles en comportamiento comercial y ninguno puede describirse sin recurrir a coordenadas del modelo.

**Paso 1 — Elegir variables con justificación de negocio.** El equipo escribe primero el supuesto asociado a **variable de entrada** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **cohesión y separación** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Normalizar escalas y documentar el criterio.** El trabajo aquí es separar lo observado de lo inferido sobre **cohesión del grupo**. La evidencia que ordena la discusión es **estabilidad entre periodos**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Generar agrupaciones y evaluar cohesión.** El riesgo de este paso es cerrar demasiado rápido alrededor de **interpretabilidad**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **diferencia de valor entre grupos** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Describir cada grupo con una regla accionable.** Con **estabilidad temporal** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **cohesión y separación** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Verificar estabilidad en un periodo distinto.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **variable de entrada**. **estabilidad entre periodos** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **variable de entrada** | Atributo incluido en el agrupamiento, cuya escala condiciona el resultado | Cuando **cohesión y separación** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **cohesión del grupo** | Grado en que los miembros de un grupo se parecen entre sí más que a los de otros grupos | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** El agrupamiento describe, no explica. No indica causa ni predice respuesta a un tratamiento: para eso hace falta experimentación.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre clustering conceptual de clientes |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing manager, Product marketing y Head of Growth. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Un análisis entrega cinco clusters de clientes de Ruta Andina. Tres son indistinguibles en comportamiento comercial y ninguno puede describirse sin recurrir a coordenadas del modelo.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **elegir variables con justificación de negocio → normalizar escalas y documentar el criterio → generar agrupaciones y evaluar cohesión → describir cada grupo con una regla accionable → verificar estabilidad en un periodo distinto** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **cohesión y separación**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Data Science for Business* y la de *Customer Centricity*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **variable de entrada** y **cohesión del grupo** como sinónimos | Se perdió la distinción entre «atributo incluido en el agrupamiento, cuya escala condiciona el resultado» y «grado en que los miembros de un grupo se parecen entre sí más que a los de otros grupos» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «verificar estabilidad en un periodo distinto» | Se saltó «elegir variables con justificación de negocio»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **cohesión y separación** | La métrica local reemplazó al resultado del sistema | Contrástala con **diferencia de valor entre grupos** y explicita el costo de oportunidad. |
| Aceptar grupos que no se pueden describir en lenguaje de negocio | Error específico de esta clase | Exige una regla verbal por grupo; si no existe, revisa las variables de entrada. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **variable de entrada** y **cohesión del grupo** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **interpretabilidad** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «elegir variables con justificación de negocio» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **cohesión y separación** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «El agrupamiento describe, no explica. No indica causa ni predice respuesta a un tratamiento: para eso hace falta experimentación»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **interpretabilidad** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **cohesión y separación**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Data Science for Business* y *Web Analytics 2.0*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Segmentar con variables decorativas que no cambian oferta, canal ni mensaje.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P04-C04-clustering-conceptual-de-clientes/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **cohesión y separación**, **estabilidad entre periodos** y **diferencia de valor entre grupos** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **arquitectura STP con criterios de atractivo, accesibilidad y declaración de posicionamiento probada**.

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

- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — **aporta a esta clase:** el sobreajuste y la validación fuera de muestra. **Dónde buscarlo:** los capítulos sobre sobreajuste. Registra edición y páginas consultadas en tu nota de lectura.
- Peter Fader — *Customer Centricity* (2020, 2.ª ed.) — **aporta a esta clase:** recencia, frecuencia y valor como base de segmentación conductual. **Dónde buscarlo:** los capítulos sobre segmentación por comportamiento. Registra edición y páginas consultadas en tu nota de lectura.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — **aporta a esta clase:** el análisis de cohortes como corrección al promedio que esconde la mezcla. **Dónde buscarlo:** el capítulo sobre cohortes y segmentación. Registra edición y páginas consultadas en tu nota de lectura.
- Avinash Kaushik — *Web Analytics 2.0* (2009) — **aporta a esta clase:** la segmentación como condición para que un promedio signifique algo. **Dónde buscarlo:** el capítulo sobre segmentación de datos. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 03 · Variables de segmentación B2B](class-03-variables-de-segmentacion-b2b.md) · [Índice de la parte](README.md) · [Clase 05 · Atractivo y accesibilidad de segmentos](class-05-atractivo-y-accesibilidad-de-segmentos.md) →
