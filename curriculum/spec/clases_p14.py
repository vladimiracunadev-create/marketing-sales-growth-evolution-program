# -*- coding: utf-8 -*-
"""Parte 14 — Publicidad y performance marketing."""

CLASES = [
    dict(
        n="01",
        slug="paid-media-y-subastas",
        titulo="Medios pagados y subastas",
        tesis=(
            "La publicidad digital se asigna mediante subastas donde no gana quien más paga sino quien "
            "combina oferta, relevancia y probabilidad de acción. Entender esa mecánica cambia la gestión: "
            "mejorar la relevancia reduce el costo tanto o más que aumentar la oferta. La segunda "
            "consecuencia es que el costo por resultado no es una constante del canal sino una función del "
            "propio desempeño."
        ),
        conceptos=[
            ("subasta publicitaria", "mecanismo que asigna impresiones combinando oferta y calidad estimada"),
            ("relevancia estimada", "evaluación de la plataforma sobre la correspondencia entre anuncio y audiencia"),
            ("costo por resultado", "gasto dividido por la unidad de resultado que se compra"),
            ("competencia por audiencia", "presión de precio provocada por otros anunciantes que buscan al mismo público"),
        ],
        metodo=[
            "definir la unidad de resultado que se compra",
            "medir el costo por resultado actual como línea base",
            "mejorar relevancia antes de aumentar la oferta",
            "monitorear la competencia por la audiencia",
            "fijar el costo máximo admisible según la economía unitaria",
        ],
        senales=[
            ("costo por resultado", "gasto del periodo dividido por unidades de resultado obtenidas"),
            ("indicador de relevancia", "evaluación de relevancia reportada por la plataforma, por grupo de anuncios"),
            ("tasa de impresiones perdidas", "impresiones no obtenidas por presupuesto o por posición, sobre impresiones elegibles"),
        ],
        caso=(
            "Ruta Andina sube su oferta un 30 % para ganar volumen. El costo por oportunidad sube 41 % y el "
            "volumen apenas 9 %: el problema era la relevancia del anuncio."
        ),
        limite=(
            "Las plataformas cambian sus mecánicas y su información. Construir un modelo detallado sobre "
            "supuestos de la subasta actual tiene fecha de vencimiento."
        ),
        libros=["geddes", "kaushik", "chaffey", "ogilvy"],
        error=("Subir la oferta antes de revisar la relevancia",
               "Mejora correspondencia entre término, anuncio y página antes de aumentar el costo por clic."),
    ),
    dict(
        n="02",
        slug="objetivos-de-campana",
        titulo="Objetivos de campaña",
        tesis=(
            "El objetivo declarado en la plataforma determina cómo se optimiza la entrega. Elegir "
            "«interacciones» cuando se busca oportunidades produce exactamente lo pedido: mucha interacción y "
            "pocos negocios. El objetivo debe derivarse del resultado de negocio y de la etapa del cliente, y "
            "debe coincidir con la métrica que efectivamente se evaluará."
        ),
        conceptos=[
            ("objetivo de optimización", "señal que la plataforma usa para decidir a quién mostrar el anuncio"),
            ("coherencia objetivo-métrica", "correspondencia entre lo que se optimiza y lo que se evalúa"),
            ("etapa del cliente", "momento del recorrido al que la campaña se dirige"),
            ("señal de conversión", "evento registrado que la plataforma usa para aprender"),
        ],
        metodo=[
            "definir el resultado de negocio esperado",
            "elegir el objetivo de optimización coherente",
            "verificar que la señal de conversión esté bien instrumentada",
            "asegurar volumen suficiente de señal para el aprendizaje",
            "evaluar con la misma métrica que se optimizó",
        ],
        senales=[
            ("coherencia entre objetivo y evaluación", "campañas cuya métrica de evaluación coincide con su objetivo, sobre campañas activas"),
            ("volumen de señal de conversión", "conversiones registradas por semana, comparadas con el mínimo de aprendizaje"),
            ("costo por resultado de negocio", "gasto dividido por oportunidades calificadas, por campaña"),
        ],
        caso=(
            "Las campañas de Ruta Andina se optimizan por clics y se evalúan por oportunidades. La plataforma "
            "entrega el tráfico más barato, que es también el menos calificado."
        ),
        limite=(
            "Optimizar por una conversión escasa impide el aprendizaje del sistema. En volúmenes bajos puede "
            "ser necesario optimizar por un evento intermedio bien correlacionado."
        ),
        libros=["geddes", "kaushik", "chaffey", "provost"],
        error=("Optimizar por una métrica y evaluar por otra",
               "Alinea objetivo de plataforma, señal instrumentada y métrica de evaluación."),
    ),
    dict(
        n="03",
        slug="audiencias",
        titulo="Audiencias",
        tesis=(
            "Definir audiencias es decidir a quién se le paga por mostrar el anuncio. Las opciones van desde "
            "segmentación explícita hasta audiencias similares construidas por la plataforma. El criterio "
            "económico es simple: una audiencia más estrecha suele costar más por impresión y menos por "
            "resultado. El criterio legal no lo es tanto: el uso de datos de clientes para construir "
            "audiencias exige base de licitud e información al titular."
        ),
        conceptos=[
            ("audiencia definida", "conjunto de personas seleccionado por criterios explícitos"),
            ("audiencia similar", "grupo construido por la plataforma a partir de una base de referencia"),
            ("superposición de audiencias", "presencia de las mismas personas en varias campañas, que eleva el costo"),
            ("licitud de la base cargada", "fundamento jurídico que permite usar datos propios para publicidad"),
        ],
        metodo=[
            "definir el perfil objetivo antes de configurar",
            "verificar la base de licitud de cualquier dato propio cargado",
            "controlar la superposición entre campañas",
            "comparar costo por resultado entre tipos de audiencia",
            "documentar la configuración y revisarla periódicamente",
        ],
        senales=[
            ("costo por resultado por audiencia", "gasto dividido por resultados, comparado entre tipos de audiencia"),
            ("superposición entre campañas", "personas alcanzadas por más de una campaña, sobre alcance total"),
            ("audiencias con base de licitud documentada", "audiencias con fundamento registrado, sobre audiencias activas"),
        ],
        caso=(
            "Ruta Andina cargó su base de clientes para construir audiencias similares sin verificar si esos "
            "clientes fueron informados de esa finalidad."
        ),
        limite=(
            "Las restricciones de privacidad reducen la precisión de las audiencias y la disponibilidad de "
            "identificadores. Las estrategias que dependían de rastreo entre sitios pierden efectividad."
        ),
        libros=["geddes", "kaushik", "chaffey", "oneil"],
        error=("Cargar bases de clientes sin base de licitud",
               "Verifica finalidad informada y base legal antes de usar datos propios en plataformas publicitarias."),
    ),
    dict(
        n="04",
        slug="creatividades",
        titulo="Creatividades",
        tesis=(
            "La creatividad es, en promedio, la variable con mayor efecto sobre el resultado publicitario, "
            "por encima de la segmentación fina. Ogilvy insistía en que la investigación debe preceder a la "
            "ejecución: saber qué le importa al destinatario antes de decidir cómo decirlo. En entornos "
            "digitales se agrega una exigencia operativa: producir variantes suficientes para que el sistema "
            "aprenda y para evitar la fatiga."
        ),
        conceptos=[
            ("concepto creativo", "idea central que organiza el mensaje y lo hace reconocible"),
            ("variante", "versión que cambia un elemento específico para comparar desempeño"),
            ("fatiga creativa", "caída de desempeño por exposición repetida de la misma pieza"),
            ("activo distintivo en anuncio", "elemento de marca que permite atribuir el anuncio sin leer el nombre"),
        ],
        metodo=[
            "investigar qué importa al destinatario antes de producir",
            "definir el concepto y sus variantes",
            "incluir activos distintivos de marca",
            "monitorear la fatiga por frecuencia de exposición",
            "renovar creatividades antes de la caída de desempeño",
        ],
        senales=[
            ("desempeño por variante", "costo por resultado y tasa de clic, por variante creativa"),
            ("frecuencia de exposición", "impresiones promedio por persona alcanzada, semanal"),
            ("atribución de marca", "personas que identifican correctamente la marca del anuncio, en prueba con muestra"),
        ],
        caso=(
            "Ruta Andina usa la misma pieza desde hace cinco meses. La frecuencia semanal llegó a 11 y el "
            "costo por oportunidad se duplicó."
        ),
        limite=(
            "Producir muchas variantes tiene un costo. En presupuestos pequeños conviene menos variantes con "
            "más diferencia entre ellas que muchas con diferencias marginales."
        ),
        libros=["ogilvy", "sharp2", "binet-field", "geddes"],
        error=("Sostener la misma creatividad hasta que el resultado se desploma",
               "Define un umbral de frecuencia y renueva antes de alcanzar la caída de desempeño."),
    ),
    dict(
        n="05",
        slug="google-ads-arquitectura-conceptual",
        titulo="Google Ads: arquitectura conceptual",
        tesis=(
            "La estructura de una cuenta de búsqueda determina el control del presupuesto y la relevancia. "
            "Organizar por intención —y no por catálogo de productos— permite escribir anuncios pertinentes y "
            "asignar presupuesto donde hay retorno. Las decisiones estructurales importantes son pocas: "
            "separación por intención, tipos de coincidencia, exclusiones y correspondencia entre anuncio y "
            "página."
        ),
        conceptos=[
            ("estructura por intención", "organización de campañas según lo que busca el usuario y no según el producto"),
            ("tipo de coincidencia", "regla que define qué tan cerca debe estar la búsqueda del término configurado"),
            ("correspondencia anuncio-página", "coherencia entre lo que promete el anuncio y lo que muestra el destino"),
            ("control presupuestario", "capacidad de asignar y limitar gasto por intención"),
        ],
        metodo=[
            "clasificar términos por intención",
            "estructurar campañas y grupos según esa clasificación",
            "definir tipos de coincidencia y exclusiones",
            "vincular cada grupo a una página coherente",
            "revisar el informe de términos semanalmente",
        ],
        senales=[
            ("costo por oportunidad por intención", "gasto dividido por oportunidades calificadas, por grupo de intención"),
            ("proporción de gasto en términos no deseados", "gasto en búsquedas irrelevantes, sobre gasto total del periodo"),
            ("correspondencia auditada", "grupos con página coherente, sobre grupos activos"),
        ],
        caso=(
            "La cuenta de Ruta Andina tiene una sola campaña con 400 términos y un único anuncio. No es "
            "posible saber qué intención produce negocios ni limitar el gasto donde no los produce."
        ),
        limite=(
            "Las plataformas avanzan hacia automatización que reduce el control estructural. La arquitectura "
            "sigue importando, pero su forma cambia y debe revisarse."
        ),
        libros=["geddes", "kaushik", "chaffey", "enge-seo"],
        error=("Estructurar la cuenta por catálogo de productos",
               "Reorganiza por intención de búsqueda y vincula cada grupo a una página coherente."),
    ),
    dict(
        n="06",
        slug="meta-ads-arquitectura-conceptual",
        titulo="Meta Ads: arquitectura conceptual",
        tesis=(
            "En plataformas sociales la demanda no está declarada: se interrumpe a personas que no buscaban "
            "nada. Eso cambia la lógica: la creatividad y la propuesta hacen el trabajo que en búsqueda hacía "
            "la intención. La estructura tiende a ser más simple y el aprendizaje del sistema requiere "
            "volumen de señal; fragmentar demasiado impide que la optimización funcione."
        ),
        conceptos=[
            ("demanda no declarada", "situación en que la audiencia no está buscando activamente la solución"),
            ("fase de aprendizaje", "periodo en que el sistema necesita señal suficiente para optimizar"),
            ("fragmentación excesiva", "división del presupuesto en demasiados conjuntos que impide el aprendizaje"),
            ("gancho inicial", "primer segundo o primera línea que determina si la persona detiene el desplazamiento"),
        ],
        metodo=[
            "definir la propuesta que justifica interrumpir",
            "consolidar conjuntos para alcanzar volumen de señal",
            "priorizar el gancho inicial en la creatividad",
            "esperar a superar la fase de aprendizaje antes de juzgar",
            "evaluar por costo por resultado de negocio",
        ],
        senales=[
            ("conversiones semanales por conjunto", "conversiones registradas por conjunto, comparadas con el mínimo de aprendizaje"),
            ("tasa de retención de atención", "personas que superan los primeros segundos, sobre impresiones"),
            ("costo por oportunidad calificada", "gasto dividido por oportunidades calificadas originadas"),
        ],
        caso=(
            "Ruta Andina dividió CLP 900.000 mensuales en 14 conjuntos de anuncios. Ninguno acumula señal "
            "suficiente y el sistema no logra optimizar."
        ),
        limite=(
            "Los cambios de privacidad afectan la medición y la optimización en estas plataformas. Los "
            "resultados reportados pueden diferir de los registrados internamente."
        ),
        libros=["geddes", "sharp2", "kaushik", "binet-field"],
        error=("Fragmentar el presupuesto en demasiados conjuntos",
               "Consolida hasta alcanzar el volumen de señal que la optimización requiere."),
    ),
    dict(
        n="07",
        slug="linkedin-ads-arquitectura-conceptual",
        titulo="LinkedIn Ads: arquitectura conceptual",
        tesis=(
            "La publicidad profesional permite segmentar por cargo, industria y tamaño, lo que la hace "
            "atractiva para B2B y también cara por impresión. Su uso racional exige tickets que sostengan ese "
            "costo y una propuesta pertinente para el rol. Usarla para captar leads con un recurso genérico "
            "produce el costo por lead más alto del mercado sin mejor calidad."
        ),
        conceptos=[
            ("segmentación profesional", "selección por cargo, función, industria y tamaño de organización"),
            ("costo por impresión elevado", "precio característico del canal que exige tickets altos para ser rentable"),
            ("pertinencia por rol", "correspondencia entre el mensaje y las preocupaciones del cargo seleccionado"),
            ("umbral de viabilidad", "ticket mínimo que hace rentable el canal dada su estructura de costo"),
        ],
        metodo=[
            "verificar que el ticket sostiene el costo del canal",
            "segmentar por rol con criterios verificables",
            "construir el mensaje desde la preocupación del cargo",
            "medir hasta oportunidad calificada y no hasta lead",
            "comparar con canales alternativos antes de escalar",
        ],
        senales=[
            ("costo por oportunidad calificada", "gasto del canal dividido por oportunidades calificadas originadas"),
            ("precisión de la segmentación", "leads que corresponden al rol objetivo, sobre leads generados"),
            ("comparación con canales alternativos", "costo por oportunidad del canal frente al promedio de otros canales"),
        ],
        caso=(
            "Ruta Andina gastó CLP 1,2 millones en el canal para promocionar un ebook genérico. Obtuvo 22 "
            "leads a CLP 54.000 cada uno y ninguna oportunidad calificada."
        ),
        limite=(
            "Los datos de perfil profesional son declarados por los usuarios y pueden estar desactualizados. "
            "La segmentación no garantiza que la persona ocupe hoy ese cargo."
        ),
        libros=["geddes", "chaffey", "dixon-customer", "kaushik"],
        error=("Usar canales caros para captar leads genéricos",
               "Reserva el canal para propuestas pertinentes al rol y tickets que sostengan su costo."),
    ),
    dict(
        n="08",
        slug="presupuesto-y-pacing",
        titulo="Presupuesto y ritmo de gasto",
        tesis=(
            "Gestionar presupuesto publicitario es decidir cuánto, dónde y a qué ritmo. El ritmo importa: "
            "agotar el presupuesto en la primera semana deja el mes sin presencia, y distribuirlo de forma "
            "uniforme ignora la estacionalidad de la demanda. La regla es asignar según retorno marginal "
            "esperado y revisar con una frecuencia que permita aprender sin sobrerreaccionar al ruido."
        ),
        conceptos=[
            ("retorno marginal", "resultado adicional que produce el siguiente peso invertido en un canal"),
            ("ritmo de gasto", "distribución del presupuesto en el tiempo dentro del periodo"),
            ("estacionalidad", "variación previsible de la demanda según periodo del año o de la semana"),
            ("sobrerreacción al ruido", "cambio de asignación basado en variación aleatoria y no en señal real"),
        ],
        metodo=[
            "estimar el retorno marginal por canal",
            "definir el ritmo según estacionalidad observada",
            "fijar la frecuencia de revisión y el umbral de cambio",
            "documentar cada reasignación y su justificación",
            "evaluar el efecto de las reasignaciones a fin de periodo",
        ],
        senales=[
            ("desviación del ritmo planificado", "diferencia entre gasto real y planificado, por semana"),
            ("retorno marginal estimado", "resultado adicional por peso invertido, por canal y por tramo de inversión"),
            ("frecuencia de reasignación", "cambios de presupuesto realizados, por trimestre, y su efecto medido"),
        ],
        caso=(
            "Ruta Andina agota su presupuesto mensual en los primeros ocho días. Las últimas tres semanas "
            "queda sin presencia justo cuando los talleres planifican compras."
        ),
        limite=(
            "El retorno marginal es difícil de estimar con precisión y varía con el volumen. Las decisiones "
            "deben tomarse con rangos y no con puntos."
        ),
        libros=["kaushik", "binet-field", "wheeler-dv", "geddes"],
        error=("Reasignar presupuesto ante variaciones semanales",
               "Define un umbral de cambio y una frecuencia de revisión que distinga señal de ruido."),
    ),
    dict(
        n="09",
        slug="ctr-cpc-y-cpm",
        titulo="CTR, CPC y CPM",
        tesis=(
            "Las métricas intermedias describen la mecánica del canal: cuánto cuesta llegar, cuánto cuesta "
            "una visita y qué proporción reacciona. Son útiles para diagnosticar y peligrosas para decidir: "
            "un anuncio con excelente tasa de clic puede atraer al público equivocado. La regla es usar las "
            "métricas intermedias para explicar y las de negocio para decidir."
        ),
        conceptos=[
            ("costo por mil impresiones", "precio de alcanzar mil impresiones en la audiencia seleccionada"),
            ("tasa de clic", "clics obtenidos sobre impresiones entregadas"),
            ("costo por clic", "gasto dividido por clics obtenidos"),
            ("métrica de diagnóstico", "indicador que explica el desempeño pero no debe gobernar la decisión"),
        ],
        metodo=[
            "establecer líneas base de las métricas intermedias",
            "usarlas para diagnosticar dónde está el problema",
            "verificar la calidad del tráfico que producen",
            "decidir con métricas de negocio",
            "documentar la relación entre ambas para el canal",
        ],
        senales=[
            ("tasa de clic por variante", "clics sobre impresiones, por variante creativa y audiencia"),
            ("costo por clic por audiencia", "gasto dividido por clics, comparado entre audiencias"),
            ("conversión posterior al clic", "oportunidades calificadas, sobre clics obtenidos, por campaña"),
        ],
        caso=(
            "Una campaña de Ruta Andina tiene 6,2 % de tasa de clic —el triple del promedio— y cero "
            "oportunidades. El anuncio prometía una funcionalidad gratuita que no existe."
        ),
        limite=(
            "Las métricas intermedias no son comparables entre plataformas ni entre formatos. Compararlas "
            "directamente induce conclusiones falsas."
        ),
        libros=["kaushik", "geddes", "croll-yoskovitz", "chaffey"],
        error=("Optimizar por tasa de clic",
               "Usa las métricas intermedias para diagnosticar y decide con costo por oportunidad calificada."),
    ),
    dict(
        n="10",
        slug="cpa-cac-y-roas",
        titulo="CPA, CAC y ROAS",
        tesis=(
            "El costo por adquisición mide el gasto por conversión de campaña; el costo de adquisición de "
            "cliente incluye todo el gasto comercial, incluidos sueldos; el retorno sobre inversión "
            "publicitaria compara ingreso atribuido con gasto de medios. Los tres se confunden con "
            "frecuencia y esa confusión produce decisiones caras: un retorno publicitario alto puede "
            "coexistir con una economía unitaria negativa."
        ),
        conceptos=[
            ("costo por adquisición", "gasto de medios dividido por conversiones registradas de la campaña"),
            ("costo de adquisición de cliente", "gasto total de marketing y ventas, incluidos sueldos, por cliente nuevo"),
            ("retorno sobre inversión publicitaria", "ingreso atribuido dividido por gasto de medios"),
            ("ingreso incremental", "ingreso que no habría ocurrido sin la inversión publicitaria"),
        ],
        metodo=[
            "definir el alcance de cada métrica por escrito",
            "verificar qué ingreso es incremental y cuál no",
            "calcular el costo de adquisición completo por canal",
            "contrastar con margen y periodo de recuperación",
            "decidir escalamiento sólo con economía verificada",
        ],
        senales=[
            ("costo de adquisición completo por canal", "gasto total atribuible dividido por clientes nuevos del canal"),
            ("proporción de ingreso incremental", "ingreso incremental estimado, sobre ingreso atribuido"),
            ("relación valor de vida a costo de adquisición", "valor de vida dividido por costo de adquisición, por canal"),
        ],
        caso=(
            "El retorno publicitario reportado por Ruta Andina es 6,1 e incluye compras de clientes que ya "
            "eran clientes y que habrían comprado igual."
        ),
        limite=(
            "El ingreso atribuido depende del modelo de atribución y de la ventana. Comparar retornos entre "
            "periodos con configuraciones distintas no tiene sentido."
        ),
        libros=["croll-yoskovitz", "kaushik", "kohavi", "provost"],
        error=("Reportar retorno publicitario incluyendo ingreso no incremental",
               "Separa clientes nuevos de recurrentes y estima incrementalidad antes de reportar retorno."),
    ),
    dict(
        n="11",
        slug="tracking-y-atribucion",
        titulo="Tracking y atribución",
        tesis=(
            "Medir publicidad exige instrumentación: parámetros de campaña consistentes, eventos de "
            "conversión bien definidos y una convención de nomenclatura que permita analizar. Sin eso, cada "
            "informe requiere reconstruir manualmente qué significa cada fila. Las restricciones de "
            "privacidad reducen la cobertura del rastreo, lo que obliga a combinar medición de plataforma "
            "con datos propios del CRM."
        ),
        conceptos=[
            ("convención de nomenclatura", "regla uniforme para etiquetar campañas, fuentes y medios"),
            ("evento de conversión", "acción registrada que representa un resultado relevante"),
            ("cobertura de medición", "proporción de las conversiones reales que el sistema logra registrar"),
            ("reconciliación con CRM", "contraste entre lo reportado por plataformas y lo registrado internamente"),
        ],
        metodo=[
            "definir la convención de nomenclatura y aplicarla",
            "instrumentar eventos con definición documentada",
            "estimar la cobertura real de la medición",
            "reconciliar con el CRM cada mes",
            "declarar el margen de error en los informes",
        ],
        senales=[
            ("consistencia de etiquetado", "sesiones con parámetros correctos, sobre sesiones de campañas"),
            ("diferencia plataforma-CRM", "diferencia porcentual entre conversiones reportadas y registradas internamente"),
            ("cobertura de medición estimada", "conversiones registradas, sobre conversiones reales estimadas"),
        ],
        caso=(
            "Las plataformas reportan 96 conversiones mensuales a Ruta Andina y el CRM registra 41 "
            "oportunidades. Nadie ha reconciliado ambas cifras."
        ),
        limite=(
            "Ninguna instrumentación recupera la cobertura completa bajo las restricciones actuales de "
            "privacidad. La medición debe leerse como estimación con error conocido."
        ),
        libros=["kaushik", "provost", "kohavi", "chaffey"],
        error=("Reportar cifras de plataforma sin reconciliar con el CRM",
               "Concilia mensualmente y publica la diferencia junto con el informe."),
    ),
    dict(
        n="12",
        slug="optimizacion-de-campanas",
        titulo="Optimización de campañas",
        tesis=(
            "Optimizar es un ciclo: medir, formular hipótesis, cambiar una cosa, esperar el tiempo suficiente "
            "y evaluar. Los dos errores frecuentes son opuestos y ambos caros: cambiar todo cada dos días, "
            "impidiendo cualquier aprendizaje, o no tocar nada durante meses. Wheeler ofrece el criterio: "
            "distinguir variación común de variación especial antes de reaccionar."
        ),
        conceptos=[
            ("variación común", "fluctuación normal del proceso que no requiere intervención"),
            ("variación especial", "cambio atribuible a una causa identificable que sí justifica actuar"),
            ("ciclo de optimización", "secuencia de medición, hipótesis, cambio y evaluación"),
            ("ventana de evaluación", "periodo necesario para juzgar el efecto de un cambio"),
        ],
        metodo=[
            "establecer líneas base y rangos de variación normal",
            "identificar si el cambio observado es común o especial",
            "formular una hipótesis y cambiar una variable",
            "esperar la ventana de evaluación completa",
            "documentar el resultado y el aprendizaje",
        ],
        senales=[
            ("rango de variación normal", "límites estadísticos de la métrica en ausencia de cambios"),
            ("cambios por periodo", "modificaciones realizadas, por campaña y por mes"),
            ("proporción de cambios con hipótesis", "cambios con hipótesis documentada, sobre cambios realizados"),
        ],
        caso=(
            "El responsable de campañas de Ruta Andina modifica ofertas y creatividades tres veces por "
            "semana. Ninguna variación puede atribuirse a una causa."
        ),
        limite=(
            "Los sistemas automatizados de las plataformas reoptimizan constantemente. Intervenir demasiado "
            "reinicia su aprendizaje y empeora el resultado."
        ),
        libros=["wheeler-dv", "kohavi", "geddes", "kaushik"],
        error=("Intervenir ante cada variación diaria",
               "Calcula el rango de variación normal y actúa sólo ante señales fuera de ese rango."),
    ),
    dict(
        n="13",
        slug="fraude-brand-safety-y-privacidad",
        titulo="Fraude, brand safety y privacidad",
        tesis=(
            "La publicidad digital tiene tres riesgos que no aparecen en el tablero: tráfico no humano que "
            "consume presupuesto, aparición junto a contenido que daña la marca y tratamiento de datos "
            "personales sin base suficiente. Los tres se gestionan con controles previos —listas de "
            "exclusión, verificación de inventario, revisión de consentimiento— y no con reacciones "
            "posteriores."
        ),
        conceptos=[
            ("tráfico no válido", "interacciones generadas por sistemas automatizados que no corresponden a personas"),
            ("seguridad de marca", "control sobre el entorno donde aparece el anuncio"),
            ("consentimiento de cookies", "autorización informada para el uso de identificadores de seguimiento"),
            ("control previo", "medida establecida antes de la exposición que reduce el riesgo"),
        ],
        metodo=[
            "revisar los informes de calidad de tráfico",
            "definir listas de exclusión de sitios y categorías",
            "verificar el mecanismo de consentimiento del sitio propio",
            "auditar el tratamiento de datos en las plataformas usadas",
            "documentar los controles y revisarlos cada semestre",
        ],
        senales=[
            ("proporción de tráfico no válido", "interacciones marcadas como inválidas, sobre interacciones totales"),
            ("apariciones en contexto no deseado", "impresiones en sitios excluidos o inapropiados, sobre impresiones totales"),
            ("tasa de consentimiento válido", "visitantes con consentimiento registrado conforme, sobre visitantes totales"),
        ],
        caso=(
            "Ruta Andina descubre que el 14 % de sus clics proviene de sitios de contenido descargable y que "
            "su banner apareció junto a contenido incompatible con su marca."
        ),
        limite=(
            "Los controles reducen el riesgo pero también el alcance disponible y pueden subir el costo. La "
            "decisión debe ser explícita y no un efecto colateral."
        ),
        libros=["oneil", "kaushik", "nist-airmf", "chaffey"],
        error=("Operar sin listas de exclusión ni revisión de tráfico",
               "Define exclusiones y revisa mensualmente los informes de calidad de tráfico."),
    ),
    dict(
        n="14",
        slug="plan-de-performance-marketing",
        titulo="Plan de performance marketing",
        tesis=(
            "Esta clase integra la parte en un plan operativo: objetivos, estructura de campañas, audiencias, "
            "creatividades, presupuesto con ritmo, medición, controles de riesgo y umbrales de decisión. La "
            "prueba de calidad es que el plan indique de antemano qué se hará si el costo por oportunidad "
            "sube 30 % o si un canal deja de rendir."
        ),
        conceptos=[
            ("umbral de decisión", "valor de una métrica que activa una acción definida de antemano"),
            ("plan de contingencia", "conjunto de respuestas preparadas ante escenarios adversos"),
            ("gobierno de la inversión", "reglas de autoridad sobre cambios de presupuesto y de configuración"),
            ("registro de aprendizajes", "documentación acumulada de qué funcionó y qué no, con evidencia"),
        ],
        metodo=[
            "consolidar objetivos, estructura y presupuesto",
            "definir umbrales de decisión por métrica",
            "preparar contingencias para los escenarios principales",
            "establecer el gobierno de cambios y su registro",
            "revisar mensualmente contra los umbrales definidos",
        ],
        senales=[
            ("cumplimiento de umbrales", "métricas dentro de los umbrales definidos, sobre métricas monitoreadas"),
            ("acciones ejecutadas por contingencia", "contingencias activadas, sobre eventos que las gatillaban"),
            ("aprendizajes documentados", "aprendizajes registrados con evidencia, por trimestre"),
        ],
        caso=(
            "El presupuesto publicitario de Ruta Andina para el próximo año es CLP 50 millones. El directorio "
            "pregunta qué se hará si el costo por oportunidad sube 30 %."
        ),
        limite=(
            "Los umbrales fijos pueden inducir reacciones ante ruido. Deben definirse considerando la "
            "variación normal de cada métrica."
        ),
        libros=["kaushik", "geddes", "binet-field", "wheeler-dv"],
        error=("Presentar un plan sin umbrales ni contingencias",
               "Define para cada métrica crítica el valor que activa una acción y cuál es esa acción."),
    ),
]
