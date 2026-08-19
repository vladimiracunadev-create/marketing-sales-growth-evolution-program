# -*- coding: utf-8 -*-
"""Parte 24 — Empresa real, regulación y Capstone."""

CLASES = [
    dict(
        n="01",
        slug="diseno-de-la-empresa-del-capstone",
        titulo="Diseño de la empresa del Capstone",
        tesis=(
            "El Capstone exige operar una empresa comercial completa: propia o la simulación persistente del "
            "programa. La primera decisión es de alcance: qué se construirá realmente, qué se simulará con "
            "datos y qué queda explícitamente fuera. Un Capstone que promete todo termina entregando "
            "documentos superficiales; uno con alcance acotado y profundidad real produce evidencia "
            "utilizable en un proceso de selección."
        ),
        conceptos=[
            ("alcance del Capstone", "conjunto de entregables comprometidos con su nivel de profundidad"),
            ("frontera entre real y simulado", "declaración explícita de qué datos son reales y cuáles construidos"),
            ("evidencia utilizable", "artefacto que otra persona podría usar o auditar en un contexto profesional"),
            ("criterio de suficiencia", "estándar que define cuándo un entregable está completo"),
        ],
        metodo=[
            "elegir empresa propia o simulación persistente",
            "definir el alcance y lo que queda fuera",
            "declarar qué es real y qué es simulado",
            "fijar el criterio de suficiencia por entregable",
            "planificar el trabajo con hitos verificables",
        ],
        senales=[
            ("entregables con criterio de suficiencia", "entregables con estándar definido, sobre entregables comprometidos"),
            ("proporción de datos reales", "entregables basados en datos reales, sobre entregables totales"),
            ("cumplimiento de hitos", "hitos alcanzados en plazo, sobre hitos definidos"),
        ],
        caso=(
            "El Capstone puede desarrollarse sobre Ruta Andina con los datos sintéticos del repositorio o "
            "sobre una empresa propia. En ambos casos debe declararse el origen de cada dato."
        ),
        limite=(
            "Un Capstone sobre datos simulados no acredita resultados reales de mercado. Su valor está en el "
            "razonamiento y en la calidad de los artefactos, y así debe presentarse."
        ),
        libros=["osterwalder-bmg", "rumelt", "ellet", "blank"],
        error=("Comprometer un alcance mayor que el tiempo disponible",
               "Define el alcance con criterio de suficiencia por entregable y declara lo que queda fuera."),
    ),
    dict(
        n="02",
        slug="seleccion-de-mercado-y-problema",
        titulo="Selección de mercado y problema",
        tesis=(
            "La elección del mercado y del problema determina el techo de todo lo que venga después. Los "
            "criterios son cuatro: el problema existe y duele, hay clientes accesibles, la empresa puede "
            "servirlos y existe una forma de capturar valor. Fallar en cualquiera invalida el resto del "
            "trabajo, por bien ejecutado que esté."
        ),
        conceptos=[
            ("problema verificado", "dificultad documentada con frecuencia, costo y consecuencia"),
            ("accesibilidad del cliente", "existencia de un camino viable para alcanzarlo"),
            ("capacidad de servir", "aptitud real de entregar el resultado prometido"),
            ("mecanismo de captura", "forma en que la empresa convierte el valor entregado en ingreso"),
        ],
        metodo=[
            "documentar el problema con evidencia primaria",
            "verificar la accesibilidad del cliente objetivo",
            "evaluar la capacidad de servir con recursos reales",
            "definir el mecanismo de captura de valor",
            "declarar los supuestos críticos y su plan de validación",
        ],
        senales=[
            ("evidencia del problema", "observaciones del problema con fuente y fecha registradas, sobre observaciones totales recogidas"),
            ("accesibilidad verificada", "canales con costo de alcance estimado, sobre canales identificados para el segmento"),
            ("supuestos críticos declarados", "supuestos identificados con plan de validación, sobre supuestos del proyecto"),
        ],
        caso=(
            "El Capstone debe elegir entre profundizar en talleres, abrir centros médicos o atender "
            "municipios. Cada opción cambia producto, cumplimiento y camino de acceso."
        ),
        limite=(
            "La verificación completa del problema puede exceder el tiempo del Capstone. Lo exigible es "
            "evidencia suficiente y declaración honesta de lo que falta."
        ),
        libros=["blank", "christensen", "moore", "fitzpatrick"],
        error=("Elegir el mercado por interés personal sin verificar accesibilidad",
               "Estima el costo de alcanzar al cliente antes de comprometer la elección."),
    ),
    dict(
        n="03",
        slug="investigacion-con-evidencia",
        titulo="Investigación con evidencia",
        tesis=(
            "El componente de investigación del Capstone se evalúa por método, no por extensión: qué "
            "pregunta responde, cómo se recogió la evidencia, qué sesgos tiene y qué decisión cambió. Diez "
            "entrevistas bien ejecutadas y documentadas valen más que una encuesta de doscientas respuestas "
            "mal diseñada."
        ),
        conceptos=[
            ("pregunta de investigación", "formulación que puede responderse con evidencia y que informa una decisión"),
            ("declaración de método", "descripción de fuentes, muestra, procedimiento y límites"),
            ("sesgo declarado", "limitación reconocida que afecta la interpretación de los hallazgos"),
            ("decisión informada", "elección concreta que cambió a partir de la evidencia"),
        ],
        metodo=[
            "formular las preguntas desde las decisiones pendientes",
            "elegir el método proporcional al tiempo disponible",
            "ejecutar y documentar el procedimiento",
            "declarar sesgos y límites",
            "conectar cada hallazgo con la decisión que informa",
        ],
        senales=[
            ("hallazgos con decisión asociada", "hallazgos que modificaron una decisión, sobre hallazgos presentados"),
            ("trazabilidad del método", "afirmaciones con procedimiento documentado, sobre afirmaciones del informe"),
            ("sesgos declarados", "limitaciones explicitadas, sobre limitaciones identificables"),
        ],
        caso=(
            "El Capstone exige investigación primaria con al menos ocho entrevistas documentadas y una "
            "revisión de fuentes secundarias con trazabilidad completa."
        ),
        limite=(
            "La investigación de un Capstone tiene muestra pequeña por diseño. Su valor está en el método y "
            "en la honestidad sobre los límites, no en la representatividad."
        ),
        libros=["fitzpatrick", "malhotra", "portigal", "hubbard"],
        error=("Presentar hallazgos sin conectarlos a decisiones",
               "Asocia cada hallazgo a la decisión concreta que informa o retíralo del informe."),
    ),
    dict(
        n="04",
        slug="oferta-y-pricing",
        titulo="Oferta y pricing del Capstone",
        tesis=(
            "El componente de oferta y precio debe demostrar coherencia entre valor entregado, disposición a "
            "pagar y economía unitaria. No basta con proponer un precio: hay que mostrar de dónde sale, qué "
            "evidencia lo sostiene y qué margen deja después del costo real de servir. Un plan con precio "
            "atractivo y margen negativo es un error, no una estrategia de penetración."
        ),
        conceptos=[
            ("estructura de oferta", "conjunto de planes, alcances y condiciones definidos"),
            ("fundamento del precio", "evidencia y razonamiento que sostienen el nivel elegido"),
            ("economía unitaria del plan", "margen de contribución y periodo de recuperación por plan"),
            ("coherencia oferta-operación", "correspondencia entre lo prometido y lo que la operación puede entregar"),
        ],
        metodo=[
            "definir la oferta con alcance y exclusiones",
            "fundamentar el precio con evidencia de valor",
            "calcular la economía unitaria completa",
            "verificar la coherencia con la capacidad operativa",
            "declarar los supuestos y su sensibilidad",
        ],
        senales=[
            ("margen de contribución por plan", "ingreso menos costo variable de servir, sobre ingreso del plan"),
            ("periodo de recuperación", "meses hasta recuperar el costo de adquisición, por plan"),
            ("fundamento documentado", "decisiones de precio con evidencia asociada, sobre decisiones de precio"),
        ],
        caso=(
            "El Capstone exige presentar la arquitectura de precios con economía unitaria verificable y "
            "análisis de sensibilidad ante cambios de churn y de costo de servir."
        ),
        limite=(
            "Sin clientes reales, la disposición a pagar es una estimación. El trabajo debe declarar el nivel "
            "de evidencia de cada supuesto de precio."
        ),
        libros=["ramanujam", "nagle", "croll-yoskovitz", "simon"],
        error=("Fijar precio sin calcular el costo real de servir",
               "Incluye implementación y soporte en el costo antes de declarar el margen del plan."),
    ),
    dict(
        n="05",
        slug="marca-y-activos-comerciales",
        titulo="Marca y activos comerciales",
        tesis=(
            "El Capstone debe producir los activos que una operación real necesita: posicionamiento, "
            "identidad mínima, mensajes por segmento, materiales de venta y sitio o página de conversión. La "
            "prueba es de uso: otra persona debe poder tomar esos activos y ejecutar una conversación "
            "comercial completa sin inventar nada."
        ),
        conceptos=[
            ("activo comercial", "material que permite ejecutar una interacción comercial sin improvisar"),
            ("coherencia entre activos", "consistencia de promesa y tono entre todas las piezas"),
            ("prueba de uso", "verificación de que una persona ajena puede ejecutar con los activos"),
            ("nivel mínimo viable", "grado de terminación suficiente para operar sin comprometer credibilidad"),
        ],
        metodo=[
            "definir el conjunto mínimo de activos necesarios",
            "producirlos con coherencia de promesa y tono",
            "someterlos a prueba de uso con alguien ajeno",
            "corregir lo que no resultó ejecutable",
            "documentar las reglas de uso y actualización",
        ],
        senales=[
            ("activos completos", "activos producidos, sobre activos definidos como mínimos"),
            ("resultado de la prueba de uso", "interacciones que la persona ajena pudo ejecutar, sobre interacciones planteadas"),
            ("coherencia auditada", "activos que respetan la declaración de posicionamiento, sobre activos auditados"),
        ],
        caso=(
            "El Capstone exige entregar declaración de posicionamiento, guía verbal mínima, tres mensajes por "
            "segmento, propuesta comercial estándar y página de conversión."
        ),
        limite=(
            "La calidad visual profesional no es el objetivo ni el criterio de evaluación. Lo que se evalúa "
            "es coherencia, claridad y capacidad de uso."
        ),
        libros=["ries-trout", "wheeler", "handley", "keller-brand"],
        error=("Producir activos sin prueba de uso",
               "Entrega los materiales a alguien ajeno y verifica si puede ejecutar una conversación completa."),
    ),
    dict(
        n="06",
        slug="gtm",
        titulo="Go-to-market del Capstone",
        tesis=(
            "El componente de salida al mercado debe declarar el movimiento comercial elegido, su economía y "
            "la secuencia de ejecución. La coherencia es el criterio de evaluación: un movimiento de terreno "
            "para un ticket bajo, o un plan de autoservicio sobre un producto que exige implementación "
            "asistida, invalidan el plan aunque estén bien redactados."
        ),
        conceptos=[
            ("movimiento elegido", "forma dominante de adquisición seleccionada con su justificación"),
            ("economía del movimiento", "costo por cliente y periodo de recuperación asociados"),
            ("secuencia de ejecución", "orden temporal de las acciones con sus dependencias"),
            ("prueba de coherencia", "verificación de compatibilidad entre movimiento, ticket y capacidad"),
        ],
        metodo=[
            "elegir el movimiento y justificarlo con la economía",
            "definir canales y su contribución esperada",
            "construir la secuencia con dependencias",
            "verificar la coherencia con la capacidad declarada",
            "definir los indicadores de seguimiento",
        ],
        senales=[
            ("costo por cliente del movimiento", "gasto estimado del movimiento, dividido por clientes esperados"),
            ("coherencia movimiento-ticket", "relación entre costo de adquisición y valor del primer año"),
            ("dependencias identificadas", "acciones con precondiciones declaradas, sobre acciones del plan"),
        ],
        caso=(
            "El Capstone debe demostrar que su movimiento comercial es económicamente viable para el ticket "
            "elegido y ejecutable con la capacidad declarada."
        ),
        limite=(
            "Un plan de salida al mercado no ejecutado es una hipótesis. Su evaluación se centra en la "
            "calidad del razonamiento y en la explicitación de supuestos."
        ),
        libros=["moore", "ross", "bush-plg", "rumelt"],
        error=("Elegir el movimiento sin verificar su economía",
               "Compara el costo del movimiento con el valor del contrato antes de comprometer el plan."),
    ),
    dict(
        n="07",
        slug="campana-de-adquisicion",
        titulo="Campaña de adquisición",
        tesis=(
            "El componente de adquisición debe incluir una campaña diseñada de punta a punta: audiencia, "
            "mensaje, canal, página de destino, medición y presupuesto con supuestos. Se evalúa la "
            "coherencia interna y la explicitación de las condiciones bajo las cuales la campaña sería "
            "detenida, no la creatividad de las piezas."
        ),
        conceptos=[
            ("diseño integral de campaña", "conjunto coherente de audiencia, mensaje, canal, destino y medición"),
            ("supuesto de desempeño", "estimación declarada de costo y conversión que sostiene el presupuesto"),
            ("condición de detención", "resultado que obligaría a suspender o modificar la campaña"),
            ("plan de medición", "definición de qué se registrará y cómo se evaluará"),
        ],
        metodo=[
            "definir audiencia y mensaje desde la investigación",
            "elegir canal y construir la página de destino",
            "declarar los supuestos de costo y conversión",
            "definir el plan de medición y las condiciones de detención",
            "presentar el presupuesto con escenarios",
        ],
        senales=[
            ("costo por oportunidad estimado", "presupuesto dividido por oportunidades esperadas, con su supuesto"),
            ("coherencia mensaje-destino", "correspondencia entre la promesa del anuncio y la página de llegada"),
            ("condiciones de detención definidas", "métricas con umbral de detención, sobre métricas críticas"),
        ],
        caso=(
            "El Capstone exige una campaña completa con presupuesto de CLP 3 millones, medición definida y "
            "condiciones explícitas de detención."
        ),
        limite=(
            "Sin ejecución real, los supuestos de desempeño no están validados. El trabajo debe declarar de "
            "dónde salió cada estimación."
        ),
        libros=["geddes", "kaushik", "laja", "handley"],
        error=("Presentar la campaña sin condiciones de detención",
               "Define para cada métrica crítica el umbral que obligaría a suspender o modificar."),
    ),
    dict(
        n="08",
        slug="prospeccion-y-ventas",
        titulo="Prospección y ventas del Capstone",
        tesis=(
            "El componente comercial debe entregar el sistema completo: lista objetivo con base de licitud, "
            "secuencias, guion de diagnóstico, propuesta estándar, manejo de objeciones y criterios de "
            "calificación. Se evalúa que sea ejecutable: otra persona debe poder trabajar una oportunidad "
            "completa con esos materiales."
        ),
        conceptos=[
            ("sistema comercial ejecutable", "conjunto de materiales y reglas que permite operar sin improvisar"),
            ("base de licitud de la lista", "fundamento jurídico que permite contactar a los prospectos"),
            ("guion de diagnóstico", "conjunto de preguntas ordenadas por objetivo"),
            ("criterio de calificación", "condiciones verificables para invertir tiempo comercial"),
        ],
        metodo=[
            "construir la lista objetivo con base de licitud documentada",
            "diseñar secuencias y guiones por segmento",
            "producir la propuesta estándar con alcance y exclusiones",
            "documentar objeciones frecuentes con respuesta",
            "probar el sistema con una persona ajena",
        ],
        senales=[
            ("materiales completos", "materiales producidos, sobre materiales definidos como necesarios"),
            ("resultado de la prueba de ejecución", "etapas que la persona ajena pudo ejecutar, sobre etapas del proceso"),
            ("cumplimiento normativo de la lista", "contactos con base de licitud documentada, sobre contactos de la lista"),
        ],
        caso=(
            "El Capstone exige un sistema comercial que otra persona pueda ejecutar, con lista construida "
            "conforme a la normativa de datos personales."
        ),
        limite=(
            "Sin ejecución real no hay tasas de conversión propias. Las estimaciones deben declararse como "
            "supuestos con su fuente de referencia."
        ),
        libros=["weinberg-sales", "blount", "rackham", "ross"],
        error=("Construir la lista sin documentar la base de licitud",
               "Registra origen y fundamento de cada contacto antes de incorporarlo a la lista."),
    ),
    dict(
        n="09",
        slug="crm-y-pipeline",
        titulo="CRM y pipeline del Capstone",
        tesis=(
            "El componente operativo debe entregar un CRM configurado o simulado con modelo de datos, "
            "etapas con criterios de salida, campos mínimos, tableros y reglas de higiene. Se evalúa la "
            "coherencia entre el proceso comercial declarado y la configuración: si las etapas del sistema "
            "no corresponden al proceso, el diseño es decorativo."
        ),
        conceptos=[
            ("configuración coherente", "correspondencia entre el proceso declarado y la configuración del sistema"),
            ("campo mínimo necesario", "dato indispensable para calcular las métricas comprometidas"),
            ("regla de higiene", "criterio que mantiene el dato completo y vigente"),
            ("tablero operativo", "conjunto de vistas que permite trabajar y dirigir"),
        ],
        metodo=[
            "traducir el proceso comercial a etapas del sistema",
            "definir campos mínimos y su justificación",
            "configurar tableros para operación y dirección",
            "establecer reglas de higiene y responsables",
            "verificar que las métricas comprometidas se pueden calcular",
        ],
        senales=[
            ("métricas calculables", "métricas comprometidas que el modelo permite calcular, sobre métricas comprometidas"),
            ("campos obligatorios con uso", "campos requeridos que aparecen en algún tablero, sobre campos requeridos"),
            ("coherencia proceso-sistema", "etapas del sistema que corresponden al proceso declarado, sobre etapas configuradas"),
        ],
        caso=(
            "El Capstone exige demostrar que las métricas comprometidas en el plan pueden calcularse con el "
            "modelo de datos propuesto."
        ),
        limite=(
            "Una configuración sin datos reales no prueba usabilidad. La evaluación se centra en la coherencia "
            "del diseño y en la calculabilidad de las métricas."
        ),
        libros=["roberge", "diorio", "grove", "provost"],
        error=("Configurar etapas que no corresponden al proceso declarado",
               "Traduce el proceso comercial paso a paso y verifica la correspondencia con la configuración."),
    ),
    dict(
        n="10",
        slug="customer-success",
        titulo="Customer Success del Capstone",
        tesis=(
            "El componente de retención debe definir el resultado esperado del cliente, el onboarding que lo "
            "produce, el puntaje de salud, el ciclo de renovación y el criterio de expansión. Se evalúa la "
            "conexión con el resto: si la venta promete algo que el onboarding no entrega, el diseño es "
            "incoherente y el churn está garantizado."
        ),
        conceptos=[
            ("resultado esperado documentado", "beneficio comprometido expresado en la métrica del cliente"),
            ("coherencia venta-entrega", "correspondencia entre lo prometido y lo que el proceso produce"),
            ("modelo de cobertura", "forma de atender la cartera según valor y complejidad"),
            ("criterio de expansión", "condición que autoriza proponer una venta adicional"),
        ],
        metodo=[
            "definir el resultado esperado por segmento",
            "diseñar el onboarding que lo produce",
            "construir el puntaje de salud con componentes justificados",
            "definir el ciclo de renovación y el criterio de expansión",
            "verificar la coherencia con lo prometido en la venta",
        ],
        senales=[
            ("coherencia venta-entrega", "promesas comerciales cubiertas por el proceso de entrega, sobre promesas declaradas"),
            ("tiempo hasta el primer valor proyectado", "días estimados hasta el primer resultado, por segmento"),
            ("componentes del puntaje justificados", "componentes con fundamento documentado, sobre componentes del puntaje"),
        ],
        caso=(
            "El Capstone exige mostrar cómo el onboarding produce el resultado prometido en la propuesta "
            "comercial y cómo se verificará."
        ),
        limite=(
            "Sin clientes reales no hay curvas de retención propias. Las proyecciones deben apoyarse en "
            "referencias declaradas y presentarse como supuestos."
        ),
        libros=["mehta", "hulick", "fader-ltv", "dixon-effort"],
        error=("Diseñar el onboarding sin verificar la promesa comercial",
               "Contrasta cada promesa de la propuesta con el proceso que la entregaría."),
    ),
    dict(
        n="11",
        slug="dashboard-financiero-comercial",
        titulo="Dashboard financiero-comercial",
        tesis=(
            "El Capstone debe entregar un tablero que conecte la operación comercial con la economía del "
            "negocio: ingreso, margen de contribución, costo de adquisición, periodo de recuperación, "
            "retención y proyección. Se evalúa la trazabilidad de cada cifra y la coherencia aritmética del "
            "conjunto, no la sofisticación visual."
        ),
        conceptos=[
            ("trazabilidad de la cifra", "posibilidad de reconstruir el cálculo desde sus componentes"),
            ("coherencia aritmética", "consistencia entre los indicadores del tablero"),
            ("proyección con supuestos", "estimación futura acompañada de las condiciones que la sostienen"),
            ("indicador de alerta", "métrica con umbral definido que gatilla una acción"),
        ],
        metodo=[
            "definir los indicadores y su cálculo",
            "construir el tablero con datos del proyecto",
            "verificar la coherencia aritmética del conjunto",
            "declarar los supuestos de la proyección",
            "definir umbrales de alerta y sus acciones",
        ],
        senales=[
            ("cifras trazables", "indicadores con cálculo documentado, sobre indicadores del tablero"),
            ("coherencia aritmética verificada", "relaciones que cuadran entre indicadores, sobre relaciones verificables"),
            ("indicadores con umbral", "métricas con umbral y acción definidos, sobre métricas críticas"),
        ],
        caso=(
            "El Capstone exige un tablero donde el ingreso proyectado, el costo de adquisición y la retención "
            "sean aritméticamente consistentes entre sí."
        ),
        limite=(
            "Un tablero con datos simulados demuestra diseño, no desempeño. Debe declararse el origen de cada "
            "serie utilizada."
        ),
        libros=["kaplan-norton", "croll-yoskovitz", "provost", "kaushik"],
        error=("Presentar indicadores sin verificar su coherencia entre sí",
               "Comprueba que las relaciones aritméticas entre indicadores cuadren antes de presentar."),
    ),
    dict(
        n="12",
        slug="cumplimiento-chile",
        titulo="Cumplimiento normativo en Chile",
        tesis=(
            "El Capstone debe demostrar que la operación propuesta cumple el marco chileno aplicable: "
            "derechos del consumidor y comercio electrónico, tratamiento de datos personales, propiedad "
            "industrial de la marca, obligaciones tributarias de la venta y reglas de libre competencia. No "
            "se trata de un anexo legal: cada uno de esos frentes impone requisitos de diseño sobre "
            "materiales, procesos y sistemas."
        ),
        conceptos=[
            ("obligación aplicable", "requisito normativo que rige la operación propuesta"),
            ("requisito de diseño", "consecuencia concreta de la norma sobre un proceso o material"),
            ("verificación en fuente primaria", "comprobación de la norma en su texto oficial vigente"),
            ("registro de cumplimiento", "documentación que acredita el cumplimiento ante una revisión"),
        ],
        metodo=[
            "identificar las obligaciones aplicables a la operación",
            "traducir cada una en requisitos de diseño concretos",
            "verificar la vigencia en fuente primaria",
            "documentar el cumplimiento con evidencia",
            "declarar los frentes que requieren asesoría especializada",
        ],
        senales=[
            ("obligaciones identificadas y cubiertas", "requisitos con solución de diseño documentada, sobre requisitos identificados"),
            ("verificaciones en fuente primaria", "normas comprobadas en texto oficial, sobre normas citadas"),
            ("brechas declaradas", "incumplimientos reconocidos con plan de corrección, sobre brechas detectadas"),
        ],
        caso=(
            "El Capstone debe mostrar cómo su tienda cumple el derecho a retracto, cómo trata los datos "
            "personales de su base y cómo protege su marca."
        ),
        limite=(
            "Este trabajo es formación aplicada, no asesoría legal. Toda operación real requiere revisión "
            "profesional y verificación de la norma vigente a esa fecha."
        ),
        libros=["iso-31000", "oneil", "nist-airmf", "rumelt"],
        error=("Tratar el cumplimiento como anexo final",
               "Traduce cada obligación en requisitos de diseño e incorpóralos a procesos y materiales."),
    ),
    dict(
        n="13",
        slug="defensa-ejecutiva",
        titulo="Defensa ejecutiva",
        tesis=(
            "La defensa somete el trabajo a preguntas duras: por qué este segmento, de dónde sale este "
            "precio, qué pasa si el churn duplica, qué harías con la mitad del presupuesto. Se evalúa la "
            "capacidad de sostener el razonamiento con evidencia y de reconocer los límites del propio "
            "trabajo. Defender no es convencer: es mostrar cómo se pensó y qué cambiaría la conclusión."
        ),
        conceptos=[
            ("argumento sostenido en evidencia", "afirmación respaldada por dato o razonamiento verificable"),
            ("reconocimiento de límites", "declaración honesta de lo que el trabajo no puede sostener"),
            ("pregunta de estrés", "cuestionamiento que somete el plan a un escenario adverso"),
            ("condición de cambio", "resultado que llevaría a modificar la recomendación"),
        ],
        metodo=[
            "preparar el resumen ejecutivo con la recomendación al inicio",
            "anticipar las preguntas de estrés y preparar la respuesta",
            "declarar los límites del trabajo",
            "responder con evidencia y reconocer lo que no se sabe",
            "registrar las observaciones para la retrospectiva",
        ],
        senales=[
            ("respuestas sostenidas en evidencia", "respuestas con dato o razonamiento verificable, sobre preguntas recibidas"),
            ("límites reconocidos", "limitaciones declaradas espontáneamente, sobre limitaciones identificables"),
            ("coherencia bajo estrés", "respuestas consistentes ante escenarios adversos, sobre preguntas de estrés recibidas"),
        ],
        caso=(
            "El panel preguntará por qué el segmento elegido, cómo se fijó el precio, qué ocurre si el churn "
            "duplica y qué se haría con la mitad del presupuesto."
        ),
        limite=(
            "Una defensa brillante no corrige un trabajo débil. La preparación no sustituye la calidad del "
            "análisis subyacente."
        ),
        libros=["ellet", "heath", "rumelt", "grove"],
        error=("Defender afirmaciones que no se pueden sostener",
               "Reconoce explícitamente los límites y qué evidencia haría falta para cerrarlos."),
    ),
    dict(
        n="14",
        slug="retrospectiva-y-portafolio-profesional",
        titulo="Retrospectiva y portafolio profesional",
        tesis=(
            "El cierre del programa convierte el trabajo en portafolio: artefactos seleccionados, "
            "documentados y presentables ante un empleador o un cliente. La retrospectiva es igual de "
            "importante: qué se aprendió, qué se haría distinto y qué competencias quedan por desarrollar. "
            "Un portafolio sin esa reflexión muestra qué se hizo pero no qué se entendió."
        ),
        conceptos=[
            ("artefacto de portafolio", "entregable seleccionado por su calidad y su capacidad de mostrar competencia"),
            ("documentación del contexto", "explicación del problema, del método y de las decisiones tomadas"),
            ("retrospectiva", "análisis honesto de lo que funcionó, lo que no y por qué"),
            ("plan de desarrollo", "definición de las competencias que quedan por construir y cómo"),
        ],
        metodo=[
            "seleccionar los artefactos que mejor muestran competencia",
            "documentar contexto, método y decisiones de cada uno",
            "escribir la retrospectiva con hallazgos concretos",
            "definir el plan de desarrollo posterior",
            "publicar el portafolio en un formato accesible",
        ],
        senales=[
            ("artefactos documentados", "entregables con contexto y método documentados, sobre entregables del portafolio"),
            ("hallazgos de la retrospectiva", "aprendizajes con evidencia asociada, sobre aprendizajes declarados en la retrospectiva"),
            ("competencias con plan de desarrollo", "brechas identificadas con plan asociado, sobre brechas declaradas"),
        ],
        caso=(
            "El cierre del programa exige un portafolio con al menos seis artefactos documentados y una "
            "retrospectiva que identifique competencias pendientes."
        ),
        limite=(
            "Un portafolio abundante no equivale a uno bueno. Seis artefactos excelentes muestran más "
            "competencia que veinte incompletos."
        ),
        libros=["ellet", "ericsson", "ambrose", "wiggins"],
        error=("Incluir todo el trabajo sin selección ni documentación",
               "Selecciona los mejores artefactos y documenta contexto, método y decisiones de cada uno."),
    ),
]
