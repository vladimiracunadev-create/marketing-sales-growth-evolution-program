---
title: "Time to value"
type: class
language: es
standard: clase-profunda-v2
part: 18
class: 03
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["hulick", "mehta", "croll-yoskovitz", "cagan"]
anchors: {"cagan": "resultado-output", "croll-yoskovitz": "una-metrica", "hulick": "carga-cognitiva", "mehta": "segmentacion-cs"}
updated: 2026-08-19
---

# Clase 18.03 — Time to value

**Parte 18 · Customer experience, success y fidelización** · Nivel: Operación de ingresos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 18.02 — *Onboarding*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de tiempo hasta el primer valor para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** La reducción de carga cognitiva en los primeros minutos — Samuel Hulick. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

El tiempo hasta el primer valor es el indicador más predictivo de retención en modelos recurrentes. Cada día adicional aumenta la probabilidad de que el cliente pierda impulso, cambie de prioridad o encuentre otra solución. Reducirlo suele exigir decisiones incómodas: eliminar pasos de configuración, ofrecer plantillas por defecto o asumir parte del trabajo inicial.

Antes de cualquier herramienta, esta clase obliga a nombrar qué cambiaría si el análisis fuese correcto. La parte 18 busca **sostener y expandir el ingreso existente con un sistema de valor entregado**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **time to value** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿En qué momento el cliente obtiene valor y qué lo hace quedarse o irse?

Los conceptos que estructuran la sesión son **primer valor**, **tiempo hasta el primer valor**, **bloqueador de implementación** y **valor por defecto**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `primer valor`, `tiempo hasta el primer valor`, `bloqueador de implementación` y `valor por defecto` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **Customer experience, success y fidelización**.
3. **Aplicar** la secuencia **definir el evento que representa el primer valor → medir el tiempo actual por segmento → identificar los bloqueadores más frecuentes → reducir el trabajo inicial exigido al cliente → verificar el efecto sobre retención a 90 días** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **tiempo hasta el primer valor**, **bloqueadores por implementación** y **retención por tiempo hasta el valor** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **primer valor** y **tiempo hasta el primer valor** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **tiempo hasta el primer valor**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **primer valor** | momento en que el cliente obtiene un beneficio verificable del producto | Construye un caso límite donde el concepto se confunde con el anterior. |
| **tiempo hasta el primer valor** | días entre la contratación y ese momento | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **bloqueador de implementación** | obstáculo que retrasa la obtención del primer valor | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **valor por defecto** | configuración inicial que produce beneficio sin trabajo del cliente | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. definir el evento que representa el primer valor → 2. medir el tiempo actual por segmento → 3. identificar los bloqueadores más frecuentes → 4. reducir el trabajo inicial exigido al cliente → 5. verificar el efecto sobre retención a 90 días
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** Acelerar la implementación puede trasladar costo a la empresa. La decisión requiere comparar ese costo contra el valor de la retención adicional.

## 📖 Desarrollo

### 1. Primer valor: mecanismo central

**Primer valor** se entiende aquí como **momento en que el cliente obtiene un beneficio verificable del producto**.

El tiempo hasta el primer valor es la distancia entre la firma y el momento en que el cliente obtiene algo que le sirve. Es la métrica más predictiva de la relación y la que más se confunde con el tiempo de implementación técnica. Un sistema puede estar operativo en una semana y no producir valor hasta el mes tres si nadie cambió el proceso.

**De dónde viene esta afirmación.** Samuel Hulick — *The Elements of User Onboarding* (2014) aporta la idea que sostiene este bloque: la reducción de carga cognitiva en los primeros minutos. Búscala en los capítulos sobre diseño de la primera experiencia. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «tiempo hasta el primer valor» debería moverse cuando cambie **primer valor**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **tiempo hasta el primer valor**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Tiempo hasta el primer valor: frontera conceptual y error de clasificación

**Definición operacional:** días entre la contratación y ese momento. Su valor está en distinguirlo de **primer valor**.

El valor por defecto es una decisión de diseño con efecto directo sobre este indicador: entregar el producto configurado con supuestos razonables permite obtener resultado antes que exigir una configuración completa. Cada decisión que se traslada al cliente al inicio alarga la distancia hasta el valor.

**Contraste bibliográfico.** Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) aporta aquí una distinción concreta: los modelos de cobertura según valor y complejidad de la cuenta (los capítulos sobre modelos de atención). Formula dos mini-casos: uno que satisface la definición de **tiempo hasta el primer valor** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «medir el tiempo actual por segmento», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Bloqueador de implementación: operacionalización y medición

**Bloqueador de implementación** significa **obstáculo que retrasa la obtención del primer valor**.

El bloqueador de implementación debe identificarse y clasificarse: falta de datos, falta de una persona disponible, dependencia de otro sistema, falta de decisión interna. Registrar la causa de cada retraso durante seis meses produce una lista priorizada de qué corregir, y casi siempre revela que el bloqueador principal está del lado del cliente y es previsible.

Ficha de medición obligatoria para **tiempo hasta el primer valor**: `días entre contratación y primer valor, mediana por segmento`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) pone una condición sobre la medición: la métrica que importa ahora: una sola, según etapa y modelo de negocio (los capítulos sobre la métrica única). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Valor por defecto: trade-offs y efectos de segundo orden

**Definición:** configuración inicial que produce beneficio sin trabajo del cliente.

Acelerar el primer valor puede exigir reducir el alcance inicial, lo que el cliente puede percibir como una entrega incompleta. La alternativa —implementar todo antes de mostrar algo— es más riesgosa. Comunicar explícitamente la secuencia por fases, y por qué, resuelve la mayor parte de esa tensión.

**Lo que aporta la fuente.** Marty Cagan — *Inspired* (2017, 2.ª ed.) aporta el criterio para pesar el intercambio: la orientación a resultado en lugar de a entrega de funcionalidades (los capítulos sobre equipos de producto). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **retención por tiempo hasta el valor** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **valor por defecto** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «verificar el efecto sobre retención a 90 días», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El primer valor se define desde el cliente y no desde el proveedor. Lo que la empresa considera un hito puede no serlo para quien lo usa. Verificar esa definición con clientes reales —preguntar cuándo sintieron que valía la pena— es un ejercicio breve que suele corregir el supuesto interno.

**Frontera declarada.** Acelerar la implementación puede trasladar costo a la empresa. La decisión requiere comparar ese costo contra el valor de la retención adicional. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Retener con castigos contractuales en lugar de valor entregado y dañar reputación.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar time to value no consiste en sumar definiciones. Empieza por **primer valor**, contrasta **tiempo hasta el primer valor** con **bloqueador de implementación**, incorpora **valor por defecto** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Samuel Hulick — *The Elements of User Onboarding* (2014) | La reducción de carga cognitiva en los primeros minutos | Los capítulos sobre diseño de la primera experiencia | ¿Qué debería observarse en **primer valor** si aquí opera «la reducción de carga cognitiva en los primeros minutos»? ¿Y qué observación lo desmentiría en este caso? |
| Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) | Los modelos de cobertura según valor y complejidad de la cuenta | Los capítulos sobre modelos de atención | ¿Qué debería observarse en **tiempo hasta el primer valor** si aquí opera «los modelos de cobertura según valor y complejidad de la cuenta»? ¿Y qué observación lo desmentiría en este caso? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | La métrica que importa ahora: una sola, según etapa y modelo de negocio | Los capítulos sobre la métrica única | ¿Qué debería observarse en **bloqueador de implementación** si aquí opera «la métrica que importa ahora: una sola, según etapa y modelo de negocio»? ¿Y qué observación lo desmentiría en este caso? |
| Marty Cagan — *Inspired* (2017, 2.ª ed.) | La orientación a resultado en lugar de a entrega de funcionalidades | Los capítulos sobre equipos de producto | ¿Qué debería observarse en **valor por defecto** si aquí opera «la orientación a resultado en lugar de a entrega de funcionalidades»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** Los clientes de Ruta Andina que activan el módulo de pagos en las dos primeras semanas retienen 3,2 veces más. El proceso actual toma en promedio 34 días.

**Paso 1 — Definir el evento que representa el primer valor.** El equipo escribe primero el supuesto asociado a **primer valor** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **tiempo hasta el primer valor** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Medir el tiempo actual por segmento.** El trabajo aquí es separar lo observado de lo inferido sobre **tiempo hasta el primer valor**. La evidencia que ordena la discusión es **bloqueadores por implementación**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Identificar los bloqueadores más frecuentes.** El riesgo de este paso es cerrar demasiado rápido alrededor de **bloqueador de implementación**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **retención por tiempo hasta el valor** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Reducir el trabajo inicial exigido al cliente.** Con **valor por defecto** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **tiempo hasta el primer valor** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Verificar el efecto sobre retención a 90 días.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **primer valor**. **bloqueadores por implementación** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **primer valor** | Momento en que el cliente obtiene un beneficio verificable del producto | Cuando **tiempo hasta el primer valor** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **tiempo hasta el primer valor** | Días entre la contratación y ese momento | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** Acelerar la implementación puede trasladar costo a la empresa. La decisión requiere comparar ese costo contra el valor de la retención adicional.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre time to value |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Customer success manager, Account manager y Head of CS. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

Los clientes de Ruta Andina que activan el módulo de pagos en las dos primeras semanas retienen 3,2 veces más. El proceso actual toma en promedio 34 días.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **definir el evento que representa el primer valor → medir el tiempo actual por segmento → identificar los bloqueadores más frecuentes → reducir el trabajo inicial exigido al cliente → verificar el efecto sobre retención a 90 días** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **tiempo hasta el primer valor**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *The Elements of User Onboarding* y la de *Customer Success*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **primer valor** y **tiempo hasta el primer valor** como sinónimos | Se perdió la distinción entre «momento en que el cliente obtiene un beneficio verificable del producto» y «días entre la contratación y ese momento» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «verificar el efecto sobre retención a 90 días» | Se saltó «definir el evento que representa el primer valor»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **tiempo hasta el primer valor** | La métrica local reemplazó al resultado del sistema | Contrástala con **retención por tiempo hasta el valor** y explicita el costo de oportunidad. |
| Delegar en el cliente todo el trabajo de configuración | Error específico de esta clase | Ofrece configuraciones por defecto y asume los pasos que bloquean el primer valor. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **primer valor** y **tiempo hasta el primer valor** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **bloqueador de implementación** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «definir el evento que representa el primer valor» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **tiempo hasta el primer valor** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «Acelerar la implementación puede trasladar costo a la empresa. La decisión requiere comparar ese costo contra el valor de la retención adicional»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **bloqueador de implementación** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **tiempo hasta el primer valor**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *The Elements of User Onboarding* y *Inspired*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Retener con castigos contractuales en lugar de valor entregado y dañar reputación.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P18-C03-time-to-value/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **tiempo hasta el primer valor**, **bloqueadores por implementación** y **retención por tiempo hasta el valor** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **sistema de retención y expansión con onboarding, health score, renovación y advocacy**.

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

- Samuel Hulick — *The Elements of User Onboarding* (2014) — **aporta a esta clase:** la reducción de carga cognitiva en los primeros minutos. **Dónde buscarlo:** los capítulos sobre diseño de la primera experiencia. Registra edición y páginas consultadas en tu nota de lectura.
- Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) — **aporta a esta clase:** los modelos de cobertura según valor y complejidad de la cuenta. **Dónde buscarlo:** los capítulos sobre modelos de atención. Registra edición y páginas consultadas en tu nota de lectura.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — **aporta a esta clase:** la métrica que importa ahora: una sola, según etapa y modelo de negocio. **Dónde buscarlo:** los capítulos sobre la métrica única. Registra edición y páginas consultadas en tu nota de lectura.
- Marty Cagan — *Inspired* (2017, 2.ª ed.) — **aporta a esta clase:** la orientación a resultado en lugar de a entrega de funcionalidades. **Dónde buscarlo:** los capítulos sobre equipos de producto. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 02 · Onboarding](class-02-onboarding.md) · [Índice de la parte](README.md) · [Clase 04 · Customer Success](class-04-customer-success.md) →
