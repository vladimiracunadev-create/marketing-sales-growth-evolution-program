---
title: "Arquitectura de monetización"
type: class
language: es
standard: clase-profunda-v2
part: 07
class: 14
level: Oferta comercial
mastery_threshold: 80
estimated_minutes: 150
sources: ["nagle", "ramanujam", "simon", "croll-yoskovitz"]
anchors: {"croll-yoskovitz": "modelos", "nagle": "politica", "ramanujam": "modelo-monetizacion", "simon": "palanca-precio"}
updated: 2026-08-19
---

# Clase 07.14 — Arquitectura de monetización

**Parte 07 · Pricing y monetización** · Nivel: Oferta comercial · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 07.13 — *Experimentación de precios*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de margen por plan para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La política de precios como sistema de reglas que evita negociar cada caso — Thomas T. Nagle y Georg Müller. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Esta clase integra la parte en una arquitectura completa: métrica de cobro, estructura de planes, price fences, política de descuentos, modelo de recurrencia y economía unitaria verificada. La prueba de calidad es doble: el equipo comercial puede cotizar sin consultar y el área financiera puede proyectar ingreso con supuestos explícitos.

Esta sesión distingue lo que se sabe, lo que se supone y lo que todavía no se ha medido. La parte 07 busca **diseñar una arquitectura de precios que capture valor sin destruir demanda ni confianza**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **arquitectura de monetización** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Cuánto vale esto para quién, y qué estructura de cobro alinea precio con valor entregado?

Los conceptos que estructuran la sesión son **arquitectura de monetización**, **coherencia precio-valor**, **gobierno de precios** y **proyección de ingreso**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `arquitectura de monetización`, `coherencia precio-valor`, `gobierno de precios` y `proyección de ingreso` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Pricing y monetización**.
3. **Aplicar** la secuencia **consolidar métrica de cobro, planes y barreras → verificar economía unitaria por plan → documentar política de descuentos y autoridad → proyectar ingreso con escenarios → definir la revisión periódica de precios** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **margen por plan**, **desviación de cotizaciones** y **precisión de la proyección** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **arquitectura de monetización** y **coherencia precio-valor** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **margen por plan**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **arquitectura de monetización** | sistema completo de decisiones de precio, estructura y política | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **coherencia precio-valor** | correspondencia entre lo que se cobra y el valor que percibe cada segmento | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **gobierno de precios** | reglas de autoridad, revisión y excepción documentadas | Da un hecho compatible con la definición y otro que la refute. |
| **proyección de ingreso** | estimación de ingreso futuro basada en la arquitectura y sus supuestos | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. consolidar métrica de cobro, planes y barreras → 2. verificar economía unitaria por plan → 3. documentar política de descuentos y autoridad → 4. proyectar ingreso con escenarios → 5. definir la revisión periódica de precios
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Una arquitectura de precios envejece con el producto y con el mercado. Sin una revisión anual programada, la estructura queda desalineada del valor entregado.

## 📖 Desarrollo

### 1. Arquitectura de monetización: mecanismo central

**Arquitectura de monetización** se entiende aquí como **sistema completo de decisiones de precio, estructura y política**.

Una arquitectura de monetización integra las decisiones que las clases anteriores tomaron por separado: qué se cobra, con qué unidad, en qué niveles, con qué barreras y con qué política de excepción. Su valor está en la coherencia: cada pieza debe ser explicable en relación con el valor que el cliente recibe, y las que no lo son suelen ser herencias que nadie revisó.

**De dónde viene esta afirmación.** Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) aporta la idea que sostiene este bloque: la política de precios como sistema de reglas que evita negociar cada caso. Búscala en el capítulo sobre política y disciplina de precios. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «margen por plan» debería moverse cuando cambie **arquitectura de monetización**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **coherencia precio-valor**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Coherencia precio-valor: frontera conceptual y error de clasificación

**Definición operacional:** correspondencia entre lo que se cobra y el valor que percibe cada segmento. Su valor está en distinguirlo de **arquitectura de monetización**.

La coherencia precio-valor se audita con una revisión concreta: para cada nivel de la estructura, verificar que el salto de precio corresponde a un salto de valor perceptible. Cuando un plan cuesta el doble y aporta una funcionalidad marginal, el cliente lo detecta y la estructura pierde credibilidad completa, no sólo en ese nivel.

**Contraste bibliográfico.** Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) aporta aquí una distinción concreta: los modelos de monetización disponibles y el criterio para elegir la métrica de cobro (el capítulo sobre modelos de monetización). Formula dos mini-casos: uno que satisface la definición de **coherencia precio-valor** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «verificar economía unitaria por plan», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Gobierno de precios: operacionalización y medición

**Gobierno de precios** significa **reglas de autoridad, revisión y excepción documentadas**.

El gobierno de precios define quién puede cambiar qué, con qué proceso y con qué registro. Sin gobierno, la estructura diseñada se degrada por acumulación de excepciones hasta que nadie sabe cuál es el precio real. Una revisión anual del precio realizado por segmento, comparado con la lista, es el control mínimo.

Ficha de medición obligatoria para **margen por plan**: `margen de contribución por plan, sobre ingreso del plan`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Hermann Simon — *Confessions of the Pricing Man* (2015) pone una condición sobre la medición: el precio como la palanca de utilidad más rápida frente a volumen y costo (los capítulos sobre el poder del precio). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Proyección de ingreso: trade-offs y efectos de segundo orden

**Definición:** estimación de ingreso futuro basada en la arquitectura y sus supuestos.

Una arquitectura simple se comunica y se administra bien y captura menos valor; una compleja captura mejor y aumenta el costo de venta, de facturación y de soporte. El límite práctico es la capacidad del equipo comercial de explicarla sin material de apoyo: si no puede, la complejidad se pagará en errores y en descuentos para compensar la confusión.

**Lo que aporta la fuente.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) aporta el criterio para pesar el intercambio: los seis modelos de negocio y las métricas que cambian entre ellos (la parte sobre modelos de negocio). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **precisión de la proyección** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **proyección de ingreso** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «definir la revisión periódica de precios», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La proyección de ingreso que se construye sobre la arquitectura hereda todos sus supuestos: mezcla de planes, tasa de conversión entre niveles, permanencia. Presentarla como pronóstico sin declarar esos supuestos convierte un ejercicio de diseño en una promesa financiera. La versión honesta acompaña la proyección con su sensibilidad a los dos supuestos más frágiles.

**Frontera declarada.** Una arquitectura de precios envejece con el producto y con el mercado. Sin una revisión anual programada, la estructura queda desalineada del valor entregado. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar arquitectura de monetización no consiste en sumar definiciones. Empieza por **arquitectura de monetización**, contrasta **coherencia precio-valor** con **gobierno de precios**, incorpora **proyección de ingreso** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) | La política de precios como sistema de reglas que evita negociar cada caso | El capítulo sobre política y disciplina de precios | ¿Qué debería observarse en **arquitectura de monetización** si aquí opera «la política de precios como sistema de reglas que evita negociar cada caso»? ¿Y qué observación lo desmentiría en este caso? |
| Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) | Los modelos de monetización disponibles y el criterio para elegir la métrica de cobro | El capítulo sobre modelos de monetización | ¿Qué debería observarse en **coherencia precio-valor** si aquí opera «los modelos de monetización disponibles y el criterio para elegir la métrica de cobro»? ¿Y qué observación lo desmentiría en este caso? |
| Hermann Simon — *Confessions of the Pricing Man* (2015) | El precio como la palanca de utilidad más rápida frente a volumen y costo | Los capítulos sobre el poder del precio | ¿Qué debería observarse en **gobierno de precios** si aquí opera «el precio como la palanca de utilidad más rápida frente a volumen y costo»? ¿Y qué observación lo desmentiría en este caso? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | Los seis modelos de negocio y las métricas que cambian entre ellos | La parte sobre modelos de negocio | ¿Qué debería observarse en **proyección de ingreso** si aquí opera «los seis modelos de negocio y las métricas que cambian entre ellos»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina debe presentar su arquitectura de monetización al directorio junto al presupuesto. Hoy hay cinco planes, precios negociados caso a caso y ninguna política escrita.

**Paso 1 — Consolidar métrica de cobro, planes y barreras.** El equipo escribe primero el supuesto asociado a **arquitectura de monetización** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **margen por plan** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Verificar economía unitaria por plan.** El trabajo aquí es separar lo observado de lo inferido sobre **coherencia precio-valor**. La evidencia que ordena la discusión es **desviación de cotizaciones**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Documentar política de descuentos y autoridad.** El riesgo de este paso es cerrar demasiado rápido alrededor de **gobierno de precios**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **precisión de la proyección** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Proyectar ingreso con escenarios.** Con **proyección de ingreso** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **margen por plan** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Definir la revisión periódica de precios.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **arquitectura de monetización**. **desviación de cotizaciones** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **arquitectura de monetización** | Sistema completo de decisiones de precio, estructura y política | Cuando **margen por plan** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **coherencia precio-valor** | Correspondencia entre lo que se cobra y el valor que percibe cada segmento | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Una arquitectura de precios envejece con el producto y con el mercado. Sin una revisión anual programada, la estructura queda desalineada del valor entregado.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre arquitectura de monetización |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Pricing manager, Product marketing, CFO comercial y Founder. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina debe presentar su arquitectura de monetización al directorio junto al presupuesto. Hoy hay cinco planes, precios negociados caso a caso y ninguna política escrita.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **consolidar métrica de cobro, planes y barreras → verificar economía unitaria por plan → documentar política de descuentos y autoridad → proyectar ingreso con escenarios → definir la revisión periódica de precios** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **margen por plan**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *The Strategy and Tactics of Pricing* y la de *Monetizing Innovation*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **arquitectura de monetización** y **coherencia precio-valor** como sinónimos | Se perdió la distinción entre «sistema completo de decisiones de precio, estructura y política» y «correspondencia entre lo que se cobra y el valor que percibe cada segmento» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «definir la revisión periódica de precios» | Se saltó «consolidar métrica de cobro, planes y barreras»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **margen por plan** | La métrica local reemplazó al resultado del sistema | Contrástala con **precisión de la proyección** y explicita el costo de oportunidad. |
| Operar sin política de precios escrita | Error específico de esta clase | Publica la política con niveles de autoridad y audita mensualmente las excepciones. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **arquitectura de monetización** y **coherencia precio-valor** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **gobierno de precios** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «consolidar métrica de cobro, planes y barreras» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **margen por plan** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Una arquitectura de precios envejece con el producto y con el mercado. Sin una revisión anual programada, la estructura queda desalineada del valor entregado»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **gobierno de precios** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **margen por plan**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *The Strategy and Tactics of Pricing* y *Lean Analytics*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P07-C14-arquitectura-de-monetizacion/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **margen por plan**, **desviación de cotizaciones** y **precisión de la proyección** con fuente, ventana y lectura prohibida.
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

- Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) — **aporta a esta clase:** la política de precios como sistema de reglas que evita negociar cada caso. **Dónde buscarlo:** el capítulo sobre política y disciplina de precios. Registra edición y páginas consultadas en tu nota de lectura.
- Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) — **aporta a esta clase:** los modelos de monetización disponibles y el criterio para elegir la métrica de cobro. **Dónde buscarlo:** el capítulo sobre modelos de monetización. Registra edición y páginas consultadas en tu nota de lectura.
- Hermann Simon — *Confessions of the Pricing Man* (2015) — **aporta a esta clase:** el precio como la palanca de utilidad más rápida frente a volumen y costo. **Dónde buscarlo:** los capítulos sobre el poder del precio. Registra edición y páginas consultadas en tu nota de lectura.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — **aporta a esta clase:** los seis modelos de negocio y las métricas que cambian entre ellos. **Dónde buscarlo:** la parte sobre modelos de negocio. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 13 · Experimentación de precios](class-13-experimentacion-de-precios.md) · [Índice de la parte](README.md)
