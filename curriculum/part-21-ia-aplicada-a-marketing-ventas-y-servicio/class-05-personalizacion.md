---
title: "Personalización"
type: class
language: es
standard: clase-profunda-v2
part: 21
class: 05
level: IA y expansión
mastery_threshold: 80
estimated_minutes: 150
sources: ["thaler", "oneil", "nist-airmf", "cialdini"]
anchors: {"cialdini": "reciprocidad", "nist-airmf": "contexto", "oneil": "proxy", "thaler": "arquitectura-decision"}
updated: 2026-08-19
---

# Clase 21.05 — Personalización

**Parte 21 · IA aplicada a marketing, ventas y servicio** · Nivel: IA y expansión · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 21.04 — *Generación de contenido con controles*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de efecto en conversión para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La arquitectura de la decisión: no existe presentación neutra de las opciones — Richard H. Thaler y Cass R. Sunstein. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La personalización mejora la pertinencia y puede cruzar rápidamente hacia lo invasivo. El límite no es técnico sino de expectativa: usar información que el cliente no sabe que la empresa posee produce desconfianza, aunque su obtención haya sido lícita. La regla práctica es personalizar con datos que el cliente entregó conscientemente y para la finalidad que conoce.

La clase trata el tema como un problema de evidencia y de consecuencia, no como vocabulario. La parte 21 busca **usar IA como capacidad operativa con evaluación, control y responsabilidad humana**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **personalización** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué tarea mejora con IA, cómo sé que mejora y quién responde cuando falla?

Los conceptos que estructuran la sesión son **pertinencia percibida**, **expectativa de privacidad**, **finalidad declarada** y **efecto inquietante**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `pertinencia percibida`, `expectativa de privacidad`, `finalidad declarada` y `efecto inquietante` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **IA aplicada a marketing, ventas y servicio**.
3. **Aplicar** la secuencia **identificar qué datos entregó el cliente conscientemente → verificar la finalidad declarada al recogerlos → diseñar la personalización dentro de esa expectativa → probar la reacción con un grupo pequeño → medir efecto en conversión y en bajas** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **efecto en conversión**, **tasa de baja tras personalización** y **consultas sobre uso de datos** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **pertinencia percibida** y **expectativa de privacidad** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **efecto en conversión**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **pertinencia percibida** | grado en que el cliente considera útil la adaptación del mensaje | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **expectativa de privacidad** | supuesto del cliente sobre qué información tiene la empresa y para qué | Da un hecho compatible con la definición y otro que la refute. |
| **finalidad declarada** | uso informado al momento de recoger el dato | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **efecto inquietante** | reacción negativa ante una personalización que revela información inesperada | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. identificar qué datos entregó el cliente conscientemente → 2. verificar la finalidad declarada al recogerlos → 3. diseñar la personalización dentro de esa expectativa → 4. probar la reacción con un grupo pequeño → 5. medir efecto en conversión y en bajas
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** La normativa de datos personales exige finalidad determinada e información al titular. La personalización basada en inferencias no declaradas es especialmente riesgosa.

## 📖 Desarrollo

### 1. Pertinencia percibida: mecanismo central

**Pertinencia percibida** se entiende aquí como **grado en que el cliente considera útil la adaptación del mensaje**.

La personalización mejora la pertinencia y cruza un umbral a partir del cual produce incomodidad. Ese umbral no depende de la tecnología sino de la expectativa: cuando el mensaje revela un conocimiento que la persona no recuerda haber entregado, la reacción es de invasión aunque el dato sea público.

**De dónde viene esta afirmación.** Richard H. Thaler y Cass R. Sunstein — *Nudge: The Final Edition* (2021) aporta la idea que sostiene este bloque: la arquitectura de la decisión: no existe presentación neutra de las opciones. Búscala en los capítulos sobre arquitectura de elección. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «efecto en conversión» debería moverse cuando cambie **pertinencia percibida**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **expectativa de privacidad**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Expectativa de privacidad: frontera conceptual y error de clasificación

**Definición operacional:** supuesto del cliente sobre qué información tiene la empresa y para qué. Su valor está en distinguirlo de **pertinencia percibida**.

La expectativa de privacidad es el criterio operativo. Antes de usar un dato para personalizar, la pregunta es si la persona esperaría que se usara así. Cuando la respuesta es dudosa, la salida profesional es no usarlo o declarar explícitamente su origen, que suele desactivar la incomodidad.

**Contraste bibliográfico.** Cathy O'Neil — *Weapons of Math Destruction* (2016) aporta aquí una distinción concreta: las variables sustitutas que codifican prejuicio sin nombrarlo (los capítulos sobre selección de variables). Formula dos mini-casos: uno que satisface la definición de **expectativa de privacidad** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «verificar la finalidad declarada al recogerlos», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Finalidad declarada: operacionalización y medición

**Finalidad declarada** significa **uso informado al momento de recoger el dato**.

La finalidad declarada limita el uso: los datos recogidos para una finalidad no pueden usarse para otra sin nueva base de licitud. Esa restricción es normativa y también práctica, porque el uso fuera de la finalidad es exactamente lo que produce el efecto inquietante que destruye la confianza.

Ficha de medición obligatoria para **efecto en conversión**: `diferencia de conversión entre versión personalizada y estándar`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** NIST — *AI Risk Management Framework 1.0* (2023) pone una condición sobre la medición: el riesgo evaluado en el contexto de uso y no en abstracto (la sección sobre mapeo del contexto). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Efecto inquietante: trade-offs y efectos de segundo orden

**Definición:** reacción negativa ante una personalización que revela información inesperada.

Personalizar más aumenta la relevancia y el costo de producción, la complejidad operativa y el riesgo. Personalizar menos es más simple y menos efectivo. La proporción razonable personaliza aquello que mejora claramente la experiencia y deja el resto estándar, en lugar de personalizar por capacidad técnica.

**Lo que aporta la fuente.** Robert B. Cialdini — *Influence: The Psychology of Persuasion, New and Expanded* (2021) aporta el criterio para pesar el intercambio: la reciprocidad: el aporte previo genera disposición a corresponder (el capítulo sobre reciprocidad). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **consultas sobre uso de datos** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **efecto inquietante** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «medir efecto en conversión y en bajas», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

La arquitectura de la decisión —cómo se presentan las opciones— nunca es neutra, y la personalización la vuelve individual. Esa combinación exige un control ético explícito: si el destinatario conociera el mecanismo, ¿lo consideraría legítimo? Cuando la respuesta es no, la técnica está operando contra la persona a la que dice servir.

**Frontera declarada.** La normativa de datos personales exige finalidad determinada e información al titular. La personalización basada en inferencias no declaradas es especialmente riesgosa. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar personalización no consiste en sumar definiciones. Empieza por **pertinencia percibida**, contrasta **expectativa de privacidad** con **finalidad declarada**, incorpora **efecto inquietante** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Richard H. Thaler y Cass R. Sunstein — *Nudge: The Final Edition* (2021) | La arquitectura de la decisión: no existe presentación neutra de las opciones | Los capítulos sobre arquitectura de elección | ¿Qué debería observarse en **pertinencia percibida** si aquí opera «la arquitectura de la decisión: no existe presentación neutra de las opciones»? ¿Y qué observación lo desmentiría en este caso? |
| Cathy O'Neil — *Weapons of Math Destruction* (2016) | Las variables sustitutas que codifican prejuicio sin nombrarlo | Los capítulos sobre selección de variables | ¿Qué debería observarse en **expectativa de privacidad** si aquí opera «las variables sustitutas que codifican prejuicio sin nombrarlo»? ¿Y qué observación lo desmentiría en este caso? |
| NIST — *AI Risk Management Framework 1.0* (2023) | El riesgo evaluado en el contexto de uso y no en abstracto | La sección sobre mapeo del contexto | ¿Qué debería observarse en **finalidad declarada** si aquí opera «el riesgo evaluado en el contexto de uso y no en abstracto»? ¿Y qué observación lo desmentiría en este caso? |
| Robert B. Cialdini — *Influence: The Psychology of Persuasion, New and Expanded* (2021) | La reciprocidad: el aporte previo genera disposición a corresponder | El capítulo sobre reciprocidad | ¿Qué debería observarse en **efecto inquietante** si aquí opera «la reciprocidad: el aporte previo genera disposición a corresponder»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina envió un correo mencionando la cantidad de citas canceladas de cada taller. Varios clientes preguntaron cómo obtuvieron ese dato y dos solicitaron eliminación.

**Paso 1 — Identificar qué datos entregó el cliente conscientemente.** El equipo escribe primero el supuesto asociado a **pertinencia percibida** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **efecto en conversión** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Verificar la finalidad declarada al recogerlos.** El trabajo aquí es separar lo observado de lo inferido sobre **expectativa de privacidad**. La evidencia que ordena la discusión es **tasa de baja tras personalización**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Diseñar la personalización dentro de esa expectativa.** El riesgo de este paso es cerrar demasiado rápido alrededor de **finalidad declarada**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **consultas sobre uso de datos** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Probar la reacción con un grupo pequeño.** Con **efecto inquietante** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **efecto en conversión** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Medir efecto en conversión y en bajas.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **pertinencia percibida**. **tasa de baja tras personalización** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **pertinencia percibida** | Grado en que el cliente considera útil la adaptación del mensaje | Cuando **efecto en conversión** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **expectativa de privacidad** | Supuesto del cliente sobre qué información tiene la empresa y para qué | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** La normativa de datos personales exige finalidad determinada e información al titular. La personalización basada en inferencias no declaradas es especialmente riesgosa.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre personalización |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager con IA, RevOps, Marketing manager y Sales enablement. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina envió un correo mencionando la cantidad de citas canceladas de cada taller. Varios clientes preguntaron cómo obtuvieron ese dato y dos solicitaron eliminación.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **identificar qué datos entregó el cliente conscientemente → verificar la finalidad declarada al recogerlos → diseñar la personalización dentro de esa expectativa → probar la reacción con un grupo pequeño → medir efecto en conversión y en bajas** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **efecto en conversión**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Nudge: The Final Edition* y la de *Weapons of Math Destruction*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **pertinencia percibida** y **expectativa de privacidad** como sinónimos | Se perdió la distinción entre «grado en que el cliente considera útil la adaptación del mensaje» y «supuesto del cliente sobre qué información tiene la empresa y para qué» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «medir efecto en conversión y en bajas» | Se saltó «identificar qué datos entregó el cliente conscientemente»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **efecto en conversión** | La métrica local reemplazó al resultado del sistema | Contrástala con **consultas sobre uso de datos** y explicita el costo de oportunidad. |
| Personalizar con datos fuera de la finalidad declarada | Error específico de esta clase | Limita la personalización a datos entregados conscientemente y para el uso informado. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **pertinencia percibida** y **expectativa de privacidad** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **finalidad declarada** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «identificar qué datos entregó el cliente conscientemente» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **efecto en conversión** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «La normativa de datos personales exige finalidad determinada e información al titular. La personalización basada en inferencias no declaradas es especialmente riesgosa»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **finalidad declarada** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **efecto en conversión**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Nudge: The Final Edition* y *Influence: The Psychology of Persuasion, New and Expanded*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P21-C05-personalizacion/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **efecto en conversión**, **tasa de baja tras personalización** y **consultas sobre uso de datos** con fuente, ventana y lectura prohibida.
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

- Richard H. Thaler y Cass R. Sunstein — *Nudge: The Final Edition* (2021) — **aporta a esta clase:** la arquitectura de la decisión: no existe presentación neutra de las opciones. **Dónde buscarlo:** los capítulos sobre arquitectura de elección. Registra edición y páginas consultadas en tu nota de lectura.
- Cathy O'Neil — *Weapons of Math Destruction* (2016) — **aporta a esta clase:** las variables sustitutas que codifican prejuicio sin nombrarlo. **Dónde buscarlo:** los capítulos sobre selección de variables. Registra edición y páginas consultadas en tu nota de lectura.
- NIST — *AI Risk Management Framework 1.0* (2023) — **aporta a esta clase:** el riesgo evaluado en el contexto de uso y no en abstracto. **Dónde buscarlo:** la sección sobre mapeo del contexto. Registra edición y páginas consultadas en tu nota de lectura.
- Robert B. Cialdini — *Influence: The Psychology of Persuasion, New and Expanded* (2021) — **aporta a esta clase:** la reciprocidad: el aporte previo genera disposición a corresponder. **Dónde buscarlo:** el capítulo sobre reciprocidad. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 04 · Generación de contenido con controles](class-04-generacion-de-contenido-con-controles.md) · [Índice de la parte](README.md) · [Clase 06 · Investigación de prospectos asistida](class-06-lead-research.md) →
