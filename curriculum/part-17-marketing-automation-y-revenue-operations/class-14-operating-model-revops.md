---
title: "Operating model de RevOps"
type: class
language: es
standard: clase-profunda-v2
part: 17
class: 14
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["diorio", "roberge", "kaplan-norton", "grove"]
anchors: {"diorio": "sistema-ingresos", "grove": "output-gerencial", "kaplan-norton": "cuatro-perspectivas", "roberge": "formacion"}
updated: 2026-08-19
---

# Clase 17.14 — Operating model de RevOps

**Parte 17 · Marketing automation y revenue operations** · Nivel: Operación de ingresos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 17.13 — *Gobernanza de automatizaciones*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de indicadores con definición única para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El ingreso como resultado de un sistema integrado y no de tres áreas separadas — Stephen G. Diorio y Chris K. Hummel. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Esta clase integra la parte en un modelo operativo de ingresos: definiciones compartidas, modelo de datos, ciclo de vida, automatizaciones gobernadas, acuerdos entre áreas, forecast unificado y observabilidad. La prueba de calidad es que una pregunta de negocio pueda responderse con una sola cifra, con su definición y su fuente.

Esta sesión distingue lo que se sabe, lo que se supone y lo que todavía no se ha medido. La parte 17 busca **integrar marketing, ventas y servicio en un solo modelo de datos y de proceso**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **operating model de RevOps** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué automatizo porque mejora el sistema y qué estaría solo escalando un desorden?

Los conceptos que estructuran la sesión son **modelo operativo de ingresos**, **cifra única**, **responsabilidad por proceso** y **ritmo de gestión**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `modelo operativo de ingresos`, `cifra única`, `responsabilidad por proceso` y `ritmo de gestión` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Marketing automation y revenue operations**.
3. **Aplicar** la secuencia **consolidar definiciones, datos y acuerdos → documentar el modelo con responsables por proceso → establecer el ritmo de revisiones → verificar que cada indicador tenga cifra única → revisar el modelo completo cada semestre** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **indicadores con definición única**, **procesos con responsable** y **discrepancia entre informes** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **modelo operativo de ingresos** y **cifra única** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **indicadores con definición única**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **modelo operativo de ingresos** | conjunto de procesos, datos, acuerdos y responsabilidades que produce ingreso | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **cifra única** | valor acordado para cada indicador con su definición y fuente | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **responsabilidad por proceso** | asignación explícita de quién responde por cada tramo del sistema | Da un hecho compatible con la definición y otro que la refute. |
| **ritmo de gestión** | calendario de revisiones que sostiene la operación | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. consolidar definiciones, datos y acuerdos → 2. documentar el modelo con responsables por proceso → 3. establecer el ritmo de revisiones → 4. verificar que cada indicador tenga cifra única → 5. revisar el modelo completo cada semestre
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un modelo operativo maduro exige capacidad dedicada. En equipos pequeños, la alternativa realista es un subconjunto bien mantenido en lugar de un modelo completo mal sostenido.

## 📖 Desarrollo

### 1. Modelo operativo de ingresos: mecanismo central

**Modelo operativo de ingresos** se entiende aquí como **conjunto de procesos, datos, acuerdos y responsabilidades que produce ingreso**.

Un modelo operativo de ingresos describe cómo trabajan juntas las áreas que producen ingreso: qué procesos existen, quién responde por cada uno, con qué información y con qué ritmo. Es el documento que permite que la coordinación no dependa de las relaciones personales entre jefaturas.

**De dónde viene esta afirmación.** Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) aporta la idea que sostiene este bloque: el ingreso como resultado de un sistema integrado y no de tres áreas separadas. Búscala en los capítulos introductorios sobre revenue operations. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «indicadores con definición única» debería moverse cuando cambie **modelo operativo de ingresos**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **cifra única**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Cifra única: frontera conceptual y error de clasificación

**Definición operacional:** valor acordado para cada indicador con su definición y fuente. Su valor está en distinguirlo de **modelo operativo de ingresos**.

La cifra única es el acuerdo de que existe una fuente autoritativa para cada indicador relevante y que todas las áreas la usan. Parece obvio y es raro: en la mayoría de las organizaciones, marketing, ventas y finanzas reportan cifras distintas del mismo concepto, y las reuniones empiezan reconciliando.

**Contraste bibliográfico.** Mark Roberge — *The Sales Acceleration Formula* (2015) aporta aquí una distinción concreta: la formación estandarizada con certificación por componente (los capítulos sobre la fórmula de entrenamiento). Formula dos mini-casos: uno que satisface la definición de **cifra única** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «documentar el modelo con responsables por proceso», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Responsabilidad por proceso: operacionalización y medición

**Responsabilidad por proceso** significa **asignación explícita de quién responde por cada tramo del sistema**.

La responsabilidad por proceso debe estar asignada de extremo a extremo y no por tramo. Cuando cada área responde por su parte, los traspasos quedan sin dueño y ahí es donde se pierde la mayor parte del valor. Nombrar un responsable del proceso completo, aunque no dirija a todos los equipos, cambia la dinámica.

Ficha de medición obligatoria para **indicadores con definición única**: `indicadores con definición y fuente acordadas, sobre indicadores usados`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) pone una condición sobre la medición: las cuatro perspectivas: financiera, cliente, procesos y aprendizaje (los capítulos que presentan el cuadro de mando). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Ritmo de gestión: trade-offs y efectos de segundo orden

**Definición:** calendario de revisiones que sostiene la operación.

Un modelo operativo detallado alinea y puede volverse burocrático si no se ajusta al tamaño de la organización. En equipos pequeños, la formalización excesiva consume más de lo que aporta. El criterio es formalizar lo que ya produce fricción y dejar lo demás en acuerdos simples.

**Lo que aporta la fuente.** Andrew S. Grove — *High Output Management* (1983) aporta el criterio para pesar el intercambio: el output del gerente es el de su organización más el de las unidades que influye (los capítulos sobre el trabajo del gerente). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **discrepancia entre informes** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **ritmo de gestión** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar el modelo completo cada semestre», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El ritmo de gestión —qué se revisa semanalmente, mensualmente, trimestralmente— es parte del modelo y no un detalle de calendario. Un sistema sin ritmo definido revisa cuando hay problemas, que es siempre tarde. Definir el ritmo y sostenerlo es una de las pocas prácticas cuya ausencia se nota inmediatamente en los resultados.

**Frontera declarada.** Un modelo operativo maduro exige capacidad dedicada. En equipos pequeños, la alternativa realista es un subconjunto bien mantenido en lugar de un modelo completo mal sostenido. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar operating model de RevOps no consiste en sumar definiciones. Empieza por **modelo operativo de ingresos**, contrasta **cifra única** con **responsabilidad por proceso**, incorpora **ritmo de gestión** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) | El ingreso como resultado de un sistema integrado y no de tres áreas separadas | Los capítulos introductorios sobre revenue operations | ¿Qué debería observarse en **modelo operativo de ingresos** si aquí opera «el ingreso como resultado de un sistema integrado y no de tres áreas separadas»? ¿Y qué observación lo desmentiría en este caso? |
| Mark Roberge — *The Sales Acceleration Formula* (2015) | La formación estandarizada con certificación por componente | Los capítulos sobre la fórmula de entrenamiento | ¿Qué debería observarse en **cifra única** si aquí opera «la formación estandarizada con certificación por componente»? ¿Y qué observación lo desmentiría en este caso? |
| Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) | Las cuatro perspectivas: financiera, cliente, procesos y aprendizaje | Los capítulos que presentan el cuadro de mando | ¿Qué debería observarse en **responsabilidad por proceso** si aquí opera «las cuatro perspectivas: financiera, cliente, procesos y aprendizaje»? ¿Y qué observación lo desmentiría en este caso? |
| Andrew S. Grove — *High Output Management* (1983) | El output del gerente es el de su organización más el de las unidades que influye | Los capítulos sobre el trabajo del gerente | ¿Qué debería observarse en **ritmo de gestión** si aquí opera «el output del gerente es el de su organización más el de las unidades que influye»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El directorio de Ruta Andina pregunta cuál es el ingreso recurrente. Tres áreas entregan tres cifras distintas y ninguna puede explicar la diferencia.

**Paso 1 — Consolidar definiciones, datos y acuerdos.** El equipo escribe primero el supuesto asociado a **modelo operativo de ingresos** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **indicadores con definición única** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Documentar el modelo con responsables por proceso.** El trabajo aquí es separar lo observado de lo inferido sobre **cifra única**. La evidencia que ordena la discusión es **procesos con responsable**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Establecer el ritmo de revisiones.** El riesgo de este paso es cerrar demasiado rápido alrededor de **responsabilidad por proceso**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **discrepancia entre informes** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Verificar que cada indicador tenga cifra única.** Con **ritmo de gestión** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **indicadores con definición única** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar el modelo completo cada semestre.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **modelo operativo de ingresos**. **procesos con responsable** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **modelo operativo de ingresos** | Conjunto de procesos, datos, acuerdos y responsabilidades que produce ingreso | Cuando **indicadores con definición única** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **cifra única** | Valor acordado para cada indicador con su definición y fuente | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un modelo operativo maduro exige capacidad dedicada. En equipos pequeños, la alternativa realista es un subconjunto bien mantenido en lugar de un modelo completo mal sostenido.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre operating model de RevOps |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Marketing ops, RevOps manager y Sales ops. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El directorio de Ruta Andina pregunta cuál es el ingreso recurrente. Tres áreas entregan tres cifras distintas y ninguna puede explicar la diferencia.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **consolidar definiciones, datos y acuerdos → documentar el modelo con responsables por proceso → establecer el ritmo de revisiones → verificar que cada indicador tenga cifra única → revisar el modelo completo cada semestre** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **indicadores con definición única**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Revenue Operations* y la de *The Sales Acceleration Formula*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **modelo operativo de ingresos** y **cifra única** como sinónimos | Se perdió la distinción entre «conjunto de procesos, datos, acuerdos y responsabilidades que produce ingreso» y «valor acordado para cada indicador con su definición y fuente» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar el modelo completo cada semestre» | Se saltó «consolidar definiciones, datos y acuerdos»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **indicadores con definición única** | La métrica local reemplazó al resultado del sistema | Contrástala con **discrepancia entre informes** y explicita el costo de oportunidad. |
| Tolerar cifras distintas para el mismo indicador | Error específico de esta clase | Declara la definición y la fuente única de cada indicador crítico y publícalas. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **modelo operativo de ingresos** y **cifra única** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **responsabilidad por proceso** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «consolidar definiciones, datos y acuerdos» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **indicadores con definición única** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un modelo operativo maduro exige capacidad dedicada. En equipos pequeños, la alternativa realista es un subconjunto bien mantenido en lugar de un modelo completo mal sostenido»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **responsabilidad por proceso** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **indicadores con definición única**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Revenue Operations* y *High Output Management*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P17-C14-operating-model-revops/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **indicadores con definición única**, **procesos con responsable** y **discrepancia entre informes** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **operating model de RevOps con lifecycle, scoring, SLA, integraciones y observabilidad**.

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

- Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) — **aporta a esta clase:** el ingreso como resultado de un sistema integrado y no de tres áreas separadas. **Dónde buscarlo:** los capítulos introductorios sobre revenue operations. Registra edición y páginas consultadas en tu nota de lectura.
- Mark Roberge — *The Sales Acceleration Formula* (2015) — **aporta a esta clase:** la formación estandarizada con certificación por componente. **Dónde buscarlo:** los capítulos sobre la fórmula de entrenamiento. Registra edición y páginas consultadas en tu nota de lectura.
- Robert S. Kaplan y David P. Norton — *The Balanced Scorecard* (1996) — **aporta a esta clase:** las cuatro perspectivas: financiera, cliente, procesos y aprendizaje. **Dónde buscarlo:** los capítulos que presentan el cuadro de mando. Registra edición y páginas consultadas en tu nota de lectura.
- Andrew S. Grove — *High Output Management* (1983) — **aporta a esta clase:** el output del gerente es el de su organización más el de las unidades que influye. **Dónde buscarlo:** los capítulos sobre el trabajo del gerente. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 13 · Gobernanza de automatizaciones](class-13-gobernanza-de-automatizaciones.md) · [Índice de la parte](README.md)
