---
title: "Cuotas y territorios"
type: class
language: es
standard: clase-profunda-v2
part: 16
class: 08
level: Operación de ingresos
mastery_threshold: 80
estimated_minutes: 150
sources: ["zoltners", "roberge", "grove", "collins"]
anchors: {"collins": "personas-primero", "grove": "output-gerencial", "roberge": "contratacion-datos", "zoltners": "cuotas"}
updated: 2026-08-19
---

# Clase 16.08 — Cuotas y territorios

**Parte 16 · CRM, pipeline y sales operations** · Nivel: Operación de ingresos · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v2`

## 🚦 Antes de empezar

| Requisito | Detalle |
|---|---|
| **Qué debes traer resuelto** | La clase 16.07 — *Forecast*, cuyo entregable se reutiliza aquí. |
| **Con qué datos trabajarás** | Los del caso de la clase; si usas datos propios, necesitas al menos una serie histórica de proporción del equipo que alcanza la cuota para calcular la línea base. |
| **Materiales** | Una planilla o cuaderno para la ficha de medición, y las obras de la lectura comparada (basta el índice y los capítulos indicados). |
| **Tiempo mínimo real** | 150 minutos de trabajo dirigido más 60 de lectura selectiva. |
| **Cómo sabrás que terminaste** | Existe el entregable de la clase y respondes las seis preguntas de comprobación sin volver al texto. |

**Cómo trabajar esta clase.** Lee el propósito y la agenda antes que el desarrollo: la agenda indica qué producir en cada tramo, y el desarrollo se entiende mejor cuando ya sabes qué artefacto tiene que salir de él. No avances de sección sin escribir algo; este material está diseñado para producir decisiones documentadas, no notas de lectura.

**La idea que ordena la sesión.** El diseño de cuotas alcanzables derivadas del potencial y no del deseo — Andris A. Zoltners, Prabhakant Sinha y Sally E. Lorimer. Todo lo demás en esta clase existe para poner esa idea a prueba contra un caso concreto.

## 🎯 Propósito

Una cuota mal calibrada produce comportamiento perverso: si es inalcanzable, el equipo desiste; si es demasiado baja, se deja negocio sobre la mesa. Los territorios mal repartidos generan desigualdad de oportunidad que ninguna habilidad compensa. Zoltners documenta que el diseño de cuotas y territorios explica una parte importante de la varianza de desempeño que suele atribuirse a las personas.

El punto de partida de esta clase no es la definición sino la decisión que la definición debe mejorar. La parte 16 busca **convertir el CRM en un sistema de trabajo y de verdad operacional**; en esta clase esa progresión se concreta exigiendo que toda afirmación sobre **cuotas y territorios** termine en una definición operacional, una señal observable, una decisión y una condición de revisión.

> **Pregunta rectora de la parte:** ¿El pipeline describe la realidad o solo el optimismo del equipo?

Los conceptos que estructuran la sesión son **cuota**, **territorio**, **equidad de oportunidad** y **alcanzabilidad**. No se estudian como lista de vocabulario: cada uno debe producir una predicción distinta sobre lo que ocurriría en la operación.

## 📚 Resultados de aprendizaje

Al terminar esta clase serás capaz de:

1. **Distinguir** `cuota`, `territorio`, `equidad de oportunidad` y `alcanzabilidad` por sus observables y no por su definición memorizada.
2. **Explicar** por qué esas distinciones cambian una decisión concreta dentro de **CRM, pipeline y sales operations**.
3. **Aplicar** la secuencia **estimar el potencial por territorio con datos → distribuir territorios buscando equidad de potencial → derivar la cuota del potencial y no del deseo → verificar la alcanzabilidad histórica → revisar la asignación cada año con datos de resultado** conservando supuestos, alternativas descartadas y trazabilidad.
4. **Operacionalizar** **proporción del equipo que alcanza la cuota**, **dispersión de potencial entre territorios** y **rotación por territorio** indicando numerador, denominador, ventana, fuente y uso permitido.
5. **Resolver** el caso con al menos dos opciones defendibles y un criterio explícito de detención.
6. **Contrastar** dos obras de la lectura comparada y señalar dónde entregan recomendaciones distintas.

## 🧭 Agenda sugerida (150 minutos)

| Tramo | Foco | Evidencia de avance |
|---|---|---|
| 0–15 min | Recuperación | Define **cuota** y **territorio** sin mirar el material; corrige después con la tabla de conceptos. |
| 15–45 min | Núcleo conceptual | Lectura del desarrollo y construcción de la tabla `hecho / inferencia / supuesto`. |
| 45–75 min | Medición | Ficha de la señal **proporción del equipo que alcanza la cuota**: fórmula, fuente, ventana y lectura prohibida. |
| 75–110 min | Ejemplo trabajado | Recorrido de los 5 pasos del método sobre el caso de la clase. |
| 110–140 min | Caso ejecutivo | Dos alternativas, trade-offs, recomendación y señal de detención. |
| 140–150 min | Cierre | Entregable, preguntas de comprobación y registro de lo que aún no sabes. |

## 🧩 Conceptos centrales

| Concepto | Definición operacional | Cómo demostrar que lo entendiste |
|---|---|---|
| **cuota** | meta individual de resultado asignada para un periodo | Construye un caso límite donde el concepto se confunde con el anterior. |
| **territorio** | conjunto de cuentas o zona asignada a un vendedor | Indica qué dato tendrías que ver para afirmarlo en una reunión de comité. |
| **equidad de oportunidad** | grado en que los territorios ofrecen potencial comparable | Traduce el concepto en una pregunta que puedas hacerle a un cliente real. |
| **alcanzabilidad** | proporción del equipo que puede alcanzar la cuota con desempeño normal | Da un hecho compatible con la definición y otro que la refute. |

Una definición que no produce predicciones observables sigue siendo demasiado vaga para dirigir. Si dos personas del equipo aplican la misma definición a un caso y clasifican distinto, la definición todavía no es operacional.

## 🧠 Modelo mental

```text
1. estimar el potencial por territorio con datos → 2. distribuir territorios buscando equidad de potencial → 3. derivar la cuota del potencial y no del deseo → 4. verificar la alcanzabilidad histórica → 5. revisar la asignación cada año con datos de resultado
```

La secuencia no es un ritual: cada paso reduce una incertidumbre distinta y produce un artefacto revisable. Saltarse un paso no acelera la decisión, sólo traslada el error a una etapa donde corregirlo cuesta más caro.

**Frontera de aplicación.** La equidad perfecta de territorios no existe. El objetivo es que las diferencias sean conocidas y compensadas explícitamente en la cuota.

## 📖 Desarrollo

### 1. Cuota: mecanismo central

**Cuota** se entiende aquí como **meta individual de resultado asignada para un periodo**.

Las cuotas y los territorios determinan la conducta del equipo comercial más que cualquier discurso de dirección. Una cuota inalcanzable produce desmotivación y rotación; una demasiado baja deja resultado sobre la mesa. El diseño debe partir del potencial real del territorio y no de la necesidad de la empresa.

**De dónde viene esta afirmación.** Andris A. Zoltners, Prabhakant Sinha y Sally E. Lorimer — *The Complete Guide to Sales Force Incentive Compensation* (2006) aporta la idea que sostiene este bloque: el diseño de cuotas alcanzables derivadas del potencial y no del deseo. Búscala en los capítulos sobre diseño de cuotas. Aplicada a esta clase, esa idea predice algo verificable: si es correcta, «proporción del equipo que alcanza la cuota» debería moverse cuando cambie **cuota**, y no debería moverse cuando cambie el resto. Ese es el contraste que tienes que montar antes de recomendar nada.

Relaciona el mecanismo con **territorio**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Territorio: frontera conceptual y error de clasificación

**Definición operacional:** conjunto de cuentas o zona asignada a un vendedor. Su valor está en distinguirlo de **cuota**.

La equidad de oportunidad es la condición para que la comparación entre vendedores signifique algo. Si un territorio tiene el doble de potencial que otro, la diferencia de resultados no informa sobre desempeño. Medir el potencial por territorio, aunque sea de forma aproximada, es lo que permite evaluar con justicia.

**Contraste bibliográfico.** Mark Roberge — *The Sales Acceleration Formula* (2015) aporta aquí una distinción concreta: el perfil de contratación derivado del desempeño observado en la propia empresa (los capítulos sobre la fórmula de contratación). Formula dos mini-casos: uno que satisface la definición de **territorio** y otro que sólo se le parece en la superficie; después decide cuál de los dos describiría esa obra con su propio vocabulario. Si la obra no permite separarlos, la distinción es tuya y tienes que sostenerla con evidencia del caso, no con la cita.

Antes de pasar a «distribuir territorios buscando equidad de potencial», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Equidad de oportunidad: operacionalización y medición

**Equidad de oportunidad** significa **grado en que los territorios ofrecen potencial comparable**.

La alcanzabilidad se verifica con el historial: qué proporción del equipo alcanzó la cuota en los últimos periodos. Cuando esa proporción es muy baja de forma sostenida, el problema es de diseño y no de capacidad. Cuando es muy alta, la cuota dejó de cumplir su función de exigencia.

Ficha de medición obligatoria para **proporción del equipo que alcanza la cuota**: `vendedores que cumplen, sobre vendedores con cuota`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

**Control de lectura.** Andrew S. Grove — *High Output Management* (1983) pone una condición sobre la medición: el output del gerente es el de su organización más el de las unidades que influye (los capítulos sobre el trabajo del gerente). Contrasta tu ficha con ella: si la métrica que acabas de definir cae dentro de lo que esa obra considera un error de medición, corrígela antes de usarla para decidir.

### 4. Alcanzabilidad: trade-offs y efectos de segundo orden

**Definición:** proporción del equipo que puede alcanzar la cuota con desempeño normal.

Cuotas más exigentes empujan el esfuerzo y aumentan el riesgo de conductas indeseadas: descuentos excesivos al cierre del periodo, ventas a clientes que no calificaban, adelanto de negocios. Ese efecto es predecible y debe contrapesarse con indicadores de calidad del negocio vendido.

**Lo que aporta la fuente.** Jim Collins — *Good to Great* (2001) aporta el criterio para pesar el intercambio: primero quién y después qué: las personas correctas antes que la dirección (el capítulo sobre primero quién). Úsalo para construir una matriz `beneficio esperado / costo / reversibilidad / afectado / señal temprana`. La evidencia **rotación por territorio** ayuda a detectar si el intercambio está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **alcanzabilidad** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «revisar la asignación cada año con datos de resultado», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

El diseño de territorios y cuotas afecta a las personas de forma directa y su modificación tiene consecuencias que exceden lo comercial. Los cambios deben comunicarse con anticipación, explicarse con criterios y, cuando reducen el potencial de alguien, considerarse en el diseño de la transición.

**Frontera declarada.** La equidad perfecta de territorios no existe. El objetivo es que las diferencias sean conocidas y compensadas explícitamente en la cuota. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Tomar decisiones de contratación y presupuesto sobre un pipeline que no representa la realidad.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar cuotas y territorios no consiste en sumar definiciones. Empieza por **cuota**, contrasta **territorio** con **equidad de oportunidad**, incorpora **alcanzabilidad** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. El resultado no es una opinión mejor redactada: es una decisión con dueño, fecha y condición de revisión.

## 📚 Lectura comparada

No se pide leer las obras completas. Para cada una se indica **qué idea concreta** sostiene esta clase, **dónde buscarla** y **qué pregunta** esa idea le hace a tu propio diagnóstico. La lectura termina cuando puedes responder esa pregunta con evidencia del caso.

| Obra | Idea que sostiene esta clase | Dónde buscarla | Pregunta que le hace a tu diagnóstico |
|---|---|---|---|
| Andris A. Zoltners, Prabhakant Sinha y Sally E. Lorimer — *The Complete Guide to Sales Force Incentive Compensation* (2006) | El diseño de cuotas alcanzables derivadas del potencial y no del deseo | Los capítulos sobre diseño de cuotas | ¿Qué debería observarse en **cuota** si aquí opera «el diseño de cuotas alcanzables derivadas del potencial y no del deseo»? ¿Y qué observación lo desmentiría en este caso? |
| Mark Roberge — *The Sales Acceleration Formula* (2015) | El perfil de contratación derivado del desempeño observado en la propia empresa | Los capítulos sobre la fórmula de contratación | ¿Qué debería observarse en **territorio** si aquí opera «el perfil de contratación derivado del desempeño observado en la propia empresa»? ¿Y qué observación lo desmentiría en este caso? |
| Andrew S. Grove — *High Output Management* (1983) | El output del gerente es el de su organización más el de las unidades que influye | Los capítulos sobre el trabajo del gerente | ¿Qué debería observarse en **equidad de oportunidad** si aquí opera «el output del gerente es el de su organización más el de las unidades que influye»? ¿Y qué observación lo desmentiría en este caso? |
| Jim Collins — *Good to Great* (2001) | Primero quién y después qué: las personas correctas antes que la dirección | El capítulo sobre primero quién | ¿Qué debería observarse en **alcanzabilidad** si aquí opera «primero quién y después qué: las personas correctas antes que la dirección»? ¿Y qué observación lo desmentiría en este caso? |

**Después de leer, escribe una discrepancia real.** Al menos dos de estas obras entregan recomendaciones que no coinciden cuando se aplican al mismo caso; identifica cuáles y qué condición del caso decide a favor de una. Si no encuentras la discrepancia, es señal de que leíste buscando confirmación.

La lectura se evalúa por **uso**, no por cantidad de páginas. La nota de lectura debe indicar qué tesis modifica tu diagnóstico, qué evidencia del caso la tensiona y qué decisión concreta cambiarías después del contraste.

## 🧮 Ejemplo trabajado

**Situación.** En Ruta Andina dos vendedores tienen la Región Metropolitana y cuatro se reparten el resto del país. Todos tienen la misma cuota.

**Paso 1 — Estimar el potencial por territorio con datos.** El equipo escribe primero el supuesto asociado a **cuota** y se prohíbe tratarlo como hecho. Contrasta ese supuesto con **proporción del equipo que alcanza la cuota** y anota qué parte del dato todavía no existe. Del paso sale un artefacto revisable y una frase explícita: «cambiaríamos de rumbo si…».

**Paso 2 — Distribuir territorios buscando equidad de potencial.** El trabajo aquí es separar lo observado de lo inferido sobre **territorio**. La evidencia que ordena la discusión es **dispersión de potencial entre territorios**; si su definición no está escrita, escribirla es parte del paso. Nada avanza mientras el equipo no acuerde qué contaría como refutación.

**Paso 3 — Derivar la cuota del potencial y no del deseo.** El riesgo de este paso es cerrar demasiado rápido alrededor de **equidad de oportunidad**. Antes de concluir, el equipo enumera dos explicaciones alternativas del mismo patrón y revisa si **rotación por territorio** logra distinguirlas. Si no lo logra, hace falta otra evidencia y así debe quedar registrado.

**Paso 4 — Verificar la alcanzabilidad histórica.** Con **alcanzabilidad** ya delimitado, la pregunta pasa a ser de consecuencia: qué cambia en la operación, en la caja y en la carga del equipo. **proporción del equipo que alcanza la cuota** entrega la lectura cuantitativa; el juicio sobre el costo de oportunidad sigue siendo humano y debe quedar firmado.

**Paso 5 — Revisar la asignación cada año con datos de resultado.** El cierre exige compromiso: responsable, fecha, umbral de éxito y condición de detención asociados a **cuota**. **dispersión de potencial entre territorios** se convierte en la señal de seguimiento y se acuerda con qué frecuencia se revisa y quién puede declarar el fracaso sin costo político.

**Síntesis.** La recomendación termina con responsable, fecha, evidencia de éxito y señal de detención. Omitir cualquiera de esas cuatro piezas convierte el análisis en opinión difícil de auditar.

## 🔀 Comparación de caminos y límites

| Camino | Qué privilegia | Cuándo elegirlo | Riesgo principal |
|---|---|---|---|
| Actuar sobre **cuota** | Meta individual de resultado asignada para un periodo | Cuando **proporción del equipo que alcanza la cuota** es observable y accionable en el plazo de la decisión. | Sobrerreaccionar a una señal parcial. |
| Actuar sobre **territorio** | Conjunto de cuentas o zona asignada a un vendedor | Cuando la primera explicación no distingue mecanismo ni responsable. | Convertir el concepto en etiqueta y no en intervención. |
| Experimentar antes de decidir | Aprender antes de comprometer recursos mayores | Cuando la decisión es reversible y la incertidumbre es alta. | Experimentar indefinidamente y no decidir. |
| Escalar la decisión | Elevar autoridad, especialidad o control legal | Cuando hay compromisos contractuales, datos personales, regulación o irreversibilidad. | Delegar hacia arriba lo que sí correspondía decidir. |

**Frontera de aplicación.** La equidad perfecta de territorios no existe. El objetivo es que las diferencias sean conocidas y compensadas explícitamente en la cuota.

## 🪜 El mismo tema según el rol

| Nivel | Responsabilidad sobre cuotas y territorios |
|---|---|
| **Analista / especialista** | Produce la evidencia, documenta el método y declara los límites del dato. |
| **Jefatura de equipo** | Convierte el análisis en prioridad, carga de trabajo y criterio compartido. |
| **Gerencia comercial** | Conecta la decisión con presupuesto, capacidad, dependencias y riesgo interáreas; es el nivel donde operan perfiles como Sales operations, RevOps analyst y Jefe de ventas. |
| **Dirección comercial (CRO/CMO)** | Decide si esto cambia la estrategia de ingresos y qué llega al directorio. |
| **Founder / dueño** | Pregunta si la solución reduce dependencia de personas, preserva caja y puede operar como sistema repetible. |

Al subir de nivel aumentan las personas, el dinero y las consecuencias que quedan dentro de la decisión. La misma herramienta debe volverse más explícita en evidencia, gobierno y revisión a medida que crece el alcance.

## 🏢 Caso ejecutivo

En Ruta Andina dos vendedores tienen la Región Metropolitana y cuatro se reparten el resto del país. Todos tienen la misma cuota.

Entrega un **decision brief** que contenga: (a) hechos y fuentes; (b) hipótesis; (c) dos opciones realmente defendibles; (d) efecto sobre cliente, operación, caja y riesgo; (e) recomendación; (f) la condición que la haría cambiar; (g) responsable y fecha de revisión. Usa al menos **dos** fuentes de la lectura comparada para desafiar tu primera respuesta.

## 🧪 Práctica guiada

Cada paso indica qué hacer, con qué material y cómo saber que está terminado. No avances si la última columna todavía no se cumple: los pasos siguientes suponen el anterior resuelto.

| # | Paso | Qué haces | Con qué | Criterio de término |
|---:|---|---|---|---|
| 1 | **Reconstruir los hechos** | Vuelca el caso en una tabla `hecho / inferencia / supuesto / decisión` sin agregar información que no esté en el enunciado. | El caso y nada más | Ninguna fila de la columna «hecho» contiene un juicio; cada supuesto tiene un responsable de verificarlo. |
| 2 | **Ejecutar el método** | Recorre la secuencia **estimar el potencial por territorio con datos → distribuir territorios buscando equidad de potencial → derivar la cuota del potencial y no del deseo → verificar la alcanzabilidad histórica → revisar la asignación cada año con datos de resultado** y adjunta la evidencia usada en cada transición. | La tabla del paso 1 | Cada paso deja un artefacto revisable y una alternativa descartada con su razón. |
| 3 | **Operacionalizar la señal** | Construye la ficha de medición de **proporción del equipo que alcanza la cuota**; si el dato no existe, diseña cómo obtenerlo y estima cuánto costaría. | Fuentes de datos reales o el diseño de captura | Dos personas del equipo calculan el mismo número con la ficha y llegan al mismo resultado. |
| 4 | **Atacar tu propia respuesta** | Escribe la alternativa que contradice tu preferencia inicial y hazle un *pre-mortem* a seis meses. | Tu borrador de recomendación | Puedes nombrar el dato concreto que te haría cambiar de opinión. |
| 5 | **Contrastar con la fuente** | Lee la idea anclada de *The Complete Guide to Sales Force Incentive Compensation* y la de *The Sales Acceleration Formula*, y registra una coincidencia y una tensión con tu diagnóstico. | La tabla de lectura comparada | La nota de lectura cita qué idea usaste y qué decisión cambió por ella, o declara que ninguna cambió y por qué. |
| 6 | **Subir de nivel** | Rehaz la decisión desde la dirección comercial: qué cambia al aumentar alcance, dinero e irreversibilidad. | El brief completo | El brief indica qué parte de la decisión ya no corresponde al analista y a quién pasa. |

**Si te atascas.** El bloqueo más común no es de método sino de definición: vuelve a la tabla de conceptos y comprueba que puedes clasificar un caso límite sin dudar. Si dudas, el problema está ahí y no en el paso que estabas ejecutando.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Usar **cuota** y **territorio** como sinónimos | Se perdió la distinción entre «meta individual de resultado asignada para un periodo» y «conjunto de cuentas o zona asignada a un vendedor» | Vuelve a los observables y exige una señal distinta para cada concepto. |
| Empezar por «revisar la asignación cada año con datos de resultado» | Se saltó «estimar el potencial por territorio con datos»: la solución llegó antes que el diagnóstico | Reconstruye la cadena completa y marca el primer supuesto no demostrado. |
| Optimizar sólo **proporción del equipo que alcanza la cuota** | La métrica local reemplazó al resultado del sistema | Contrástala con **rotación por territorio** y explicita el costo de oportunidad. |
| Asignar la misma cuota a territorios de potencial distinto | Error específico de esta clase | Estima el potencial por territorio y ajusta la cuota proporcionalmente. |
| No fijar revisión | La decisión se vuelve permanente por inercia | Define responsable, fecha, señal de éxito y condición de detención. |

## ❓ Preguntas de comprobación

1. Explica la diferencia entre **cuota** y **territorio** con un ejemplo donde elegir mal cambie la decisión.
2. ¿Qué observarías para validar **equidad de oportunidad** y qué observación te obligaría a rechazar tu interpretación?
3. Aplica «estimar el potencial por territorio con datos» al caso de la clase. ¿Qué dato sigue faltando?
4. ¿Por qué **proporción del equipo que alcanza la cuota** no basta por sí sola para atribuir causalidad?
5. Compara dos fuentes de la lectura comparada: ¿dónde llevarían a recomendaciones distintas?
6. ¿Qué decisión equivocada se produciría si se ignora este límite: «La equidad perfecta de territorios no existe. El objetivo es que las diferencias sean conocidas y compensadas explícitamente en la cuota»?

## 🗝️ Respuestas orientadoras

No encontrarás aquí las respuestas: encontrarás **qué tiene que contener** una respuesta suficiente. Úsalo para autoevaluarte antes de entregar y para corregir a un par.

| Pregunta | Una respuesta suficiente contiene |
|:--:|---|
| 1 | Nombra un caso real donde la clasificación cambie la intervención, no sólo la etiqueta. Si el ejemplo funciona igual con los dos conceptos intercambiados, la distinción todavía no está entendida. |
| 2 | Dos observaciones concretas: una que confirmaría **equidad de oportunidad** y otra que te obligaría a abandonarlo. Una respuesta sin condición de refutación no es suficiente. |
| 3 | El dato faltante debe ser nombrable y obtenible: qué se mide, quién lo tiene y en cuánto tiempo. «Faltan datos» no cuenta como respuesta. |
| 4 | Debes distinguir asociación de causa y proponer al menos una explicación alternativa del mismo movimiento de **proporción del equipo que alcanza la cuota**. |
| 5 | Identifica la condición del caso que decide entre ambas obras. Basta con que sea una: la respuesta correcta no es «depende», sino «depende de esto, y aquí ocurre así». Ancla el contraste en *The Complete Guide to Sales Force Incentive Compensation* y *Good to Great*. |
| 6 | Describe la decisión equivocada concreta —qué se haría de más o de menos— y quién pagaría el costo. Un límite que no produce una decisión distinta no está operando como límite. |

Si tres o más respuestas no alcanzan el criterio, no sigas a la clase siguiente: repite el desarrollo con el caso en la mano. Avanzar con la definición floja es lo que produce, más adelante, decisiones que nadie puede auditar.

## 🇨🇱 Contexto chileno y cumplimiento

Riesgo asociado a esta parte: **Tomar decisiones de contratación y presupuesto sobre un pipeline que no representa la realidad.** Antes de ejecutar cualquier recomendación de esta clase en una operación real, revisa el mapa regulatorio del repositorio y valida la norma en su fuente primaria vigente.

- Consumo y comercio: `docs/MAPA-REGULATORIO-CHILE.md` (Ley 19.496 y reglamento de comercio electrónico).
- Datos personales: `docs/DATOS-PERSONALES-Y-ETICA.md` (Ley 21.719 y régimen vigente).
- Fuentes oficiales con fecha de consulta: `docs/FUENTES-OFICIALES.md`.

La regla del programa es simple: **la fuente oficial manda sobre el material pedagógico**. Si la norma cambió después de la fecha de esta clase, gana la norma.

## 📥 Entregable

Guarda en `evidence/P16-C08-cuotas-y-territorios/`:

- `decision-brief.md` — problema, evidencia, alternativas, recomendación y gobierno.
- `ficha-metricas.md` — definición operacional de **proporción del equipo que alcanza la cuota**, **dispersión de potencial entre territorios** y **rotación por territorio** con fuente, ventana y lectura prohibida.
- `nota-de-lectura.md` — dos fuentes contrastadas con edición y páginas consultadas.
- `red-team.md` — la objeción más fuerte a tu recomendación y el dato que la invalidaría.

Este entregable alimenta el artefacto de la parte: **diseño de sales operations con pipeline, criterios de etapa, forecast y gobierno de datos**.

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

- Andris A. Zoltners, Prabhakant Sinha y Sally E. Lorimer — *The Complete Guide to Sales Force Incentive Compensation* (2006) — **aporta a esta clase:** el diseño de cuotas alcanzables derivadas del potencial y no del deseo. **Dónde buscarlo:** los capítulos sobre diseño de cuotas. Registra edición y páginas consultadas en tu nota de lectura.
- Mark Roberge — *The Sales Acceleration Formula* (2015) — **aporta a esta clase:** el perfil de contratación derivado del desempeño observado en la propia empresa. **Dónde buscarlo:** los capítulos sobre la fórmula de contratación. Registra edición y páginas consultadas en tu nota de lectura.
- Andrew S. Grove — *High Output Management* (1983) — **aporta a esta clase:** el output del gerente es el de su organización más el de las unidades que influye. **Dónde buscarlo:** los capítulos sobre el trabajo del gerente. Registra edición y páginas consultadas en tu nota de lectura.
- Jim Collins — *Good to Great* (2001) — **aporta a esta clase:** primero quién y después qué: las personas correctas antes que la dirección. **Dónde buscarlo:** el capítulo sobre primero quién. Registra edición y páginas consultadas en tu nota de lectura.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

> **Dónde encontrar estas obras.** Cada una tiene su localizador —ISBN-13, DOI o dirección de la fuente primaria— en el [registro de fuentes](../../sources/bibliography.json). No busques la edición por el título: distintas ediciones cambian capítulos y ejemplos, y el anclaje de arriba está hecho sobre la que declara el registro.

---

← [Clase 07 · Forecast](class-07-forecast.md) · [Índice de la parte](README.md) · [Clase 09 · Capacidad comercial](class-09-sales-capacity.md) →
