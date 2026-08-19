---
title: "Product-led growth"
type: class
language: es
standard: clase-profunda-v2
part: 19
class: 13
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["bush-plg", "ellis-brown", "cagan", "croll-yoskovitz"]
anchors: {"bush-plg": "autoservicio", "cagan": "resultado-output", "croll-yoskovitz": "modelos", "ellis-brown": "must-have"}
updated: 2026-08-19
---

# Clase 19.13 — Product-led growth

Clase 13 de 14 de la parte [19 — Growth marketing y growth engineering](README.md), de nivel Crecimiento y analítica. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 19.12, *Growth engineering*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de tasa de conversión autoservicio con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** Las condiciones que hacen viable el autoservicio: valor perceptible sin asistencia — Wes Bush. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

En el crecimiento liderado por producto, el propio producto adquiere, activa y expande: prueba gratuita o plan libre, valor perceptible sin intervención comercial y expansión por uso. No aplica a todos los negocios: requiere un producto que pueda usarse sin implementación asistida y un valor que se perciba rápido. Adoptarlo sin esas condiciones produce una base grande que no convierte.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 19 busca **instalar un motor de experimentación que produzca aprendizaje acumulativo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **product-led growth** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué bucle hace que el crecimiento se retroalimente en lugar de depender del gasto?

Los conceptos que estructuran la sesión son **autoservicio**, **valor perceptible sin ayuda**, **expansión por uso** y **condición de aplicabilidad**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `autoservicio`, `valor perceptible sin ayuda`, `expansión por uso` y `condición de aplicabilidad` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Growth marketing y growth engineering**.
3. **Aplicar** la secuencia **verificar si el producto puede usarse sin asistencia → medir el tiempo hasta el valor sin intervención → definir el gatillo de conversión y de expansión → instrumentar el recorrido completo → evaluar la economía del modelo antes de escalarlo** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **tasa de conversión autoservicio**, **tiempo hasta el valor sin asistencia** y **expansión por uso** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **autoservicio** y **valor perceptible sin ayuda** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **tasa de conversión autoservicio**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **autoservicio** | capacidad del cliente de contratar y usar sin intervención comercial | Construye un caso límite donde el concepto se confunde con el anterior. |
| **valor perceptible sin ayuda** | beneficio que el usuario obtiene por su cuenta en poco tiempo | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **expansión por uso** | aumento de ingreso que ocurre naturalmente al crecer el uso | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **condición de aplicabilidad** | conjunto de requisitos que hacen viable el modelo | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. verificar si el producto puede usarse sin asistencia → 2. medir el tiempo hasta el valor sin intervención → 3. definir el gatillo de conversión y de expansión → 4. instrumentar el recorrido completo → 5. evaluar la economía del modelo antes de escalarlo
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** El modelo reduce costo comercial y aumenta costo de producto y soporte. La economía debe evaluarse completa antes de decidir la transición.

## 📖 Desarrollo

### 1. Autoservicio: mecanismo central

**Autoservicio** se entiende aquí como **capacidad del cliente de contratar y usar sin intervención comercial**.

El crecimiento liderado por producto supone que el usuario puede descubrir, probar y adoptar sin intervención comercial. Esa condición no depende de la voluntad de la empresa sino de la naturaleza del producto: si requiere configuración, integración o cambio de proceso, el autoservicio no funcionará por más que se invierta en él.

**De dónde viene esta afirmación.** Wes Bush — *Product-Led Growth* (2019) aporta la idea que sostiene este bloque: las condiciones que hacen viable el autoservicio: valor perceptible sin asistencia. Búscala en los capítulos sobre el modelo liderado por producto. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «tasa de conversión autoservicio» debería moverse cuando cambie **autoservicio**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **valor perceptible sin ayuda**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Valor perceptible sin ayuda: frontera conceptual y error de clasificación

**Definición operacional:** beneficio que el usuario obtiene por su cuenta en poco tiempo. Su valor está en distinguirlo de **autoservicio**.

El valor perceptible sin ayuda es la prueba de aplicabilidad. Se verifica observando a usuarios reales intentando llegar al momento de valor sin acompañamiento y registrando dónde se detienen. Ese ejercicio, con cinco o seis personas, entrega un diagnóstico más útil que cualquier análisis de embudo.

**Contraste bibliográfico.** Sean Ellis y Morgan Brown — *Hacking Growth* (2017) aporta aquí una distinción concreta: la prueba de imprescindibilidad antes de acelerar la adquisición (los capítulos sobre encaje producto-mercado). Formula dos mini-casos: uno que satisface la definición de **valor perceptible sin ayuda** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «medir el tiempo hasta el valor sin intervención», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Expansión por uso: operacionalización y medición

**Expansión por uso** significa **aumento de ingreso que ocurre naturalmente al crecer el uso**.

La expansión por uso es el mecanismo de monetización característico del modelo: el cliente crece dentro del producto y el ingreso lo sigue. Requiere que la métrica de cobro esté alineada con el valor y que los límites del plan se alcancen de forma natural, no artificial.

Ficha de medición obligatoria para **tasa de conversión autoservicio**: `cuentas que pagan sin intervención comercial, sobre cuentas registradas`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Marty Cagan — *Inspired* (2017, 2.ª ed.) pone una condición sobre la medición: la orientación a resultado en lugar de a entrega de funcionalidades (los capítulos sobre equipos de producto). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Condición de aplicabilidad: trade-offs y efectos de segundo orden

**Definición:** conjunto de requisitos que hacen viable el modelo.

El autoservicio reduce el costo de adquisición y limita el ticket alcanzable; el modelo asistido permite negocios mayores y no escala igual. Muchas empresas terminan combinando ambos, y esa combinación exige definir con precisión dónde está la frontera y cómo se traspasan las cuentas entre modelos.

**Lo que aporta la fuente.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) aporta el criterio para pesar el intercambio: los seis modelos de negocio y las métricas que cambian entre ellos (la parte sobre modelos de negocio). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **expansión por uso** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **condición de aplicabilidad** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «evaluar la economía del modelo antes de escalarlo», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La condición de aplicabilidad debe verificarse antes de reorganizar la empresa alrededor del modelo. Adoptar el crecimiento liderado por producto en un negocio cuyo cliente no puede autoservirse produce una transformación costosa y un retroceso comercial. La verificación previa es barata comparada con ese error.

**Frontera declarada.** El modelo reduce costo comercial y aumenta costo de producto y soporte. La economía debe evaluarse completa antes de decidir la transición. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar product-led growth no consiste en sumar definiciones. Empieza por **autoservicio**, contrasta **valor perceptible sin ayuda** con **expansión por uso**, incorpora **condición de aplicabilidad** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Wes Bush — *Product-Led Growth* (2019) | Las condiciones que hacen viable el autoservicio: valor perceptible sin asistencia | Los capítulos sobre el modelo liderado por producto | ¿Qué debería observarse en **autoservicio** si aquí opera «las condiciones que hacen viable el autoservicio: valor perceptible sin asistencia»? ¿Y qué observación lo desmentiría en este caso? |
| Sean Ellis y Morgan Brown — *Hacking Growth* (2017) | La prueba de imprescindibilidad antes de acelerar la adquisición | Los capítulos sobre encaje producto-mercado | ¿Qué debería observarse en **valor perceptible sin ayuda** si aquí opera «la prueba de imprescindibilidad antes de acelerar la adquisición»? ¿Y qué observación lo desmentiría en este caso? |
| Marty Cagan — *Inspired* (2017, 2.ª ed.) | La orientación a resultado en lugar de a entrega de funcionalidades | Los capítulos sobre equipos de producto | ¿Qué debería observarse en **expansión por uso** si aquí opera «la orientación a resultado en lugar de a entrega de funcionalidades»? ¿Y qué observación lo desmentiría en este caso? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | Los seis modelos de negocio y las métricas que cambian entre ellos | La parte sobre modelos de negocio | ¿Qué debería observarse en **condición de aplicabilidad** si aquí opera «los seis modelos de negocio y las métricas que cambian entre ellos»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina quiere lanzar un plan self-service, pero su implementación exige migrar datos históricos que hoy hace una persona del equipo en cada cuenta.

**Paso 1 — Verificar si el producto puede usarse sin asistencia.** El equipo escribe primero el supuesto asociado a **autoservicio** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **tasa de conversión autoservicio** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Medir el tiempo hasta el valor sin intervención.** El trabajo aquí es separar lo observado de lo inferido sobre **valor perceptible sin ayuda**. La evidencia que ordena la discusión es **tiempo hasta el valor sin asistencia**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Definir el gatillo de conversión y de expansión.** El riesgo de este paso es cerrar demasiado rápido alrededor de **expansión por uso**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **expansión por uso** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Instrumentar el recorrido completo.** Con **condición de aplicabilidad** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **tasa de conversión autoservicio** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Evaluar la economía del modelo antes de escalarlo.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **autoservicio**. **tiempo hasta el valor sin asistencia** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **autoservicio** | Capacidad del cliente de contratar y usar sin intervención comercial | Cuando **tasa de conversión autoservicio** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **valor perceptible sin ayuda** | Beneficio que el usuario obtiene por su cuenta en poco tiempo | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** El modelo reduce costo comercial y aumenta costo de producto y soporte. La economía debe evaluarse completa antes de decidir la transición.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre product-led growth |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager, Growth engineer y Head of Growth. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina quiere lanzar un plan self-service, pero su implementación exige migrar datos históricos que hoy hace una persona del equipo en cada cuenta.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **verificar si el producto puede usarse sin asistencia → medir el tiempo hasta el valor sin intervención → definir el gatillo de conversión y de expansión → instrumentar el recorrido completo → evaluar la economía del modelo antes de escalarlo** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **tasa de conversión autoservicio**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Product-Led Growth* y la de *Hacking Growth*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **autoservicio** y **valor perceptible sin ayuda** como sinónimos | Se perdió la distinción entre «capacidad del cliente de contratar y usar sin intervención comercial» y «beneficio que el usuario obtiene por su cuenta en poco tiempo» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «evaluar la economía del modelo antes de escalarlo» | Se saltó «verificar si el producto puede usarse sin asistencia»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **tasa de conversión autoservicio** | La métrica local reemplazó al resultado del sistema | Contrástala con **expansión por uso** y explicita el costo de oportunidad. |
| Adoptar el modelo sin verificar el autoservicio real | Error específico de esta clase | Comprueba que un cliente pueda obtener valor sin intervención antes de lanzar el plan. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **autoservicio** y **valor perceptible sin ayuda** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **expansión por uso** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «verificar si el producto puede usarse sin asistencia» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **tasa de conversión autoservicio** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «El modelo reduce costo comercial y aumenta costo de producto y soporte. La economía debe evaluarse completa antes de decidir la transición»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **expansión por uso** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **tasa de conversión autoservicio**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Product-Led Growth* y *Lean Analytics*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, comprueba la norma en su texto vigente. Los enlaces van al texto completo publicado por la Biblioteca del Congreso Nacional; son gratuitos y no hace falta creerle a este material.

- **Consumo y comercio.** [Ley 19.496](https://www.bcn.cl/leychile/navegar?idNorma=61438) — *Establece normas sobre protección de los derechos de los consumidores* (Ministerio de Economía, Fomento y Reconstrucción), y su reglamento de comercio electrónico, [Decreto 6/2021](https://www.bcn.cl/leychile/navegar?idNorma=1165504) — *Aprueba reglamento de comercio electrónico* (Ministerio de Economía, Fomento y Turismo).
- **Datos personales.** [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales* (Ministerio Secretaría General de la Presidencia), que sustituye progresivamente a [Ley 19.628](https://www.bcn.cl/leychile/navegar?idNorma=141599) — *Sobre protección de la vida privada* (Ministerio Secretaría General de la Presidencia).
- **Derecho a retracto.** [Decreto 52/2024](https://www.bcn.cl/leychile/navegar?idNorma=1206144) — *Aprueba reglamento que regula la forma y condiciones en que los proveedores deberán comunicar la exclusión del derecho a retracto y los bienes en que excepcionalmente y por su naturaleza procederá tal exclusión* (Ministerio de Economía, Fomento y Turismo).

Dentro del repositorio, el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) ordena qué norma aplica a cada decisión comercial, [datos personales y ética](../../docs/DATOS-PERSONALES-Y-ETICA.md) desarrolla el tratamiento de datos y [fuentes oficiales](../../docs/FUENTES-OFICIALES.md) lista los organismos con su fecha de consulta. Ninguno de esos documentos reemplaza al texto legal.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P19-C13-product-led-growth/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **tasa de conversión autoservicio**, **tiempo hasta el valor sin asistencia** y **expansión por uso** con fuente, ventana y lectura prohibida.
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

Aquí conviene separar dos cosas que suelen ir juntas y no son lo mismo.

**Lo que está comprobado.** Que cada obra existe y cuál es exactamente la edición: el enlace resuelve su ISBN contra el catálogo de OpenLibrary, y eso se revalida periódicamente. Las normas chilenas citadas más arriba enlazan su texto completo y gratuito.

**Lo que es atribución del programa.** Que la idea señalada esté en el capítulo que se indica. Eso es la lectura que este material hace de cada obra, no una cita textual cotejada frase por frase, y se declara así de explícito para que puedas contrastarlo: si abres la obra y no encuentras la idea donde se dice, la cita está mal puesta y **corresponde reportarlo como error del material**. No se citan números de página porque cambian entre ediciones.

- Wes Bush — [*Product-Led Growth*](https://openlibrary.org/isbn/9781777119317) (2019) · ISBN 9781777119317 — **aporta a esta clase:** las condiciones que hacen viable el autoservicio: valor perceptible sin asistencia. **Dónde buscarlo:** los capítulos sobre el modelo liderado por producto. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Sean Ellis y Morgan Brown — [*Hacking Growth*](https://openlibrary.org/isbn/9780451497215) (2017) · ISBN 9780451497215 — **aporta a esta clase:** la prueba de imprescindibilidad antes de acelerar la adquisición. **Dónde buscarlo:** los capítulos sobre encaje producto-mercado. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Marty Cagan — [*Inspired*](https://openlibrary.org/isbn/9781119387541) (2017, 2.ª ed.) · ISBN 9781119387541 — **aporta a esta clase:** la orientación a resultado en lugar de a entrega de funcionalidades. **Dónde buscarlo:** los capítulos sobre equipos de producto. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Alistair Croll y Benjamin Yoskovitz — [*Lean Analytics*](https://openlibrary.org/isbn/9781449335670) (2013) · ISBN 9781449335670 — **aporta a esta clase:** los seis modelos de negocio y las métricas que cambian entre ellos. **Dónde buscarlo:** la parte sobre modelos de negocio. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 12 · Growth engineering](class-12-growth-engineering.md) · [Índice de la parte](README.md) · [Clase 14 · Growth model completo](class-14-growth-model-completo.md) →
