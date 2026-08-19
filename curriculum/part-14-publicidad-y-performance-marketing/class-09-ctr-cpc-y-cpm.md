---
title: "CTR, CPC y CPM"
type: class
language: es
standard: clase-profunda-v2
part: 14
class: 09
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["kaushik", "geddes", "croll-yoskovitz", "chaffey"]
anchors: {"chaffey": "modelo-canal", "croll-yoskovitz": "una-metrica", "geddes": "subasta", "kaushik": "vanidad"}
updated: 2026-08-19
---

# Clase 14.09 — CTR, CPC y CPM

**Parte 14 · Publicidad y performance marketing** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 14.08 — *Presupuesto y ritmo de gasto*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de tasa de clic por variante para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La distinción entre métricas de vanidad y métricas accionables — Avinash Kaushik. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Las métricas intermedias describen la mecánica del canal: cuánto cuesta llegar, cuánto cuesta una visita y qué proporción reacciona. Son útiles para diagnosticar y peligrosas para decidir: un anuncio con excelente tasa de clic puede atraer al público equivocado. La regla es usar las métricas intermedias para explicar y las de negocio para decidir.

Esta clase existe porque el error que corrige es caro y frecuente en operaciones reales. La parte 14 busca **invertir en medios pagados con control de costo, calidad y riesgo**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **CTR, CPC y CPM** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué unidad de resultado estoy comprando y a qué costo marginal deja de tener sentido?

Los conceptos que estructuran la sesión son **costo por mil impresiones**, **tasa de clic**, **costo por clic** y **métrica de diagnóstico**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `costo por mil impresiones`, `tasa de clic`, `costo por clic` y `métrica de diagnóstico` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Publicidad y performance marketing**.
3. **Aplicar** la secuencia **establecer líneas base de las métricas intermedias → usarlas para diagnosticar dónde está el problema → verificar la calidad del tráfico que producen → decidir con métricas de negocio → documentar la relación entre ambas para el canal** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **tasa de clic por variante**, **costo por clic por audiencia** y **conversión posterior al clic** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **costo por mil impresiones** y **tasa de clic** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **tasa de clic por variante**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **costo por mil impresiones** | precio de alcanzar mil impresiones en la audiencia seleccionada | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **tasa de clic** | clics obtenidos sobre impresiones entregadas | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **costo por clic** | gasto dividido por clics obtenidos | Da un hecho compatible con la definición y otro que la refute. |
| **métrica de diagnóstico** | indicador que explica el desempeño pero no debe gobernar la decisión | Explica qué decisión cambiaría si el concepto estuviera ausente. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. establecer líneas base de las métricas intermedias → 2. usarlas para diagnosticar dónde está el problema → 3. verificar la calidad del tráfico que producen → 4. decidir con métricas de negocio → 5. documentar la relación entre ambas para el canal
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Las métricas intermedias no son comparables entre plataformas ni entre formatos. Compararlas directamente induce conclusiones falsas.

## 📖 Desarrollo

### 1. Costo por mil impresiones: mecanismo central

**Costo por mil impresiones** se entiende aquí como **precio de alcanzar mil impresiones en la audiencia seleccionada**.

Las métricas de plataforma —costo por mil impresiones, tasa de clic, costo por clic— son indicadores de diagnóstico y no de resultado. Sirven para entender por qué el costo por adquisición se movió: si subió el costo por mil, si cayó la tasa de clic, si empeoró la conversión posterior. Usarlas como objetivo lleva a optimizar hacia el lugar equivocado.

**De dónde viene esta afirmación.** Avinash Kaushik — *Web Analytics 2.0* (2009) aporta la idea que sostiene este bloque: la distinción entre métricas de vanidad y métricas accionables. Búscala en los capítulos sobre selección de métricas. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «tasa de clic por variante» debería moverse cuando cambie **costo por mil impresiones**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **tasa de clic**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Tasa de clic: frontera conceptual y error de clasificación

**Definición operacional:** clics obtenidos sobre impresiones entregadas. Su valor está en distinguirlo de **costo por mil impresiones**.

La tasa de clic mide relevancia percibida antes de la visita y no calidad del tráfico. Un anuncio con tasa alta y conversión baja está atrayendo a la audiencia equivocada o prometiendo algo que la página no cumple. Esa combinación es diagnóstica y debería revisarse siempre junta, nunca por separado.

**Contraste bibliográfico.** Brad Geddes — *Advanced Google AdWords* (2014, 3.ª ed.) aporta aquí una distinción concreta: la mecánica de la subasta: no gana quien más paga sino quien combina oferta y relevancia (los capítulos sobre funcionamiento de la subasta). Formula dos mini-casos: uno que satisface la definición de **tasa de clic** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «usarlas para diagnosticar dónde está el problema», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Costo por clic: operacionalización y medición

**Costo por clic** significa **gasto dividido por clics obtenidos**.

La descomposición del costo por adquisición en sus factores —costo por mil, tasa de clic, tasa de conversión— es el ejercicio analítico básico de este canal. Permite identificar cuál de los tres se movió y actuar sobre él. Sin esa descomposición, la discusión sobre una campaña que empeoró se resuelve por opinión.

Ficha de medición obligatoria para **tasa de clic por variante**: `clics sobre impresiones, por variante creativa y audiencia`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) pone una condición sobre la medición: la métrica que importa ahora: una sola, según etapa y modelo de negocio (los capítulos sobre la métrica única). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Métrica de diagnóstico: trade-offs y efectos de segundo orden

**Definición:** indicador que explica el desempeño pero no debe gobernar la decisión.

Optimizar la tasa de clic mejora el costo por clic y puede empeorar el costo por adquisición si atrae tráfico menos calificado. La relación entre métricas intermedias y finales no es monótona, y por eso el objetivo de optimización debe ser siempre el más cercano al resultado de negocio que tenga volumen suficiente.

**Lo que aporta la fuente.** Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) aporta el criterio para pesar el intercambio: el modelo de contribución de canal a la conversión (los capítulos sobre estrategia de canales). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **conversión posterior al clic** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **métrica de diagnóstico** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «documentar la relación entre ambas para el canal», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Estas métricas dependen de definiciones de la plataforma que cambian y que no siempre coinciden entre proveedores. Comparar el costo por mil de dos plataformas distintas puede ser comparar unidades diferentes. Las comparaciones entre canales deben hacerse en el resultado final y declarando las diferencias de medición.

**Frontera declarada.** Las métricas intermedias no son comparables entre plataformas ni entre formatos. Compararlas directamente induce conclusiones falsas. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Atribuirse demanda existente, inflar el retorno y decidir presupuesto sobre una ilusión.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar CTR, CPC y CPM no consiste en sumar definiciones. Empieza por **costo por mil impresiones**, contrasta **tasa de clic** con **costo por clic**, incorpora **métrica de diagnóstico** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Avinash Kaushik — *Web Analytics 2.0* (2009) | La distinción entre métricas de vanidad y métricas accionables | Los capítulos sobre selección de métricas | ¿Qué debería observarse en **costo por mil impresiones** si aquí opera «la distinción entre métricas de vanidad y métricas accionables»? ¿Y qué observación lo desmentiría en este caso? |
| Brad Geddes — *Advanced Google AdWords* (2014, 3.ª ed.) | La mecánica de la subasta: no gana quien más paga sino quien combina oferta y relevancia | Los capítulos sobre funcionamiento de la subasta | ¿Qué debería observarse en **tasa de clic** si aquí opera «la mecánica de la subasta: no gana quien más paga sino quien combina oferta y relevancia»? ¿Y qué observación lo desmentiría en este caso? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | La métrica que importa ahora: una sola, según etapa y modelo de negocio | Los capítulos sobre la métrica única | ¿Qué debería observarse en **costo por clic** si aquí opera «la métrica que importa ahora: una sola, según etapa y modelo de negocio»? ¿Y qué observación lo desmentiría en este caso? |
| Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) | El modelo de contribución de canal a la conversión | Los capítulos sobre estrategia de canales | ¿Qué debería observarse en **métrica de diagnóstico** si aquí opera «el modelo de contribución de canal a la conversión»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Una campaña de Ruta Andina tiene 6,2 % de tasa de clic —el triple del promedio— y cero oportunidades. El anuncio prometía una funcionalidad gratuita que no existe.

**Paso 1 — Establecer líneas base de las métricas intermedias.** El equipo escribe primero el supuesto asociado a **costo por mil impresiones** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **tasa de clic por variante** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Usarlas para diagnosticar dónde está el problema.** El trabajo aquí es separar lo observado de lo inferido sobre **tasa de clic**. La evidencia que ordena la discusión es **costo por clic por audiencia**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Verificar la calidad del tráfico que producen.** El riesgo de este paso es cerrar demasiado rápido alrededor de **costo por clic**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **conversión posterior al clic** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Decidir con métricas de negocio.** Con **métrica de diagnóstico** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **tasa de clic por variante** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Documentar la relación entre ambas para el canal.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **costo por mil impresiones**. **costo por clic por audiencia** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **costo por mil impresiones** | Precio de alcanzar mil impresiones en la audiencia seleccionada | Cuando **tasa de clic por variante** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **tasa de clic** | Clics obtenidos sobre impresiones entregadas | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Las métricas intermedias no son comparables entre plataformas ni entre formatos. Compararlas directamente induce conclusiones falsas.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre CTR, CPC y CPM |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Performance marketer, Media buyer y Growth marketer. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Una campaña de Ruta Andina tiene 6,2 % de tasa de clic —el triple del promedio— y cero oportunidades. El anuncio prometía una funcionalidad gratuita que no existe.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **establecer líneas base de las métricas intermedias → usarlas para diagnosticar dónde está el problema → verificar la calidad del tráfico que producen → decidir con métricas de negocio → documentar la relación entre ambas para el canal** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **tasa de clic por variante**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *Web Analytics 2.0* y la de *Advanced Google AdWords*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **costo por mil impresiones** y **tasa de clic** como sinónimos | Se perdió la distinción entre «precio de alcanzar mil impresiones en la audiencia seleccionada» y «clics obtenidos sobre impresiones entregadas» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «documentar la relación entre ambas para el canal» | Se saltó «establecer líneas base de las métricas intermedias»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **tasa de clic por variante** | La métrica local reemplazó al resultado del sistema | Contrástala con **conversión posterior al clic** y explicita el costo de oportunidad. |
| Optimizar por tasa de clic | Error específico de esta clase | Usa las métricas intermedias para diagnosticar y decide con costo por oportunidad calificada. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **costo por mil impresiones** y **tasa de clic** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **costo por clic** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «establecer líneas base de las métricas intermedias» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **tasa de clic por variante** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Las métricas intermedias no son comparables entre plataformas ni entre formatos. Compararlas directamente induce conclusiones falsas»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **costo por clic** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **tasa de clic por variante**. |
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

Guarda en `evidence/P14-C09-ctr-cpc-y-cpm/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **tasa de clic por variante**, **costo por clic por audiencia** y **conversión posterior al clic** con fuente, ventana y lectura prohibida.
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

- Avinash Kaushik — *Web Analytics 2.0* (2009) — **aporta a esta clase:** la distinción entre métricas de vanidad y métricas accionables. **Dónde buscarlo:** los capítulos sobre selección de métricas. Registra edición y páginas consultadas en tu nota de lectura.
- Brad Geddes — *Advanced Google AdWords* (2014, 3.ª ed.) — **aporta a esta clase:** la mecánica de la subasta: no gana quien más paga sino quien combina oferta y relevancia. **Dónde buscarlo:** los capítulos sobre funcionamiento de la subasta. Registra edición y páginas consultadas en tu nota de lectura.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — **aporta a esta clase:** la métrica que importa ahora: una sola, según etapa y modelo de negocio. **Dónde buscarlo:** los capítulos sobre la métrica única. Registra edición y páginas consultadas en tu nota de lectura.
- Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) — **aporta a esta clase:** el modelo de contribución de canal a la conversión. **Dónde buscarlo:** los capítulos sobre estrategia de canales. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 08 · Presupuesto y ritmo de gasto](class-08-presupuesto-y-pacing.md) · [Índice de la parte](README.md) · [Clase 10 · CPA, CAC y ROAS](class-10-cpa-cac-y-roas.md) →
