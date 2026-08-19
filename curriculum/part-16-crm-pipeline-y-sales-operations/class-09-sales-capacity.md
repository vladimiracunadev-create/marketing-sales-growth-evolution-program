---
title: "Capacidad comercial"
type: class
language: es
standard: clase-profunda-v2
part: 16
class: 09
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["roberge", "zoltners", "grove", "ross"]
anchors: {"grove": "apalancamiento", "roberge": "contratacion-datos", "ross": "especializacion", "zoltners": "territorios"}
updated: 2026-08-19
---

# Clase 16.09 — Capacidad comercial

**Parte 16 · CRM, pipeline y sales operations** · Nivel: Operación de ingresos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 16.08 — *Cuotas y territorios*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de tiempo comercial efectivo para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El perfil de contratación derivado del desempeño observado en la propia empresa — Mark Roberge. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La capacidad comercial es la cantidad de negocio que el equipo puede trabajar con calidad, considerando el tiempo real disponible y el esfuerzo que exige cada tipo de oportunidad. Planificar crecimiento sin calcularla produce dos errores simétricos: generar demanda que nadie atiende o contratar personas para un pipeline que no existe.

Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales. La parte 16 busca **convertir el CRM en un sistema de trabajo y de verdad operacional**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **capacidad comercial** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿El pipeline describe la realidad o solo el optimismo del equipo?

Los conceptos que estructuran la sesión son **capacidad por vendedor**, **tiempo comercial efectivo**, **rampa de productividad** y **capacidad del sistema**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `capacidad por vendedor`, `tiempo comercial efectivo`, `rampa de productividad` y `capacidad del sistema` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **CRM, pipeline y sales operations**.
3. **Aplicar** la secuencia **medir el tiempo comercial efectivo del equipo → estimar el esfuerzo por tipo de oportunidad → calcular la capacidad actual del sistema → considerar la rampa antes de proyectar contrataciones → ajustar la generación de demanda a la capacidad** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **tiempo comercial efectivo**, **oportunidades activas por vendedor** y **duración de la rampa** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **capacidad por vendedor** y **tiempo comercial efectivo** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **tiempo comercial efectivo**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **capacidad por vendedor** | número de oportunidades que una persona puede trabajar con calidad simultáneamente | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **tiempo comercial efectivo** | horas realmente disponibles para actividad de venta tras descontar tareas internas | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **rampa de productividad** | tiempo que tarda una incorporación en alcanzar desempeño pleno | Da un hecho compatible con la definición y otro que la refute. |
| **capacidad del sistema** | resultado agregado que la estructura actual puede producir | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. medir el tiempo comercial efectivo del equipo → 2. estimar el esfuerzo por tipo de oportunidad → 3. calcular la capacidad actual del sistema → 4. considerar la rampa antes de proyectar contrataciones → 5. ajustar la generación de demanda a la capacidad
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** La capacidad no es fija: depende del proceso, de las herramientas y del tipo de negocio. Mejorar el proceso puede aumentar la capacidad sin contratar.

## 📖 Desarrollo

### 1. Capacidad por vendedor: mecanismo central

**Capacidad por vendedor** se entiende aquí como **número de oportunidades que una persona puede trabajar con calidad simultáneamente**.

La capacidad comercial es una restricción física que casi nunca se calcula: cuántas oportunidades puede atender bien una persona en un periodo. Planificar sobre una capacidad inexistente produce pipelines saturados, oportunidades mal atendidas y la conclusión errónea de que el equipo no rinde.

**De dónde viene esta afirmación.** Mark Roberge — *The Sales Acceleration Formula* (2015) aporta la idea que sostiene este bloque: el perfil de contratación derivado del desempeño observado en la propia empresa. Búscala en los capítulos sobre la fórmula de contratación. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «tiempo comercial efectivo» debería moverse cuando cambie **capacidad por vendedor**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **tiempo comercial efectivo**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Tiempo comercial efectivo: frontera conceptual y error de clasificación

**Definición operacional:** horas realmente disponibles para actividad de venta tras descontar tareas internas. Su valor está en distinguirlo de **capacidad por vendedor**.

El tiempo comercial efectivo es la porción del tiempo que se dedica realmente a actividades con clientes, y suele ser mucho menor de lo que se supone. Medirlo durante dos semanas —aunque sea de forma aproximada— revela cuánto se va en tareas administrativas, reuniones internas y coordinación. Esa medición justifica inversiones en automatización mejor que cualquier argumento.

**Contraste bibliográfico.** Andris A. Zoltners, Prabhakant Sinha y Sally E. Lorimer — *The Complete Guide to Sales Force Incentive Compensation* (2006) aporta aquí una distinción concreta: el diseño de territorios y la equidad de oportunidad entre vendedores (los capítulos sobre alineación de territorios). Formula dos mini-casos: uno que satisface la definición de **tiempo comercial efectivo** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «estimar el esfuerzo por tipo de oportunidad», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Rampa de productividad: operacionalización y medición

**Rampa de productividad** significa **tiempo que tarda una incorporación en alcanzar desempeño pleno**.

La rampa de productividad es el tiempo que tarda una persona nueva en alcanzar el desempeño esperado, y es un dato que debe conocerse para planificar contrataciones. Contratar tres meses antes de necesitar la capacidad no es previsión excesiva si la rampa es de cuatro meses: es la única forma de tener la capacidad cuando se necesita.

Ficha de medición obligatoria para **tiempo comercial efectivo**: `horas de actividad comercial, sobre horas laborales totales, por vendedor`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Andrew S. Grove — *High Output Management* (1983) pone una condición sobre la medición: el apalancamiento gerencial: qué actividades multiplican el output (los capítulos sobre apalancamiento). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Capacidad del sistema: trade-offs y efectos de segundo orden

**Definición:** resultado agregado que la estructura actual puede producir.

Aumentar la capacidad contratando produce resultado con retraso y compromete costo fijo inmediato. Aumentarla mejorando la eficiencia es más lento y no agrega costo estructural. La decisión debe considerar la rampa, la certeza de la demanda y la reversibilidad, porque revertir una contratación tiene costos humanos y económicos.

**Lo que aporta la fuente.** Aaron Ross y Marylou Tyler — *Predictable Revenue* (2011) aporta el criterio para pesar el intercambio: la especialización de roles comerciales: prospección, cierre y gestión separados (los capítulos sobre especialización del equipo). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **duración de la rampa** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **capacidad del sistema** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «ajustar la generación de demanda a la capacidad», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La capacidad del sistema está limitada por el eslabón más restringido, que no siempre es ventas: puede ser implementación, soporte o producción. Aumentar la capacidad comercial cuando el cuello está aguas abajo produce ventas que la operación no puede cumplir, lo que es peor que no venderlas.

**Frontera declarada.** La capacidad no es fija: depende del proceso, de las herramientas y del tipo de negocio. Mejorar el proceso puede aumentar la capacidad sin contratar. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Tomar decisiones de contratación y presupuesto sobre un pipeline que no representa la realidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar capacidad comercial no consiste en sumar definiciones. Empieza por **capacidad por vendedor**, contrasta **tiempo comercial efectivo** con **rampa de productividad**, incorpora **capacidad del sistema** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Mark Roberge — *The Sales Acceleration Formula* (2015) | El perfil de contratación derivado del desempeño observado en la propia empresa | Los capítulos sobre la fórmula de contratación | ¿Qué debería observarse en **capacidad por vendedor** si aquí opera «el perfil de contratación derivado del desempeño observado en la propia empresa»? ¿Y qué observación lo desmentiría en este caso? |
| Andris A. Zoltners, Prabhakant Sinha y Sally E. Lorimer — *The Complete Guide to Sales Force Incentive Compensation* (2006) | El diseño de territorios y la equidad de oportunidad entre vendedores | Los capítulos sobre alineación de territorios | ¿Qué debería observarse en **tiempo comercial efectivo** si aquí opera «el diseño de territorios y la equidad de oportunidad entre vendedores»? ¿Y qué observación lo desmentiría en este caso? |
| Andrew S. Grove — *High Output Management* (1983) | El apalancamiento gerencial: qué actividades multiplican el output | Los capítulos sobre apalancamiento | ¿Qué debería observarse en **rampa de productividad** si aquí opera «el apalancamiento gerencial: qué actividades multiplican el output»? ¿Y qué observación lo desmentiría en este caso? |
| Aaron Ross y Marylou Tyler — *Predictable Revenue* (2011) | La especialización de roles comerciales: prospección, cierre y gestión separados | Los capítulos sobre especialización del equipo | ¿Qué debería observarse en **capacidad del sistema** si aquí opera «la especialización de roles comerciales: prospección, cierre y gestión separados»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina planea generar 400 oportunidades mensuales con un equipo de seis personas que dedica el 38 % de su tiempo a tareas administrativas.

**Paso 1 — Medir el tiempo comercial efectivo del equipo.** El equipo escribe primero el supuesto asociado a **capacidad por vendedor** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **tiempo comercial efectivo** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Estimar el esfuerzo por tipo de oportunidad.** El trabajo aquí es separar lo observado de lo inferido sobre **tiempo comercial efectivo**. La evidencia que ordena la discusión es **oportunidades activas por vendedor**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Calcular la capacidad actual del sistema.** El riesgo de este paso es cerrar demasiado rápido alrededor de **rampa de productividad**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **duración de la rampa** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Considerar la rampa antes de proyectar contrataciones.** Con **capacidad del sistema** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **tiempo comercial efectivo** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Ajustar la generación de demanda a la capacidad.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **capacidad por vendedor**. **oportunidades activas por vendedor** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **capacidad por vendedor** | Número de oportunidades que una persona puede trabajar con calidad simultáneamente | Cuando **tiempo comercial efectivo** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **tiempo comercial efectivo** | Horas realmente disponibles para actividad de venta tras descontar tareas internas | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** La capacidad no es fija: depende del proceso, de las herramientas y del tipo de negocio. Mejorar el proceso puede aumentar la capacidad sin contratar.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre capacidad comercial |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Sales operations, RevOps analyst y Jefe de ventas. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina planea generar 400 oportunidades mensuales con un equipo de seis personas que dedica el 38 % de su tiempo a tareas administrativas.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **medir el tiempo comercial efectivo del equipo → estimar el esfuerzo por tipo de oportunidad → calcular la capacidad actual del sistema → considerar la rampa antes de proyectar contrataciones → ajustar la generación de demanda a la capacidad** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **tiempo comercial efectivo**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *The Sales Acceleration Formula* y la de *The Complete Guide to Sales Force Incentive Compensation*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **capacidad por vendedor** y **tiempo comercial efectivo** como sinónimos | Se perdió la distinción entre «número de oportunidades que una persona puede trabajar con calidad simultáneamente» y «horas realmente disponibles para actividad de venta tras descontar tareas internas» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «ajustar la generación de demanda a la capacidad» | Se saltó «medir el tiempo comercial efectivo del equipo»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **tiempo comercial efectivo** | La métrica local reemplazó al resultado del sistema | Contrástala con **duración de la rampa** y explicita el costo de oportunidad. |
| Proyectar crecimiento sin calcular capacidad | Error específico de esta clase | Mide el tiempo comercial efectivo y la carga por oportunidad antes de comprometer metas. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **capacidad por vendedor** y **tiempo comercial efectivo** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **rampa de productividad** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «medir el tiempo comercial efectivo del equipo» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **tiempo comercial efectivo** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «La capacidad no es fija: depende del proceso, de las herramientas y del tipo de negocio. Mejorar el proceso puede aumentar la capacidad sin contratar»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **rampa de productividad** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **tiempo comercial efectivo**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *The Sales Acceleration Formula* y *Predictable Revenue*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Tomar decisiones de contratación y presupuesto sobre un pipeline que no representa la realidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P16-C09-sales-capacity/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **tiempo comercial efectivo**, **oportunidades activas por vendedor** y **duración de la rampa** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **diseño de sales operations con pipeline, criterios de etapa, forecast y gobierno de datos**.

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

- Mark Roberge — *The Sales Acceleration Formula* (2015) — **aporta a esta clase:** el perfil de contratación derivado del desempeño observado en la propia empresa. **Dónde buscarlo:** los capítulos sobre la fórmula de contratación. Registra edición y páginas consultadas en tu nota de lectura.
- Andris A. Zoltners, Prabhakant Sinha y Sally E. Lorimer — *The Complete Guide to Sales Force Incentive Compensation* (2006) — **aporta a esta clase:** el diseño de territorios y la equidad de oportunidad entre vendedores. **Dónde buscarlo:** los capítulos sobre alineación de territorios. Registra edición y páginas consultadas en tu nota de lectura.
- Andrew S. Grove — *High Output Management* (1983) — **aporta a esta clase:** el apalancamiento gerencial: qué actividades multiplican el output. **Dónde buscarlo:** los capítulos sobre apalancamiento. Registra edición y páginas consultadas en tu nota de lectura.
- Aaron Ross y Marylou Tyler — *Predictable Revenue* (2011) — **aporta a esta clase:** la especialización de roles comerciales: prospección, cierre y gestión separados. **Dónde buscarlo:** los capítulos sobre especialización del equipo. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 08 · Cuotas y territorios](class-08-cuotas-y-territorios.md) · [Índice de la parte](README.md) · [Clase 10 · Velocidad comercial](class-10-sales-velocity.md) →
