---
title: "Google Ads: arquitectura conceptual"
type: class
language: es
standard: clase-profunda-v2
part: 14
class: 05
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["geddes", "kaushik", "chaffey", "enge-seo"]
anchors: {"chaffey": "modelo-canal", "enge-seo": "intencion", "geddes": "estructura-cuenta", "kaushik": "segmentacion"}
updated: 2026-08-19
---

# Clase 14.05 — Google Ads: arquitectura conceptual

**Parte 14 · Publicidad y performance marketing** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 14.04 — *Creatividades*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de costo por oportunidad por intención para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La estructura de cuenta por intención como condición del control presupuestario — Brad Geddes. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La estructura de una cuenta de búsqueda determina el control del presupuesto y la relevancia. Organizar por intención —y no por catálogo de productos— permite escribir anuncios pertinentes y asignar presupuesto donde hay retorno. Las decisiones estructurales importantes son pocas: separación por intención, tipos de coincidencia, exclusiones y correspondencia entre anuncio y página.

La clase trata el tema como un problema de evidencia y de consecuencia, no como vocabulario. La parte 14 busca **invertir en medios pagados con control de costo, calidad y riesgo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **google Ads: arquitectura conceptual** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué unidad de resultado estoy comprando y a qué costo marginal deja de tener sentido?

Los conceptos que estructuran la sesión son **estructura por intención**, **tipo de coincidencia**, **correspondencia anuncio-página** y **control presupuestario**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `estructura por intención`, `tipo de coincidencia`, `correspondencia anuncio-página` y `control presupuestario` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Publicidad y performance marketing**.
3. **Aplicar** la secuencia **clasificar términos por intención → estructurar campañas y grupos según esa clasificación → definir tipos de coincidencia y exclusiones → vincular cada grupo a una página coherente → revisar el informe de términos semanalmente** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **costo por oportunidad por intención**, **proporción de gasto en términos no deseados** y **correspondencia auditada** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **estructura por intención** y **tipo de coincidencia** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **costo por oportunidad por intención**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **estructura por intención** | organización de campañas según lo que busca el usuario y no según el producto | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **tipo de coincidencia** | regla que define qué tan cerca debe estar la búsqueda del término configurado | Da un hecho compatible con la definición y otro que la refute. |
| **correspondencia anuncio-página** | coherencia entre lo que promete el anuncio y lo que muestra el destino | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **control presupuestario** | capacidad de asignar y limitar gasto por intención | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. clasificar términos por intención → 2. estructurar campañas y grupos según esa clasificación → 3. definir tipos de coincidencia y exclusiones → 4. vincular cada grupo a una página coherente → 5. revisar el informe de términos semanalmente
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Las plataformas avanzan hacia automatización que reduce el control estructural. La arquitectura sigue importando, pero su forma cambia y debe revisarse.

## 📖 Desarrollo

### 1. Estructura por intención: mecanismo central

**Estructura por intención** se entiende aquí como **organización de campañas según lo que busca el usuario y no según el producto**.

La arquitectura de una cuenta de búsqueda determina qué se puede controlar. Agrupar por intención permite asignar presupuesto y ofertas según el valor esperado; agrupar por producto o por conveniencia administrativa obliga a promediar rendimientos distintos. La estructura se decide una vez y condiciona la gestión durante años.

**De dónde viene esta afirmación.** Brad Geddes — *Advanced Google AdWords* (2014, 3.ª ed.) aporta la idea que sostiene este bloque: la estructura de cuenta por intención como condición del control presupuestario. Búscala en los capítulos sobre organización de campañas. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «costo por oportunidad por intención» debería moverse cuando cambie **estructura por intención**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **tipo de coincidencia**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Tipo de coincidencia: frontera conceptual y error de clasificación

**Definición operacional:** regla que define qué tan cerca debe estar la búsqueda del término configurado. Su valor está en distinguirlo de **estructura por intención**.

El tipo de coincidencia define qué consultas activan cada término, y su uso ha cambiado con las modificaciones de las plataformas. Lo que se mantiene es el principio: cuanto más amplia la coincidencia, mayor el alcance y menor el control. La revisión de consultas reales es lo que permite gestionar esa apertura sin perder eficiencia.

**Contraste bibliográfico.** Avinash Kaushik — *Web Analytics 2.0* (2009) aporta aquí una distinción concreta: la segmentación como condición para que un promedio signifique algo (el capítulo sobre segmentación de datos). Formula dos mini-casos: uno que satisface la definición de **tipo de coincidencia** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «estructurar campañas y grupos según esa clasificación», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Correspondencia anuncio-página: operacionalización y medición

**Correspondencia anuncio-página** significa **coherencia entre lo que promete el anuncio y lo que muestra el destino**.

La correspondencia entre anuncio y página de destino afecta tanto a la conversión como al costo, porque la plataforma la considera en su estimación de calidad. Una campaña con anuncios específicos que llevan a una página genérica desperdicia esa correspondencia y paga más por cada clic sin que nadie lo note.

Ficha de medición obligatoria para **costo por oportunidad por intención**: `gasto dividido por oportunidades calificadas, por grupo de intención`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) pone una condición sobre la medición: el modelo de contribución de canal a la conversión (los capítulos sobre estrategia de canales). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Control presupuestario: trade-offs y efectos de segundo orden

**Definición:** capacidad de asignar y limitar gasto por intención.

Cuentas más granulares permiten control fino y fragmentan el volumen, con lo que cada grupo tiene menos datos para optimizar y las plataformas automatizadas rinden peor. La tendencia actual favorece estructuras más consolidadas, pero esa recomendación depende del volumen: con poco tráfico, la fragmentación es especialmente dañina.

**Lo que aporta la fuente.** Eric Enge, Stephan Spencer y Jessie Stricchiola — *The Art of SEO* (2023, 4.ª ed.) aporta el criterio para pesar el intercambio: la intención de búsqueda como criterio de priorización por encima del volumen (los capítulos sobre investigación de palabras clave). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **correspondencia auditada** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **control presupuestario** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar el informe de términos semanalmente», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Las plataformas cambian sus reglas de coincidencia, sus opciones de puja y sus métricas con frecuencia. Una estructura optimizada para las condiciones de hace dos años puede estar trabajando en contra hoy. Revisar la arquitectura periódicamente, y no sólo las campañas, es parte del mantenimiento.

**Frontera declarada.** Las plataformas avanzan hacia automatización que reduce el control estructural. La arquitectura sigue importando, pero su forma cambia y debe revisarse. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Atribuirse demanda existente, inflar el retorno y decidir presupuesto sobre una ilusión.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar google Ads: arquitectura conceptual no consiste en sumar definiciones. Empieza por **estructura por intención**, contrasta **tipo de coincidencia** con **correspondencia anuncio-página**, incorpora **control presupuestario** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Brad Geddes — *Advanced Google AdWords* (2014, 3.ª ed.) | La estructura de cuenta por intención como condición del control presupuestario | Los capítulos sobre organización de campañas | ¿Qué debería observarse en **estructura por intención** si aquí opera «la estructura de cuenta por intención como condición del control presupuestario»? ¿Y qué observación lo desmentiría en este caso? |
| Avinash Kaushik — *Web Analytics 2.0* (2009) | La segmentación como condición para que un promedio signifique algo | El capítulo sobre segmentación de datos | ¿Qué debería observarse en **tipo de coincidencia** si aquí opera «la segmentación como condición para que un promedio signifique algo»? ¿Y qué observación lo desmentiría en este caso? |
| Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) | El modelo de contribución de canal a la conversión | Los capítulos sobre estrategia de canales | ¿Qué debería observarse en **correspondencia anuncio-página** si aquí opera «el modelo de contribución de canal a la conversión»? ¿Y qué observación lo desmentiría en este caso? |
| Eric Enge, Stephan Spencer y Jessie Stricchiola — *The Art of SEO* (2023, 4.ª ed.) | La intención de búsqueda como criterio de priorización por encima del volumen | Los capítulos sobre investigación de palabras clave | ¿Qué debería observarse en **control presupuestario** si aquí opera «la intención de búsqueda como criterio de priorización por encima del volumen»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** La cuenta de Ruta Andina tiene una sola campaña con 400 términos y un único anuncio. No es posible saber qué intención produce negocios ni limitar el gasto donde no los produce.

**Paso 1 — Clasificar términos por intención.** El equipo escribe primero el supuesto asociado a **estructura por intención** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **costo por oportunidad por intención** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Estructurar campañas y grupos según esa clasificación.** El trabajo aquí es separar lo observado de lo inferido sobre **tipo de coincidencia**. La evidencia que ordena la discusión es **proporción de gasto en términos no deseados**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Definir tipos de coincidencia y exclusiones.** El riesgo de este paso es cerrar demasiado rápido alrededor de **correspondencia anuncio-página**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **correspondencia auditada** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Vincular cada grupo a una página coherente.** Con **control presupuestario** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **costo por oportunidad por intención** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar el informe de términos semanalmente.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **estructura por intención**. **proporción de gasto en términos no deseados** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **estructura por intención** | Organización de campañas según lo que busca el usuario y no según el producto | Cuando **costo por oportunidad por intención** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **tipo de coincidencia** | Regla que define qué tan cerca debe estar la búsqueda del término configurado | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Las plataformas avanzan hacia automatización que reduce el control estructural. La arquitectura sigue importando, pero su forma cambia y debe revisarse.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre google Ads: arquitectura conceptual |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Performance marketer, Media buyer y Growth marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

La cuenta de Ruta Andina tiene una sola campaña con 400 términos y un único anuncio. No es posible saber qué intención produce negocios ni limitar el gasto donde no los produce.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **clasificar términos por intención → estructurar campañas y grupos según esa clasificación → definir tipos de coincidencia y exclusiones → vincular cada grupo a una página coherente → revisar el informe de términos semanalmente** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **costo por oportunidad por intención**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Advanced Google AdWords* y la de *Web Analytics 2.0*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **estructura por intención** y **tipo de coincidencia** como sinónimos | Se perdió la distinción entre «organización de campañas según lo que busca el usuario y no según el producto» y «regla que define qué tan cerca debe estar la búsqueda del término configurado» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar el informe de términos semanalmente» | Se saltó «clasificar términos por intención»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **costo por oportunidad por intención** | La métrica local reemplazó al resultado del sistema | Contrástala con **correspondencia auditada** y explicita el costo de oportunidad. |
| Estructurar la cuenta por catálogo de productos | Error específico de esta clase | Reorganiza por intención de búsqueda y vincula cada grupo a una página coherente. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **estructura por intención** y **tipo de coincidencia** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **correspondencia anuncio-página** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «clasificar términos por intención» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **costo por oportunidad por intención** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Las plataformas avanzan hacia automatización que reduce el control estructural. La arquitectura sigue importando, pero su forma cambia y debe revisarse»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **correspondencia anuncio-página** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **costo por oportunidad por intención**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Advanced Google AdWords* y *The Art of SEO*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Atribuirse demanda existente, inflar el retorno y decidir presupuesto sobre una ilusión.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P14-C05-google-ads-arquitectura-conceptual/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **costo por oportunidad por intención**, **proporción de gasto en términos no deseados** y **correspondencia auditada** con fuente, ventana y lectura prohibida.
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

Cada obra aparece con la idea concreta que aporta a esta clase. Si al leer no encuentras esa idea, la cita está mal puesta y corresponde reportarlo como error del material.

- Brad Geddes — *Advanced Google AdWords* (2014, 3.ª ed.) — **aporta a esta clase:** la estructura de cuenta por intención como condición del control presupuestario. **Dónde buscarlo:** los capítulos sobre organización de campañas. Registra edición y páginas consultadas en tu nota de lectura.
- Avinash Kaushik — *Web Analytics 2.0* (2009) — **aporta a esta clase:** la segmentación como condición para que un promedio signifique algo. **Dónde buscarlo:** el capítulo sobre segmentación de datos. Registra edición y páginas consultadas en tu nota de lectura.
- Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) — **aporta a esta clase:** el modelo de contribución de canal a la conversión. **Dónde buscarlo:** los capítulos sobre estrategia de canales. Registra edición y páginas consultadas en tu nota de lectura.
- Eric Enge, Stephan Spencer y Jessie Stricchiola — *The Art of SEO* (2023, 4.ª ed.) — **aporta a esta clase:** la intención de búsqueda como criterio de priorización por encima del volumen. **Dónde buscarlo:** los capítulos sobre investigación de palabras clave. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 04 · Creatividades](class-04-creatividades.md) · [Índice de la parte](README.md) · [Clase 06 · Meta Ads: arquitectura conceptual](class-06-meta-ads-arquitectura-conceptual.md) →
