---
title: "Catálogo y merchandising digital"
type: class
language: es
standard: clase-profunda-v2
part: 15
class: 02
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["krug", "flint", "eisenberg", "chaffey"]
anchors: {"chaffey": "omnicanal", "eisenberg": "escenarios", "flint": "migracion-clientes", "krug": "jerarquia-visual"}
updated: 2026-08-19
---

# Clase 15.02 — Catálogo y merchandising digital

**Parte 15 · E-commerce y marketplaces** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 15.01 — *Modelo operativo de e-commerce*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de completitud de atributos para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La jerarquía visual como traducción de la importancia relativa — Steve Krug. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

El catálogo es la estructura que permite encontrar: categorías, atributos, filtros y nomenclatura. Un catálogo mal estructurado obliga al visitante a buscar y la mayoría no lo hace: se va. El merchandising digital decide qué se muestra primero, y esa decisión debe responder a margen y disponibilidad, no sólo a popularidad.

Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales. La parte 15 busca **operar una tienda y un canal de marketplace con economía verificable**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **catálogo y merchandising digital** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Dónde se pierde el pedido y cuánto queda después de comisión, envío y devolución?

Los conceptos que estructuran la sesión son **taxonomía de catálogo**, **calidad del dato de producto**, **merchandising** y **descubribilidad**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `taxonomía de catálogo`, `calidad del dato de producto`, `merchandising` y `descubribilidad` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **E-commerce y marketplaces**.
3. **Aplicar** la secuencia **auditar la completitud de atributos del catálogo → definir la taxonomía desde el vocabulario del cliente → configurar filtros útiles y verificarlos → priorizar el destacado por margen y disponibilidad → medir búsquedas sin resultado y corregir** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **completitud de atributos**, **búsquedas sin resultado** y **conversión por categoría** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **taxonomía de catálogo** y **calidad del dato de producto** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **completitud de atributos**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **taxonomía de catálogo** | estructura de categorías y atributos que organiza los productos | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **calidad del dato de producto** | completitud y exactitud de los atributos que permiten filtrar y comparar | Construye un caso límite donde el concepto se confunde con el anterior. |
| **merchandising** | decisión sobre qué productos se destacan y en qué orden | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **descubribilidad** | facilidad con que un visitante encuentra el producto que busca | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. auditar la completitud de atributos del catálogo → 2. definir la taxonomía desde el vocabulario del cliente → 3. configurar filtros útiles y verificarlos → 4. priorizar el destacado por margen y disponibilidad → 5. medir búsquedas sin resultado y corregir
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un catálogo excesivamente detallado aumenta el costo de mantenimiento. La profundidad debe corresponder a los atributos que el cliente usa para decidir.

## 📖 Desarrollo

### 1. Taxonomía de catálogo: mecanismo central

**Taxonomía de catálogo** se entiende aquí como **estructura de categorías y atributos que organiza los productos**.

El catálogo es la interfaz principal de un comercio digital y su calidad determina cuánto se encuentra y cuánto se compra. Una taxonomía construida desde la lógica interna —por proveedor, por código de sistema— obliga al cliente a aprender la organización de la empresa. Una construida desde cómo busca el cliente reduce el esfuerzo y aumenta la descubribilidad.

**De dónde viene esta afirmación.** Steve Krug — *Don't Make Me Think, Revisited* (2014) aporta la idea que sostiene este bloque: la jerarquía visual como traducción de la importancia relativa. Búscala en el capítulo sobre diseño de páginas. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «completitud de atributos» debería moverse cuando cambie **taxonomía de catálogo**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **calidad del dato de producto**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Calidad del dato de producto: frontera conceptual y error de clasificación

**Definición operacional:** completitud y exactitud de los atributos que permiten filtrar y comparar. Su valor está en distinguirlo de **taxonomía de catálogo**.

La calidad del dato de producto es la base de todo lo demás: títulos consistentes, atributos completos, imágenes que muestran lo que importa. Un producto sin atributos no aparece en los filtros y por lo tanto no existe para quien navega filtrando. Medir la completitud de atributos por categoría es un diagnóstico rápido y revelador.

**Contraste bibliográfico.** Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) aporta aquí una distinción concreta: el análisis de migración de clientes entre canales y categorías (los capítulos sobre comportamiento multicanal). Formula dos mini-casos: uno que satisface la definición de **calidad del dato de producto** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «definir la taxonomía desde el vocabulario del cliente», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Merchandising: operacionalización y medición

**Merchandising** significa **decisión sobre qué productos se destacan y en qué orden**.

La descubribilidad se mide con datos propios: qué proporción de los productos del catálogo recibió al menos una visita en el periodo, y qué proporción de las búsquedas internas terminó sin resultados. Ese segundo dato es especialmente valioso porque indica demanda expresada que la operación no está capturando.

Ficha de medición obligatoria para **completitud de atributos**: `productos con atributos obligatorios completos, sobre productos publicados`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Bryan Eisenberg y Jeffrey Eisenberg — *Call to Action* (2005) pone una condición sobre la medición: los escenarios de conversión construidos desde la intención del visitante (los capítulos sobre planificación de escenarios). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Descubribilidad: trade-offs y efectos de segundo orden

**Definición:** facilidad con que un visitante encuentra el producto que busca.

Un catálogo amplio ofrece más opciones y dificulta la elección, además de multiplicar el costo de mantener datos actualizados. Uno acotado facilita la decisión y deja demanda sin atender. La decisión debe considerar la capacidad real de mantener la calidad del dato: un catálogo grande con información deficiente rinde peor que uno pequeño y bien descrito.

**Lo que aporta la fuente.** Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) aporta el criterio para pesar el intercambio: la integración de la experiencia entre canales digitales y físicos (los capítulos sobre multicanalidad). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **conversión por categoría** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **descubribilidad** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «medir búsquedas sin resultado y corregir», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La información del producto obliga: características, compatibilidades, plazos y condiciones publicadas forman parte de lo ofrecido. En Chile, la normativa de consumo exige información veraz y oportuna, y los errores en fichas de producto generan responsabilidad. El control de calidad del dato no es sólo una cuestión de conversión.

**Frontera declarada.** Un catálogo excesivamente detallado aumenta el costo de mantenimiento. La profundidad debe corresponder a los atributos que el cliente usa para decidir. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar catálogo y merchandising digital no consiste en sumar definiciones. Empieza por **taxonomía de catálogo**, contrasta **calidad del dato de producto** con **merchandising**, incorpora **descubribilidad** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Steve Krug — *Don't Make Me Think, Revisited* (2014) | La jerarquía visual como traducción de la importancia relativa | El capítulo sobre diseño de páginas | ¿Qué debería observarse en **taxonomía de catálogo** si aquí opera «la jerarquía visual como traducción de la importancia relativa»? ¿Y qué observación lo desmentiría en este caso? |
| Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) | El análisis de migración de clientes entre canales y categorías | Los capítulos sobre comportamiento multicanal | ¿Qué debería observarse en **calidad del dato de producto** si aquí opera «el análisis de migración de clientes entre canales y categorías»? ¿Y qué observación lo desmentiría en este caso? |
| Bryan Eisenberg y Jeffrey Eisenberg — *Call to Action* (2005) | Los escenarios de conversión construidos desde la intención del visitante | Los capítulos sobre planificación de escenarios | ¿Qué debería observarse en **merchandising** si aquí opera «los escenarios de conversión construidos desde la intención del visitante»? ¿Y qué observación lo desmentiría en este caso? |
| Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) | La integración de la experiencia entre canales digitales y físicos | Los capítulos sobre multicanalidad | ¿Qué debería observarse en **descubribilidad** si aquí opera «la integración de la experiencia entre canales digitales y físicos»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El 34 % de las búsquedas internas en la tienda de Ruta Andina no devuelve resultados porque los productos están cargados con nombres técnicos que nadie usa.

**Paso 1 — Auditar la completitud de atributos del catálogo.** El equipo escribe primero el supuesto asociado a **taxonomía de catálogo** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **completitud de atributos** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Definir la taxonomía desde el vocabulario del cliente.** El trabajo aquí es separar lo observado de lo inferido sobre **calidad del dato de producto**. La evidencia que ordena la discusión es **búsquedas sin resultado**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Configurar filtros útiles y verificarlos.** El riesgo de este paso es cerrar demasiado rápido alrededor de **merchandising**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **conversión por categoría** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Priorizar el destacado por margen y disponibilidad.** Con **descubribilidad** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **completitud de atributos** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Medir búsquedas sin resultado y corregir.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **taxonomía de catálogo**. **búsquedas sin resultado** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **taxonomía de catálogo** | Estructura de categorías y atributos que organiza los productos | Cuando **completitud de atributos** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **calidad del dato de producto** | Completitud y exactitud de los atributos que permiten filtrar y comparar | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un catálogo excesivamente detallado aumenta el costo de mantenimiento. La profundidad debe corresponder a los atributos que el cliente usa para decidir.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre catálogo y merchandising digital |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como E-commerce manager, Marketplace specialist y Emprendedor. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El 34 % de las búsquedas internas en la tienda de Ruta Andina no devuelve resultados porque los productos están cargados con nombres técnicos que nadie usa.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **auditar la completitud de atributos del catálogo → definir la taxonomía desde el vocabulario del cliente → configurar filtros útiles y verificarlos → priorizar el destacado por margen y disponibilidad → medir búsquedas sin resultado y corregir** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **completitud de atributos**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Don't Make Me Think, Revisited* y la de *Hillstrom's Multichannel Forensics*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **taxonomía de catálogo** y **calidad del dato de producto** como sinónimos | Se perdió la distinción entre «estructura de categorías y atributos que organiza los productos» y «completitud y exactitud de los atributos que permiten filtrar y comparar» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «medir búsquedas sin resultado y corregir» | Se saltó «auditar la completitud de atributos del catálogo»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **completitud de atributos** | La métrica local reemplazó al resultado del sistema | Contrástala con **conversión por categoría** y explicita el costo de oportunidad. |
| Nombrar productos con vocabulario interno | Error específico de esta clase | Usa los términos con que los clientes buscan, verificados en el informe de búsqueda interna. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **taxonomía de catálogo** y **calidad del dato de producto** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **merchandising** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «auditar la completitud de atributos del catálogo» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **completitud de atributos** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un catálogo excesivamente detallado aumenta el costo de mantenimiento. La profundidad debe corresponder a los atributos que el cliente usa para decidir»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **merchandising** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **completitud de atributos**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Don't Make Me Think, Revisited* y *Digital Marketing*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P15-C02-catalogo-y-merchandising-digital/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **completitud de atributos**, **búsquedas sin resultado** y **conversión por categoría** con fuente, ventana y lectura prohibida.
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

- Steve Krug — *Don't Make Me Think, Revisited* (2014) — **aporta a esta clase:** la jerarquía visual como traducción de la importancia relativa. **Dónde buscarlo:** el capítulo sobre diseño de páginas. Registra edición y páginas consultadas en tu nota de lectura.
- Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) — **aporta a esta clase:** el análisis de migración de clientes entre canales y categorías. **Dónde buscarlo:** los capítulos sobre comportamiento multicanal. Registra edición y páginas consultadas en tu nota de lectura.
- Bryan Eisenberg y Jeffrey Eisenberg — *Call to Action* (2005) — **aporta a esta clase:** los escenarios de conversión construidos desde la intención del visitante. **Dónde buscarlo:** los capítulos sobre planificación de escenarios. Registra edición y páginas consultadas en tu nota de lectura.
- Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) — **aporta a esta clase:** la integración de la experiencia entre canales digitales y físicos. **Dónde buscarlo:** los capítulos sobre multicanalidad. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 01 · Modelo operativo de e-commerce](class-01-modelo-operativo-e-commerce.md) · [Índice de la parte](README.md) · [Clase 03 · Página de producto](class-03-product-detail-page.md) →
