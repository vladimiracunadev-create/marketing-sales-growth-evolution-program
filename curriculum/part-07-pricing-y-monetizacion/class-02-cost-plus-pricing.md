---
title: "Pricing por costo"
type: class
language: es
standard: clase-profunda-v2
part: 07
class: 02
level: Oferta comercial
mastery_threshold: 80
estimated_minutes: 150
sources: ["nagle", "simon", "smith-pricing", "croll-yoskovitz"]
anchors: {"croll-yoskovitz": "modelos", "nagle": "costo-piso", "simon": "valor-percibido", "smith-pricing": "estructura"}
updated: 2026-08-19
---

# Clase 07.02 — Pricing por costo

**Parte 07 · Pricing y monetización** · Nivel: Oferta comercial · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 07.01 — *El precio como decisión estratégica*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de costo de servir por segmento para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El costo como piso de decisión y no como método de fijación — Thomas T. Nagle y Georg Müller. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Fijar precio sumando un margen al costo es simple, defendible internamente y sistemáticamente subóptimo: ignora al cliente y a la competencia. Su único mérito es garantizar que no se venda bajo costo, lo que es necesario pero insuficiente. Además tiene una trampa lógica: el costo unitario depende del volumen, y el volumen depende del precio, por lo que el método razona en círculo. Su lugar correcto es como piso, no como método.

Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales. La parte 07 busca **diseñar una arquitectura de precios que capture valor sin destruir demanda ni confianza**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **pricing por costo** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Cuánto vale esto para quién, y qué estructura de cobro alinea precio con valor entregado?

Los conceptos que estructuran la sesión son **costo variable unitario**, **costo de servir completo**, **margen objetivo** y **circularidad costo-volumen**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `costo variable unitario`, `costo de servir completo`, `margen objetivo` y `circularidad costo-volumen` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Pricing y monetización**.
3. **Aplicar** la secuencia **identificar todos los costos atribuibles al cliente → separar costos fijos de variables → calcular el piso de precio por segmento → contrastar el piso con la disposición a pagar → usar el resultado como restricción y no como decisión** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **costo de servir por segmento**, **proporción de ventas bajo el piso** y **margen de contribución real** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **costo variable unitario** y **costo de servir completo** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **costo de servir por segmento**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **costo variable unitario** | costo que se incurre por cada unidad adicional vendida o servida | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **costo de servir completo** | suma de costos directos, soporte, implementación y comisiones atribuibles al cliente | Construye un caso límite donde el concepto se confunde con el anterior. |
| **margen objetivo** | porcentaje que la empresa decide agregar sobre el costo | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **circularidad costo-volumen** | dependencia mutua entre costo unitario y volumen que invalida el cálculo ingenuo | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. identificar todos los costos atribuibles al cliente → 2. separar costos fijos de variables → 3. calcular el piso de precio por segmento → 4. contrastar el piso con la disposición a pagar → 5. usar el resultado como restricción y no como decisión
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Sin un costeo que incluya implementación y soporte, el piso calculado es ficticio y puede llevar a vender con pérdida creyendo que hay margen.

## 📖 Desarrollo

### 1. Costo variable unitario: mecanismo central

**Costo variable unitario** se entiende aquí como **costo que se incurre por cada unidad adicional vendida o servida**.

El costo más un margen es el método más usado y el menos defendible. Su atractivo es la aparente objetividad: parte de un número que la empresa conoce. Su problema es que el costo no dice nada sobre lo que el cliente está dispuesto a pagar, de modo que el método produce precios demasiado altos donde el valor es bajo y demasiado bajos donde el valor es alto, con la misma seguridad en ambos casos.

**De dónde viene esta afirmación.** Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) aporta la idea que sostiene este bloque: el costo como piso de decisión y no como método de fijación. Búscala en el capítulo sobre costos relevantes para la decisión. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «costo de servir por segmento» debería moverse cuando cambie **costo variable unitario**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **costo de servir completo**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Costo de servir completo: frontera conceptual y error de clasificación

**Definición operacional:** suma de costos directos, soporte, implementación y comisiones atribuibles al cliente. Su valor está en distinguirlo de **costo variable unitario**.

El costo variable unitario y el costo de servir completo se confunden con frecuencia. El primero incluye lo que se consume por unidad vendida; el segundo agrega soporte, implementación, gestión de cuenta y todo lo que ese cliente demanda. Un cliente puede tener margen bruto excelente y margen real negativo, y sólo el segundo cálculo lo revela.

**Contraste bibliográfico.** Hermann Simon — *Confessions of the Pricing Man* (2015) aporta aquí una distinción concreta: el precio como reflejo del valor percibido y la tarea de comunicarlo (los capítulos sobre valor y precio). Formula dos mini-casos: uno que satisface la definición de **costo de servir completo** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «separar costos fijos de variables», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Margen objetivo: operacionalización y medición

**Margen objetivo** significa **porcentaje que la empresa decide agregar sobre el costo**.

El costo tiene un uso legítimo y preciso: es el piso, no el método. Sirve para saber por debajo de qué precio la operación pierde dinero y para decidir qué negocios rechazar. La ficha debe registrar qué costos están incluidos, cuáles son escalonados y a partir de qué volumen aparece un salto, porque ese salto es el que rompe los cálculos lineales.

Ficha de medición obligatoria para **costo de servir por segmento**: `costos directos e indirectos atribuibles, dividido por clientes del segmento`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Tim J. Smith — *Pricing Strategy* (2011) pone una condición sobre la medición: la estructura de precios como decisión separada del nivel de precio (los capítulos sobre arquitectura de precios). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Circularidad costo-volumen: trade-offs y efectos de segundo orden

**Definición:** dependencia mutua entre costo unitario y volumen que invalida el cálculo ingenuo.

La circularidad costo-volumen es la trampa técnica del método: el costo unitario depende del volumen y el volumen depende del precio, que se calcula sobre el costo unitario. En productos con altos costos fijos, esa circularidad puede llevar a una espiral donde la caída de volumen sube el costo unitario y justifica subir el precio, que reduce más el volumen.

**Lo que aporta la fuente.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) aporta el criterio para pesar el intercambio: los seis modelos de negocio y las métricas que cambian entre ellos (la parte sobre modelos de negocio). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **margen de contribución real** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **circularidad costo-volumen** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «usar el resultado como restricción y no como decisión», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El método por costo es razonable en contextos específicos: contratos regulados que exigen justificación de costos, licitaciones con estructura definida, servicios estandarizados en mercados muy competidos. Fuera de esos casos, usarlo como método principal deja valor sobre la mesa de forma sistemática y silenciosa.

**Frontera declarada.** Sin un costeo que incluya implementación y soporte, el piso calculado es ficticio y puede llevar a vender con pérdida creyendo que hay margen. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar pricing por costo no consiste en sumar definiciones. Empieza por **costo variable unitario**, contrasta **costo de servir completo** con **margen objetivo**, incorpora **circularidad costo-volumen** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) | El costo como piso de decisión y no como método de fijación | El capítulo sobre costos relevantes para la decisión | ¿Qué debería observarse en **costo variable unitario** si aquí opera «el costo como piso de decisión y no como método de fijación»? ¿Y qué observación lo desmentiría en este caso? |
| Hermann Simon — *Confessions of the Pricing Man* (2015) | El precio como reflejo del valor percibido y la tarea de comunicarlo | Los capítulos sobre valor y precio | ¿Qué debería observarse en **costo de servir completo** si aquí opera «el precio como reflejo del valor percibido y la tarea de comunicarlo»? ¿Y qué observación lo desmentiría en este caso? |
| Tim J. Smith — *Pricing Strategy* (2011) | La estructura de precios como decisión separada del nivel de precio | Los capítulos sobre arquitectura de precios | ¿Qué debería observarse en **margen objetivo** si aquí opera «la estructura de precios como decisión separada del nivel de precio»? ¿Y qué observación lo desmentiría en este caso? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | Los seis modelos de negocio y las métricas que cambian entre ellos | La parte sobre modelos de negocio | ¿Qué debería observarse en **circularidad costo-volumen** si aquí opera «los seis modelos de negocio y las métricas que cambian entre ellos»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El plan básico de Ruta Andina se fijó con 40 % de margen sobre costos de infraestructura. Al incluir las 9 horas de migración, el margen real es negativo.

**Paso 1 — Identificar todos los costos atribuibles al cliente.** El equipo escribe primero el supuesto asociado a **costo variable unitario** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **costo de servir por segmento** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Separar costos fijos de variables.** El trabajo aquí es separar lo observado de lo inferido sobre **costo de servir completo**. La evidencia que ordena la discusión es **proporción de ventas bajo el piso**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Calcular el piso de precio por segmento.** El riesgo de este paso es cerrar demasiado rápido alrededor de **margen objetivo**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **margen de contribución real** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Contrastar el piso con la disposición a pagar.** Con **circularidad costo-volumen** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **costo de servir por segmento** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Usar el resultado como restricción y no como decisión.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **costo variable unitario**. **proporción de ventas bajo el piso** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **costo variable unitario** | Costo que se incurre por cada unidad adicional vendida o servida | Cuando **costo de servir por segmento** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **costo de servir completo** | Suma de costos directos, soporte, implementación y comisiones atribuibles al cliente | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Sin un costeo que incluya implementación y soporte, el piso calculado es ficticio y puede llevar a vender con pérdida creyendo que hay margen.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre pricing por costo |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Pricing manager, Product marketing, CFO comercial y Founder. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El plan básico de Ruta Andina se fijó con 40 % de margen sobre costos de infraestructura. Al incluir las 9 horas de migración, el margen real es negativo.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **identificar todos los costos atribuibles al cliente → separar costos fijos de variables → calcular el piso de precio por segmento → contrastar el piso con la disposición a pagar → usar el resultado como restricción y no como decisión** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **costo de servir por segmento**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *The Strategy and Tactics of Pricing* y la de *Confessions of the Pricing Man*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **costo variable unitario** y **costo de servir completo** como sinónimos | Se perdió la distinción entre «costo que se incurre por cada unidad adicional vendida o servida» y «suma de costos directos, soporte, implementación y comisiones atribuibles al cliente» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «usar el resultado como restricción y no como decisión» | Se saltó «identificar todos los costos atribuibles al cliente»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **costo de servir por segmento** | La métrica local reemplazó al resultado del sistema | Contrástala con **margen de contribución real** y explicita el costo de oportunidad. |
| Calcular el piso sin costo de servir completo | Error específico de esta clase | Incorpora horas de implementación, soporte y comisiones antes de declarar el margen. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **costo variable unitario** y **costo de servir completo** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **margen objetivo** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «identificar todos los costos atribuibles al cliente» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **costo de servir por segmento** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Sin un costeo que incluya implementación y soporte, el piso calculado es ficticio y puede llevar a vender con pérdida creyendo que hay margen»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **margen objetivo** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **costo de servir por segmento**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *The Strategy and Tactics of Pricing* y *Lean Analytics*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P07-C02-cost-plus-pricing/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **costo de servir por segmento**, **proporción de ventas bajo el piso** y **margen de contribución real** con fuente, ventana y lectura prohibida.
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

- Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) — **aporta a esta clase:** el costo como piso de decisión y no como método de fijación. **Dónde buscarlo:** el capítulo sobre costos relevantes para la decisión. Registra edición y páginas consultadas en tu nota de lectura.
- Hermann Simon — *Confessions of the Pricing Man* (2015) — **aporta a esta clase:** el precio como reflejo del valor percibido y la tarea de comunicarlo. **Dónde buscarlo:** los capítulos sobre valor y precio. Registra edición y páginas consultadas en tu nota de lectura.
- Tim J. Smith — *Pricing Strategy* (2011) — **aporta a esta clase:** la estructura de precios como decisión separada del nivel de precio. **Dónde buscarlo:** los capítulos sobre arquitectura de precios. Registra edición y páginas consultadas en tu nota de lectura.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — **aporta a esta clase:** los seis modelos de negocio y las métricas que cambian entre ellos. **Dónde buscarlo:** la parte sobre modelos de negocio. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 01 · El precio como decisión estratégica](class-01-precio-como-decision-estrategica.md) · [Índice de la parte](README.md) · [Clase 03 · Pricing por competencia](class-03-competitor-based-pricing.md) →
