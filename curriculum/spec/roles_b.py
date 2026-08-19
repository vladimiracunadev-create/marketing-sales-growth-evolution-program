# -*- coding: utf-8 -*-
"""Rutas profesionales — segundo bloque: venta, operación de ingresos y dirección.

Se agrega a `spec.roles.ROLES`. Misma estructura de campos.
"""

from spec.roles import SALARIO_DIRECCION, SALARIO_ENTRADA, SALARIO_MEDIO

ROLES_B = [
    # ------------------------------------------------------------------ 05
    dict(
        slug="sdr-bdr",
        emoji="📞",
        titulo="SDR / BDR — desarrollo de ventas",
        familia="Ventas",
        resumen=(
            "El puesto que origina las conversaciones que después alguien cierra. Es la puerta de entrada más "
            "frecuente a una carrera comercial y también el rol donde más gente se quema, porque se mide por "
            "actividad y se sostiene con disciplina frente al rechazo."
        ),
        nivel="Entrada; no exige experiencia previa pero sí tolerancia al rechazo y método",
        foco="Listas objetivo, señales de oportunidad, secuencias multicanal y calificación temprana",
        credencial="Un sistema de prospección con relación actividad-oportunidades medida",
        que_es=[
            "El desarrollo de ventas separa dos trabajos que antes hacía la misma persona: originar "
            "conversaciones y cerrar negocios. La especialización funciona porque las habilidades son "
            "distintas y porque el vendedor que prospecta sólo cuando le falta pipeline produce ciclos de "
            "abundancia y sequía.",
            "El determinante principal es la disciplina de actividad sostenida, porque el pipeline responde "
            "con retardo: la sequía de hoy se originó en la falta de prospección de hace dos meses. Pero el "
            "volumen sin calidad de lista produce ruido, quema la reputación del dominio y expone a la "
            "empresa legalmente.",
            "Es un rol con techo bajo si se ejecuta mecánicamente y con techo alto si se ejecuta con criterio. "
            "Quien aprende a investigar una cuenta, encontrar la señal que hace pertinente el contacto y "
            "escribir tres líneas que alguien responde, tiene una habilidad que se paga durante toda la "
            "carrera.",
        ],
        dia=[
            "**Bloques de prospección:** franjas fijas de contacto, elegidas según la contactabilidad medida "
            "del segmento y no según la comodidad propia.",
            "**Investigación previa:** dos minutos por cuenta buscando la señal que justifica el contacto "
            "ahora. Sin señal, el mensaje es genérico y compite con decenas iguales.",
            "**Secuencias multicanal:** correo, teléfono y red profesional, con un aporte distinto en cada "
            "paso y condiciones de salida claras.",
            "**Calificación:** verificar perfil y problema en la conversación, y descalificar temprano sin "
            "drama cuando no corresponde.",
            "**Registro y traspaso:** dejar el contexto que el ejecutivo necesita para no empezar de cero.",
        ],
        tecnico=[
            "**Construcción ética de listas.** Base de licitud documentada, origen del dato y mecanismo de "
            "oposición. No es burocracia: es la condición legal y la que protege el dominio.",
            "**Señales de oportunidad.** Hechos observables que hacen pertinente el contacto: apertura, "
            "contratación, cambio normativo, reclamo público.",
            "**Escritura breve y específica.** Asunto informativo, cuerpo corto y petición proporcional al "
            "nivel de confianza existente.",
            "**Cadencia con variación.** Cada paso aporta algo distinto; repetir el mismo mensaje en tres "
            "canales es saturación, no persistencia.",
            "**Calificación temprana.** Criterios verificables aplicados en la primera conversación, con "
            "descalificación explícita.",
            "**Métricas del propio trabajo.** Contactabilidad por franja, respuesta por paso, conversaciones "
            "por reunión agendada.",
        ],
        herramientas=(
            "CRM:              HubSpot, Salesforce, Pipedrive\n"
            "Secuencias:       herramientas de cadencia y correo\n"
            "Investigación:    LinkedIn, fuentes públicas, prensa sectorial\n"
            "Verificación:     validación de correos y de datos de contacto\n"
            "Registro:         notas estructuradas para el traspaso"
        ),
        blandas=[
            "**Gestión del rechazo.** La mayoría de los intentos no obtiene respuesta y eso es el "
            "funcionamiento normal del canal, no una señal sobre la persona.",
            "**Disciplina de calendario.** El rol se sostiene con bloques protegidos, no con voluntad.",
            "**Curiosidad genuina.** Quien investiga la cuenta escribe mejor y responde mejor.",
            "**Honestidad al calificar.** Inflar el pipeline para verse bien esta semana produce un forecast "
            "falso y una conversación incómoda dentro de un mes.",
        ],
        ruta=[
            ("01", "el motor de ingresos completo: para entender dónde encaja tu trabajo"),
            ("02", "cliente y unidad de decisión: a quién le hablas y qué le importa"),
            ("11", "**el núcleo del rol**: listas, señales, secuencias y calificación"),
            ("08", "proceso comercial: apertura, discovery y traspaso"),
            ("16", "CRM y disciplina de registro, que es donde vive tu trabajo"),
            ("13", "copywriting: la diferencia entre 0,4 % y 8 % de respuesta"),
        ],
        clases=[
            ("11", "02", "Construcción ética de listas: base de licitud y reputación de dominio"),
            ("11", "03", "Investigación de prospectos: la señal que justifica el contacto ahora"),
            ("11", "04", "Correo en frío: petición proporcional al nivel de confianza"),
            ("11", "05", "Llamada en frío: verificar la franja horaria antes de invertir esfuerzo"),
            ("11", "13", "Secuencias multicanal: variación de aporte y punto de salida"),
            ("08", "04", "Discovery: sin cifra estimada por el cliente no hay diagnóstico"),
            ("11", "14", "Sistema de prospección repetible: predecir oportunidades desde la actividad"),
        ],
        labs=["11", "08"],
        artefactos=[
            "Lista objetivo con base de licitud documentada por contacto",
            "Secuencia multicanal con aporte por paso y condiciones de salida",
            "Registro de respuesta por paso con umbrales de revisión",
            "Relación actividad-oportunidades medida por segmento",
        ],
        credenciales=[
            "**No hay certificación relevante para este rol.** Lo que se evalúa en entrevista es un correo "
            "escrito en vivo y una llamada simulada.",
            "**Portafolio** — una secuencia real con métricas por paso y la explicación de qué ajustaste "
            "cuando la respuesta cayó.",
        ],
        progresion=(
            "SDR → **[ejecutivo comercial](ejecutivo-comercial.md)** en doce a dieciocho meses es la ruta "
            "clásica. Otros caminos: jefatura de desarrollo de ventas, [RevOps](revops.md) si te atrae el "
            "sistema, o [growth](growth-manager.md) si te atrae la experimentación."
        ),
        salario=SALARIO_ENTRADA,
        mitos=[
            ("«Es llamar por teléfono todo el día.»",
             "La mitad del trabajo es investigar y escribir. Quien sólo marca números obtiene el resultado "
             "que corresponde a no investigar."),
            ("«Más volumen es mejor.»",
             "Volumen sin calidad de lista quema el dominio y genera reclamos. La cadencia supone que la "
             "lista ya fue filtrada."),
            ("«Hay que insistir hasta que respondan.»",
             "Existe un punto donde la insistencia produce rechazo y daño reputacional; además, la solicitud "
             "de no contacto se respeta de inmediato y en todos los canales."),
            ("«Es un trabajo sin futuro.»",
             "Es la mejor escuela comercial que existe: enseña a investigar, escribir y calificar, que es la "
             "base de todo lo que viene después."),
        ],
        honestidad=(
            "El programa te da método, mensajes y criterio de calificación. Lo que no simula es la resistencia "
            "emocional de cien intentos con dos respuestas, que es la parte que hace fracasar a la mayoría. "
            "Si vas a este rol, prueba antes una semana real de prospección en un proyecto propio."
        ),
    ),
    # ------------------------------------------------------------------ 06
    dict(
        slug="ejecutivo-comercial",
        emoji="🤝",
        titulo="Ejecutivo comercial / Account Executive",
        familia="Ventas",
        resumen=(
            "Quien conduce el negocio desde el diagnóstico hasta la firma. En venta compleja no gana quien "
            "mejor presenta, sino quien mejor diagnostica y quien logra que el comité interno del cliente "
            "llegue a un acuerdo."
        ),
        nivel="Intermedio; se entra desde SDR o desde otra industria con base comercial",
        foco="Discovery, calificación, comité de compra, propuesta, negociación y cierre",
        credencial="Un deal review completo con mapa de comité y plan mutuo",
        que_es=[
            "El ejecutivo comercial responde por un número. Esa es la diferencia con cualquier otro rol del "
            "área: al final del trimestre hay una cifra y hay alguien que responde por ella.",
            "El trabajo real no es persuadir. Rackham documentó que en ventas grandes las técnicas de cierre "
            "agresivo reducen los resultados, y que lo que se asocia al éxito son las preguntas de "
            "implicación: ayudar al cliente a dimensionar lo que le cuesta su problema. La urgencia se "
            "construye con evidencia del propio cliente, no con presión.",
            "La segunda mitad del oficio es política, en el buen sentido: entender quién decide, quién puede "
            "vetar, qué necesita cada uno y dónde se va a romper el consenso interno. El vendedor rara vez "
            "está presente cuando se toma la decisión; lo que circula en su ausencia es el material que dejó.",
        ],
        dia=[
            "**Preparación de reuniones:** investigar antes, formular una hipótesis del problema y llegar con "
            "preguntas, no con una presentación.",
            "**Discovery:** conversaciones donde el cliente habla más que tú y donde sale una cifra que él "
            "mismo estima.",
            "**Trabajo de comité:** conseguir acceso a quien controla el presupuesto y preparar al campeón "
            "con material que pueda defender sin ti.",
            "**Propuestas:** documentos con alcance, exclusiones y supuestos explícitos, porque lo omitido se "
            "cobra después en implementación o en reclamo.",
            "**Higiene de pipeline:** registrar evidencia de avance y cerrar lo que no va a ocurrir. Un "
            "pipeline honesto vale más que uno grande.",
        ],
        tecnico=[
            "**Discovery estructurado.** Situación, problema, implicación y beneficio, con el costo de no "
            "actuar cuantificado por el cliente.",
            "**Calificación rigurosa.** Criterios verificables con evidencia registrada; descalificar temprano "
            "es parte del trabajo.",
            "**Mapa de comité.** Usuario, comprador económico, veto técnico y campeón, con su postura y su "
            "criterio de decisión.",
            "**Negociación preparada.** Intereses, alternativa fuera de la mesa, punto de retirada, criterios "
            "objetivos y concesiones decrecientes con contrapartida.",
            "**Propuesta como documento contractual.** Alcance, exclusiones, supuestos y vigencia; en Chile, "
            "lo ofrecido por escrito obliga.",
            "**Traspaso a implementación.** Documentar lo prometido: el mayor punto de fuga del churn "
            "temprano está aquí.",
        ],
        herramientas=(
            "CRM:              Salesforce, HubSpot, Pipedrive\n"
            "Calificación:     MEDDPICC o equivalente con evidencia registrada\n"
            "Propuestas:       plantilla estándar con alcance y exclusiones\n"
            "Conversaciones:   grabación con consentimiento y análisis\n"
            "Planificación:    plan mutuo acordado con el cliente"
        ),
        blandas=[
            "**Escuchar más de lo que se habla.** Si el vendedor ocupa el 78 % del tiempo de la primera "
            "reunión, no hubo diagnóstico.",
            "**Tolerar el silencio.** La pregunta incómoda seguida de silencio produce más información que "
            "cualquier argumento.",
            "**Honestidad en el forecast.** Comprometer un negocio sin evidencia genera decisiones de "
            "contratación equivocadas.",
            "**Sostener el precio con criterio.** Ceder margen bajo presión de cierre crea un precedente que "
            "el gremio conoce.",
        ],
        ruta=[
            ("01", "el sistema comercial: dónde empieza y termina tu responsabilidad"),
            ("02", "cliente, roles y objeciones antes de comprar"),
            ("08", "**la base**: proceso comercial reproducible de punta a punta"),
            ("09", "**el núcleo**: venta consultiva, comité de compra y calificación"),
            ("10", "negociación con preparación, no con improvisación"),
            ("16", "CRM, etapas y forecast: la parte administrativa que sostiene el número"),
            ("18", "qué pasa después de la firma, para no vender lo que produce churn"),
        ],
        clases=[
            ("08", "04", "Discovery: la cifra que el cliente estima y que ancla todo lo demás"),
            ("09", "02", "SPIN Selling: la progresión que la evidencia respalda"),
            ("09", "07", "Comité de compra: dónde se rompe el consenso interno"),
            ("09", "08", "Champion y comprador económico: el error de calificación más caro"),
            ("10", "03", "BATNA: la fuente real de poder en una negociación"),
            ("10", "06", "Concesiones: por qué la secuencia creciente destruye margen"),
            ("08", "12", "Handoff a implementación: el punto de fuga que produce churn temprano"),
        ],
        labs=["08", "09", "10"],
        artefactos=[
            "Playbook comercial con etapas y criterios de salida verificables",
            "Deal review completo con calificación evidenciada y plan mutuo",
            "Carpeta de negociación con BATNA, ZOPA y concesiones planificadas",
            "Propuesta estándar con alcance, exclusiones y supuestos",
        ],
        credenciales=[
            "**No hay certificación que pese en este rol.** Lo que se evalúa es una simulación de discovery "
            "y un caso de negociación.",
            "**Portafolio** — un deal review con evidencia y una carpeta de negociación completa demuestran "
            "método mejor que cualquier curso.",
        ],
        progresion=(
            "Ejecutivo → ejecutivo senior o de cuentas estratégicas → **jefatura comercial** → "
            "[VP de ventas](vp-sales.md) y [CRO](cro.md). Salida lateral frecuente: "
            "[customer success](customer-success.md) si te atrae la relación de largo plazo."
        ),
        salario=SALARIO_MEDIO,
        mitos=[
            ("«Vender es convencer.»",
             "En venta compleja, convencer sin diagnóstico produce clientes que no obtienen valor y se van."),
            ("«El cierre es una técnica.»",
             "El cierre es la consecuencia de haber resuelto problema, valor, riesgo y proceso. Si hace falta "
             "técnica, faltó trabajo antes."),
            ("«Hay que hablar con quien te atienda.»",
             "El entusiasmo de un contacto sin presupuesto es la causa más común de negocios estancados."),
            ("«El descuento salva el trimestre.»",
             "Crea un precedente que el gremio aprende. El descuento de cierre de mes se vuelve la "
             "expectativa del próximo."),
        ],
        honestidad=(
            "El programa entrega método, guiones y criterio. No entrega la resistencia de sostener un número "
            "trimestre a trimestre ni la lectura de sala que sólo dan las conversaciones reales. Practica el "
            "discovery con personas reales, aunque sea en un proyecto propio, y graba con consentimiento."
        ),
    ),
    # ------------------------------------------------------------------ 07
    dict(
        slug="customer-success",
        emoji="🔁",
        titulo="Customer Success Manager",
        familia="Retención",
        resumen=(
            "Responsable de que el cliente obtenga el resultado por el que pagó, y de que ese resultado quede "
            "acreditado. No es soporte con otro nombre: soporte es reactivo y resuelve incidencias; éxito de "
            "cliente es proactivo y responde por la renovación."
        ),
        nivel="Intermedio; se entra desde soporte, desde ventas o desde la operación del propio cliente",
        foco="Onboarding, tiempo hasta el primer valor, salud de cuenta, renovación y expansión",
        credencial="Un sistema de retención con puntaje de salud validado contra bajas reales",
        que_es=[
            "En modelos recurrentes la venta no termina en la firma: ahí empieza el periodo en que el cliente "
            "decide si el gasto se justifica. Customer success es la función que garantiza que alcance el "
            "resultado comprometido y que esa evidencia quede registrada.",
            "El indicador que más pesa es el tiempo hasta el primer valor. Cada día adicional aumenta la "
            "probabilidad de que el cliente pierda impulso o cambie de prioridad. Reducirlo suele exigir "
            "decisiones incómodas: eliminar pasos de configuración o asumir parte del trabajo inicial.",
            "El rol tiene una frontera que conviene reconocer: no puede compensar un producto que no resuelve "
            "el problema ni una venta que prometió lo que no existe. Cuando el churn se concentra en un "
            "segmento, el diagnóstico casi siempre está en la oferta o en la calificación comercial.",
        ],
        dia=[
            "**Revisión de salud de cartera:** qué cuentas cambiaron de estado y cuáles requieren "
            "intervención hoy.",
            "**Onboarding activo:** acompañar a las cuentas nuevas hasta el primer resultado verificable, que "
            "es donde se decide la retención.",
            "**Conversaciones de valor:** mostrar con datos qué obtuvo el cliente, no preguntar si está "
            "contento.",
            "**Ciclo de renovación:** trabajarlo con noventa días de anticipación, no la semana del "
            "vencimiento.",
            "**Voz de cliente:** enrutar los hallazgos a quien puede modificar el producto o el proceso, y "
            "cerrar el circuito con quien los reportó.",
        ],
        tecnico=[
            "**Resultado deseado del cliente.** Expresado en la métrica del cliente y no en la del proveedor.",
            "**Diseño de onboarding.** El camino más corto al primer resultado, eliminando todo lo que no "
            "conduzca a él.",
            "**Puntaje de salud validado.** Construido desde el análisis de las cuentas perdidas y "
            "contrastado contra bajas reales, no desde la percepción del equipo.",
            "**Análisis de cohortes y churn.** Distinguir churn de clientes de churn de ingreso; analizar por "
            "cohorte de incorporación.",
            "**Renovación y expansión.** Expansión sólo sobre cuentas con resultado acreditado; vender más a "
            "una base insatisfecha adelanta ingreso y multiplica el churn.",
            "**Reducción de esfuerzo.** La evidencia muestra que reducir fricción retiene más que sorprender.",
        ],
        herramientas=(
            "Plataformas CS:   herramientas de salud de cuenta y ciclos de renovación\n"
            "Datos de uso:     analítica de producto y eventos de activación\n"
            "CRM:              historial comercial y contexto de la venta\n"
            "Encuestas:        NPS, CSAT y esfuerzo, con cierre de circuito\n"
            "Documentación:    planes de éxito y evidencia de resultado"
        ),
        blandas=[
            "**Conversación difícil sin evasión.** Un cliente frustrado necesita una persona, no una "
            "respuesta automática.",
            "**Priorización de cartera.** No todas las cuentas pueden atenderse igual; el modelo de cobertura "
            "es una decisión, no una omisión.",
            "**Traducción entre cliente y producto.** El hallazgo tiene que llegar a quien puede actuar.",
            "**Firmeza comercial.** Decir que una cuenta no está lista para expandir es parte del trabajo.",
        ],
        ruta=[
            ("02", "resultados deseados del cliente y fricciones"),
            ("05", "la oferta y su promesa: lo que tendrás que sostener después"),
            ("18", "**el núcleo completo**: onboarding, salud, churn, renovación y expansión"),
            ("20", "cohortes, retención y valor de vida con rigor"),
            ("16", "CRM y registro: sin dato no hay gestión de cartera"),
            ("21", "IA en éxito de cliente, con el límite de no automatizar la conversación de riesgo"),
        ],
        clases=[
            ("18", "02", "Onboarding: producir un resultado, no enseñar funcionalidades"),
            ("18", "03", "Time to value: el indicador más predictivo de retención"),
            ("18", "05", "Health score: construido desde las cuentas perdidas y validado"),
            ("18", "07", "Churn: de clientes y de ingreso son cosas distintas"),
            ("18", "10", "Renovación: noventa días de anticipación, no una semana"),
            ("18", "11", "Expansión legítima: resultado acreditado como requisito"),
            ("21", "11", "IA en customer success: qué automatizar y qué mantener humano"),
        ],
        labs=["18", "20"],
        artefactos=[
            "Sistema de retención y expansión con responsables por cartera",
            "Puntaje de salud con validación predictiva documentada",
            "Diseño de onboarding con tiempo hasta el primer valor medido",
            "Ciclo de renovación con evidencia de resultado por cuenta",
        ],
        credenciales=[
            "**Formaciones de plataformas CS** — útiles para la herramienta, no para el criterio.",
            "**Portafolio** — un puntaje de salud validado contra bajas reales es el artefacto que más "
            "distingue a un candidato en este rol.",
        ],
        progresion=(
            "CSM → CSM senior o de cuentas estratégicas → **head of customer success** → [CRO](cro.md). "
            "Salidas laterales frecuentes: [product marketing](product-marketing.md), por el conocimiento "
            "profundo del cliente, o [RevOps](revops.md)."
        ),
        salario=SALARIO_MEDIO,
        mitos=[
            ("«Es soporte con otro nombre.»",
             "Soporte responde cuando el cliente escribe. Éxito de cliente actúa antes y responde por la "
             "renovación."),
            ("«Se mide por tickets resueltos.»",
             "Se mide por resultado acreditado y por ingreso neto retenido. Los tickets miden actividad."),
            ("«Hay que sorprender al cliente.»",
             "La evidencia muestra que reducir el esfuerzo retiene más que el deleite. Primero elimina "
             "fricción."),
            ("«Retener es responsabilidad de CS.»",
             "Si el churn se concentra en un segmento, la causa suele estar en la calificación comercial o en "
             "el producto."),
        ],
        honestidad=(
            "El programa entrega el sistema completo y el rigor de cohortes. Lo que no puede darte es la "
            "conversación con un cliente que lleva dos semanas sin poder facturar. Ese músculo se construye "
            "en operación real."
        ),
    ),
    # ------------------------------------------------------------------ 08
    dict(
        slug="revops",
        emoji="⚙️",
        titulo="RevOps / Sales Operations",
        familia="Operación de ingresos",
        resumen=(
            "Quien hace que marketing, ventas y éxito de cliente funcionen como un solo sistema. Su valor no "
            "está en producir más informes sino en que las decisiones dejen de discutirse sobre cifras que "
            "nadie puede reconciliar."
        ),
        nivel="Intermedio a senior; suele venir de analítica, de ventas o de administración de CRM",
        foco="Modelo de datos, pipeline, forecast, automatización gobernada y acuerdos entre áreas",
        credencial="Un operating model donde cada indicador tiene una cifra única con su definición",
        que_es=[
            "RevOps existe porque los sistemas de marketing, ventas y servicio evolucionaron por separado y "
            "produjeron tres versiones incompatibles de la verdad. El síntoma clásico: marketing informa 300 "
            "leads, ventas trabaja 60 y la reunión mensual se consume discutiendo cuál cifra es la real.",
            "El trabajo tiene dos capas. La visible es la técnica: configurar el CRM, diseñar el pipeline, "
            "construir automatizaciones e integraciones. La invisible y más difícil es la de acuerdos: lograr "
            "que dos áreas con incentivos distintos usen la misma definición de lead calificado.",
            "Es un rol de apalancamiento silencioso. Nadie felicita a quien evitó que el forecast se "
            "construyera sobre un pipeline con 44 % de oportunidades sin actividad, pero esa corrección "
            "cambia decisiones de contratación y de presupuesto.",
        ],
        dia=[
            "**Higiene de datos:** duplicados, campos críticos incompletos, oportunidades sin actividad y "
            "etapas sin evidencia.",
            "**Monitoreo de integraciones:** si el flujo entre CRM y facturación se detuvo, hay que saberlo "
            "hoy y no cuando reclame un cliente.",
            "**Preparación de forecast:** consolidar ingreso nuevo, renovación, expansión y contracción, y "
            "reportar la precisión histórica junto a la proyección.",
            "**Gobierno de cambios:** aprobar o rechazar modificaciones de configuración con procedimiento y "
            "registro.",
            "**Acuerdos entre áreas:** medir el cumplimiento del acuerdo de servicio y llevar el dato a la "
            "conversación, no la opinión.",
        ],
        tecnico=[
            "**Modelo de datos de ingresos.** Entidades, estados válidos, fuente autoritativa por dato y "
            "jerarquía de cuentas.",
            "**Diseño de pipeline.** Etapas por evidencia del cliente, criterios de salida verificables y "
            "probabilidades calculadas con datos históricos.",
            "**Forecast unificado.** Ingreso nuevo, renovación, expansión y contracción modelados por "
            "separado, con precisión medida por componente.",
            "**Automatización gobernada.** Documentación, prueba controlada, responsable y capacidad de "
            "detención inmediata.",
            "**Observabilidad.** Indicadores de salud por proceso; enterarse de las fallas por reclamo es la "
            "forma más cara de enterarse.",
            "**Cumplimiento de datos.** Base de licitud, retención, eliminación efectiva y registro del "
            "tratamiento.",
        ],
        herramientas=(
            "CRM:              Salesforce, HubSpot (administración avanzada)\n"
            "Automatización:   flujos, enrutamiento, lifecycle stages\n"
            "Datos:            SQL, herramientas de integración, conciliación\n"
            "Reporte:          tableros operativos y de dirección\n"
            "Gobierno:         procedimiento de cambio y registro de configuración"
        ),
        blandas=[
            "**Mediar entre áreas con incentivos opuestos.** El acuerdo de servicio es una negociación "
            "permanente, no un documento.",
            "**Resistir la petición de más campos.** Cada campo obligatorio adicional degrada la calidad del "
            "conjunto.",
            "**Explicar la diferencia entre dos cifras** sin que ninguna área quede como culpable.",
            "**Documentar.** Un sistema sin registro de por qué está configurado así se vuelve inmanejable en "
            "dos años.",
        ],
        ruta=[
            ("01", "el motor de ingresos completo, que es exactamente el objeto del rol"),
            ("16", "**el núcleo operativo**: CRM, pipeline, forecast, cuotas y capacidad"),
            ("17", "**el núcleo de integración**: lifecycle, scoring, SLA, datos y observabilidad"),
            ("20", "analítica: definiciones, cohortes y coherencia aritmética"),
            ("18", "retención y renovación, la mitad del forecast que suele estimarse a ojo"),
            ("23", "dirección comercial: para hablar el idioma de quien recibe tus informes"),
        ],
        clases=[
            ("16", "03", "Etapas y criterios de salida: la evidencia del cliente, no la intención propia"),
            ("16", "07", "Forecast: método declarado y sesgo corregido"),
            ("17", "07", "Acuerdo de servicio entre marketing y ventas: la definición compartida"),
            ("17", "08", "Modelo de datos: fuente autoritativa por dato"),
            ("17", "12", "Calidad y observabilidad: no enterarse por reclamo"),
            ("17", "13", "Gobernanza de automatizaciones: poder explicar qué hizo el sistema"),
            ("16", "05", "Higiene de datos: degradación, deduplicación y retención"),
        ],
        labs=["16", "17"],
        artefactos=[
            "Diseño de sales operations con pipeline, criterios y gobierno",
            "Operating model de RevOps con cifra única por indicador",
            "Acuerdo de servicio entre marketing y ventas con cumplimiento medido",
            "Modelo de datos con fuente autoritativa declarada por campo",
        ],
        credenciales=[
            "**Salesforce Administrator / HubSpot Operations** — sí pesan en este rol, porque acreditan "
            "operación real de la plataforma.",
            "**SQL** — no hay credencial, pero se evalúa en entrevista.",
            "**Portafolio** — un modelo de datos y un diseño de pipeline documentados demuestran criterio.",
        ],
        progresion=(
            "Sales ops o marketing ops → **RevOps manager** → head of revenue operations → [CRO](cro.md) o "
            "dirección de operaciones. Es uno de los caminos más directos hacia la dirección comercial para "
            "perfiles no vendedores."
        ),
        salario=SALARIO_MEDIO,
        mitos=[
            ("«Es administrar el CRM.»",
             "Administrar la herramienta es el 30 %. El resto son definiciones, acuerdos y gobierno."),
            ("«Más automatización es mejor.»",
             "Automatizar un proceso desordenado produce desorden a escala. Primero estandarizar."),
            ("«El forecast es un cálculo.»",
             "Es consecuencia de la disciplina de calificación. Ningún método corrige criterios de etapa "
             "débiles."),
            ("«Los conflictos entre áreas se arreglan con datos.»",
             "Los datos hacen visible el conflicto de incentivos; resolverlo exige cambiar la compensación."),
        ],
        honestidad=(
            "El programa entrega el diseño completo del sistema. No entrega experiencia administrando una "
            "instancia real de Salesforce o HubSpot con miles de registros, que es lo que muchas ofertas "
            "piden. Complementa con la certificación de administrador de la plataforma que uses."
        ),
    ),
    # ------------------------------------------------------------------ 09
    dict(
        slug="performance-marketer",
        emoji="📈",
        titulo="Performance marketer / Media buyer",
        familia="Adquisición",
        resumen=(
            "Quien invierte presupuesto en medios pagados y responde por lo que ese dinero produce. El rol "
            "vive de una tensión: la plataforma reporta un retorno y el negocio necesita saber cuánto de eso "
            "es incremental."
        ),
        nivel="Entrada a intermedio; es de los roles con curva de aprendizaje más rápida y techo alto",
        foco="Subastas, estructura de campañas, creatividades, medición y control de riesgo",
        credencial="Una prueba de incrementalidad ejecutada sobre el canal que concentra el gasto",
        que_es=[
            "La publicidad digital se asigna en subastas donde no gana quien más paga sino quien combina "
            "oferta y relevancia. Entender eso cambia la gestión: mejorar la correspondencia entre término, "
            "anuncio y página reduce el costo tanto o más que subir la oferta.",
            "El trabajo tiene una parte operativa —estructurar cuentas, escribir anuncios, controlar "
            "exclusiones, vigilar el ritmo de gasto— y una parte de criterio que es la que se paga: "
            "distinguir el resultado que la campaña produjo del que habría ocurrido igual.",
            "Es un rol donde los errores son caros y rápidos. Una cuenta sin lista de exclusiones puede "
            "consumir el 38 % del presupuesto en búsquedas irrelevantes, y un retorno reportado que incluye "
            "clientes existentes puede sostener una decisión de escalar equivocada durante meses.",
        ],
        dia=[
            "**Revisión de gasto y ritmo:** que el presupuesto no se agote en la primera semana ni quede sin "
            "ejecutar.",
            "**Informe de términos de búsqueda:** excluir lo irrelevante. Es la tarea más rentable y la que "
            "más se posterga.",
            "**Rotación de creatividades:** vigilar la frecuencia de exposición y renovar antes de la caída "
            "de desempeño, no después.",
            "**Conciliación con el CRM:** las plataformas reportan más conversiones de las que registra el "
            "negocio; la diferencia se documenta.",
            "**Decisiones de asignación:** mover presupuesto sólo cuando la señal supera el rango de "
            "variación normal.",
        ],
        tecnico=[
            "**Mecánica de subasta.** Oferta, relevancia y calidad estimada; por qué subir la oferta sin "
            "mejorar relevancia encarece el resultado.",
            "**Estructura por intención.** Organizar campañas según lo que busca el usuario y no según el "
            "catálogo de productos.",
            "**Economía de la campaña.** Costo por oportunidad calificada y por cliente ganado; CPA, CAC y "
            "ROAS son tres cosas distintas.",
            "**Incrementalidad.** Diseñar una prueba de suspensión cuando el gasto lo justifica.",
            "**Creatividad con método.** Concepto, variantes, activos distintivos de marca y control de "
            "fatiga.",
            "**Riesgo.** Tráfico no válido, seguridad de marca, consentimiento y uso lícito de bases propias.",
        ],
        herramientas=(
            "Plataformas:      Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads\n"
            "Medición:         analítica web, conciliación con CRM\n"
            "Creatividad:      producción de variantes y control de frecuencia\n"
            "Conversión:       páginas de destino y pruebas A/B\n"
            "Control:          listas de exclusión, informes de calidad de tráfico"
        ),
        blandas=[
            "**Escepticismo con las cifras propias.** El sesgo natural del rol es creerle a la plataforma que "
            "vende el espacio.",
            "**Disciplina para no intervenir.** Cambiar ofertas tres veces por semana impide que cualquier "
            "variación se atribuya a una causa.",
            "**Explicar un mal resultado sin excusas.** El presupuesto se defiende con método, no con "
            "optimismo.",
            "**Curiosidad por el negocio.** Sin entender el margen y el ciclo, no se puede fijar un costo por "
            "resultado admisible.",
        ],
        ruta=[
            ("01", "el sistema comercial: para saber qué costo por resultado es admisible"),
            ("12", "estrategia digital, conversión y plan de medición"),
            ("14", "**el núcleo**: subastas, campañas, creatividades, medición y riesgo"),
            ("13", "copywriting: el anuncio y la página son texto antes que diseño"),
            ("20", "analítica: atribución, incrementalidad y economía unitaria"),
            ("15", "comercio digital, si el destino es e-commerce"),
        ],
        clases=[
            ("14", "01", "Medios pagados y subastas: por qué la relevancia baja el costo"),
            ("14", "02", "Objetivos de campaña: optimizar y evaluar por lo mismo"),
            ("14", "09", "CTR, CPC y CPM: métricas de diagnóstico, no de decisión"),
            ("14", "10", "CPA, CAC y ROAS: la confusión más cara del área"),
            ("14", "12", "Optimización: variación común frente a variación especial"),
            ("14", "13", "Fraude, brand safety y privacidad: controles previos"),
            ("20", "09", "Incrementalidad: qué habría pasado sin la inversión"),
        ],
        labs=["14", "12"],
        artefactos=[
            "Plan de performance con umbrales de decisión y contingencias",
            "Auditoría de cuenta con gasto irrelevante identificado y excluido",
            "Conciliación plataforma-CRM con diferencia documentada",
            "Prueba de incrementalidad con efecto estimado e intervalo",
        ],
        credenciales=[
            "**Google Ads** y **Meta Blueprint** — sí importan en este rol para pasar filtros; son gratuitas "
            "o baratas y se renuevan.",
            "**Portafolio** — una cuenta real gestionada con su economía documentada pesa mucho más.",
        ],
        progresion=(
            "Media buyer → performance manager → **[head of growth](growth-manager.md)** o dirección de "
            "adquisición. También es rampa hacia [analítica](analista-de-marketing.md) para quien disfruta "
            "la parte de medición."
        ),
        salario=SALARIO_ENTRADA,
        mitos=[
            ("«El ROAS que reporta la plataforma es el retorno.»",
             "Incluye conversiones que habrían ocurrido igual. Sin prueba de incrementalidad, es una "
             "estimación optimista por construcción."),
            ("«Subir la oferta trae más volumen.»",
             "Encarece el resultado si la relevancia no mejora. Primero se revisa la correspondencia."),
            ("«Hay que testear todo el tiempo.»",
             "Sin muestra suficiente, un test produce conclusiones falsas con apariencia de rigor."),
            ("«Es un rol técnico de plataforma.»",
             "La plataforma se aprende en semanas. Lo que distingue es el criterio económico y la honestidad "
             "de la medición."),
        ],
        honestidad=(
            "El programa entrega criterio económico, método de medición y control de riesgo. No entrega horas "
            "de operación de cuenta, que es lo que más pesa al postular. Gestiona una cuenta real, aunque sea "
            "con presupuesto pequeño, y documenta la economía completa."
        ),
    ),
    # ------------------------------------------------------------------ 10
    dict(
        slug="content-manager",
        emoji="✍️",
        titulo="Content manager / Copywriter comercial",
        familia="Adquisición",
        resumen=(
            "Quien produce los mensajes que informan, mueven a la acción y resisten el escrutinio. El oficio "
            "no es escribir bonito: es que un desconocido entienda, crea y actúe, sin afirmar nada que la "
            "empresa no pueda sostener."
        ),
        nivel="Entrada a intermedio; se entra desde periodismo, letras, marketing o desde el propio rubro",
        foco="Estrategia editorial, copywriting, control de afirmaciones y testing de mensajes",
        credencial="Un sistema editorial con control de afirmaciones aplicado",
        que_es=[
            "El contenido comercial tiene dos fracasos típicos y opuestos. Uno es publicar sobre lo que "
            "interesa a la empresa —tendencias, novedades, cultura interna— y construir un archivo que nadie "
            "lee. El otro es publicar sólo promoción y agotar la atención de la audiencia.",
            "La salida es aburrida y efectiva: responder las preguntas que aparecen en las llamadas de venta, "
            "con el vocabulario que usa el cliente. Ese material sirve para atraer, para vender y para "
            "reducir consultas de soporte.",
            "El copywriting comercial agrega una exigencia que la escritura creativa no tiene: cada "
            "afirmación cuantitativa o comparativa necesita respaldo. En Chile, la información al consumidor "
            "debe ser veraz y comprobable, y un caso de éxito publicado sin autorización ni base de cálculo "
            "es un riesgo real.",
        ],
        dia=[
            "**Escucha:** revisar llamadas de venta y tickets de soporte para encontrar las preguntas que se "
            "repiten.",
            "**Producción:** escribir, editar y eliminar. Editar es sobre todo quitar lo que no ayuda al "
            "lector a decidir.",
            "**Control de afirmaciones:** verificar el respaldo de cada cifra o comparación antes de "
            "publicar.",
            "**Testing:** probar titulares y llamados a la acción con criterio previo y una variable por vez.",
            "**Mantenimiento:** actualizar contenido que envejeció. El contenido normativo o de producto "
            "caduca y desactualizado hace daño.",
        ],
        tecnico=[
            "**Pilares de contenido.** Tres temas donde la empresa tiene autoridad real y conexión con lo que "
            "vende; el resto se descarta por escrito.",
            "**Estructuras persuasivas.** AIDA y PAS como listas de verificación, no como fórmulas; con el "
            "límite de que la agitación debe usar consecuencias verificables.",
            "**Características, beneficios y prueba.** Descartar los beneficios que cualquier competidor "
            "podría afirmar.",
            "**Titulares.** Específicos, relevantes y honestos; el clickbait produce apertura y destruye la "
            "apertura siguiente.",
            "**Copy de conversión.** Jerarquía informativa según las preguntas reales del visitante, con la "
            "objeción dominante respondida en página.",
            "**Cumplimiento.** Autorización de testimonios, base de cálculo de toda cifra y respeto del "
            "consentimiento en correo.",
        ],
        herramientas=(
            "Investigación:    grabaciones de venta, tickets, búsquedas internas\n"
            "SEO:              intención de búsqueda, arquitectura de contenido\n"
            "Publicación:      CMS, calendario editorial, guía de estilo\n"
            "Correo:           plataformas de envío con segmentación\n"
            "Testing:          pruebas de titular y de llamado a la acción"
        ),
        blandas=[
            "**Escribir para el lector y no para el jefe.** La aprobación interna y la efectividad rara vez "
            "coinciden.",
            "**Aceptar la edición.** El primer borrador siempre sobra en un tercio.",
            "**Rigor con las fuentes.** Una cifra sin origen no se publica, aunque suene bien.",
            "**Constancia.** El contenido compone con el tiempo; publicar tres meses y abandonar no produce "
            "nada.",
        ],
        ruta=[
            ("02", "cliente, objeciones y vocabulario real"),
            ("04", "posicionamiento: el criterio que ordena qué se dice y qué no"),
            ("13", "**el núcleo completo**: estrategia editorial, copywriting y testing"),
            ("12", "digital: sitio, landing pages, SEO y conversión"),
            ("06", "marca: identidad verbal y coherencia"),
            ("14", "publicidad: el copy que se paga por mostrar"),
        ],
        clases=[
            ("13", "02", "Pilares de contenido: qué se descarta y por qué"),
            ("13", "05", "Características frente a beneficios: descartar lo genérico"),
            ("13", "06", "Titulares: optimizar apertura y permanencia, no sólo clics"),
            ("13", "08", "Copy de landing page: responder la objeción dominante"),
            ("13", "12", "Prueba social: similitud del referente y transparencia del incentivo"),
            ("13", "14", "Sistema editorial: control de afirmaciones antes de publicar"),
            ("12", "04", "SEO: intención de búsqueda antes que volumen"),
        ],
        labs=["13", "12"],
        artefactos=[
            "Sistema editorial con pilares, calendario y guía de estilo",
            "Biblioteca de piezas con control de afirmaciones documentado",
            "Página de conversión con objeciones respondidas y prueba de comprensión",
            "Registro de pruebas de mensaje con criterio previo",
        ],
        credenciales=[
            "**No hay certificación que pese.** Se evalúa con una prueba de escritura y con el portafolio.",
            "**Portafolio** — tres piezas con resultado medido y la explicación de qué cambiaste tras el "
            "primer test valen más que cualquier curso de copywriting.",
        ],
        progresion=(
            "Copywriter o content manager → **head of content** → [marketing manager](marketing-manager.md) "
            "o [product marketing](product-marketing.md). Muchos derivan a consultoría independiente, donde "
            "el portafolio y el rubro de especialización determinan la tarifa."
        ),
        salario=SALARIO_ENTRADA,
        mitos=[
            ("«Escribir bien es suficiente.»",
             "Escribir bien sobre el tema equivocado produce un archivo, no demanda."),
            ("«El contenido no se puede medir.»",
             "Se mide por uso en ventas, por demanda originada y por reducción de consultas repetidas."),
            ("«Hay que publicar todos los días.»",
             "La constancia importa más que la frecuencia. Un ritmo sostenible durante años supera a tres "
             "meses intensos."),
            ("«La IA reemplaza este rol.»",
             "Acelera la producción y multiplica el riesgo de afirmaciones sin respaldo. El control de "
             "afirmaciones se vuelve más necesario, no menos."),
        ],
        honestidad=(
            "El programa entrega método editorial, estructura persuasiva y control de cumplimiento. La voz "
            "propia y el oficio de editar se construyen escribiendo mucho y recibiendo crítica. Publica con "
            "regularidad en algún espacio propio."
        ),
    ),
    # ------------------------------------------------------------------ 11
    dict(
        slug="ecommerce-manager",
        emoji="🛒",
        titulo="E-commerce manager",
        familia="Adquisición",
        resumen=(
            "Responsable de una operación de venta digital completa: catálogo, conversión, pagos, "
            "cumplimiento logístico, postventa y —sobre todo— de que cada pedido deje margen después de "
            "comisión, despacho y devolución."
        ),
        nivel="Intermedio; combina marketing, operación y economía unitaria",
        foco="Conversión, economía por pedido, marketplaces, postventa y cumplimiento al consumidor",
        credencial="Un modelo económico de tienda con análisis de sensibilidad",
        que_es=[
            "Vender en línea es una operación logística y financiera antes que una vitrina. La mayoría de los "
            "emprendimientos digitales que fracasan no tenía un problema de tráfico: tenía un costo por "
            "pedido superior a su margen y no lo sabía.",
            "El rol exige moverse entre planos muy distintos en el mismo día: por qué el checkout pierde 63 % "
            "en el paso de despacho, por qué el marketplace representa el 28 % de las unidades y el 4 % del "
            "margen, y qué dice la normativa sobre el derecho a retracto de la venta que se acaba de hacer.",
            "En Chile hay un frente que no es opcional: información al consumidor, derecho a retracto en "
            "venta a distancia y garantía legal. Una condición publicada que restrinja derechos reconocidos "
            "por ley es inoponible y expone a sanción.",
        ],
        dia=[
            "**Revisión de conversión por paso:** dónde se pierde el pedido, segmentado por dispositivo y por "
            "origen.",
            "**Economía por pedido:** verificar margen real después de comisión, despacho, empaque, pasarela "
            "y devoluciones.",
            "**Catálogo:** completar atributos, corregir búsquedas internas sin resultado y ajustar el "
            "destacado por margen y disponibilidad.",
            "**Operación:** cumplimiento de plazos prometidos e incidencias logísticas por zona.",
            "**Postventa:** devoluciones, garantías y causas raíz. Cada devolución por incompatibilidad es un "
            "defecto de la ficha de producto.",
        ],
        tecnico=[
            "**Economía por pedido.** Contribución después de todos los costos variables, por producto y por "
            "canal.",
            "**Conversión digital.** Embudo por etapa, prioridad por pérdida absoluta y no por peor "
            "porcentaje.",
            "**Checkout y pagos.** Costos revelados temprano, medios de pago del segmento, tasa de aprobación "
            "y calibración antifraude sin falsos rechazos.",
            "**Marketplaces.** Comisión efectiva total, pérdida de relación con el cliente y dependencia del "
            "canal.",
            "**Cumplimiento logístico.** Prometer el plazo que se cumple en el 95 % de los casos, no el mejor "
            "caso.",
            "**Normativa de consumo.** Retracto, garantía legal, información previa y condiciones que no "
            "pueden restringir derechos.",
        ],
        herramientas=(
            "Plataforma:       Shopify, WooCommerce, VTEX, Magento\n"
            "Marketplaces:     integraciones y gestión de catálogo\n"
            "Analítica:        embudos, mapas de calor, pruebas A/B\n"
            "Pagos:            pasarelas, conciliación y contracargos\n"
            "Logística:        seguimiento de plazos e incidencias por zona"
        ),
        blandas=[
            "**Obsesión por el margen y no por la venta.** Es la diferencia entre crecer y crecer perdiendo "
            "dinero.",
            "**Coordinación con operaciones.** La promesa comercial la cumple bodega, no marketing.",
            "**Tolerancia al detalle.** El rol se gana en atributos de catálogo y pasos de checkout.",
            "**Rigor normativo.** Las condiciones publicadas obligan; improvisarlas sale caro.",
        ],
        ruta=[
            ("15", "**el núcleo completo**: operación, catálogo, checkout, pagos, marketplaces y postventa"),
            ("12", "adquisición digital, conversión y medición del embudo completo"),
            ("07", "pricing y unit economics, sin lo cual la tienda no se evalúa"),
            ("20", "analítica: cohortes, recompra y contribución"),
            ("13", "copy de ficha de producto y de página de conversión"),
            ("18", "retención, si la categoría admite recompra"),
        ],
        clases=[
            ("15", "01", "Modelo operativo: el costo por pedido que casi nadie calcula completo"),
            ("15", "04", "Checkout: el costo sorpresa que produce 63 % de abandono"),
            ("15", "05", "Pagos: falsos rechazos frente a contracargos evitados"),
            ("15", "11", "Marketplaces: comisión efectiva y pérdida de relación"),
            ("15", "12", "Postventa: derechos del consumidor como requisito de diseño"),
            ("15", "14", "Simulación de tienda rentable: sensibilidad y variables críticas"),
            ("07", "12", "Unit economics: márgenes reales por segmento"),
        ],
        labs=["15", "12"],
        artefactos=[
            "Modelo económico de tienda con variables críticas identificadas",
            "Auditoría de checkout con pérdida por paso y correcciones priorizadas",
            "Análisis de canal con comisión efectiva y margen neto",
            "Revisión de cumplimiento de condiciones publicadas",
        ],
        credenciales=[
            "**Certificaciones de plataforma** (Shopify, VTEX) — útiles si el puesto exige esa herramienta.",
            "**Portafolio** — una tienda real con su economía documentada, aunque sea pequeña, es el "
            "argumento más fuerte.",
        ],
        progresion=(
            "E-commerce manager → **head of e-commerce** o dirección de canal digital → "
            "[CRO](cro.md) en empresas donde el canal digital es el negocio. Salida frecuente: "
            "[founder](founder.md) de tienda propia."
        ),
        salario=SALARIO_MEDIO,
        mitos=[
            ("«Con más tráfico se vende más.»",
             "Con margen negativo por pedido, más tráfico acelera la pérdida."),
            ("«El marketplace es un canal más.»",
             "Entrega tráfico y confianza a cambio de comisión, reglas y la relación con el cliente. Es una "
             "decisión estratégica."),
            ("«Las devoluciones son un costo inevitable.»",
             "Una parte importante son defectos de información: compatibilidad, medidas o expectativa."),
            ("«El retracto se puede limitar en las condiciones.»",
             "No. Una cláusula que restrinja derechos legales es inoponible y expone a sanción."),
        ],
        honestidad=(
            "El programa entrega la economía y el método de conversión. No entrega experiencia operando "
            "logística real con incidencias diarias. Si puedes, opera una tienda pequeña de punta a punta: "
            "aprenderás más de un mes de despachos que de cualquier curso."
        ),
    ),
    # ------------------------------------------------------------------ 12
    dict(
        slug="brand-manager",
        emoji="🎨",
        titulo="Brand manager",
        familia="Marketing",
        resumen=(
            "Responsable de que el mercado recuerde a la empresa cuando aparece la necesidad. Trabaja sobre "
            "un activo que se construye en años y se mide con incomodidad, en organizaciones que piden "
            "resultados trimestrales."
        ),
        nivel="Intermedio; suele venir de marketing, comunicación o diseño con criterio comercial",
        foco="Posicionamiento, activos distintivos, coherencia omnicanal y medición de marca",
        credencial="Un brand book operativo con sistema de medición y línea base",
        que_es=[
            "Una marca no es un logo: es la estructura de memoria que existe en la cabeza de las personas y "
            "que se activa cuando aparece una necesidad. Sharp y Romaniuk lo formularon en términos "
            "operativos —disponibilidad mental y física—, lo que convierte al branding en una inversión "
            "medible en lugar de un ejercicio estético.",
            "El trabajo central es la consistencia. Los activos distintivos funcionan por repetición "
            "sostenida; cambiar la identidad cada dos años destruye lo acumulado. La tarea más frecuente del "
            "rol es defender esa consistencia frente al aburrimiento interno, que siempre llega antes que el "
            "reconocimiento externo.",
            "Su tensión permanente es de horizonte. La activación produce resultado este mes; la construcción "
            "de marca reduce el costo de adquisición dentro de años. Binet y Field documentaron que las "
            "métricas de corto plazo sesgan el presupuesto hacia lo inmediato, y sostener el equilibrio con "
            "evidencia es parte del oficio.",
        ],
        dia=[
            "**Auditoría de coherencia:** revisar puntos de contacto reales —factura, correo de cobranza, "
            "atención— y no sólo las piezas de campaña.",
            "**Revisión de piezas:** verificar que respeten la declaración de posicionamiento y los activos "
            "distintivos.",
            "**Medición:** preparar o leer la ola de notoriedad y consideración, con método idéntico al "
            "anterior para que sea comparable.",
            "**Coordinación con agencias o diseño:** entregar criterio, no gusto personal.",
            "**Gestión de incidentes:** cuando algo sale mal públicamente, el orden es contener, reparar, "
            "comunicar y prevenir.",
        ],
        tecnico=[
            "**Disponibilidad mental y física.** Recuerdo ante la situación de compra y presencia donde el "
            "cliente decide.",
            "**Activos distintivos.** Elementos que el mercado asocia únicamente con la marca; medir su "
            "asociación antes de cambiarlos.",
            "**Identidad verbal.** Tono por contexto y vocabulario propio, con ejemplos de antes y después.",
            "**Arquitectura de marca.** Cuántas marcas se sostienen y qué cuesta construir cada una.",
            "**Medición.** Notoriedad espontánea, consideración y prima de precio, en olas comparables.",
            "**Accesibilidad y aplicabilidad.** Contraste suficiente y funcionamiento en los soportes reales, "
            "no sólo en la presentación.",
        ],
        herramientas=(
            "Investigación:    estudios de notoriedad y percepción por olas\n"
            "Identidad:        manual operativo, activos y reglas de aplicación\n"
            "Auditoría:        revisión de puntos de contacto y coherencia\n"
            "Producción:       coordinación con diseño y agencias\n"
            "Medición:         separación de tráfico de marca y genérico"
        ),
        blandas=[
            "**Defender la consistencia.** El equipo se aburre de la identidad mucho antes de que el mercado "
            "la recuerde.",
            "**Separar gusto de criterio.** «No me gusta» no es un argumento; «no funciona en pantalla de "
            "taller con luz directa» sí.",
            "**Explicar el largo plazo con datos.** Sin medición, la marca pierde toda discusión de "
            "presupuesto.",
            "**Serenidad ante incidentes.** La respuesta a un error propio define la reputación más que "
            "cualquier campaña.",
        ],
        ruta=[
            ("04", "posicionamiento y diferenciación: sin esto, la marca no tiene contenido"),
            ("06", "**el núcleo completo**: marca, identidad, arquitectura, medición y brand book"),
            ("13", "identidad verbal y relato con evidencia"),
            ("12", "coherencia omnicanal en el terreno digital"),
            ("20", "medición: separar el efecto de marca del de activación"),
        ],
        clases=[
            ("06", "01", "Qué es una marca: disponibilidad mental y física"),
            ("06", "02", "Identidad frente a imagen: la brecha es el diagnóstico"),
            ("06", "06", "Identidad visual: reconocimiento y accesibilidad, no gusto"),
            ("06", "09", "Brand equity: prima de precio y costo de adquisición"),
            ("06", "12", "Coherencia omnicanal: primero el dato único, después el mensaje"),
            ("06", "13", "Medición de marca: olas comparables y línea base"),
            ("06", "14", "Brand book mínimo viable: la prueba de producción"),
        ],
        labs=["06", "04"],
        artefactos=[
            "Brand book operativo con reglas de aplicación y prueba de producción",
            "Medición de notoriedad y consideración con línea base establecida",
            "Auditoría de coherencia omnicanal con incoherencias priorizadas",
            "Declaración de posicionamiento con criterio de rechazo aplicado",
        ],
        credenciales=[
            "**No hay certificación relevante.** El portafolio y la capacidad de argumentar decisiones son "
            "lo que se evalúa.",
            "**Portafolio** — un brand book con sistema de medición y una auditoría de coherencia demuestran "
            "criterio comercial, no sólo estético.",
        ],
        progresion=(
            "Brand manager → **head of brand** o [marketing manager](marketing-manager.md) → "
            "[CMO](cmo.md). En empresas de consumo el camino de marca es una vía directa a la dirección de "
            "marketing."
        ),
        salario=SALARIO_MEDIO,
        mitos=[
            ("«La marca es el logo.»",
             "El logo es un activo distintivo entre varios. La marca es la memoria que existe en el mercado."),
            ("«Hay que renovar la identidad cada cierto tiempo.»",
             "Cada renovación destruye activos acumulados. Se mide su asociación antes de tocarlos."),
            ("«La marca no se mide.»",
             "Se mide con notoriedad, consideración y prima de precio. Lo que no se puede es evaluarla como "
             "una campaña trimestral."),
            ("«Marca y performance compiten.»",
             "Compiten por presupuesto y se necesitan: la marca baja el costo de la activación futura."),
        ],
        honestidad=(
            "El programa entrega el marco empírico y el sistema de medición. Lo que no puede darte es "
            "presupuesto real de medios sostenido en el tiempo, que es donde la marca se construye. Documenta "
            "al menos una ola de medición propia, aunque sea con muestra pequeña."
        ),
    ),
    # ------------------------------------------------------------------ 13
    dict(
        slug="head-of-gtm",
        emoji="🗺️",
        titulo="Head of Go-To-Market",
        familia="Dirección",
        resumen=(
            "Quien decide cómo llega la oferta al mercado: qué segmento, qué movimiento comercial, qué "
            "canales y en qué secuencia. Su error más caro no es elegir mal un canal, sino abrir varios "
            "frentes con la capacidad de uno."
        ),
        nivel="Senior; exige haber ejecutado antes en marketing, ventas o producto",
        foco="Beachhead, movimiento comercial, canales, lanzamientos y expansión",
        credencial="Un plan GTM coherente con la capacidad real declarada",
        que_es=[
            "Una estrategia de salida al mercado responde cinco preguntas encadenadas: a quién servimos, qué "
            "le ofrecemos, cómo lo alcanzamos, cómo lo convertimos y cómo lo retenemos. No es un calendario "
            "de campañas: es la elección del movimiento comercial completo y de su economía.",
            "La incoherencia más frecuente es económica: atender con visitas en terreno a clientes cuyo "
            "contrato anual no cubre el costo del movimiento. La segunda es de capacidad: abrir una geografía "
            "nueva, un plan de autoservicio y un programa de socios el mismo año, con el mismo equipo.",
            "El rol exige decir que no con frecuencia. Cada frente abierto sin criterio de expansión consume "
            "atención de dirección, que es el recurso más escaso y el menos contabilizado. Abrir tres frentes "
            "con la capacidad de uno no triplica las opciones: garantiza llegar tarde a los tres y quedarse "
            "sin referencias en ninguno.",
        ],
        dia=[
            "**Revisión de eficiencia:** ingreso incremental frente a gasto incremental por movimiento. "
            "Crecer perdiendo eficiencia es una apuesta que alguien deberá pagar.",
            "**Coordinación de lanzamiento:** verificar listeza interna —ventas capacitada, soporte con "
            "documentación— antes de cualquier comunicación externa.",
            "**Gestión de canales:** medir socios activos y no acuerdos firmados; resolver conflictos de "
            "canal con reglas escritas.",
            "**Decisiones de expansión:** aplicar el criterio que autoriza abrir el siguiente frente, o "
            "posponerlo.",
            "**Alineamiento:** producto, marketing, ventas y operaciones deben compartir el mismo movimiento; "
            "si cada uno optimiza el suyo, el plan no existe.",
        ],
        tecnico=[
            "**Movimiento comercial y su economía.** Autoservicio, venta interna, terreno o socios: cada uno "
            "tiene un umbral de ticket bajo el cual no es viable.",
            "**Beachhead.** Elegir el segmento inicial por dominancia alcanzable y circulación de "
            "referencias, no por tamaño.",
            "**Economía de canales.** Costo total incluido el sostenimiento, margen retenido y velocidad de "
            "escalamiento.",
            "**Lanzamientos.** Criterios de listeza verificables y plan de reversión.",
            "**Expansión.** Geográfica y por segmento, con criterio de continuidad y de abandono definido "
            "antes de invertir.",
            "**Métricas de eficiencia.** Periodo de recuperación, productividad por movimiento y deterioro al "
            "escalar.",
        ],
        herramientas=(
            "Planificación:    modelos de economía por movimiento y por canal\n"
            "Coordinación:     planes de lanzamiento con criterios de listeza\n"
            "Canales:          programas de habilitación y reglas de conflicto\n"
            "Medición:         eficiencia del crecimiento por segmento\n"
            "Decisión:         criterios de expansión y de abandono escritos"
        ),
        blandas=[
            "**Decidir con información incompleta** y declarar qué la haría cambiar.",
            "**Sostener la secuencia.** La presión por abrir todos los frentes a la vez es constante y viene "
            "de arriba.",
            "**Coordinar sin autoridad directa** sobre producto, ventas y operaciones.",
            "**Reconocer un frente fallido a tiempo.** El criterio de abandono se define antes de invertir, "
            "no cuando ya duele.",
        ],
        ruta=[
            ("04", "segmentación y targeting: la base de cualquier elección de mercado"),
            ("05", "oferta y encaje producto-mercado, que define lo que se puede llevar al mercado"),
            ("22", "**el núcleo completo**: movimientos, canales, lanzamientos y expansión"),
            ("07", "pricing: la coherencia entre ticket y costo del movimiento"),
            ("23", "dirección comercial: presupuesto, objetivos y gobierno"),
            ("20", "métricas de eficiencia del crecimiento"),
        ],
        clases=[
            ("22", "01", "Qué es una estrategia GTM: coherencia entre ticket y movimiento"),
            ("22", "03", "Beachhead: dominancia alcanzable antes que tamaño"),
            ("22", "06", "Crecimiento liderado por socios: activos frente a acuerdos firmados"),
            ("22", "08", "Economía de canales: incluir el costo de sostenerlos"),
            ("22", "10", "Expansión geográfica: tratarla como mercado nuevo"),
            ("22", "13", "Métricas GTM: eficiencia además de crecimiento"),
            ("22", "14", "Plan GTM completo: la secuencia y el criterio de expansión"),
        ],
        labs=["22", "04"],
        artefactos=[
            "Plan go-to-market con movimiento justificado por economía",
            "Análisis de canales con costo total y margen retenido",
            "Plan de lanzamiento con criterios de listeza verificados",
            "Secuencia de expansión con criterio de apertura y de abandono",
        ],
        credenciales=[
            "**No hay certificación relevante.** Se evalúa por resultados previos y por la calidad del "
            "razonamiento en el caso de entrevista.",
            "**Portafolio** — un plan GTM con economía por movimiento y capacidad declarada.",
        ],
        progresion=(
            "Head of GTM → [CRO](cro.md) o dirección general. Es también un puesto habitual de transición "
            "para quien viene de [product marketing](product-marketing.md) o de "
            "[VP de ventas](vp-sales.md)."
        ),
        salario=SALARIO_DIRECCION,
        mitos=[
            ("«GTM es el plan de lanzamiento.»",
             "El lanzamiento es un evento dentro de la estrategia. GTM decide el movimiento comercial "
             "completo."),
            ("«Más canales, más alcance.»",
             "Cada canal consume habilitación y gestión. Los canales sin sostenimiento no producen."),
            ("«Si funciona aquí, funciona allá.»",
             "Cambian competidores, normas, hábitos de pago y referencias. Cada geografía es un mercado "
             "nuevo."),
            ("«El crecimiento justifica la ineficiencia.»",
             "A veces sí, si se declara y se mide. Lo que no es defendible es no notarlo."),
        ],
        honestidad=(
            "Este es un rol de decisión con consecuencias grandes; el programa entrega el marco y la "
            "economía, pero la experiencia de haber abierto y cerrado frentes reales no se sustituye. Es un "
            "destino de carrera, no un punto de entrada."
        ),
    ),
    # ------------------------------------------------------------------ 14
    dict(
        slug="cmo",
        emoji="🏛️",
        titulo="CMO — dirección de marketing",
        familia="Dirección",
        resumen=(
            "Responde ante el directorio por la contribución del marketing al ingreso. Su trabajo más difícil "
            "no es elegir campañas: es sostener la construcción de marca frente a la presión trimestral y "
            "asignar presupuesto con criterio de eficiencia."
        ),
        nivel="Dirección; exige trayectoria en marketing y capacidad de gobierno",
        foco="Estrategia, presupuesto, equipo, marca, medición y reporte al directorio",
        credencial="Un presupuesto con supuestos declarados y su desviación explicada",
        que_es=[
            "El CMO responde por dos horizontes a la vez. En el corto plazo, por la demanda del trimestre. En "
            "el largo, por un activo de marca que reduce el costo de adquisición futuro y que ninguna métrica "
            "trimestral captura bien. Ceder por completo al corto plazo es el error más común del cargo.",
            "La segunda mitad del trabajo es organizacional: estructura, roles con responsabilidad única, "
            "presupuesto derivado de supuestos explícitos y un ritmo de gestión que produzca decisiones en "
            "lugar de informes. Un área de marketing sin dueño único por indicador discute cada mes quién "
            "responde por la conversión, y esa discusión sustituye al trabajo.",
            "La tercera es política, en el sentido de gobierno: qué llega al directorio, cuándo se declara un "
            "riesgo y cómo se explica una desviación. Reportar un problema cuando ya se materializó se "
            "interpreta como ocultamiento, y esa lectura es difícil de revertir.",
        ],
        dia=[
            "**Revisión de eficiencia:** costo de adquisición completo, periodo de recuperación y "
            "contribución por canal.",
            "**Decisiones de asignación:** mover presupuesto según reglas escritas y no según la última "
            "reunión.",
            "**Desarrollo del equipo:** acompañamiento basado en observación real, no en revisión de "
            "números.",
            "**Coordinación con ventas:** cumplimiento del acuerdo de servicio en ambas direcciones.",
            "**Preparación de comité:** resultado frente a plan, causas del desvío, riesgos anticipados y "
            "decisiones que requieren aprobación.",
        ],
        tecnico=[
            "**Estrategia con diagnóstico.** Obstáculo principal, política rectora y acciones coherentes; una "
            "lista de iniciativas no es una estrategia.",
            "**Presupuesto base cero.** Cada línea derivada de la meta y de un supuesto declarado.",
            "**Equilibrio marca-activación.** Sostenido con medición y no con convicción.",
            "**Medición honesta.** Incrementalidad donde el gasto lo justifica; separación de tráfico de "
            "marca.",
            "**Objetivos y resultados clave.** Pocos, medibles y separados del sistema de compensación.",
            "**Gobierno.** Reporte al directorio con precisión histórica visible y riesgos declarados antes.",
        ],
        herramientas=(
            "Dirección:        presupuesto, OKR, tableros ejecutivos\n"
            "Medición:         modelos de atribución y pruebas de incrementalidad\n"
            "Equipo:           marcos de desempeño y desarrollo\n"
            "Coordinación:     acuerdos de servicio con ventas\n"
            "Reporte:          material de directorio con causas de desvío"
        ),
        blandas=[
            "**Sostener el largo plazo con evidencia.** Sin medición de marca, esa discusión se pierde "
            "siempre.",
            "**Comunicar malas noticias temprano.** Es la base de la confianza del directorio.",
            "**Construir equipo.** El resultado deja de depender de la presencia propia en cada reunión.",
            "**Decidir con información incompleta** y declarar la condición de revisión.",
        ],
        ruta=[
            ("04", "posicionamiento: la elección que ordena todo el presupuesto"),
            ("06", "marca como activo económico, con su medición"),
            ("12", "sistema digital de adquisición y su economía por canal"),
            ("14", "medios pagados con control de eficiencia"),
            ("20", "**analítica ejecutiva**: economía unitaria, incrementalidad y tableros"),
            ("23", "**el núcleo de dirección**: organización, presupuesto, OKR, gobierno y reporte"),
            ("22", "go-to-market y expansión, con su criterio de apertura de frentes"),
        ],
        clases=[
            ("23", "01", "Diseño de la organización comercial: cada frontera es un punto de pérdida"),
            ("23", "06", "Presupuesto: supuestos declarados en lugar de porcentaje del año anterior"),
            ("23", "07", "OKR y KPI: la confusión entre indicador de estado y objetivo"),
            ("23", "13", "Reporte al directorio: declarar el riesgo antes de que se materialice"),
            ("06", "13", "Medición de marca: olas comparables y línea base"),
            ("20", "09", "Incrementalidad: la evidencia que sostiene el presupuesto"),
            ("22", "13", "Métricas GTM: eficiencia además de crecimiento"),
        ],
        labs=["23", "20"],
        artefactos=[
            "Plan de marketing con diagnóstico y política rectora explícitos",
            "Presupuesto con supuestos declarados y reglas de reasignación",
            "Sistema de medición de marca con línea base",
            "Material de directorio con precisión histórica del forecast",
        ],
        credenciales=[
            "**Programas ejecutivos** — útiles para la red de contactos y el marco de gestión.",
            "**Portafolio** — un presupuesto con supuestos y su desviación explicada, y un caso de "
            "reasignación fundamentada.",
        ],
        progresion=(
            "CMO → [CRO](cro.md) en organizaciones que integran la función de ingresos, o dirección general. "
            "Muchos derivan a consultoría de dirección o a directorios."
        ),
        salario=SALARIO_DIRECCION,
        mitos=[
            ("«El CMO decide las campañas.»",
             "Decide dónde compite la empresa, cómo se asigna el presupuesto y cómo se mide. Las campañas "
             "las ejecuta el equipo."),
            ("«La marca no se puede defender ante el directorio.»",
             "Se defiende con notoriedad, consideración y prima de precio medidas en olas comparables."),
            ("«Hay que reportar sólo lo bueno.»",
             "Un riesgo reportado tarde se lee como ocultamiento y cuesta más que el problema."),
            ("«El equipo grande es señal de éxito.»",
             "La eficiencia del crecimiento importa más que el tamaño del área."),
        ],
        honestidad=(
            "Es un cargo de dirección: el programa entrega el sistema y el criterio, no la trayectoria. Su "
            "utilidad real aquí es ordenar lo que ya se ejerce y llenar los huecos —normalmente medición, "
            "economía unitaria y gobierno—."
        ),
    ),
    # ------------------------------------------------------------------ 15
    dict(
        slug="vp-sales",
        emoji="🏅",
        titulo="VP de ventas / Gerente comercial",
        familia="Dirección",
        resumen=(
            "Responde por el número del equipo, no por el propio. Su trabajo es que el resultado deje de "
            "depender de dos vendedores estrella y pase a depender de un sistema que otros puedan ejecutar."
        ),
        nivel="Dirección; se llega desde jefatura comercial con trayectoria de resultado",
        foco="Estructura, cuotas, territorios, forecast, contratación, desarrollo y compensación",
        credencial="Un forecast con precisión histórica publicada y corregida",
        que_es=[
            "El salto de vendedor a jefatura es el más difícil del área porque cambia el objeto del trabajo: "
            "ya no se trata de cerrar, sino de que otros cierren. Muchos buenos vendedores fracasan aquí "
            "porque siguen vendiendo en lugar de construir el sistema.",
            "El trabajo tiene cuatro frentes simultáneos: personas —contratar, formar, acompañar y decidir "
            "salidas—, sistema —proceso, CRM y forecast—, números —cuotas, territorios y capacidad— y "
            "gobierno —incentivos, cultura y reporte al directorio—. Descuidar cualquiera de los cuatro "
            "aparece en el resultado dentro de dos trimestres.",
            "El diseño de cuotas y territorios explica una parte importante de la varianza de desempeño que "
            "suele atribuirse a las personas. Poner en plan de mejora a alguien cuyo territorio tiene un "
            "tercio del potencial es un error de gestión, no de la persona.",
        ],
        dia=[
            "**Revisión de pipeline:** por valor y riesgo, con decisiones registradas y seguimiento en la "
            "sesión siguiente.",
            "**Acompañamiento:** escuchar conversaciones reales, no revisar el CRM y llamarlo coaching.",
            "**Forecast:** consolidar por categoría, contrastar con método alternativo y reportar la "
            "precisión histórica.",
            "**Contratación:** entrevistas con ejercicio que reproduzca una tarea real del puesto.",
            "**Gestión de desempeño:** distinguir problema de capacidad, de claridad o de condiciones de "
            "territorio antes de intervenir.",
        ],
        tecnico=[
            "**Diseño de proceso.** Etapas por evidencia del cliente y criterios de salida verificables.",
            "**Forecast.** Categorías con criterio, precisión medida y sesgo corregido.",
            "**Cuotas y territorios.** Potencial estimado y equidad de oportunidad; la cuota se deriva del "
            "potencial, no del deseo.",
            "**Capacidad comercial.** Tiempo efectivo, carga por oportunidad y rampa de productividad.",
            "**Compensación.** Contrapesos de margen y permanencia; el esquema produce exactamente el "
            "comportamiento que premia.",
            "**Contratación y desarrollo.** Perfil derivado de datos y práctica deliberada con "
            "retroalimentación.",
        ],
        herramientas=(
            "CRM:              administración de pipeline y forecast\n"
            "Conversaciones:   grabación con consentimiento y análisis\n"
            "Planificación:    modelos de capacidad, cuota y territorio\n"
            "Compensación:     simulación de esquemas y efectos no deseados\n"
            "Gestión:          rutinas de revisión y registro de acuerdos"
        ),
        blandas=[
            "**Dejar de vender.** El error más común al asumir el cargo.",
            "**Dar retroalimentación específica** sobre comportamiento observable y no sobre resultados.",
            "**Tomar decisiones de salida a tiempo.** Postergarlas daña al equipo y a la persona.",
            "**Actuar ante el primer incumplimiento ético.** La ausencia de consecuencia es la política "
            "real.",
        ],
        ruta=[
            ("08", "proceso comercial: lo que vas a estandarizar"),
            ("09", "venta consultiva y deal review: la conversación que sostendrás con el equipo"),
            ("16", "**CRM, pipeline, forecast, cuotas y capacidad**"),
            ("23", "**el núcleo de dirección**: organización, contratación, compensación y gobierno"),
            ("18", "retención: la mitad del ingreso que no depende de nuevas ventas"),
            ("20", "analítica: para que el forecast deje de ser una intuición"),
        ],
        clases=[
            ("16", "07", "Forecast: método, sesgo y corrección"),
            ("16", "08", "Cuotas y territorios: la varianza que no es de las personas"),
            ("16", "09", "Capacidad comercial: tiempo efectivo y rampa"),
            ("23", "05", "Compensación: los efectos no deseados que produce el esquema"),
            ("23", "10", "Coaching comercial: observación real y práctica deliberada"),
            ("23", "11", "Gestión de desempeño: capacidad, claridad o condiciones"),
            ("23", "12", "Ética y cultura: lo que la organización tolera bajo presión"),
        ],
        labs=["16", "23"],
        artefactos=[
            "Diseño de sales operations con forecast y gobierno",
            "Modelo de cuotas y territorios con potencial estimado",
            "Esquema de compensación con contrapesos simulados",
            "Operating system comercial con ritmo de gestión definido",
        ],
        credenciales=[
            "**No hay certificación relevante.** Se evalúa por historial de resultado de equipo y por el "
            "caso de gestión en entrevista.",
            "**Portafolio** — un modelo de capacidad y cuotas, y un forecast con precisión publicada.",
        ],
        progresion=(
            "Jefatura comercial → VP de ventas → **[CRO](cro.md)** o dirección general. Salida lateral "
            "frecuente: [RevOps](revops.md) para quien prefiere el sistema a las personas."
        ),
        salario=SALARIO_DIRECCION,
        mitos=[
            ("«El mejor vendedor debe ser el jefe.»",
             "Son trabajos distintos. Vender bien no predice dirigir bien."),
            ("«Más vendedores, más ingreso.»",
             "Escalar un motor roto genera rotación y destruye margen. Primero se corrige el proceso."),
            ("«El forecast es responsabilidad del equipo.»",
             "La precisión es consecuencia de los criterios de etapa que la jefatura define y hace "
             "cumplir."),
            ("«La compensación resuelve la motivación.»",
             "Produce el comportamiento que premia, incluidos los efectos no deseados."),
        ],
        honestidad=(
            "El programa entrega el sistema de dirección comercial completo. No entrega la experiencia de "
            "sostener un número con un equipo real durante varios trimestres, que es lo que el mercado "
            "evalúa para este cargo."
        ),
    ),
    # ------------------------------------------------------------------ 16
    dict(
        slug="cro",
        emoji="👑",
        titulo="CRO — dirección de ingresos",
        familia="Dirección",
        resumen=(
            "Dirige marketing, ventas y éxito de cliente como un solo sistema. Es el cargo donde se hace "
            "visible que el ingreso no lo produce un área, sino la coherencia entre las tres."
        ),
        nivel="Dirección ejecutiva; se llega desde CMO, VP de ventas o dirección de operaciones de ingreso",
        foco="Estrategia de ingresos, modelo operativo, economía unitaria, equipo y gobierno",
        credencial="Un operating system del CRO que funcione sin la presencia del CRO",
        que_es=[
            "El CRO existe porque marketing, ventas y servicio optimizan métricas distintas y el sistema "
            "completo pierde. Su trabajo es que exista un modelo de datos común, definiciones únicas y una "
            "economía unitaria verificada, y que las tres áreas respondan por el mismo resultado.",
            "La prueba de su trabajo es la independencia: el sistema debe producir resultados sin que la "
            "dirección esté presente en cada decisión, y debe detectar problemas antes de que aparezcan en "
            "los estados financieros.",
            "Su tentación permanente es responder a la presión de crecimiento contratando. Duplicar el equipo "
            "sobre un motor con periodo de recuperación mayor que la vida del cliente no acelera el "
            "crecimiento: acelera la destrucción de caja.",
        ],
        dia=[
            "**Revisión del sistema:** ingreso neto retenido, eficiencia del crecimiento y economía unitaria "
            "por segmento.",
            "**Resolución de fronteras:** los problemas del cargo aparecen en los traspasos entre áreas, no "
            "dentro de ellas.",
            "**Forecast unificado:** ingreso nuevo, renovación, expansión y contracción, con precisión "
            "medida por componente.",
            "**Desarrollo de la línea directiva:** el resultado debe sobrevivir a la ausencia de cualquier "
            "persona, incluida la propia.",
            "**Gobierno:** qué llega al directorio, con qué anticipación y con qué evidencia.",
        ],
        tecnico=[
            "**Economía unitaria verificada.** Costo de adquisición completo, periodo de recuperación frente "
            "a vida media y contribución por segmento.",
            "**Modelo operativo de ingresos.** Definiciones únicas, fuente autoritativa por dato y "
            "responsabilidad por proceso.",
            "**Forecast unificado.** Con precisión histórica publicada y sesgo corregido.",
            "**Diseño organizacional.** Especialización proporcional al volumen; cada frontera es un punto de "
            "pérdida.",
            "**Incentivos.** Esquemas con contrapesos que no premien comportamientos contradictorios entre "
            "áreas.",
            "**Cumplimiento y ética.** Lo que la organización tolera bajo presión define su cultura real.",
        ],
        herramientas=(
            "Dirección:        tableros ejecutivos y ritmo de gestión\n"
            "Modelo:           economía unitaria y proyección por componente\n"
            "Organización:     diseño de roles, cuotas y compensación\n"
            "Gobierno:         reporte a directorio y registro de decisiones\n"
            "Sistema:          modelo de datos e indicadores con cifra única"
        ),
        blandas=[
            "**Construir un sistema que no dependa de uno.** Es literalmente el criterio de éxito del cargo.",
            "**Sostener decisiones impopulares.** Frenar contrataciones cuando la retención no se estabiliza "
            "es lo correcto y lo que menos gusta.",
            "**Transparencia con el directorio.** Los riesgos se declaran antes, no cuando se materializan.",
            "**Cultura por acción.** Lo que se premia y lo que se sanciona define lo que el equipo hará bajo "
            "presión.",
        ],
        ruta=[
            ("01", "el motor de ingresos como sistema: la tesis completa del cargo"),
            ("16", "sales operations, pipeline y forecast con precisión medida"),
            ("17", "RevOps: definiciones únicas, datos e integración"),
            ("18", "retención y expansión: la mitad del ingreso"),
            ("20", "economía unitaria, incrementalidad y coherencia de las cifras"),
            ("22", "go-to-market y expansión, con su criterio de apertura de frentes"),
            ("23", "**el núcleo**: operating system del CRO"),
            ("24", "integración final con cumplimiento y defensa ejecutiva"),
        ],
        clases=[
            ("01", "01", "El sistema comercial: dónde se pierde el valor realmente"),
            ("17", "14", "Operating model de RevOps: una cifra única por indicador"),
            ("18", "14", "Sistema de retención: anticipar las bajas del próximo trimestre"),
            ("20", "05", "Periodo de recuperación: la restricción de caja que decide el ritmo"),
            ("23", "08", "Forecast ejecutivo: precisión histórica visible"),
            ("23", "14", "Operating system del CRO: independencia y detección temprana"),
            ("24", "13", "Defensa ejecutiva: sostener el razonamiento bajo preguntas duras"),
        ],
        labs=["23", "17", "24"],
        artefactos=[
            "Operating system del CRO con estructura, ritmo y gobierno",
            "Economía unitaria por segmento verificada con contabilidad",
            "Forecast unificado con precisión por componente",
            "Capstone completo con defensa ante panel",
        ],
        credenciales=[
            "**No hay certificación relevante.** Se evalúa por trayectoria y por la calidad del razonamiento "
            "ante un caso real.",
            "**Portafolio** — el Capstone del programa, si se desarrolla sobre una operación propia, es un "
            "artefacto defendible ante un directorio.",
        ],
        progresion=(
            "CRO → dirección general o directorios. También es un punto de partida frecuente hacia "
            "[founder](founder.md) o hacia consultoría de dirección comercial."
        ),
        salario=SALARIO_DIRECCION,
        mitos=[
            ("«Es el jefe de ventas con otro nombre.»",
             "Responde por marketing, ventas y éxito de cliente como un sistema, no por una de las tres."),
            ("«Su trabajo es cerrar los negocios grandes.»",
             "Su trabajo es que el sistema cierre sin él. Si depende de su presencia, no hay sistema."),
            ("«Crecer resuelve los problemas.»",
             "Escalar un motor roto los multiplica y los hace más caros de corregir."),
            ("«Los números son responsabilidad de finanzas.»",
             "La economía unitaria del ingreso es responsabilidad del cargo y debe resistir revisión "
             "financiera."),
        ],
        honestidad=(
            "Es el cargo más alto de la función comercial y no se alcanza con formación. El programa sirve "
            "para ordenar el sistema completo y para preparar la defensa de decisiones ante un directorio, "
            "pero la trayectoria es requisito."
        ),
    ),
    # ------------------------------------------------------------------ 17
    dict(
        slug="founder",
        emoji="🚩",
        titulo="Founder / dueño de negocio",
        familia="Dirección",
        resumen=(
            "Quien tiene que vender antes de poder contratar a alguien que venda. No necesita dominar todas "
            "las áreas: necesita saber cuál es su cuello de botella real y no gastar dinero en el resto."
        ),
        nivel="Cualquiera; el programa asume que puedes estar partiendo de cero",
        foco="Problema verificado, oferta, precio, primeras ventas, economía unitaria y cumplimiento",
        credencial="Un Capstone sobre la propia empresa con economía y cumplimiento verificados",
        que_es=[
            "El fundador enfrenta una versión comprimida de todo el programa: tiene que elegir mercado, "
            "diseñar oferta, fijar precio, conseguir los primeros clientes y sostener la operación, muchas "
            "veces solo y con caja limitada.",
            "Su error más caro no es táctico sino de secuencia: invertir en adquisición antes de verificar "
            "que el problema existe, que alguien paga y que la economía cierra. La mayoría de los negocios "
            "que fracasan no tenía un problema de marketing: tenía un costo por cliente superior a lo que ese "
            "cliente aportaba.",
            "El segundo error es de dependencia: construir un negocio que sólo funciona si el fundador está "
            "en cada conversación. Ese negocio no se puede vender, no se puede delegar y no se puede "
            "sostener.",
        ],
        dia=[
            "**Conversaciones con clientes:** la actividad de mayor retorno en las primeras etapas, y la "
            "primera que se abandona cuando llega la operación.",
            "**Venta directa:** el fundador vende antes que nadie, porque es quien puede cambiar la oferta en "
            "tiempo real según lo que escucha.",
            "**Decisiones de caja:** dónde no gastar. La restricción de caja define el ritmo de adquisición, "
            "no el entusiasmo.",
            "**Operación:** entregar lo prometido, que es la única forma de que el cliente vuelva y refiera.",
            "**Cumplimiento:** boletas, condiciones publicadas, tratamiento de datos y marca registrada. "
            "Barato de hacer bien al inicio y caro de corregir después.",
        ],
        tecnico=[
            "**Verificación del problema.** Evidencia de comportamiento pasado y compromiso costoso, no "
            "elogios.",
            "**Diseño de oferta y precio.** Disposición a pagar antes de construir; el costo como piso y no "
            "como método.",
            "**Primeras ventas.** Proceso comercial mínimo, discovery y calificación.",
            "**Economía unitaria.** Costo de adquisición completo, margen de contribución y periodo de "
            "recuperación frente a vida media.",
            "**Retención.** Si la curva no se estabiliza, adquirir es llenar un estanque con fuga.",
            "**Cumplimiento chileno.** Consumo, comercio electrónico, datos personales, marca y tributación "
            "como requisitos de diseño.",
        ],
        herramientas=(
            "Investigación:    entrevistas y validación con compromiso costoso\n"
            "Venta:            CRM simple, propuesta estándar, seguimiento\n"
            "Economía:         planilla de unit economics y flujo de caja\n"
            "Digital:          sitio, analítica básica, correo\n"
            "Cumplimiento:     boleta electrónica, condiciones, registro de marca"
        ),
        blandas=[
            "**Escuchar sin defender la idea.** El sesgo de confirmación es la causa más común de gastar un "
            "año en algo que nadie quería.",
            "**Vender sin vergüenza.** Nadie va a vender el producto propio con más convicción y menos costo.",
            "**Decidir con poca información** y declarar qué la haría cambiar.",
            "**Reconocer el cuello de botella real** en lugar de trabajar en lo que resulta más cómodo.",
        ],
        ruta=[
            ("01", "el sistema completo, para no confundir síntoma con causa"),
            ("02", "cliente: quién decide, quién paga y qué progreso busca"),
            ("03", "investigación mínima que cambia decisiones"),
            ("05", "oferta y encaje problema-solución antes de construir nada"),
            ("07", "precio: la palanca de utilidad más rápida y la peor gestionada"),
            ("08", "proceso comercial para las primeras ventas"),
            ("11", "prospección: de dónde vendrá el próximo cliente"),
            ("12", "adquisición digital con economía verificable"),
            ("24", "**el cierre**: empresa completa, cumplimiento y defensa"),
        ],
        clases=[
            ("02", "02", "Resultados deseados: qué compra realmente el cliente"),
            ("03", "03", "Diseño de entrevistas: comportamiento pasado, no intención futura"),
            ("05", "03", "Encaje problema-solución: señales de compromiso antes de construir"),
            ("07", "04", "Pricing basado en valor: cuánto vale para quién"),
            ("20", "05", "Periodo de recuperación: la restricción de caja que define el ritmo"),
            ("19", "06", "Retención antes que adquisición: el orden que salva la caja"),
            ("24", "12", "Cumplimiento en Chile: obligaciones traducidas a diseño"),
        ],
        labs=["05", "07", "24"],
        artefactos=[
            "Expediente de cliente con evidencia de compromiso costoso",
            "Oferta lista para vender con precio fundamentado",
            "Economía unitaria con periodo de recuperación y sensibilidad",
            "Capstone con la operación completa y cumplimiento verificado",
        ],
        credenciales=[
            "**Ninguna importa aquí.** Lo que importa son clientes que pagan y una economía que cierra.",
            "**El Capstone sobre tu propia empresa** es el artefacto más útil del programa para este perfil: "
            "obliga a revisar números, evidencia y cumplimiento a la vez.",
        ],
        progresion=(
            "Founder → contratación del primer perfil comercial → construcción de equipo → "
            "[CRO](cro.md) interno o contratación de dirección comercial. La transición difícil es dejar de "
            "ser el único que sabe vender."
        ),
        salario=(
            "No aplica un rango salarial: el ingreso depende del negocio. El indicador relevante en esta\n"
            "etapa no es el sueldo sino la economía unitaria:\n\n"
            "Indicador                        Umbral de alerta\n"
            "-------------------------------  ---------------------------------\n"
            "Periodo de recuperación          mayor que la vida media del cliente\n"
            "Margen de contribución           bajo el 30 % en servicios recurrentes\n"
            "Retención de la cohorte          curva que no se estabiliza\n"
            "Concentración de ingreso         un cliente sobre el 25 % del total"
        ),
        mitos=[
            ("«Primero el producto, después las ventas.»",
             "Construir sin señales de compromiso costoso es la forma más común de perder un año."),
            ("«Necesito invertir en marketing para empezar.»",
             "Las primeras ventas suelen venir de conversación directa y referencias, no de campañas."),
            ("«El precio bajo facilita entrar.»",
             "Un precio bajo con margen negativo hace que cada cliente nuevo empeore la caja."),
            ("«El cumplimiento se ve después.»",
             "Registrar la marca, publicar condiciones correctas y tratar bien los datos es barato al inicio "
             "y caro de corregir."),
        ],
        honestidad=(
            "El programa entrega criterio y método, no clientes. Su mayor utilidad para un fundador es "
            "evitar los errores caros de secuencia: verificar antes de construir, medir antes de escalar y "
            "cumplir antes de crecer."
        ),
    ),
]
