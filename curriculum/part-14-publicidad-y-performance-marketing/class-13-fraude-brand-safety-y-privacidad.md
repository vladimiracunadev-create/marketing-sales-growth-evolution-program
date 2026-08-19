# Clase 14.13 — Fraude, brand safety y privacidad

Clase 13 de 14 de la parte [14 — Publicidad y performance marketing](README.md), de nivel Adquisición. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 14.12, *Optimización de campañas*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de proporción de tráfico no válido con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La exigencia de auditabilidad en modelos que afectan a personas — Cathy O'Neil. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

La publicidad digital tiene tres riesgos que no aparecen en el tablero: tráfico no humano que consume presupuesto, aparición junto a contenido que daña la marca y tratamiento de datos personales sin base suficiente. Los tres se gestionan con controles previos —listas de exclusión, verificación de inventario, revisión de consentimiento— y no con reacciones posteriores.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 14 busca **invertir en medios pagados con control de costo, calidad y riesgo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **fraude, brand safety y privacidad** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué unidad de resultado estoy comprando y a qué costo marginal deja de tener sentido?

Los conceptos que estructuran la sesión son **tráfico no válido**, **seguridad de marca**, **consentimiento de cookies** y **control previo**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `tráfico no válido`, `seguridad de marca`, `consentimiento de cookies` y `control previo` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Publicidad y performance marketing**.
3. **Aplicar** la secuencia **revisar los informes de calidad de tráfico → definir listas de exclusión de sitios y categorías → verificar el mecanismo de consentimiento del sitio propio → auditar el tratamiento de datos en las plataformas usadas → documentar los controles y revisarlos cada semestre** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **proporción de tráfico no válido**, **apariciones en contexto no deseado** y **tasa de consentimiento válido** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **tráfico no válido** y **seguridad de marca** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **proporción de tráfico no válido**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **tráfico no válido** | interacciones generadas por sistemas automatizados que no corresponden a personas | Construye un caso límite donde el concepto se confunde con el anterior. |
| **seguridad de marca** | control sobre el entorno donde aparece el anuncio | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **consentimiento de cookies** | autorización informada para el uso de identificadores de seguimiento | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **control previo** | medida establecida antes de la exposición que reduce el riesgo | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. revisar los informes de calidad de tráfico → 2. definir listas de exclusión de sitios y categorías → 3. verificar el mecanismo de consentimiento del sitio propio → 4. auditar el tratamiento de datos en las plataformas usadas → 5. documentar los controles y revisarlos cada semestre
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Los controles reducen el riesgo pero también el alcance disponible y pueden subir el costo. La decisión debe ser explícita y no un efecto colateral.

## 📖 Desarrollo

### 1. Tráfico no válido: mecanismo central

**Tráfico no válido** se entiende aquí como **interacciones generadas por sistemas automatizados que no corresponden a personas**.

El tráfico no válido, la seguridad de marca y la privacidad son tres riesgos distintos que comparten una característica: no aparecen en las métricas de desempeño y sólo se detectan si se buscan. Una campaña puede mostrar excelentes números y estar comprando tráfico fraudulento o apareciendo junto a contenido que daña la marca.

**De dónde viene esta afirmación.** Cathy O'Neil — *Weapons of Math Destruction* (2016) aporta la idea que sostiene este bloque: la exigencia de auditabilidad en modelos que afectan a personas. Búscala en el capítulo final sobre desarme. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «proporción de tráfico no válido» debería moverse cuando cambie **tráfico no válido**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **seguridad de marca**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Seguridad de marca: frontera conceptual y error de clasificación

**Definición operacional:** control sobre el entorno donde aparece el anuncio. Su valor está en distinguirlo de **tráfico no válido**.

El tráfico no válido se estima observando patrones anómalos: tasas de rebote extremas, concentraciones geográficas inexplicables, comportamientos idénticos. Ninguna verificación es definitiva, pero la ausencia total de revisión garantiza no detectarlo. Las herramientas de las propias plataformas ofrecen filtros que conviene activar y auditar.

**Contraste bibliográfico.** Avinash Kaushik — *Web Analytics 2.0* (2009) aporta aquí una distinción concreta: la prueba del «¿y entonces qué?» aplicada tres veces a cada informe (los capítulos sobre informes accionables). Formula dos mini-casos: uno que satisface la definición de **seguridad de marca** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «definir listas de exclusión de sitios y categorías», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Consentimiento de cookies: operacionalización y medición

**Consentimiento de cookies** significa **autorización informada para el uso de identificadores de seguimiento**.

La seguridad de marca exige definir con antelación en qué contextos no se quiere aparecer y aplicar las exclusiones disponibles. Esa definición debe ser una decisión documentada y no una reacción tras un incidente. Las listas de exclusión requieren revisión periódica porque el inventario cambia.

Ficha de medición obligatoria para **proporción de tráfico no válido**: `interacciones marcadas como inválidas, sobre interacciones totales`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** NIST — *AI Risk Management Framework 1.0* (2023) pone una condición sobre la medición: el riesgo evaluado en el contexto de uso y no en abstracto (la sección sobre mapeo del contexto). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Control previo: trade-offs y efectos de segundo orden

**Definición:** medida establecida antes de la exposición que reduce el riesgo.

Controles más estrictos reducen el riesgo y el alcance disponible, con lo que sube el costo. Controles laxos abaratan y exponen. La decisión debe tomarse considerando el costo reputacional potencial, que en marcas con alta visibilidad puede superar con mucho el ahorro en medios.

**Lo que aporta la fuente.** Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) aporta el criterio para pesar el intercambio: el gobierno de la operación digital: capacidades, procesos y medición (los capítulos sobre transformación y capacidades). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **tasa de consentimiento válido** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **control previo** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «documentar los controles y revisarlos cada semestre», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El consentimiento de cookies y el tratamiento de datos publicitarios están regulados y su incumplimiento tiene consecuencias que exceden lo comercial. La configuración del consentimiento debe reflejar lo que efectivamente ocurre en el sitio, y esa correspondencia hay que verificarla técnicamente. La revisión legal del marco vigente es obligatoria y no la sustituye este material.

**Frontera declarada.** Los controles reducen el riesgo pero también el alcance disponible y pueden subir el costo. La decisión debe ser explícita y no un efecto colateral. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Atribuirse demanda existente, inflar el retorno y decidir presupuesto sobre una ilusión.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar fraude, brand safety y privacidad no consiste en sumar definiciones. Empieza por **tráfico no válido**, contrasta **seguridad de marca** con **consentimiento de cookies**, incorpora **control previo** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Cathy O'Neil — *Weapons of Math Destruction* (2016) | La exigencia de auditabilidad en modelos que afectan a personas | El capítulo final sobre desarme | ¿Qué debería observarse en **tráfico no válido** si aquí opera «la exigencia de auditabilidad en modelos que afectan a personas»? ¿Y qué observación lo desmentiría en este caso? |
| Avinash Kaushik — *Web Analytics 2.0* (2009) | La prueba del «¿y entonces qué?» aplicada tres veces a cada informe | Los capítulos sobre informes accionables | ¿Qué debería observarse en **seguridad de marca** si aquí opera «la prueba del «¿y entonces qué?» aplicada tres veces a cada informe»? ¿Y qué observación lo desmentiría en este caso? |
| NIST — *AI Risk Management Framework 1.0* (2023) | El riesgo evaluado en el contexto de uso y no en abstracto | La sección sobre mapeo del contexto | ¿Qué debería observarse en **consentimiento de cookies** si aquí opera «el riesgo evaluado en el contexto de uso y no en abstracto»? ¿Y qué observación lo desmentiría en este caso? |
| Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) | El gobierno de la operación digital: capacidades, procesos y medición | Los capítulos sobre transformación y capacidades | ¿Qué debería observarse en **control previo** si aquí opera «el gobierno de la operación digital: capacidades, procesos y medición»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina descubre que el 14 % de sus clics proviene de sitios de contenido descargable y que su banner apareció junto a contenido incompatible con su marca.

**Paso 1 — Revisar los informes de calidad de tráfico.** El equipo escribe primero el supuesto asociado a **tráfico no válido** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **proporción de tráfico no válido** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Definir listas de exclusión de sitios y categorías.** El trabajo aquí es separar lo observado de lo inferido sobre **seguridad de marca**. La evidencia que ordena la discusión es **apariciones en contexto no deseado**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Verificar el mecanismo de consentimiento del sitio propio.** El riesgo de este paso es cerrar demasiado rápido alrededor de **consentimiento de cookies**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **tasa de consentimiento válido** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Auditar el tratamiento de datos en las plataformas usadas.** Con **control previo** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **proporción de tráfico no válido** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Documentar los controles y revisarlos cada semestre.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **tráfico no válido**. **apariciones en contexto no deseado** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **tráfico no válido** | Interacciones generadas por sistemas automatizados que no corresponden a personas | Cuando **proporción de tráfico no válido** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **seguridad de marca** | Control sobre el entorno donde aparece el anuncio | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Los controles reducen el riesgo pero también el alcance disponible y pueden subir el costo. La decisión debe ser explícita y no un efecto colateral.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre fraude, brand safety y privacidad |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Performance marketer, Media buyer y Growth marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina descubre que el 14 % de sus clics proviene de sitios de contenido descargable y que su banner apareció junto a contenido incompatible con su marca.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **revisar los informes de calidad de tráfico → definir listas de exclusión de sitios y categorías → verificar el mecanismo de consentimiento del sitio propio → auditar el tratamiento de datos en las plataformas usadas → documentar los controles y revisarlos cada semestre** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **proporción de tráfico no válido**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Weapons of Math Destruction* y la de *Web Analytics 2.0*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **tráfico no válido** y **seguridad de marca** como sinónimos | Se perdió la distinción entre «interacciones generadas por sistemas automatizados que no corresponden a personas» y «control sobre el entorno donde aparece el anuncio» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «documentar los controles y revisarlos cada semestre» | Se saltó «revisar los informes de calidad de tráfico»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **proporción de tráfico no válido** | La métrica local reemplazó al resultado del sistema | Contrástala con **tasa de consentimiento válido** y explicita el costo de oportunidad. |
| Operar sin listas de exclusión ni revisión de tráfico | Error específico de esta clase | Define exclusiones y revisa mensualmente los informes de calidad de tráfico. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **tráfico no válido** y **seguridad de marca** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **consentimiento de cookies** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «revisar los informes de calidad de tráfico» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **proporción de tráfico no válido** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Los controles reducen el riesgo pero también el alcance disponible y pueden subir el costo. La decisión debe ser explícita y no un efecto colateral»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **consentimiento de cookies** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **proporción de tráfico no válido**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *Weapons of Math Destruction* y *Digital Marketing*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Atribuirse demanda existente, inflar el retorno y decidir presupuesto sobre una ilusión.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, comprueba la norma en su texto vigente. Los enlaces van al texto completo publicado por la Biblioteca del Congreso Nacional; son gratuitos y no hace falta creerle a este material.

- **Consumo y comercio.** [Ley 19.496](https://www.bcn.cl/leychile/navegar?idNorma=61438) — *Establece normas sobre protección de los derechos de los consumidores* (Ministerio de Economía, Fomento y Reconstrucción), y su reglamento de comercio electrónico, [Decreto 6/2021](https://www.bcn.cl/leychile/navegar?idNorma=1165504) — *Aprueba reglamento de comercio electrónico* (Ministerio de Economía, Fomento y Turismo).
- **Datos personales.** [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales* (Ministerio Secretaría General de la Presidencia), que sustituye progresivamente a [Ley 19.628](https://www.bcn.cl/leychile/navegar?idNorma=141599) — *Sobre protección de la vida privada* (Ministerio Secretaría General de la Presidencia).
- **Derecho a retracto.** [Decreto 52/2024](https://www.bcn.cl/leychile/navegar?idNorma=1206144) — *Aprueba reglamento que regula la forma y condiciones en que los proveedores deberán comunicar la exclusión del derecho a retracto y los bienes en que excepcionalmente y por su naturaleza procederá tal exclusión* (Ministerio de Economía, Fomento y Turismo).

Dentro del repositorio, el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) ordena qué norma aplica a cada decisión comercial, [datos personales y ética](../../docs/DATOS-PERSONALES-Y-ETICA.md) desarrolla el tratamiento de datos y [fuentes oficiales](../../docs/FUENTES-OFICIALES.md) lista los organismos con su fecha de consulta. Ninguno de esos documentos reemplaza al texto legal.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P14-C13-fraude-brand-safety-y-privacidad/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **proporción de tráfico no válido**, **apariciones en contexto no deseado** y **tasa de consentimiento válido** con fuente, ventana y lectura prohibida.
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

Aquí conviene separar dos cosas que suelen ir juntas y no son lo mismo.

**Lo que está comprobado.** Que cada obra existe y cuál es exactamente la edición: el enlace resuelve su ISBN contra el catálogo de OpenLibrary, y eso se revalida periódicamente. Las normas chilenas citadas más arriba enlazan su texto completo y gratuito.

**Lo que es atribución del programa.** Que la idea señalada esté en el capítulo que se indica. Eso es la lectura que este material hace de cada obra, no una cita textual cotejada frase por frase, y se declara así de explícito para que puedas contrastarlo: si abres la obra y no encuentras la idea donde se dice, la cita está mal puesta y **corresponde reportarlo como error del material**. No se citan números de página porque cambian entre ediciones.

- Cathy O'Neil — [*Weapons of Math Destruction*](https://openlibrary.org/isbn/9780141985428) (2016) · ISBN 9780141985428 — **aporta a esta clase:** la exigencia de auditabilidad en modelos que afectan a personas. **Dónde buscarlo:** el capítulo final sobre desarme. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Avinash Kaushik — [*Web Analytics 2.0*](https://openlibrary.org/isbn/9780470596425) (2009) · ISBN 9780470596425 — **aporta a esta clase:** la prueba del «¿y entonces qué?» aplicada tres veces a cada informe. **Dónde buscarlo:** los capítulos sobre informes accionables. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- NIST — [*AI Risk Management Framework 1.0*](https://doi.org/10.6028/NIST.AI.100-1) (2023) · DOI 10.6028/NIST.AI.100-1 — **aporta a esta clase:** el riesgo evaluado en el contexto de uso y no en abstracto. **Dónde buscarlo:** la sección sobre mapeo del contexto. **Acceso:** gratis. Registra edición y páginas consultadas en tu nota de lectura.
- Dave Chaffey y Fiona Ellis-Chadwick — [*Digital Marketing*](https://openlibrary.org/isbn/9781292400990) (2022, 8.ª ed.) · ISBN 9781292400990 — **aporta a esta clase:** el gobierno de la operación digital: capacidades, procesos y medición. **Dónde buscarlo:** los capítulos sobre transformación y capacidades. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 12 · Optimización de campañas](class-12-optimizacion-de-campanas.md) · [Índice de la parte](README.md) · [Clase 14 · Plan de performance marketing](class-14-plan-de-performance-marketing.md) →
