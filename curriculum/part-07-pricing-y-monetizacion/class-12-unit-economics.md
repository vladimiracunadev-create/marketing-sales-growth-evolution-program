---
title: "Unit economics"
type: class
language: es
standard: clase-profunda-v2
part: 07
class: 12
level: Oferta comercial
mastery_threshold: 80
estimated_minutes: 150
sources: ["croll-yoskovitz", "fader-ltv", "provost", "hubbard"]
anchors: {"croll-yoskovitz": "modelos", "fader-ltv": "ltv-modelo", "hubbard": "calibracion", "provost": "valor-esperado"}
updated: 2026-08-19
---

# Clase 07.12 — Unit economics

**Parte 07 · Pricing y monetización** · Nivel: Oferta comercial · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 07.11 — *Descuentos sin destruir valor*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de relación valor de vida a costo de adquisición para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** Los seis modelos de negocio y las métricas que cambian entre ellos — Alistair Croll y Benjamin Yoskovitz. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La economía unitaria responde si cada cliente adicional deja o consume dinero. Sus componentes son el costo de adquisición completo, el margen de contribución por cliente, el periodo de recuperación y el valor de vida. El error más común no es de fórmula sino de alcance: excluir sueldos comerciales del costo de adquisición o usar margen bruto sin costo de soporte produce una economía que sólo existe en la planilla.

La clase trata el tema como un problema de evidencia y de consecuencia, no como vocabulario. La parte 07 busca **diseñar una arquitectura de precios que capture valor sin destruir demanda ni confianza**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **unit economics** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Cuánto vale esto para quién, y qué estructura de cobro alinea precio con valor entregado?

Los conceptos que estructuran la sesión son **costo de adquisición completo**, **margen de contribución por cliente**, **periodo de recuperación** y **valor de vida**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `costo de adquisición completo`, `margen de contribución por cliente`, `periodo de recuperación` y `valor de vida` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Pricing y monetización**.
3. **Aplicar** la secuencia **definir el alcance de cada componente por escrito → calcular por segmento y no sólo agregado → verificar los números contra contabilidad → analizar sensibilidad ante cambios de churn y margen → fijar el umbral que autoriza escalar la inversión** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **relación valor de vida a costo de adquisición**, **periodo de recuperación por segmento** y **margen de contribución por cohorte** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **costo de adquisición completo** y **margen de contribución por cliente** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **relación valor de vida a costo de adquisición**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **costo de adquisición completo** | gasto total de marketing y ventas, incluidos sueldos y herramientas, por cliente nuevo | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **margen de contribución por cliente** | ingreso menos costos variables de servir a ese cliente | Construye un caso límite donde el concepto se confunde con el anterior. |
| **periodo de recuperación** | meses hasta recuperar el costo de adquisición con el margen mensual | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **valor de vida** | margen acumulado esperado del cliente durante su permanencia estimada | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir el alcance de cada componente por escrito → 2. calcular por segmento y no sólo agregado → 3. verificar los números contra contabilidad → 4. analizar sensibilidad ante cambios de churn y margen → 5. fijar el umbral que autoriza escalar la inversión
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** El valor de vida es una proyección basada en supuestos de retención y margen. Sin cohortes maduras, su precisión es baja y debe presentarse como rango.

## 📖 Desarrollo

### 1. Costo de adquisición completo: mecanismo central

**Costo de adquisición completo** se entiende aquí como **gasto total de marketing y ventas, incluidos sueldos y herramientas, por cliente nuevo**.

La economía unitaria responde una pregunta simple y decisiva: ¿cada cliente adicional aporta o consume valor? Si el margen de contribución por cliente supera el costo de adquirirlo dentro de su permanencia esperada, crecer tiene sentido; si no, crecer acelera la pérdida. Muchos negocios descubren esa relación demasiado tarde porque miran ingreso total y no unidad.

**De dónde viene esta afirmación.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) aporta la idea que sostiene este bloque: los seis modelos de negocio y las métricas que cambian entre ellos. Búscala en la parte sobre modelos de negocio. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «relación valor de vida a costo de adquisición» debería moverse cuando cambie **costo de adquisición completo**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **margen de contribución por cliente**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Margen de contribución por cliente: frontera conceptual y error de clasificación

**Definición operacional:** ingreso menos costos variables de servir a ese cliente. Su valor está en distinguirlo de **costo de adquisición completo**.

El costo de adquisición completo incluye lo que casi siempre se omite: sueldos del equipo comercial y de marketing, herramientas, comisiones y el costo de las oportunidades perdidas en el proceso. Un cálculo que sólo considera el gasto en medios subestima el costo real por un factor considerable y produce decisiones de inversión equivocadas.

**Contraste bibliográfico.** Peter Fader y Sarah Toms — *The Customer Centricity Playbook* (2018) aporta aquí una distinción concreta: el valor de vida como proyección con supuestos declarados y no como cifra única (los capítulos sobre cálculo del valor de vida). Formula dos mini-casos: uno que satisface la definición de **margen de contribución por cliente** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «calcular por segmento y no sólo agregado», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Periodo de recuperación: operacionalización y medición

**Periodo de recuperación** significa **meses hasta recuperar el costo de adquisición con el margen mensual**.

El margen de contribución por cliente exige imputar el costo de servir, que varía mucho entre cuentas. La ficha debe registrar qué costos se imputaron, cómo se distribuyeron los compartidos y qué periodo cubre. Dos cálculos con supuestos distintos no son comparables, y la mayor parte de las discusiones sobre unit economics son en realidad discusiones sobre supuestos no declarados.

Ficha de medición obligatoria para **relación valor de vida a costo de adquisición**: `valor de vida dividido por costo de adquisición, por segmento y cohorte`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) pone una condición sobre la medición: el marco de valor esperado que combina probabilidad y consecuencia económica (el capítulo sobre valor esperado). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Valor de vida: trade-offs y efectos de segundo orden

**Definición:** margen acumulado esperado del cliente durante su permanencia estimada.

Mejorar la economía unitaria puede lograrse subiendo precio, bajando costo de servir o alargando la permanencia. Las tres palancas tienen efectos cruzados: subir precio puede acortar la permanencia; bajar costo de servir puede deteriorar el resultado del cliente. Modelar el efecto conjunto, aunque sea de forma gruesa, evita optimizar una variable destruyendo otra.

**Lo que aporta la fuente.** Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) aporta el criterio para pesar el intercambio: la calibración de estimaciones subjetivas como habilidad entrenable (los capítulos sobre estimación calibrada). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **margen de contribución por cohorte** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **valor de vida** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «fijar el umbral que autoriza escalar la inversión», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La economía unitaria es una proyección basada en permanencia esperada, y esa esperanza es el supuesto más frágil. En negocios jóvenes no hay historia suficiente para estimarla, y usar el supuesto optimista es la forma habitual de justificar inversión. La práctica honesta declara el supuesto, muestra la sensibilidad y define qué señal obligaría a revisarlo.

**Frontera declarada.** El valor de vida es una proyección basada en supuestos de retención y margen. Sin cohortes maduras, su precisión es baja y debe presentarse como rango. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar unit economics no consiste en sumar definiciones. Empieza por **costo de adquisición completo**, contrasta **margen de contribución por cliente** con **periodo de recuperación**, incorpora **valor de vida** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | Los seis modelos de negocio y las métricas que cambian entre ellos | La parte sobre modelos de negocio | ¿Qué debería observarse en **costo de adquisición completo** si aquí opera «los seis modelos de negocio y las métricas que cambian entre ellos»? ¿Y qué observación lo desmentiría en este caso? |
| Peter Fader y Sarah Toms — *The Customer Centricity Playbook* (2018) | El valor de vida como proyección con supuestos declarados y no como cifra única | Los capítulos sobre cálculo del valor de vida | ¿Qué debería observarse en **margen de contribución por cliente** si aquí opera «el valor de vida como proyección con supuestos declarados y no como cifra única»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | El marco de valor esperado que combina probabilidad y consecuencia económica | El capítulo sobre valor esperado | ¿Qué debería observarse en **periodo de recuperación** si aquí opera «el marco de valor esperado que combina probabilidad y consecuencia económica»? ¿Y qué observación lo desmentiría en este caso? |
| Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) | La calibración de estimaciones subjetivas como habilidad entrenable | Los capítulos sobre estimación calibrada | ¿Qué debería observarse en **valor de vida** si aquí opera «la calibración de estimaciones subjetivas como habilidad entrenable»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina reporta una relación de valor de vida a costo de adquisición de 4,2. Al incluir sueldos comerciales y horas de soporte, la relación real es 1,3.

**Paso 1 — Definir el alcance de cada componente por escrito.** El equipo escribe primero el supuesto asociado a **costo de adquisición completo** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **relación valor de vida a costo de adquisición** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Calcular por segmento y no sólo agregado.** El trabajo aquí es separar lo observado de lo inferido sobre **margen de contribución por cliente**. La evidencia que ordena la discusión es **periodo de recuperación por segmento**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Verificar los números contra contabilidad.** El riesgo de este paso es cerrar demasiado rápido alrededor de **periodo de recuperación**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **margen de contribución por cohorte** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Analizar sensibilidad ante cambios de churn y margen.** Con **valor de vida** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **relación valor de vida a costo de adquisición** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Fijar el umbral que autoriza escalar la inversión.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **costo de adquisición completo**. **periodo de recuperación por segmento** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **costo de adquisición completo** | Gasto total de marketing y ventas, incluidos sueldos y herramientas, por cliente nuevo | Cuando **relación valor de vida a costo de adquisición** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **margen de contribución por cliente** | Ingreso menos costos variables de servir a ese cliente | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** El valor de vida es una proyección basada en supuestos de retención y margen. Sin cohortes maduras, su precisión es baja y debe presentarse como rango.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre unit economics |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Pricing manager, Product marketing, CFO comercial y Founder. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina reporta una relación de valor de vida a costo de adquisición de 4,2. Al incluir sueldos comerciales y horas de soporte, la relación real es 1,3.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir el alcance de cada componente por escrito → calcular por segmento y no sólo agregado → verificar los números contra contabilidad → analizar sensibilidad ante cambios de churn y margen → fijar el umbral que autoriza escalar la inversión** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **relación valor de vida a costo de adquisición**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Lean Analytics* y la de *The Customer Centricity Playbook*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **costo de adquisición completo** y **margen de contribución por cliente** como sinónimos | Se perdió la distinción entre «gasto total de marketing y ventas, incluidos sueldos y herramientas, por cliente nuevo» y «ingreso menos costos variables de servir a ese cliente» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «fijar el umbral que autoriza escalar la inversión» | Se saltó «definir el alcance de cada componente por escrito»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **relación valor de vida a costo de adquisición** | La métrica local reemplazó al resultado del sistema | Contrástala con **margen de contribución por cohorte** y explicita el costo de oportunidad. |
| Excluir sueldos comerciales del costo de adquisición | Error específico de esta clase | Define el alcance por escrito y valida los componentes con contabilidad antes de decidir. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **costo de adquisición completo** y **margen de contribución por cliente** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **periodo de recuperación** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir el alcance de cada componente por escrito» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **relación valor de vida a costo de adquisición** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «El valor de vida es una proyección basada en supuestos de retención y margen. Sin cohortes maduras, su precisión es baja y debe presentarse como rango»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **periodo de recuperación** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **relación valor de vida a costo de adquisición**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Lean Analytics* y *How to Measure Anything*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P07-C12-unit-economics/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **relación valor de vida a costo de adquisición**, **periodo de recuperación por segmento** y **margen de contribución por cohorte** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **arquitectura de monetización con métrica de cobro, planes, price fences y política de descuentos**.

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

- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — **aporta a esta clase:** los seis modelos de negocio y las métricas que cambian entre ellos. **Dónde buscarlo:** la parte sobre modelos de negocio. Registra edición y páginas consultadas en tu nota de lectura.
- Peter Fader y Sarah Toms — *The Customer Centricity Playbook* (2018) — **aporta a esta clase:** el valor de vida como proyección con supuestos declarados y no como cifra única. **Dónde buscarlo:** los capítulos sobre cálculo del valor de vida. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — **aporta a esta clase:** el marco de valor esperado que combina probabilidad y consecuencia económica. **Dónde buscarlo:** el capítulo sobre valor esperado. Registra edición y páginas consultadas en tu nota de lectura.
- Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) — **aporta a esta clase:** la calibración de estimaciones subjetivas como habilidad entrenable. **Dónde buscarlo:** los capítulos sobre estimación calibrada. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 11 · Descuentos sin destruir valor](class-11-descuentos-sin-destruir-valor.md) · [Índice de la parte](README.md) · [Clase 13 · Experimentación de precios](class-13-experimentacion-de-precios.md) →
