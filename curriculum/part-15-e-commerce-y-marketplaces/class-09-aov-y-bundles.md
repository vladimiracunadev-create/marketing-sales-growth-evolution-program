---
title: "Ticket promedio y paquetes"
type: class
language: es
standard: clase-profunda-v2
part: 15
class: 09
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["ramanujam", "flint", "fader", "nagle"]
anchors: {"fader": "rfm", "flint": "recompra", "nagle": "segmentacion-precio", "ramanujam": "empaquetado"}
updated: 2026-08-19
---

# Clase 15.09 — Ticket promedio y paquetes

**Parte 15 · E-commerce y marketplaces** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 15.08 — *Abandono de carrito*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de ticket promedio por segmento para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El empaquetado desde la disposición a pagar por atributo y no desde la arquitectura técnica — Madhavan Ramanujam y Georg Tacke. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Aumentar el ticket promedio suele ser más barato que aumentar el tráfico, porque opera sobre personas que ya decidieron comprar. Las palancas son conocidas: paquetes, umbrales de despacho gratis, complementos pertinentes. Su límite también: un paquete que obliga a comprar lo que no se necesita reduce la conversión y aumenta las devoluciones.

Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales. La parte 15 busca **operar una tienda y un canal de marketplace con economía verificable**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **ticket promedio y paquetes** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Dónde se pierde el pedido y cuánto queda después de comisión, envío y devolución?

Los conceptos que estructuran la sesión son **ticket promedio**, **paquete pertinente**, **umbral de beneficio** y **efecto sobre conversión**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `ticket promedio`, `paquete pertinente`, `umbral de beneficio` y `efecto sobre conversión` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **E-commerce y marketplaces**.
3. **Aplicar** la secuencia **analizar qué productos se compran juntos → diseñar paquetes con lógica de uso real → definir umbrales de beneficio con margen verificado → medir efecto conjunto en ticket y en conversión → revisar devoluciones asociadas a los paquetes** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **ticket promedio por segmento**, **efecto en conversión** y **devoluciones de productos en paquete** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **ticket promedio** y **paquete pertinente** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **ticket promedio por segmento**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **ticket promedio** | ingreso del periodo dividido por número de pedidos | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **paquete pertinente** | combinación que el cliente usaría efectivamente en conjunto | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **umbral de beneficio** | monto que activa un incentivo como despacho sin costo | Da un hecho compatible con la definición y otro que la refute. |
| **efecto sobre conversión** | cambio en la tasa de compra provocado por la intervención de ticket | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. analizar qué productos se compran juntos → 2. diseñar paquetes con lógica de uso real → 3. definir umbrales de beneficio con margen verificado → 4. medir efecto conjunto en ticket y en conversión → 5. revisar devoluciones asociadas a los paquetes
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Subir el ticket puede reducir la frecuencia de compra. La evaluación debe considerar el ingreso por cliente en el periodo, no sólo el ticket por pedido.

## 📖 Desarrollo

### 1. Ticket promedio: mecanismo central

**Ticket promedio** se entiende aquí como **ingreso del periodo dividido por número de pedidos**.

Subir el ticket promedio es una palanca de margen que no requiere más tráfico, y por eso suele ser la más rentable en operaciones con costo de adquisición alto. Sus mecanismos habituales —paquetes, umbrales de envío gratuito, recomendaciones— funcionan cuando son pertinentes y molestan cuando no lo son.

**De dónde viene esta afirmación.** Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) aporta la idea que sostiene este bloque: el empaquetado desde la disposición a pagar por atributo y no desde la arquitectura técnica. Búscala en el capítulo sobre configuración y empaquetado. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «ticket promedio por segmento» debería moverse cuando cambie **ticket promedio**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **paquete pertinente**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Paquete pertinente: frontera conceptual y error de clasificación

**Definición operacional:** combinación que el cliente usaría efectivamente en conjunto. Su valor está en distinguirlo de **ticket promedio**.

El paquete pertinente combina productos que efectivamente se usan juntos, y esa combinación se descubre en los datos de compra y no en la lógica de catálogo. Un paquete armado por conveniencia de inventario se percibe como intento de colocar lo que no se vende, y esa percepción daña más que el ingreso que produce.

**Contraste bibliográfico.** Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) aporta aquí una distinción concreta: los patrones de recompra que distinguen un negocio de compra única de uno recurrente (los capítulos sobre ciclos de compra). Formula dos mini-casos: uno que satisface la definición de **paquete pertinente** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «diseñar paquetes con lógica de uso real», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Umbral de beneficio: operacionalización y medición

**Umbral de beneficio** significa **monto que activa un incentivo como despacho sin costo**.

El umbral de beneficio —el monto a partir del cual se ofrece una ventaja— debe fijarse con el análisis de la distribución de tickets: un poco por encima de donde se concentra la mayoría, para que sea alcanzable. Fijarlo muy arriba no mueve a nadie; muy abajo regala margen a quien ya habría superado ese monto.

Ficha de medición obligatoria para **ticket promedio por segmento**: `ingreso, sobre pedidos, por segmento y periodo`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Peter Fader — *Customer Centricity* (2020, 2.ª ed.) pone una condición sobre la medición: recencia, frecuencia y valor como base de segmentación conductual (los capítulos sobre segmentación por comportamiento). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Efecto sobre conversión: trade-offs y efectos de segundo orden

**Definición:** cambio en la tasa de compra provocado por la intervención de ticket.

Empujar el ticket puede reducir la conversión si el mecanismo introduce fricción o si el cliente percibe presión. La medición correcta observa el ingreso total por visitante y no el ticket promedio aislado, porque un ticket mayor con menos compradores puede significar menos ingreso.

**Lo que aporta la fuente.** Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) aporta el criterio para pesar el intercambio: las barreras de segmentación de precio y su legitimidad ante el cliente (el capítulo sobre estructura de precios). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **devoluciones de productos en paquete** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **efecto sobre conversión** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar devoluciones asociadas a los paquetes», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Estas técnicas operan sobre la decisión del cliente y tienen un límite: la recomendación debe ser genuinamente útil. Cuando el mecanismo lleva sistemáticamente a comprar más de lo necesario, el efecto aparece en devoluciones y en la relación de largo plazo, y en operaciones de consumo puede constituir una práctica cuestionable.

**Frontera declarada.** Subir el ticket puede reducir la frecuencia de compra. La evaluación debe considerar el ingreso por cliente en el periodo, no sólo el ticket por pedido. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar ticket promedio y paquetes no consiste en sumar definiciones. Empieza por **ticket promedio**, contrasta **paquete pertinente** con **umbral de beneficio**, incorpora **efecto sobre conversión** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) | El empaquetado desde la disposición a pagar por atributo y no desde la arquitectura técnica | El capítulo sobre configuración y empaquetado | ¿Qué debería observarse en **ticket promedio** si aquí opera «el empaquetado desde la disposición a pagar por atributo y no desde la arquitectura técnica»? ¿Y qué observación lo desmentiría en este caso? |
| Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) | Los patrones de recompra que distinguen un negocio de compra única de uno recurrente | Los capítulos sobre ciclos de compra | ¿Qué debería observarse en **paquete pertinente** si aquí opera «los patrones de recompra que distinguen un negocio de compra única de uno recurrente»? ¿Y qué observación lo desmentiría en este caso? |
| Peter Fader — *Customer Centricity* (2020, 2.ª ed.) | Recencia, frecuencia y valor como base de segmentación conductual | Los capítulos sobre segmentación por comportamiento | ¿Qué debería observarse en **umbral de beneficio** si aquí opera «recencia, frecuencia y valor como base de segmentación conductual»? ¿Y qué observación lo desmentiría en este caso? |
| Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) | Las barreras de segmentación de precio y su legitimidad ante el cliente | El capítulo sobre estructura de precios | ¿Qué debería observarse en **efecto sobre conversión** si aquí opera «las barreras de segmentación de precio y su legitimidad ante el cliente»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El umbral de despacho gratis de Ruta Andina es CLP 60.000 y su ticket promedio es CLP 89.000: el incentivo se entrega a casi todos sin cambiar comportamiento.

**Paso 1 — Analizar qué productos se compran juntos.** El equipo escribe primero el supuesto asociado a **ticket promedio** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **ticket promedio por segmento** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Diseñar paquetes con lógica de uso real.** El trabajo aquí es separar lo observado de lo inferido sobre **paquete pertinente**. La evidencia que ordena la discusión es **efecto en conversión**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Definir umbrales de beneficio con margen verificado.** El riesgo de este paso es cerrar demasiado rápido alrededor de **umbral de beneficio**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **devoluciones de productos en paquete** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Medir efecto conjunto en ticket y en conversión.** Con **efecto sobre conversión** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **ticket promedio por segmento** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar devoluciones asociadas a los paquetes.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **ticket promedio**. **efecto en conversión** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **ticket promedio** | Ingreso del periodo dividido por número de pedidos | Cuando **ticket promedio por segmento** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **paquete pertinente** | Combinación que el cliente usaría efectivamente en conjunto | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Subir el ticket puede reducir la frecuencia de compra. La evaluación debe considerar el ingreso por cliente en el periodo, no sólo el ticket por pedido.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre ticket promedio y paquetes |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como E-commerce manager, Marketplace specialist y Emprendedor. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El umbral de despacho gratis de Ruta Andina es CLP 60.000 y su ticket promedio es CLP 89.000: el incentivo se entrega a casi todos sin cambiar comportamiento.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **analizar qué productos se compran juntos → diseñar paquetes con lógica de uso real → definir umbrales de beneficio con margen verificado → medir efecto conjunto en ticket y en conversión → revisar devoluciones asociadas a los paquetes** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **ticket promedio por segmento**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Monetizing Innovation* y la de *Hillstrom's Multichannel Forensics*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **ticket promedio** y **paquete pertinente** como sinónimos | Se perdió la distinción entre «ingreso del periodo dividido por número de pedidos» y «combinación que el cliente usaría efectivamente en conjunto» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar devoluciones asociadas a los paquetes» | Se saltó «analizar qué productos se compran juntos»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **ticket promedio por segmento** | La métrica local reemplazó al resultado del sistema | Contrástala con **devoluciones de productos en paquete** y explicita el costo de oportunidad. |
| Fijar umbrales de beneficio bajo el ticket promedio | Error específico de esta clase | Ubica el umbral por sobre el ticket actual y verifica el efecto en margen y conversión. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **ticket promedio** y **paquete pertinente** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **umbral de beneficio** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «analizar qué productos se compran juntos» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **ticket promedio por segmento** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Subir el ticket puede reducir la frecuencia de compra. La evaluación debe considerar el ingreso por cliente en el periodo, no sólo el ticket por pedido»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **umbral de beneficio** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **ticket promedio por segmento**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Monetizing Innovation* y *The Strategy and Tactics of Pricing*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P15-C09-aov-y-bundles/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **ticket promedio por segmento**, **efecto en conversión** y **devoluciones de productos en paquete** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **simulación de tienda rentable con catálogo, checkout, costos y plan postventa**.

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

- Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) — **aporta a esta clase:** el empaquetado desde la disposición a pagar por atributo y no desde la arquitectura técnica. **Dónde buscarlo:** el capítulo sobre configuración y empaquetado. Registra edición y páginas consultadas en tu nota de lectura.
- Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) — **aporta a esta clase:** los patrones de recompra que distinguen un negocio de compra única de uno recurrente. **Dónde buscarlo:** los capítulos sobre ciclos de compra. Registra edición y páginas consultadas en tu nota de lectura.
- Peter Fader — *Customer Centricity* (2020, 2.ª ed.) — **aporta a esta clase:** recencia, frecuencia y valor como base de segmentación conductual. **Dónde buscarlo:** los capítulos sobre segmentación por comportamiento. Registra edición y páginas consultadas en tu nota de lectura.
- Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) — **aporta a esta clase:** las barreras de segmentación de precio y su legitimidad ante el cliente. **Dónde buscarlo:** el capítulo sobre estructura de precios. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 08 · Abandono de carrito](class-08-abandono-de-carrito.md) · [Índice de la parte](README.md) · [Clase 10 · Venta cruzada y venta incremental](class-10-cross-sell-y-upsell.md) →
