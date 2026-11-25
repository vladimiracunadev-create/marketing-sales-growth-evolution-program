# -*- coding: utf-8 -*-
"""Ampliaciones de reputación, relaciones públicas, vocería y comunicación de crisis.

Complementan las ampliaciones A–N sin alterar la numeración del currículo. Cada
entrada se incorpora a su clase principal y remite por referencia cruzada a la
especialización «Reputación, relaciones públicas y comunicación de crisis»
(`curriculum/specializations/reputacion-relaciones-publicas-y-crisis/`), donde
se desarrolla el tema completo. Aquí sólo se agrega lo que la clase huésped
necesita para no quedar incompleta.
"""

from spec.ampliaciones_integrales import ia, metrica

ESPECIALIZACION = "reputacion-relaciones-publicas-y-crisis"

AMPLIACIONES_REPUTACION = {
    "06.10": [dict(
        eje="O", titulo="Reputación, daño y reparación verificable",
        conceptos=[
            ("capital reputacional", "confianza acumulada de los públicos clave que reduce el costo de ser creídos y absorbe parte del daño de un error"),
            ("control de daños", "conjunto de acciones para limitar el perjuicio a las personas afectadas y a la organización mientras se establecen los hechos"),
            ("encubrimiento", "ocultar, retrasar sin justificación o deformar hechos relevantes para evitar consecuencias; es lo opuesto al control de daños legítimo"),
            ("reparación verificable", "medida correctiva con responsable, plazo y evidencia que un tercero puede comprobar"),
            ("crisis", "evento que amenaza expectativas de los públicos, exige decisiones en plazos cortos y puede afectar la continuidad o la legitimidad de la organización"),
        ],
        teoria=[
            "Esta clase trata la confianza como resultado de conducta observable. La ampliación separa siete fases que suelen mezclarse: prevención (reducir la probabilidad), detección (ver a tiempo), contención (limitar el daño), respuesta (decir y hacer lo necesario), corrección (arreglar la causa), recuperación (recomponer la confianza con evidencia) y aprendizaje (cambiar el sistema). Un equipo que sólo domina la respuesta llega tarde a todo lo demás.",
            "Control de daños no es encubrimiento. Controlar daños es proteger primero a quienes pueden resultar afectados, establecer hechos y comunicar lo confirmado, lo incierto y lo que se hará. Encubrir es retener o deformar información relevante. La frontera se prueba con una pregunta: si la información completa se hiciera pública mañana, ¿la comunicación de hoy resultaría engañosa por omisión? Si la respuesta es sí, ya no es gestión de crisis sino un segundo problema, con riesgos jurídicos y reputacionales propios.",
            "Responder no siempre es hablar más. Corresponde responder cuando hay personas afectadas, la señal tiene fuente verificable y su alcance puede crecer; corresponde reconocer un error cuando la evidencia interna lo confirma; corresponde pedir disculpas cuando la organización causó el daño y puede nombrar qué hará distinto; corresponde corregir cuando circula información falsa que afecta decisiones; corresponde suspender publicaciones cuando el calendario puede agravar el conflicto; y corresponde escalar cuando el hecho supera la autoridad, el conocimiento o el riesgo jurídico del equipo.",
        ],
        marco=[
            ("Prevención y detección", "reducir probabilidad y ver a tiempo", "registrar riesgos, dueños y umbrales de alerta"),
            ("Contención y respuesta", "limitar el daño y comunicar lo confirmado", "activar protocolo con dueño, canal y plazo"),
            ("Corrección y recuperación", "reparar la causa y recomponer confianza", "publicar medida, fecha y evidencia de cumplimiento"),
            ("Aprendizaje", "cambiar proceso, política o producto", "cerrar con revisión posterior y acciones con responsable"),
            ("Límite ético", "no engañar por acción ni por omisión", "someter el texto a la prueba de publicación completa"),
        ],
        actividad=dict(
            consigna="Una nueva versión de Ruta Andina duplica citas en la agenda de 80 clientes durante 36 horas. Aún no se conoce la causa, 12 clientes ya reclamaron en redes y existe una campaña programada para mañana. Decide qué hacer en las primeras tres horas: responder o esperar, qué reconocer, qué suspender y a quién escalar.",
            pasos=["clasificar hechos confirmados, inciertos y supuestos", "identificar afectados y daño inmediato", "decidir qué se suspende y qué se comunica", "asignar dueño, canal y hora de la próxima actualización"],
            solucion="Se reconoce el fallo con lo confirmado (duplicación, rango horario, clientes afectados), se declara que la causa se investiga y se fija hora de próxima actualización. Se suspende la campaña programada porque promocionar un servicio con falla activa agrava la percepción. Se contacta directamente a los 80 clientes con instrucciones para corregir citas. No se atribuye la causa a un proveedor sin evidencia ni se promete que no volverá a ocurrir. La decisión de compensar se escala a dirección si implica costo o compromiso contractual.",
            evidencia="registro de decisiones de las tres primeras horas, texto de la primera declaración y lista de afectados contactados",
            rubrica="30 % distinción hechos/supuestos; 25 % protección de afectados; 25 % decisión sobre suspender y escalar; 20 % ausencia de promesas no verificables",
        ),
        metricas=[metrica("tiempo hasta primera comunicación confirmada", "minutos entre la detección verificada y la primera comunicación a afectados", "incidentes con afectados identificables", "por incidente y trimestre", "registro de incidentes y bitácora de comunicación", "Responsable de comunicaciones", "muestra velocidad de respuesta a partir de una detección confirmada", "no mide calidad del contenido ni evita que un mensaje rápido sea incorrecto")],
        ia=ia("preparar borradores de declaración y listas de preguntas probables", "hechos confirmados, supuestos marcados y público afectado, sin datos personales", "Con los hechos confirmados que te entrego, redacta una declaración breve que no afirme nada fuera de ellos. Lista las preguntas difíciles probables y marca qué respuesta aún no puede darse.", "borrador de declaración y banco de preguntas", "responsable jurídico y dueño del hecho contrastan cada frase con la evidencia antes de publicar", "afirmaciones no verificadas, tono evasivo y filtración de datos de afectados", "plantillas aprobadas con anterioridad y revisión por dos personas"),
        transferencias=["falla de producto", "reclamo masivo de consumidores", "error de publicidad", "incidente con datos de clientes"],
        referencias=["06.12", "06.13", "13.12", "18.10", "21.12", "23.12"],
    )],
    "06.11": [dict(
        eje="P", titulo="Marca personal, vocería y marca empleadora bajo exposición pública",
        conceptos=[
            ("vocería", "función de hablar en nombre de una organización con mensajes autorizados, preparación previa y límites definidos"),
            ("mensaje central", "idea que la persona vocera debe dejar clara aunque la conversación se desvíe"),
            ("pregunta difícil", "pregunta que expone un riesgo, un error o un conflicto y cuya respuesta puede ser citada fuera de contexto"),
            ("exposición pública del empleado", "conducta o declaración de una persona de la organización que, por su rol o por su alcance, puede ser atribuida a la empresa"),
        ],
        teoria=[
            "La marca personal de empleados, profesionales, fundadores, ejecutivos y figuras públicas comparte un mecanismo: otras personas repiten lo que creen saber de ti. Lo que cambia es el riesgo. Un empleado comunica sobre todo su trabajo y sus criterios; un ejecutivo o fundador comunica también a la organización, y cada declaración puede interpretarse como postura corporativa. Por eso la política de redes no se limita a prohibir: define qué se habla a título personal, qué requiere autorización y qué se deriva a vocería.",
            "La vocería se prepara como una decisión, no como un talento. Se acuerda el mensaje central, se identifican las tres preguntas más difíciles, se escribe qué se puede y qué no se puede decir, y se ensaya la respuesta a cada una. La respuesta a una pregunta difícil sigue un orden: reconocer lo que se sabe, decir lo que se hace, declarar lo que se ignora y comprometer cuándo se informará. Cambiar de tema o improvisar cifras es la causa más frecuente de una crisis secundaria.",
            "La marca empleadora comparte el mismo principio de coherencia: lo que la empresa promete a candidatos debe corresponder con lo que viven los equipos. Una controversia de un empleado o de un influencer asociado a la marca se analiza con cuatro preguntas: ¿hay hecho verificable?, ¿afecta a personas o a la legalidad?, ¿habla a título personal o corporativo?, ¿qué obliga la norma laboral antes de actuar? La respuesta rara vez es inmediata ni pública.",
        ],
        marco=[
            ("Mensaje central", "idea única que debe quedar", "someter a prueba de cita aislada"),
            ("Pregunta difícil", "riesgo o error expuesto", "preparar respuesta con hecho, acción, incertidumbre y plazo"),
            ("Alcance de la persona", "título personal o corporativo", "aclarar en política de redes y contrato"),
            ("Controversia de empleado", "conducta atribuible a la organización", "verificar hecho, derecho aplicable y proporcionalidad"),
            ("Influencer asociado", "persona con acuerdo comercial", "exigir divulgación, cláusula de conducta y plan de salida"),
        ],
        actividad=dict(
            consigna="La gerente comercial de Ruta Andina será entrevistada sobre una caída del servicio. Prepara el mensaje central, tres preguntas difíciles y las respuestas que sí puede dar. Una de las preguntas es cuánto dinero perdieron los clientes.",
            pasos=["definir el mensaje central", "listar tres preguntas difíciles", "escribir hecho, acción, incertidumbre y plazo por pregunta", "ensayar y detectar frases citables fuera de contexto"],
            solucion="Mensaje central: «Reconocemos la falla, protegimos a los clientes afectados y publicaremos la causa el viernes». Para la pregunta de pérdidas se responde con lo medido (clientes afectados y horas), se declara que aún no existe una cifra confiable de pérdida por cliente, se explica cómo se recogerá y se compromete fecha. No se improvisa un monto ni se minimiza.",
            evidencia="guion de vocería con mensaje central, tres preguntas, respuestas y observaciones del ensayo",
            rubrica="25 % mensaje central; 30 % calidad de respuestas difíciles; 25 % honestidad ante lo desconocido; 20 % revisión de frases citables",
        ),
        metricas=[metrica("preparación de vocería completada", "voceros con mensaje central, banco de preguntas y ensayo documentado antes de una exposición", "voceros con exposición prevista", "por trimestre", "registro de capacitación y agenda de exposiciones", "Comunicaciones", "indica si la exposición se preparó con método", "no mide el desempeño real ni la recepción del público")],
        ia=ia("simular preguntas difíciles de un entrevistador", "mensaje central, hechos autorizados y perfil de la audiencia", "Actúa como un entrevistador escéptico. Formula diez preguntas difíciles sobre estos hechos autorizados. No inventes datos ni cifras sobre la empresa.", "banco de preguntas para ensayo", "el vocero y comunicaciones descartan preguntas fuera de contexto y completan respuestas con evidencia", "preguntas irreales, falsa seguridad y uso de información reservada", "ensayo con un colega que juegue el papel de entrevistador"),
        transferencias=["ejecutivo en medios", "fundador en redes", "empleado con perfil público", "influencer contratado"],
        referencias=["06.10", "06.12", "11.06", "23.12"],
    )],
    "03.11": [dict(
        eje="Q", titulo="Escucha social, percepción y alertas tempranas",
        conceptos=[
            ("señal débil", "mención aislada o patrón incipiente que todavía no alcanza volumen pero puede anticipar un conflicto"),
            ("umbral de alerta", "valor predefinido de volumen, velocidad o sentimiento que activa una revisión humana"),
            ("rumor", "afirmación sin verificar que circula entre personas; no es lo mismo que desinformación, que exige falsedad e intención de dañar"),
            ("severidad de una señal", "combinación de alcance potencial, credibilidad de la fuente y daño posible a personas o a la organización"),
        ],
        teoria=[
            "La escucha social descrita en esta clase sirve también para reputación: detectar controversias, rumores y conflictos emergentes antes de que se conviertan en crisis. La diferencia con la investigación de mercado es el plazo. Aquí interesa la velocidad: ¿cuántas menciones por hora?, ¿qué cuentas amplifican?, ¿hay hechos verificables o sólo opinión?",
            "Una alerta útil combina tres variables y no una: volumen, velocidad de crecimiento y severidad. Un aumento de menciones sin personas afectadas no equivale a una crisis, y una sola mención grave de una persona con daño real puede requerir acción inmediata. Las herramientas automáticas clasifican sentimiento con errores conocidos, sobre todo en ironía y modismos locales; por eso toda alerta crítica pasa por revisión humana.",
        ],
        marco=[
            ("Señal débil", "mención o patrón incipiente", "observar y registrar sin responder"),
            ("Señal confirmada", "hecho verificable con afectados", "activar protocolo y asignar dueño"),
            ("Rumor", "afirmación sin verificar", "verificar fuente antes de decidir si se corrige"),
            ("Ataque coordinado", "patrón de cuentas y tiempos anómalos", "documentar, reportar a la plataforma y escalar"),
        ],
        actividad=dict(
            consigna="En una hora aparecen 140 menciones sobre un supuesto cobro duplicado de Ruta Andina. 90 provienen de 12 cuentas creadas hace menos de una semana; 6 son clientes reales con comprobante.",
            pasos=["separar cuentas reales de patrón anómalo", "verificar los seis casos con registros internos", "clasificar severidad", "decidir respuesta y escalamiento"],
            solucion="Los seis casos reales se tratan como señal confirmada: se verifica el cobro, se contacta a cada cliente y se corrige. Las 90 menciones de cuentas nuevas se documentan como posible amplificación artificial y se reportan a la plataforma, sin responderles individualmente. Se prepara una declaración sobre lo verificado y se escala porque hay clientes con perjuicio y un patrón coordinado.",
            evidencia="tabla de menciones clasificadas, verificación interna y decisión documentada",
            rubrica="30 % separación entre patrón y casos reales; 25 % verificación; 25 % decisión proporcional; 20 % documentación",
        ),
        metricas=[metrica("alertas críticas verificadas", "alertas con hecho confirmado tras revisión humana", "alertas críticas emitidas", "mensual", "panel de escucha y bitácora de verificación", "Social Listening Lead", "mide precisión del sistema de alertas", "no mide cobertura de lo que el sistema no detectó")],
        ia=ia("agrupar menciones y detectar patrones anómalos", "menciones públicas anonimizadas con fecha, plataforma y antigüedad de cuenta", "Agrupa las menciones por tema. Señala patrones de tiempo y antigüedad de cuentas que parezcan anómalos y explica por qué. No concluyas que son falsas.", "mapa de temas y patrones sospechosos", "analista verifica una muestra y confirma o descarta cada patrón", "falsos positivos, sesgo de idioma y perfilado de personas", "revisión manual por muestra y reglas simples de volumen"),
        transferencias=["reclamos de consumidores", "controversia de ejecutivo", "rumor sobre producto", "campaña de reseñas falsas"],
        referencias=["06.10", "12.07", "21.12"],
    )],
    "12.07": [dict(
        eje="R", titulo="Community management y respuesta multiplataforma",
        conceptos=[
            ("moderación", "aplicación coherente de reglas de conversación publicadas, sin borrar críticas legítimas"),
            ("protocolo de escalamiento", "regla que define qué consulta pública pasa a atención, jurídico o dirección y en qué plazo"),
            ("silencio de calendario", "suspensión deliberada de publicaciones programadas durante un incidente"),
            ("respuesta pública y privada", "separación entre lo que se contesta en abierto y lo que se resuelve por un canal con datos personales"),
        ],
        teoria=[
            "Community management es la operación diaria que decide cómo se ve la empresa cuando alguien reclama en público. Las reglas de conversación se publican, se aplican igual a todos y distinguen crítica de abuso: borrar críticas legítimas es un incidente en sí mismo. Lo que se resuelve en abierto es la confirmación de que se atiende; lo que contiene datos personales se traslada a un canal privado.",
            "En una crisis, cada plataforma exige un formato distinto: una publicación fijada en el perfil, una respuesta breve en comentarios, un comunicado en el sitio, un aviso en el producto y un correo a los afectados. La fuente de verdad es una sola y las demás la remiten. Antes de publicar, se revisa si el calendario programado contiene mensajes promocionales que contradicen la situación.",
        ],
        marco=[
            ("Crítica legítima", "queja con hecho verificable", "responder y resolver, no borrar"),
            ("Abuso", "insulto, amenaza o spam", "aplicar regla publicada y registrar"),
            ("Dato personal en público", "información sensible expuesta", "ocultar según política y trasladar a canal privado"),
            ("Incidente activo", "falla o crisis en curso", "suspender calendario y fijar comunicado único"),
        ],
        actividad=dict(
            consigna="Durante la caída del servicio hay 40 comentarios en Instagram, 25 en X y 18 reclamos por correo. Hay también una publicación promocional programada. Diseña la respuesta por plataforma.",
            pasos=["definir comunicado único", "adaptar formato por plataforma", "suspender lo programado", "trasladar casos con datos a canal privado"],
            solucion="Se fija un comunicado único en el sitio y se enlaza desde cada plataforma. En Instagram se responde con una frase y el enlace; en X una actualización breve con hora de la próxima; por correo se envía un mensaje directo a afectados. Se suspende la publicación promocional. Cualquier cliente que entregue datos en público recibe indicación de moverse a un canal privado.",
            evidencia="comunicado único, respuestas por plataforma y registro de la suspensión",
            rubrica="30 % coherencia; 25 % formato por plataforma; 25 % protección de datos; 20 % control de calendario",
        ),
        metricas=[metrica("tiempo de primera respuesta pública", "minutos desde el comentario hasta la primera respuesta del equipo", "comentarios que requieren respuesta", "diario y por incidente", "herramienta de gestión social", "Community Manager", "mide capacidad de atención en abierto", "no mide si el reclamo quedó resuelto")],
        ia=ia("clasificar comentarios y sugerir respuestas", "comentarios públicos sin datos personales y política de conversación", "Clasifica estos comentarios en crítica legítima, abuso, consulta y spam. Sugiere una respuesta breve sin prometer plazos ni compensaciones.", "clasificación y borradores", "el Community Manager aprueba cada respuesta antes de publicar", "respuestas genéricas, promesas no autorizadas y errores de tono", "banco de respuestas aprobadas y revisión humana"),
        transferencias=["falla de producto", "reclamo viral", "publicidad cuestionada", "ataque de cuentas falsas"],
        referencias=["06.10", "12.08", "03.11", "18.10"],
    )],
    "13.12": [dict(
        eje="S", titulo="Prueba social, publicidad engañosa y reputación",
        conceptos=[
            ("publicidad engañosa", "mensaje comercial que induce a error sobre características, precio, condiciones o resultados de lo ofrecido"),
            ("reseña auténtica", "opinión de una persona con experiencia real, sin pago oculto ni incentivo condicionado a su signo"),
            ("cuenta falsa", "perfil que simula identidad o comportamiento orgánico para influir en la percepción"),
            ("retractación", "corrección pública de una afirmación comercial que resultó inexacta"),
        ],
        teoria=[
            "La prueba social crea reputación solo si es verificable. Reseñas compradas, testimonios sin consentimiento o cifras sin fuente convierten un activo en un riesgo: si se descubre, el daño excede el beneficio de la mejora de conversión. La regla práctica es publicar solo lo que puede respaldarse con un registro que un tercero pueda revisar.",
            "Cuando un mensaje resulta engañoso, aun sin intención, la respuesta correcta es retirar, corregir y explicar qué cambió. Defender el mensaje original agrava el problema. Si la publicidad ya produjo decisiones de compra, corresponde evaluar compensación y comunicación directa a quienes compraron.",
        ],
        marco=[
            ("Afirmación con respaldo", "dato o resultado documentado", "publicar con fuente y fecha"),
            ("Afirmación sin respaldo", "promesa o cifra sin registro", "retirar o reformular"),
            ("Reseña incentivada", "opinión con beneficio asociado", "declarar el incentivo"),
            ("Reseñas sospechosas", "patrón anómalo de cuentas", "reportar, no responder en bloque"),
        ],
        actividad=dict(
            consigna="La landing de Ruta Andina dice «reduce inasistencias en 60 %» a partir de un piloto con cuatro clientes. Un periodista consulta por la cifra.",
            pasos=["rastrear la fuente de la cifra", "evaluar tamaño y condiciones del piloto", "decidir retirar, matizar o respaldar", "preparar la respuesta al periodista"],
            solucion="La cifra proviene de un piloto pequeño sin grupo de comparación, por lo que no puede presentarse como resultado general. Se retira de la landing, se reformula como resultado del piloto con su tamaño y se responde al periodista con la fuente, el límite y la corrección realizada. No se discute la intención.",
            evidencia="registro de la fuente, versión corregida y texto de respuesta",
            rubrica="30 % rastreo de evidencia; 30 % decisión proporcional; 25 % transparencia; 15 % tono",
        ),
        metricas=[metrica("afirmaciones comerciales con respaldo", "afirmaciones publicadas con fuente archivada", "afirmaciones publicadas", "trimestral", "inventario de afirmaciones y evidencias", "Marketing y Legal", "mide higiene de evidencia previa a campaña", "no prueba que el respaldo sea suficiente en sede regulatoria")],
        ia=ia("detectar afirmaciones sin respaldo en una pieza", "texto de la pieza y lista de evidencias disponibles", "Lista cada afirmación cuantitativa o de resultado de este texto y marca si existe evidencia en la lista entregada. No inventes fuentes.", "inventario de afirmaciones", "Legal contrasta cada afirmación con su evidencia", "falsos respaldos y omisiones", "revisión manual con checklist"),
        transferencias=["landing de producto", "campaña pagada", "testimonios de clientes", "reseñas de marketplace"],
        referencias=["06.10", "13.13", "14.13"],
    )],
    "21.12": [dict(
        eje="T", titulo="Desinformación, suplantación y deepfakes: verificación y respuesta",
        conceptos=[
            ("suplantación de identidad", "uso no autorizado del nombre, imagen, voz o cuenta de una persona u organización"),
            ("deepfake", "contenido sintético que imita rostro o voz de una persona para aparentar hechos o declaraciones que no ocurrieron"),
            ("procedencia de contenido", "registro verificable de origen y modificaciones de una pieza"),
            ("verificación independiente", "contraste de una afirmación con una fuente que no depende de quien la difunde"),
        ],
        teoria=[
            "La IA reduce el costo de producir mensajes falsos creíbles y también el de comunicar con rapidez. La organización necesita ambos conocimientos: cómo detectar y responder a contenido sintético que la suplanta, y cómo usar IA como apoyo de redacción sin delegar el juicio. Distinguir información errónea, desinformación y malinformación evita atribuir intención donde solo hay error.",
            "Ante un deepfake o suplantación se actúa en tres planos: verificar (¿hay registro original?, ¿hay fallas técnicas?, ¿puede confirmarse con la persona?), contener (reportar a la plataforma, avisar a quienes puedan ser engañados, preservar evidencia) y comunicar (desmentir con evidencia, canales oficiales y sin amplificar innecesariamente el contenido falso).",
        ],
        marco=[
            ("Contenido sospechoso", "pieza con indicios de manipulación", "preservar y verificar antes de responder"),
            ("Suplantación confirmada", "cuenta o mensaje falso", "reportar, avisar y publicar canales oficiales"),
            ("Información errónea", "falsedad sin intención de dañar", "corregir con evidencia"),
            ("Desinformación coordinada", "falsedad intencional y patrón", "documentar, escalar y evaluar acción legal"),
        ],
        actividad=dict(
            consigna="Circula un audio atribuido al gerente de Ruta Andina que anuncia el cierre de la empresa. El gerente confirma que nunca lo grabó. Define verificación, contención y comunicación.",
            pasos=["preservar el audio y su origen", "confirmar con la persona y con análisis técnico", "reportar y avisar a públicos clave", "publicar desmentido en canales oficiales"],
            solucion="Se guarda el archivo y su trayectoria de difusión, se pide análisis técnico y se confirma con el gerente. Se reporta a la plataforma, se avisa a clientes y empleados por canal oficial y se publica un desmentido breve con evidencia, sin repetir el contenido falso. Se evalúa denuncia con asesoría jurídica.",
            evidencia="registro de verificación, avisos enviados y desmentido publicado",
            rubrica="30 % verificación; 25 % contención; 25 % comunicación; 20 % criterio jurídico",
        ),
        metricas=[metrica("incidentes de suplantación contenidos", "incidentes con retiro o reporte confirmado dentro de 48 horas", "incidentes de suplantación detectados", "trimestral", "registro de incidentes y respuestas de plataformas", "Seguridad y Comunicaciones", "mide capacidad de contención", "no mide el daño ya producido antes de la detección")],
        ia=ia("apoyar la redacción de desmentidos y la preparación de materiales", "hechos verificados y canales oficiales", "Redacta un desmentido breve usando solo estos hechos verificados. No repitas el contenido falso ni agregues datos.", "borrador de desmentido", "responsable verifica cada afirmación y Legal aprueba", "inclusión de datos no verificados y amplificación del falso", "plantilla de desmentido preaprobada"),
        transferencias=["suplantación de ejecutivo", "cuenta falsa de atención", "audio o video manipulado", "falsa oferta de empleo"],
        referencias=["06.10", "03.11", "21.13"],
    )],
    "23.13": [dict(
        eje="U", titulo="Partes interesadas, asuntos públicos y gestión de controversias",
        conceptos=[
            ("parte interesada", "persona o grupo que puede afectar o ser afectado por las decisiones de la organización"),
            ("prominencia", "grado de atención que merece una parte interesada según su poder, legitimidad y urgencia"),
            ("asuntos públicos", "relación de la organización con autoridades, reguladores y políticas que afectan su operación"),
            ("gestión de controversias", "identificación temprana de temas que pueden transformarse en conflicto público y decisión sobre su tratamiento"),
        ],
        teoria=[
            "El reporte al directorio incluye riesgos que no figuran en el tablero comercial: relación con reguladores, comunidad, medios, empleados y proveedores. La matriz de partes interesadas registra, para cada una, qué espera, qué puede hacer a la organización, qué canal la alcanza y quién es el responsable. Priorizar por poder, legitimidad y urgencia evita atender solo a quien grita más fuerte.",
            "La gestión de controversias es un proceso previo a la crisis: se identifican temas con potencial de conflicto, se evalúa su probabilidad e impacto, se decide si se prepara posición, se dialoga o se ajusta la práctica. Los asuntos públicos operan dentro de la transparencia: la influencia legítima se declara y se documenta, no se ejerce de forma opaca.",
        ],
        marco=[
            ("Poder", "capacidad de afectar a la organización", "evaluar con evidencia, no con intuición"),
            ("Legitimidad", "derecho reconocido a reclamar", "distinguir de la capacidad de hacer ruido"),
            ("Urgencia", "plazo y criticidad del reclamo", "ordenar la agenda de respuesta"),
            ("Tema emergente", "controversia potencial", "decidir preparar, dialogar o ajustar práctica"),
        ],
        actividad=dict(
            consigna="Ruta Andina debe priorizar cinco partes interesadas ante un incidente de datos: clientes afectados, regulador, medio local, empleados y un influencer del rubro. Construye la matriz y define el orden de contacto.",
            pasos=["describir expectativa y canal por parte", "puntuar poder, legitimidad y urgencia", "ordenar prioridad", "asignar responsable y plazo"],
            solucion="Clientes afectados y regulador concentran legitimidad y urgencia; se contactan primero y con texto aprobado por Legal. Empleados se informan inmediatamente después para que no se enteren por medios. El medio local recibe una declaración al publicarse la comunicación a afectados. El influencer se atiende con la misma información pública, sin trato privilegiado.",
            evidencia="matriz de partes interesadas con prioridad, canal, responsable y plazo",
            rubrica="30 % criterio de priorización; 25 % canal adecuado; 25 % coherencia del mensaje; 20 % responsabilidad y plazo",
        ),
        metricas=[metrica("temas emergentes con posición definida", "temas priorizados con posición y responsable", "temas priorizados", "trimestral", "registro de controversias y comité", "Asuntos Corporativos", "mide preparación previa a la controversia", "no mide la evolución pública del tema")],
        ia=ia("ordenar información de partes interesadas y escenarios", "registro anonimizado de reclamos, normas y expectativas", "Resume por parte interesada las expectativas que aparecen en el registro. Indica qué datos faltan y no asignes puntajes sin criterios.", "resumen por parte interesada", "responsable valida expectativas con fuentes", "supuestos sobre personas y sesgo de selección", "taller con matriz impresa"),
        transferencias=["incidente de datos", "cambio regulatorio", "conflicto con comunidad", "controversia pública del sector"],
        referencias=["06.10", "23.12", "24.12"],
    )],
}
