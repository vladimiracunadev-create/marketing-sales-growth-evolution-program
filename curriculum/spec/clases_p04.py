# -*- coding: utf-8 -*-
"""Parte 04 — Segmentación, targeting y posicionamiento."""

CLASES = [
    dict(
        n="01",
        slug="segmentacion-util-versus-decorativa",
        titulo="Segmentación útil versus decorativa",
        tesis=(
            "Una segmentación es útil cuando cambia al menos una de cuatro cosas: la oferta, el precio, el "
            "canal o el mensaje. Si al mover a un cliente de un segmento a otro nada cambia en la operación, "
            "la segmentación es decorativa y sólo consume tiempo de reuniones. Kotler sistematizó los "
            "criterios de una segmentación operativa: medible, sustancial, accesible, diferenciable y "
            "accionable. El último es el que más se incumple en la práctica."
        ),
        conceptos=[
            ("segmento accionable", "grupo al que la empresa puede alcanzar y tratar de forma distinta con los recursos actuales"),
            ("variable discriminante", "característica cuya variación se asocia a diferencias reales de comportamiento o valor"),
            ("sustancialidad", "tamaño suficiente del segmento para justificar un tratamiento propio"),
            ("costo de la segmentación", "gasto adicional en producción, operación y gestión que impone tratar segmentos por separado"),
        ],
        metodo=[
            "listar las decisiones que la segmentación debería cambiar",
            "proponer variables candidatas y verificar su poder discriminante",
            "estimar tamaño y accesibilidad de cada segmento",
            "calcular el costo de tratarlos de forma separada",
            "conservar sólo los segmentos que superan ese costo",
        ],
        senales=[
            ("diferencial de comportamiento entre segmentos", "diferencia en conversión, ticket o retención entre segmentos ante el mismo tratamiento"),
            ("costo incremental por segmento", "gasto adicional de producción y operación atribuible a mantener el segmento separado"),
            ("proporción de decisiones segmentadas", "decisiones comerciales que efectivamente difieren por segmento, sobre decisiones tomadas"),
        ],
        caso=(
            "Ruta Andina mantiene nueve segmentos por rubro. Los materiales, el precio y el proceso comercial "
            "son idénticos en los nueve; la segmentación sólo existe en una lámina."
        ),
        limite=(
            "Menos segmentos casi siempre es mejor al comenzar: cada segmento adicional multiplica materiales, "
            "mediciones y coordinación. La sofisticación debe llegar cuando la operación puede sostenerla."
        ),
        libros=["kotler", "sharp", "fader", "rumelt"],
        error=("Segmentar por variables que no cambian ninguna decisión",
               "Elimina todo segmento que no produzca una diferencia real en oferta, precio, canal o mensaje."),
    ),
    dict(
        n="02",
        slug="variables-de-segmentacion-b2c",
        titulo="Variables de segmentación B2C",
        tesis=(
            "En consumo masivo conviven cuatro familias de variables: demográficas, geográficas, "
            "psicográficas y conductuales. La evidencia de Sharp cuestiona el uso ingenuo de las "
            "psicográficas: las marcas grandes crecen sobre todo por penetración, y sus compradores se "
            "parecen mucho a los de la competencia. Eso no invalida la segmentación, pero corrige la "
            "expectativa: sirve más para asignar recursos y adaptar ejecución que para descubrir tribus "
            "exclusivas."
        ),
        conceptos=[
            ("variable demográfica", "característica objetiva de la persona como edad, ingreso, ocupación o composición del hogar"),
            ("variable psicográfica", "valores, actitudes e intereses declarados que se asocian a preferencias"),
            ("variable conductual", "acción registrada de compra o uso, como frecuencia, recencia o categoría comprada"),
            ("penetración", "proporción de la población objetivo que compró la categoría o la marca en un periodo"),
        ],
        metodo=[
            "definir la decisión que la segmentación debe informar",
            "priorizar variables conductuales por su disponibilidad y poder predictivo",
            "complementar con demográficas sólo si mejoran la predicción",
            "verificar tamaño y alcanzabilidad de cada grupo",
            "medir si el tratamiento diferenciado produce efecto",
        ],
        senales=[
            ("penetración por segmento", "compradores del segmento en el periodo, sobre población estimada del segmento"),
            ("frecuencia de compra", "compras por comprador en el periodo, por segmento"),
            ("elasticidad de respuesta", "cambio porcentual en conversión ante el mismo estímulo, comparado entre segmentos"),
        ],
        caso=(
            "La línea de hardware de Ruta Andina segmenta por «estilo de vida emprendedor». Los datos de "
            "compra muestran que la variable que predice recompra es haber comprado impresora térmica antes, "
            "no el estilo declarado."
        ),
        limite=(
            "Los datos demográficos y de comportamiento son datos personales: su tratamiento requiere base "
            "legal, finalidad declarada y medidas de seguridad conforme a la normativa vigente en Chile."
        ),
        libros=["sharp", "solomon", "kotler", "fader"],
        error=("Construir segmentos psicográficos sin verificar poder predictivo",
               "Compara la capacidad predictiva de la variable psicográfica contra una conductual disponible."),
    ),
    dict(
        n="03",
        slug="variables-de-segmentacion-b2b",
        titulo="Variables de segmentación B2B",
        tesis=(
            "En B2B las variables útiles son firmográficas —rubro, tamaño, madurez, geografía—, operativas "
            "—tecnología instalada, volumen de transacciones, complejidad— y de comportamiento de compra "
            "—proceso, ciclo, tamaño del comité—. La segmentación relevante suele cruzar dos ejes: capacidad "
            "de obtener valor con la solución y costo de servir. Ese cruce revela segmentos rentables que la "
            "clasificación por rubro esconde."
        ),
        conceptos=[
            ("variable firmográfica", "atributo objetivo de la organización como tamaño, rubro, antigüedad o estructura"),
            ("variable operativa", "característica del funcionamiento del cliente que condiciona el valor obtenible"),
            ("capacidad de absorción", "aptitud del cliente para implementar y sostener el uso de la solución"),
            ("costo de servir", "recursos de implementación, soporte y gestión que consume ese tipo de cliente"),
        ],
        metodo=[
            "cruzar valor obtenible con costo de servir",
            "verificar el cruce con datos de retención y margen",
            "nombrar segmentos por comportamiento y no por rubro",
            "definir tratamiento comercial por segmento",
            "revisar el mapa cada semestre con datos nuevos",
        ],
        senales=[
            ("margen por segmento", "ingreso menos costo de servir, dividido por ingreso, calculado por segmento y trimestre"),
            ("tiempo de implementación", "días entre firma y puesta en marcha, mediana por segmento"),
            ("retención a 12 meses por segmento", "cuentas activas al mes 12, sobre cuentas incorporadas 12 meses antes"),
        ],
        caso=(
            "Ruta Andina descubre que los centros médicos pequeños tienen mejor precio pero triplican las "
            "horas de soporte por su necesidad de cumplir requisitos de registro clínico."
        ),
        limite=(
            "Los datos firmográficos públicos suelen estar desactualizados. Antes de construir política sobre "
            "ellos, verifica una muestra contra la realidad operativa del cliente."
        ),
        libros=["moore", "ross", "fader", "roberge"],
        error=("Segmentar B2B sólo por rubro",
               "Agrega capacidad de absorción y costo de servir como ejes antes de definir el tratamiento."),
    ),
    dict(
        n="04",
        slug="clustering-conceptual-de-clientes",
        titulo="Clustering conceptual de clientes",
        tesis=(
            "Agrupar clientes por similitud es una técnica poderosa y fácil de mal usar. El algoritmo siempre "
            "devuelve grupos, incluso cuando no existen. La utilidad depende de tres decisiones humanas: qué "
            "variables entran, cómo se escalan y qué significa cada grupo en términos de negocio. Un cluster "
            "que no puede describirse en una frase accionable no sirve, aunque sea estadísticamente "
            "impecable."
        ),
        conceptos=[
            ("variable de entrada", "atributo incluido en el agrupamiento, cuya escala condiciona el resultado"),
            ("cohesión del grupo", "grado en que los miembros de un grupo se parecen entre sí más que a los de otros grupos"),
            ("interpretabilidad", "posibilidad de describir el grupo con una regla de negocio comprensible"),
            ("estabilidad temporal", "permanencia de la estructura de grupos al repetir el análisis en otro periodo"),
        ],
        metodo=[
            "elegir variables con justificación de negocio",
            "normalizar escalas y documentar el criterio",
            "generar agrupaciones y evaluar cohesión",
            "describir cada grupo con una regla accionable",
            "verificar estabilidad en un periodo distinto",
        ],
        senales=[
            ("cohesión y separación", "medida de distancia intragrupo frente a distancia entre grupos"),
            ("estabilidad entre periodos", "proporción de clientes que permanecen en el mismo grupo al repetir el análisis"),
            ("diferencia de valor entre grupos", "ingreso y retención promedio por grupo, con su dispersión"),
        ],
        caso=(
            "Un análisis entrega cinco clusters de clientes de Ruta Andina. Tres son indistinguibles en "
            "comportamiento comercial y ninguno puede describirse sin recurrir a coordenadas del modelo."
        ),
        limite=(
            "El agrupamiento describe, no explica. No indica causa ni predice respuesta a un tratamiento: para "
            "eso hace falta experimentación."
        ),
        libros=["provost", "fader", "croll-yoskovitz", "kaushik"],
        error=("Aceptar grupos que no se pueden describir en lenguaje de negocio",
               "Exige una regla verbal por grupo; si no existe, revisa las variables de entrada."),
    ),
    dict(
        n="05",
        slug="atractivo-y-accesibilidad-de-segmentos",
        titulo="Atractivo y accesibilidad de segmentos",
        tesis=(
            "Un segmento atractivo que no es accesible con los recursos disponibles vale cero en el corto "
            "plazo. La evaluación seria cruza dos dimensiones: atractivo —tamaño, crecimiento, margen, "
            "intensidad competitiva— y accesibilidad —existencia de canal, costo de alcance, ajuste de la "
            "oferta, capacidad de servir—. La disciplina consiste en puntuar ambas con criterios escritos y "
            "no con entusiasmo."
        ),
        conceptos=[
            ("atractivo del segmento", "combinación de tamaño, crecimiento, margen potencial e intensidad competitiva"),
            ("accesibilidad", "existencia de un canal viable y de un costo de alcance compatible con el margen"),
            ("ajuste de capacidad", "grado en que la operación actual puede entregar el resultado prometido a ese segmento"),
            ("criterio de puntuación", "escala documentada con definiciones que permite comparar segmentos sin arbitrariedad"),
        ],
        metodo=[
            "definir los criterios de atractivo y su ponderación",
            "definir los criterios de accesibilidad",
            "puntuar cada segmento con evidencia y no con impresión",
            "graficar la matriz y discutir los casos límite",
            "elegir y declarar explícitamente qué segmentos se descartan",
        ],
        senales=[
            ("costo de alcance por segmento", "gasto necesario para generar una oportunidad calificada en el segmento"),
            ("margen potencial por segmento", "margen de contribución estimado por cliente del segmento"),
            ("tasa de éxito en pilotos", "clientes del segmento que alcanzaron el resultado comprometido, sobre pilotos ejecutados"),
        ],
        caso=(
            "El vertical de centros médicos parece atractivo por ticket y crecimiento, pero exige "
            "certificaciones y un canal de venta que Ruta Andina no tiene ni puede construir en 12 meses."
        ),
        limite=(
            "La matriz ordena la conversación pero no decide: dos segmentos con puntajes similares exigen un "
            "criterio estratégico adicional, normalmente de foco y capacidad."
        ),
        libros=["kotler", "moore", "porter", "rumelt"],
        error=("Puntuar el atractivo sin evidencia",
               "Asocia cada puntaje a un dato o a un supuesto marcado, y registra su fuente."),
    ),
    dict(
        n="06",
        slug="targeting-y-priorizacion",
        titulo="Targeting y priorización",
        tesis=(
            "Elegir un objetivo implica renunciar a otros, y esa renuncia es la parte difícil. Rumelt "
            "observó que la mala estrategia se reconoce porque nunca dice qué no se hará. En targeting eso se "
            "traduce en una lista de segmentos ordenada con criterio explícito, con recursos asignados de "
            "forma desigual y con una regla clara sobre qué hacer con las oportunidades que llegan desde "
            "segmentos no prioritarios."
        ),
        conceptos=[
            ("segmento prioritario", "grupo que concentra recursos por decisión explícita y no por inercia"),
            ("regla de atención", "criterio que define cómo se trata una oportunidad fuera del foco"),
            ("concentración de recursos", "proporción del presupuesto y del tiempo asignada a los segmentos prioritarios"),
            ("costo de dispersión", "pérdida de efectividad por atender demasiados segmentos con la misma capacidad"),
        ],
        metodo=[
            "ordenar los segmentos con la matriz de atractivo y accesibilidad",
            "asignar recursos de forma deliberadamente desigual",
            "escribir la regla de atención para oportunidades fuera del foco",
            "comunicar la decisión al equipo comercial",
            "revisar trimestralmente con datos de resultado",
        ],
        senales=[
            ("concentración del pipeline", "valor de oportunidades en segmentos prioritarios, sobre valor total del pipeline"),
            ("resultado por segmento priorizado", "tasa de cierre y margen en segmentos prioritarios frente al resto"),
            ("tiempo comercial fuera de foco", "horas del equipo dedicadas a segmentos no prioritarios, sobre horas comerciales totales"),
        ],
        caso=(
            "Ruta Andina declara foco en talleres, pero el 58 % del tiempo comercial se destina a "
            "oportunidades entrantes de otros rubros porque «igual son ventas»."
        ),
        limite=(
            "El foco no significa rechazar todo negocio fuera de él: significa no invertir capacidad de "
            "desarrollo, materiales ni prospección proactiva en esos segmentos."
        ),
        libros=["rumelt", "porter-hbr", "moore", "doerr"],
        error=("Declarar foco sin cambiar la asignación de recursos",
               "Compara el reparto real de horas y presupuesto contra el foco declarado, cada trimestre."),
    ),
    dict(
        n="07",
        slug="estrategias-de-nicho",
        titulo="Estrategias de nicho",
        tesis=(
            "Una estrategia de nicho concentra recursos en un grupo estrecho para alcanzar una superioridad "
            "que sería imposible en un mercado amplio. Su lógica es de eficiencia: el mensaje se afina, la "
            "referencia circula dentro del gremio y el producto se especializa. Su riesgo es doble: techo de "
            "crecimiento y dependencia de un mercado que puede contraerse. Moore propone tratarlo como "
            "beachhead, es decir, como base para expandir y no como destino final."
        ),
        conceptos=[
            ("nicho", "segmento estrecho con necesidades homogéneas y canales de comunicación propios"),
            ("beachhead", "nicho inicial elegido por su capacidad de generar referencia hacia segmentos adyacentes"),
            ("dominancia en nicho", "posición de liderazgo reconocible dentro del grupo elegido"),
            ("adyacencia", "segmento vecino al que se puede expandir aprovechando reputación y producto existentes"),
        ],
        metodo=[
            "elegir un nicho con circulación interna de referencias",
            "especializar oferta y lenguaje para ese grupo",
            "medir dominancia relativa dentro del nicho",
            "identificar las adyacencias posibles",
            "definir la condición que gatilla la expansión",
        ],
        senales=[
            ("participación dentro del nicho", "clientes del nicho atendidos, sobre universo estimado del nicho"),
            ("tasa de referencia interna", "oportunidades originadas por clientes del mismo nicho, sobre oportunidades del nicho"),
            ("costo de adquisición en nicho frente a mercado amplio", "comparación del costo por cliente ganado en ambos contextos"),
        ],
        caso=(
            "Ruta Andina domina el segmento de talleres mecánicos de Valparaíso con 34 % de participación. La "
            "pregunta es si expandir a talleres de otras regiones o a rubros vecinos en la misma región."
        ),
        limite=(
            "Un nicho pequeño puede volverse una trampa: la especialización que dio ventaja se transforma en "
            "rigidez cuando llega el momento de servir a un segmento distinto."
        ),
        libros=["moore", "godin", "porter", "kim-mauborgne"],
        error=("Confundir nicho con público pequeño cualquiera",
               "Verifica que el grupo tenga canales propios y circulación interna de referencias."),
    ),
    dict(
        n="08",
        slug="diferenciacion",
        titulo="Diferenciación",
        tesis=(
            "Diferenciarse no es ser distinto: es ser distinto en algo que el cliente valora, puede percibir "
            "antes de comprar y el competidor no puede copiar rápido. Las tres condiciones deben cumplirse a "
            "la vez. La mayoría de las «diferencias» que declaran las empresas fallan en la segunda: son "
            "reales pero invisibles hasta después de la compra, y por lo tanto no influyen en la decisión."
        ),
        conceptos=[
            ("diferencia valorada", "atributo que el cliente considera relevante para su decisión"),
            ("diferencia perceptible", "atributo que el cliente puede verificar antes de comprar"),
            ("diferencia defendible", "atributo cuya imitación exige tiempo, inversión o capacidades que el competidor no tiene"),
            ("señal de calidad", "evidencia observable que comunica una diferencia difícil de verificar directamente"),
        ],
        metodo=[
            "listar las diferencias reales de la oferta",
            "verificar cuáles el cliente valora con evidencia",
            "evaluar si son perceptibles antes de comprar",
            "estimar el tiempo de imitación de cada una",
            "diseñar señales para las diferencias no perceptibles",
        ],
        senales=[
            ("menciones espontáneas de la diferencia", "clientes que citan el atributo como razón de elección, sobre clientes ganados"),
            ("prima de precio sostenida", "diferencia porcentual de precio efectivo frente al competidor, sostenida en el tiempo"),
            ("tiempo de imitación observado", "meses desde el lanzamiento hasta que un competidor ofrece un atributo equivalente"),
        ],
        caso=(
            "Ruta Andina afirma diferenciarse por «mejor soporte». El cliente no puede verificarlo antes de "
            "comprar y todos los competidores dicen lo mismo en su página de inicio."
        ),
        limite=(
            "Una diferencia defendible hoy puede dejar de serlo con un cambio tecnológico. La revisión debe ser "
            "periódica y no un ejercicio de una sola vez."
        ),
        libros=["porter-hbr", "ries-trout", "sharp2", "aaker"],
        error=("Declarar diferencias que el cliente no puede verificar",
               "Convierte cada diferencia no perceptible en una señal comprobable: garantía, prueba, dato público."),
    ),
    dict(
        n="09",
        slug="puntos-de-paridad-y-diferencia",
        titulo="Puntos de paridad y de diferencia",
        tesis=(
            "Keller distingue entre puntos de paridad —atributos necesarios para ser considerado parte de la "
            "categoría— y puntos de diferencia —los que justifican la elección—. El error frecuente es "
            "invertir todo el esfuerzo comunicacional en la diferencia mientras se incumple una paridad "
            "básica: si el cliente duda de que el producto haga lo esencial, ninguna diferencia lo "
            "convencerá."
        ),
        conceptos=[
            ("punto de paridad", "atributo que se debe alcanzar para ser considerado una alternativa válida"),
            ("punto de diferencia", "atributo que inclina la elección hacia esta oferta y no hacia otra"),
            ("paridad competitiva", "neutralización de una ventaja del competidor para que deje de ser criterio decisivo"),
            ("jerarquía de mensajes", "orden en que se comunican paridades y diferencias según la etapa del cliente"),
        ],
        metodo=[
            "identificar las paridades exigidas por la categoría",
            "verificar cuáles la oferta no cumple",
            "definir las diferencias que se quieren instalar",
            "ordenar los mensajes por etapa del cliente",
            "medir si la paridad dudosa sigue apareciendo como objeción",
        ],
        senales=[
            ("objeciones de paridad", "objeciones sobre requisitos básicos, sobre objeciones totales registradas"),
            ("reconocimiento de la diferencia", "clientes que identifican correctamente el punto de diferencia, en prueba de mensaje"),
            ("tasa de descalificación temprana", "oportunidades perdidas antes de la propuesta por incumplimiento de un requisito básico"),
        ],
        caso=(
            "La comunicación de Ruta Andina destaca su motor de recordatorios. En 4 de cada 10 negocios "
            "perdidos, la razón fue la duda sobre si emite documentos tributarios válidos: una paridad."
        ),
        limite=(
            "Las paridades cambian con la categoría: lo que hoy diferencia mañana es requisito. La lista debe "
            "revisarse al menos una vez al año."
        ),
        libros=["keller-brand", "kotler", "ries-trout", "sharp"],
        error=("Comunicar la diferencia antes de resolver la duda de paridad",
               "Ordena el mensaje: primero acredita el requisito básico, después instala la diferencia."),
    ),
    dict(
        n="10",
        slug="mapas-perceptuales",
        titulo="Mapas perceptuales",
        tesis=(
            "Un mapa perceptual representa cómo el mercado percibe a las alternativas en dos ejes relevantes "
            "para la decisión. Su valor depende enteramente de dos cosas: que los ejes sean criterios reales "
            "de elección y que las posiciones provengan de percepción medida, no de opinión interna. Un mapa "
            "construido en una reunión describe las creencias del equipo, no el mercado."
        ),
        conceptos=[
            ("eje perceptual", "criterio de decisión relevante sobre el cual el mercado ubica a las alternativas"),
            ("posición percibida", "ubicación que el mercado asigna a una marca, medida con datos y no supuesta"),
            ("espacio vacante", "zona del mapa sin ocupantes que puede o no representar una oportunidad real"),
            ("distancia percibida", "grado en que el mercado distingue una marca de otra"),
        ],
        metodo=[
            "identificar los criterios de decisión con investigación previa",
            "medir la percepción con una muestra del segmento",
            "construir el mapa con datos y no con juicio interno",
            "evaluar si los espacios vacantes tienen demanda",
            "definir el movimiento de posición y su costo",
        ],
        senales=[
            ("consistencia de la percepción", "dispersión de las respuestas sobre la ubicación de la marca en cada eje"),
            ("distancia con el competidor principal", "diferencia media de puntuación entre ambas marcas en los ejes relevantes"),
            ("cambio de posición en el tiempo", "variación de la posición medida entre dos olas de medición"),
        ],
        caso=(
            "El mapa que Ruta Andina usa en su plan fue dibujado por el equipo de marketing en una jornada de "
            "trabajo. Ninguna de las posiciones proviene de una medición con clientes."
        ),
        limite=(
            "Un espacio vacante puede estar vacío porque nadie lo quiere. Antes de moverse hacia él hay que "
            "verificar que exista demanda y disposición a pagar."
        ),
        libros=["ries-trout", "keller-brand", "malhotra", "aaker"],
        error=("Dibujar el mapa sin medición",
               "Recoge percepción con una muestra del segmento antes de ubicar cualquier marca en el mapa."),
    ),
    dict(
        n="11",
        slug="declaracion-de-posicionamiento",
        titulo="Declaración de posicionamiento",
        tesis=(
            "La declaración de posicionamiento es un documento interno que fija cuatro cosas: para quién es, "
            "en qué categoría compite, qué beneficio central promete y por qué eso es creíble. No es un "
            "eslogan ni se publica: es el criterio contra el cual se evalúan todas las piezas y decisiones "
            "comerciales. Su calidad se mide por su capacidad de rechazar ideas que no encajan."
        ),
        conceptos=[
            ("marco de referencia", "categoría en la que la marca quiere ser considerada por el cliente"),
            ("beneficio central", "resultado principal que la marca promete y que ordena el resto de la comunicación"),
            ("razón para creer", "evidencia que sostiene la promesa y que puede verificarse"),
            ("criterio de rechazo", "capacidad de la declaración de descartar ideas y piezas que no la respetan"),
        ],
        metodo=[
            "definir destinatario, categoría, beneficio y razón para creer",
            "verificar que el beneficio sea relevante y diferenciable",
            "probar la declaración rechazando tres ideas concretas",
            "difundirla como criterio de evaluación interno",
            "auditar piezas existentes contra la declaración",
        ],
        senales=[
            ("piezas alineadas", "piezas activas que respetan la declaración, sobre piezas auditadas"),
            ("ideas rechazadas por criterio", "propuestas descartadas citando la declaración, por trimestre"),
            ("consistencia de recuerdo", "proporción de clientes que atribuye a la marca el beneficio central declarado"),
        ],
        caso=(
            "Ruta Andina tiene tres versiones distintas de su promesa: una en la página, otra en la "
            "presentación comercial y otra en el pitch del fundador. Nadie sabe cuál manda."
        ),
        limite=(
            "El posicionamiento se instala con años de consistencia, no con una campaña. Cambiarlo cada "
            "semestre equivale a no tener ninguno."
        ),
        libros=["ries-trout", "keller-brand", "kotler", "aaker"],
        error=("Redactar la declaración como eslogan publicitario",
               "Escríbela como criterio interno de decisión, con destinatario, categoría, beneficio y evidencia."),
    ),
    dict(
        n="12",
        slug="reposicionamiento",
        titulo="Reposicionamiento",
        tesis=(
            "Reposicionar es caro porque exige desaprender lo que el mercado ya asoció a la marca. Se "
            "justifica cuando la posición actual limita el crecimiento, cuando el segmento se contrae o "
            "cuando la oferta cambió de forma sustantiva. La decisión debe considerar el costo de la "
            "transición, el riesgo de perder a los clientes actuales y el tiempo necesario para que la nueva "
            "posición se instale."
        ),
        conceptos=[
            ("posición heredada", "asociación existente en la mente del mercado, producto de la comunicación y la experiencia pasadas"),
            ("costo de transición", "inversión y pérdida temporal de claridad durante el cambio de posición"),
            ("riesgo de canibalización", "posibilidad de perder a clientes actuales al mover la promesa hacia otro segmento"),
            ("horizonte de instalación", "tiempo estimado hasta que la nueva posición sea reconocida por el mercado"),
        ],
        metodo=[
            "documentar la posición heredada con evidencia de percepción",
            "justificar por qué la posición actual limita el crecimiento",
            "estimar costo, riesgo y horizonte del cambio",
            "diseñar la transición con puentes explícitos",
            "medir la instalación de la nueva posición en olas sucesivas",
        ],
        senales=[
            ("cambio en atribución de beneficio", "diferencia entre olas en la proporción que asocia el nuevo beneficio a la marca"),
            ("retención durante la transición", "tasa de retención de clientes existentes en los seis meses posteriores al cambio"),
            ("costo total de la transición", "inversión en comunicación, materiales y capacitación asociada al reposicionamiento"),
        ],
        caso=(
            "Ruta Andina quiere pasar de «software de agendamiento» a «plataforma de gestión de ingresos para "
            "pymes de servicios». Sus clientes actuales la contrataron por lo primero."
        ),
        limite=(
            "Reposicionar no arregla un problema de producto ni de operación: si la experiencia contradice la "
            "nueva promesa, el cambio acelera la pérdida de confianza."
        ),
        libros=["ries-trout", "aaker", "keller-brand", "rumelt"],
        error=("Cambiar la comunicación sin cambiar la experiencia",
               "Verifica que la operación pueda sostener la nueva promesa antes de comunicarla."),
    ),
    dict(
        n="13",
        slug="prueba-de-posicionamiento",
        titulo="Prueba de posicionamiento",
        tesis=(
            "Un posicionamiento se prueba, no se declara. Las pruebas útiles son sencillas: exposición breve y "
            "recuerdo, comparación entre alternativas de mensaje, y medición de intención de avance en un "
            "contexto realista. Lo que se busca no es que guste, sino que sea comprendido, recordado y "
            "asociado al beneficio correcto. Un mensaje que gusta pero no se recuerda no cumple su función."
        ),
        conceptos=[
            ("prueba de comprensión", "verificación de que el destinatario puede explicar la promesa con sus palabras"),
            ("prueba de recuerdo", "medición de qué se retiene después de una exposición breve"),
            ("prueba de preferencia", "comparación entre alternativas con la misma audiencia y las mismas condiciones"),
            ("validez ecológica", "grado en que la prueba se parece a la situación real de exposición"),
        ],
        metodo=[
            "definir qué debe entenderse, recordarse y asociarse",
            "diseñar la prueba con condiciones realistas",
            "ejecutar con muestra suficiente del segmento",
            "analizar comprensión, recuerdo y preferencia por separado",
            "decidir con criterio previo y documentar el resultado",
        ],
        senales=[
            ("comprensión correcta", "personas que reformulan la promesa sin error, sobre personas expuestas"),
            ("recuerdo del beneficio central", "personas que recuerdan el beneficio tras 24 horas, sobre expuestas"),
            ("preferencia declarada frente a alternativa", "proporción que elige la propuesta sobre la alternativa, con intervalo reportado"),
        ],
        caso=(
            "El equipo de Ruta Andina eligió su nuevo mensaje por votación interna. En una prueba con 30 "
            "prospectos, la versión ganadora internamente quedó última en comprensión."
        ),
        limite=(
            "Las pruebas de mensaje predicen comprensión y recuerdo, no ventas. La decisión final debe "
            "considerar también el efecto sobre segmentos no incluidos en la prueba."
        ),
        libros=["heath", "keller-brand", "kohavi", "malhotra"],
        error=("Elegir el mensaje por votación del equipo",
               "Prueba con el segmento destinatario y decide por comprensión y recuerdo, no por gusto interno."),
    ),
    dict(
        n="14",
        slug="arquitectura-stp-completa",
        titulo="Arquitectura STP completa",
        tesis=(
            "Esta clase integra segmentación, targeting y posicionamiento en un documento único y coherente: "
            "quién es el segmento prioritario, por qué se eligió, qué se descartó, cuál es la promesa y qué "
            "evidencia la sostiene. La prueba de coherencia es que la arquitectura permita rechazar "
            "decisiones concretas: un canal, una funcionalidad, una campaña que no correspondan al foco "
            "elegido."
        ),
        conceptos=[
            ("arquitectura STP", "documento que conecta segmentación, elección de objetivo y posicionamiento con sus fundamentos"),
            ("coherencia interna", "ausencia de contradicción entre segmento elegido, promesa, precio y canal"),
            ("decisión descartada", "opción explícitamente rechazada con su razón, que impide reabrir la discusión sin datos nuevos"),
            ("indicador de seguimiento", "métrica que informa si la estrategia elegida está produciendo el efecto esperado"),
        ],
        metodo=[
            "consolidar la segmentación con sus criterios y evidencia",
            "declarar el foco y los descartes con su justificación",
            "fijar la declaración de posicionamiento y su prueba",
            "verificar coherencia entre promesa, precio, canal y operación",
            "definir los indicadores de seguimiento y su periodicidad",
        ],
        senales=[
            ("coherencia auditada", "decisiones comerciales del trimestre compatibles con la arquitectura, sobre decisiones revisadas"),
            ("evolución de participación en el segmento prioritario", "clientes del segmento atendidos, sobre universo estimado, medida semestralmente"),
            ("costo de adquisición en el foco", "costo por cliente ganado en el segmento prioritario frente al promedio general"),
        ],
        caso=(
            "Ruta Andina debe presentar su arquitectura STP al directorio como base del presupuesto anual. "
            "Hoy conviven tres focos declarados en documentos distintos."
        ),
        limite=(
            "La arquitectura es una hipótesis estratégica, no una verdad. Debe revisarse con datos de "
            "resultado y no defenderse por costo hundido."
        ),
        libros=["kotler", "rumelt", "ries-trout", "moore"],
        error=("Mantener varios focos declarados simultáneamente",
               "Consolida en un documento único y archiva formalmente las versiones anteriores."),
    ),
]
