# -*- coding: utf-8 -*-
"""Parte 15 — E-commerce y marketplaces."""

CLASES = [
    dict(
        n="01",
        slug="modelo-operativo-e-commerce",
        titulo="Modelo operativo de e-commerce",
        tesis=(
            "Vender en línea es una operación logística y financiera antes que una vitrina. El modelo "
            "operativo define quién almacena, quién despacha, quién cobra, quién responde por una devolución "
            "y cuánto cuesta cada uno de esos pasos. La mayoría de los emprendimientos digitales que "
            "fracasan no tenía un problema de tráfico: tenía un costo por pedido superior a su margen y no lo "
            "sabía."
        ),
        conceptos=[
            ("costo por pedido", "suma de costos de producto, empaque, despacho, pasarela y atención por cada pedido"),
            ("modelo de cumplimiento", "forma en que se almacena, prepara y entrega el producto"),
            ("margen por pedido", "ingreso del pedido menos todos los costos variables asociados"),
            ("punto de equilibrio operativo", "volumen a partir del cual la operación cubre sus costos fijos"),
        ],
        metodo=[
            "mapear el flujo completo desde el pedido hasta la entrega",
            "costear cada paso con datos reales",
            "calcular el margen por pedido y por categoría",
            "identificar el punto de equilibrio operativo",
            "decidir qué pasos internalizar o externalizar",
        ],
        senales=[
            ("margen por pedido", "ingreso menos costos variables, dividido por ingreso, por categoría"),
            ("costo logístico sobre ingreso", "costo de preparación y despacho, sobre ingreso del periodo"),
            ("pedidos bajo el punto de equilibrio", "pedidos con margen negativo, sobre pedidos del periodo"),
        ],
        caso=(
            "La línea de hardware de Ruta Andina vende bien y pierde dinero: 16 % de comisión de marketplace, "
            "despacho subsidiado y 9 % de devoluciones que nadie costeó."
        ),
        limite=(
            "El costo por pedido varía con el volumen y con la mezcla de productos. Un cálculo promedio "
            "esconde categorías que pierden dinero en cada venta."
        ),
        libros=["flint", "croll-yoskovitz", "chaffey", "fader"],
        error=("Evaluar el canal por ingreso y no por margen por pedido",
               "Costea despacho, comisión y devoluciones antes de declarar rentable una categoría."),
    ),
    dict(
        n="02",
        slug="catalogo-y-merchandising-digital",
        titulo="Catálogo y merchandising digital",
        tesis=(
            "El catálogo es la estructura que permite encontrar: categorías, atributos, filtros y "
            "nomenclatura. Un catálogo mal estructurado obliga al visitante a buscar y la mayoría no lo "
            "hace: se va. El merchandising digital decide qué se muestra primero, y esa decisión debe "
            "responder a margen y disponibilidad, no sólo a popularidad."
        ),
        conceptos=[
            ("taxonomía de catálogo", "estructura de categorías y atributos que organiza los productos"),
            ("calidad del dato de producto", "completitud y exactitud de los atributos que permiten filtrar y comparar"),
            ("merchandising", "decisión sobre qué productos se destacan y en qué orden"),
            ("descubribilidad", "facilidad con que un visitante encuentra el producto que busca"),
        ],
        metodo=[
            "auditar la completitud de atributos del catálogo",
            "definir la taxonomía desde el vocabulario del cliente",
            "configurar filtros útiles y verificarlos",
            "priorizar el destacado por margen y disponibilidad",
            "medir búsquedas sin resultado y corregir",
        ],
        senales=[
            ("completitud de atributos", "productos con atributos obligatorios completos, sobre productos publicados"),
            ("búsquedas sin resultado", "búsquedas internas sin resultados, sobre búsquedas internas totales"),
            ("conversión por categoría", "pedidos, sobre visitas de categoría, comparado entre categorías"),
        ],
        caso=(
            "El 34 % de las búsquedas internas en la tienda de Ruta Andina no devuelve resultados porque los "
            "productos están cargados con nombres técnicos que nadie usa."
        ),
        limite=(
            "Un catálogo excesivamente detallado aumenta el costo de mantenimiento. La profundidad debe "
            "corresponder a los atributos que el cliente usa para decidir."
        ),
        libros=["krug", "flint", "eisenberg", "chaffey"],
        error=("Nombrar productos con vocabulario interno",
               "Usa los términos con que los clientes buscan, verificados en el informe de búsqueda interna."),
    ),
    dict(
        n="03",
        slug="product-detail-page",
        titulo="Página de producto",
        tesis=(
            "La página de producto debe responder todo lo que el cliente necesita para decidir sin contactar "
            "a nadie: qué es, si sirve para su caso, cuánto cuesta con despacho, cuándo llega, qué pasa si no "
            "funciona. En Chile la información al consumidor no es opcional: precio total, condiciones, "
            "garantía legal y derecho a retracto cuando corresponde deben estar disponibles antes de la "
            "compra."
        ),
        conceptos=[
            ("información suficiente", "conjunto de datos que permite decidir sin consultar"),
            ("precio total", "monto final incluyendo impuestos y costos de despacho conocidos"),
            ("garantía legal", "derecho del consumidor que existe con independencia de la garantía comercial"),
            ("compatibilidad declarada", "información que permite verificar si el producto sirve para el caso del cliente"),
        ],
        metodo=[
            "listar las preguntas que llegan a soporte antes de comprar",
            "responderlas en la página",
            "mostrar precio total y plazo de entrega",
            "declarar garantía y condiciones de devolución",
            "medir consultas previas a la compra y reducirlas",
        ],
        senales=[
            ("consultas previas a la compra", "consultas sobre información que la página debería contener, sobre pedidos"),
            ("tasa de conversión de la página", "pedidos, sobre visitas únicas de la página de producto"),
            ("devoluciones por información deficiente", "devoluciones cuyo motivo es incompatibilidad o expectativa, sobre devoluciones totales"),
        ],
        caso=(
            "El lector de tarjetas de Ruta Andina no indica con qué modelos de teléfono es compatible. El 41 "
            "% de las devoluciones se debe a incompatibilidad."
        ),
        limite=(
            "Demasiada información dificulta la lectura. La solución es jerarquía y secciones desplegables, no "
            "omitir datos que la ley exige o que el cliente necesita."
        ),
        libros=["krug", "eisenberg", "laja", "dixon-effort"],
        error=("Omitir información de compatibilidad o de costo total",
               "Publica precio total, plazo de entrega, compatibilidad y condiciones de devolución en la propia página."),
    ),
    dict(
        n="04",
        slug="checkout",
        titulo="Checkout",
        tesis=(
            "El checkout es donde se pierde la mayor parte del valor generado por todo lo anterior. Las "
            "causas de abandono son conocidas y en su mayoría corregibles: costos que aparecen al final, "
            "registro obligatorio, formularios largos, falta de medios de pago y desconfianza. Cada campo "
            "eliminado y cada costo revelado antes reducen el abandono."
        ),
        conceptos=[
            ("abandono de checkout", "sesiones que inician el proceso de pago y no lo completan"),
            ("costo sorpresa", "cargo revelado al final que altera la decisión ya tomada"),
            ("fricción de registro", "obligación de crear cuenta antes de poder pagar"),
            ("señal de seguridad", "elemento que reduce la desconfianza en el momento del pago"),
        ],
        metodo=[
            "medir el abandono por paso del checkout",
            "revelar todos los costos antes de iniciar el proceso",
            "eliminar campos y pasos no indispensables",
            "ofrecer compra sin registro obligatorio",
            "probar el flujo en dispositivos reales del segmento",
        ],
        senales=[
            ("tasa de abandono por paso", "abandonos, sobre entradas a cada paso del checkout"),
            ("tiempo de finalización", "mediana de segundos para completar el pago, por dispositivo"),
            ("tasa de error en pagos", "intentos fallidos, sobre intentos de pago"),
        ],
        caso=(
            "El checkout de Ruta Andina revela el costo de despacho en el último paso. El abandono en ese "
            "paso es 63 %."
        ),
        limite=(
            "Reducir fricción no puede comprometer la verificación necesaria para prevenir fraude. El "
            "equilibrio se define con datos de contracargos, no por defecto."
        ),
        libros=["krug", "laja", "eisenberg", "flint"],
        error=("Revelar el costo de despacho al final",
               "Muestra el costo total estimado desde la página de producto o el carrito."),
    ),
    dict(
        n="05",
        slug="pagos",
        titulo="Pagos",
        tesis=(
            "Los medios de pago determinan quién puede comprar y cuánto cuesta cada transacción. En Chile "
            "conviven débito, crédito, transferencia y billeteras, con costos y tasas de aprobación "
            "distintos. Las decisiones relevantes son tres: qué medios ofrecer según el segmento, cómo "
            "manejar los rechazos y cómo prevenir el fraude sin bloquear compras legítimas."
        ),
        conceptos=[
            ("tasa de aprobación", "transacciones aprobadas sobre transacciones intentadas, por medio de pago"),
            ("costo de la transacción", "comisión y costos asociados a cada medio de pago"),
            ("contracargo", "reversión de un pago solicitada por el titular, con su costo asociado"),
            ("falso rechazo", "transacción legítima bloqueada por reglas de prevención de fraude"),
        ],
        metodo=[
            "identificar los medios que usa el segmento",
            "medir aprobación y costo por medio",
            "analizar las causas de rechazo",
            "calibrar las reglas antifraude con datos de contracargos",
            "revisar la mezcla de medios cada semestre",
        ],
        senales=[
            ("tasa de aprobación por medio", "transacciones aprobadas, sobre intentadas, por medio de pago"),
            ("costo de pagos sobre ingreso", "comisiones totales, sobre ingreso del periodo"),
            ("tasa de contracargos", "contracargos recibidos, sobre transacciones aprobadas"),
        ],
        caso=(
            "El 22 % de las transacciones de Ruta Andina se rechaza. La causa principal es una regla "
            "antifraude que bloquea compras de regiones distintas a la de facturación."
        ),
        limite=(
            "Ampliar medios de pago aumenta el costo de conciliación y de operación. La decisión debe "
            "considerar el costo administrativo, no sólo la comisión."
        ),
        libros=["flint", "chaffey", "croll-yoskovitz", "krug"],
        error=("Calibrar reglas antifraude sin medir falsos rechazos",
               "Compara contracargos evitados contra ventas legítimas bloqueadas antes de endurecer las reglas."),
    ),
    dict(
        n="06",
        slug="fulfillment",
        titulo="Fulfillment",
        tesis=(
            "El cumplimiento es la promesa que el cliente experimenta. Un plazo incumplido daña más que un "
            "precio alto porque afecta la confianza y genera contacto con soporte. La decisión central es "
            "entre operar la logística propia o externalizarla, y depende del volumen, del margen y de la "
            "capacidad de sostener el estándar prometido."
        ),
        conceptos=[
            ("promesa de entrega", "plazo comunicado al cliente al momento de la compra"),
            ("cumplimiento del plazo", "proporción de pedidos entregados dentro de lo prometido"),
            ("costo de cumplimiento", "gasto de preparación, empaque y despacho por pedido"),
            ("incidencia logística", "pedido con problema de entrega que genera contacto y costo adicional"),
        ],
        metodo=[
            "medir el cumplimiento real antes de prometer",
            "definir la promesa con margen de seguridad",
            "costear el cumplimiento por zona y por tamaño",
            "monitorear incidencias y sus causas",
            "revisar la decisión de operar o externalizar con datos",
        ],
        senales=[
            ("cumplimiento del plazo prometido", "pedidos entregados en plazo, sobre pedidos despachados"),
            ("costo de cumplimiento por pedido", "gasto logístico total dividido por pedidos despachados"),
            ("tasa de incidencias", "pedidos con incidencia, sobre pedidos despachados, por zona"),
        ],
        caso=(
            "Ruta Andina promete entrega en 48 horas y cumple en 61 % de los casos. Cada incumplimiento "
            "genera en promedio 2,3 contactos con soporte."
        ),
        limite=(
            "Prometer plazos amplios reduce incumplimientos y también conversión. El punto óptimo se "
            "encuentra midiendo ambos efectos, no eligiendo uno."
        ),
        libros=["dixon-effort", "flint", "chaffey", "grove"],
        error=("Prometer plazos que la operación no cumple",
               "Calcula el plazo que se cumple en el 95 % de los casos y comunica ese, no el mejor caso."),
    ),
    dict(
        n="07",
        slug="conversion",
        titulo="Conversión en comercio digital",
        tesis=(
            "La conversión en comercio digital es un embudo con etapas medibles: visita, vista de producto, "
            "agregado al carrito, inicio de pago y compra. Trabajar sobre el promedio global no sirve: cada "
            "etapa tiene causas distintas de abandono. El análisis correcto identifica la mayor pérdida "
            "absoluta y no el peor porcentaje, porque mejorar una etapa con poco volumen produce poco "
            "efecto."
        ),
        conceptos=[
            ("embudo de comercio", "secuencia de etapas desde la visita hasta la compra con sus tasas de paso"),
            ("pérdida absoluta", "número de usuarios perdidos en una etapa, no su porcentaje"),
            ("segmentación de conversión", "análisis del embudo por dispositivo, origen y categoría"),
            ("hipótesis de causa", "explicación del abandono que puede verificarse con evidencia"),
        ],
        metodo=[
            "construir el embudo con datos propios",
            "identificar la mayor pérdida absoluta",
            "segmentar por dispositivo, origen y categoría",
            "formular hipótesis de causa con evidencia cualitativa",
            "intervenir y verificar el efecto con grupo de comparación",
        ],
        senales=[
            ("tasa de paso por etapa", "usuarios que avanzan, sobre usuarios que ingresaron a la etapa"),
            ("pérdida absoluta por etapa", "número de usuarios perdidos en cada etapa, por periodo"),
            ("conversión por dispositivo", "pedidos, sobre sesiones, comparado entre móvil y escritorio"),
        ],
        caso=(
            "La conversión móvil de Ruta Andina es 0,6 % frente a 2,4 % en escritorio, y el 71 % del tráfico "
            "es móvil. La mayor pérdida absoluta está allí."
        ),
        limite=(
            "Las tasas de conversión no son comparables entre categorías ni entre fuentes de tráfico. "
            "Compararlas sin segmentar produce conclusiones erróneas."
        ),
        libros=["laja", "eisenberg", "kaushik", "krug"],
        error=("Trabajar sobre el peor porcentaje y no sobre la mayor pérdida",
               "Prioriza por número absoluto de usuarios perdidos y por valor en juego."),
    ),
    dict(
        n="08",
        slug="abandono-de-carrito",
        titulo="Abandono de carrito",
        tesis=(
            "El abandono de carrito no es un solo fenómeno: incluye a quienes comparan precios, a quienes "
            "usan el carrito como lista de deseos y a quienes se encontraron con un obstáculo real. Las "
            "intervenciones deben distinguir esos casos. Recordar por correo funciona con el tercero y "
            "molesta a los primeros; corregir el obstáculo funciona con todos."
        ),
        conceptos=[
            ("intención de compra", "grado en que el usuario pretendía efectivamente comprar en esa sesión"),
            ("obstáculo real", "impedimento concreto que interrumpió la compra"),
            ("recuperación", "acción posterior que busca completar la compra abandonada"),
            ("frecuencia de recordatorio", "número de contactos posteriores al abandono y su espaciamiento"),
        ],
        metodo=[
            "clasificar los abandonos por causa probable",
            "corregir primero los obstáculos del proceso",
            "diseñar la recuperación sólo para casos con intención",
            "limitar la frecuencia y respetar la oposición",
            "medir recuperación incremental con grupo de control",
        ],
        senales=[
            ("tasa de abandono de carrito", "carritos no convertidos, sobre carritos creados"),
            ("tasa de recuperación", "compras completadas tras el recordatorio, sobre recordatorios enviados"),
            ("recuperación incremental", "diferencia de compras entre grupo con recordatorio y grupo de control"),
        ],
        caso=(
            "Ruta Andina envía tres recordatorios en 24 horas y atribuye a esa secuencia todas las compras "
            "posteriores, sin grupo de control que permita saber cuántas habrían ocurrido igual."
        ),
        limite=(
            "El envío de recordatorios requiere base de licitud y respeto a la oposición. Además, atribuir sin "
            "grupo de control sobreestima sistemáticamente el efecto."
        ),
        libros=["laja", "kohavi", "flint", "chaffey"],
        error=("Atribuir toda compra posterior al recordatorio",
               "Usa un grupo de control sin recordatorio para estimar el efecto incremental real."),
    ),
    dict(
        n="09",
        slug="aov-y-bundles",
        titulo="Ticket promedio y paquetes",
        tesis=(
            "Aumentar el ticket promedio suele ser más barato que aumentar el tráfico, porque opera sobre "
            "personas que ya decidieron comprar. Las palancas son conocidas: paquetes, umbrales de despacho "
            "gratis, complementos pertinentes. Su límite también: un paquete que obliga a comprar lo que no "
            "se necesita reduce la conversión y aumenta las devoluciones."
        ),
        conceptos=[
            ("ticket promedio", "ingreso del periodo dividido por número de pedidos"),
            ("paquete pertinente", "combinación que el cliente usaría efectivamente en conjunto"),
            ("umbral de beneficio", "monto que activa un incentivo como despacho sin costo"),
            ("efecto sobre conversión", "cambio en la tasa de compra provocado por la intervención de ticket"),
        ],
        metodo=[
            "analizar qué productos se compran juntos",
            "diseñar paquetes con lógica de uso real",
            "definir umbrales de beneficio con margen verificado",
            "medir efecto conjunto en ticket y en conversión",
            "revisar devoluciones asociadas a los paquetes",
        ],
        senales=[
            ("ticket promedio por segmento", "ingreso, sobre pedidos, por segmento y periodo"),
            ("efecto en conversión", "tasa de compra del grupo con la intervención, sobre tasa del grupo de control, en el mismo periodo"),
            ("devoluciones de productos en paquete", "devoluciones de productos vendidos en paquete, sobre unidades vendidas en paquete"),
        ],
        caso=(
            "El umbral de despacho gratis de Ruta Andina es CLP 60.000 y su ticket promedio es CLP 89.000: el "
            "incentivo se entrega a casi todos sin cambiar comportamiento."
        ),
        limite=(
            "Subir el ticket puede reducir la frecuencia de compra. La evaluación debe considerar el ingreso "
            "por cliente en el periodo, no sólo el ticket por pedido."
        ),
        libros=["ramanujam", "flint", "fader", "nagle"],
        error=("Fijar umbrales de beneficio bajo el ticket promedio",
               "Ubica el umbral por sobre el ticket actual y verifica el efecto en margen y conversión."),
    ),
    dict(
        n="10",
        slug="cross-sell-y-upsell",
        titulo="Venta cruzada y venta incremental",
        tesis=(
            "La venta cruzada ofrece un producto complementario; la incremental, una versión superior. Ambas "
            "funcionan cuando son pertinentes y en el momento correcto; ambas irritan cuando son genéricas o "
            "interrumpen. El criterio ético y comercial coincide: recomendar lo que el cliente efectivamente "
            "necesita produce más ingreso sostenido que empujar lo que deja más margen."
        ),
        conceptos=[
            ("pertinencia de la recomendación", "correspondencia entre lo recomendado y la necesidad real del cliente"),
            ("momento de la oferta", "instante del recorrido donde la sugerencia ayuda en lugar de interrumpir"),
            ("recomendación basada en comportamiento", "sugerencia derivada de patrones reales de compra conjunta"),
            ("costo de la interrupción", "efecto negativo sobre conversión y satisfacción de una oferta inoportuna"),
        ],
        metodo=[
            "analizar patrones reales de compra conjunta",
            "definir el momento donde la sugerencia ayuda",
            "priorizar pertinencia sobre margen",
            "medir aceptación, conversión global y devoluciones",
            "retirar las recomendaciones que dañan la conversión",
        ],
        senales=[
            ("tasa de aceptación de la recomendación", "recomendaciones aceptadas, sobre recomendaciones mostradas"),
            ("efecto en conversión global", "variación de la tasa de compra total con y sin recomendación"),
            ("devoluciones de productos recomendados", "devoluciones de productos añadidos por recomendación, sobre unidades añadidas"),
        ],
        caso=(
            "Ruta Andina recomienda su impresora térmica más cara a todos los compradores de lector de "
            "tarjetas. La aceptación es 3 % y la conversión del carrito cayó 8 %."
        ),
        limite=(
            "Las recomendaciones automatizadas heredan sesgos del histórico y pueden reforzar patrones "
            "indeseados. Requieren revisión humana periódica."
        ),
        libros=["fader", "flint", "cialdini", "laja"],
        error=("Recomendar por margen y no por pertinencia",
               "Construye las recomendaciones desde patrones reales de compra conjunta y mide el efecto en conversión global."),
    ),
    dict(
        n="11",
        slug="marketplaces",
        titulo="Marketplaces",
        tesis=(
            "Un marketplace entrega tráfico y confianza a cambio de comisión, reglas y pérdida de relación "
            "con el cliente. Es una decisión estratégica, no sólo un canal más: quien vende allí acepta "
            "competir por precio en una vitrina donde el diferenciador visible es limitado. La evaluación "
            "correcta compara margen neto y aprendizaje obtenido, no volumen."
        ),
        conceptos=[
            ("comisión efectiva", "porcentaje total retenido incluyendo comisión, publicidad interna y servicios"),
            ("pérdida de relación", "imposibilidad de contactar directamente al cliente y construir base propia"),
            ("competencia en vitrina", "presión de precio provocada por la comparación directa en el mismo espacio"),
            ("dependencia del canal", "riesgo de que un cambio de reglas afecte una parte sustantiva del ingreso"),
        ],
        metodo=[
            "calcular la comisión efectiva total",
            "evaluar el margen neto por producto en el canal",
            "definir qué productos corresponden al canal y cuáles no",
            "medir la dependencia y fijar un límite",
            "usar el canal para aprendizaje de demanda, no sólo para volumen",
        ],
        senales=[
            ("margen neto por producto en marketplace", "ingreso menos comisiones y costos, sobre ingreso del canal"),
            ("dependencia del canal", "ingreso del marketplace, sobre ingreso total de la línea"),
            ("diferencial de precio con tienda propia", "diferencia de precio efectivo entre canales, por producto"),
        ],
        caso=(
            "El marketplace representa el 28 % de las unidades de Ruta Andina y el 4 % del margen. Además "
            "impide contactar a esos clientes para vender el software."
        ),
        limite=(
            "Salir de un marketplace donde se tiene volumen puede afectar la caja de inmediato. La transición "
            "debe planificarse con construcción previa de canal propio."
        ),
        libros=["flint", "chaffey", "porter", "nagle"],
        error=("Medir el marketplace por volumen de unidades",
               "Calcula la comisión efectiva total y el margen neto antes de decidir la permanencia."),
    ),
    dict(
        n="12",
        slug="postventa",
        titulo="Postventa",
        tesis=(
            "La postventa es donde se define si el cliente vuelve. Incluye seguimiento del pedido, gestión de "
            "incidencias, devoluciones y garantía. En Chile, el derecho a retracto en compras a distancia y "
            "la garantía legal son obligaciones, no gestos comerciales: el proveedor debe informarlas y "
            "cumplirlas. Una postventa bien operada convierte un problema en una razón para volver."
        ),
        conceptos=[
            ("derecho a retracto", "facultad del consumidor de terminar la compra a distancia dentro del plazo legal"),
            ("garantía legal", "derecho a reparación, cambio o devolución que existe con independencia de la voluntad del proveedor"),
            ("esfuerzo del cliente", "cantidad de pasos y tiempo que exige resolver un problema"),
            ("recuperación de servicio", "gestión que convierte una experiencia negativa en confianza recuperada"),
        ],
        metodo=[
            "documentar el proceso de devolución y garantía",
            "informar los derechos de forma clara y accesible",
            "reducir el esfuerzo del cliente en la resolución",
            "medir tiempo de resolución e insatisfacción",
            "analizar causas raíz y corregir el origen",
        ],
        senales=[
            ("tiempo de resolución", "días entre la solicitud y la resolución efectiva, mediana"),
            ("esfuerzo declarado del cliente", "puntuación media de esfuerzo declarada tras la resolución, sobre una muestra definida de casos cerrados"),
            ("recompra tras incidencia resuelta", "clientes que vuelven a comprar tras una incidencia, sobre clientes con incidencia"),
        ],
        caso=(
            "Ruta Andina exige que las devoluciones se soliciten por correo, con boleta física y dentro de 5 "
            "días. El plazo legal de retracto es mayor y el requisito de boleta física es un obstáculo "
            "innecesario."
        ),
        limite=(
            "Un proceso de devolución muy laxo puede ser abusado. El equilibrio se gestiona con verificación "
            "proporcional, nunca restringiendo derechos legales."
        ),
        libros=["dixon-effort", "reichheld", "flint", "mehta"],
        error=("Restringir derechos del consumidor en las condiciones",
               "Revisa las condiciones publicadas contra la normativa vigente y elimina toda cláusula que limite derechos legales."),
    ),
    dict(
        n="13",
        slug="economia-del-e-commerce",
        titulo="Economía del e-commerce",
        tesis=(
            "La economía del comercio digital se juega en la contribución por pedido y en la frecuencia de "
            "recompra. Un negocio con margen delgado sólo funciona si el cliente vuelve; uno con margen alto "
            "puede sostenerse con compras únicas. Confundir ambos modelos lleva a invertir en adquisición "
            "donde no hay recompra o a descuidar la retención donde sí la hay."
        ),
        conceptos=[
            ("contribución por pedido", "ingreso menos todos los costos variables del pedido"),
            ("frecuencia de recompra", "número de compras por cliente en un periodo definido"),
            ("valor del cliente en comercio", "contribución acumulada esperada durante la relación"),
            ("modelo de compra única o repetida", "clasificación que determina dónde invertir el esfuerzo comercial"),
        ],
        metodo=[
            "calcular la contribución por pedido con costos completos",
            "medir la frecuencia de recompra por cohorte",
            "clasificar el modelo del negocio",
            "asignar esfuerzo a adquisición o retención según el modelo",
            "revisar la clasificación con datos cada semestre",
        ],
        senales=[
            ("contribución por pedido", "ingreso menos costos variables, dividido por pedidos"),
            ("frecuencia de recompra por cohorte", "compras por cliente en 12 meses, por cohorte de incorporación"),
            ("proporción de ingreso de clientes recurrentes", "ingreso de clientes con más de una compra, sobre ingreso total"),
        ],
        caso=(
            "El 88 % de los clientes de hardware de Ruta Andina compra una sola vez. La inversión en "
            "programas de fidelización de esa línea no tiene base."
        ),
        limite=(
            "La frecuencia de recompra depende de la categoría: un producto duradero no se repite y eso no "
            "indica un problema de retención."
        ),
        libros=["fader", "croll-yoskovitz", "flint", "fader-ltv"],
        error=("Invertir en retención donde la categoría no permite recompra",
               "Clasifica el modelo por frecuencia observada antes de asignar presupuesto de fidelización."),
    ),
    dict(
        n="14",
        slug="simulacion-de-tienda-rentable",
        titulo="Simulación de tienda rentable",
        tesis=(
            "Esta clase integra la parte en una simulación completa: catálogo, precios, costos de "
            "cumplimiento, comisiones, devoluciones, conversión y recompra. El resultado no es una tienda "
            "bonita sino un modelo económico que muestra bajo qué condiciones el negocio gana dinero y bajo "
            "cuáles no. La prueba de calidad es la sensibilidad: qué variable, al moverse 10 %, cambia el "
            "resultado de signo."
        ),
        conceptos=[
            ("modelo económico de la tienda", "representación de ingresos, costos y volúmenes con sus supuestos"),
            ("análisis de sensibilidad", "evaluación del efecto de variar cada supuesto sobre el resultado"),
            ("variable crítica", "supuesto cuyo cambio moderado altera la viabilidad del negocio"),
            ("escenario de estrés", "combinación adversa de supuestos usada para probar la resistencia del modelo"),
        ],
        metodo=[
            "construir el modelo con supuestos documentados",
            "calcular contribución y punto de equilibrio",
            "ejecutar el análisis de sensibilidad",
            "identificar las variables críticas",
            "definir los controles que vigilarán esas variables",
        ],
        senales=[
            ("contribución total del modelo", "ingreso menos costos variables, proyectado por escenario"),
            ("variables críticas identificadas", "supuestos cuya variación de 10 % altera el resultado en más de 30 %"),
            ("resultado en escenario de estrés", "contribución total proyectada bajo el escenario adverso, sobre contribución del escenario base"),
        ],
        caso=(
            "Ruta Andina debe decidir si mantiene, rediseña o cierra su línea de hardware. La decisión "
            "requiere un modelo económico con sensibilidad, no una opinión."
        ),
        limite=(
            "Un modelo es tan bueno como sus supuestos. Sin datos reales de conversión, devoluciones y costo "
            "logístico, la simulación sólo ordena la ignorancia."
        ),
        libros=["croll-yoskovitz", "flint", "provost", "hubbard"],
        error=("Presentar el modelo sin análisis de sensibilidad",
               "Identifica las variables críticas y muestra el resultado bajo escenario adverso."),
    ),
]
