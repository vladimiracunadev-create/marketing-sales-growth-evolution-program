---
title: "Diseño de experimentos"
type: class
language: es
standard: clase-profunda-v2
part: 19
class: 11
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["kohavi", "provost", "laja", "wheeler-dv"]
anchors: {"kohavi": "efecto-minimo", "laja": "potencia", "provost": "evaluacion", "wheeler-dv": "variacion-comun"}
updated: 2026-08-19
---

# Clase 19.11 — Diseño de experimentos

**Parte 19 · Growth marketing y growth engineering** · Nivel: Crecimiento y analítica · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 19.10 — *ICE, RICE y priorización*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de potencia del experimento para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El efecto mínimo relevante como base del cálculo de muestra — Ron Kohavi, Diane Tang y Ya Xu. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Un experimento válido requiere hipótesis previa, asignación comparable, tamaño suficiente, duración que cubra el ciclo y métricas guardarraíl. Kohavi documenta las trampas más comunes: detención temprana, comparaciones múltiples sin corrección y contaminación entre grupos. Un experimento mal diseñado no es neutro: produce conclusiones falsas con apariencia de rigor.

El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta. La parte 19 busca **instalar un motor de experimentación que produzca aprendizaje acumulativo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **diseño de experimentos** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué bucle hace que el crecimiento se retroalimente en lugar de depender del gasto?

Los conceptos que estructuran la sesión son **asignación comparable**, **tamaño mínimo detectable**, **métrica guardarraíl** y **contaminación**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `asignación comparable`, `tamaño mínimo detectable`, `métrica guardarraíl` y `contaminación` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Growth marketing y growth engineering**.
3. **Aplicar** la secuencia **formular la hipótesis y las métricas antes de iniciar → calcular tamaño y duración necesarios → verificar la comparabilidad de los grupos → ejecutar sin detener anticipadamente → analizar con el criterio previo y documentar** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **potencia del experimento**, **experimentos detenidos anticipadamente** y **resultados replicados** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **asignación comparable** y **tamaño mínimo detectable** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **potencia del experimento**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **asignación comparable** | distribución de sujetos que hace equivalentes a los grupos | Da un hecho compatible con la definición y otro que la refute. |
| **tamaño mínimo detectable** | efecto más pequeño que el experimento puede identificar con la muestra | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **métrica guardarraíl** | indicador que no debe deteriorarse aunque mejore la métrica principal | Construye un caso límite donde el concepto se confunde con el anterior. |
| **contaminación** | situación en que el tratamiento afecta también al grupo de control | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. formular la hipótesis y las métricas antes de iniciar → 2. calcular tamaño y duración necesarios → 3. verificar la comparabilidad de los grupos → 4. ejecutar sin detener anticipadamente → 5. analizar con el criterio previo y documentar
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** En volúmenes bajos, la experimentación rigurosa es inviable. La alternativa honesta es decidir con investigación cualitativa y declarar la incertidumbre.

## 📖 Desarrollo

### 1. Asignación comparable: mecanismo central

**Asignación comparable** se entiende aquí como **distribución de sujetos que hace equivalentes a los grupos**.

Un experimento confiable exige condiciones que se incumplen con frecuencia: asignación comparable, tamaño suficiente, duración predefinida y una métrica decidida antes. Ronny Kohavi documentó que la mayoría de los problemas de experimentación no son estadísticos sino de ejecución, y por eso la lista de verificación importa más que la técnica.

**De dónde viene esta afirmación.** Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) aporta la idea que sostiene este bloque: el efecto mínimo relevante como base del cálculo de muestra. Búscala en los capítulos sobre potencia y tamaño de muestra. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «potencia del experimento» debería moverse cuando cambie **asignación comparable**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **tamaño mínimo detectable**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Tamaño mínimo detectable: frontera conceptual y error de clasificación

**Definición operacional:** efecto más pequeño que el experimento puede identificar con la muestra. Su valor está en distinguirlo de **asignación comparable**.

La asignación comparable significa que los grupos difieren sólo en el tratamiento. Se verifica con una comprobación previa: comparar los grupos en métricas anteriores al experimento. Si ya diferían, la asignación falló y cualquier diferencia posterior es ininterpretable.

**Contraste bibliográfico.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta aquí una distinción concreta: la evaluación contra una línea base y no contra la nada (los capítulos sobre evaluación de modelos). Formula dos mini-casos: uno que satisface la definición de **tamaño mínimo detectable** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «calcular tamaño y duración necesarios», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Métrica guardarraíl: operacionalización y medición

**Métrica guardarraíl** significa **indicador que no debe deteriorarse aunque mejore la métrica principal**.

El tamaño mínimo detectable se calcula a partir del efecto que justificaría actuar, no del efecto que se espera. Si el tráfico disponible no permite detectar ese efecto, la conclusión correcta es no hacer el experimento o cambiar el diseño, no ejecutarlo y confiar en el resultado.

Ficha de medición obligatoria para **potencia del experimento**: `probabilidad de detectar el efecto mínimo relevante con la muestra disponible, calculada antes de iniciar`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Peep Laja y el equipo de CXL — *Conversion Optimization Playbooks (CXL)* (2024) pone una condición sobre la medición: el cálculo de muestra y potencia antes de iniciar cualquier prueba (las guías sobre validez estadística). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Contaminación: trade-offs y efectos de segundo orden

**Definición:** situación en que el tratamiento afecta también al grupo de control.

Experimentar más rápido acelera el aprendizaje y aumenta la proporción de falsos positivos, especialmente si se detienen las pruebas al ver un resultado favorable. La disciplina de fijar duración y respetarla cuesta más de lo que parece, porque la presión por consolidar un buen resultado es constante.

**Lo que aporta la fuente.** Donald J. Wheeler — *Understanding Variation* (2000) aporta el criterio para pesar el intercambio: la distinción entre variación común y variación especial antes de reaccionar (los capítulos que introducen la distinción). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **resultados replicados** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **contaminación** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «analizar con el criterio previo y documentar», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La contaminación entre grupos —usuarios que ven ambas versiones, efectos que se transmiten entre participantes— invalida el experimento sin que sea evidente. Verificar que la unidad de asignación sea adecuada y que no exista interacción entre grupos es parte del diseño y no una consideración posterior.

**Frontera declarada.** En volúmenes bajos, la experimentación rigurosa es inviable. La alternativa honesta es decidir con investigación cualitativa y declarar la incertidumbre. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar diseño de experimentos no consiste en sumar definiciones. Empieza por **asignación comparable**, contrasta **tamaño mínimo detectable** con **métrica guardarraíl**, incorpora **contaminación** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | El efecto mínimo relevante como base del cálculo de muestra | Los capítulos sobre potencia y tamaño de muestra | ¿Qué debería observarse en **asignación comparable** si aquí opera «el efecto mínimo relevante como base del cálculo de muestra»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La evaluación contra una línea base y no contra la nada | Los capítulos sobre evaluación de modelos | ¿Qué debería observarse en **tamaño mínimo detectable** si aquí opera «la evaluación contra una línea base y no contra la nada»? ¿Y qué observación lo desmentiría en este caso? |
| Peep Laja y el equipo de CXL — *Conversion Optimization Playbooks (CXL)* (2024) | El cálculo de muestra y potencia antes de iniciar cualquier prueba | Las guías sobre validez estadística | ¿Qué debería observarse en **métrica guardarraíl** si aquí opera «el cálculo de muestra y potencia antes de iniciar cualquier prueba»? ¿Y qué observación lo desmentiría en este caso? |
| Donald J. Wheeler — *Understanding Variation* (2000) | La distinción entre variación común y variación especial antes de reaccionar | Los capítulos que introducen la distinción | ¿Qué debería observarse en **contaminación** si aquí opera «la distinción entre variación común y variación especial antes de reaccionar»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina declaró ganadora una variante tras cuatro días con 120 usuarios por grupo. El efecto desapareció al mes siguiente.

**Paso 1 — Formular la hipótesis y las métricas antes de iniciar.** El equipo escribe primero el supuesto asociado a **asignación comparable** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **potencia del experimento** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Calcular tamaño y duración necesarios.** El trabajo aquí es separar lo observado de lo inferido sobre **tamaño mínimo detectable**. La evidencia que ordena la discusión es **experimentos detenidos anticipadamente**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Verificar la comparabilidad de los grupos.** El riesgo de este paso es cerrar demasiado rápido alrededor de **métrica guardarraíl**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **resultados replicados** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Ejecutar sin detener anticipadamente.** Con **contaminación** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **potencia del experimento** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Analizar con el criterio previo y documentar.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **asignación comparable**. **experimentos detenidos anticipadamente** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **asignación comparable** | Distribución de sujetos que hace equivalentes a los grupos | Cuando **potencia del experimento** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **tamaño mínimo detectable** | Efecto más pequeño que el experimento puede identificar con la muestra | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** En volúmenes bajos, la experimentación rigurosa es inviable. La alternativa honesta es decidir con investigación cualitativa y declarar la incertidumbre.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre diseño de experimentos |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager, Growth engineer y Head of Growth. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina declaró ganadora una variante tras cuatro días con 120 usuarios por grupo. El efecto desapareció al mes siguiente.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **formular la hipótesis y las métricas antes de iniciar → calcular tamaño y duración necesarios → verificar la comparabilidad de los grupos → ejecutar sin detener anticipadamente → analizar con el criterio previo y documentar** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **potencia del experimento**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Trustworthy Online Controlled Experiments* y la de *Data Science for Business*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **asignación comparable** y **tamaño mínimo detectable** como sinónimos | Se perdió la distinción entre «distribución de sujetos que hace equivalentes a los grupos» y «efecto más pequeño que el experimento puede identificar con la muestra» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «analizar con el criterio previo y documentar» | Se saltó «formular la hipótesis y las métricas antes de iniciar»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **potencia del experimento** | La métrica local reemplazó al resultado del sistema | Contrástala con **resultados replicados** y explicita el costo de oportunidad. |
| Detener el experimento al ver un resultado favorable | Error específico de esta clase | Fija duración y tamaño antes de iniciar y analiza sólo al finalizar el plazo definido. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **asignación comparable** y **tamaño mínimo detectable** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **métrica guardarraíl** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «formular la hipótesis y las métricas antes de iniciar» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **potencia del experimento** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «En volúmenes bajos, la experimentación rigurosa es inviable. La alternativa honesta es decidir con investigación cualitativa y declarar la incertidumbre»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **métrica guardarraíl** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **potencia del experimento**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Trustworthy Online Controlled Experiments* y *Understanding Variation*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P19-C11-experiment-design/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **potencia del experimento**, **experimentos detenidos anticipadamente** y **resultados replicados** con fuente, ventana y lectura prohibida.
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

- Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) — **aporta a esta clase:** el efecto mínimo relevante como base del cálculo de muestra. **Dónde buscarlo:** los capítulos sobre potencia y tamaño de muestra. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — **aporta a esta clase:** la evaluación contra una línea base y no contra la nada. **Dónde buscarlo:** los capítulos sobre evaluación de modelos. Registra edición y páginas consultadas en tu nota de lectura.
- Peep Laja y el equipo de CXL — *Conversion Optimization Playbooks (CXL)* (2024) — **aporta a esta clase:** el cálculo de muestra y potencia antes de iniciar cualquier prueba. **Dónde buscarlo:** las guías sobre validez estadística. Registra edición y páginas consultadas en tu nota de lectura.
- Donald J. Wheeler — *Understanding Variation* (2000) — **aporta a esta clase:** la distinción entre variación común y variación especial antes de reaccionar. **Dónde buscarlo:** los capítulos que introducen la distinción. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 10 · ICE, RICE y priorización](class-10-ice-rice-y-priorizacion.md) · [Índice de la parte](README.md) · [Clase 12 · Growth engineering](class-12-growth-engineering.md) →
