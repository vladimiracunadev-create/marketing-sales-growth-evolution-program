---
title: "Descuentos sin destruir valor"
type: class
language: es
standard: clase-profunda-v2
part: 07
class: 11
level: Oferta comercial
mastery_threshold: 80
estimated_minutes: 150
sources: ["nagle", "simon", "fisher-ury", "zoltners"]
anchors: {"fisher-ury": "criterios-objetivos", "nagle": "cascada", "simon": "guerra-precios", "zoltners": "incentivos"}
updated: 2026-08-19
---

# Clase 07.11 — Descuentos sin destruir valor

Clase 11 de 14 de la parte [07 — Pricing y monetización](README.md), de nivel Oferta comercial. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 07.10, *Freemium y pruebas gratuitas*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de descuento promedio ponderado con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La cascada de precio: del precio de lista al precio de bolsillo tras descuentos y concesiones — Thomas T. Nagle y Georg Müller. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Un descuento no negociado a cambio de nada enseña al mercado que el precio de lista es ficticio. La disciplina consiste en pedir siempre una contrapartida: plazo mayor, pago anticipado, volumen, caso de éxito, reducción de alcance. Nagle documenta que la política de descuentos debe estar escrita, con niveles de autoridad, porque la presión de cierre de periodo produce concesiones que se vuelven permanentes.

El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta. La parte 07 busca **diseñar una arquitectura de precios que capture valor sin destruir demanda ni confianza**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **descuentos sin destruir valor** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Cuánto vale esto para quién, y qué estructura de cobro alinea precio con valor entregado?

Los conceptos que estructuran la sesión son **contrapartida**, **autoridad de descuento**, **erosión de precio** y **precedente**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `contrapartida`, `autoridad de descuento`, `erosión de precio` y `precedente` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Pricing y monetización**.
3. **Aplicar** la secuencia **medir la erosión actual del precio efectivo → definir la escala de descuentos y su autoridad → asociar cada nivel a una contrapartida obligatoria → registrar las excepciones con su justificación → revisar mensualmente la dispersión por vendedor** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **descuento promedio ponderado**, **descuentos con contrapartida registrada** y **dispersión por vendedor** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **contrapartida** y **autoridad de descuento** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **descuento promedio ponderado**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **contrapartida** | concesión del cliente que justifica la reducción de precio | Da un hecho compatible con la definición y otro que la refute. |
| **autoridad de descuento** | nivel jerárquico habilitado para aprobar cada rango de descuento | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **erosión de precio** | caída sostenida del precio efectivo por acumulación de excepciones | Construye un caso límite donde el concepto se confunde con el anterior. |
| **precedente** | efecto de un descuento sobre las expectativas de futuras negociaciones con ese cliente y su gremio | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. medir la erosión actual del precio efectivo → 2. definir la escala de descuentos y su autoridad → 3. asociar cada nivel a una contrapartida obligatoria → 4. registrar las excepciones con su justificación → 5. revisar mensualmente la dispersión por vendedor
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Una política rígida sin excepciones puede perder negocios legítimos. Lo que no puede faltar es el registro y la revisión de cada excepción.

## 📖 Desarrollo

### 1. Contrapartida: mecanismo central

**Contrapartida** se entiende aquí como **concesión del cliente que justifica la reducción de precio**.

Un descuento sin contrapartida es una transferencia de margen sin retorno. La disciplina básica del descuento es que siempre se intercambia por algo verificable: plazo mayor, pago anticipado, volumen comprometido, caso de referencia autorizado, reducción de alcance. Cuando no hay contrapartida, lo que se está pagando es la incomodidad de sostener el precio.

**De dónde viene esta afirmación.** Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) aporta la idea que sostiene este bloque: la cascada de precio: del precio de lista al precio de bolsillo tras descuentos y concesiones. Búscala en el capítulo sobre gestión del precio realizado. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «descuento promedio ponderado» debería moverse cuando cambie **contrapartida**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **autoridad de descuento**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Autoridad de descuento: frontera conceptual y error de clasificación

**Definición operacional:** nivel jerárquico habilitado para aprobar cada rango de descuento. Su valor está en distinguirlo de **contrapartida**.

La autoridad de descuento debe estar escrita y escalonada, y su ausencia se paga en dispersión: cada vendedor concede lo que su carácter y su presión de cuota permiten. Una política clara —hasta cierto porcentaje decide el vendedor, más allá decide la jefatura— no elimina el descuento pero deja registro y hace visible el patrón.

**Contraste bibliográfico.** Hermann Simon — *Confessions of the Pricing Man* (2015) aporta aquí una distinción concreta: la guerra de precios como resultado evitable de decisiones tácticas (los capítulos sobre competencia en precio). Formula dos mini-casos: uno que satisface la definición de **autoridad de descuento** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «definir la escala de descuentos y su autoridad», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Erosión de precio: operacionalización y medición

**Erosión de precio** significa **caída sostenida del precio efectivo por acumulación de excepciones**.

La erosión de precio se mide con el precio realizado promedio y su evolución, no con la lista. La cascada —de precio de lista a precio de bolsillo— muestra dónde se pierde: descuento comercial, condiciones de pago, servicios regalados, penalizaciones no cobradas. Construirla una vez suele revelar varios puntos porcentuales de margen que nadie estaba mirando.

Ficha de medición obligatoria para **descuento promedio ponderado**: `diferencia entre precio de lista y efectivo, ponderada por ingreso, mensual`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Roger Fisher, William Ury y Bruce Patton — *Getting to Yes* (2011, 3.ª ed.) pone una condición sobre la medición: los criterios objetivos e independientes de la voluntad de las partes (el capítulo sobre criterios objetivos). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Precedente: trade-offs y efectos de segundo orden

**Definición:** efecto de un descuento sobre las expectativas de futuras negociaciones con ese cliente y su gremio.

Un descuento cierra el negocio de hoy y fija el precio de referencia de la próxima renovación. Ese precedente es el costo oculto: el cliente que obtuvo veinte por ciento esperará al menos lo mismo la vez siguiente. Antes de conceder conviene declarar explícitamente si es por única vez y bajo qué condición, y dejarlo por escrito en la propuesta.

**Lo que aporta la fuente.** Andris A. Zoltners, Prabhakant Sinha y Sally E. Lorimer — *The Complete Guide to Sales Force Incentive Compensation* (2006) aporta el criterio para pesar el intercambio: los efectos no deseados que produce cada estructura de incentivo (los capítulos sobre diseño de planes de compensación). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **dispersión por vendedor** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **precedente** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar mensualmente la dispersión por vendedor», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La política de descuentos debe aplicarse de forma consistente para no incurrir en discriminación arbitraria, y las condiciones especiales deben quedar documentadas. En operaciones con sector público, además, las reglas del procedimiento limitan qué puede ofrecerse y cuándo. La verificación del marco aplicable precede a cualquier concesión.

**Frontera declarada.** Una política rígida sin excepciones puede perder negocios legítimos. Lo que no puede faltar es el registro y la revisión de cada excepción. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar descuentos sin destruir valor no consiste en sumar definiciones. Empieza por **contrapartida**, contrasta **autoridad de descuento** con **erosión de precio**, incorpora **precedente** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) | La cascada de precio: del precio de lista al precio de bolsillo tras descuentos y concesiones | El capítulo sobre gestión del precio realizado | ¿Qué debería observarse en **contrapartida** si aquí opera «la cascada de precio: del precio de lista al precio de bolsillo tras descuentos y concesiones»? ¿Y qué observación lo desmentiría en este caso? |
| Hermann Simon — *Confessions of the Pricing Man* (2015) | La guerra de precios como resultado evitable de decisiones tácticas | Los capítulos sobre competencia en precio | ¿Qué debería observarse en **autoridad de descuento** si aquí opera «la guerra de precios como resultado evitable de decisiones tácticas»? ¿Y qué observación lo desmentiría en este caso? |
| Roger Fisher, William Ury y Bruce Patton — *Getting to Yes* (2011, 3.ª ed.) | Los criterios objetivos e independientes de la voluntad de las partes | El capítulo sobre criterios objetivos | ¿Qué debería observarse en **erosión de precio** si aquí opera «los criterios objetivos e independientes de la voluntad de las partes»? ¿Y qué observación lo desmentiría en este caso? |
| Andris A. Zoltners, Prabhakant Sinha y Sally E. Lorimer — *The Complete Guide to Sales Force Incentive Compensation* (2006) | Los efectos no deseados que produce cada estructura de incentivo | Los capítulos sobre diseño de planes de compensación | ¿Qué debería observarse en **precedente** si aquí opera «los efectos no deseados que produce cada estructura de incentivo»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** En Ruta Andina el descuento promedio de cierre de mes es 22 % y en el resto del mes es 7 %. Los compradores del gremio ya saben cuándo pedir.

**Paso 1 — Medir la erosión actual del precio efectivo.** El equipo escribe primero el supuesto asociado a **contrapartida** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **descuento promedio ponderado** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Definir la escala de descuentos y su autoridad.** El trabajo aquí es separar lo observado de lo inferido sobre **autoridad de descuento**. La evidencia que ordena la discusión es **descuentos con contrapartida registrada**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Asociar cada nivel a una contrapartida obligatoria.** El riesgo de este paso es cerrar demasiado rápido alrededor de **erosión de precio**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **dispersión por vendedor** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Registrar las excepciones con su justificación.** Con **precedente** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **descuento promedio ponderado** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar mensualmente la dispersión por vendedor.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **contrapartida**. **descuentos con contrapartida registrada** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **contrapartida** | Concesión del cliente que justifica la reducción de precio | Cuando **descuento promedio ponderado** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **autoridad de descuento** | Nivel jerárquico habilitado para aprobar cada rango de descuento | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Una política rígida sin excepciones puede perder negocios legítimos. Lo que no puede faltar es el registro y la revisión de cada excepción.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre descuentos sin destruir valor |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Pricing manager, Product marketing, CFO comercial y Founder. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

En Ruta Andina el descuento promedio de cierre de mes es 22 % y en el resto del mes es 7 %. Los compradores del gremio ya saben cuándo pedir.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **medir la erosión actual del precio efectivo → definir la escala de descuentos y su autoridad → asociar cada nivel a una contrapartida obligatoria → registrar las excepciones con su justificación → revisar mensualmente la dispersión por vendedor** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **descuento promedio ponderado**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *The Strategy and Tactics of Pricing* y la de *Confessions of the Pricing Man*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **contrapartida** y **autoridad de descuento** como sinónimos | Se perdió la distinción entre «concesión del cliente que justifica la reducción de precio» y «nivel jerárquico habilitado para aprobar cada rango de descuento» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar mensualmente la dispersión por vendedor» | Se saltó «medir la erosión actual del precio efectivo»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **descuento promedio ponderado** | La métrica local reemplazó al resultado del sistema | Contrástala con **dispersión por vendedor** y explicita el costo de oportunidad. |
| Otorgar descuentos sin contrapartida | Error específico de esta clase | Exige y registra una contrapartida concreta para cada descuento aprobado. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **contrapartida** y **autoridad de descuento** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **erosión de precio** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «medir la erosión actual del precio efectivo» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **descuento promedio ponderado** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Una política rígida sin excepciones puede perder negocios legítimos. Lo que no puede faltar es el registro y la revisión de cada excepción»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **erosión de precio** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **descuento promedio ponderado**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *The Strategy and Tactics of Pricing* y *The Complete Guide to Sales Force Incentive Compensation*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P07-C11-descuentos-sin-destruir-valor/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **descuento promedio ponderado**, **descuentos con contrapartida registrada** y **dispersión por vendedor** con fuente, ventana y lectura prohibida.
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

Estas son las obras sobre las que se apoya lo que acabas de leer. Cada una aparece con la idea concreta que aporta a esta clase, dónde buscarla dentro del libro y el enlace donde se resuelve la edición exacta. Si al leer no encuentras esa idea, la cita está mal puesta y corresponde reportarlo como error del material.

- Thomas T. Nagle y Georg Müller — [*The Strategy and Tactics of Pricing*](https://openlibrary.org/isbn/9781138737501) (2018, 6.ª ed.) · ISBN 9781138737501 — **aporta a esta clase:** la cascada de precio: del precio de lista al precio de bolsillo tras descuentos y concesiones. **Dónde buscarlo:** el capítulo sobre gestión del precio realizado. Registra edición y páginas consultadas en tu nota de lectura.
- Hermann Simon — [*Confessions of the Pricing Man*](https://openlibrary.org/isbn/9783319204000) (2015) · ISBN 9783319204000 — **aporta a esta clase:** la guerra de precios como resultado evitable de decisiones tácticas. **Dónde buscarlo:** los capítulos sobre competencia en precio. Registra edición y páginas consultadas en tu nota de lectura.
- Roger Fisher, William Ury y Bruce Patton — [*Getting to Yes*](https://openlibrary.org/isbn/9781101539545) (2011, 3.ª ed.) · ISBN 9781101539545 — **aporta a esta clase:** los criterios objetivos e independientes de la voluntad de las partes. **Dónde buscarlo:** el capítulo sobre criterios objetivos. Registra edición y páginas consultadas en tu nota de lectura.
- Andris A. Zoltners, Prabhakant Sinha y Sally E. Lorimer — [*The Complete Guide to Sales Force Incentive Compensation*](https://openlibrary.org/isbn/9780814473245) (2006) · ISBN 9780814473245 — **aporta a esta clase:** los efectos no deseados que produce cada estructura de incentivo. **Dónde buscarlo:** los capítulos sobre diseño de planes de compensación. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 10 · Freemium y pruebas gratuitas](class-10-freemium-y-pruebas-gratuitas.md) · [Índice de la parte](README.md) · [Clase 12 · Unit economics](class-12-unit-economics.md) →
