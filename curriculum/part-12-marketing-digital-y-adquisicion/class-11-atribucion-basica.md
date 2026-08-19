---
title: "Atribución básica"
type: class
language: es
standard: clase-profunda-v2
part: 12
class: 11
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["kaushik", "kohavi", "provost", "binet-field"]
anchors: {"binet-field": "corto-largo", "kaushik": "multiplicidad", "kohavi": "metricas-sustitutas", "provost": "asociacion-causalidad"}
updated: 2026-08-19
---

# Clase 12.11 — Atribución básica

**Parte 12 · Marketing digital y adquisición** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 12.10 — *Analítica digital*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de diferencia de crédito entre modelos para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La multiplicidad: combinar clics, resultados, experiencia y competencia — Avinash Kaushik. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La atribución intenta repartir el crédito de una conversión entre los puntos de contacto que la precedieron. Todos los modelos —último clic, primer clic, lineal, decaimiento— son convenciones, no verdades. El último clic sobrevalora los canales de captura de intención y subvalora los que crean demanda. La conclusión práctica es usar la atribución para ordenar la conversación y la incrementalidad para decidir presupuesto.

El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta. La parte 12 busca **operar un sistema digital de adquisición medible de punta a punta**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **atribución básica** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué activo digital genera demanda propia y qué parte del resultado es alquilada?

Los conceptos que estructuran la sesión son **modelo de atribución**, **sesgo del último clic**, **ventana de atribución** y **incrementalidad**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `modelo de atribución`, `sesgo del último clic`, `ventana de atribución` y `incrementalidad` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Marketing digital y adquisición**.
3. **Aplicar** la secuencia **documentar el modelo y la ventana utilizados → comparar resultados bajo dos modelos distintos → identificar los canales cuyo valor cambia según el modelo → diseñar una prueba de incrementalidad para los casos críticos → decidir presupuesto con evidencia causal donde el monto lo justifique** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **diferencia de crédito entre modelos**, **cobertura de la atribución** y **resultado de pruebas de incrementalidad** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **modelo de atribución** y **sesgo del último clic** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **diferencia de crédito entre modelos**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **modelo de atribución** | regla convencional que reparte el crédito de la conversión entre puntos de contacto | Da un hecho compatible con la definición y otro que la refute. |
| **sesgo del último clic** | sobrevaloración del canal más cercano a la conversión | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **ventana de atribución** | periodo dentro del cual un contacto se considera contribuyente | Construye un caso límite donde el concepto se confunde con el anterior. |
| **incrementalidad** | efecto causal real de un canal, estimado con grupo de comparación | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. documentar el modelo y la ventana utilizados → 2. comparar resultados bajo dos modelos distintos → 3. identificar los canales cuyo valor cambia según el modelo → 4. diseñar una prueba de incrementalidad para los casos críticos → 5. decidir presupuesto con evidencia causal donde el monto lo justifique
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Ningún modelo de atribución establece causalidad. Con presupuestos pequeños, el costo de una prueba de incrementalidad puede superar su beneficio.

## 📖 Desarrollo

### 1. Modelo de atribución: mecanismo central

**Modelo de atribución** se entiende aquí como **regla convencional que reparte el crédito de la conversión entre puntos de contacto**.

La atribución intenta responder qué contribuyó al resultado, y ninguna respuesta es exacta. Los modelos basados en reglas —último clic, primer clic, lineal— son convenciones, no descubrimientos. Elegir uno significa decidir qué sesgo se acepta, y esa decisión debe ser consciente y estar documentada.

**De dónde viene esta afirmación.** Avinash Kaushik — *Web Analytics 2.0* (2009) aporta la idea que sostiene este bloque: la multiplicidad: combinar clics, resultados, experiencia y competencia. Búscala en los capítulos sobre analítica multicanal. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «diferencia de crédito entre modelos» debería moverse cuando cambie **modelo de atribución**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **sesgo del último clic**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Sesgo del último clic: frontera conceptual y error de clasificación

**Definición operacional:** sobrevaloración del canal más cercano a la conversión. Su valor está en distinguirlo de **modelo de atribución**.

El sesgo del último clic favorece sistemáticamente a los canales de cierre y castiga a los de descubrimiento. Como es el modelo por defecto en la mayoría de las herramientas, produce una reasignación gradual de presupuesto hacia la captura de demanda existente, que se justifica con datos y erosiona la generación de demanda futura.

**Contraste bibliográfico.** Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) aporta aquí una distinción concreta: los riesgos de optimizar una métrica sustituta en lugar del resultado (los capítulos sobre selección de métricas). Formula dos mini-casos: uno que satisface la definición de **sesgo del último clic** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «comparar resultados bajo dos modelos distintos», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Ventana de atribución: operacionalización y medición

**Ventana de atribución** significa **periodo dentro del cual un contacto se considera contribuyente**.

La ventana de atribución debe fijarse según el ciclo de compra real y no según el valor por defecto de la herramienta. En un negocio con ciclo de tres meses, una ventana de treinta días deja fuera la mayor parte de las interacciones relevantes y produce una imagen sistemáticamente incompleta.

Ficha de medición obligatoria para **diferencia de crédito entre modelos**: `variación del crédito asignado a cada canal según el modelo aplicado`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) pone una condición sobre la medición: la distinción entre correlación observada y causalidad y qué exige cada una (los capítulos sobre inferencia y sesgo). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Incrementalidad: trade-offs y efectos de segundo orden

**Definición:** efecto causal real de un canal, estimado con grupo de comparación.

Modelos más sofisticados capturan mejor la contribución y son más difíciles de explicar y de auditar. Un modelo que nadie entiende no se usa para decidir o se usa sin cuestionarlo, y ambas salidas son malas. La complejidad debe justificarse con una mejora demostrable en la decisión, no con su sofisticación.

**Lo que aporta la fuente.** Les Binet y Peter Field — *The Long and the Short of It* (2013) aporta el criterio para pesar el intercambio: los efectos de corto plazo decaen; los de marca se acumulan y bajan la elasticidad de precio (los capítulos sobre curvas de respuesta en el tiempo). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **resultado de pruebas de incrementalidad** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **incrementalidad** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «decidir presupuesto con evidencia causal donde el monto lo justifique», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La atribución mide asociación entre contactos y resultados; la incrementalidad mide causa. Sólo un diseño experimental —suspender un canal en un grupo comparable— responde qué habría pasado sin esa inversión. Cuando la decisión es de presupuesto significativo, la atribución no basta.

**Frontera declarada.** Ningún modelo de atribución establece causalidad. Con presupuestos pequeños, el costo de una prueba de incrementalidad puede superar su beneficio. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Optimizar métricas de vanidad y desatender consentimiento, cookies y datos personales.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar atribución básica no consiste en sumar definiciones. Empieza por **modelo de atribución**, contrasta **sesgo del último clic** con **ventana de atribución**, incorpora **incrementalidad** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Avinash Kaushik — *Web Analytics 2.0* (2009) | La multiplicidad: combinar clics, resultados, experiencia y competencia | Los capítulos sobre analítica multicanal | ¿Qué debería observarse en **modelo de atribución** si aquí opera «la multiplicidad: combinar clics, resultados, experiencia y competencia»? ¿Y qué observación lo desmentiría en este caso? |
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | Los riesgos de optimizar una métrica sustituta en lugar del resultado | Los capítulos sobre selección de métricas | ¿Qué debería observarse en **sesgo del último clic** si aquí opera «los riesgos de optimizar una métrica sustituta en lugar del resultado»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La distinción entre correlación observada y causalidad y qué exige cada una | Los capítulos sobre inferencia y sesgo | ¿Qué debería observarse en **ventana de atribución** si aquí opera «la distinción entre correlación observada y causalidad y qué exige cada una»? ¿Y qué observación lo desmentiría en este caso? |
| Les Binet y Peter Field — *The Long and the Short of It* (2013) | Los efectos de corto plazo decaen; los de marca se acumulan y bajan la elasticidad de precio | Los capítulos sobre curvas de respuesta en el tiempo | ¿Qué debería observarse en **incrementalidad** si aquí opera «los efectos de corto plazo decaen; los de marca se acumulan y bajan la elasticidad de precio»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Bajo último clic, la búsqueda de marca recibe el 61 % del crédito en Ruta Andina. Bajo primer clic, el contenido orgánico recibe el 44 %. El presupuesto se asigna con el primero.

**Paso 1 — Documentar el modelo y la ventana utilizados.** El equipo escribe primero el supuesto asociado a **modelo de atribución** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **diferencia de crédito entre modelos** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Comparar resultados bajo dos modelos distintos.** El trabajo aquí es separar lo observado de lo inferido sobre **sesgo del último clic**. La evidencia que ordena la discusión es **cobertura de la atribución**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Identificar los canales cuyo valor cambia según el modelo.** El riesgo de este paso es cerrar demasiado rápido alrededor de **ventana de atribución**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **resultado de pruebas de incrementalidad** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Diseñar una prueba de incrementalidad para los casos críticos.** Con **incrementalidad** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **diferencia de crédito entre modelos** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Decidir presupuesto con evidencia causal donde el monto lo justifique.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **modelo de atribución**. **cobertura de la atribución** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **modelo de atribución** | Regla convencional que reparte el crédito de la conversión entre puntos de contacto | Cuando **diferencia de crédito entre modelos** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **sesgo del último clic** | Sobrevaloración del canal más cercano a la conversión | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Ningún modelo de atribución establece causalidad. Con presupuestos pequeños, el costo de una prueba de incrementalidad puede superar su beneficio.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre atribución básica |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Digital marketing manager, Growth marketer y Especialista SEO/SEM. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Bajo último clic, la búsqueda de marca recibe el 61 % del crédito en Ruta Andina. Bajo primer clic, el contenido orgánico recibe el 44 %. El presupuesto se asigna con el primero.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **documentar el modelo y la ventana utilizados → comparar resultados bajo dos modelos distintos → identificar los canales cuyo valor cambia según el modelo → diseñar una prueba de incrementalidad para los casos críticos → decidir presupuesto con evidencia causal donde el monto lo justifique** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **diferencia de crédito entre modelos**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Web Analytics 2.0* y la de *Trustworthy Online Controlled Experiments*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **modelo de atribución** y **sesgo del último clic** como sinónimos | Se perdió la distinción entre «regla convencional que reparte el crédito de la conversión entre puntos de contacto» y «sobrevaloración del canal más cercano a la conversión» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «decidir presupuesto con evidencia causal donde el monto lo justifique» | Se saltó «documentar el modelo y la ventana utilizados»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **diferencia de crédito entre modelos** | La métrica local reemplazó al resultado del sistema | Contrástala con **resultado de pruebas de incrementalidad** y explicita el costo de oportunidad. |
| Asignar presupuesto sólo por último clic | Error específico de esta clase | Compara al menos dos modelos y valida los canales críticos con una prueba de incrementalidad. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **modelo de atribución** y **sesgo del último clic** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **ventana de atribución** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «documentar el modelo y la ventana utilizados» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **diferencia de crédito entre modelos** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Ningún modelo de atribución establece causalidad. Con presupuestos pequeños, el costo de una prueba de incrementalidad puede superar su beneficio»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **ventana de atribución** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **diferencia de crédito entre modelos**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Web Analytics 2.0* y *The Long and the Short of It*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Optimizar métricas de vanidad y desatender consentimiento, cookies y datos personales.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P12-C11-atribucion-basica/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **diferencia de crédito entre modelos**, **cobertura de la atribución** y **resultado de pruebas de incrementalidad** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **plan de adquisición digital con arquitectura de sitio, canales, medición y auditoría inicial**.

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

- Avinash Kaushik — *Web Analytics 2.0* (2009) — **aporta a esta clase:** la multiplicidad: combinar clics, resultados, experiencia y competencia. **Dónde buscarlo:** los capítulos sobre analítica multicanal. Registra edición y páginas consultadas en tu nota de lectura.
- Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) — **aporta a esta clase:** los riesgos de optimizar una métrica sustituta en lugar del resultado. **Dónde buscarlo:** los capítulos sobre selección de métricas. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — **aporta a esta clase:** la distinción entre correlación observada y causalidad y qué exige cada una. **Dónde buscarlo:** los capítulos sobre inferencia y sesgo. Registra edición y páginas consultadas en tu nota de lectura.
- Les Binet y Peter Field — *The Long and the Short of It* (2013) — **aporta a esta clase:** los efectos de corto plazo decaen; los de marca se acumulan y bajan la elasticidad de precio. **Dónde buscarlo:** los capítulos sobre curvas de respuesta en el tiempo. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 10 · Analítica digital](class-10-analitica-digital.md) · [Índice de la parte](README.md) · [Clase 12 · Omnicanalidad](class-12-omnicanalidad.md) →
