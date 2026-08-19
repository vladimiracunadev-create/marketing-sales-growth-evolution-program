---
title: "Inteligencia de conversaciones"
type: class
language: es
standard: clase-profunda-v2
part: 21
class: 10
level: IA y expansión
mastery_threshold: 80
estimated_minutes: 150
sources: ["nist-airmf", "provost", "rackham", "roberge"]
anchors: {"nist-airmf": "contexto", "provost": "asociacion-causalidad", "rackham": "implicacion", "roberge": "metricas-coaching"}
updated: 2026-08-19
---

# Clase 21.10 — Inteligencia de conversaciones

**Parte 21 · IA aplicada a marketing, ventas y servicio** · Nivel: IA y expansión · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 21.09 — *Agentes comerciales automatizados*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de cobertura de consentimiento para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El riesgo evaluado en el contexto de uso y no en abstracto — NIST. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

El análisis automatizado de llamadas y reuniones produce información valiosa: qué objeciones aparecen, cuánto habla el vendedor, qué temas correlacionan con el cierre. Su condición previa es legal y ética: grabar conversaciones requiere informar y, según el caso, obtener consentimiento. Usarlo para vigilancia individual en lugar de mejora del proceso destruye la confianza del equipo.

Antes de cualquier herramienta, esta clase obliga a nombrar qué cambiaría si el análisis fuese correcto. La parte 21 busca **usar IA como capacidad operativa con evaluación, control y responsabilidad humana**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **inteligencia de conversaciones** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿Qué tarea mejora con IA, cómo sé que mejora y quién responde cuando falla?

Los conceptos que estructuran la sesión son **consentimiento de grabación**, **análisis agregado**, **patrón asociado al resultado** y **uso para desarrollo**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `consentimiento de grabación`, `análisis agregado`, `patrón asociado al resultado` y `uso para desarrollo` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **IA aplicada a marketing, ventas y servicio**.
3. **Aplicar** la secuencia **verificar el marco legal y obtener consentimiento → definir qué se analizará y para qué → priorizar el análisis agregado sobre el individual → usar los hallazgos para formación y no para sanción → revisar el efecto sobre el desempeño del equipo** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **cobertura de consentimiento**, **patrones identificados** y **uso en formación** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **consentimiento de grabación** y **análisis agregado** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **cobertura de consentimiento**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **consentimiento de grabación** | autorización informada de los participantes para registrar la conversación | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **análisis agregado** | estudio de patrones del conjunto en lugar de vigilancia individual | Da un hecho compatible con la definición y otro que la refute. |
| **patrón asociado al resultado** | comportamiento conversacional que correlaciona con el cierre | Explica qué decisión cambiaría si el concepto estuviera ausente. |
| **uso para desarrollo** | aplicación orientada a mejorar la habilidad y no a sancionar | Construye un caso límite donde el concepto se confunde con el anterior. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. verificar el marco legal y obtener consentimiento → 2. definir qué se analizará y para qué → 3. priorizar el análisis agregado sobre el individual → 4. usar los hallazgos para formación y no para sanción → 5. revisar el efecto sobre el desempeño del equipo
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** El análisis conversacional identifica correlaciones, no causas. Imponer un patrón conversacional sin entender su mecanismo puede empeorar el resultado.

## 📖 Desarrollo

### 1. Consentimiento de grabación: mecanismo central

**Consentimiento de grabación** se entiende aquí como **autorización informada de los participantes para registrar la conversación**.

El análisis de conversaciones comerciales permite identificar patrones que ningún acompañamiento manual detectaría: qué preguntas se asocian con avance, cuánto habla cada parte, qué objeciones aparecen. Su valor es agregado y de mejora de proceso; usarlo para evaluar individualmente cambia su naturaleza y su aceptación.

**De dónde viene esta afirmación.** NIST — *AI Risk Management Framework 1.0* (2023) aporta la idea que sostiene este bloque: el riesgo evaluado en el contexto de uso y no en abstracto. Búscala en la sección sobre mapeo del contexto. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «cobertura de consentimiento» debería moverse cuando cambie **consentimiento de grabación**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **análisis agregado**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Análisis agregado: frontera conceptual y error de clasificación

**Definición operacional:** estudio de patrones del conjunto en lugar de vigilancia individual. Su valor está en distinguirlo de **consentimiento de grabación**.

El consentimiento de grabación es previo y no negociable: todas las partes deben conocer que la conversación se registra y para qué se usará. En Chile hay obligaciones específicas al respecto que deben verificarse en su fuente vigente. Un análisis construido sobre grabaciones sin consentimiento es inutilizable además de riesgoso.

**Contraste bibliográfico.** Foster Provost y Tom Fawcett — *Data Science for Business* (2013) aporta aquí una distinción concreta: la distinción entre correlación observada y causalidad y qué exige cada una (los capítulos sobre inferencia y sesgo). Formula dos mini-casos: uno que satisface la definición de **análisis agregado** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «definir qué se analizará y para qué», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Patrón asociado al resultado: operacionalización y medición

**Patrón asociado al resultado** significa **comportamiento conversacional que correlaciona con el cierre**.

El patrón asociado al resultado es una correlación y no una receta. Que las llamadas exitosas tengan cierta proporción de habla no significa que forzar esa proporción produzca éxito. Confundir asociación con causa lleva a entrenar al equipo en conductas superficiales que imitan el síntoma y no la causa.

Ficha de medición obligatoria para **cobertura de consentimiento**: `conversaciones grabadas con consentimiento registrado, sobre grabaciones`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Neil Rackham — *SPIN Selling* (1988) pone una condición sobre la medición: las preguntas de implicación como el predictor más fuerte de éxito en ventas grandes (los capítulos sobre la secuencia SPIN). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Uso para desarrollo: trade-offs y efectos de segundo orden

**Definición:** aplicación orientada a mejorar la habilidad y no a sancionar.

Analizar más conversaciones entrega mejores patrones y aumenta la sensación de vigilancia, que puede alterar la conducta que se pretende medir. Declarar explícitamente el uso agregado y respetarlo es lo que permite que el equipo colabore en lugar de adaptarse a la medición.

**Lo que aporta la fuente.** Mark Roberge — *The Sales Acceleration Formula* (2015) aporta el criterio para pesar el intercambio: el acompañamiento dirigido por una métrica diagnóstica por vendedor (los capítulos sobre la fórmula de gestión). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **uso en formación** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **uso para desarrollo** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar el efecto sobre el desempeño del equipo», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El uso para desarrollo y el uso para evaluación deben separarse y declararse. Un sistema presentado como herramienta de mejora que después alimenta la evaluación de desempeño destruye la confianza de forma permanente. Esa decisión debe tomarse y comunicarse al inicio, no cuando resulte conveniente.

**Frontera declarada.** El análisis conversacional identifica correlaciones, no causas. Imponer un patrón conversacional sin entender su mecanismo puede empeorar el resultado. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar inteligencia de conversaciones no consiste en sumar definiciones. Empieza por **consentimiento de grabación**, contrasta **análisis agregado** con **patrón asociado al resultado**, incorpora **uso para desarrollo** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. La prueba de dominio es poder explicar el caso contrario: cuándo esta recomendación sería incorrecta.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| NIST — *AI Risk Management Framework 1.0* (2023) | El riesgo evaluado en el contexto de uso y no en abstracto | La sección sobre mapeo del contexto | ¿Qué debería observarse en **consentimiento de grabación** si aquí opera «el riesgo evaluado en el contexto de uso y no en abstracto»? ¿Y qué observación lo desmentiría en este caso? |
| Foster Provost y Tom Fawcett — *Data Science for Business* (2013) | La distinción entre correlación observada y causalidad y qué exige cada una | Los capítulos sobre inferencia y sesgo | ¿Qué debería observarse en **análisis agregado** si aquí opera «la distinción entre correlación observada y causalidad y qué exige cada una»? ¿Y qué observación lo desmentiría en este caso? |
| Neil Rackham — *SPIN Selling* (1988) | Las preguntas de implicación como el predictor más fuerte de éxito en ventas grandes | Los capítulos sobre la secuencia SPIN | ¿Qué debería observarse en **patrón asociado al resultado** si aquí opera «las preguntas de implicación como el predictor más fuerte de éxito en ventas grandes»? ¿Y qué observación lo desmentiría en este caso? |
| Mark Roberge — *The Sales Acceleration Formula* (2015) | El acompañamiento dirigido por una métrica diagnóstica por vendedor | Los capítulos sobre la fórmula de gestión | ¿Qué debería observarse en **uso para desarrollo** si aquí opera «el acompañamiento dirigido por una métrica diagnóstica por vendedor»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Ruta Andina activó grabación automática de llamadas sin informar a los clientes ni al equipo, y la jefatura empezó a usar los resúmenes en evaluaciones individuales.

**Paso 1 — Verificar el marco legal y obtener consentimiento.** El equipo escribe primero el supuesto asociado a **consentimiento de grabación** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **cobertura de consentimiento** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Definir qué se analizará y para qué.** El trabajo aquí es separar lo observado de lo inferido sobre **análisis agregado**. La evidencia que ordena la discusión es **patrones identificados**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Priorizar el análisis agregado sobre el individual.** El riesgo de este paso es cerrar demasiado rápido alrededor de **patrón asociado al resultado**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **uso en formación** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Usar los hallazgos para formación y no para sanción.** Con **uso para desarrollo** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **cobertura de consentimiento** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar el efecto sobre el desempeño del equipo.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **consentimiento de grabación**. **patrones identificados** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **consentimiento de grabación** | Autorización informada de los participantes para registrar la conversación | Cuando **cobertura de consentimiento** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **análisis agregado** | Estudio de patrones del conjunto en lugar de vigilancia individual | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** El análisis conversacional identifica correlaciones, no causas. Imponer un patrón conversacional sin entender su mecanismo puede empeorar el resultado.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre inteligencia de conversaciones |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Growth manager con IA, RevOps, Marketing manager y Sales enablement. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Ruta Andina activó grabación automática de llamadas sin informar a los clientes ni al equipo, y la jefatura empezó a usar los resúmenes en evaluaciones individuales.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **verificar el marco legal y obtener consentimiento → definir qué se analizará y para qué → priorizar el análisis agregado sobre el individual → usar los hallazgos para formación y no para sanción → revisar el efecto sobre el desempeño del equipo** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **cobertura de consentimiento**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *AI Risk Management Framework 1.0* y la de *Data Science for Business*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **consentimiento de grabación** y **análisis agregado** como sinónimos | Se perdió la distinción entre «autorización informada de los participantes para registrar la conversación» y «estudio de patrones del conjunto en lugar de vigilancia individual» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar el efecto sobre el desempeño del equipo» | Se saltó «verificar el marco legal y obtener consentimiento»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **cobertura de consentimiento** | La métrica local reemplazó al resultado del sistema | Contrástala con **uso en formación** y explicita el costo de oportunidad. |
| Grabar sin informar ni obtener consentimiento | Error específico de esta clase | Verifica el marco legal, informa a todas las partes y obtén el consentimiento antes de grabar. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **consentimiento de grabación** y **análisis agregado** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **patrón asociado al resultado** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «verificar el marco legal y obtener consentimiento» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **cobertura de consentimiento** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «El análisis conversacional identifica correlaciones, no causas. Imponer un patrón conversacional sin entender su mecanismo puede empeorar el resultado»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **patrón asociado al resultado** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **cobertura de consentimiento**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *AI Risk Management Framework 1.0* y *The Sales Acceleration Formula*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P21-C10-conversation-intelligence/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **cobertura de consentimiento**, **patrones identificados** y **uso en formación** con fuente, ventana y lectura prohibida.
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

- NIST — *AI Risk Management Framework 1.0* (2023) — **aporta a esta clase:** el riesgo evaluado en el contexto de uso y no en abstracto. **Dónde buscarlo:** la sección sobre mapeo del contexto. Registra edición y páginas consultadas en tu nota de lectura.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — **aporta a esta clase:** la distinción entre correlación observada y causalidad y qué exige cada una. **Dónde buscarlo:** los capítulos sobre inferencia y sesgo. Registra edición y páginas consultadas en tu nota de lectura.
- Neil Rackham — *SPIN Selling* (1988) — **aporta a esta clase:** las preguntas de implicación como el predictor más fuerte de éxito en ventas grandes. **Dónde buscarlo:** los capítulos sobre la secuencia SPIN. Registra edición y páginas consultadas en tu nota de lectura.
- Mark Roberge — *The Sales Acceleration Formula* (2015) — **aporta a esta clase:** el acompañamiento dirigido por una métrica diagnóstica por vendedor. **Dónde buscarlo:** los capítulos sobre la fórmula de gestión. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 09 · Agentes comerciales automatizados](class-09-agentes-comerciales.md) · [Índice de la parte](README.md) · [Clase 11 · IA en customer success](class-11-ia-en-customer-success.md) →
