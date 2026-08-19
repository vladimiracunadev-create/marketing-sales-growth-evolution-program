---
title: "CTR, CPC y CPM"
type: class
language: es
standard: clase-profunda-v3
part: 14
class: 09
level: Adquisición
mastery_threshold: 80
estimated_minutes: 150
sources: ["kaushik", "geddes", "croll-yoskovitz", "chaffey"]
updated: 2026-08-18
---

# Clase 14.09 — CTR, CPC y CPM

**Parte 14 · Publicidad y performance marketing** · Nivel: Adquisición · Duración sugerida: 150 minutos · Estándar: `clase-profunda-v3`

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

**costo por mil impresiones** se entiende aquí como **precio de alcanzar mil impresiones en la audiencia seleccionada**. Es la pieza desde la que se inicia el análisis de CTR, CPC y CPM: antes de «establecer líneas base de las métricas intermedias», hay que poder señalar qué cambia en la operación si el concepto está presente y qué debería observarse si no lo está.

La lectura rectora de este bloque es Avinash Kaushik — *Web Analytics 2.0* (2009). **Lente que aporta:** medición orientada a decisión, segmentación y crítica del dato de vanidad. Úsala sin convertirla en dogma: escribe una proposición de la obra que apoye tu diagnóstico, una condición del caso que la limite y una consecuencia práctica. La evidencia mínima es **tasa de clic por variante**; regístrala con periodo, unidad, población y línea base.

Relaciona el mecanismo con **tasa de clic**. Si ambos se mueven juntos no concluyas causalidad: nombra una tercera variable capaz de explicar el mismo patrón. El resultado de este bloque debe ser una hipótesis refutable, no una recomendación anticipada.

### 2. Tasa de clic: frontera conceptual y error de clasificación

**Definición operacional:** clics obtenidos sobre impresiones entregadas. Su valor está en distinguirlo de **costo por mil impresiones**. En una decisión real, clasificar mal una situación cambia la intervención: se asigna presupuesto donde faltaba diagnóstico, se mide un resultado cuando había que observar un proceso, o se trata una restricción como si fuera una preferencia.

Contrasta el problema con Brad Geddes — *Advanced Google AdWords* (2014, 3.ª ed.) —**lente:** estructura de cuentas, subastas, calidad y control del gasto en búsqueda pagada—. Formula dos mini-casos: uno que satisface la definición de **tasa de clic** y otro que sólo se le parece en la superficie. Después pregunta qué señal los distingue; **costo por clic por audiencia** es candidata, pero debe combinarse con evidencia cualitativa cuando el fenómeno no es directamente medible.

Antes de pasar a «usarlas para diagnosticar dónde está el problema», registra explícitamente qué decisión sería errónea si esta frontera se ignora. Esa frase convierte el vocabulario en criterio de gestión.

### 3. Costo por clic: operacionalización y medición

**costo por clic** significa **gasto dividido por clics obtenidos**. El problema ya no es definirlo sino medirlo: qué contar, en qué ventana, con qué denominador, contra qué línea base y con qué segmentación. Una métrica útil conserva contexto suficiente para no confundir una mejora local con una mejora del sistema.

Ficha de medición obligatoria para **tasa de clic por variante**: `clics sobre impresiones, por variante creativa y audiencia`. Registra además fuente del dato, frecuencia, responsable, interpretación permitida e interpretación prohibida. Si no existe un dato confiable, la salida correcta no es inventar precisión: es diseñar el mecanismo de captura y declarar la incertidumbre.

Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) orienta este bloque —**lente:** una métrica que importa por etapa y por modelo de negocio—. Pregúntate si el indicador es adelantado o rezagado y si puede ser manipulado por quienes son evaluados con él. La medición debe informar una decisión; en el momento en que reemplaza al fenómeno, deja de servir.

### 4. Métrica de diagnóstico: trade-offs y efectos de segundo orden

**Definición:** indicador que explica el desempeño pero no debe gobernar la decisión. Este concepto obliga a abandonar la idea de que CTR, CPC y CPM tiene una solución gratuita. Toda intervención consume caja, tiempo, atención del equipo, capacidad de la operación, reputación o tolerancia al riesgo. Por eso, antes de «decidir con métricas de negocio», se comparan al menos dos alternativas plausibles y se explicita qué se sacrifica en cada una.

Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) —**lente:** planificación digital integrada: canales, medición y gobierno— sirve para construir una matriz `beneficio esperado / costo / reversibilidad / stakeholder afectado / señal temprana`. La evidencia **conversión posterior al clic** ayuda a detectar si el trade-off está ocurriendo como se esperaba, pero no elimina la obligación de observar efectos laterales fuera del indicador principal.

Haz un *pre-mortem*: supón que la opción recomendada fracasó a los seis meses y enumera tres mecanismos que lo expliquen. Al menos uno debe provenir de un efecto de segundo orden asociado a **métrica de diagnóstico** y otro de un supuesto del caso que nunca fue validado.

### 5. Gobernanza, límites y responsabilidad

La pregunta ejecutiva es siempre la misma: quién decide, quién ejecuta, a quién hay que consultar, qué evidencia queda registrada y qué condición obliga a detener, corregir o escalar. Al ejecutar «documentar la relación entre ambas para el canal», deja una traza que permita a otra persona reconstruir por qué la decisión parecía razonable con la información disponible en ese momento.

Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) sirve para contrastar la recomendación final desde otro lente: planificación digital integrada: canales, medición y gobierno. La frontera de esta clase es explícita: Las métricas intermedias no son comparables entre plataformas ni entre formatos. Compararlas directamente induce conclusiones falsas. Conviértela en una regla operativa con el formato `si ocurre X → no aplicar automáticamente → consultar, escalar o revalidar`.

Esta parte vigila además un riesgo que es obligatorio declarar: **Atribuirse demanda existente, inflar el retorno y decidir presupuesto sobre una ilusión.** Se documenta en el entregable con su mitigación y su responsable; no se resuelve en la conversación.

### 6. Integración: de conceptos a una decisión defendible

Sintetizar CTR, CPC y CPM no consiste en sumar definiciones. Empieza por **costo por mil impresiones**, contrasta **tasa de clic** con **costo por clic**, incorpora **métrica de diagnóstico** como restricción y cierra con la medición. Aplica entonces la secuencia completa conservando tres columnas por paso: evidencia utilizada, alternativa descartada y razón del descarte.

Esa disciplina permite que una revisión posterior distinga una mala decisión de un mal resultado. Sin ella, el equipo reescribe la historia después de conocer el desenlace y no aprende nada transferible. Cuando la integración funciona, cualquier persona del equipo puede reconstruir el razonamiento sin el autor presente.

## 📚 Lectura comparada

Las obras no cumplen el mismo papel. Esta tabla indica qué lente buscar; después de leer, escribe una discrepancia real entre al menos dos fuentes.

| Fuente | Lente que aporta | Pregunta crítica |
|---|---|---|
| Avinash Kaushik — *Web Analytics 2.0* (2009) | medición orientada a decisión, segmentación y crítica del dato de vanidad | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Brad Geddes — *Advanced Google AdWords* (2014, 3.ª ed.) | estructura de cuentas, subastas, calidad y control del gasto en búsqueda pagada | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) | una métrica que importa por etapa y por modelo de negocio | ¿Qué supuesto de esta clase ayuda a desafiar? |
| Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.) | planificación digital integrada: canales, medición y gobierno | ¿Qué supuesto de esta clase ayuda a desafiar? |

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

1. Reconstruye el caso con una tabla `hecho / inferencia / supuesto / decisión`.
2. Ejecuta la secuencia **establecer líneas base de las métricas intermedias → usarlas para diagnosticar dónde está el problema → verificar la calidad del tráfico que producen → decidir con métricas de negocio → documentar la relación entre ambas para el canal** y adjunta evidencia en cada transición.
3. Construye la ficha de medición de **tasa de clic por variante**; si el dato no existe, diseña cómo obtenerlo y cuánto costaría.
4. Escribe una alternativa que contradiga tu preferencia inicial y hazle un *pre-mortem*.
5. Lee dos referencias de la tabla, registra una coincidencia y una tensión, y corrige el brief si corresponde.
6. Repite la decisión desde el rol de dirección: indica qué cambia al aumentar alcance e irreversibilidad.

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

- Avinash Kaushik — *Web Analytics 2.0* (2009). **Uso en esta clase:** medición orientada a decisión, segmentación y crítica del dato de vanidad. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Brad Geddes — *Advanced Google AdWords* (2014, 3.ª ed.). **Uso en esta clase:** estructura de cuentas, subastas, calidad y control del gasto en búsqueda pagada. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013). **Uso en esta clase:** una métrica que importa por etapa y por modelo de negocio. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.
- Dave Chaffey y Fiona Ellis-Chadwick — *Digital Marketing* (2022, 8.ª ed.). **Uso en esta clase:** planificación digital integrada: canales, medición y gobierno. Lectura selectiva: índice y capítulos pertinentes; registra edición y páginas consultadas.

**Estándar pedagógico del programa:** Susan A. Ambrose et al. — *How Learning Works* (2010); Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — *Make It Stick* (2014); Grant Wiggins y Jay McTighe — *Understanding by Design* (2005, 2.ª ed.); Anders Ericsson y Robert Pool — *Peak* (2016); William Ellet — *The Case Study Handbook* (2018, ed. revisada).

> **Regla de fuentes.** Las obras anteriores estructuran las perspectivas de esta materia. Cualquier norma, impuesto, tarifa, política de plataforma o estándar vivo mencionado debe comprobarse nuevamente en su fuente primaria vigente antes de usarse en una operación real. El desarrollo de esta clase es original y no reproduce capítulos protegidos por derechos de autor.

---

← [Clase 08 · Presupuesto y ritmo de gasto](class-08-presupuesto-y-pacing.md) · [Índice de la parte](README.md) · [Clase 10 · CPA, CAC y ROAS](class-10-cpa-cac-y-roas.md) →
