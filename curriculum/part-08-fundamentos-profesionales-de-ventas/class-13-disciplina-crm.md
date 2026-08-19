# Clase 08.13 — Disciplina de CRM

Clase 13 de 14 de la parte [08 — Fundamentos profesionales de ventas](README.md), de nivel Venta. Dura unos 150 minutos.

## 🚦 Antes de empezar

Vienes de la clase 08.12, *Handoff a implementación*: ten a mano su entregable, porque esta sesión lo retoma y lo lleva más lejos.

Trabajarás sobre el caso de la clase. Si prefieres usar datos de tu organización, lo mínimo que necesitas es una serie histórica de completitud de campos críticos con la que calcular una línea base: sin ella podrás discutir el concepto, pero no comprobar si tu decisión mejora algo. Ten también dónde escribir —planilla o cuaderno— y, de la lectura comparada, al menos el índice y los capítulos que se indican al pie.

Calcula 150 minutos de trabajo dirigido más una hora de lectura selectiva. Sabrás que terminaste cuando exista el entregable y puedas responder las seis preguntas de comprobación sin volver al texto; si tienes el entregable pero no las respuestas, lo que produjiste es un documento, no un criterio.

Lee el propósito y la agenda antes que el desarrollo. La agenda dice qué debe salir de cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que producir. No avances de sección sin escribir algo: este material está hecho para dejar decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El acompañamiento dirigido por una métrica diagnóstica por vendedor — Mark Roberge. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

El CRM sólo vale lo que vale su dato. La disciplina de registro no es burocracia: es la condición para que exista forecast, análisis de conversión y continuidad cuando alguien sale del equipo. El error de gestión más frecuente es exigir registro sin devolver valor al vendedor: si el sistema sólo sirve para controlar, el dato se degrada de inmediato.

El contenido se organiza para que la conclusión pueda ser auditada por otra persona del equipo. La parte 08 busca **ejecutar un proceso comercial reproducible que no dependa del talento individual**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **disciplina de CRM** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué debe ocurrir en cada etapa para que la siguiente sea probable y no accidental?

Los conceptos que estructuran la sesión son **campo crítico**, **higiene de datos**, **valor devuelto al usuario** y **registro oportuno**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `campo crítico`, `higiene de datos`, `valor devuelto al usuario` y `registro oportuno` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Fundamentos profesionales de ventas**.
3. **Aplicar** la secuencia **definir el conjunto mínimo de campos críticos → eliminar los campos que nadie usa → devolver valor al vendedor con vistas y alertas útiles → medir completitud y oportunidad del registro → corregir el proceso antes de sancionar a la persona** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **completitud de campos críticos**, **oportunidad del registro** y **duplicados detectados** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **campo crítico** y **higiene de datos** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **completitud de campos críticos**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **campo crítico** | dato sin el cual no puede calcularse forecast ni conversión | Construye un caso límite donde el concepto se confunde con el anterior. |
| **higiene de datos** | conjunto de reglas que mantiene el registro completo, actualizado y sin duplicados | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **valor devuelto al usuario** | beneficio concreto que el vendedor obtiene del sistema por registrar bien | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **registro oportuno** | actualización realizada dentro del plazo definido tras cada interacción | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir el conjunto mínimo de campos críticos → 2. eliminar los campos que nadie usa → 3. devolver valor al vendedor con vistas y alertas útiles → 4. medir completitud y oportunidad del registro → 5. corregir el proceso antes de sancionar a la persona
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Más campos no es más control: cada campo obligatorio adicional reduce la calidad del conjunto. La disciplina se sostiene con pocos campos que realmente se usan.

## 📖 Desarrollo

### 1. Campo crítico: mecanismo central

**Campo crítico** se entiende aquí como **dato sin el cual no puede calcularse forecast ni conversión**.

La disciplina de CRM se justifica sólo si el sistema devuelve valor a quien registra. Un CRM que existe para que la gerencia tenga reportes y que no ayuda al vendedor a vender será completado con el mínimo esfuerzo y con datos de dudosa calidad. El diseño correcto empieza preguntando qué le sirve a quien ingresa el dato.

**De dónde viene esta afirmación.** Mark Roberge — *The Sales Acceleration Formula* (2015) aporta la idea que sostiene este bloque: el acompañamiento dirigido por una métrica diagnóstica por vendedor. Búscala en los capítulos sobre la fórmula de gestión. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «completitud de campos críticos» debería moverse cuando cambie **campo crítico**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **higiene de datos**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Higiene de datos: frontera conceptual y error de clasificación

**Definición operacional:** conjunto de reglas que mantiene el registro completo, actualizado y sin duplicados. Su valor está en distinguirlo de **campo crítico**.

El campo crítico es aquel cuya ausencia impide una decisión. La mayoría de los CRM acumula campos que alguna vez alguien pidió y que ya nadie usa, y cada uno de ellos consume atención y deteriora la calidad de los importantes. Una revisión anual que elimine campos sin uso mejora los datos más que cualquier campaña de disciplina.

**Contraste bibliográfico.** Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) aporta aquí una distinción concreta: el modelo de datos común como condición para que las áreas discutan sobre lo mismo (los capítulos sobre infraestructura de datos comercial). Formula dos mini-casos: uno que satisface la definición de **higiene de datos** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «eliminar los campos que nadie usa», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Valor devuelto al usuario: operacionalización y medición

**Valor devuelto al usuario** significa **beneficio concreto que el vendedor obtiene del sistema por registrar bien**.

La higiene de datos se mide y se gestiona: proporción de oportunidades sin siguiente paso, antigüedad media de la última actualización, registros duplicados, campos obligatorios vacíos. Esos cuatro indicadores, revisados mensualmente, convierten un problema difuso en una lista concreta de correcciones con responsable.

Ficha de medición obligatoria para **completitud de campos críticos**: `registros con todos los campos críticos completos, sobre registros creados`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Andrew S. Grove — *High Output Management* (1983) pone una condición sobre la medición: los indicadores adelantados y pareados que permiten corregir a tiempo (los capítulos sobre medición en la producción). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Registro oportuno: trade-offs y efectos de segundo orden

**Definición:** actualización realizada dentro del plazo definido tras cada interacción.

Exigir más registro mejora la información y consume tiempo comercial. Cada campo obligatorio tiene un costo en minutos por oportunidad que, multiplicado por el volumen, es significativo. La decisión debe hacerse con ese cálculo a la vista y no con el supuesto de que registrar es gratis.

**Lo que aporta la fuente.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta el criterio para pesar el intercambio: la formulación del problema de negocio como problema de datos antes de elegir técnica (los capítulos iniciales sobre pensamiento analítico). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **duplicados detectados** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **registro oportuno** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «corregir el proceso antes de sancionar a la persona», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Los datos del CRM contienen información personal de contactos y están sujetos a la normativa de protección de datos: finalidad declarada, plazo de conservación y derechos del titular. La configuración del sistema debe permitir ejercer esos derechos, y esa capacidad hay que verificarla antes de necesitarla, no cuando llega la primera solicitud.

**Frontera declarada.** Más campos no es más control: cada campo obligatorio adicional reduce la calidad del conjunto. La disciplina se sostiene con pocos campos que realmente se usan. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Presionar por cierre sin diagnóstico y vender a clientes que no pueden obtener valor.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar disciplina de CRM no consiste en sumar definiciones. Empieza por **campo crítico**, contrasta **higiene de datos** con **valor devuelto al usuario**, incorpora **registro oportuno** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Mark Roberge — *The Sales Acceleration Formula* (2015) | El acompañamiento dirigido por una métrica diagnóstica por vendedor | Los capítulos sobre la fórmula de gestión | ¿Qué debería observarse en **campo crítico** si aquí opera «el acompañamiento dirigido por una métrica diagnóstica por vendedor»? ¿Y qué observación lo desmentiría en este caso? |
| Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) | El modelo de datos común como condición para que las áreas discutan sobre lo mismo | Los capítulos sobre infraestructura de datos comercial | ¿Qué debería observarse en **higiene de datos** si aquí opera «el modelo de datos común como condición para que las áreas discutan sobre lo mismo»? ¿Y qué observación lo desmentiría en este caso? |
| Andrew S. Grove — *High Output Management* (1983) | Los indicadores adelantados y pareados que permiten corregir a tiempo | Los capítulos sobre medición en la producción | ¿Qué debería observarse en **valor devuelto al usuario** si aquí opera «los indicadores adelantados y pareados que permiten corregir a tiempo»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La formulación del problema de negocio como problema de datos antes de elegir técnica | Los capítulos iniciales sobre pensamiento analítico | ¿Qué debería observarse en **registro oportuno** si aquí opera «la formulación del problema de negocio como problema de datos antes de elegir técnica»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** El CRM de Ruta Andina exige 23 campos obligatorios. Los vendedores completan con datos falsos para poder guardar y el forecast se construye sobre esa base.

**Paso 1 — Definir el conjunto mínimo de campos críticos.** El equipo escribe primero el supuesto asociado a **campo crítico** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **completitud de campos críticos** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Eliminar los campos que nadie usa.** El trabajo aquí es separar lo observado de lo inferido sobre **higiene de datos**. La evidencia que ordena la discusión es **oportunidad del registro**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Devolver valor al vendedor con vistas y alertas útiles.** El riesgo de este paso es cerrar demasiado rápido alrededor de **valor devuelto al usuario**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **duplicados detectados** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Medir completitud y oportunidad del registro.** Con **registro oportuno** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **completitud de campos críticos** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Corregir el proceso antes de sancionar a la persona.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **campo crítico**. **oportunidad del registro** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **campo crítico** | Dato sin el cual no puede calcularse forecast ni conversión | Cuando **completitud de campos críticos** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **higiene de datos** | Conjunto de reglas que mantiene el registro completo, actualizado y sin duplicados | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Más campos no es más control: cada campo obligatorio adicional reduce la calidad del conjunto. La disciplina se sostiene con pocos campos que realmente se usan.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre disciplina de CRM |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Ejecutivo comercial, SDR y Jefe de ventas. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

El CRM de Ruta Andina exige 23 campos obligatorios. Los vendedores completan con datos falsos para poder guardar y el forecast se construye sobre esa base.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir el conjunto mínimo de campos críticos → eliminar los campos que nadie usa → devolver valor al vendedor con vistas y alertas útiles → medir completitud y oportunidad del registro → corregir el proceso antes de sancionar a la persona** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **completitud de campos críticos**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *The Sales Acceleration Formula* y la de *Revenue Operations*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **campo crítico** y **higiene de datos** como sinónimos | Se perdió la distinción entre «dato sin el cual no puede calcularse forecast ni conversión» y «conjunto de reglas que mantiene el registro completo, actualizado y sin duplicados» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «corregir el proceso antes de sancionar a la persona» | Se saltó «definir el conjunto mínimo de campos críticos»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **completitud de campos críticos** | La métrica local reemplazó al resultado del sistema | Contrástala con **duplicados detectados** y explicita el costo de oportunidad. |
| Exigir registro sin devolver valor | Error específico de esta clase | Reduce los campos obligatorios al mínimo y entrega vistas que el vendedor use para trabajar. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **campo crítico** y **higiene de datos** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **valor devuelto al usuario** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir el conjunto mínimo de campos críticos» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **completitud de campos críticos** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Más campos no es más control: cada campo obligatorio adicional reduce la calidad del conjunto. La disciplina se sostiene con pocos campos que realmente se usan»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **valor devuelto al usuario** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **completitud de campos críticos**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *The Sales Acceleration Formula* y *Data Science for Business*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Presionar por cierre sin diagnóstico y vender a clientes que no pueden obtener valor.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, comprueba la norma en su texto vigente. Los enlaces van al texto completo publicado por la Biblioteca del Congreso Nacional; son gratuitos y no hace falta creerle a este material.

- **Consumo y comercio.** [Ley 19.496](https://www.bcn.cl/leychile/navegar?idNorma=61438) — *Establece normas sobre protección de los derechos de los consumidores* (Ministerio de Economía, Fomento y Reconstrucción), y su reglamento de comercio electrónico, [Decreto 6/2021](https://www.bcn.cl/leychile/navegar?idNorma=1165504) — *Aprueba reglamento de comercio electrónico* (Ministerio de Economía, Fomento y Turismo).
- **Datos personales.** [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) — *Regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales* (Ministerio Secretaría General de la Presidencia), que sustituye progresivamente a [Ley 19.628](https://www.bcn.cl/leychile/navegar?idNorma=141599) — *Sobre protección de la vida privada* (Ministerio Secretaría General de la Presidencia).
- **Derecho a retracto.** [Decreto 52/2024](https://www.bcn.cl/leychile/navegar?idNorma=1206144) — *Aprueba reglamento que regula la forma y condiciones en que los proveedores deberán comunicar la exclusión del derecho a retracto y los bienes en que excepcionalmente y por su naturaleza procederá tal exclusión* (Ministerio de Economía, Fomento y Turismo).

Dentro del repositorio, el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) ordena qué norma aplica a cada decisión comercial, [datos personales y ética](../../docs/DATOS-PERSONALES-Y-ETICA.md) desarrolla el tratamiento de datos y [fuentes oficiales](../../docs/FUENTES-OFICIALES.md) lista los organismos con su fecha de consulta. Ninguno de esos documentos reemplaza al texto legal.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P08-C13-disciplina-crm/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **completitud de campos críticos**, **oportunidad del registro** y **duplicados detectados** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **playbook comercial con etapas, criterios de salida, guiones y materiales**.

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

- Mark Roberge — [*The Sales Acceleration Formula*](https://openlibrary.org/isbn/9781119047018) (2015) · ISBN 9781119047018 — **aporta a esta clase:** el acompañamiento dirigido por una métrica diagnóstica por vendedor. **Dónde buscarlo:** los capítulos sobre la fórmula de gestión. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Stephen G. Diorio y Chris K. Hummel — [*Revenue Operations*](https://openlibrary.org/isbn/9781119871132) (2022) · ISBN 9781119871132 — **aporta a esta clase:** el modelo de datos común como condición para que las áreas discutan sobre lo mismo. **Dónde buscarlo:** los capítulos sobre infraestructura de datos comercial. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Andrew S. Grove — [*High Output Management*](https://openlibrary.org/isbn/9780394532349) (1983) · ISBN 9780394532349 — **aporta a esta clase:** los indicadores adelantados y pareados que permiten corregir a tiempo. **Dónde buscarlo:** los capítulos sobre medición en la producción. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) · ISBN 9781449374280 — **aporta a esta clase:** la formulación del problema de negocio como problema de datos antes de elegir técnica. **Dónde buscarlo:** los capítulos iniciales sobre pensamiento analítico. **Acceso:** comprar o biblioteca. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014); Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.); Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016); William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Sobre la edición.** No busques estas obras sólo por el título: distintas ediciones cambian capítulos y ejemplos, y los anclajes de arriba están hechos sobre la que declara el [registro de fuentes](../../sources/bibliography.json). La bibliografía completa de la parte, con todas sus obras, está en su [índice](README.md).

---

← [Clase 12 · Handoff a implementación](class-12-handoff-a-implementacion.md) · [Índice de la parte](README.md) · [Clase 14 · Playbook comercial básico](class-14-playbook-comercial-basico.md) →
