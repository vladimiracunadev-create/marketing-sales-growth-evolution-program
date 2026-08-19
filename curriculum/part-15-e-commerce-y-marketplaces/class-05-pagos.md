---
title: "Pagos"
type: class
language: es
standard: clase-profunda-v2
part: 15
class: 05
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["flint", "chaffey", "croll-yoskovitz", "krug"]
anchors: {"chaffey": "gobierno-digital", "croll-yoskovitz": "modelos", "flint": "valor-canal", "krug": "no-pensar"}
updated: 2026-08-19
---

# Clase 15.05 — Pagos

**Parte 15 · E-commerce y marketplaces** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 15.04 — *Checkout*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de tasa de aprobación por medio para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La contribución real de cada canal descontando lo que habría ocurrido igual — Kevin Hillstrom. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Los medios de pago determinan quién puede comprar y cuánto cuesta cada transacción. En Chile conviven débito, crédito, transferencia y billeteras, con costos y tasas de aprobación distintos. Las decisiones relevantes son tres: qué medios ofrecer según el segmento, cómo manejar los rechazos y cómo prevenir el fraude sin bloquear compras legítimas.

La clase trata el tema como un problema de evidencia y de consecuencia, no como vocabulario. La parte 15 busca **operar una tienda y un canal de marketplace con economía verificable**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **pagos** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Dónde se pierde el pedido y cuánto queda después de comisión, envío y devolución?

Los conceptos que estructuran la sesión son **tasa de aprobación**, **costo de la transacción**, **contracargo** y **falso rechazo**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `tasa de aprobación`, `costo de la transacción`, `contracargo` y `falso rechazo` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **E-commerce y marketplaces**.
3. **Aplicar** la secuencia **identificar los medios que usa el segmento → medir aprobación y costo por medio → analizar las causas de rechazo → calibrar las reglas antifraude con datos de contracargos → revisar la mezcla de medios cada semestre** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **tasa de aprobación por medio**, **costo de pagos sobre ingreso** y **tasa de contracargos** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **tasa de aprobación** y **costo de la transacción** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **tasa de aprobación por medio**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **tasa de aprobación** | transacciones aprobadas sobre transacciones intentadas, por medio de pago | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **costo de la transacción** | comisión y costos asociados a cada medio de pago | Da un hecho compatible con la definición y otro que la refute. |
| **contracargo** | reversión de un pago solicitada por el titular, con su costo asociado | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **falso rechazo** | transacción legítima bloqueada por reglas de prevención de fraude | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. identificar los medios que usa el segmento → 2. medir aprobación y costo por medio → 3. analizar las causas de rechazo → 4. calibrar las reglas antifraude con datos de contracargos → 5. revisar la mezcla de medios cada semestre
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Ampliar medios de pago aumenta el costo de conciliación y de operación. La decisión debe considerar el costo administrativo, no sólo la comisión.

## 📖 Desarrollo

### 1. Tasa de aprobación: mecanismo central

**Tasa de aprobación** se entiende aquí como **transacciones aprobadas sobre transacciones intentadas, por medio de pago**.

Los medios de pago determinan qué proporción de las intenciones de compra se convierte efectivamente en ingreso. La tasa de aprobación —cuántas transacciones intentadas se completan— es una métrica operativa que rara vez se monitorea y que puede explicar pérdidas significativas sin que nadie las atribuya a esa causa.

**De dónde viene esta afirmación.** Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) aporta la idea que sostiene este bloque: la contribución real de cada canal descontando lo que habría ocurrido igual. Búscala en los capítulos sobre análisis forense de canales. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «tasa de aprobación por medio» debería moverse cuando cambie **tasa de aprobación**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **costo de la transacción**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Costo de la transacción: frontera conceptual y error de clasificación

**Definición operacional:** comisión y costos asociados a cada medio de pago. Su valor está en distinguirlo de **tasa de aprobación**.

El falso rechazo es una transacción legítima bloqueada por un control antifraude demasiado estricto. Su costo es doble: se pierde la venta y se daña la relación con un cliente que no hizo nada mal. Ajustar los umbrales de control exige comparar el costo del fraude aceptado con el de las ventas rechazadas, y ese cálculo casi nunca se hace.

**Contraste bibliográfico.** Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) aporta aquí una distinción concreta: el gobierno de la operación digital: capacidades, procesos y medición (los capítulos sobre transformación y capacidades). Formula dos mini-casos: uno que satisface la definición de **costo de la transacción** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «medir aprobación y costo por medio», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Contracargo: operacionalización y medición

**Contracargo** significa **reversión de un pago solicitada por el titular, con su costo asociado**.

El costo de la transacción varía por medio de pago y puede representar una porción relevante del margen en categorías de ticket bajo. Calcular el margen neto por medio de pago permite decidir cuáles promover y cuáles ofrecer con condiciones distintas, dentro de lo que la normativa permite.

Ficha de medición obligatoria para **tasa de aprobación por medio**: `transacciones aprobadas, sobre intentadas, por medio de pago`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) pone una condición sobre la medición: los seis modelos de negocio y las métricas que cambian entre ellos (la parte sobre modelos de negocio). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Falso rechazo: trade-offs y efectos de segundo orden

**Definición:** transacción legítima bloqueada por reglas de prevención de fraude.

Ofrecer más medios de pago aumenta la conversión y multiplica la complejidad operativa, de conciliación y de soporte. Cada medio adicional exige integración, monitoreo y procedimientos de excepción. La decisión debe considerar qué proporción de la demanda quedaría sin atender sin ese medio, dato estimable con encuestas breves en el checkout.

**Lo que aporta la fuente.** Steve Krug — *Don't Make Me Think, Revisited* (2014) aporta el criterio para pesar el intercambio: la primera ley: la página no debe obligar a pensar dónde está uno ni qué hacer (los capítulos iniciales sobre usabilidad). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **tasa de contracargos** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **falso rechazo** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar la mezcla de medios cada semestre», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El tratamiento de datos de pago está sujeto a estándares específicos de seguridad y a obligaciones normativas. La operación no debe almacenar información sensible de tarjetas salvo bajo condiciones muy determinadas. La verificación de esos requisitos con el proveedor de pagos y con asesoría especializada es previa a cualquier implementación.

**Frontera declarada.** Ampliar medios de pago aumenta el costo de conciliación y de operación. La decisión debe considerar el costo administrativo, no sólo la comisión. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar pagos no consiste en sumar definiciones. Empieza por **tasa de aprobación**, contrasta **costo de la transacción** con **contracargo**, incorpora **falso rechazo** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) | La contribución real de cada canal descontando lo que habría ocurrido igual | Los capítulos sobre análisis forense de canales | ¿Qué debería observarse en **tasa de aprobación** si aquí opera «la contribución real de cada canal descontando lo que habría ocurrido igual»? ¿Y qué observación lo desmentiría en este caso? |
| Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) | El gobierno de la operación digital: capacidades, procesos y medición | Los capítulos sobre transformación y capacidades | ¿Qué debería observarse en **costo de la transacción** si aquí opera «el gobierno de la operación digital: capacidades, procesos y medición»? ¿Y qué observación lo desmentiría en este caso? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | Los seis modelos de negocio y las métricas que cambian entre ellos | La parte sobre modelos de negocio | ¿Qué debería observarse en **contracargo** si aquí opera «los seis modelos de negocio y las métricas que cambian entre ellos»? ¿Y qué observación lo desmentiría en este caso? |
| Steve Krug — *Don't Make Me Think, Revisited* (2014) | La primera ley: la página no debe obligar a pensar dónde está uno ni qué hacer | Los capítulos iniciales sobre usabilidad | ¿Qué debería observarse en **falso rechazo** si aquí opera «la primera ley: la página no debe obligar a pensar dónde está uno ni qué hacer»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El 22 % de las transacciones de Ruta Andina se rechaza. La causa principal es una regla antifraude que bloquea compras de regiones distintas a la de facturación.

**Paso 1 — Identificar los medios que usa el segmento.** El equipo escribe primero el supuesto asociado a **tasa de aprobación** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **tasa de aprobación por medio** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Medir aprobación y costo por medio.** El trabajo aquí es separar lo observado de lo inferido sobre **costo de la transacción**. La evidencia que ordena la discusión es **costo de pagos sobre ingreso**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Analizar las causas de rechazo.** El riesgo de este paso es cerrar demasiado rápido alrededor de **contracargo**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **tasa de contracargos** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Calibrar las reglas antifraude con datos de contracargos.** Con **falso rechazo** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **tasa de aprobación por medio** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar la mezcla de medios cada semestre.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **tasa de aprobación**. **costo de pagos sobre ingreso** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **tasa de aprobación** | Transacciones aprobadas sobre transacciones intentadas, por medio de pago | Cuando **tasa de aprobación por medio** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **costo de la transacción** | Comisión y costos asociados a cada medio de pago | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Ampliar medios de pago aumenta el costo de conciliación y de operación. La decisión debe considerar el costo administrativo, no sólo la comisión.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre pagos |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como E-commerce manager, Marketplace specialist y Emprendedor. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El 22 % de las transacciones de Ruta Andina se rechaza. La causa principal es una regla antifraude que bloquea compras de regiones distintas a la de facturación.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **identificar los medios que usa el segmento → medir aprobación y costo por medio → analizar las causas de rechazo → calibrar las reglas antifraude con datos de contracargos → revisar la mezcla de medios cada semestre** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **tasa de aprobación por medio**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Hillstrom's Multichannel Forensics* y la de *Digital Marketing*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **tasa de aprobación** y **costo de la transacción** como sinónimos | Se perdió la distinción entre «transacciones aprobadas sobre transacciones intentadas, por medio de pago» y «comisión y costos asociados a cada medio de pago» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar la mezcla de medios cada semestre» | Se saltó «identificar los medios que usa el segmento»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **tasa de aprobación por medio** | La métrica local reemplazó al resultado del sistema | Contrástala con **tasa de contracargos** y explicita el costo de oportunidad. |
| Calibrar reglas antifraude sin medir falsos rechazos | Error específico de esta clase | Compara contracargos evitados contra ventas legítimas bloqueadas antes de endurecer las reglas. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **tasa de aprobación** y **costo de la transacción** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **contracargo** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «identificar los medios que usa el segmento» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **tasa de aprobación por medio** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Ampliar medios de pago aumenta el costo de conciliación y de operación. La decisión debe considerar el costo administrativo, no sólo la comisión»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **contracargo** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **tasa de aprobación por medio**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Hillstrom's Multichannel Forensics* y *Don't Make Me Think, Revisited*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P15-C05-pagos/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **tasa de aprobación por medio**, **costo de pagos sobre ingreso** y **tasa de contracargos** con fuente, ventana y lectura prohibida.
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
- Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) — **aporta a esta clase:** el gobierno de la operación digital: capacidades, procesos y medición. **Dónde buscarlo:** los capítulos sobre transformación y capacidades. Registra edición y páginas consultadas en tu nota de lectura.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — **aporta a esta clase:** los seis modelos de negocio y las métricas que cambian entre ellos. **Dónde buscarlo:** la parte sobre modelos de negocio. Registra edición y páginas consultadas en tu nota de lectura.
- Steve Krug — *Don't Make Me Think, Revisited* (2014) — **aporta a esta clase:** la primera ley: la página no debe obligar a pensar dónde está uno ni qué hacer. **Dónde buscarlo:** los capítulos iniciales sobre usabilidad. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 04 · Checkout](class-04-checkout.md) · [Índice de la parte](README.md) · [Clase 06 · Fulfillment](class-06-fulfillment.md) →
