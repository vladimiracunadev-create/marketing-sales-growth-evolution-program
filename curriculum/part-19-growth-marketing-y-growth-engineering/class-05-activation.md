---
title: "Activación"
type: class
language: es
standard: clase-profunda-v2
part: 19
class: 05
level: Crecimiento y analítica
mastery_threshold: 80
estimated_minutes: 150
sources: ["ellis-brown", "hulick", "croll-yoskovitz", "kohavi"]
anchors: {"croll-yoskovitz": "cohortes", "ellis-brown": "aha", "hulick": "primer-exito", "kohavi": "efecto-minimo"}
updated: 2026-08-19
---

# Clase 19.05 — Activación

**Parte 19 · Growth marketing y growth engineering** · Nivel: Crecimiento y analítica · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 19.04 — *Growth loops*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de tasa de activación para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El momento «ajá» identificado con datos y no supuesto — Sean Ellis y Morgan Brown. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La activación es el momento en que el usuario experimenta el valor del producto por primera vez. Identificarla con precisión es una tarea analítica: consiste en encontrar qué acción, realizada en qué plazo, predice la permanencia. Una vez identificada, todo el diseño inicial debe orientarse a que ocurra lo antes posible.

La clase trata el tema como un problema de evidencia y de consecuencia, no como vocabulario. La parte 19 busca **instalar un motor de experimentación que produzca aprendizaje acumulativo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **activación** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué bucle hace que el crecimiento se retroalimente en lugar de depender del gasto?

Los conceptos que estructuran la sesión son **evento de activación**, **ventana de activación**, **análisis predictivo de activación** y **tasa de activación**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `evento de activación`, `ventana de activación`, `análisis predictivo de activación` y `tasa de activación` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Growth marketing y growth engineering**.
3. **Aplicar** la secuencia **analizar qué acciones distinguen a quienes permanecen → definir el evento y la ventana de activación → medir la tasa actual por segmento y origen → rediseñar el inicio para producir ese evento antes → verificar el efecto sobre la retención de las cohortes nuevas** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **tasa de activación**, **retención por activación** y **tiempo hasta la activación** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **evento de activación** y **ventana de activación** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **tasa de activación**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **evento de activación** | acción cuya realización predice la permanencia del usuario | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **ventana de activación** | plazo dentro del cual esa acción debe ocurrir para predecir retención | Da un hecho compatible con la definición y otro que la refute. |
| **análisis predictivo de activación** | método que identifica el evento a partir de datos históricos | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **tasa de activación** | usuarios que realizan el evento en la ventana, sobre usuarios incorporados | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. analizar qué acciones distinguen a quienes permanecen → 2. definir el evento y la ventana de activación → 3. medir la tasa actual por segmento y origen → 4. rediseñar el inicio para producir ese evento antes → 5. verificar el efecto sobre la retención de las cohortes nuevas
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** La correlación entre el evento y la retención no prueba causalidad: puede que quienes ya estaban comprometidos hagan ambas cosas. Verificarlo requiere un experimento.

## 📖 Desarrollo

### 1. Evento de activación: mecanismo central

**Evento de activación** se entiende aquí como **acción cuya realización predice la permanencia del usuario**.

La activación es el momento en que el usuario obtiene por primera vez el valor que el producto promete. No es el registro ni la primera sesión: es la acción que se correlaciona con la permanencia. Identificarla con datos, comparando el comportamiento temprano de quienes se quedan y quienes se van, es el análisis fundacional de cualquier programa de crecimiento.

**De dónde viene esta afirmación.** Sean Ellis y Morgan Brown — *Hacking Growth* (2017) aporta la idea que sostiene este bloque: el momento «ajá» identificado con datos y no supuesto. Búscala en los capítulos sobre el momento de valor. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «tasa de activación» debería moverse cuando cambie **evento de activación**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **ventana de activación**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Ventana de activación: frontera conceptual y error de clasificación

**Definición operacional:** plazo dentro del cual esa acción debe ocurrir para predecir retención. Su valor está en distinguirlo de **evento de activación**.

El evento de activación debe ser específico y observable. «Entendió el producto» no lo es; «completó su primera hoja de ruta y la exportó» sí. Esa precisión permite medir la tasa de activación, construir el onboarding hacia ella y evaluar si las intervenciones funcionan.

**Contraste bibliográfico.** Samuel Hulick — *The Elements of User Onboarding* (2014) aporta aquí una distinción concreta: el onboarding diseñado hacia el primer éxito y no hacia el recorrido del producto (los capítulos sobre objetivos del onboarding). Formula dos mini-casos: uno que satisface la definición de **ventana de activación** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «definir el evento y la ventana de activación», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Análisis predictivo de activación: operacionalización y medición

**Análisis predictivo de activación** significa **método que identifica el evento a partir de datos históricos**.

La ventana de activación —el plazo dentro del cual debe ocurrir— es parte de la definición. Un usuario que activa a los tres meses no se comporta como uno que activa el primer día. Definir la ventana con datos, observando a partir de cuándo la probabilidad de activación cae, evita perseguir usuarios que ya se perdieron.

Ficha de medición obligatoria para **tasa de activación**: `usuarios activados en la ventana, sobre usuarios incorporados`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) pone una condición sobre la medición: el análisis de cohortes como corrección al promedio que esconde la mezcla (el capítulo sobre cohortes y segmentación). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Tasa de activación: trade-offs y efectos de segundo orden

**Definición:** usuarios que realizan el evento en la ventana, sobre usuarios incorporados.

Reducir los pasos hasta la activación mejora la tasa y puede producir usuarios que activan sin entender, y que abandonan después. La medición correcta observa la retención posterior de los activados y no sólo la tasa de activación, porque optimizar la segunda a costa de la primera es fácil y contraproducente.

**Lo que aporta la fuente.** Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) aporta el criterio para pesar el intercambio: el efecto mínimo relevante como base del cálculo de muestra (los capítulos sobre potencia y tamaño de muestra). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **tiempo hasta la activación** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **tasa de activación** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «verificar el efecto sobre la retención de las cohortes nuevas», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La activación se define para un producto y un segmento. Un mismo producto puede tener eventos de activación distintos según el caso de uso, y promediarlos oculta ambos. Cuando la tasa de activación es estable pero la retención varía mucho, esa mezcla es la primera hipótesis a revisar.

**Frontera declarada.** La correlación entre el evento y la retención no prueba causalidad: puede que quienes ya estaban comprometidos hagan ambas cosas. Verificarlo requiere un experimento. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar activación no consiste en sumar definiciones. Empieza por **evento de activación**, contrasta **ventana de activación** con **análisis predictivo de activación**, incorpora **tasa de activación** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Sean Ellis y Morgan Brown — *Hacking Growth* (2017) | El momento «ajá» identificado con datos y no supuesto | Los capítulos sobre el momento de valor | ¿Qué debería observarse en **evento de activación** si aquí opera «el momento «ajá» identificado con datos y no supuesto»? ¿Y qué observación lo desmentiría en este caso? |
| Samuel Hulick — *The Elements of User Onboarding* (2014) | El onboarding diseñado hacia el primer éxito y no hacia el recorrido del producto | Los capítulos sobre objetivos del onboarding | ¿Qué debería observarse en **ventana de activación** si aquí opera «el onboarding diseñado hacia el primer éxito y no hacia el recorrido del producto»? ¿Y qué observación lo desmentiría en este caso? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | El análisis de cohortes como corrección al promedio que esconde la mezcla | El capítulo sobre cohortes y segmentación | ¿Qué debería observarse en **análisis predictivo de activación** si aquí opera «el análisis de cohortes como corrección al promedio que esconde la mezcla»? ¿Y qué observación lo desmentiría en este caso? |
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | El efecto mínimo relevante como base del cálculo de muestra | Los capítulos sobre potencia y tamaño de muestra | ¿Qué debería observarse en **tasa de activación** si aquí opera «el efecto mínimo relevante como base del cálculo de muestra»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El análisis de Ruta Andina muestra que quienes cargan más de 20 clientes en la primera semana retienen 3,4 veces más. Sólo el 22 % lo hace.

**Paso 1 — Analizar qué acciones distinguen a quienes permanecen.** El equipo escribe primero el supuesto asociado a **evento de activación** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **tasa de activación** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Definir el evento y la ventana de activación.** El trabajo aquí es separar lo observado de lo inferido sobre **ventana de activación**. La evidencia que ordena la discusión es **retención por activación**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Medir la tasa actual por segmento y origen.** El riesgo de este paso es cerrar demasiado rápido alrededor de **análisis predictivo de activación**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **tiempo hasta la activación** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Rediseñar el inicio para producir ese evento antes.** Con **tasa de activación** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **tasa de activación** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Verificar el efecto sobre la retención de las cohortes nuevas.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **evento de activación**. **retención por activación** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **evento de activación** | Acción cuya realización predice la permanencia del usuario | Cuando **tasa de activación** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **ventana de activación** | Plazo dentro del cual esa acción debe ocurrir para predecir retención | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** La correlación entre el evento y la retención no prueba causalidad: puede que quienes ya estaban comprometidos hagan ambas cosas. Verificarlo requiere un experimento.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre activación |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager, Growth engineer y Head of Growth. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El análisis de Ruta Andina muestra que quienes cargan más de 20 clientes en la primera semana retienen 3,4 veces más. Sólo el 22 % lo hace.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **analizar qué acciones distinguen a quienes permanecen → definir el evento y la ventana de activación → medir la tasa actual por segmento y origen → rediseñar el inicio para producir ese evento antes → verificar el efecto sobre la retención de las cohortes nuevas** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **tasa de activación**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Hacking Growth* y la de *The Elements of User Onboarding*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **evento de activación** y **ventana de activación** como sinónimos | Se perdió la distinción entre «acción cuya realización predice la permanencia del usuario» y «plazo dentro del cual esa acción debe ocurrir para predecir retención» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «verificar el efecto sobre la retención de las cohortes nuevas» | Se saltó «analizar qué acciones distinguen a quienes permanecen»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **tasa de activación** | La métrica local reemplazó al resultado del sistema | Contrástala con **tiempo hasta la activación** y explicita el costo de oportunidad. |
| Confundir correlación con causalidad en el evento de activación | Error específico de esta clase | Diseña un experimento que induzca el evento y verifica si la retención mejora. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **evento de activación** y **ventana de activación** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **análisis predictivo de activación** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «analizar qué acciones distinguen a quienes permanecen» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **tasa de activación** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «La correlación entre el evento y la retención no prueba causalidad: puede que quienes ya estaban comprometidos hagan ambas cosas. Verificarlo requiere un experimento»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **análisis predictivo de activación** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **tasa de activación**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Hacking Growth* y *Trustworthy Online Controlled Experiments*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P19-C05-activation/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **tasa de activación**, **retención por activación** y **tiempo hasta la activación** con fuente, ventana y lectura prohibida.
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

Cada obra aparece con la idea concreta que aporta a esta clase. Si al leer no encuentras esa idea, la cita está mal puesta y corresponde reportarlo como error del material.

- Sean Ellis y Morgan Brown — *Hacking Growth* (2017) — **aporta a esta clase:** el momento «ajá» identificado con datos y no supuesto. **Dónde buscarlo:** los capítulos sobre el momento de valor. Registra edición y páginas consultadas en tu nota de lectura.
- Samuel Hulick — *The Elements of User Onboarding* (2014) — **aporta a esta clase:** el onboarding diseñado hacia el primer éxito y no hacia el recorrido del producto. **Dónde buscarlo:** los capítulos sobre objetivos del onboarding. Registra edición y páginas consultadas en tu nota de lectura.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — **aporta a esta clase:** el análisis de cohortes como corrección al promedio que esconde la mezcla. **Dónde buscarlo:** el capítulo sobre cohortes y segmentación. Registra edición y páginas consultadas en tu nota de lectura.
- Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) — **aporta a esta clase:** el efecto mínimo relevante como base del cálculo de muestra. **Dónde buscarlo:** los capítulos sobre potencia y tamaño de muestra. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 04 · Growth loops](class-04-growth-loops.md) · [Índice de la parte](README.md) · [Clase 06 · Crecimiento centrado en retención](class-06-retention-first-growth.md) →
