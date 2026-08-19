---
title: "Investigación cuantitativa"
type: class
language: es
standard: clase-profunda-v2
part: 03
class: 07
level: Fundamentos
mastery_threshold: 80
estimated_minutes: 150
sources: ["provost", "kohavi", "malhotra", "wheeler-dv"]
anchors: {"kohavi": "efecto-minimo", "malhotra": "escalas", "provost": "asociacion-causalidad", "wheeler-dv": "variacion-comun"}
updated: 2026-08-19
---

# Clase 03.07 — Investigación cuantitativa

Clase 7 de 14 de la parte [03 — Investigación de mercados e inteligencia competitiva](README.md), de nivel Fundamentos. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 03.06, *Investigación cualitativa*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de potencia del estudio con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La distinción entre correlación observada y causalidad y qué exige cada una — Foster Provost y Tom Fawcett. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La investigación cuantitativa responde preguntas de magnitud y de relación: cuántos, con qué frecuencia, qué tan asociado. Su valor depende de tres cosas que suelen omitirse en informes comerciales: definición operacional de la variable, tamaño de muestra suficiente y declaración de incertidumbre. Un número sin intervalo ni denominador es retórica con apariencia de dato.

Esta sesión distingue lo que se sabe, lo que se supone y lo que todavía no se ha medido. La parte 03 busca **producir investigación que cambie una decisión y resista una auditoría metodológica**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **investigación cuantitativa** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué evidencia mínima necesito para decidir, y qué sesgo podría estar produciéndola?

Los conceptos que estructuran la sesión son **variable operacionalizada**, **tamaño de muestra suficiente**, **incertidumbre declarada** y **asociación frente a causalidad**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `variable operacionalizada`, `tamaño de muestra suficiente`, `incertidumbre declarada` y `asociación frente a causalidad` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Investigación de mercados e inteligencia competitiva**.
3. **Aplicar** la secuencia **definir las variables y su forma de medición → calcular el tamaño de muestra según el efecto mínimo relevante → recolectar con procedimiento uniforme → reportar estimación e incertidumbre → distinguir explícitamente asociación de causalidad** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **potencia del estudio**, **proporción de resultados con intervalo reportado** y **consistencia entre olas** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **variable operacionalizada** y **tamaño de muestra suficiente** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **potencia del estudio**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **variable operacionalizada** | concepto traducido en una medición reproducible con unidad y fuente | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **tamaño de muestra suficiente** | número de observaciones necesario para detectar el efecto que importaría | Construye un caso límite donde el concepto se confunde con el anterior. |
| **incertidumbre declarada** | rango dentro del cual se espera que esté el valor real | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **asociación frente a causalidad** | distinción entre variables que se mueven juntas y variables donde una produce la otra | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir las variables y su forma de medición → 2. calcular el tamaño de muestra según el efecto mínimo relevante → 3. recolectar con procedimiento uniforme → 4. reportar estimación e incertidumbre → 5. distinguir explícitamente asociación de causalidad
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Más muestra no arregla una variable mal definida. Precisión sin validez sólo produce error con más decimales.

## 📖 Desarrollo

### 1. Variable operacionalizada: mecanismo central

**Variable operacionalizada** se entiende aquí como **concepto traducido en una medición reproducible con unidad y fuente**.

Operacionalizar una variable es decidir cómo se convierte un concepto en un número que otra persona podría reproducir. «Cliente activo» no es una variable hasta que alguien fija qué acción, en qué ventana y con qué frecuencia lo constituye. Esa decisión no es técnica sino sustantiva: distintas definiciones de actividad producen tasas de retención que difieren en decenas de puntos, y todas son igualmente calculables.

**De dónde viene esta afirmación.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta la idea que sostiene este bloque: la distinción entre correlación observada y causalidad y qué exige cada una. Búscala en los capítulos sobre inferencia y sesgo. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «potencia del estudio» debería moverse cuando cambie **variable operacionalizada**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **tamaño de muestra suficiente**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Tamaño de muestra suficiente: frontera conceptual y error de clasificación

**Definición operacional:** número de observaciones necesario para detectar el efecto que importaría. Su valor está en distinguirlo de **variable operacionalizada**.

La distinción entre asociación y causalidad es la frontera que separa un análisis útil de una recomendación peligrosa. Que los clientes que usan cierto módulo renueven más no significa que el módulo produzca renovación: puede ser que las cuentas más comprometidas usen más módulos. Actuar sobre la asociación —empujar el módulo— sólo funciona si la relación era causal, y determinarlo exige un diseño distinto del que produjo el hallazgo.

**Contraste bibliográfico.** Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) aporta aquí una distinción concreta: el efecto mínimo relevante como base del cálculo de muestra (los capítulos sobre potencia y tamaño de muestra). Formula dos mini-casos: uno que satisface la definición de **tamaño de muestra suficiente** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «calcular el tamaño de muestra según el efecto mínimo relevante», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Incertidumbre declarada: operacionalización y medición

**Incertidumbre declarada** significa **rango dentro del cual se espera que esté el valor real**.

La incertidumbre declarada es parte del resultado, no un apéndice. Un número sin intervalo invita a comparaciones que no corresponden: dos periodos con 12,1 % y 12,7 % pueden ser indistinguibles y aparecer en el informe como una mejora. La ficha debe registrar la incertidumbre en la misma línea que el valor, y el tablero debe mostrarla, porque nadie va a buscarla a una nota al pie.

Ficha de medición obligatoria para **potencia del estudio**: `probabilidad de detectar el efecto mínimo relevante con la muestra disponible, calculada antes de recolectar`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Naresh K. Malhotra — *Marketing Research: An Applied Orientation* (2019, 7.ª ed.) pone una condición sobre la medición: la construcción de escalas y las amenazas a la validez del constructo (los capítulos sobre medición y escalamiento). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Asociación frente a causalidad: trade-offs y efectos de segundo orden

**Definición:** distinción entre variables que se mueven juntas y variables donde una produce la otra.

Mayor precisión exige más datos, más tiempo y a veces más intrusión sobre el cliente. Hay decisiones que no la requieren: si la acción es la misma para cualquier valor dentro de un rango amplio, invertir en estrechar el intervalo es desperdicio. La pregunta previa a cualquier refinamiento metodológico es qué decisión cambiaría con el número más preciso.

**Lo que aporta la fuente.** Donald J. Wheeler — *Understanding Variation* (2000) aporta el criterio para pesar el intercambio: la distinción entre variación común y variación especial antes de reaccionar (los capítulos que introducen la distinción). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **consistencia entre olas** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **asociación frente a causalidad** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «distinguir explícitamente asociación de causalidad», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Los métodos cuantitativos suponen que lo medido representa el fenómeno. Cuando el fenómeno es reciente, cambió de definición o depende de un sistema que se modificó a mitad del periodo, la serie no es comparable aunque el sistema la muestre continua. Antes de analizar una tendencia hay que verificar que la definición no cambió durante la ventana.

**Frontera declarada.** Más muestra no arregla una variable mal definida. Precisión sin validez sólo produce error con más decimales. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Investigar para confirmar una decisión ya tomada y presentar el resultado como hallazgo.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar investigación cuantitativa no consiste en sumar definiciones. Empieza por **variable operacionalizada**, contrasta **tamaño de muestra suficiente** con **incertidumbre declarada**, incorpora **asociación frente a causalidad** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Una síntesis correcta indica qué evidencia falta y qué decisión se posterga hasta obtenerla.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La distinción entre correlación observada y causalidad y qué exige cada una | Los capítulos sobre inferencia y sesgo | ¿Qué debería observarse en **variable operacionalizada** si aquí opera «la distinción entre correlación observada y causalidad y qué exige cada una»? ¿Y qué observación lo desmentiría en este caso? |
| Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) | El efecto mínimo relevante como base del cálculo de muestra | Los capítulos sobre potencia y tamaño de muestra | ¿Qué debería observarse en **tamaño de muestra suficiente** si aquí opera «el efecto mínimo relevante como base del cálculo de muestra»? ¿Y qué observación lo desmentiría en este caso? |
| Naresh K. Malhotra — *Marketing Research: An Applied Orientation* (2019, 7.ª ed.) | La construcción de escalas y las amenazas a la validez del constructo | Los capítulos sobre medición y escalamiento | ¿Qué debería observarse en **incertidumbre declarada** si aquí opera «la construcción de escalas y las amenazas a la validez del constructo»? ¿Y qué observación lo desmentiría en este caso? |
| Donald J. Wheeler — *Understanding Variation* (2000) | La distinción entre variación común y variación especial antes de reaccionar | Los capítulos que introducen la distinción | ¿Qué debería observarse en **asociación frente a causalidad** si aquí opera «la distinción entre variación común y variación especial antes de reaccionar»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El informe de Ruta Andina afirma que «los clientes del sur convierten 15 % más». La diferencia proviene de 11 observaciones y ningún intervalo acompaña la cifra.

**Paso 1 — Definir las variables y su forma de medición.** El equipo escribe primero el supuesto asociado a **variable operacionalizada** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **potencia del estudio** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Calcular el tamaño de muestra según el efecto mínimo relevante.** El trabajo aquí es separar lo observado de lo inferido sobre **tamaño de muestra suficiente**. La evidencia que ordena la discusión es **proporción de resultados con intervalo reportado**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Recolectar con procedimiento uniforme.** El riesgo de este paso es cerrar demasiado rápido alrededor de **incertidumbre declarada**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **consistencia entre olas** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Reportar estimación e incertidumbre.** Con **asociación frente a causalidad** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **potencia del estudio** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Distinguir explícitamente asociación de causalidad.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **variable operacionalizada**. **proporción de resultados con intervalo reportado** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **variable operacionalizada** | Concepto traducido en una medición reproducible con unidad y fuente | Cuando **potencia del estudio** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **tamaño de muestra suficiente** | Número de observaciones necesario para detectar el efecto que importaría | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Más muestra no arregla una variable mal definida. Precisión sin validez sólo produce error con más decimales.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre investigación cuantitativa |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Market researcher, Product marketing y Consultor comercial. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El informe de Ruta Andina afirma que «los clientes del sur convierten 15 % más». La diferencia proviene de 11 observaciones y ningún intervalo acompaña la cifra.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir las variables y su forma de medición → calcular el tamaño de muestra según el efecto mínimo relevante → recolectar con procedimiento uniforme → reportar estimación e incertidumbre → distinguir explícitamente asociación de causalidad** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **potencia del estudio**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Data Science for Business* y la de *Trustworthy Online Controlled Experiments*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **variable operacionalizada** y **tamaño de muestra suficiente** como sinónimos | Se perdió la distinción entre «concepto traducido en una medición reproducible con unidad y fuente» y «número de observaciones necesario para detectar el efecto que importaría» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «distinguir explícitamente asociación de causalidad» | Se saltó «definir las variables y su forma de medición»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **potencia del estudio** | La métrica local reemplazó al resultado del sistema | Contrástala con **consistencia entre olas** y explicita el costo de oportunidad. |
| Reportar diferencias sin denominador ni incertidumbre | Error específico de esta clase | Acompaña toda comparación con tamaño de muestra e intervalo, o preséntala como observación exploratoria. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **variable operacionalizada** y **tamaño de muestra suficiente** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **incertidumbre declarada** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir las variables y su forma de medición» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **potencia del estudio** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Más muestra no arregla una variable mal definida. Precisión sin validez sólo produce error con más decimales»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **incertidumbre declarada** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **potencia del estudio**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Data Science for Business* y *Understanding Variation*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Investigar para confirmar una decisión ya tomada y presentar el resultado como hallazgo.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P03-C07-investigacion-cuantitativa/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **potencia del estudio**, **proporción de resultados con intervalo reportado** y **consistencia entre olas** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **informe de oportunidad de mercado con método, muestra, límites y decisión recomendada**.

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

- Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) · ISBN 9781449374280 — **aporta a esta clase:** la distinción entre correlación observada y causalidad y qué exige cada una. **Dónde buscarlo:** los capítulos sobre inferencia y sesgo. Registra edición y páginas consultadas en tu nota de lectura.
- Ron Kohavi, Diane Tang y Ya Xu — [*Trustworthy Online Controlled Experiments*](https://openlibrary.org/isbn/9781108601375) (2020) · ISBN 9781108601375 — **aporta a esta clase:** el efecto mínimo relevante como base del cálculo de muestra. **Dónde buscarlo:** los capítulos sobre potencia y tamaño de muestra. Registra edición y páginas consultadas en tu nota de lectura.
- Naresh K. Malhotra — [*Marketing Research: An Applied Orientation*](https://openlibrary.org/isbn/9781292265636) (2019, 7.ª ed.) · ISBN 9781292265636 — **aporta a esta clase:** la construcción de escalas y las amenazas a la validez del constructo. **Dónde buscarlo:** los capítulos sobre medición y escalamiento. Registra edición y páginas consultadas en tu nota de lectura.
- Donald J. Wheeler — [*Understanding Variation*](https://openlibrary.org/isbn/9780945320531) (2000) · ISBN 9780945320531 — **aporta a esta clase:** la distinción entre variación común y variación especial antes de reaccionar. **Dónde buscarlo:** los capítulos que introducen la distinción. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 06 · Investigación cualitativa](class-06-investigacion-cualitativa.md) · [Índice de la parte](README.md) · [Clase 08 · TAM, SAM y SOM](class-08-tam-sam-y-som.md) →
