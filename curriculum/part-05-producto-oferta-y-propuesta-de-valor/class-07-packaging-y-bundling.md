---
title: "Packaging y bundling"
type: class
language: es
standard: clase-profunda-v2
part: 05
class: 07
level: Oferta comercial
mastery_threshold: 80
estimated_minutes: 150
sources: ["ramanujam", "nagle", "smith-pricing", "ariely"]
anchors: {"ariely": "relatividad", "nagle": "segmentacion-precio", "ramanujam": "empaquetado", "smith-pricing": "versionado"}
updated: 2026-08-19
---

# Clase 05.07 — Packaging y bundling

**Parte 05 · Producto, oferta y propuesta de valor** · Nivel: Oferta comercial · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 05.06 — *Diseño de ofertas*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de distribución de ventas por plan para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El empaquetado desde la disposición a pagar por atributo y no desde la arquitectura técnica — Madhavan Ramanujam y Georg Tacke. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Empaquetar es decidir qué va junto y qué se vende por separado. Un buen empaquetado alinea el precio con el valor recibido y facilita la elección; uno malo obliga a pagar por lo que no se usa o fragmenta tanto que nadie entiende qué comprar. Ramanujam propone diseñar los paquetes desde la disposición a pagar por atributo, y no desde la arquitectura técnica del producto.

Esta sesión distingue lo que se sabe, lo que se supone y lo que todavía no se ha medido. La parte 05 busca **convertir una capacidad técnica en una oferta que alguien quiera comprar hoy**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **packaging y bundling** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué compra realmente el cliente y por qué elegiría esta oferta frente a no hacer nada?

Los conceptos que estructuran la sesión son **paquete**, **componente diferenciador**, **componente de volumen** y **canibalización de planes**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `paquete`, `componente diferenciador`, `componente de volumen` y `canibalización de planes` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Producto, oferta y propuesta de valor**.
3. **Aplicar** la secuencia **medir disposición a pagar por atributo → clasificar atributos en diferenciadores, de volumen y opcionales → construir dos o tres paquetes con lógica clara → simular canibalización y margen por escenario → probar la estructura antes de publicarla** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **distribución de ventas por plan**, **tasa de migración entre planes** y **margen por paquete** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **paquete** y **componente diferenciador** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **distribución de ventas por plan**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **paquete** | combinación de componentes ofrecida como unidad con un precio propio | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **componente diferenciador** | atributo con alta disposición a pagar que justifica un plan superior | Construye un caso límite donde el concepto se confunde con el anterior. |
| **componente de volumen** | atributo de bajo valor incremental que conviene incluir en todos los planes | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **canibalización de planes** | traslado de clientes desde un plan superior a uno inferior por diseño del paquete | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. medir disposición a pagar por atributo → 2. clasificar atributos en diferenciadores, de volumen y opcionales → 3. construir dos o tres paquetes con lógica clara → 4. simular canibalización y margen por escenario → 5. probar la estructura antes de publicarla
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Más paquetes no es mejor: la elección excesiva reduce conversión. Tres alternativas claras suelen superar a siete opciones matizadas.

## 📖 Desarrollo

### 1. Paquete: mecanismo central

**Paquete** se entiende aquí como **combinación de componentes ofrecida como unidad con un precio propio**.

Empaquetar es decidir qué va junto y qué se cobra aparte, y esa decisión define el precio efectivo de cada segmento. El error habitual es armar los paquetes según la arquitectura técnica del producto —lo que es fácil de separar— en lugar de según la disposición a pagar por atributo, que es lo que determina el ingreso.

**De dónde viene esta afirmación.** Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) aporta la idea que sostiene este bloque: el empaquetado desde la disposición a pagar por atributo y no desde la arquitectura técnica. Búscala en el capítulo sobre configuración y empaquetado. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «distribución de ventas por plan» debería moverse cuando cambie **paquete**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **componente diferenciador**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Componente diferenciador: frontera conceptual y error de clasificación

**Definición operacional:** atributo con alta disposición a pagar que justifica un plan superior. Su valor está en distinguirlo de **paquete**.

El componente diferenciador es aquel por el que un segmento paga y otro no; el de volumen es el que todos usan. Ubicar el diferenciador en el plan básico regala margen; ubicar un componente de volumen en el plan alto obliga a todos a subir y genera resistencia. Identificar cuál es cuál exige evidencia de uso, no intuición de producto.

**Contraste bibliográfico.** Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) aporta aquí una distinción concreta: las barreras de segmentación de precio y su legitimidad ante el cliente (el capítulo sobre estructura de precios). Formula dos mini-casos: uno que satisface la definición de **componente diferenciador** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «clasificar atributos en diferenciadores, de volumen y opcionales», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Componente de volumen: operacionalización y medición

**Componente de volumen** significa **atributo de bajo valor incremental que conviene incluir en todos los planes**.

La canibalización entre planes se mide observando la migración: qué proporción de clientes que habrían comprado el plan superior compra el intermedio tras un cambio de empaquetado. Requiere definir la ventana y la cohorte, y compararla con el periodo anterior. Sin esa medición, un cambio de paquetes que baja el ingreso medio se interpreta como éxito porque suben las unidades.

Ficha de medición obligatoria para **distribución de ventas por plan**: `unidades y margen por plan, sobre ventas totales del periodo`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Tim J. Smith — *Pricing Strategy* (2011) pone una condición sobre la medición: el versionado como mecanismo de captura en segmentos con disposición distinta (los capítulos sobre estructura de la oferta). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Canibalización de planes: trade-offs y efectos de segundo orden

**Definición:** traslado de clientes desde un plan superior a uno inferior por diseño del paquete.

Más planes permiten capturar mejor la disposición a pagar y aumentan la carga cognitiva de la decisión, con lo que reducen la conversión. La evidencia sobre exceso de opciones es consistente y el punto de equilibrio suele estar en tres. Agregar un cuarto plan exige justificar qué segmento quedaba sin capturar y con qué evidencia.

**Lo que aporta la fuente.** Dan Ariely — *Predictably Irrational* (2008) aporta el criterio para pesar el intercambio: la relatividad: la opción señuelo cambia la elección entre las otras dos (el capítulo sobre relatividad). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **margen por paquete** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **canibalización de planes** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «probar la estructura antes de publicarla», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El empaquetado se diseña con supuestos sobre valoración que cambian con el mercado y con el producto. Un esquema que funcionó dos años puede volverse incoherente tras agregar funcionalidades. La revisión periódica del empaquetado es una tarea permanente y no un proyecto: cuando se trata como proyecto, se revisa cada tres años y se pierde ingreso todo ese tiempo.

**Frontera declarada.** Más paquetes no es mejor: la elección excesiva reduce conversión. Tres alternativas claras suelen superar a siete opciones matizadas. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Prometer resultados que la operación no puede sostener y generar churn temprano.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar packaging y bundling no consiste en sumar definiciones. Empieza por **paquete**, contrasta **componente diferenciador** con **componente de volumen**, incorpora **canibalización de planes** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) | El empaquetado desde la disposición a pagar por atributo y no desde la arquitectura técnica | El capítulo sobre configuración y empaquetado | ¿Qué debería observarse en **paquete** si aquí opera «el empaquetado desde la disposición a pagar por atributo y no desde la arquitectura técnica»? ¿Y qué observación lo desmentiría en este caso? |
| Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) | Las barreras de segmentación de precio y su legitimidad ante el cliente | El capítulo sobre estructura de precios | ¿Qué debería observarse en **componente diferenciador** si aquí opera «las barreras de segmentación de precio y su legitimidad ante el cliente»? ¿Y qué observación lo desmentiría en este caso? |
| Tim J. Smith — *Pricing Strategy* (2011) | El versionado como mecanismo de captura en segmentos con disposición distinta | Los capítulos sobre estructura de la oferta | ¿Qué debería observarse en **componente de volumen** si aquí opera «el versionado como mecanismo de captura en segmentos con disposición distinta»? ¿Y qué observación lo desmentiría en este caso? |
| Dan Ariely — *Predictably Irrational* (2008) | La relatividad: la opción señuelo cambia la elección entre las otras dos | El capítulo sobre relatividad | ¿Qué debería observarse en **canibalización de planes** si aquí opera «la relatividad: la opción señuelo cambia la elección entre las otras dos»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina tiene cinco planes y el 78 % de las ventas se concentra en el más barato porque incluye el módulo de pagos, que es el atributo más valorado.

**Paso 1 — Medir disposición a pagar por atributo.** El equipo escribe primero el supuesto asociado a **paquete** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **distribución de ventas por plan** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Clasificar atributos en diferenciadores, de volumen y opcionales.** El trabajo aquí es separar lo observado de lo inferido sobre **componente diferenciador**. La evidencia que ordena la discusión es **tasa de migración entre planes**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Construir dos o tres paquetes con lógica clara.** El riesgo de este paso es cerrar demasiado rápido alrededor de **componente de volumen**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **margen por paquete** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Simular canibalización y margen por escenario.** Con **canibalización de planes** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **distribución de ventas por plan** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Probar la estructura antes de publicarla.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **paquete**. **tasa de migración entre planes** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **paquete** | Combinación de componentes ofrecida como unidad con un precio propio | Cuando **distribución de ventas por plan** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **componente diferenciador** | Atributo con alta disposición a pagar que justifica un plan superior | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Más paquetes no es mejor: la elección excesiva reduce conversión. Tres alternativas claras suelen superar a siete opciones matizadas.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre packaging y bundling |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Product marketing, Product manager y Founder. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina tiene cinco planes y el 78 % de las ventas se concentra en el más barato porque incluye el módulo de pagos, que es el atributo más valorado.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **medir disposición a pagar por atributo → clasificar atributos en diferenciadores, de volumen y opcionales → construir dos o tres paquetes con lógica clara → simular canibalización y margen por escenario → probar la estructura antes de publicarla** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **distribución de ventas por plan**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Monetizing Innovation* y la de *The Strategy and Tactics of Pricing*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **paquete** y **componente diferenciador** como sinónimos | Se perdió la distinción entre «combinación de componentes ofrecida como unidad con un precio propio» y «atributo con alta disposición a pagar que justifica un plan superior» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «probar la estructura antes de publicarla» | Se saltó «medir disposición a pagar por atributo»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **distribución de ventas por plan** | La métrica local reemplazó al resultado del sistema | Contrástala con **margen por paquete** y explicita el costo de oportunidad. |
| Diseñar planes desde la arquitectura técnica | Error específico de esta clase | Construye los paquetes desde la disposición a pagar por atributo, medida en el segmento. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **paquete** y **componente diferenciador** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **componente de volumen** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «medir disposición a pagar por atributo» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **distribución de ventas por plan** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Más paquetes no es mejor: la elección excesiva reduce conversión. Tres alternativas claras suelen superar a siete opciones matizadas»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **componente de volumen** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **distribución de ventas por plan**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Monetizing Innovation* y *Predictably Irrational*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Prometer resultados que la operación no puede sostener y generar churn temprano.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P05-C07-packaging-y-bundling/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **distribución de ventas por plan**, **tasa de migración entre planes** y **margen por paquete** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **oferta lista para vender con propuesta de valor, alcance, garantía y prueba de concepto**.

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
- Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) — **aporta a esta clase:** las barreras de segmentación de precio y su legitimidad ante el cliente. **Dónde buscarlo:** el capítulo sobre estructura de precios. Registra edición y páginas consultadas en tu nota de lectura.
- Tim J. Smith — *Pricing Strategy* (2011) — **aporta a esta clase:** el versionado como mecanismo de captura en segmentos con disposición distinta. **Dónde buscarlo:** los capítulos sobre estructura de la oferta. Registra edición y páginas consultadas en tu nota de lectura.
- Dan Ariely — *Predictably Irrational* (2008) — **aporta a esta clase:** la relatividad: la opción señuelo cambia la elección entre las otras dos. **Dónde buscarlo:** el capítulo sobre relatividad. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 06 · Diseño de ofertas](class-06-diseno-de-ofertas.md) · [Índice de la parte](README.md) · [Clase 08 · Garantías y reducción de riesgo](class-08-garantias-y-reduccion-de-riesgo.md) →
