# -*- coding: utf-8 -*-
"""Parte 07 — Pricing y monetización."""

CLASES = [
    dict(
        n="01",
        slug="precio-como-decision-estrategica",
        titulo="El precio como decisión estratégica",
        tesis=(
            "El precio es la única variable del marketing que produce ingreso directamente; todas las demás "
            "producen costo. Simon documentó que una mejora de 1 % en precio suele aumentar la utilidad "
            "operacional más que una mejora equivalente en volumen o en costo, porque no exige capacidad "
            "adicional. Sin embargo, en la mayoría de las pymes el precio se fija por costo más margen o por "
            "imitación, sin conocer la disposición a pagar. Esa omisión no es un detalle técnico: define el "
            "techo de rentabilidad del negocio."
        ),
        conceptos=[
            ("apalancamiento del precio", "efecto de una variación de precio sobre la utilidad, comparado con volumen y costo"),
            ("política de precios", "conjunto de reglas escritas sobre listas, descuentos, excepciones y autoridad"),
            ("métrica de cobro", "unidad sobre la que se cobra: usuario, local, transacción, volumen o resultado"),
            ("disposición a pagar", "monto máximo que un cliente pagaría antes de elegir otra alternativa"),
        ],
        metodo=[
            "calcular el efecto de ±5 % de precio sobre la utilidad",
            "documentar la política vigente y sus excepciones reales",
            "verificar si la métrica de cobro sigue al valor entregado",
            "estimar disposición a pagar con evidencia",
            "definir la decisión de precio y su responsable",
        ],
        senales=[
            ("precio efectivo promedio", "ingreso del periodo dividido por unidades vendidas, comparado con el precio de lista"),
            ("elasticidad observada", "variación porcentual de unidades ante una variación porcentual de precio, en periodos comparables"),
            ("dispersión de descuentos", "desviación estándar del descuento otorgado, por vendedor y por segmento"),
        ],
        caso=(
            "Ruta Andina fija su precio agregando 40 % al costo de servidores. Nadie ha estimado cuánto vale "
            "para un taller evitar dos citas perdidas por semana."
        ),
        limite=(
            "El apalancamiento del precio supone que el volumen no cae de forma proporcional. En categorías muy "
            "elásticas o con competidores capaces de sostener pérdidas, ese supuesto puede fallar."
        ),
        libros=["simon", "nagle", "ramanujam", "smith-pricing"],
        error=("Fijar precio por costo más margen",
               "Estima primero la disposición a pagar del segmento y usa el costo sólo como piso."),
    ),
    dict(
        n="02",
        slug="cost-plus-pricing",
        titulo="Pricing por costo",
        tesis=(
            "Fijar precio sumando un margen al costo es simple, defendible internamente y sistemáticamente "
            "subóptimo: ignora al cliente y a la competencia. Su único mérito es garantizar que no se venda "
            "bajo costo, lo que es necesario pero insuficiente. Además tiene una trampa lógica: el costo "
            "unitario depende del volumen, y el volumen depende del precio, por lo que el método razona en "
            "círculo. Su lugar correcto es como piso, no como método."
        ),
        conceptos=[
            ("costo variable unitario", "costo que se incurre por cada unidad adicional vendida o servida"),
            ("costo de servir completo", "suma de costos directos, soporte, implementación y comisiones atribuibles al cliente"),
            ("margen objetivo", "porcentaje que la empresa decide agregar sobre el costo"),
            ("circularidad costo-volumen", "dependencia mutua entre costo unitario y volumen que invalida el cálculo ingenuo"),
        ],
        metodo=[
            "identificar todos los costos atribuibles al cliente",
            "separar costos fijos de variables",
            "calcular el piso de precio por segmento",
            "contrastar el piso con la disposición a pagar",
            "usar el resultado como restricción y no como decisión",
        ],
        senales=[
            ("costo de servir por segmento", "costos directos e indirectos atribuibles, dividido por clientes del segmento"),
            ("proporción de ventas bajo el piso", "unidades vendidas bajo el costo de servir, sobre unidades del periodo"),
            ("margen de contribución real", "ingreso menos costo variable completo, dividido por ingreso"),
        ],
        caso=(
            "El plan básico de Ruta Andina se fijó con 40 % de margen sobre costos de infraestructura. Al "
            "incluir las 9 horas de migración, el margen real es negativo."
        ),
        limite=(
            "Sin un costeo que incluya implementación y soporte, el piso calculado es ficticio y puede llevar a "
            "vender con pérdida creyendo que hay margen."
        ),
        libros=["nagle", "simon", "smith-pricing", "croll-yoskovitz"],
        error=("Calcular el piso sin costo de servir completo",
               "Incorpora horas de implementación, soporte y comisiones antes de declarar el margen."),
    ),
    dict(
        n="03",
        slug="competitor-based-pricing",
        titulo="Pricing por competencia",
        tesis=(
            "Fijar precio mirando al competidor es rápido y peligroso: se importa la estructura de costos y "
            "la estrategia de otro. Sólo es defendible cuando la oferta es realmente comparable y el cliente "
            "puede verificar esa equivalencia. En la mayoría de los casos las ofertas difieren en alcance, "
            "servicio o riesgo, y comparar sólo el número de la lista produce decisiones equivocadas en ambas "
            "direcciones."
        ),
        conceptos=[
            ("precio de referencia competitivo", "precio que el cliente considera normal en la categoría, formado por las alternativas visibles"),
            ("comparabilidad real", "grado en que dos ofertas entregan el mismo alcance, riesgo y servicio"),
            ("guerra de precios", "espiral de reducciones que erosiona el margen de toda la categoría"),
            ("valor diferencial cuantificado", "monto en que la oferta supera a la alternativa, expresado en la unidad del cliente"),
        ],
        metodo=[
            "construir la comparación con alcance equivalente",
            "cuantificar el valor diferencial en unidades del cliente",
            "estimar la capacidad del competidor de sostener su precio",
            "decidir posición relativa con criterio explícito",
            "monitorear el efecto en participación y margen",
        ],
        senales=[
            ("brecha de precio ajustada por alcance", "diferencia de precio efectivo tras normalizar por alcance y servicio incluido"),
            ("participación en negocios enfrentados", "negocios ganados frente al competidor, sobre negocios donde estuvo presente"),
            ("evolución del margen tras el ajuste", "variación del margen de contribución en los dos trimestres posteriores"),
        ],
        caso=(
            "El competidor de Ruta Andina publica CLP 29.900 mensuales sin migración ni soporte. La "
            "comparación directa deja a Ruta Andina 34 % más cara por una oferta que no es equivalente."
        ),
        limite=(
            "Igualar precios con un competidor financiado por capital de riesgo puede ser insostenible. La "
            "comparación debe incluir capacidad de resistencia, no sólo nivel de precio."
        ),
        libros=["nagle", "porter", "simon", "smith-pricing"],
        error=("Comparar precios de lista sin normalizar alcance",
               "Construye una tabla de equivalencia que incluya implementación, soporte y garantías."),
    ),
    dict(
        n="04",
        slug="value-based-pricing",
        titulo="Pricing basado en valor",
        tesis=(
            "El pricing basado en valor parte del beneficio económico que la oferta produce para un segmento y "
            "captura una fracción de él. Requiere tres piezas: una alternativa de referencia clara, el valor "
            "diferencial cuantificado en la unidad del cliente y una regla de captura explícita. Nagle "
            "advierte que el método no consiste en cobrar todo el valor: dejar excedente al cliente es lo que "
            "sostiene la relación y hace defendible el precio."
        ),
        conceptos=[
            ("valor de referencia", "costo de la mejor alternativa disponible para el cliente"),
            ("valor diferencial", "beneficio adicional que la oferta produce frente a esa alternativa, cuantificado"),
            ("regla de captura", "proporción del valor diferencial que la empresa decide cobrar"),
            ("excedente para el cliente", "parte del valor diferencial que queda en manos del cliente y sostiene la elección"),
        ],
        metodo=[
            "identificar la alternativa de referencia del segmento",
            "cuantificar el valor diferencial en unidades del cliente",
            "verificar la cuantificación con clientes reales",
            "definir la regla de captura y justificarla",
            "probar el precio resultante antes de generalizarlo",
        ],
        senales=[
            ("valor diferencial verificado", "clientes que confirman la magnitud estimada, sobre clientes consultados"),
            ("tasa de aceptación al nuevo precio", "aceptaciones, sobre propuestas presentadas con el precio basado en valor"),
            ("proporción de valor capturado", "precio cobrado, sobre valor diferencial estimado, por segmento"),
        ],
        caso=(
            "Para un taller que pierde 6 citas semanales a CLP 45.000 cada una, el valor diferencial de "
            "reducir inasistencias a la mitad es del orden de CLP 540.000 mensuales. El plan cuesta CLP "
            "79.000."
        ),
        limite=(
            "El valor no es uniforme dentro de un segmento: el mismo cálculo puede sobreestimar el beneficio "
            "para clientes con menor volumen. La estimación debe declarar su rango."
        ),
        libros=["nagle", "ramanujam", "simon", "hubbard"],
        error=("Cuantificar el valor sin verificarlo con clientes",
               "Presenta el cálculo a cinco clientes y ajusta los supuestos que rechacen."),
    ),
    dict(
        n="05",
        slug="willingness-to-pay",
        titulo="Disposición a pagar",
        tesis=(
            "La disposición a pagar es una distribución, no un número. Ramanujam sostiene que preguntarla "
            "temprano —antes de construir— evita el error más caro de la innovación: desarrollar algo que "
            "nadie pagará. Las técnicas van desde preguntas directas calibradas hasta análisis de "
            "compensación; todas tienen sesgos y ninguna reemplaza la observación de decisiones reales con "
            "precio real."
        ),
        conceptos=[
            ("distribución de disposición a pagar", "rango de montos que distintos clientes del segmento pagarían"),
            ("sesgo de declaración", "diferencia entre lo que el cliente dice que pagaría y lo que efectivamente paga"),
            ("análisis de compensación", "técnica que fuerza a elegir entre combinaciones de atributos y precio"),
            ("validación con decisión real", "observación de compra efectiva con precio real como prueba final"),
        ],
        metodo=[
            "definir el segmento y la configuración a evaluar",
            "elegir la técnica según presupuesto y precisión requerida",
            "recoger la distribución y no sólo el promedio",
            "corregir por sesgo de declaración",
            "validar con una prueba de decisión real",
        ],
        senales=[
            ("dispersión de la disposición declarada", "rango intercuartil de los montos declarados por el segmento"),
            ("diferencia declaración-comportamiento", "brecha entre disposición declarada y precio efectivamente aceptado"),
            ("tasa de aceptación por nivel de precio", "aceptaciones, sobre propuestas, para cada nivel de precio probado"),
        ],
        caso=(
            "Ruta Andina preguntó «¿cuánto pagarías?» y obtuvo un promedio de CLP 120.000. Al presentar una "
            "propuesta real a ese precio, la aceptación fue de 6 %."
        ),
        limite=(
            "Las técnicas declarativas sobreestiman sistemáticamente. Sirven para ordenar preferencias entre "
            "configuraciones, no para fijar el precio final."
        ),
        libros=["ramanujam", "nagle", "hubbard", "malhotra"],
        error=("Fijar precio con el promedio de lo declarado",
               "Usa la distribución completa y valida con una prueba de decisión real antes de publicar el precio."),
    ),
    dict(
        n="06",
        slug="elasticidad-y-sensibilidad",
        titulo="Elasticidad y sensibilidad al precio",
        tesis=(
            "La elasticidad mide cuánto cambia la cantidad demandada ante un cambio de precio. No es una "
            "constante: varía por segmento, por momento y por la presencia de alternativas visibles. Nagle "
            "identificó factores que la reducen —costo de cambio, valor único percibido, dificultad de "
            "comparar, gasto compartido— y esos factores son gestionables. Estimarla con datos propios "
            "requiere variación real de precios, no opinión."
        ),
        conceptos=[
            ("elasticidad precio", "variación porcentual de la cantidad ante una variación porcentual del precio"),
            ("factor de sensibilidad", "condición que aumenta o reduce la reacción del cliente ante el precio"),
            ("segmentación de sensibilidad", "diferencia de elasticidad entre grupos de clientes del mismo mercado"),
            ("prueba de precio", "experimento controlado que produce variación real para estimar la respuesta"),
        ],
        metodo=[
            "identificar los factores de sensibilidad presentes en el segmento",
            "diseñar una prueba con variación real y grupos comparables",
            "estimar la respuesta con intervalo de incertidumbre",
            "verificar si la respuesta difiere por segmento",
            "decidir el nivel de precio y su condición de revisión",
        ],
        senales=[
            ("elasticidad estimada por segmento", "variación porcentual de unidades sobre variación porcentual de precio, con intervalo"),
            ("tasa de abandono ante alza", "clientes que se dan de baja tras el aumento, sobre clientes afectados"),
            ("efecto en ingreso total", "ingreso del grupo tratado sobre ingreso del grupo de control, en el mismo periodo"),
        ],
        caso=(
            "Ruta Andina subió 12 % el precio a clientes nuevos y mantuvo el de los antiguos. Puede estimar la "
            "elasticidad comparando conversión entre ambos grupos si controla estacionalidad y mezcla."
        ),
        limite=(
            "Las pruebas de precio con clientes reales tienen consecuencias comerciales y éticas: cobrar "
            "distinto a personas equivalentes sin justificación puede constituir discriminación arbitraria."
        ),
        libros=["nagle", "kohavi", "simon", "smith-pricing"],
        error=("Estimar elasticidad con datos históricos sin controlar mezcla",
               "Usa grupos comparables y controla estacionalidad, canal y mezcla de segmentos."),
    ),
    dict(
        n="07",
        slug="van-westendorp-y-tecnicas-de-investigacion",
        titulo="Van Westendorp y técnicas de investigación de precio",
        tesis=(
            "Van Westendorp pregunta a qué precio el producto sería demasiado caro, caro pero aceptable, "
            "barato y tan barato que generaría dudas de calidad. El cruce de esas curvas sugiere un rango "
            "aceptable. Su virtud es la simplicidad y su defecto es conocido: mide percepción declarada, no "
            "decisión. Usada como insumo exploratorio es valiosa; usada como método de fijación produce "
            "precios cómodos para el cliente y pobres para la empresa."
        ),
        conceptos=[
            ("rango de precios aceptable", "intervalo entre el punto de baratura excesiva y el de carestía excesiva"),
            ("punto de precio óptimo", "cruce de curvas que la técnica sugiere como referencia, no como conclusión"),
            ("técnica de compensación", "método que fuerza elección entre configuraciones para revelar preferencias"),
            ("triangulación de métodos", "uso de dos o más técnicas para reducir el sesgo de cada una"),
        ],
        metodo=[
            "elegir la técnica según decisión, presupuesto y precisión",
            "aplicar con muestra representativa del segmento",
            "analizar rangos y no puntos únicos",
            "triangular con datos de comportamiento",
            "declarar el nivel de incertidumbre en la recomendación",
        ],
        senales=[
            ("amplitud del rango aceptable", "diferencia entre los extremos del rango identificado, por segmento"),
            ("coincidencia entre métodos", "diferencia entre el rango declarado y el precio de aceptación observado"),
            ("tamaño de muestra por segmento", "respuestas válidas por segmento, comparadas con el mínimo definido"),
        ],
        caso=(
            "El estudio de Van Westendorp de Ruta Andina sugiere un rango de CLP 45.000 a CLP 95.000. El "
            "equipo quiere fijar CLP 45.000 «para asegurar volumen»."
        ),
        limite=(
            "La técnica no considera la alternativa competitiva ni el valor diferencial. Un rango declarado "
            "puede estar completamente por debajo del valor real entregado."
        ),
        libros=["malhotra", "nagle", "ramanujam", "hubbard"],
        error=("Fijar el precio en el extremo inferior del rango",
               "Contrasta el rango declarado con el valor diferencial cuantificado antes de decidir."),
    ),
    dict(
        n="08",
        slug="versionado-y-price-fences",
        titulo="Versionado y price fences",
        tesis=(
            "Cobrar distinto a segmentos con distinta disposición a pagar aumenta el ingreso total, pero "
            "requiere barreras legítimas que impidan que quien puede pagar más acceda al precio menor. Esas "
            "barreras —volumen, funcionalidad, canal, plazo, tipo de cliente— deben ser transparentes y "
            "justificables. Una barrera arbitraria o basada en características personales protegidas no es "
            "una técnica de pricing: es una práctica indebida."
        ),
        conceptos=[
            ("price fence", "criterio objetivo que separa segmentos con precios distintos"),
            ("versionado", "creación de variantes del producto con valor y precio diferenciados"),
            ("arbitraje entre segmentos", "traslado de clientes al precio menor cuando la barrera es débil"),
            ("legitimidad de la barrera", "justificación objetiva y comunicable de la diferencia de precio"),
        ],
        metodo=[
            "identificar los segmentos con disposición a pagar distinta",
            "diseñar barreras basadas en criterios objetivos",
            "verificar que la barrera resiste el arbitraje",
            "comprobar la legitimidad y comunicabilidad del criterio",
            "medir migración entre versiones tras la implementación",
        ],
        senales=[
            ("tasa de arbitraje", "clientes que acceden al precio menor sin cumplir el criterio, sobre clientes del plan"),
            ("distribución de ingreso por versión", "ingreso por versión, sobre ingreso total del periodo"),
            ("reclamos por diferencia de precio", "reclamos que citan la diferencia, sobre transacciones del periodo"),
        ],
        caso=(
            "Ruta Andina ofrece precio de «pyme pequeña» sin definir el criterio. Tres cadenas se registran "
            "local por local para acceder a ese precio."
        ),
        limite=(
            "En Chile la diferenciación de precios debe basarse en criterios objetivos y comunicados. Cobrar "
            "distinto por características personales del consumidor puede constituir discriminación arbitraria."
        ),
        libros=["smith-pricing", "nagle", "ramanujam", "simon"],
        error=("Diferenciar precios sin criterio objetivo escrito",
               "Define el criterio, publícalo y verifica que la barrera resiste el arbitraje."),
    ),
    dict(
        n="09",
        slug="suscripcion-y-recurring-revenue",
        titulo="Suscripción e ingreso recurrente",
        tesis=(
            "La suscripción cambia la economía del negocio: el ingreso se reconoce en el tiempo, el costo de "
            "adquisición se recupera en meses y la retención pasa a ser la variable dominante. Ese modelo "
            "obliga a decisiones nuevas: métrica de cobro, ciclo de facturación, política de renovación y "
            "tratamiento de la baja. La renovación automática es legítima cuando se informa con claridad y "
            "permite cancelar sin fricción indebida."
        ),
        conceptos=[
            ("ingreso recurrente", "ingreso comprometido que se repite en periodos sucesivos bajo un contrato vigente"),
            ("periodo de recuperación", "tiempo necesario para recuperar el costo de adquisición con el margen del cliente"),
            ("renovación automática", "continuidad del contrato sin acción del cliente, sujeta a deber de información"),
            ("contracción", "reducción del ingreso de un cliente que permanece activo"),
        ],
        metodo=[
            "elegir la métrica de cobro que sigue al valor",
            "calcular el periodo de recuperación por segmento",
            "definir la política de renovación y de cancelación",
            "verificar el cumplimiento del deber de información",
            "seguir expansión, contracción y baja por cohorte",
        ],
        senales=[
            ("ingreso recurrente mensual", "suma del ingreso comprometido de contratos vigentes, al cierre de cada mes"),
            ("periodo de recuperación", "costo de adquisición dividido por margen de contribución mensual, por segmento"),
            ("tasa de contracción", "ingreso perdido por reducciones de plan, sobre ingreso recurrente inicial del periodo"),
        ],
        caso=(
            "Ruta Andina recupera su costo de adquisición en 14 meses y su churn mensual es 3,4 %: la vida "
            "media del cliente es menor que el periodo de recuperación."
        ),
        limite=(
            "La renovación automática exige información oportuna y un mecanismo de cancelación equivalente al "
            "de contratación. Dificultar la baja expone a sanción y destruye reputación."
        ),
        libros=["croll-yoskovitz", "mehta", "ramanujam", "fader-ltv"],
        error=("Escalar adquisición con periodo de recuperación mayor que la vida del cliente",
               "Compara periodo de recuperación con vida media antes de aumentar el gasto comercial."),
    ),
    dict(
        n="10",
        slug="freemium-y-pruebas-gratuitas",
        titulo="Freemium y pruebas gratuitas",
        tesis=(
            "Gratis no es una estrategia: es un costo con la esperanza de una conversión. Freemium funciona "
            "cuando el costo marginal de servir al usuario gratuito es bajo, cuando el plan gratuito produce "
            "un activo —datos, red, distribución— y cuando existe una razón clara para migrar. La prueba "
            "gratuita, en cambio, funciona cuando el valor se percibe rápido. Elegir mal entre ambos modelos "
            "produce bases enormes que no convierten y saturan soporte."
        ),
        conceptos=[
            ("freemium", "plan gratuito permanente con limitaciones que motivan la migración a un plan pagado"),
            ("prueba gratuita", "acceso completo por tiempo limitado para que el cliente experimente el valor"),
            ("costo marginal de servir gratis", "gasto adicional por cada usuario gratuito, incluido soporte"),
            ("gatillo de conversión", "limitación o momento que hace racional pasar al plan pagado"),
        ],
        metodo=[
            "definir el objetivo del modelo gratuito",
            "estimar el costo marginal de servir",
            "diseñar el gatillo de conversión en torno al valor",
            "medir conversión y calidad de la cohorte gratuita",
            "ajustar límites o abandonar el modelo con criterio previo",
        ],
        senales=[
            ("tasa de conversión a pago", "usuarios que pasan a plan pagado, sobre usuarios gratuitos de la cohorte, a 90 días"),
            ("costo de soporte por usuario gratuito", "horas de soporte valorizadas, dividido por usuarios gratuitos activos"),
            ("uso del gatillo de conversión", "usuarios que alcanzan el límite definido, sobre usuarios gratuitos activos"),
        ],
        caso=(
            "Ruta Andina abrió un plan gratuito sin límites de uso. Tiene 1.900 cuentas gratuitas, 2 % de "
            "conversión y el 44 % de los tickets de soporte proviene de ellas."
        ),
        limite=(
            "Un plan gratuito con costo de soporte alto puede destruir la economía del negocio incluso con "
            "buena conversión. El costo marginal debe medirse antes de escalar."
        ),
        libros=["bush-plg", "croll-yoskovitz", "ramanujam", "ellis-brown"],
        error=("Abrir plan gratuito sin límite ni gatillo",
               "Define el límite que activa la conversión y mide el costo marginal de servir antes de escalar."),
    ),
    dict(
        n="11",
        slug="descuentos-sin-destruir-valor",
        titulo="Descuentos sin destruir valor",
        tesis=(
            "Un descuento no negociado a cambio de nada enseña al mercado que el precio de lista es ficticio. "
            "La disciplina consiste en pedir siempre una contrapartida: plazo mayor, pago anticipado, volumen, "
            "caso de éxito, reducción de alcance. Nagle documenta que la política de descuentos debe estar "
            "escrita, con niveles de autoridad, porque la presión de cierre de periodo produce concesiones "
            "que se vuelven permanentes."
        ),
        conceptos=[
            ("contrapartida", "concesión del cliente que justifica la reducción de precio"),
            ("autoridad de descuento", "nivel jerárquico habilitado para aprobar cada rango de descuento"),
            ("erosión de precio", "caída sostenida del precio efectivo por acumulación de excepciones"),
            ("precedente", "efecto de un descuento sobre las expectativas de futuras negociaciones con ese cliente y su gremio"),
        ],
        metodo=[
            "medir la erosión actual del precio efectivo",
            "definir la escala de descuentos y su autoridad",
            "asociar cada nivel a una contrapartida obligatoria",
            "registrar las excepciones con su justificación",
            "revisar mensualmente la dispersión por vendedor",
        ],
        senales=[
            ("descuento promedio ponderado", "diferencia entre precio de lista y efectivo, ponderada por ingreso, mensual"),
            ("descuentos con contrapartida registrada", "descuentos con contrapartida documentada, sobre descuentos otorgados"),
            ("dispersión por vendedor", "desviación estándar del descuento otorgado entre vendedores del mismo segmento"),
        ],
        caso=(
            "En Ruta Andina el descuento promedio de cierre de mes es 22 % y en el resto del mes es 7 %. Los "
            "compradores del gremio ya saben cuándo pedir."
        ),
        limite=(
            "Una política rígida sin excepciones puede perder negocios legítimos. Lo que no puede faltar es el "
            "registro y la revisión de cada excepción."
        ),
        libros=["nagle", "simon", "fisher-ury", "zoltners"],
        error=("Otorgar descuentos sin contrapartida",
               "Exige y registra una contrapartida concreta para cada descuento aprobado."),
    ),
    dict(
        n="12",
        slug="unit-economics",
        titulo="Unit economics",
        tesis=(
            "La economía unitaria responde si cada cliente adicional deja o consume dinero. Sus componentes "
            "son el costo de adquisición completo, el margen de contribución por cliente, el periodo de "
            "recuperación y el valor de vida. El error más común no es de fórmula sino de alcance: excluir "
            "sueldos comerciales del costo de adquisición o usar margen bruto sin costo de soporte produce "
            "una economía que sólo existe en la planilla."
        ),
        conceptos=[
            ("costo de adquisición completo", "gasto total de marketing y ventas, incluidos sueldos y herramientas, por cliente nuevo"),
            ("margen de contribución por cliente", "ingreso menos costos variables de servir a ese cliente"),
            ("periodo de recuperación", "meses hasta recuperar el costo de adquisición con el margen mensual"),
            ("valor de vida", "margen acumulado esperado del cliente durante su permanencia estimada"),
        ],
        metodo=[
            "definir el alcance de cada componente por escrito",
            "calcular por segmento y no sólo agregado",
            "verificar los números contra contabilidad",
            "analizar sensibilidad ante cambios de churn y margen",
            "fijar el umbral que autoriza escalar la inversión",
        ],
        senales=[
            ("relación valor de vida a costo de adquisición", "valor de vida dividido por costo de adquisición, por segmento y cohorte"),
            ("periodo de recuperación por segmento", "meses hasta recuperar el costo de adquisición, por segmento"),
            ("margen de contribución por cohorte", "margen acumulado por cohorte de incorporación, seguido mensualmente"),
        ],
        caso=(
            "Ruta Andina reporta una relación de valor de vida a costo de adquisición de 4,2. Al incluir "
            "sueldos comerciales y horas de soporte, la relación real es 1,3."
        ),
        limite=(
            "El valor de vida es una proyección basada en supuestos de retención y margen. Sin cohortes "
            "maduras, su precisión es baja y debe presentarse como rango."
        ),
        libros=["croll-yoskovitz", "fader-ltv", "provost", "hubbard"],
        error=("Excluir sueldos comerciales del costo de adquisición",
               "Define el alcance por escrito y valida los componentes con contabilidad antes de decidir."),
    ),
    dict(
        n="13",
        slug="experimentacion-de-precios",
        titulo="Experimentación de precios",
        tesis=(
            "Experimentar con precios es la forma más directa de reducir incertidumbre y la que más "
            "consecuencias tiene sobre clientes reales. Un experimento válido requiere grupos comparables, "
            "tamaño suficiente, duración que cubra el ciclo de compra y métricas guardrail sobre churn y "
            "reclamos. Kohavi advierte sobre las trampas: detener la prueba al ver un resultado favorable o "
            "cambiar el criterio a mitad de camino invalida la conclusión."
        ),
        conceptos=[
            ("grupo de comparación", "conjunto equivalente que no recibe el cambio y permite estimar el efecto"),
            ("métrica guardrail", "indicador que no debe deteriorarse aunque mejore la métrica principal"),
            ("duración mínima", "tiempo necesario para cubrir el ciclo completo de decisión del segmento"),
            ("detención prematura", "interrupción del experimento al observar un resultado favorable transitorio"),
        ],
        metodo=[
            "definir hipótesis, métrica principal y guardarraíles",
            "calcular tamaño y duración mínima antes de iniciar",
            "asignar grupos de forma comparable y documentada",
            "no modificar criterios durante la ejecución",
            "decidir con el criterio previo y registrar el aprendizaje",
        ],
        senales=[
            ("efecto en conversión", "diferencia de conversión entre grupos, con intervalo de confianza"),
            ("efecto en ingreso por visitante", "ingreso total dividido por visitantes, comparado entre grupos"),
            ("guardarraíl de reclamos", "reclamos por precio en el grupo de prueba, comparados con el de control"),
        ],
        caso=(
            "Ruta Andina probó un alza de 15 % durante nueve días y observó mejora en ingreso. Su ciclo "
            "mediano de decisión es 34 días, por lo que la prueba midió sólo a los compradores más rápidos."
        ),
        limite=(
            "Cobrar precios distintos a clientes equivalentes por asignación aleatoria plantea un problema "
            "ético y de trato justo. Los experimentos deben tener criterio de equidad y compensación definida."
        ),
        libros=["kohavi", "nagle", "provost", "simon"],
        error=("Detener el experimento al ver un resultado favorable",
               "Fija duración y tamaño antes de iniciar y no evalúes resultados parciales como definitivos."),
    ),
    dict(
        n="14",
        slug="arquitectura-de-monetizacion",
        titulo="Arquitectura de monetización",
        tesis=(
            "Esta clase integra la parte en una arquitectura completa: métrica de cobro, estructura de "
            "planes, price fences, política de descuentos, modelo de recurrencia y economía unitaria "
            "verificada. La prueba de calidad es doble: el equipo comercial puede cotizar sin consultar y el "
            "área financiera puede proyectar ingreso con supuestos explícitos."
        ),
        conceptos=[
            ("arquitectura de monetización", "sistema completo de decisiones de precio, estructura y política"),
            ("coherencia precio-valor", "correspondencia entre lo que se cobra y el valor que percibe cada segmento"),
            ("gobierno de precios", "reglas de autoridad, revisión y excepción documentadas"),
            ("proyección de ingreso", "estimación de ingreso futuro basada en la arquitectura y sus supuestos"),
        ],
        metodo=[
            "consolidar métrica de cobro, planes y barreras",
            "verificar economía unitaria por plan",
            "documentar política de descuentos y autoridad",
            "proyectar ingreso con escenarios",
            "definir la revisión periódica de precios",
        ],
        senales=[
            ("margen por plan", "margen de contribución por plan, sobre ingreso del plan"),
            ("desviación de cotizaciones", "cotizaciones fuera de política, sobre cotizaciones emitidas"),
            ("precisión de la proyección", "diferencia entre ingreso proyectado y real, por trimestre"),
        ],
        caso=(
            "Ruta Andina debe presentar su arquitectura de monetización al directorio junto al presupuesto. "
            "Hoy hay cinco planes, precios negociados caso a caso y ninguna política escrita."
        ),
        limite=(
            "Una arquitectura de precios envejece con el producto y con el mercado. Sin una revisión anual "
            "programada, la estructura queda desalineada del valor entregado."
        ),
        libros=["nagle", "ramanujam", "simon", "croll-yoskovitz"],
        error=("Operar sin política de precios escrita",
               "Publica la política con niveles de autoridad y audita mensualmente las excepciones."),
    ),
]
