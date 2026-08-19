---
title: "Tracking y atribución"
type: class
language: es
standard: clase-profunda-v2
part: 14
class: 11
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["kaushik", "provost", "kohavi", "chaffey"]
anchors: {"chaffey": "gobierno-digital", "kaushik": "multiplicidad", "kohavi": "confianza", "provost": "asociacion-causalidad"}
updated: 2026-08-19
---

# Clase 14.11 — Tracking y atribución

Clase 11 de 14 de la parte [14 — Publicidad y performance marketing](README.md), de nivel Adquisición. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 14.10, *CPA, CAC y ROAS*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de consistencia de etiquetado con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La multiplicidad: combinar clics, resultados, experiencia y competencia — Avinash Kaushik. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Medir publicidad exige instrumentación: parámetros de campaña consistentes, eventos de conversión bien definidos y una convención de nomenclatura que permita analizar. Sin eso, cada informe requiere reconstruir manualmente qué significa cada fila. Las restricciones de privacidad reducen la cobertura del rastreo, lo que obliga a combinar medición de plataforma con datos propios del CRM.

El material se ordena alrededor de una pregunta que un comité comercial haría en voz alta. La parte 14 busca **invertir en medios pagados con control de costo, calidad y riesgo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **tracking y atribución** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué unidad de resultado estoy comprando y a qué costo marginal deja de tener sentido?

Los conceptos que estructuran la sesión son **convención de nomenclatura**, **evento de conversión**, **cobertura de medición** y **reconciliación con CRM**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `convención de nomenclatura`, `evento de conversión`, `cobertura de medición` y `reconciliación con CRM` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Publicidad y performance marketing**.
3. **Aplicar** la secuencia **definir la convención de nomenclatura y aplicarla → instrumentar eventos con definición documentada → estimar la cobertura real de la medición → reconciliar con el CRM cada mes → declarar el margen de error en los informes** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **consistencia de etiquetado**, **diferencia plataforma-CRM** y **cobertura de medición estimada** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **convención de nomenclatura** y **evento de conversión** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **consistencia de etiquetado**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **convención de nomenclatura** | regla uniforme para etiquetar campañas, fuentes y medios | Da un hecho compatible con la definición y otro que la refute. |
| **evento de conversión** | acción registrada que representa un resultado relevante | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **cobertura de medición** | proporción de las conversiones reales que el sistema logra registrar | Construye un caso límite donde el concepto se confunde con el anterior. |
| **reconciliación con CRM** | contraste entre lo reportado por plataformas y lo registrado internamente | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir la convención de nomenclatura y aplicarla → 2. instrumentar eventos con definición documentada → 3. estimar la cobertura real de la medición → 4. reconciliar con el CRM cada mes → 5. declarar el margen de error en los informes
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Ninguna instrumentación recupera la cobertura completa bajo las restricciones actuales de privacidad. La medición debe leerse como estimación con error conocido.

## 📖 Desarrollo

### 1. Convención de nomenclatura: mecanismo central

**Convención de nomenclatura** se entiende aquí como **regla uniforme para etiquetar campañas, fuentes y medios**.

El seguimiento y la atribución son la infraestructura que hace posible todo lo anterior, y su calidad se degrada silenciosamente. Un evento que dejó de dispararse tras un cambio en el sitio puede pasar semanas sin detectarse, y todas las decisiones tomadas en ese periodo se basan en datos incompletos.

**De dónde viene esta afirmación.** Avinash Kaushik — *Web Analytics 2.0* (2009) aporta la idea que sostiene este bloque: la multiplicidad: combinar clics, resultados, experiencia y competencia. Búscala en los capítulos sobre analítica multicanal. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «consistencia de etiquetado» debería moverse cuando cambie **convención de nomenclatura**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **evento de conversión**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Evento de conversión: frontera conceptual y error de clasificación

**Definición operacional:** acción registrada que representa un resultado relevante. Su valor está en distinguirlo de **convención de nomenclatura**.

La convención de nomenclatura parece un detalle administrativo y determina si los datos se pueden analizar. Sin una convención aplicada de forma consistente, agrupar el gasto por canal, campaña o audiencia exige limpieza manual cada vez. Definirla antes de lanzar la primera campaña ahorra meses de trabajo posterior.

**Contraste bibliográfico.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta aquí una distinción concreta: la distinción entre correlación observada y causalidad y qué exige cada una (los capítulos sobre inferencia y sesgo). Formula dos mini-casos: uno que satisface la definición de **evento de conversión** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «instrumentar eventos con definición documentada», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Cobertura de medición: operacionalización y medición

**Cobertura de medición** significa **proporción de las conversiones reales que el sistema logra registrar**.

La cobertura de medición debe verificarse periódicamente: qué proporción de las conversiones registradas en el sistema comercial tiene origen identificado. Cuando esa proporción es baja, cualquier análisis de canal describe una minoría del resultado. Declarar esa cobertura junto a los informes es una práctica de honestidad básica.

Ficha de medición obligatoria para **consistencia de etiquetado**: `sesiones con parámetros correctos, sobre sesiones de campañas`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) pone una condición sobre la medición: las condiciones que hacen confiable un experimento en línea (los capítulos sobre experimentos confiables). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Reconciliación con CRM: trade-offs y efectos de segundo orden

**Definición:** contraste entre lo reportado por plataformas y lo registrado internamente.

Medir más eventos entrega mejor visibilidad y aumenta la complejidad, el mantenimiento y las obligaciones sobre datos. Cada evento adicional necesita definición, verificación y documentación. Un plan de medición diseñado desde las decisiones suele requerir menos eventos de los que se implementan por defecto.

**Lo que aporta la fuente.** Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) aporta el criterio para pesar el intercambio: el gobierno de la operación digital: capacidades, procesos y medición (los capítulos sobre transformación y capacidades). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **cobertura de medición estimada** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **reconciliación con CRM** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «declarar el margen de error en los informes», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La reconciliación con el sistema comercial es la verificación final: las conversiones reportadas por las plataformas deben poder contrastarse con las oportunidades reales. Las diferencias son esperables; lo que no es aceptable es no conocerlas. Una revisión mensual de esa brecha es el control mínimo.

**Frontera declarada.** Ninguna instrumentación recupera la cobertura completa bajo las restricciones actuales de privacidad. La medición debe leerse como estimación con error conocido. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Atribuirse demanda existente, inflar el retorno y decidir presupuesto sobre una ilusión.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar tracking y atribución no consiste en sumar definiciones. Empieza por **convención de nomenclatura**, contrasta **evento de conversión** con **cobertura de medición**, incorpora **reconciliación con CRM** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Si el análisis no puede nombrar qué pieza sostiene la recomendación, todavía no hay comprensión transferible.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Avinash Kaushik — *Web Analytics 2.0* (2009) | La multiplicidad: combinar clics, resultados, experiencia y competencia | Los capítulos sobre analítica multicanal | ¿Qué debería observarse en **convención de nomenclatura** si aquí opera «la multiplicidad: combinar clics, resultados, experiencia y competencia»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La distinción entre correlación observada y causalidad y qué exige cada una | Los capítulos sobre inferencia y sesgo | ¿Qué debería observarse en **evento de conversión** si aquí opera «la distinción entre correlación observada y causalidad y qué exige cada una»? ¿Y qué observación lo desmentiría en este caso? |
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | Las condiciones que hacen confiable un experimento en línea | Los capítulos sobre experimentos confiables | ¿Qué debería observarse en **cobertura de medición** si aquí opera «las condiciones que hacen confiable un experimento en línea»? ¿Y qué observación lo desmentiría en este caso? |
| Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) | El gobierno de la operación digital: capacidades, procesos y medición | Los capítulos sobre transformación y capacidades | ¿Qué debería observarse en **reconciliación con CRM** si aquí opera «el gobierno de la operación digital: capacidades, procesos y medición»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Las plataformas reportan 96 conversiones mensuales a Ruta Andina y el CRM registra 41 oportunidades. Nadie ha reconciliado ambas cifras.

**Paso 1 — Definir la convención de nomenclatura y aplicarla.** El equipo escribe primero el supuesto asociado a **convención de nomenclatura** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **consistencia de etiquetado** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Instrumentar eventos con definición documentada.** El trabajo aquí es separar lo observado de lo inferido sobre **evento de conversión**. La evidencia que ordena la discusión es **diferencia plataforma-CRM**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Estimar la cobertura real de la medición.** El riesgo de este paso es cerrar demasiado rápido alrededor de **cobertura de medición**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **cobertura de medición estimada** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Reconciliar con el CRM cada mes.** Con **reconciliación con CRM** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **consistencia de etiquetado** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Declarar el margen de error en los informes.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **convención de nomenclatura**. **diferencia plataforma-CRM** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **convención de nomenclatura** | Regla uniforme para etiquetar campañas, fuentes y medios | Cuando **consistencia de etiquetado** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **evento de conversión** | Acción registrada que representa un resultado relevante | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Ninguna instrumentación recupera la cobertura completa bajo las restricciones actuales de privacidad. La medición debe leerse como estimación con error conocido.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre tracking y atribución |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Performance marketer, Media buyer y Growth marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Las plataformas reportan 96 conversiones mensuales a Ruta Andina y el CRM registra 41 oportunidades. Nadie ha reconciliado ambas cifras.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir la convención de nomenclatura y aplicarla → instrumentar eventos con definición documentada → estimar la cobertura real de la medición → reconciliar con el CRM cada mes → declarar el margen de error en los informes** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **consistencia de etiquetado**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Web Analytics 2.0* y la de *Data Science for Business*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **convención de nomenclatura** y **evento de conversión** como sinónimos | Se perdió la distinción entre «regla uniforme para etiquetar campañas, fuentes y medios» y «acción registrada que representa un resultado relevante» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «declarar el margen de error en los informes» | Se saltó «definir la convención de nomenclatura y aplicarla»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **consistencia de etiquetado** | La métrica local reemplazó al resultado del sistema | Contrástala con **cobertura de medición estimada** y explicita el costo de oportunidad. |
| Reportar cifras de plataforma sin reconciliar con el CRM | Error específico de esta clase | Concilia mensualmente y publica la diferencia junto con el informe. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **convención de nomenclatura** y **evento de conversión** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **cobertura de medición** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir la convención de nomenclatura y aplicarla» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **consistencia de etiquetado** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Ninguna instrumentación recupera la cobertura completa bajo las restricciones actuales de privacidad. La medición debe leerse como estimación con error conocido»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **cobertura de medición** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **consistencia de etiquetado**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Web Analytics 2.0* y *Digital Marketing*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Atribuirse demanda existente, inflar el retorno y decidir presupuesto sobre una ilusión.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P14-C11-tracking-y-atribucion/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **consistencia de etiquetado**, **diferencia plataforma-CRM** y **cobertura de medición estimada** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **plan de performance con estructura de campañas, presupuestos, medición y salvaguardas**.

## ✅ Evaluación de la clase

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Precisión conceptual | 25 % | Distinciones correctas y observables entre los conceptos de la clase. |
| Diagnóstico y evidencia | 30 % | Datos pertinentes, línea base, supuestos explícitos y límites del dato. |
| Decisión y trade-offs | 30 % | Dos opciones defendibles, costo de oportunidad y condición de revisión. |
| Fuentes y comunicación | 15 % | Dos lecturas realmente utilizadas y argumento ejecutivo trazable. |

**Aprobación:** 80/100 y ningún criterio bajo 60 %. Una respuesta que podría copiarse sin cambios a otra clase se considera insuficiente.

## 📗 Fuentes y verificación

Estas son las obras sobre las que se apoya lo que acabas de leer. Cada una aparece con la idea concreta que aporta a esta clase, dónde buscarla dentro del libro y el enlace donde se resuelve la edición exacta. Si al leer no encuentras esa idea, la cita está mal puesta y corresponde reportarlo como error del material.

- Avinash Kaushik — [*Web Analytics 2.0*](https://openlibrary.org/isbn/9780470596425) (2009) · ISBN 9780470596425 — **aporta a esta clase:** la multiplicidad: combinar clics, resultados, experiencia y competencia. **Dónde buscarlo:** los capítulos sobre analítica multicanal. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) · ISBN 9781449374280 — **aporta a esta clase:** la distinción entre correlación observada y causalidad y qué exige cada una. **Dónde buscarlo:** los capítulos sobre inferencia y sesgo. Registra edición y páginas consultadas en tu nota de lectura.
- Ron Kohavi, Diane Tang y Ya Xu — [*Trustworthy Online Controlled Experiments*](https://openlibrary.org/isbn/9781108601375) (2020) · ISBN 9781108601375 — **aporta a esta clase:** las condiciones que hacen confiable un experimento en línea. **Dónde buscarlo:** los capítulos sobre experimentos confiables. Registra edición y páginas consultadas en tu nota de lectura.
- Dave Chaffey y Fiona Ellis-Chadwick — [*Digital Marketing*](https://openlibrary.org/isbn/9781292400990) (2022, 8.ª ed.) · ISBN 9781292400990 — **aporta a esta clase:** el gobierno de la operación digital: capacidades, procesos y medición. **Dónde buscarlo:** los capítulos sobre transformación y capacidades. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 10 · CPA, CAC y ROAS](class-10-cpa-cac-y-roas.md) · [Índice de la parte](README.md) · [Clase 12 · Optimización de campañas](class-12-optimizacion-de-campanas.md) →
