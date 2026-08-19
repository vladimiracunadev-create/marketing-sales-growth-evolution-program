# -*- coding: utf-8 -*-
"""Parte 05 — Producto, oferta y propuesta de valor."""

CLASES = [
    dict(
        n="01",
        slug="producto-servicio-y-solucion",
        titulo="Producto, servicio y solución",
        tesis=(
            "Producto, servicio y solución no son sinónimos comerciales: describen tres niveles distintos de "
            "compromiso con el resultado del cliente. Un producto entrega una capacidad; un servicio entrega "
            "una actividad ejecutada; una solución entrega un resultado y asume parte del riesgo de "
            "lograrlo. Cada nivel cambia el precio, la estructura de costos, la promesa legal y el tipo de "
            "cliente que corresponde atender. Vender como solución lo que se opera como producto es la vía "
            "más rápida al churn y al reclamo."
        ),
        conceptos=[
            ("producto", "capacidad estandarizada que el cliente usa por su cuenta para obtener un resultado"),
            ("servicio", "actividad ejecutada por el proveedor con un nivel de desempeño comprometido"),
            ("solución", "conjunto integrado que asume responsabilidad sobre el resultado del cliente"),
            ("nivel de compromiso", "grado de riesgo del resultado que el proveedor traslada a su propio balance"),
        ],
        metodo=[
            "declarar qué resultado se promete y con qué alcance",
            "identificar qué parte del resultado depende del cliente",
            "elegir el nivel de compromiso sostenible por la operación",
            "traducir ese nivel a precio, contrato y capacidad",
            "verificar coherencia entre promesa comercial y operación real",
        ],
        senales=[
            ("cumplimiento de compromiso de servicio", "casos que cumplieron el nivel comprometido, sobre casos comprometidos en el periodo"),
            ("costo de servir por nivel", "horas y gastos por cliente según nivel de compromiso, comparados con el margen del plan"),
            ("reclamos por alcance", "reclamos que citan diferencias de alcance, sobre transacciones del periodo"),
        ],
        caso=(
            "Ruta Andina vende como «solución de gestión» algo que operativamente es un producto de "
            "autoservicio. Los clientes esperan configuración e informes que nadie está entregando."
        ),
        limite=(
            "Subir de nivel de compromiso exige capacidad instalada y contratos distintos. Prometer resultado "
            "sin controlar sus determinantes traslada un riesgo que la empresa no puede gestionar."
        ),
        libros=["kotler", "cagan", "osterwalder-vpd", "mehta"],
        error=("Comunicar solución y operar producto",
               "Alinea la promesa comercial con el nivel de servicio que la operación puede sostener y documenta el alcance."),
    ),
    dict(
        n="02",
        slug="value-proposition-canvas",
        titulo="Value Proposition Canvas",
        tesis=(
            "El canvas de Osterwalder separa dos mitades que suelen mezclarse: el perfil del cliente —tareas, "
            "dolores y ganancias— y el mapa de valor —productos, aliviadores y generadores—. Su utilidad no "
            "está en llenarlo sino en verificar el encaje: cada aliviador debe apuntar a un dolor documentado "
            "y cada generador a una ganancia que el cliente efectivamente busca. Los canvas llenos de "
            "supuestos son mapas de las creencias del equipo."
        ),
        conceptos=[
            ("perfil del cliente", "descripción de tareas, dolores y ganancias observadas y no supuestas"),
            ("aliviador de dolor", "elemento de la oferta que reduce un dolor específico y documentado"),
            ("encaje problema-solución", "correspondencia verificada entre lo que la oferta hace y lo que el cliente necesita"),
            ("supuesto no verificado", "elemento del canvas sin evidencia asociada, marcado como pendiente de validar"),
        ],
        metodo=[
            "completar el perfil del cliente sólo con evidencia",
            "mapear la oferta actual sin idealizarla",
            "trazar la correspondencia entre ambas mitades",
            "marcar los supuestos sin evidencia",
            "diseñar la validación de los tres supuestos más caros",
        ],
        senales=[
            ("proporción de elementos con evidencia", "elementos del canvas con fuente registrada, sobre elementos totales"),
            ("dolores atendidos por la oferta", "dolores documentados con aliviador correspondiente, sobre dolores priorizados"),
            ("supuestos validados por trimestre", "supuestos convertidos en hechos con evidencia, sobre supuestos marcados"),
        ],
        caso=(
            "El canvas de Ruta Andina lista once ganancias y ninguna proviene de entrevistas: fueron "
            "propuestas por el equipo de producto en una sesión de dos horas."
        ),
        limite=(
            "El canvas ordena el pensamiento pero no valida nada por sí mismo. Un canvas perfecto puede describir "
            "una propuesta que nadie comprará."
        ),
        libros=["osterwalder-vpd", "christensen", "fitzpatrick", "cagan"],
        error=("Llenar el canvas con supuestos sin marcarlos",
               "Marca con color o etiqueta cada elemento sin evidencia y define cómo se validará."),
    ),
    dict(
        n="03",
        slug="problema-solucion",
        titulo="Encaje problema-solución",
        tesis=(
            "El encaje problema-solución es anterior al encaje producto-mercado: verifica que el problema "
            "existe, que duele lo suficiente y que la solución propuesta lo alivia de forma perceptible. La "
            "evidencia útil no es el elogio sino el compromiso: personas que dedican tiempo, cambian su "
            "proceso o pagan antes de que el producto esté terminado. Sin ese encaje, escalar adquisición "
            "sólo acelera la pérdida."
        ),
        conceptos=[
            ("problema verificado", "dificultad documentada con frecuencia, costo y consecuencia para el cliente"),
            ("intensidad del dolor", "magnitud del costo que el problema impone y urgencia con que se busca resolverlo"),
            ("alivio perceptible", "reducción del problema que el cliente puede notar sin necesidad de un informe"),
            ("señal de compromiso", "acción costosa del cliente que confirma que el problema le importa"),
        ],
        metodo=[
            "documentar el problema con frecuencia y costo",
            "estimar la intensidad del dolor en el segmento",
            "verificar que la solución produce alivio perceptible",
            "buscar señales de compromiso antes de construir",
            "decidir avanzar, ajustar o abandonar con criterio previo",
        ],
        senales=[
            ("costo del problema declarado", "monto o tiempo que el cliente estima perder por el problema, por periodo"),
            ("tasa de compromiso previo", "prospectos que aceptaron una acción costosa, sobre prospectos entrevistados"),
            ("alivio percibido tras piloto", "clientes que reportan mejora atribuible, sobre clientes en piloto"),
        ],
        caso=(
            "Ruta Andina construyó un módulo de reportes avanzados en cuatro meses. Ningún cliente había "
            "pedido reportes ni había señales de compromiso previas al desarrollo."
        ),
        limite=(
            "Un problema intenso para pocos puede no sostener un negocio. El encaje problema-solución no "
            "reemplaza el dimensionamiento del segmento."
        ),
        libros=["ries-lean", "fitzpatrick", "blank", "cagan"],
        error=("Construir antes de obtener señales de compromiso",
               "Exige al menos tres señales costosas del cliente antes de comprometer desarrollo."),
    ),
    dict(
        n="04",
        slug="mvp-comercial",
        titulo="MVP comercial",
        tesis=(
            "El producto mínimo viable no es una versión incompleta: es el experimento más barato capaz de "
            "producir aprendizaje validado sobre una hipótesis específica. En contexto comercial suele no "
            "requerir código: una propuesta, una página, una demo manual o un servicio ejecutado a mano "
            "pueden bastar. El error habitual es llamar MVP a un producto reducido que se lanza sin "
            "hipótesis, sin criterio y sin plan de medición."
        ),
        conceptos=[
            ("hipótesis del MVP", "afirmación específica que el experimento debe confirmar o refutar"),
            ("nivel de fidelidad", "grado de terminación necesario para que la prueba sea válida"),
            ("aprendizaje validado", "conclusión respaldada por evidencia que modifica la siguiente decisión"),
            ("deuda de expectativa", "compromiso implícito adquirido con quienes probaron la versión inicial"),
        ],
        metodo=[
            "escribir la hipótesis y su criterio de refutación",
            "elegir el nivel mínimo de fidelidad que la prueba requiere",
            "definir la medición antes de lanzar",
            "ejecutar con un grupo acotado y consentido",
            "decidir perseverar, ajustar o abandonar con el criterio previo",
        ],
        senales=[
            ("tiempo hasta el primer aprendizaje", "días entre el inicio del experimento y la primera conclusión documentada"),
            ("costo por experimento", "costo directo e indirecto de la prueba, comparado con el valor de la decisión"),
            ("tasa de conversión del MVP", "usuarios que completaron la acción crítica, sobre usuarios expuestos"),
        ],
        caso=(
            "Para probar el interés en un plan por cadena, Ruta Andina puede construir el módulo completo en "
            "tres meses o vender el plan y operarlo manualmente durante seis semanas."
        ),
        limite=(
            "Un MVP genera expectativas reales en clientes reales. Debe declararse su carácter experimental y "
            "no puede usarse para cobrar por algo que no se entregará."
        ),
        libros=["ries-lean", "cagan", "blank", "kohavi"],
        error=("Llamar MVP a un producto reducido sin hipótesis",
               "Define hipótesis, criterio de refutación y medición antes de decidir el alcance del MVP."),
    ),
    dict(
        n="05",
        slug="product-market-fit",
        titulo="Product-market fit",
        tesis=(
            "El encaje producto-mercado no es un evento binario sino una acumulación de evidencia: retención "
            "que se estabiliza en una cohorte, uso repetido sin estímulo, crecimiento orgánico y clientes que "
            "se molestarían si el producto desapareciera. Ninguna métrica aislada lo demuestra. El riesgo "
            "práctico es declararlo antes de tiempo y escalar costos comerciales sobre una base que todavía "
            "se fuga."
        ),
        conceptos=[
            ("retención estabilizada", "curva de uso o permanencia que deja de caer y se aplana en una cohorte"),
            ("uso sin estímulo", "actividad que continúa sin campañas ni intervención comercial"),
            ("crecimiento orgánico", "incorporación de clientes sin gasto directo de adquisición atribuible"),
            ("prueba de decepción", "proporción de usuarios que declararía una pérdida relevante si el producto dejara de existir"),
        ],
        metodo=[
            "definir la acción que representa valor entregado",
            "construir curvas de retención por cohorte",
            "verificar si la curva se aplana y a qué nivel",
            "complementar con evidencia cualitativa de decepción",
            "decidir escalar sólo si la evidencia converge",
        ],
        senales=[
            ("retención por cohorte", "usuarios activos en el mes N, sobre usuarios que iniciaron en el mes 0, por cohorte"),
            ("proporción de crecimiento orgánico", "clientes nuevos sin origen pagado atribuible, sobre clientes nuevos totales"),
            ("resultado de la prueba de decepción", "usuarios que declaran decepción relevante, sobre usuarios encuestados con muestra definida"),
        ],
        caso=(
            "Ruta Andina declaró encaje al alcanzar 200 clientes. Las curvas por cohorte muestran caída "
            "continua hasta el mes 9 sin estabilizarse en ninguna cohorte."
        ),
        limite=(
            "El encaje puede existir en un segmento y no en otro. Declararlo de forma global esconde que el "
            "producto funciona sólo para una parte de la base."
        ),
        libros=["ellis-brown", "croll-yoskovitz", "cagan", "ries-lean"],
        error=("Declarar encaje con métricas agregadas",
               "Analiza retención por cohorte y por segmento antes de escalar el gasto comercial."),
    ),
    dict(
        n="06",
        slug="diseno-de-ofertas",
        titulo="Diseño de ofertas",
        tesis=(
            "Una oferta es la traducción comercial del producto: qué incluye, en qué condiciones, con qué "
            "garantía, a qué precio y con qué llamado a la acción. Dos empresas con el mismo producto pueden "
            "obtener resultados muy distintos según cómo lo empaqueten. Diseñar oferta implica decidir qué se "
            "excluye deliberadamente, porque una oferta que incluye todo no permite escalar precio ni "
            "diferenciar segmentos."
        ),
        conceptos=[
            ("alcance de la oferta", "conjunto explícito de lo incluido y lo excluido, con sus condiciones"),
            ("mecanismo de urgencia legítima", "razón real por la que conviene decidir ahora, sin presión artificial"),
            ("garantía", "compromiso que reduce el riesgo percibido y acota la responsabilidad del proveedor"),
            ("llamado a la acción", "siguiente paso concreto, con esfuerzo proporcional al nivel de confianza alcanzado"),
        ],
        metodo=[
            "definir el resultado que la oferta promete",
            "declarar inclusiones y exclusiones explícitas",
            "diseñar garantía y condiciones sostenibles",
            "elegir un llamado a la acción proporcional",
            "probar la oferta con un grupo acotado antes de publicarla",
        ],
        senales=[
            ("tasa de aceptación de la oferta", "aceptaciones, sobre propuestas presentadas, por segmento"),
            ("uso de la garantía", "solicitudes de garantía ejecutadas, sobre ventas cubiertas por ella"),
            ("consultas por alcance no claro", "consultas de clarificación recibidas, sobre propuestas enviadas"),
        ],
        caso=(
            "La propuesta estándar de Ruta Andina no dice qué pasa con la migración de datos ni cuántas horas "
            "de capacitación incluye. Cada vendedor promete algo distinto."
        ),
        limite=(
            "La urgencia artificial —cupos falsos, plazos que se repiten— puede constituir publicidad engañosa "
            "y erosiona la confianza incluso cuando funciona a corto plazo."
        ),
        libros=["ramanujam", "nagle", "sugarman", "cialdini"],
        error=("Dejar el alcance implícito en la propuesta",
               "Escribe inclusiones, exclusiones y condiciones en la propuesta estándar y audita su uso."),
    ),
    dict(
        n="07",
        slug="packaging-y-bundling",
        titulo="Packaging y bundling",
        tesis=(
            "Empaquetar es decidir qué va junto y qué se vende por separado. Un buen empaquetado alinea el "
            "precio con el valor recibido y facilita la elección; uno malo obliga a pagar por lo que no se "
            "usa o fragmenta tanto que nadie entiende qué comprar. Ramanujam propone diseñar los paquetes "
            "desde la disposición a pagar por atributo, y no desde la arquitectura técnica del producto."
        ),
        conceptos=[
            ("paquete", "combinación de componentes ofrecida como unidad con un precio propio"),
            ("componente diferenciador", "atributo con alta disposición a pagar que justifica un plan superior"),
            ("componente de volumen", "atributo de bajo valor incremental que conviene incluir en todos los planes"),
            ("canibalización de planes", "traslado de clientes desde un plan superior a uno inferior por diseño del paquete"),
        ],
        metodo=[
            "medir disposición a pagar por atributo",
            "clasificar atributos en diferenciadores, de volumen y opcionales",
            "construir dos o tres paquetes con lógica clara",
            "simular canibalización y margen por escenario",
            "probar la estructura antes de publicarla",
        ],
        senales=[
            ("distribución de ventas por plan", "unidades y margen por plan, sobre ventas totales del periodo"),
            ("tasa de migración entre planes", "clientes que cambian de plan, sobre clientes activos, por dirección del cambio"),
            ("margen por paquete", "ingreso menos costo de servir del paquete, dividido por ingreso del paquete"),
        ],
        caso=(
            "Ruta Andina tiene cinco planes y el 78 % de las ventas se concentra en el más barato porque "
            "incluye el módulo de pagos, que es el atributo más valorado."
        ),
        limite=(
            "Más paquetes no es mejor: la elección excesiva reduce conversión. Tres alternativas claras suelen "
            "superar a siete opciones matizadas."
        ),
        libros=["ramanujam", "nagle", "smith-pricing", "ariely"],
        error=("Diseñar planes desde la arquitectura técnica",
               "Construye los paquetes desde la disposición a pagar por atributo, medida en el segmento."),
    ),
    dict(
        n="08",
        slug="garantias-y-reduccion-de-riesgo",
        titulo="Garantías y reducción de riesgo",
        tesis=(
            "Una garantía traslada riesgo del cliente al proveedor y por eso aumenta la conversión. Su diseño "
            "debe cumplir tres condiciones: cubrir el riesgo que realmente frena la decisión, ser verificable "
            "sin discusión y ser sostenible para la operación. En Chile, además, existe una garantía legal "
            "que no depende de la voluntad del proveedor: la garantía comercial se suma a los derechos del "
            "consumidor, nunca los sustituye."
        ),
        conceptos=[
            ("garantía comercial", "compromiso voluntario del proveedor que se suma a los derechos legales del cliente"),
            ("riesgo cubierto", "contingencia específica que la garantía neutraliza y que frena la decisión"),
            ("costo esperado de la garantía", "probabilidad de ejecución multiplicada por su costo unitario"),
            ("verificabilidad", "claridad de las condiciones que evita discusión al momento de ejecutarla"),
        ],
        metodo=[
            "identificar el riesgo que efectivamente frena la decisión",
            "diseñar una garantía específica y verificable",
            "estimar su costo esperado y su efecto en conversión",
            "verificar la coherencia con la normativa de consumo",
            "medir ejecución y efecto en calidad del cliente ganado",
        ],
        senales=[
            ("efecto en conversión", "diferencia de conversión entre la oferta con garantía y sin garantía, con muestra definida"),
            ("tasa de ejecución", "garantías ejecutadas, sobre ventas cubiertas, por periodo"),
            ("costo de la garantía sobre margen", "costo total de ejecuciones, sobre margen de contribución del periodo"),
        ],
        caso=(
            "Ruta Andina ofrece «satisfacción garantizada» sin definir plazo ni condiciones. Dos clientes "
            "pidieron devolución a los cinco meses y no existe criterio para responder."
        ),
        limite=(
            "Una garantía no puede restringir derechos que la ley reconoce al consumidor. Cualquier cláusula "
            "que lo intente es inoponible y expone a la empresa a sanción."
        ),
        libros=["nagle", "cialdini", "dixon-effort", "ramanujam"],
        error=("Ofrecer garantías sin condiciones escritas",
               "Define plazo, alcance, procedimiento y costo esperado antes de publicar la garantía."),
    ),
    dict(
        n="09",
        slug="ciclo-de-vida-del-producto",
        titulo="Ciclo de vida del producto",
        tesis=(
            "El ciclo de vida —introducción, crecimiento, madurez, declive— es un marco descriptivo, no una "
            "ley. Su utilidad práctica está en obligar a preguntar en qué fase se encuentra cada producto y "
            "qué decisión corresponde: invertir en educación de mercado, en participación, en eficiencia o en "
            "retirada ordenada. Su riesgo es la profecía autocumplida: declarar un producto en declive y "
            "dejar de invertir produce el declive."
        ),
        conceptos=[
            ("fase del ciclo", "etapa estimada según crecimiento de la categoría y comportamiento competitivo"),
            ("decisión por fase", "tipo de inversión que corresponde a la fase estimada"),
            ("canibalización planificada", "reemplazo deliberado de un producto propio por otro más nuevo"),
            ("retiro ordenado", "proceso de discontinuación que protege a los clientes existentes y la reputación"),
        ],
        metodo=[
            "estimar la fase con datos de categoría y no de la propia empresa",
            "definir la decisión de inversión que corresponde",
            "planificar la canibalización si se lanza un reemplazo",
            "diseñar el retiro ordenado cuando corresponda",
            "revisar la estimación cada semestre",
        ],
        senales=[
            ("crecimiento de la categoría", "variación porcentual anual de la demanda estimada de la categoría"),
            ("participación relativa", "participación propia frente al competidor principal en el segmento"),
            ("margen por producto en el tiempo", "evolución del margen de contribución por producto, trimestral"),
        ],
        caso=(
            "La línea de hardware de Ruta Andina crece 4 % anual mientras el software crece 60 %. Nadie ha "
            "decidido si mantenerla, integrarla al paquete o retirarla."
        ),
        limite=(
            "El marco es descriptivo y puede inducir decisiones erróneas si la fase se estima con datos "
            "internos en lugar de datos de categoría."
        ),
        libros=["kotler", "moore", "porter", "cagan"],
        error=("Estimar la fase con datos propios",
               "Usa datos de la categoría y del comportamiento competitivo, no la curva de ventas propia."),
    ),
    dict(
        n="10",
        slug="portafolio-y-arquitectura-de-oferta",
        titulo="Portafolio y arquitectura de oferta",
        tesis=(
            "Un portafolio es un sistema de decisiones sobre dónde asignar capacidad: qué productos "
            "sostienen la caja, cuáles construyen futuro y cuáles sólo consumen atención. La arquitectura de "
            "oferta define cómo se relacionan entre sí —complementos, escalones, sustitutos— y qué camino "
            "recorre un cliente al crecer. Sin esa arquitectura, cada lanzamiento agrega complejidad sin "
            "aumentar el valor del conjunto."
        ),
        conceptos=[
            ("rol del producto en el portafolio", "función que cumple: generar caja, construir posición, defender o explorar"),
            ("escalera de oferta", "secuencia de productos que un cliente puede recorrer a medida que crece"),
            ("complejidad del portafolio", "costo de mantener, comunicar y operar el conjunto de productos"),
            ("asignación de capacidad", "distribución de personas, desarrollo y presupuesto entre los productos"),
        ],
        metodo=[
            "asignar un rol explícito a cada producto",
            "calcular margen y consumo de capacidad por producto",
            "diseñar la escalera de crecimiento del cliente",
            "eliminar o fusionar lo que no cumple rol",
            "revisar la asignación de capacidad cada trimestre",
        ],
        senales=[
            ("margen y capacidad por producto", "margen de contribución y horas de equipo consumidas por producto, por trimestre"),
            ("tasa de ascenso en la escalera", "clientes que migran a un producto superior, sobre clientes elegibles"),
            ("productos sin rol definido", "productos activos sin rol asignado, sobre productos totales"),
        ],
        caso=(
            "Ruta Andina mantiene once combinaciones de plan y hardware. Cuatro representan el 2 % del ingreso "
            "y consumen un tercio de las consultas de soporte."
        ),
        limite=(
            "Podar el portafolio afecta a clientes reales. La discontinuación requiere plan de migración, aviso "
            "razonable y respeto de las condiciones contratadas."
        ),
        libros=["kotler", "cagan", "rumelt", "aaker"],
        error=("Lanzar productos sin asignarles un rol",
               "Exige rol, métrica y capacidad asignada antes de aprobar cualquier lanzamiento."),
    ),
    dict(
        n="11",
        slug="roadmap-orientado-a-valor",
        titulo="Roadmap orientado a valor",
        tesis=(
            "Un roadmap de funcionalidades con fechas es una promesa que casi siempre se incumple. Un roadmap "
            "orientado a valor organiza el trabajo por problema a resolver y resultado esperado, con niveles "
            "de confianza declarados. Para el equipo comercial esto es crítico: permite conversar con "
            "clientes sin comprometer fechas que producirán decepción y, eventualmente, reclamos por "
            "incumplimiento."
        ),
        conceptos=[
            ("resultado esperado", "cambio medible que la iniciativa busca producir en el cliente o en el negocio"),
            ("nivel de confianza", "grado de certeza declarado sobre alcance y plazo de una iniciativa"),
            ("compromiso comercial", "afirmación sobre el futuro que la empresa queda obligada a cumplir"),
            ("gestión de expectativa", "práctica de comunicar dirección sin comprometer fechas no confirmadas"),
        ],
        metodo=[
            "organizar el roadmap por problema y resultado",
            "asignar nivel de confianza a cada iniciativa",
            "definir qué puede comunicarse comercialmente y qué no",
            "acordar el protocolo de comunicación con ventas",
            "revisar el cumplimiento de lo comprometido cada trimestre",
        ],
        senales=[
            ("cumplimiento de lo comprometido", "iniciativas entregadas dentro del plazo comprometido, sobre iniciativas comprometidas"),
            ("negocios cerrados con promesa futura", "negocios cuyo cierre dependió de una funcionalidad no existente, sobre negocios cerrados"),
            ("churn asociado a promesa incumplida", "bajas que citan una funcionalidad prometida y no entregada, sobre bajas totales"),
        ],
        caso=(
            "Tres negocios de Ruta Andina se cerraron con la promesa de una integración contable. La "
            "iniciativa está en el roadmap con confianza baja y sin fecha comprometida."
        ),
        limite=(
            "Comunicar sólo dirección sin ninguna fecha puede frenar decisiones legítimas del cliente. El "
            "equilibrio es declarar el nivel de confianza, no ocultar el plan."
        ),
        libros=["cagan", "ries-lean", "roberge", "doerr"],
        error=("Vender funcionalidades que aún no existen",
               "Prohíbe comprometer por escrito iniciativas con nivel de confianza bajo y registra las excepciones."),
    ),
    dict(
        n="12",
        slug="voice-of-customer",
        titulo="Voice of Customer",
        tesis=(
            "Voice of Customer es el sistema que recoge, clasifica y enruta lo que dicen los clientes en todos "
            "los puntos de contacto: soporte, ventas, encuestas, reseñas, cancelaciones. Su valor está en la "
            "sistematización: un comentario suelto es anécdota; cien comentarios clasificados por tema y "
            "cruzados con datos de retención son evidencia. Sin enrutamiento a un responsable, el sistema "
            "sólo produce archivos."
        ),
        conceptos=[
            ("captura estructurada", "registro uniforme de la voz del cliente con tema, fuente, segmento y fecha"),
            ("taxonomía de temas", "clasificación estable que permite comparar volúmenes en el tiempo"),
            ("enrutamiento", "asignación de cada tema a un responsable con capacidad de actuar"),
            ("cierre del circuito", "comunicación al cliente de lo que se hizo con su comentario"),
        ],
        metodo=[
            "definir los puntos de captura y su formato",
            "construir una taxonomía de temas estable",
            "clasificar y cruzar con datos de comportamiento",
            "enrutar a responsables con capacidad de decidir",
            "cerrar el circuito con el cliente y medir el efecto",
        ],
        senales=[
            ("volumen por tema", "comentarios clasificados por tema, sobre comentarios totales del periodo"),
            ("temas con responsable asignado", "temas activos con responsable, sobre temas registrados"),
            ("tasa de cierre de circuito", "clientes que recibieron respuesta sobre su comentario, sobre comentarios accionables"),
        ],
        caso=(
            "Ruta Andina recibe comentarios en cuatro canales distintos. Ninguno se clasifica y el equipo de "
            "producto se entera de los problemas cuando aparecen en una reunión de escalamiento."
        ),
        limite=(
            "La voz del cliente sobrerrepresenta a quienes hablan. Debe complementarse con datos de "
            "comportamiento de quienes callan y se van."
        ),
        libros=["dixon-effort", "mehta", "reichheld", "portigal"],
        error=("Recoger comentarios sin taxonomía ni responsable",
               "Define temas estables y un responsable por tema antes de ampliar la captura."),
    ),
    dict(
        n="13",
        slug="prueba-de-concepto-comercial",
        titulo="Prueba de concepto comercial",
        tesis=(
            "Una prueba de concepto comercial verifica si la oferta se vende, no si el producto funciona. Se "
            "ejecuta con propuesta real, precio real y decisión real, aunque la entrega sea parcial o manual. "
            "Su resultado más valioso no es la venta sino el aprendizaje sobre objeciones, tiempo de decisión "
            "y disposición a pagar. Requiere honestidad explícita sobre el estado del producto."
        ),
        conceptos=[
            ("prueba con precio real", "presentación de la oferta con su precio efectivo para observar decisión genuina"),
            ("compromiso condicionado", "acuerdo de compra sujeto a la entrega de una condición futura verificable"),
            ("aprendizaje de objeciones", "registro estructurado de las razones de no avanzar en la prueba"),
            ("transparencia del estado", "declaración explícita de qué existe y qué está por construirse"),
        ],
        metodo=[
            "definir la hipótesis comercial a probar",
            "preparar propuesta y precio reales",
            "ejecutar con un grupo acotado y declarar el estado del producto",
            "registrar decisiones, objeciones y tiempos",
            "decidir avanzar o abandonar con criterio previo",
        ],
        senales=[
            ("tasa de aceptación con precio real", "aceptaciones, sobre propuestas presentadas en la prueba"),
            ("tiempo de decisión", "días entre presentación de la propuesta y respuesta del cliente, mediana"),
            ("objeciones por categoría", "objeciones clasificadas por causa, sobre propuestas rechazadas"),
        ],
        caso=(
            "Antes de construir el plan para cadenas, Ruta Andina puede presentar la propuesta con precio real "
            "a ocho cadenas y observar cuántas firman una carta de intención condicionada."
        ),
        limite=(
            "Vender lo que no existe sin declararlo es engaño. La prueba exige transparencia sobre el estado y "
            "condiciones claras de devolución si no se cumple lo acordado."
        ),
        libros=["ramanujam", "blank", "ries-lean", "fitzpatrick"],
        error=("Probar interés sin mostrar el precio",
               "Presenta el precio efectivo: sin él, la aceptación declarada no predice compra."),
    ),
    dict(
        n="14",
        slug="oferta-lista-para-vender",
        titulo="Oferta lista para vender",
        tesis=(
            "Esta clase integra la parte en una oferta operativa: propuesta de valor probada, alcance "
            "explícito, precio, garantía, materiales de venta y criterios de calificación. La prueba de "
            "calidad es operativa: un ejecutivo comercial que no participó del diseño debe poder presentarla, "
            "responder las cinco objeciones más frecuentes y cerrar sin inventar condiciones."
        ),
        conceptos=[
            ("oferta operativa", "conjunto completo de definiciones, materiales y reglas que permite vender sin improvisar"),
            ("criterio de calificación", "regla que define a qué cliente corresponde esta oferta y a cuál no"),
            ("material habilitante", "documento que permite al vendedor y al cliente avanzar sin el diseñador presente"),
            ("prueba de traspaso", "verificación de que otra persona puede ejecutar la oferta correctamente"),
        ],
        metodo=[
            "consolidar propuesta, alcance, precio y garantía",
            "producir los materiales mínimos de venta",
            "definir criterios de calificación y descalificación",
            "ejecutar la prueba de traspaso con alguien ajeno",
            "corregir lo que no resultó ejecutable y publicar la versión",
        ],
        senales=[
            ("resultado de la prueba de traspaso", "elementos que la persona ajena ejecutó correctamente, sobre elementos evaluados"),
            ("consistencia de propuestas emitidas", "propuestas que respetan alcance y precio estándar, sobre propuestas auditadas"),
            ("tasa de aceptación de la oferta consolidada", "aceptaciones, sobre propuestas presentadas tras la consolidación"),
        ],
        caso=(
            "Ruta Andina incorpora dos ejecutivos comerciales el próximo mes y hoy cada vendedor arma su "
            "propia propuesta en un documento personal."
        ),
        limite=(
            "Una oferta estandarizada reduce la flexibilidad. Debe existir un procedimiento de excepción con "
            "aprobación y registro, no una prohibición absoluta."
        ),
        libros=["ramanujam", "roberge", "weinberg-sales", "osterwalder-vpd"],
        error=("Publicar la oferta sin prueba de traspaso",
               "Haz que una persona ajena la presente completa antes de considerarla lista."),
    ),
]
