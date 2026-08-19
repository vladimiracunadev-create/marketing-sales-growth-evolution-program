# -*- coding: utf-8 -*-
"""Parte 12 — Marketing digital y adquisición."""

CLASES = [
    dict(
        n="01",
        slug="estrategia-digital",
        titulo="Estrategia digital",
        tesis=(
            "Una estrategia digital decide qué activos propios se construyen y qué audiencia se alquila. La "
            "distinción es económica: el tráfico pagado se detiene cuando se detiene el pago; un sitio con "
            "autoridad, una lista propia y una comunidad siguen produciendo. Chaffey ordena la planificación "
            "en objetivos, audiencias, propuesta, canales y medición. El error habitual es partir por el "
            "canal de moda y construir la estrategia hacia atrás para justificarlo."
        ),
        conceptos=[
            ("activo propio", "recurso digital que la empresa controla y que produce demanda sin gasto marginal"),
            ("audiencia alquilada", "acceso a personas que depende de un pago o de una plataforma de terceros"),
            ("objetivo digital", "resultado de negocio que la actividad digital debe producir, no una métrica de plataforma"),
            ("dependencia de plataforma", "riesgo de que un cambio de reglas externo elimine una fuente de demanda"),
        ],
        metodo=[
            "definir el objetivo de negocio antes que el canal",
            "inventariar activos propios y audiencias alquiladas",
            "estimar la dependencia de cada plataforma",
            "asignar presupuesto entre construcción y activación",
            "definir la medición antes de ejecutar",
        ],
        senales=[
            ("proporción de demanda propia", "oportunidades originadas por activos propios, sobre oportunidades digitales totales"),
            ("concentración por plataforma", "demanda originada en la plataforma principal, sobre demanda digital total"),
            ("costo por oportunidad por canal", "gasto del canal dividido por oportunidades calificadas originadas"),
        ],
        caso=(
            "El 84 % de la demanda digital de Ruta Andina proviene de una sola plataforma publicitaria. Un "
            "cambio de política de esa plataforma dejaría el pipeline sin origen en dos semanas."
        ),
        limite=(
            "Construir activos propios tarda meses y no resuelve una necesidad inmediata de pipeline. La "
            "asignación debe equilibrar el corto y el largo plazo de forma explícita."
        ),
        libros=["chaffey", "binet-field", "kaushik", "weinberg-traction"],
        error=("Elegir canal antes de definir el objetivo",
               "Declara el resultado de negocio y la audiencia antes de decidir en qué plataforma invertir."),
    ),
    dict(
        n="02",
        slug="sitio-web-como-activo-comercial",
        titulo="El sitio web como activo comercial",
        tesis=(
            "Un sitio comercial tiene una función: ayudar a una persona a decidir. Eso exige responder qué "
            "es, para quién, qué problema resuelve, cuánto cuesta y qué pasa después. Krug demostró que la "
            "usabilidad se juega en segundos: si el visitante debe pensar para entender dónde está, ya se "
            "perdió una parte. Las páginas que hablan de la empresa antes que del problema del visitante "
            "convierten sistemáticamente peor."
        ),
        conceptos=[
            ("claridad de propuesta", "capacidad del sitio de comunicar qué ofrece y para quién en pocos segundos"),
            ("ruta de conversión", "secuencia de páginas y acciones que lleva de la llegada al contacto"),
            ("transparencia de precio", "información de costo suficiente para que el visitante se autocalifique"),
            ("prueba de cinco segundos", "verificación de qué comprende una persona tras una exposición muy breve"),
        ],
        metodo=[
            "definir la decisión que el visitante debe poder tomar",
            "estructurar la página desde el problema y no desde la empresa",
            "hacer visible la ruta de conversión",
            "aplicar la prueba de cinco segundos con usuarios reales",
            "medir conversión por página y corregir la peor primero",
        ],
        senales=[
            ("tasa de conversión por página", "acciones de contacto, sobre visitas únicas de la página, mensual"),
            ("comprensión en prueba breve", "personas que explican correctamente la oferta tras cinco segundos, sobre expuestas"),
            ("tasa de rebote por página de entrada", "sesiones de una sola página, sobre sesiones que entraron por esa página"),
        ],
        caso=(
            "La página de inicio de Ruta Andina abre con «Somos una empresa chilena con más de 18 meses de "
            "experiencia». No dice qué hace el producto ni cuánto cuesta."
        ),
        limite=(
            "Un sitio excelente no compensa la ausencia de demanda: si nadie llega, la conversión se aplica "
            "sobre cero. El diagnóstico debe distinguir problema de tráfico de problema de conversión."
        ),
        libros=["krug", "eisenberg", "laja", "chaffey"],
        error=("Escribir el sitio desde la perspectiva de la empresa",
               "Reescribe la primera pantalla respondiendo qué es, para quién y qué problema resuelve."),
    ),
    dict(
        n="03",
        slug="landing-pages",
        titulo="Landing pages",
        tesis=(
            "Una landing page tiene un solo objetivo y su diseño debe eliminar todo lo que compita con él. "
            "La coherencia con el anuncio o el correo de origen es determinante: si la promesa cambia entre "
            "el clic y la página, la persona se va. El trabajo serio de conversión empieza antes del test: "
            "investigación de objeciones, claridad de la oferta y eliminación de fricción."
        ),
        conceptos=[
            ("coherencia mensaje-página", "correspondencia entre lo prometido en el origen y lo que muestra la página"),
            ("objetivo único", "acción específica que la página busca producir, sin alternativas que compitan"),
            ("manejo de objeciones en página", "respuesta anticipada a las dudas que frenan la conversión"),
            ("fricción de formulario", "esfuerzo que impone la captura de datos sobre el visitante"),
        ],
        metodo=[
            "definir el objetivo único de la página",
            "verificar la coherencia con el mensaje de origen",
            "incorporar respuestas a las objeciones documentadas",
            "reducir la fricción al mínimo necesario",
            "probar una variable a la vez con muestra suficiente",
        ],
        senales=[
            ("tasa de conversión de la página", "conversiones, sobre visitas únicas, por fuente de tráfico"),
            ("coherencia auditada", "páginas cuyo mensaje coincide con su origen, sobre páginas auditadas"),
            ("abandono de formulario", "abandonos en el formulario, sobre inicios de formulario"),
        ],
        caso=(
            "El anuncio de Ruta Andina promete «prueba gratis 30 días» y la landing exige datos de tarjeta y "
            "habla de una demo con un ejecutivo. La conversión es 0,9 %."
        ),
        limite=(
            "Optimizar la página no arregla una oferta débil ni un tráfico mal segmentado. Antes de testear, "
            "hay que verificar que el visitante corresponde al perfil."
        ),
        libros=["laja", "eisenberg", "krug", "kohavi"],
        error=("Romper la coherencia entre anuncio y página",
               "Audita que la promesa del origen aparezca literalmente en la primera pantalla de la landing."),
    ),
    dict(
        n="04",
        slug="seo-tecnico-y-de-contenido",
        titulo="SEO técnico y de contenido",
        tesis=(
            "El SEO combina tres dimensiones: que el sitio sea rastreable e indexable, que el contenido "
            "responda mejor que las alternativas a una intención de búsqueda, y que existan señales de "
            "autoridad. Es un activo de largo plazo con costo hundido alto: los resultados tardan meses y "
            "por eso se abandona antes de que rinda. La intención de búsqueda es el criterio central: "
            "posicionar para términos sin intención comercial produce tráfico sin negocio."
        ),
        conceptos=[
            ("intención de búsqueda", "objetivo real de quien busca: informarse, comparar o comprar"),
            ("rastreabilidad", "capacidad de los buscadores de acceder e indexar el contenido del sitio"),
            ("autoridad", "señales externas que respaldan la credibilidad del sitio en un tema"),
            ("canibalización de contenido", "competencia entre páginas propias por la misma intención de búsqueda"),
        ],
        metodo=[
            "mapear intenciones de búsqueda del segmento",
            "auditar rastreabilidad e indexación",
            "producir contenido que responda mejor que las alternativas",
            "construir autoridad con fuentes legítimas",
            "medir posición, tráfico e ingresos por intención",
        ],
        senales=[
            ("tráfico orgánico por intención", "sesiones orgánicas segmentadas por tipo de intención, mensual"),
            ("posición media por término prioritario", "posición promedio en los términos definidos como prioritarios"),
            ("conversión del tráfico orgánico", "oportunidades calificadas, sobre sesiones orgánicas, por tipo de intención"),
        ],
        caso=(
            "Ruta Andina posiciona primero para «qué es un software de agendamiento», un término informativo "
            "que trae 4.000 visitas mensuales y ninguna oportunidad."
        ),
        limite=(
            "Los algoritmos cambian y las posiciones no son propiedad de nadie. Depender exclusivamente del "
            "SEO reproduce el riesgo de plataforma que se buscaba evitar."
        ),
        libros=["enge-seo", "chaffey", "pulizzi", "kaushik"],
        error=("Producir contenido sin analizar la intención",
               "Clasifica cada término por intención y prioriza los que corresponden a evaluación y compra."),
    ),
    dict(
        n="05",
        slug="sem",
        titulo="SEM",
        tesis=(
            "La búsqueda pagada compra intención existente: por eso suele ser el canal de mayor conversión y "
            "también el más caro por clic. Su gestión exige entender la subasta —no gana quien más paga sino "
            "quien combina oferta y relevancia—, la estructura de cuenta y la coincidencia de términos. El "
            "error costoso es dejar coincidencias amplias sin exclusiones: el presupuesto se consume en "
            "búsquedas irrelevantes."
        ),
        conceptos=[
            ("intención comercial", "señal de que la búsqueda busca comprar o evaluar y no sólo informarse"),
            ("nivel de calidad", "evaluación de la plataforma sobre relevancia que afecta el costo por clic"),
            ("término de exclusión", "palabra que impide mostrar el anuncio en búsquedas irrelevantes"),
            ("estructura de cuenta", "organización de campañas y grupos que permite controlar presupuesto y relevancia"),
        ],
        metodo=[
            "seleccionar términos por intención comercial",
            "estructurar campañas por intención y no por producto",
            "construir la lista de exclusiones desde el informe de búsquedas",
            "vincular cada anuncio a una página coherente",
            "medir costo por oportunidad y no por clic",
        ],
        senales=[
            ("costo por oportunidad calificada", "gasto de la campaña dividido por oportunidades calificadas originadas"),
            ("proporción de gasto en búsquedas irrelevantes", "gasto en términos excluidos posteriormente, sobre gasto total del periodo"),
            ("tasa de conversión por grupo de anuncios", "conversiones, sobre clics, por grupo de anuncios"),
        ],
        caso=(
            "El informe de búsquedas de Ruta Andina muestra que el 38 % del gasto se fue en consultas sobre "
            "«agenda escolar» y «agenda de papel»."
        ),
        limite=(
            "La búsqueda pagada captura demanda existente pero no la crea. En categorías nuevas puede no "
            "haber volumen suficiente y el canal correcto es otro."
        ),
        libros=["geddes", "kaushik", "chaffey", "eisenberg"],
        error=("Operar sin lista de exclusiones",
               "Revisa el informe de términos de búsqueda semanalmente y excluye lo irrelevante."),
    ),
    dict(
        n="06",
        slug="email-marketing",
        titulo="Email marketing",
        tesis=(
            "El correo es el canal con mejor economía cuando la lista es propia y consentida: costo marginal "
            "casi nulo, control total del mensaje y datos de comportamiento directos. Su fragilidad es la "
            "reputación: enviar a quien no consintió, o con frecuencia excesiva, degrada la entregabilidad de "
            "todos los correos de la empresa, incluidos los transaccionales."
        ),
        conceptos=[
            ("entregabilidad", "probabilidad de que el correo llegue a la bandeja principal del destinatario"),
            ("segmentación de envío", "división de la lista según comportamiento o perfil para enviar contenido pertinente"),
            ("frecuencia sostenible", "ritmo de envío que mantiene el interés sin producir bajas ni reclamos"),
            ("consentimiento verificable", "registro que acredita cuándo y cómo la persona aceptó recibir comunicaciones"),
        ],
        metodo=[
            "verificar consentimiento y base de licitud de la lista",
            "segmentar por comportamiento y perfil",
            "definir la frecuencia con datos de baja y reclamo",
            "medir entregabilidad y limpiar la lista con regularidad",
            "evaluar el canal por ingreso y no por aperturas",
        ],
        senales=[
            ("tasa de entrega en bandeja principal", "correos entregados en bandeja principal, sobre correos enviados"),
            ("tasa de baja por envío", "bajas solicitadas, sobre correos entregados"),
            ("ingreso atribuible por envío", "ingreso vinculado al envío, dividido por costo del envío"),
        ],
        caso=(
            "Ruta Andina envía cuatro correos semanales a toda su base. La tasa de baja mensual llegó a 6 % y "
            "los avisos de facturación empezaron a caer en correo no deseado."
        ),
        limite=(
            "Las tasas de apertura se volvieron poco confiables por la protección de privacidad de los "
            "clientes de correo. Las decisiones deben apoyarse en clics, conversiones e ingreso."
        ),
        libros=["handley", "chaffey", "kaushik", "godin"],
        error=("Enviar a toda la base sin segmentar",
               "Segmenta por comportamiento y perfil, y mide bajas y reclamos por segmento antes de aumentar la frecuencia."),
    ),
    dict(
        n="07",
        slug="social-media",
        titulo="Social media",
        tesis=(
            "Las redes sociales cumplen funciones distintas según la etapa: descubrimiento, construcción de "
            "credibilidad, atención al cliente y, en menor medida, conversión directa. Tratarlas como canal "
            "de venta directa produce contenido publicitario que la audiencia ignora. El alcance orgánico es "
            "una audiencia alquilada: puede desaparecer con un cambio de algoritmo."
        ),
        conceptos=[
            ("función del canal por etapa", "papel específico que cumple la red en el recorrido del cliente"),
            ("alcance orgánico", "personas alcanzadas sin pago, sujeto a las reglas cambiantes de la plataforma"),
            ("comunidad", "grupo de personas con interés común que interactúa entre sí y no sólo con la marca"),
            ("atención pública", "gestión de consultas y reclamos visibles para terceros"),
        ],
        metodo=[
            "definir la función de cada red en el recorrido",
            "producir contenido acorde a esa función",
            "establecer el protocolo de atención pública",
            "medir con indicadores propios de cada función",
            "evaluar la dependencia del alcance orgánico",
        ],
        senales=[
            ("alcance y participación por función", "alcance e interacciones, segmentados por tipo de contenido y función"),
            ("tiempo de respuesta en atención pública", "minutos entre la consulta pública y la primera respuesta"),
            ("oportunidades originadas por red", "oportunidades calificadas atribuidas al canal, sobre oportunidades totales"),
        ],
        caso=(
            "Ruta Andina publica ofertas tres veces por semana en redes y responde reclamos públicos en 48 "
            "horas. Los reclamos sin responder aparecen antes que su contenido."
        ),
        limite=(
            "La actividad en redes rara vez produce conversión directa en B2B con ciclos largos. Exigirle "
            "ventas atribuibles lleva a abandonar su función real de credibilidad."
        ),
        libros=["godin", "vaynerchuk", "chaffey", "handley"],
        error=("Usar redes exclusivamente para publicar ofertas",
               "Asigna una función por red y mide con indicadores propios de esa función."),
    ),
    dict(
        n="08",
        slug="community-marketing",
        titulo="Community marketing",
        tesis=(
            "Construir comunidad significa facilitar que las personas se conecten entre sí alrededor de un "
            "interés común, no acumular seguidores. Su valor comercial es indirecto y potente: reduce el "
            "costo de adquisición por confianza, mejora la retención y produce información cualitativa "
            "continua. Su costo es la moderación y la constancia, que la mayoría subestima."
        ),
        conceptos=[
            ("interés común", "tema que justifica la existencia de la comunidad más allá de la marca"),
            ("participación entre miembros", "interacciones que ocurren sin intervención de la empresa"),
            ("moderación", "trabajo de sostener normas, calidad y seguridad del espacio"),
            ("valor extraído frente a valor aportado", "relación entre lo que la empresa obtiene y lo que entrega a la comunidad"),
        ],
        metodo=[
            "definir el interés común y las normas del espacio",
            "facilitar la conversación entre miembros",
            "sostener la moderación con responsables definidos",
            "medir participación entre miembros y no sólo con la marca",
            "evaluar el efecto en retención y adquisición",
        ],
        senales=[
            ("participación entre miembros", "interacciones entre miembros, sobre interacciones totales del espacio"),
            ("miembros activos recurrentes", "miembros con actividad en dos periodos consecutivos, sobre miembros totales"),
            ("efecto en retención", "retención de clientes participantes frente a no participantes, a 12 meses"),
        ],
        caso=(
            "Ruta Andina abrió un grupo de dueños de taller. El 90 % de los mensajes son de la propia empresa "
            "y la participación cae mes a mes."
        ),
        limite=(
            "Una comunidad exige moderación sostenida y puede convertirse en canal de reclamos públicos. Sin "
            "capacidad de sostenerla, es preferible no abrirla."
        ),
        libros=["godin", "pulizzi", "reichheld", "handley"],
        error=("Usar la comunidad como canal de difusión propia",
               "Mide la participación entre miembros y limita la presencia de la marca a facilitar la conversación."),
    ),
    dict(
        n="09",
        slug="conversion-web",
        titulo="Conversión web",
        tesis=(
            "La optimización de conversión seria empieza con investigación, no con tests: analítica para "
            "saber dónde se pierde, grabaciones y encuestas para saber por qué, y sólo entonces hipótesis y "
            "experimentos. Laja insiste en que la mayoría de los tests fracasan por falta de investigación "
            "previa y por muestras insuficientes que producen conclusiones falsas."
        ),
        conceptos=[
            ("investigación previa", "análisis cuantitativo y cualitativo que precede a la formulación de hipótesis"),
            ("hipótesis de conversión", "afirmación sobre qué cambio producirá qué efecto y por qué"),
            ("potencia estadística", "capacidad del test de detectar el efecto mínimo relevante con la muestra disponible"),
            ("falso positivo", "conclusión de mejora que no se sostiene al repetir la medición"),
        ],
        metodo=[
            "identificar la mayor pérdida con analítica",
            "investigar la causa con evidencia cualitativa",
            "formular la hipótesis con mecanismo explícito",
            "calcular muestra y duración antes de iniciar",
            "validar el resultado antes de implementarlo de forma permanente",
        ],
        senales=[
            ("tasa de conversión por paso", "avances, sobre entradas al paso, en el recorrido de conversión"),
            ("potencia del test", "probabilidad de detectar el efecto mínimo relevante con el tráfico disponible, calculada antes de iniciar"),
            ("tasa de replicación", "resultados que se sostienen al repetir la medición, sobre resultados positivos"),
        ],
        caso=(
            "Ruta Andina cambió el color del botón y declaró 18 % de mejora con 120 visitantes por variante "
            "durante cuatro días. Al mes siguiente la conversión volvió al nivel anterior."
        ),
        limite=(
            "En sitios con poco tráfico los tests A/B rara vez alcanzan potencia suficiente. La alternativa "
            "correcta es investigación cualitativa y cambios fundamentados, no tests sin potencia."
        ),
        libros=["laja", "kohavi", "eisenberg", "krug"],
        error=("Testear sin calcular muestra ni duración",
               "Calcula el tamaño necesario antes de iniciar; si el tráfico no alcanza, decide con investigación cualitativa."),
    ),
    dict(
        n="10",
        slug="analitica-digital",
        titulo="Analítica digital",
        tesis=(
            "La analítica digital sirve para tomar decisiones, no para llenar tableros. Kaushik distingue "
            "entre métricas que informan acción y métricas de vanidad que sólo producen sensación de "
            "control. La condición previa es un plan de medición: qué decisiones se tomarán, qué preguntas "
            "las informan, qué eventos hay que registrar y con qué definición. Sin ese plan, se instrumenta "
            "todo y no se usa nada."
        ),
        conceptos=[
            ("plan de medición", "documento que vincula decisiones, preguntas, métricas y eventos a registrar"),
            ("métrica de vanidad", "indicador que sube sin relación con el resultado de negocio"),
            ("segmentación analítica", "análisis por grupos que revela diferencias ocultas en el promedio"),
            ("calidad del dato", "grado en que la instrumentación registra correctamente lo que ocurre"),
        ],
        metodo=[
            "definir las decisiones que la analítica debe informar",
            "traducirlas a preguntas y métricas con definición operacional",
            "instrumentar sólo lo necesario y verificar la calidad",
            "analizar por segmento y no sólo el agregado",
            "revisar el plan cada semestre y eliminar lo que no se usa",
        ],
        senales=[
            ("decisiones informadas por analítica", "decisiones documentadas que citan un análisis, por trimestre"),
            ("calidad de la instrumentación", "eventos que registran correctamente, sobre eventos auditados"),
            ("métricas activas sin uso", "métricas en tableros sin uso documentado, sobre métricas totales"),
        ],
        caso=(
            "El tablero de Ruta Andina tiene 34 métricas. En la reunión mensual se revisan tres y ninguna "
            "cambia una decisión."
        ),
        limite=(
            "Las restricciones de privacidad y el bloqueo de rastreadores reducen la cobertura de la analítica "
            "digital. Los datos deben leerse como muestra sesgada y no como censo."
        ),
        libros=["kaushik", "provost", "croll-yoskovitz", "wheeler-dv"],
        error=("Instrumentar todo sin plan de medición",
               "Parte de las decisiones y elimina del tablero toda métrica que no informe una de ellas."),
    ),
    dict(
        n="11",
        slug="atribucion-basica",
        titulo="Atribución básica",
        tesis=(
            "La atribución intenta repartir el crédito de una conversión entre los puntos de contacto que la "
            "precedieron. Todos los modelos —último clic, primer clic, lineal, decaimiento— son "
            "convenciones, no verdades. El último clic sobrevalora los canales de captura de intención y "
            "subvalora los que crean demanda. La conclusión práctica es usar la atribución para ordenar la "
            "conversación y la incrementalidad para decidir presupuesto."
        ),
        conceptos=[
            ("modelo de atribución", "regla convencional que reparte el crédito de la conversión entre puntos de contacto"),
            ("sesgo del último clic", "sobrevaloración del canal más cercano a la conversión"),
            ("ventana de atribución", "periodo dentro del cual un contacto se considera contribuyente"),
            ("incrementalidad", "efecto causal real de un canal, estimado con grupo de comparación"),
        ],
        metodo=[
            "documentar el modelo y la ventana utilizados",
            "comparar resultados bajo dos modelos distintos",
            "identificar los canales cuyo valor cambia según el modelo",
            "diseñar una prueba de incrementalidad para los casos críticos",
            "decidir presupuesto con evidencia causal donde el monto lo justifique",
        ],
        senales=[
            ("diferencia de crédito entre modelos", "variación del crédito asignado a cada canal según el modelo aplicado"),
            ("cobertura de la atribución", "conversiones con recorrido registrado, sobre conversiones totales"),
            ("resultado de pruebas de incrementalidad", "efecto causal estimado por canal, con intervalo de confianza"),
        ],
        caso=(
            "Bajo último clic, la búsqueda de marca recibe el 61 % del crédito en Ruta Andina. Bajo primer "
            "clic, el contenido orgánico recibe el 44 %. El presupuesto se asigna con el primero."
        ),
        limite=(
            "Ningún modelo de atribución establece causalidad. Con presupuestos pequeños, el costo de una "
            "prueba de incrementalidad puede superar su beneficio."
        ),
        libros=["kaushik", "kohavi", "provost", "binet-field"],
        error=("Asignar presupuesto sólo por último clic",
               "Compara al menos dos modelos y valida los canales críticos con una prueba de incrementalidad."),
    ),
    dict(
        n="12",
        slug="omnicanalidad",
        titulo="Omnicanalidad",
        tesis=(
            "La omnicanalidad no consiste en estar en todas partes sino en que la experiencia sea continua: "
            "el cliente retoma donde quedó, sin repetir información y sin contradicciones. Su obstáculo real "
            "es organizacional: canales con dueños distintos, sistemas separados y métricas que compiten. "
            "Resolverlo exige una identidad única de cliente y acuerdos de servicio entre áreas."
        ),
        conceptos=[
            ("identidad única de cliente", "registro que consolida las interacciones de una persona en todos los canales"),
            ("continuidad", "capacidad del cliente de retomar el proceso sin repetir información"),
            ("silo de canal", "gestión aislada que impide compartir contexto entre canales"),
            ("consistencia de condiciones", "coincidencia de precio, plazos y políticas entre canales"),
        ],
        metodo=[
            "mapear los canales y los sistemas que los sostienen",
            "definir la identidad única de cliente",
            "identificar los puntos donde se pierde el contexto",
            "acordar responsabilidades y niveles de servicio entre áreas",
            "medir continuidad desde la perspectiva del cliente",
        ],
        senales=[
            ("tasa de repetición de información", "interacciones donde el cliente repite datos ya entregados, sobre interacciones multicanal"),
            ("cobertura de identidad única", "clientes con identidad consolidada, sobre clientes activos"),
            ("incoherencias entre canales", "diferencias detectadas en auditoría, sobre elementos auditados"),
        ],
        caso=(
            "Un cliente de Ruta Andina escribe por chat, luego llama y luego envía correo. En cada canal "
            "explica su problema de nuevo porque los tres sistemas no se comunican."
        ),
        limite=(
            "La consolidación de datos de cliente entre canales es tratamiento de datos personales: exige "
            "finalidad declarada, base de licitud y medidas de seguridad."
        ),
        libros=["chaffey", "dixon-effort", "diorio", "flint"],
        error=("Sumar canales sin consolidar el contexto del cliente",
               "Define la identidad única y mide cuántas veces el cliente repite información."),
    ),
    dict(
        n="13",
        slug="plan-de-adquisicion",
        titulo="Plan de adquisición",
        tesis=(
            "Un plan de adquisición asigna presupuesto entre canales con supuestos explícitos de costo por "
            "oportunidad, tasa de conversión y capacidad de atención. Su calidad se mide por su falsabilidad: "
            "debe indicar qué resultado obligaría a reasignar. El error frecuente es planificar volumen sin "
            "verificar que el equipo comercial puede atender lo que se generará."
        ),
        conceptos=[
            ("supuesto de canal", "estimación declarada de costo y conversión que sostiene la asignación"),
            ("capacidad de atención", "volumen de oportunidades que el equipo comercial puede trabajar con calidad"),
            ("regla de reasignación", "criterio que determina cuándo mover presupuesto entre canales"),
            ("horizonte de maduración", "tiempo que necesita un canal antes de poder evaluarse"),
        ],
        metodo=[
            "estimar costo por oportunidad y conversión por canal",
            "verificar la capacidad de atención del equipo",
            "asignar presupuesto con supuestos explícitos",
            "definir la regla de reasignación y su periodicidad",
            "revisar mensualmente contra los supuestos declarados",
        ],
        senales=[
            ("desviación frente a supuestos", "diferencia entre costo por oportunidad real y estimado, por canal"),
            ("utilización de la capacidad comercial", "oportunidades trabajadas, sobre capacidad definida del equipo"),
            ("reasignaciones ejecutadas", "movimientos de presupuesto realizados según la regla, por trimestre"),
        ],
        caso=(
            "El plan de Ruta Andina proyecta 400 oportunidades mensuales. El equipo de tres personas puede "
            "trabajar con calidad alrededor de 120."
        ),
        limite=(
            "Reasignar presupuesto demasiado rápido impide que los canales lentos maduren. La regla debe "
            "distinguir canales de respuesta inmediata de canales de construcción."
        ),
        libros=["chaffey", "weinberg-traction", "croll-yoskovitz", "binet-field"],
        error=("Planificar volumen sin verificar capacidad de atención",
               "Ajusta la meta de generación a la capacidad real del equipo comercial."),
    ),
    dict(
        n="14",
        slug="auditoria-de-marketing-digital",
        titulo="Auditoría de marketing digital",
        tesis=(
            "Esta clase integra la parte en una auditoría completa: activos, canales, medición, conversión, "
            "cumplimiento de privacidad y economía por canal. Su producto no es una lista de hallazgos sino "
            "una priorización: qué corregir primero según efecto sobre el negocio y costo de corrección. Una "
            "auditoría sin priorización produce parálisis."
        ),
        conceptos=[
            ("inventario de activos digitales", "registro de sitios, listas, cuentas y contenidos con su estado y responsable"),
            ("hallazgo priorizado", "problema detectado con estimación de efecto y de costo de corrección"),
            ("cumplimiento de privacidad", "conformidad de cookies, consentimiento y tratamiento con la normativa vigente"),
            ("economía por canal", "costo por oportunidad y margen atribuible de cada canal"),
        ],
        metodo=[
            "inventariar activos, accesos y responsables",
            "auditar medición, conversión y economía por canal",
            "revisar cumplimiento de privacidad y consentimiento",
            "priorizar hallazgos por efecto y costo",
            "entregar plan de corrección con responsables y fechas",
        ],
        senales=[
            ("hallazgos priorizados con estimación", "hallazgos con efecto y costo estimados, sobre hallazgos totales"),
            ("activos sin responsable", "activos digitales sin responsable asignado, sobre activos inventariados"),
            ("brechas de cumplimiento", "incumplimientos detectados en privacidad y consentimiento, por categoría"),
        ],
        caso=(
            "Ruta Andina debe presentar un diagnóstico digital antes del presupuesto anual. Existen cinco "
            "cuentas publicitarias, tres de ellas sin responsable identificado."
        ),
        limite=(
            "Una auditoría refleja un momento. Sin responsables y fechas, los hallazgos se repiten idénticos "
            "en la auditoría siguiente."
        ),
        libros=["chaffey", "kaushik", "laja", "enge-seo"],
        error=("Entregar hallazgos sin priorización ni responsables",
               "Ordena por efecto sobre el negocio y costo de corrección, y asigna responsable y fecha a cada uno."),
    ),
]
