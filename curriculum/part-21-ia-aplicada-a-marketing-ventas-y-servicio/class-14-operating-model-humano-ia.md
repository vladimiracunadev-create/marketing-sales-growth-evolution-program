---
title: "Operating model humano-IA"
type: class
language: es
standard: clase-profunda-v2
part: 21
class: 14
level: IA y expansión
mastery_threshold: 80
estimated_minutes: 150
sources: ["nist-airmf", "iso-31000", "russell-norvig", "diorio"]
anchors: {"diorio": "sistema-ingresos", "iso-31000": "principios", "nist-airmf": "funciones", "russell-norvig": "medida-desempeno"}
updated: 2026-08-19
---

# Clase 21.14 — Operating model humano-IA

**Parte 21 · IA aplicada a marketing, ventas y servicio** · Nivel: IA y expansión · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 21.13 — *Privacidad y propiedad intelectual*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de casos de uso documentados para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** Las cuatro funciones: mapear, medir, gestionar y gobernar el riesgo de IA — NIST. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Esta clase integra la parte en un modelo operativo: qué tareas se asisten, qué se automatiza, qué queda humano, con qué evaluación, qué guardarraíles, qué registro y quién responde. La prueba de calidad es la rendición de cuentas: ante un error, la empresa debe poder explicar qué sistema actuó, con qué datos, bajo qué autorización y quién era responsable.

Esta sesión distingue lo que se sabe, lo que se supone y lo que todavía no se ha medido. La parte 21 busca **usar IA como capacidad operativa con evaluación, control y responsabilidad humana**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **operating model humano-IA** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué tarea mejora con IA, cómo sé que mejora y quién responde cuando falla?

Los conceptos que estructuran la sesión son **modelo operativo humano-IA**, **rendición de cuentas**, **registro de incidentes** y **revisión periódica**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `modelo operativo humano-IA`, `rendición de cuentas`, `registro de incidentes` y `revisión periódica` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **IA aplicada a marketing, ventas y servicio**.
3. **Aplicar** la secuencia **clasificar tareas en asistidas, automatizadas y humanas → documentar evaluación y guardarraíles por caso de uso → asignar responsable por cada sistema activo → instalar el registro de incidentes → revisar el modelo completo cada semestre** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **casos de uso documentados**, **incidentes registrados y corregidos** y **tiempo de rendición de cuentas** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **modelo operativo humano-IA** y **rendición de cuentas** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **casos de uso documentados**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **modelo operativo humano-IA** | distribución documentada de tareas entre personas y sistemas | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **rendición de cuentas** | capacidad de explicar qué ocurrió, con qué datos y bajo qué responsabilidad | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **registro de incidentes** | documentación de fallas, su causa y su corrección | Da un hecho compatible con la definición y otro que la refute. |
| **revisión periódica** | evaluación programada del modelo completo y sus resultados | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. clasificar tareas en asistidas, automatizadas y humanas → 2. documentar evaluación y guardarraíles por caso de uso → 3. asignar responsable por cada sistema activo → 4. instalar el registro de incidentes → 5. revisar el modelo completo cada semestre
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Un modelo operativo maduro exige capacidad dedicada. En equipos pequeños conviene menos casos de uso bien gobernados que muchos sin control.

## 📖 Desarrollo

### 1. Modelo operativo humano-IA: mecanismo central

**Modelo operativo humano-IA** se entiende aquí como **distribución documentada de tareas entre personas y sistemas**.

Un modelo operativo humano-máquina define qué hace cada uno, dónde está la frontera y cómo se escala cuando algo sale mal. Sin esa definición, la frontera se establece por costumbre y termina donde la herramienta permite llegar, que no es un criterio de gestión.

**De dónde viene esta afirmación.** NIST — *AI Risk Management Framework 1.0* (2023) aporta la idea que sostiene este bloque: las cuatro funciones: mapear, medir, gestionar y gobernar el riesgo de IA. Búscala en el núcleo del marco. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «casos de uso documentados» debería moverse cuando cambie **modelo operativo humano-IA**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **rendición de cuentas**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Rendición de cuentas: frontera conceptual y error de clasificación

**Definición operacional:** capacidad de explicar qué ocurrió, con qué datos y bajo qué responsabilidad. Su valor está en distinguirlo de **modelo operativo humano-IA**.

La rendición de cuentas debe ser nominal: por cada proceso asistido, una persona responde por el resultado. Esa asignación no puede diluirse en el área ni en el sistema. Cuando ocurre un incidente, la existencia de un responsable identificado es la diferencia entre corregir y buscar culpables.

**Contraste bibliográfico.** ISO — *ISO 31000: Gestión del riesgo* (2018) aporta aquí una distinción concreta: los principios: integrado, estructurado, adaptado y basado en la mejor información disponible (la cláusula sobre principios). Formula dos mini-casos: uno que satisface la definición de **rendición de cuentas** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «documentar evaluación y guardarraíles por caso de uso», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Registro de incidentes: operacionalización y medición

**Registro de incidentes** significa **documentación de fallas, su causa y su corrección**.

El registro de incidentes es la memoria del sistema: qué falló, con qué consecuencia, qué se hizo. Su valor aparece con el tiempo, cuando permite ver patrones y distinguir un error puntual de una falla estructural. Empezarlo desde el primer despliegue cuesta poco; reconstruirlo después es imposible.

Ficha de medición obligatoria para **casos de uso documentados**: `usos con evaluación, guardarraíl y responsable, sobre usos activos`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Stuart Russell y Peter Norvig — *Artificial Intelligence: A Modern Approach* (2021, 4.ª ed.) pone una condición sobre la medición: la medida de desempeño como definición previa a cualquier evaluación (el capítulo sobre racionalidad). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Revisión periódica: trade-offs y efectos de segundo orden

**Definición:** evaluación programada del modelo completo y sus resultados.

Un modelo con más control humano reduce el riesgo y el beneficio de productividad; uno con más autonomía multiplica ambos. La gradación debe corresponder a la consecuencia del error y a la reversibilidad, y debe revisarse a medida que se acumula evidencia sobre el desempeño real.

**Lo que aporta la fuente.** Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) aporta el criterio para pesar el intercambio: el ingreso como resultado de un sistema integrado y no de tres áreas separadas (los capítulos introductorios sobre revenue operations). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **tiempo de rendición de cuentas** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **revisión periódica** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar el modelo completo cada semestre», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La revisión periódica del modelo operativo es necesaria porque la tecnología, la normativa y las capacidades cambian con rapidez. Un modelo definido hace un año puede estar restringiendo usos ya seguros o permitiendo otros que dejaron de serlo. Fijar una frecuencia de revisión y un responsable es parte del diseño.

**Frontera declarada.** Un modelo operativo maduro exige capacidad dedicada. En equipos pequeños conviene menos casos de uso bien gobernados que muchos sin control. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar operating model humano-IA no consiste en sumar definiciones. Empieza por **modelo operativo humano-IA**, contrasta **rendición de cuentas** con **registro de incidentes**, incorpora **revisión periódica** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| NIST — *AI Risk Management Framework 1.0* (2023) | Las cuatro funciones: mapear, medir, gestionar y gobernar el riesgo de IA | El núcleo del marco | ¿Qué debería observarse en **modelo operativo humano-IA** si aquí opera «las cuatro funciones: mapear, medir, gestionar y gobernar el riesgo de IA»? ¿Y qué observación lo desmentiría en este caso? |
| ISO — *ISO 31000: Gestión del riesgo* (2018) | Los principios: integrado, estructurado, adaptado y basado en la mejor información disponible | La cláusula sobre principios | ¿Qué debería observarse en **rendición de cuentas** si aquí opera «los principios: integrado, estructurado, adaptado y basado en la mejor información disponible»? ¿Y qué observación lo desmentiría en este caso? |
| Stuart Russell y Peter Norvig — *Artificial Intelligence: A Modern Approach* (2021, 4.ª ed.) | La medida de desempeño como definición previa a cualquier evaluación | El capítulo sobre racionalidad | ¿Qué debería observarse en **registro de incidentes** si aquí opera «la medida de desempeño como definición previa a cualquier evaluación»? ¿Y qué observación lo desmentiría en este caso? |
| Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) | El ingreso como resultado de un sistema integrado y no de tres áreas separadas | Los capítulos introductorios sobre revenue operations | ¿Qué debería observarse en **revisión periódica** si aquí opera «el ingreso como resultado de un sistema integrado y no de tres áreas separadas»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Un cliente reclama por escrito una promesa que hizo el asistente automático de Ruta Andina. La empresa no puede determinar qué versión respondió ni quién la autorizó.

**Paso 1 — Clasificar tareas en asistidas, automatizadas y humanas.** El equipo escribe primero el supuesto asociado a **modelo operativo humano-IA** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **casos de uso documentados** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Documentar evaluación y guardarraíles por caso de uso.** El trabajo aquí es separar lo observado de lo inferido sobre **rendición de cuentas**. La evidencia que ordena la discusión es **incidentes registrados y corregidos**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Asignar responsable por cada sistema activo.** El riesgo de este paso es cerrar demasiado rápido alrededor de **registro de incidentes**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **tiempo de rendición de cuentas** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Instalar el registro de incidentes.** Con **revisión periódica** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **casos de uso documentados** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar el modelo completo cada semestre.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **modelo operativo humano-IA**. **incidentes registrados y corregidos** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **modelo operativo humano-IA** | Distribución documentada de tareas entre personas y sistemas | Cuando **casos de uso documentados** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **rendición de cuentas** | Capacidad de explicar qué ocurrió, con qué datos y bajo qué responsabilidad | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Un modelo operativo maduro exige capacidad dedicada. En equipos pequeños conviene menos casos de uso bien gobernados que muchos sin control.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre operating model humano-IA |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager con IA, RevOps, Marketing manager y Sales enablement. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Un cliente reclama por escrito una promesa que hizo el asistente automático de Ruta Andina. La empresa no puede determinar qué versión respondió ni quién la autorizó.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **clasificar tareas en asistidas, automatizadas y humanas → documentar evaluación y guardarraíles por caso de uso → asignar responsable por cada sistema activo → instalar el registro de incidentes → revisar el modelo completo cada semestre** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **casos de uso documentados**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *AI Risk Management Framework 1.0* y la de *ISO 31000: Gestión del riesgo*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **modelo operativo humano-IA** y **rendición de cuentas** como sinónimos | Se perdió la distinción entre «distribución documentada de tareas entre personas y sistemas» y «capacidad de explicar qué ocurrió, con qué datos y bajo qué responsabilidad» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar el modelo completo cada semestre» | Se saltó «clasificar tareas en asistidas, automatizadas y humanas»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **casos de uso documentados** | La métrica local reemplazó al resultado del sistema | Contrástala con **tiempo de rendición de cuentas** y explicita el costo de oportunidad. |
| No poder reconstruir qué hizo el sistema ante un incidente | Error específico de esta clase | Instala el registro de acciones y versiones, y designa responsable por cada sistema activo. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **modelo operativo humano-IA** y **rendición de cuentas** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **registro de incidentes** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «clasificar tareas en asistidas, automatizadas y humanas» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **casos de uso documentados** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Un modelo operativo maduro exige capacidad dedicada. En equipos pequeños conviene menos casos de uso bien gobernados que muchos sin control»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **registro de incidentes** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **casos de uso documentados**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *AI Risk Management Framework 1.0* y *Revenue Operations*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P21-C14-operating-model-humano-ia/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **casos de uso documentados**, **incidentes registrados y corregidos** y **tiempo de rendición de cuentas** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **operating model humano-IA con casos de uso, evaluaciones, guardrails y registro de incidentes**.

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

- NIST — *AI Risk Management Framework 1.0* (2023) — **aporta a esta clase:** las cuatro funciones: mapear, medir, gestionar y gobernar el riesgo de IA. **Dónde buscarlo:** el núcleo del marco. Registra edición y páginas consultadas en tu nota de lectura.
- ISO — *ISO 31000: Gestión del riesgo* (2018) — **aporta a esta clase:** los principios: integrado, estructurado, adaptado y basado en la mejor información disponible. **Dónde buscarlo:** la cláusula sobre principios. Registra edición y páginas consultadas en tu nota de lectura.
- Stuart Russell y Peter Norvig — *Artificial Intelligence: A Modern Approach* (2021, 4.ª ed.) — **aporta a esta clase:** la medida de desempeño como definición previa a cualquier evaluación. **Dónde buscarlo:** el capítulo sobre racionalidad. Registra edición y páginas consultadas en tu nota de lectura.
- Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) — **aporta a esta clase:** el ingreso como resultado de un sistema integrado y no de tres áreas separadas. **Dónde buscarlo:** los capítulos introductorios sobre revenue operations. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 13 · Privacidad y propiedad intelectual](class-13-privacidad-y-propiedad-intelectual.md) · [Índice de la parte](README.md)
