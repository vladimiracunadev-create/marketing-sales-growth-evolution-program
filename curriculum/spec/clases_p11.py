# -*- coding: utf-8 -*-
"""Parte 11 — Prospección y generación de demanda."""

CLASES = [
    dict(
        n="01",
        slug="demand-generation-versus-lead-generation",
        titulo="Generación de demanda versus generación de leads",
        tesis=(
            "Generar demanda es crear conciencia de un problema y preferencia por una solución; generar leads "
            "es capturar datos de contacto de quienes ya tienen intención. Confundirlos produce el patrón más "
            "común de marketing B2B: muchos formularios completados y ninguna venta, porque se capturó a "
            "personas que descargaron material sin intención de comprar. La demanda tarda y compone; la "
            "captura de leads es inmediata y se agota."
        ),
        conceptos=[
            ("generación de demanda", "trabajo que crea conciencia del problema y preferencia antes de que exista intención"),
            ("captura de intención", "acción que recoge datos de quienes ya buscan una solución"),
            ("lead calificado", "contacto que cumple criterios verificables de perfil y de problema"),
            ("volumen sin intención", "captura masiva de contactos sin señal de problema ni de perfil"),
        ],
        metodo=[
            "separar en el plan las acciones de demanda y las de captura",
            "definir criterios de calificación antes de capturar",
            "medir cada tipo con métricas propias",
            "evaluar la contribución de la demanda al costo de captura",
            "ajustar la proporción según el estado del pipeline",
        ],
        senales=[
            ("proporción de leads calificados", "leads que cumplen criterios, sobre leads capturados en el periodo"),
            ("costo por oportunidad calificada", "gasto del canal dividido por oportunidades calificadas originadas"),
            ("evolución de búsquedas de marca", "volumen de búsquedas del nombre de la empresa, mensual"),
        ],
        caso=(
            "Ruta Andina captura 300 leads mensuales con un ebook. Ventas trabaja 60 y cierra 4. El costo por "
            "cliente ganado por esa vía es 3,2 veces el de referidos."
        ),
        limite=(
            "La generación de demanda tiene retorno lento y difícil de atribuir. Exigirle resultado trimestral "
            "lleva a desmantelarla justo cuando empezaba a componer."
        ),
        libros=["binet-field", "godin", "weinberg-traction", "chaffey"],
        error=("Medir demanda con métricas de captura",
               "Usa indicadores propios: búsquedas de marca, recuerdo y participación en la consideración."),
    ),
    dict(
        n="02",
        slug="list-building-etico",
        titulo="Construcción ética de listas",
        tesis=(
            "Una lista es un activo o un pasivo según cómo se construyó. Comprar bases produce baja respuesta, "
            "reclamos por spam, deterioro de la reputación del dominio y exposición legal. Construir la lista "
            "desde el perfil de cliente ideal, con datos verificados y base de licitud, produce menos "
            "contactos y mejores resultados. En Chile la Ley 21.719 refuerza obligaciones de finalidad, "
            "información y derechos del titular."
        ),
        conceptos=[
            ("base de licitud", "fundamento jurídico que habilita el tratamiento de los datos personales"),
            ("dato verificado", "información de contacto confirmada y vigente, con fuente registrada"),
            ("reputación de dominio", "estado del remitente ante los proveedores de correo, afectado por rebotes y reclamos"),
            ("derecho del titular", "facultad de la persona de acceder, rectificar, oponerse y solicitar la eliminación de sus datos"),
        ],
        metodo=[
            "definir el perfil objetivo antes de construir la lista",
            "identificar la base de licitud del tratamiento",
            "verificar y documentar la fuente de cada contacto",
            "habilitar mecanismos de oposición y eliminación",
            "monitorear reputación de dominio y tasa de reclamos",
        ],
        senales=[
            ("tasa de rebote", "correos rebotados, sobre correos enviados, por campaña"),
            ("tasa de reclamos por spam", "reclamos recibidos, sobre correos entregados"),
            ("contactos con fuente documentada", "contactos con origen y base de licitud registrados, sobre contactos de la base"),
        ],
        caso=(
            "Ruta Andina compró 12.000 contactos. La respuesta es 0,4 %, hay reclamos por spam y la "
            "reputación del dominio empezó a caer, afectando también los correos transaccionales."
        ),
        limite=(
            "El cumplimiento formal no basta: una comunicación técnicamente lícita pero irrelevante destruye "
            "reputación comercial igual que una ilícita."
        ),
        libros=["blount", "godin", "handley", "oneil"],
        error=("Comprar bases de contactos",
               "Construye la lista desde el perfil objetivo con datos verificados y base de licitud documentada."),
    ),
    dict(
        n="03",
        slug="investigacion-de-prospectos",
        titulo="Investigación de prospectos",
        tesis=(
            "La diferencia entre un contacto ignorado y uno respondido suele estar en dos minutos de "
            "investigación previa. Investigar significa identificar una señal concreta —una apertura, una "
            "contratación, un cambio regulatorio, una reseña negativa— que hace pertinente el contacto ahora. "
            "Sin esa señal, el mensaje es genérico y compite con decenas iguales."
        ),
        conceptos=[
            ("señal de oportunidad", "hecho observable que hace pertinente el contacto en este momento"),
            ("investigación proporcional", "esfuerzo de investigación ajustado al valor potencial de la cuenta"),
            ("relevancia demostrada", "evidencia en el mensaje de que se conoce la situación específica del destinatario"),
            ("fuente pública", "información obtenida legítimamente de canales abiertos"),
        ],
        metodo=[
            "definir qué señales importan para el perfil objetivo",
            "establecer el nivel de investigación según valor de la cuenta",
            "documentar la señal encontrada antes de contactar",
            "construir el mensaje sobre esa señal",
            "medir la diferencia de respuesta con y sin señal",
        ],
        senales=[
            ("contactos con señal documentada", "contactos realizados con señal registrada, sobre contactos totales"),
            ("tasa de respuesta con señal", "respuestas obtenidas en contactos con señal, frente a contactos sin señal"),
            ("tiempo de investigación por contacto", "minutos invertidos, por contacto y por segmento de valor"),
        ],
        caso=(
            "Los correos de Ruta Andina empiezan con «espero que estés muy bien». Ninguno menciona que el "
            "taller destinatario abrió una segunda sucursal el mes pasado."
        ),
        limite=(
            "La investigación tiene un límite de proporcionalidad y otro de privacidad: recopilar información "
            "personal más allá de lo necesario es tratamiento excesivo."
        ),
        libros=["blount", "bertuzzi", "weinberg-sales", "ross"],
        error=("Contactar sin una señal que justifique el momento",
               "Documenta la señal antes de enviar y construye el mensaje sobre ella."),
    ),
    dict(
        n="04",
        slug="cold-email",
        titulo="Correo en frío",
        tesis=(
            "Un correo en frío efectivo es breve, específico y pide poco. Su objetivo no es vender sino "
            "obtener una conversación. La estructura que funciona es reconocible: señal concreta, problema "
            "probable, evidencia mínima y una petición de bajo compromiso. El error más frecuente es pedir "
            "demasiado —una reunión de una hora— a alguien que aún no tiene razón para conceder nada."
        ),
        conceptos=[
            ("asunto informativo", "línea que describe el contenido sin engañar ni manipular la apertura"),
            ("petición de bajo compromiso", "solicitud proporcional al nivel de confianza existente"),
            ("evidencia mínima", "dato o caso breve que sostiene la afirmación central del mensaje"),
            ("mecanismo de oposición", "medio simple y visible para que el destinatario solicite no ser contactado"),
        ],
        metodo=[
            "identificar la señal y el problema probable",
            "redactar asunto informativo y cuerpo breve",
            "incluir evidencia mínima verificable",
            "pedir un compromiso proporcional",
            "medir respuesta y ajustar una variable por vez",
        ],
        senales=[
            ("tasa de respuesta", "respuestas recibidas, sobre correos entregados, por secuencia"),
            ("tasa de respuesta positiva", "respuestas que aceptan el siguiente paso, sobre respuestas recibidas"),
            ("tasa de solicitud de baja", "solicitudes de no contacto, sobre correos entregados"),
        ],
        caso=(
            "El correo estándar de Ruta Andina tiene 340 palabras, tres párrafos sobre la empresa y pide una "
            "reunión de 45 minutos. La respuesta es 0,4 %."
        ),
        limite=(
            "El correo en frío está sujeto a normas de datos personales y de comunicaciones comerciales: debe "
            "identificar al remitente, informar el origen del dato y permitir la oposición."
        ),
        libros=["blount", "handley", "bertuzzi", "sugarman"],
        error=("Pedir una reunión larga en el primer contacto",
               "Solicita un compromiso mínimo: una respuesta de una línea o una pregunta concreta."),
    ),
    dict(
        n="05",
        slug="cold-calling",
        titulo="Llamada en frío",
        tesis=(
            "La llamada en frío sigue funcionando en segmentos donde el destinatario contesta el teléfono, y "
            "eso hay que verificarlo antes de invertir. Su ventaja es la información inmediata: en 30 "
            "segundos se sabe si hay problema, si es la persona correcta y si el momento es adecuado. Su "
            "exigencia es la preparación: una apertura que no explica en una frase por qué esta llamada "
            "importa termina antes de empezar."
        ),
        conceptos=[
            ("apertura en una frase", "declaración breve del motivo de la llamada que justifica continuar"),
            ("permiso explícito", "confirmación del destinatario de que puede conversar en ese momento"),
            ("calificación en llamada", "verificación rápida de perfil, problema y momento"),
            ("gestión del rechazo", "capacidad de sostener la actividad ante una tasa alta de respuestas negativas"),
        ],
        metodo=[
            "verificar que el segmento responde llamadas",
            "preparar apertura, señal y pregunta de calificación",
            "pedir permiso explícito antes de continuar",
            "calificar en la llamada y registrar el resultado",
            "medir contactabilidad y ajustar horarios",
        ],
        senales=[
            ("tasa de contactabilidad", "llamadas con conversación efectiva, sobre llamadas realizadas, por franja horaria"),
            ("conversaciones por reunión agendada", "conversaciones efectivas sostenidas, sobre reuniones agendadas, por vendedor y por mes"),
            ("tasa de calificación en llamada", "llamadas con criterios verificados, sobre conversaciones efectivas"),
        ],
        caso=(
            "El equipo de Ruta Andina llama entre 15:00 y 17:00. Los dueños de taller atienden clientes en ese "
            "horario; la contactabilidad es 6 % frente a 22 % antes de las 10:00."
        ),
        limite=(
            "La llamada comercial no solicitada está regulada y puede ser percibida como intrusiva. Debe "
            "respetarse la solicitud de no contacto y registrarse."
        ),
        libros=["blount", "weinberg-sales", "bertuzzi", "ross"],
        error=("Llamar sin verificar la franja horaria del segmento",
               "Mide contactabilidad por franja y concentra la actividad donde el segmento efectivamente responde."),
    ),
    dict(
        n="06",
        slug="linkedin-y-social-selling",
        titulo="LinkedIn y social selling",
        tesis=(
            "El social selling funciona cuando construye credibilidad antes de pedir: contenido útil, "
            "participación real en conversaciones del gremio y contacto personalizado. Falla cuando se "
            "convierte en automatización masiva de invitaciones y mensajes iguales, que degradan la marca "
            "personal y la de la empresa. La métrica correcta no son los contactos agregados sino las "
            "conversaciones sostenidas."
        ),
        conceptos=[
            ("credibilidad pública", "reputación construida con contenido y participación verificables"),
            ("contacto personalizado", "mensaje que demuestra conocimiento específico del destinatario"),
            ("automatización masiva", "envío indiscriminado que ignora contexto y degrada la reputación"),
            ("conversación sostenida", "intercambio de al menos dos mensajes con contenido sustantivo"),
        ],
        metodo=[
            "definir el tema en que la persona quiere ser reconocida",
            "publicar con regularidad contenido útil y verificable",
            "participar en conversaciones del gremio",
            "contactar con mensajes personalizados y proporcionales",
            "medir conversaciones sostenidas y no volumen de contactos",
        ],
        senales=[
            ("tasa de aceptación de contacto", "invitaciones aceptadas, sobre invitaciones enviadas"),
            ("conversaciones sostenidas", "intercambios con dos o más mensajes sustantivos, sobre contactos aceptados"),
            ("oportunidades originadas en el canal", "oportunidades calificadas atribuidas al canal, sobre oportunidades totales"),
        ],
        caso=(
            "Un vendedor de Ruta Andina envía 200 invitaciones semanales con el mismo texto. La tasa de "
            "aceptación cayó de 38 % a 11 % y recibió dos reportes por spam."
        ),
        limite=(
            "Las plataformas tienen términos de uso que prohíben ciertas automatizaciones. Infringirlos puede "
            "costar la cuenta y la reputación asociada."
        ),
        libros=["blount", "godin", "handley", "vaynerchuk"],
        error=("Automatizar mensajes idénticos a escala",
               "Personaliza sobre una señal concreta y mide conversaciones sostenidas, no contactos agregados."),
    ),
    dict(
        n="07",
        slug="networking",
        titulo="Networking",
        tesis=(
            "El networking comercial produce resultados cuando se entiende como construcción de relaciones "
            "recíprocas y no como recolección de tarjetas. En mercados gremiales pequeños —muy común en "
            "Chile— la reputación circula rápido y una relación bien cuidada abre puertas que ninguna "
            "campaña alcanza. La disciplina consiste en aportar antes de pedir y en dar seguimiento a lo "
            "prometido."
        ),
        conceptos=[
            ("reciprocidad", "principio por el cual el aporte previo genera disposición a corresponder"),
            ("densidad de red gremial", "grado en que los actores de un rubro se conocen entre sí"),
            ("seguimiento de compromisos", "cumplimiento de lo prometido en conversaciones informales"),
            ("capital relacional", "valor acumulado de relaciones que facilitan acceso y confianza"),
        ],
        metodo=[
            "identificar los espacios donde participa el segmento",
            "definir qué aporte concreto se puede entregar",
            "participar con regularidad y no sólo cuando se necesita",
            "registrar y cumplir los compromisos adquiridos",
            "medir oportunidades originadas por la red",
        ],
        senales=[
            ("oportunidades originadas por red", "oportunidades calificadas atribuidas a relaciones, sobre oportunidades totales"),
            ("cumplimiento de compromisos informales", "compromisos cumplidos, sobre compromisos adquiridos en instancias de red"),
            ("participación en instancias del gremio", "eventos o espacios con participación efectiva, por trimestre"),
        ],
        caso=(
            "Ruta Andina participa en la asociación gremial de talleres sólo cuando necesita vender. Su "
            "reputación allí es la de proveedor que aparece a fin de trimestre."
        ),
        limite=(
            "En asociaciones gremiales hay límites de libre competencia: intercambiar información sensible de "
            "precios o clientes entre competidores puede constituir una infracción grave."
        ),
        libros=["cialdini", "godin", "blount", "collins"],
        error=("Aparecer sólo cuando se necesita vender",
               "Participa con regularidad y entrega aporte verificable antes de pedir cualquier cosa."),
    ),
    dict(
        n="08",
        slug="referidos",
        titulo="Referidos",
        tesis=(
            "El referido es el canal con mejor conversión y menor costo, y el más descuidado porque no se "
            "sistematiza. Convertirlo en canal exige tres cosas: identificar quiénes están en condiciones de "
            "referir —clientes con resultado acreditado—, pedir de forma específica y facilitar el acto. "
            "Pedir «si conoces a alguien, avísame» produce casi nada; pedir una introducción concreta a una "
            "persona identificada produce reuniones."
        ),
        conceptos=[
            ("momento de referencia", "instante en que el cliente ha obtenido resultado y está dispuesto a referir"),
            ("petición específica", "solicitud de introducción a una persona u organización identificada"),
            ("facilitación", "material que permite al cliente referir sin esfuerzo ni riesgo"),
            ("reciprocidad no monetaria", "reconocimiento o beneficio que no compromete la credibilidad de la referencia"),
        ],
        metodo=[
            "identificar clientes con resultado acreditado",
            "elegir el momento de la petición",
            "solicitar una introducción específica",
            "facilitar el mensaje que el cliente enviará",
            "medir conversión y agradecer el resultado",
        ],
        senales=[
            ("tasa de clientes que refieren", "clientes que originaron al menos una referencia en 12 meses, sobre clientes activos"),
            ("conversión de referidos", "referidos que se convierten en clientes, sobre referidos recibidos"),
            ("costo por cliente referido", "costo del programa dividido por clientes ganados por referencia"),
        ],
        caso=(
            "El 9 % de las ventas de Ruta Andina viene de referidos y representa el 21 % del margen. No existe "
            "ningún proceso para solicitarlos: llegan solos."
        ),
        limite=(
            "Incentivar económicamente las referencias puede comprometer su credibilidad y, si no se declara, "
            "constituye publicidad encubierta."
        ),
        libros=["reichheld", "cialdini", "mehta", "godin"],
        error=("Pedir referencias de forma genérica",
               "Solicita una introducción a una persona identificada y entrega el texto que el cliente puede reenviar."),
    ),
    dict(
        n="09",
        slug="eventos-y-comunidades",
        titulo="Eventos y comunidades",
        tesis=(
            "Los eventos y las comunidades funcionan como canal cuando la empresa aporta valor antes de "
            "vender y cuando existe un plan de seguimiento. Un stand sin seguimiento produce tarjetas; un "
            "taller práctico con contenido útil produce conversaciones calificadas. El costo por oportunidad "
            "de este canal suele ser alto, por lo que su evaluación exige medir hasta el cierre y no hasta el "
            "contacto."
        ),
        conceptos=[
            ("aporte previo", "contenido o servicio útil entregado antes de cualquier petición comercial"),
            ("calidad del asistente", "grado en que los asistentes corresponden al perfil de cliente objetivo"),
            ("plan de seguimiento", "secuencia definida de contacto posterior con responsables y plazos"),
            ("costo por oportunidad del evento", "inversión total dividida por oportunidades calificadas originadas"),
        ],
        metodo=[
            "seleccionar el evento por perfil de asistente y no por tamaño",
            "diseñar un aporte de valor concreto",
            "capturar contactos con consentimiento y contexto",
            "ejecutar el seguimiento dentro de las 72 horas",
            "medir el costo por oportunidad y por cliente ganado",
        ],
        senales=[
            ("proporción de asistentes en perfil", "asistentes que cumplen el perfil objetivo, sobre asistentes contactados"),
            ("costo por oportunidad calificada", "inversión total del evento dividida por oportunidades calificadas"),
            ("tasa de seguimiento en 72 horas", "contactos seguidos dentro del plazo, sobre contactos capturados"),
        ],
        caso=(
            "Ruta Andina invirtió CLP 3,8 millones en una feria y capturó 180 contactos. El seguimiento "
            "comenzó tres semanas después y produjo dos reuniones."
        ),
        limite=(
            "La captura de datos en eventos exige información clara sobre finalidad y consentimiento. Un "
            "sorteo no es base suficiente para enviar comunicaciones comerciales indefinidas."
        ),
        libros=["godin", "weinberg-traction", "chaffey", "blount"],
        error=("Capturar contactos sin plan de seguimiento",
               "Define responsables y plazo de 72 horas antes del evento, no después."),
    ),
    dict(
        n="10",
        slug="lead-magnets",
        titulo="Lead magnets",
        tesis=(
            "Un lead magnet intercambia contenido de valor por datos de contacto. Su calidad determina la "
            "calidad del lead: una guía genérica atrae a cualquiera, una calculadora específica del problema "
            "atrae a quien lo tiene. El criterio de diseño es simple y exigente: el recurso debe ser útil por "
            "sí mismo, incluso si la persona nunca compra."
        ),
        conceptos=[
            ("recurso de valor", "material que resuelve una parte real del problema del destinatario"),
            ("filtro implícito", "característica del recurso que atrae al perfil correcto y desalienta al resto"),
            ("intercambio proporcional", "cantidad de datos solicitados acorde al valor entregado"),
            ("consentimiento informado", "autorización específica sobre el uso posterior de los datos entregados"),
        ],
        metodo=[
            "elegir un problema específico del perfil objetivo",
            "construir un recurso útil por sí mismo",
            "solicitar sólo los datos necesarios",
            "informar con claridad el uso posterior",
            "medir calidad del lead y no sólo volumen",
        ],
        senales=[
            ("tasa de conversión del recurso", "descargas o registros, sobre visitas a la página del recurso"),
            ("calidad del lead por recurso", "leads que cumplen criterios de perfil, sobre leads capturados por ese recurso"),
            ("conversión a oportunidad", "oportunidades calificadas, sobre leads capturados por el recurso"),
        ],
        caso=(
            "El ebook «Tendencias digitales 2026» de Ruta Andina genera 300 descargas mensuales y 2 % de "
            "leads en perfil. Una calculadora de costo de inasistencias generó 40 descargas y 55 % en perfil."
        ),
        limite=(
            "Un recurso demasiado específico limita el volumen. La decisión depende del estado del pipeline y "
            "de la capacidad de trabajo del equipo comercial."
        ),
        libros=["godin", "handley", "pulizzi", "chaffey"],
        error=("Priorizar volumen de descargas sobre calidad",
               "Mide leads en perfil y conversión a oportunidad, no descargas totales."),
    ),
    dict(
        n="11",
        slug="inbound-lead-capture",
        titulo="Captura de leads entrantes",
        tesis=(
            "La captura entrante falla más por operación que por marketing: formularios largos, respuestas "
            "tardías, enrutamiento equivocado. La evidencia sobre velocidad de respuesta es consistente: la "
            "probabilidad de contactar y calificar cae drásticamente con las horas transcurridas. Un lead "
            "entrante bien atendido en minutos vale más que diez atendidos en días."
        ),
        conceptos=[
            ("velocidad de respuesta", "tiempo entre la solicitud del cliente y el primer contacto efectivo"),
            ("fricción del formulario", "cantidad y sensibilidad de los datos solicitados en la captura"),
            ("enrutamiento", "asignación del lead a la persona o equipo correcto según criterios definidos"),
            ("acuerdo de servicio interno", "compromiso de tiempo de respuesta entre marketing y ventas"),
        ],
        metodo=[
            "medir la velocidad de respuesta actual",
            "reducir el formulario a los campos indispensables",
            "definir reglas de enrutamiento y responsables",
            "establecer el acuerdo de servicio y medirlo",
            "revisar semanalmente los leads sin contactar",
        ],
        senales=[
            ("tiempo medio de primera respuesta", "minutos entre la solicitud y el primer contacto efectivo, mediana"),
            ("leads sin contactar", "leads entrantes sin contacto en 24 horas, sobre leads entrantes"),
            ("conversión por velocidad", "leads calificados, sobre leads contactados, comparado entre franjas de tiempo de respuesta"),
        ],
        caso=(
            "El formulario de Ruta Andina pide 11 campos y el tiempo medio de respuesta es 19 horas. El 31 % "
            "de los leads entrantes nunca recibe contacto."
        ),
        limite=(
            "La velocidad no compensa la falta de calificación: responder en dos minutos a un lead fuera de "
            "perfil sigue siendo tiempo comercial mal usado."
        ),
        libros=["roberge", "ross", "chaffey", "diorio"],
        error=("Pedir demasiados campos en el formulario",
               "Solicita lo mínimo para calificar y enruta; el resto se obtiene en la conversación."),
    ),
    dict(
        n="12",
        slug="lead-qualification",
        titulo="Calificación de leads",
        tesis=(
            "Calificar un lead es decidir si merece tiempo comercial. El criterio debe combinar ajuste de "
            "perfil —¿es del tipo de cliente que obtiene resultado?— y señal de problema —¿tiene la "
            "dificultad que resolvemos, ahora?—. Un modelo que sólo mide interacción digital confunde "
            "curiosidad con intención, y llena el pipeline de personas que descargaron un documento."
        ),
        conceptos=[
            ("ajuste de perfil", "correspondencia entre el lead y el perfil de cliente ideal"),
            ("señal de intención", "comportamiento que indica búsqueda activa de solución"),
            ("umbral de traspaso", "nivel a partir del cual el lead se entrega al equipo comercial"),
            ("retroalimentación de ventas", "información que ventas devuelve sobre la calidad real de los leads recibidos"),
        ],
        metodo=[
            "definir criterios de perfil y de intención por separado",
            "establecer el umbral de traspaso con evidencia de cierre",
            "instrumentar la retroalimentación de ventas",
            "recalibrar el modelo con datos de resultado",
            "documentar el acuerdo entre marketing y ventas",
        ],
        senales=[
            ("tasa de aceptación por ventas", "leads aceptados como oportunidades, sobre leads traspasados"),
            ("conversión a cliente por nivel de calificación", "clientes ganados, sobre leads del tramo, comparado entre niveles de calificación"),
            ("retroalimentación registrada", "leads con evaluación devuelta por ventas, sobre leads traspasados"),
        ],
        caso=(
            "El modelo de Ruta Andina asigna puntaje alto por abrir tres correos. Los leads con mayor puntaje "
            "convierten igual que el promedio y ventas dejó de confiar en el modelo."
        ),
        limite=(
            "Los modelos de calificación heredan los sesgos de los datos históricos: si la prospección pasada "
            "ignoró un segmento, el modelo seguirá ignorándolo."
        ),
        libros=["roberge", "diorio", "provost", "ross"],
        error=("Puntuar sólo interacción digital",
               "Combina ajuste de perfil con señal de problema y valida el modelo contra tasas de cierre reales."),
    ),
    dict(
        n="13",
        slug="secuencias-multicanal",
        titulo="Secuencias multicanal",
        tesis=(
            "Una secuencia multicanal combina correo, teléfono, redes y contacto físico en un orden y ritmo "
            "definidos. Su eficacia proviene de la repetición con variación: cada contacto aporta algo nuevo y "
            "usa un canal distinto. Su riesgo es la saturación: una secuencia demasiado agresiva convierte la "
            "persistencia en hostigamiento y daña la marca."
        ),
        conceptos=[
            ("cadencia", "número, orden y espaciamiento de los contactos de la secuencia"),
            ("variación de aporte", "contenido distinto en cada contacto, evitando la repetición del mismo mensaje"),
            ("punto de salida", "condición que retira al contacto de la secuencia"),
            ("saturación", "punto en que la insistencia produce rechazo y daño reputacional"),
        ],
        metodo=[
            "diseñar la cadencia con canales y espaciamiento definidos",
            "asignar un aporte distinto a cada contacto",
            "definir puntos de salida claros",
            "medir respuesta y solicitudes de baja por paso",
            "ajustar la cadencia con datos y no con intuición",
        ],
        senales=[
            ("respuesta por paso de la secuencia", "respuestas obtenidas en cada paso, sobre contactos entregados en ese paso"),
            ("tasa de salida por solicitud", "solicitudes de no contacto, sobre contactos de la secuencia"),
            ("costo por reunión agendada", "horas y gastos de la secuencia, dividido por reuniones agendadas"),
        ],
        caso=(
            "La secuencia de Ruta Andina tiene 14 pasos en 10 días con el mismo mensaje en tres canales. Las "
            "solicitudes de baja superan a las respuestas positivas."
        ),
        limite=(
            "Las normas de datos personales y de comunicaciones comerciales obligan a respetar la oposición de "
            "inmediato y en todos los canales, no sólo en aquel donde se solicitó."
        ),
        libros=["blount", "bertuzzi", "ross", "handley"],
        error=("Repetir el mismo mensaje en varios canales",
               "Asigna un aporte distinto a cada paso y define condiciones de salida explícitas."),
    ),
    dict(
        n="14",
        slug="sistema-de-prospeccion-repetible",
        titulo="Sistema de prospección repetible",
        tesis=(
            "Esta clase integra la parte en un sistema: perfil objetivo, fuente de listas con base de "
            "licitud, señales de oportunidad, secuencias por segmento, criterios de calificación, métricas "
            "por etapa y reglas de cumplimiento. La prueba de calidad es la predictibilidad: dado un nivel de "
            "actividad, el sistema debe permitir estimar oportunidades con un margen de error conocido."
        ),
        conceptos=[
            ("sistema de prospección", "conjunto documentado de listas, mensajes, cadencias, criterios y métricas"),
            ("predictibilidad", "capacidad de estimar resultados a partir de un nivel de actividad conocido"),
            ("capacidad de prospección", "volumen de actividad sostenible con el equipo disponible"),
            ("cumplimiento normativo del sistema", "conformidad de listas, mensajes y registros con la normativa de datos y consumo"),
        ],
        metodo=[
            "consolidar perfil, fuentes y señales",
            "documentar secuencias y criterios de calificación",
            "calcular la capacidad real del equipo",
            "verificar el cumplimiento normativo de todo el sistema",
            "medir la relación entre actividad y oportunidades por trimestre",
        ],
        senales=[
            ("relación actividad-oportunidades", "oportunidades calificadas generadas, sobre contactos de calidad realizados"),
            ("estabilidad de la relación", "variación trimestral de esa relación, por segmento"),
            ("cobertura de pipeline", "valor del pipeline generado, sobre la meta del periodo siguiente"),
        ],
        caso=(
            "Ruta Andina necesita 24 oportunidades calificadas mensuales para cumplir su meta. Hoy no puede "
            "estimar cuánta actividad se requiere ni si el equipo tiene capacidad."
        ),
        limite=(
            "Un sistema predecible en un segmento no se traslada automáticamente a otro: cada segmento tiene "
            "contactabilidad y tasas propias que deben medirse por separado."
        ),
        libros=["ross", "bertuzzi", "blount", "roberge"],
        error=("Fijar metas de pipeline sin conocer la capacidad de prospección",
               "Calcula la relación actividad-oportunidades por segmento antes de comprometer una meta."),
    ),
]
