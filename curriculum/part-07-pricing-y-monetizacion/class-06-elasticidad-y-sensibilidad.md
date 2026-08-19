---
title: "Elasticidad y sensibilidad al precio"
type: class
language: es
standard: clase-profunda-v2
part: 07
class: 06
level: Oferta comercial
mastery_threshold: 80
estimated_minutes: 150
sources: ["nagle", "kohavi", "simon", "smith-pricing"]
anchors: {"kohavi": "efecto-minimo", "nagle": "sensibilidad", "simon": "psicologia-precio", "smith-pricing": "price-fences"}
updated: 2026-08-19
---

# Clase 07.06 — Elasticidad y sensibilidad al precio

**Parte 07 · Pricing y monetización** · Nivel: Oferta comercial · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 07.05 — *Disposición a pagar*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de elasticidad estimada por segmento para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** Los factores que aumentan o reducen la sensibilidad al precio y su gestión deliberada — Thomas T. Nagle y Georg Müller. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La elasticidad mide cuánto cambia la cantidad demandada ante un cambio de precio. No es una constante: varía por segmento, por momento y por la presencia de alternativas visibles. Nagle identificó factores que la reducen —costo de cambio, valor único percibido, dificultad de comparar, gasto compartido— y esos factores son gestionables. Estimarla con datos propios requiere variación real de precios, no opinión.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 07 busca **diseñar una arquitectura de precios que capture valor sin destruir demanda ni confianza**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **elasticidad y sensibilidad al precio** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Cuánto vale esto para quién, y qué estructura de cobro alinea precio con valor entregado?

Los conceptos que estructuran la sesión son **elasticidad precio**, **factor de sensibilidad**, **segmentación de sensibilidad** y **prueba de precio**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `elasticidad precio`, `factor de sensibilidad`, `segmentación de sensibilidad` y `prueba de precio` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Pricing y monetización**.
3. **Aplicar** la secuencia **identificar los factores de sensibilidad presentes en el segmento → diseñar una prueba con variación real y grupos comparables → estimar la respuesta con intervalo de incertidumbre → verificar si la respuesta difiere por segmento → decidir el nivel de precio y su condición de revisión** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **elasticidad estimada por segmento**, **tasa de abandono ante alza** y **efecto en ingreso total** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **elasticidad precio** y **factor de sensibilidad** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **elasticidad estimada por segmento**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **elasticidad precio** | variación porcentual de la cantidad ante una variación porcentual del precio | Da un hecho compatible con la definición y otro que la refute. |
| **factor de sensibilidad** | condición que aumenta o reduce la reacción del cliente ante el precio | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **segmentación de sensibilidad** | diferencia de elasticidad entre grupos de clientes del mismo mercado | Construye un caso límite donde el concepto se confunde con el anterior. |
| **prueba de precio** | experimento controlado que produce variación real para estimar la respuesta | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. identificar los factores de sensibilidad presentes en el segmento → 2. diseñar una prueba con variación real y grupos comparables → 3. estimar la respuesta con intervalo de incertidumbre → 4. verificar si la respuesta difiere por segmento → 5. decidir el nivel de precio y su condición de revisión
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Las pruebas de precio con clientes reales tienen consecuencias comerciales y éticas: cobrar distinto a personas equivalentes sin justificación puede constituir discriminación arbitraria.

## 📖 Desarrollo

### 1. Elasticidad precio: mecanismo central

**Elasticidad precio** se entiende aquí como **variación porcentual de la cantidad ante una variación porcentual del precio**.

La elasticidad describe cuánto cambia la cantidad demandada ante un cambio de precio, y en la práctica comercial casi nunca se conoce con precisión. Lo que sí puede conocerse son los factores que la aumentan o la reducen: existencia de alternativas conocidas, peso del gasto en el presupuesto del cliente, facilidad de comparación, urgencia y quién paga.

**De dónde viene esta afirmación.** Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) aporta la idea que sostiene este bloque: los factores que aumentan o reducen la sensibilidad al precio y su gestión deliberada. Búscala en el capítulo sobre sensibilidad al precio. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «elasticidad estimada por segmento» debería moverse cuando cambie **elasticidad precio**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **factor de sensibilidad**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Factor de sensibilidad: frontera conceptual y error de clasificación

**Definición operacional:** condición que aumenta o reduce la reacción del cliente ante el precio. Su valor está en distinguirlo de **elasticidad precio**.

La sensibilidad varía entre segmentos del mismo mercado, y esa variación es la base de toda segmentación de precios. Un cliente que compara tres cotizaciones es más sensible que uno que necesita resolver hoy. Tratarlos con el mismo precio y la misma política de descuento significa regalar margen al segundo y perder al primero.

**Contraste bibliográfico.** Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) aporta aquí una distinción concreta: el efecto mínimo relevante como base del cálculo de muestra (los capítulos sobre potencia y tamaño de muestra). Formula dos mini-casos: uno que satisface la definición de **factor de sensibilidad** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «diseñar una prueba con variación real y grupos comparables», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Segmentación de sensibilidad: operacionalización y medición

**Segmentación de sensibilidad** significa **diferencia de elasticidad entre grupos de clientes del mismo mercado**.

Estimar la elasticidad con datos históricos exige que haya habido variación de precio y que se puedan aislar otros factores, condiciones que rara vez se cumplen. Cuando se intenta igual, el resultado suele confundir efecto de precio con estacionalidad o con cambios de mezcla. Declarar esa limitación es más honesto que presentar un coeficiente con dos decimales.

Ficha de medición obligatoria para **elasticidad estimada por segmento**: `variación porcentual de unidades sobre variación porcentual de precio, con intervalo`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Hermann Simon — *Confessions of the Pricing Man* (2015) pone una condición sobre la medición: los efectos psicológicos del precio y su uso responsable (los capítulos sobre psicología del precio). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Prueba de precio: trade-offs y efectos de segundo orden

**Definición:** experimento controlado que produce variación real para estimar la respuesta.

Una prueba de precio entrega evidencia limpia y expone a que clientes con precios distintos se enteren. En entornos B2B ese riesgo es alto y el daño de confianza puede superar el aprendizaje. La alternativa habitual es probar con clientes nuevos, con planes nuevos o en mercados geográficamente separados, declarando el criterio de separación.

**Lo que aporta la fuente.** Tim J. Smith — *Pricing Strategy* (2011) aporta el criterio para pesar el intercambio: las barreras de precio que sostienen la segmentación sin arbitraje (los capítulos sobre segmentación de precios). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **efecto en ingreso total** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **prueba de precio** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «decidir el nivel de precio y su condición de revisión», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Toda prueba de precio debe respetar la igualdad de trato que la normativa exige y evitar discriminaciones sin justificación objetiva. Además, un cambio de precio a clientes vigentes tiene reglas contractuales propias. Antes de diseñar cualquier experimento de precio corresponde verificar el marco aplicable y las condiciones pactadas.

**Frontera declarada.** Las pruebas de precio con clientes reales tienen consecuencias comerciales y éticas: cobrar distinto a personas equivalentes sin justificación puede constituir discriminación arbitraria. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar elasticidad y sensibilidad al precio no consiste en sumar definiciones. Empieza por **elasticidad precio**, contrasta **factor de sensibilidad** con **segmentación de sensibilidad**, incorpora **prueba de precio** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) | Los factores que aumentan o reducen la sensibilidad al precio y su gestión deliberada | El capítulo sobre sensibilidad al precio | ¿Qué debería observarse en **elasticidad precio** si aquí opera «los factores que aumentan o reducen la sensibilidad al precio y su gestión deliberada»? ¿Y qué observación lo desmentiría en este caso? |
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | El efecto mínimo relevante como base del cálculo de muestra | Los capítulos sobre potencia y tamaño de muestra | ¿Qué debería observarse en **factor de sensibilidad** si aquí opera «el efecto mínimo relevante como base del cálculo de muestra»? ¿Y qué observación lo desmentiría en este caso? |
| Hermann Simon — *Confessions of the Pricing Man* (2015) | Los efectos psicológicos del precio y su uso responsable | Los capítulos sobre psicología del precio | ¿Qué debería observarse en **segmentación de sensibilidad** si aquí opera «los efectos psicológicos del precio y su uso responsable»? ¿Y qué observación lo desmentiría en este caso? |
| Tim J. Smith — *Pricing Strategy* (2011) | Las barreras de precio que sostienen la segmentación sin arbitraje | Los capítulos sobre segmentación de precios | ¿Qué debería observarse en **prueba de precio** si aquí opera «las barreras de precio que sostienen la segmentación sin arbitraje»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina subió 12 % el precio a clientes nuevos y mantuvo el de los antiguos. Puede estimar la elasticidad comparando conversión entre ambos grupos si controla estacionalidad y mezcla.

**Paso 1 — Identificar los factores de sensibilidad presentes en el segmento.** El equipo escribe primero el supuesto asociado a **elasticidad precio** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **elasticidad estimada por segmento** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Diseñar una prueba con variación real y grupos comparables.** El trabajo aquí es separar lo observado de lo inferido sobre **factor de sensibilidad**. La evidencia que ordena la discusión es **tasa de abandono ante alza**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Estimar la respuesta con intervalo de incertidumbre.** El riesgo de este paso es cerrar demasiado rápido alrededor de **segmentación de sensibilidad**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **efecto en ingreso total** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Verificar si la respuesta difiere por segmento.** Con **prueba de precio** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **elasticidad estimada por segmento** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Decidir el nivel de precio y su condición de revisión.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **elasticidad precio**. **tasa de abandono ante alza** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **elasticidad precio** | Variación porcentual de la cantidad ante una variación porcentual del precio | Cuando **elasticidad estimada por segmento** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **factor de sensibilidad** | Condición que aumenta o reduce la reacción del cliente ante el precio | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Las pruebas de precio con clientes reales tienen consecuencias comerciales y éticas: cobrar distinto a personas equivalentes sin justificación puede constituir discriminación arbitraria.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre elasticidad y sensibilidad al precio |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Pricing manager, Product marketing, CFO comercial y Founder. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina subió 12 % el precio a clientes nuevos y mantuvo el de los antiguos. Puede estimar la elasticidad comparando conversión entre ambos grupos si controla estacionalidad y mezcla.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **identificar los factores de sensibilidad presentes en el segmento → diseñar una prueba con variación real y grupos comparables → estimar la respuesta con intervalo de incertidumbre → verificar si la respuesta difiere por segmento → decidir el nivel de precio y su condición de revisión** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **elasticidad estimada por segmento**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *The Strategy and Tactics of Pricing* y la de *Trustworthy Online Controlled Experiments*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **elasticidad precio** y **factor de sensibilidad** como sinónimos | Se perdió la distinción entre «variación porcentual de la cantidad ante una variación porcentual del precio» y «condición que aumenta o reduce la reacción del cliente ante el precio» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «decidir el nivel de precio y su condición de revisión» | Se saltó «identificar los factores de sensibilidad presentes en el segmento»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **elasticidad estimada por segmento** | La métrica local reemplazó al resultado del sistema | Contrástala con **efecto en ingreso total** y explicita el costo de oportunidad. |
| Estimar elasticidad con datos históricos sin controlar mezcla | Error específico de esta clase | Usa grupos comparables y controla estacionalidad, canal y mezcla de segmentos. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **elasticidad precio** y **factor de sensibilidad** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **segmentación de sensibilidad** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «identificar los factores de sensibilidad presentes en el segmento» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **elasticidad estimada por segmento** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Las pruebas de precio con clientes reales tienen consecuencias comerciales y éticas: cobrar distinto a personas equivalentes sin justificación puede constituir discriminación arbitraria»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **segmentación de sensibilidad** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **elasticidad estimada por segmento**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *The Strategy and Tactics of Pricing* y *Pricing Strategy*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P07-C06-elasticidad-y-sensibilidad/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **elasticidad estimada por segmento**, **tasa de abandono ante alza** y **efecto en ingreso total** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **arquitectura de monetización con métrica de cobro, planes, price fences y política de descuentos**.

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

- Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) — **aporta a esta clase:** los factores que aumentan o reducen la sensibilidad al precio y su gestión deliberada. **Dónde buscarlo:** el capítulo sobre sensibilidad al precio. Registra edición y páginas consultadas en tu nota de lectura.
- Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) — **aporta a esta clase:** el efecto mínimo relevante como base del cálculo de muestra. **Dónde buscarlo:** los capítulos sobre potencia y tamaño de muestra. Registra edición y páginas consultadas en tu nota de lectura.
- Hermann Simon — *Confessions of the Pricing Man* (2015) — **aporta a esta clase:** los efectos psicológicos del precio y su uso responsable. **Dónde buscarlo:** los capítulos sobre psicología del precio. Registra edición y páginas consultadas en tu nota de lectura.
- Tim J. Smith — *Pricing Strategy* (2011) — **aporta a esta clase:** las barreras de precio que sostienen la segmentación sin arbitraje. **Dónde buscarlo:** los capítulos sobre segmentación de precios. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 05 · Disposición a pagar](class-05-willingness-to-pay.md) · [Índice de la parte](README.md) · [Clase 07 · Van Westendorp y técnicas de investigación de precio](class-07-van-westendorp-y-tecnicas-de-investigacion.md) →
