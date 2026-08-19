---
title: "Marketplaces"
type: class
language: es
standard: clase-profunda-v2
part: 15
class: 11
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["flint", "chaffey", "porter", "nagle"]
anchors: {"chaffey": "modelo-canal", "flint": "valor-canal", "nagle": "cascada", "porter": "cinco-fuerzas"}
updated: 2026-08-19
---

# Clase 15.11 — Marketplaces

**Parte 15 · E-commerce y marketplaces** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 15.10 — *Venta cruzada y venta incremental*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de margen neto por producto en marketplace para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La contribución real de cada canal descontando lo que habría ocurrido igual — Kevin Hillstrom. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Un marketplace entrega tráfico y confianza a cambio de comisión, reglas y pérdida de relación con el cliente. Es una decisión estratégica, no sólo un canal más: quien vende allí acepta competir por precio en una vitrina donde el diferenciador visible es limitado. La evaluación correcta compara margen neto y aprendizaje obtenido, no volumen.

El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta. La parte 15 busca **operar una tienda y un canal de marketplace con economía verificable**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **marketplaces** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Dónde se pierde el pedido y cuánto queda después de comisión, envío y devolución?

Los conceptos que estructuran la sesión son **comisión efectiva**, **pérdida de relación**, **competencia en vitrina** y **dependencia del canal**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `comisión efectiva`, `pérdida de relación`, `competencia en vitrina` y `dependencia del canal` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **E-commerce y marketplaces**.
3. **Aplicar** la secuencia **calcular la comisión efectiva total → evaluar el margen neto por producto en el canal → definir qué productos corresponden al canal y cuáles no → medir la dependencia y fijar un límite → usar el canal para aprendizaje de demanda, no sólo para volumen** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **margen neto por producto en marketplace**, **dependencia del canal** y **diferencial de precio con tienda propia** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **comisión efectiva** y **pérdida de relación** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **margen neto por producto en marketplace**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **comisión efectiva** | porcentaje total retenido incluyendo comisión, publicidad interna y servicios | Da un hecho compatible con la definición y otro que la refute. |
| **pérdida de relación** | imposibilidad de contactar directamente al cliente y construir base propia | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **competencia en vitrina** | presión de precio provocada por la comparación directa en el mismo espacio | Construye un caso límite donde el concepto se confunde con el anterior. |
| **dependencia del canal** | riesgo de que un cambio de reglas afecte una parte sustantiva del ingreso | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. calcular la comisión efectiva total → 2. evaluar el margen neto por producto en el canal → 3. definir qué productos corresponden al canal y cuáles no → 4. medir la dependencia y fijar un límite → 5. usar el canal para aprendizaje de demanda, no sólo para volumen
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Salir de un marketplace donde se tiene volumen puede afectar la caja de inmediato. La transición debe planificarse con construcción previa de canal propio.

## 📖 Desarrollo

### 1. Comisión efectiva: mecanismo central

**Comisión efectiva** se entiende aquí como **porcentaje total retenido incluyendo comisión, publicidad interna y servicios**.

Vender en un marketplace es acceder a demanda existente a cambio de comisión y de pérdida de relación con el cliente. Ese intercambio puede ser excelente al inicio y problemático al escalar, porque la dependencia crece y el poder de negociación se desplaza hacia la plataforma.

**De dónde viene esta afirmación.** Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) aporta la idea que sostiene este bloque: la contribución real de cada canal descontando lo que habría ocurrido igual. Búscala en los capítulos sobre análisis forense de canales. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «margen neto por producto en marketplace» debería moverse cuando cambie **comisión efectiva**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **pérdida de relación**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Pérdida de relación: frontera conceptual y error de clasificación

**Definición operacional:** imposibilidad de contactar directamente al cliente y construir base propia. Su valor está en distinguirlo de **comisión efectiva**.

La comisión efectiva incluye más que el porcentaje declarado: costos de publicidad interna necesarios para tener visibilidad, promociones obligatorias, costos logísticos del programa. Calcularla completa suele mostrar una diferencia relevante respecto de la comisión nominal, y esa cifra es la que debe compararse con el costo de adquirir el mismo cliente por canal propio.

**Contraste bibliográfico.** Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) aporta aquí una distinción concreta: el modelo de contribución de canal a la conversión (los capítulos sobre estrategia de canales). Formula dos mini-casos: uno que satisface la definición de **pérdida de relación** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «evaluar el margen neto por producto en el canal», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Competencia en vitrina: operacionalización y medición

**Competencia en vitrina** significa **presión de precio provocada por la comparación directa en el mismo espacio**.

La pérdida de relación es el costo estratégico: sin datos del cliente, no hay retención posible y cada venta es una transacción aislada. Medir qué proporción del ingreso proviene de canales donde no se posee la relación es un indicador de riesgo estructural que debería estar en la revisión de dirección.

Ficha de medición obligatoria para **margen neto por producto en marketplace**: `ingreso menos comisiones y costos, sobre ingreso del canal`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Michael E. Porter — *Competitive Strategy* (1980) pone una condición sobre la medición: las cinco fuerzas que determinan la rentabilidad estructural de una industria (el capítulo sobre análisis estructural de industrias). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Dependencia del canal: trade-offs y efectos de segundo orden

**Definición:** riesgo de que un cambio de reglas afecte una parte sustantiva del ingreso.

Aumentar la presencia en marketplaces acelera el volumen y consolida la dependencia; reducirla protege la relación y sacrifica acceso a demanda. La estrategia razonable define un techo de dependencia aceptable y trabaja activamente en canales propios mientras el marketplace financia la operación.

**Lo que aporta la fuente.** Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) aporta el criterio para pesar el intercambio: la cascada de precio: del precio de lista al precio de bolsillo tras descuentos y concesiones (el capítulo sobre gestión del precio realizado). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **diferencial de precio con tienda propia** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **dependencia del canal** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «usar el canal para aprendizaje de demanda, no sólo para volumen», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Las reglas de la plataforma pueden cambiar unilateralmente: comisiones, visibilidad, condiciones de participación. Una operación cuya viabilidad depende de esas reglas está expuesta a decisiones ajenas. Ese riesgo debe declararse y monitorearse, y el plan debe contemplar qué se hace si las condiciones cambian de forma adversa.

**Frontera declarada.** Salir de un marketplace donde se tiene volumen puede afectar la caja de inmediato. La transición debe planificarse con construcción previa de canal propio. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar marketplaces no consiste en sumar definiciones. Empieza por **comisión efectiva**, contrasta **pérdida de relación** con **competencia en vitrina**, incorpora **dependencia del canal** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) | La contribución real de cada canal descontando lo que habría ocurrido igual | Los capítulos sobre análisis forense de canales | ¿Qué debería observarse en **comisión efectiva** si aquí opera «la contribución real de cada canal descontando lo que habría ocurrido igual»? ¿Y qué observación lo desmentiría en este caso? |
| Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) | El modelo de contribución de canal a la conversión | Los capítulos sobre estrategia de canales | ¿Qué debería observarse en **pérdida de relación** si aquí opera «el modelo de contribución de canal a la conversión»? ¿Y qué observación lo desmentiría en este caso? |
| Michael E. Porter — *Competitive Strategy* (1980) | Las cinco fuerzas que determinan la rentabilidad estructural de una industria | El capítulo sobre análisis estructural de industrias | ¿Qué debería observarse en **competencia en vitrina** si aquí opera «las cinco fuerzas que determinan la rentabilidad estructural de una industria»? ¿Y qué observación lo desmentiría en este caso? |
| Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) | La cascada de precio: del precio de lista al precio de bolsillo tras descuentos y concesiones | El capítulo sobre gestión del precio realizado | ¿Qué debería observarse en **dependencia del canal** si aquí opera «la cascada de precio: del precio de lista al precio de bolsillo tras descuentos y concesiones»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El marketplace representa el 28 % de las unidades de Ruta Andina y el 4 % del margen. Además impide contactar a esos clientes para vender el software.

**Paso 1 — Calcular la comisión efectiva total.** El equipo escribe primero el supuesto asociado a **comisión efectiva** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **margen neto por producto en marketplace** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Evaluar el margen neto por producto en el canal.** El trabajo aquí es separar lo observado de lo inferido sobre **pérdida de relación**. La evidencia que ordena la discusión es **dependencia del canal**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Definir qué productos corresponden al canal y cuáles no.** El riesgo de este paso es cerrar demasiado rápido alrededor de **competencia en vitrina**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **diferencial de precio con tienda propia** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Medir la dependencia y fijar un límite.** Con **dependencia del canal** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **margen neto por producto en marketplace** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Usar el canal para aprendizaje de demanda, no sólo para volumen.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **comisión efectiva**. **dependencia del canal** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **comisión efectiva** | Porcentaje total retenido incluyendo comisión, publicidad interna y servicios | Cuando **margen neto por producto en marketplace** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **pérdida de relación** | Imposibilidad de contactar directamente al cliente y construir base propia | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Salir de un marketplace donde se tiene volumen puede afectar la caja de inmediato. La transición debe planificarse con construcción previa de canal propio.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre marketplaces |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como E-commerce manager, Marketplace specialist y Emprendedor. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El marketplace representa el 28 % de las unidades de Ruta Andina y el 4 % del margen. Además impide contactar a esos clientes para vender el software.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **calcular la comisión efectiva total → evaluar el margen neto por producto en el canal → definir qué productos corresponden al canal y cuáles no → medir la dependencia y fijar un límite → usar el canal para aprendizaje de demanda, no sólo para volumen** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **margen neto por producto en marketplace**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Hillstrom's Multichannel Forensics* y la de *Digital Marketing*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **comisión efectiva** y **pérdida de relación** como sinónimos | Se perdió la distinción entre «porcentaje total retenido incluyendo comisión, publicidad interna y servicios» y «imposibilidad de contactar directamente al cliente y construir base propia» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «usar el canal para aprendizaje de demanda, no sólo para volumen» | Se saltó «calcular la comisión efectiva total»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **margen neto por producto en marketplace** | La métrica local reemplazó al resultado del sistema | Contrástala con **diferencial de precio con tienda propia** y explicita el costo de oportunidad. |
| Medir el marketplace por volumen de unidades | Error específico de esta clase | Calcula la comisión efectiva total y el margen neto antes de decidir la permanencia. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **comisión efectiva** y **pérdida de relación** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **competencia en vitrina** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «calcular la comisión efectiva total» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **margen neto por producto en marketplace** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Salir de un marketplace donde se tiene volumen puede afectar la caja de inmediato. La transición debe planificarse con construcción previa de canal propio»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **competencia en vitrina** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **margen neto por producto en marketplace**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Hillstrom's Multichannel Forensics* y *The Strategy and Tactics of Pricing*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P15-C11-marketplaces/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **margen neto por producto en marketplace**, **dependencia del canal** y **diferencial de precio con tienda propia** con fuente, ventana y lectura prohibida.
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

- Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) — **aporta a esta clase:** la contribución real de cada canal descontando lo que habría ocurrido igual. **Dónde buscarlo:** los capítulos sobre análisis forense de canales. Registra edición y páginas consultadas en tu nota de lectura.
- Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) — **aporta a esta clase:** el modelo de contribución de canal a la conversión. **Dónde buscarlo:** los capítulos sobre estrategia de canales. Registra edición y páginas consultadas en tu nota de lectura.
- Michael E. Porter — *Competitive Strategy* (1980) — **aporta a esta clase:** las cinco fuerzas que determinan la rentabilidad estructural de una industria. **Dónde buscarlo:** el capítulo sobre análisis estructural de industrias. Registra edición y páginas consultadas en tu nota de lectura.
- Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) — **aporta a esta clase:** la cascada de precio: del precio de lista al precio de bolsillo tras descuentos y concesiones. **Dónde buscarlo:** el capítulo sobre gestión del precio realizado. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 10 · Venta cruzada y venta incremental](class-10-cross-sell-y-upsell.md) · [Índice de la parte](README.md) · [Clase 12 · Postventa](class-12-postventa.md) →
