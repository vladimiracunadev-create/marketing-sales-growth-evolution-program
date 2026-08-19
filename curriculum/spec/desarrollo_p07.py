# -*- coding: utf-8 -*-
"""Desarrollo escrito de la Parte 07 — Pricing y monetización."""

DESARROLLO = {

    "01": [
        "El precio es la única decisión comercial que actúa directamente sobre el margen sin pasar por el "
        "costo. Un punto porcentual de mejora en el precio realizado suele tener más efecto sobre la utilidad "
        "que un punto de volumen o de costo, porque llega íntegro al resultado. Esa asimetría explica por qué "
        "Hermann Simon insiste en que el precio es la palanca más rápida y, sin embargo, la que menos "
        "atención directiva recibe.",

        "Una política de precios es distinta de una lista de precios: la lista dice cuánto cuesta cada cosa, "
        "la política dice quién puede modificarla, bajo qué condiciones y con qué contrapartida. Sin política, "
        "cada negociación empieza de cero y el precio realizado depende del carácter del vendedor. Con "
        "política, la excepción existe pero deja registro y tiene dueño.",

        "La métrica de cobro —por usuario, por transacción, por volumen, por resultado— determina cómo crece "
        "el ingreso con el uso del cliente y suele decidirse por conveniencia técnica. La regla útil es "
        "elegir la unidad que más se parece al valor que el cliente percibe: si el beneficio crece con los "
        "envíos gestionados, cobrar por usuario desconecta el precio del valor y produce fricción en cada "
        "renovación.",

        "Subir precio mejora el margen unitario y expone volumen; bajarlo compra participación y compromete "
        "la caja que financia el servicio. Lo que casi nunca se calcula es el punto de indiferencia: cuánto "
        "volumen se puede perder con un alza determinada antes de quedar igual. Ese cálculo es aritmética "
        "simple y cambia por completo la percepción del riesgo de subir.",

        "Las decisiones de precio operan dentro de un marco legal que no es negociable: prohibición de "
        "acuerdos con competidores, obligación de informar el precio total y restricciones sobre publicidad "
        "de descuentos. En Chile intervienen la Ley 19.496 y la normativa de libre competencia. Este material "
        "entrega criterio económico; la verificación normativa antes de aplicar es obligatoria.",
    ],

    "02": [
        "El costo más un margen es el método más usado y el menos defendible. Su atractivo es la aparente "
        "objetividad: parte de un número que la empresa conoce. Su problema es que el costo no dice nada "
        "sobre lo que el cliente está dispuesto a pagar, de modo que el método produce precios demasiado "
        "altos donde el valor es bajo y demasiado bajos donde el valor es alto, con la misma seguridad en "
        "ambos casos.",

        "El costo variable unitario y el costo de servir completo se confunden con frecuencia. El primero "
        "incluye lo que se consume por unidad vendida; el segundo agrega soporte, implementación, gestión de "
        "cuenta y todo lo que ese cliente demanda. Un cliente puede tener margen bruto excelente y margen "
        "real negativo, y sólo el segundo cálculo lo revela.",

        "El costo tiene un uso legítimo y preciso: es el piso, no el método. Sirve para saber por debajo de "
        "qué precio la operación pierde dinero y para decidir qué negocios rechazar. La ficha debe registrar "
        "qué costos están incluidos, cuáles son escalonados y a partir de qué volumen aparece un salto, "
        "porque ese salto es el que rompe los cálculos lineales.",

        "La circularidad costo-volumen es la trampa técnica del método: el costo unitario depende del volumen "
        "y el volumen depende del precio, que se calcula sobre el costo unitario. En productos con altos "
        "costos fijos, esa circularidad puede llevar a una espiral donde la caída de volumen sube el costo "
        "unitario y justifica subir el precio, que reduce más el volumen.",

        "El método por costo es razonable en contextos específicos: contratos regulados que exigen "
        "justificación de costos, licitaciones con estructura definida, servicios estandarizados en mercados "
        "muy competidos. Fuera de esos casos, usarlo como método principal deja valor sobre la mesa de forma "
        "sistemática y silenciosa.",
    ],

    "03": [
        "Fijar precio mirando al competidor supone que el competidor sabe lo que hace y que su oferta es "
        "comparable con la tuya. Ambas premisas suelen ser falsas. El uso legítimo de la referencia "
        "competitiva no es copiarla sino conocerla: saber contra qué número se te compara para poder "
        "argumentar la diferencia.",

        "La comparabilidad real exige homologar antes de comparar: mismo alcance, mismo plazo, mismos "
        "servicios incluidos, mismo tratamiento de la implementación. Un precio aparentemente menor puede ser "
        "mayor una vez incorporados los costos que el competidor cobra aparte. Construir esa tabla de "
        "homologación es trabajo comercial de primer orden y casi nadie lo hace por escrito.",

        "El valor diferencial cuantificado es la respuesta a una referencia competitiva más baja: cuánto vale, "
        "en la moneda del cliente, aquello en que tu oferta supera a la alternativa. Se calcula con datos del "
        "propio cliente y se expresa por periodo. Sin ese cálculo, la defensa del precio se reduce a "
        "afirmaciones de calidad que el comprador no puede verificar.",

        "Seguir al competidor en una bajada protege participación y arrastra a toda la categoría a un margen "
        "menor del que se recupera con dificultad. No seguirlo protege el margen y puede costar volumen en el "
        "corto plazo. La decisión debe considerar si el competidor puede sostener ese precio: una bajada que "
        "él no puede mantener se corrige sola si no se le acompaña.",

        "El seguimiento de precios de competidores debe hacerse con información pública y por medios "
        "legítimos, y nunca coordinarse con ellos. Cualquier intercambio de información de precios entre "
        "competidores puede constituir una infracción a la libre competencia con consecuencias graves. La "
        "regla del programa es que toda referencia competitiva debe provenir de fuente pública o del propio "
        "cliente.",
    ],

    "04": [
        "El precio basado en valor parte de una pregunta distinta: cuánto vale para este cliente la "
        "diferencia entre tu oferta y su mejor alternativa. El cálculo tiene dos términos —el precio de la "
        "alternativa de referencia y el valor diferencial— y ambos deben estimarse con datos del cliente. Es "
        "más trabajo que los otros métodos y es el único que conecta precio con beneficio real.",

        "El valor de referencia no siempre es un competidor: puede ser el costo del proceso manual actual o "
        "el costo de no hacer nada. Identificarlo correctamente es la mitad del ejercicio, porque determina "
        "el punto de partida del cálculo. Un error frecuente es usar como referencia al competidor más caro "
        "porque conviene, cuando el cliente en realidad compara contra su planilla.",

        "La regla de captura define qué proporción del valor diferencial se traslada al precio. Capturar todo "
        "elimina el incentivo del cliente para cambiar; capturar poco deja margen sobre la mesa. La "
        "proporción razonable depende de la evidencia disponible: cuanto más incierta sea la estimación del "
        "valor, mayor debe ser el excedente que se deja al cliente para compensar su riesgo.",

        "Un precio basado en valor puede ser muy distinto entre clientes, lo que mejora la captura y "
        "complica la administración y la percepción de justicia. Cuando los clientes se comunican entre sí "
        "—habitual en gremios y en sector público— las diferencias no justificadas por criterios "
        "verificables generan conflicto. La solución es que la diferencia se explique por una barrera "
        "legítima y declarada.",

        "El método exige poder estimar el valor con alguna precisión y hay servicios donde eso no es posible: "
        "cuando el resultado depende mayoritariamente de la ejecución del cliente o cuando el beneficio es "
        "difuso. En esos casos, forzar una cuantificación produce cifras que no resisten la primera pregunta "
        "y dañan la credibilidad de toda la propuesta.",
    ],

    "05": [
        "La disposición a pagar no es un número por cliente sino una distribución en el mercado, y esa "
        "distribución es lo que justifica tener más de un plan. Pensarla como valor único lleva a buscar «el "
        "precio correcto», que no existe, en lugar de diseñar una estructura que capture distintos tramos de "
        "la distribución.",

        "El sesgo de declaración es el problema central de cualquier medición directa: la gente subestima lo "
        "que pagaría cuando cree que eso influirá en el precio, y sobreestima cuando quiere ser amable. Por "
        "eso las preguntas directas sobre precio se usan como orientación gruesa y nunca como base de "
        "decisión sin contrastar con conducta.",

        "El análisis de compensación —pedir que elijan entre combinaciones de atributos y precio— evita el "
        "sesgo de la pregunta directa porque obliga a renunciar a algo. Requiere diseño cuidadoso y una "
        "muestra suficiente, y entrega la valoración relativa de los atributos, que suele ser más útil que "
        "el nivel absoluto de precio.",

        "Investigar la disposición a pagar con rigor cuesta tiempo y dinero, y en mercados B2B pequeños puede "
        "ser inviable por tamaño de muestra. La alternativa practicable es la conversación estructurada con "
        "clientes reales sobre presupuestos y comparaciones, aceptando que entrega orientación y no "
        "precisión. Lo indefendible es no hacer ninguna de las dos y fijar precio por intuición.",

        "La validación definitiva es la decisión de compra con precio real. Toda medición previa es una "
        "estimación cuya utilidad está en reducir el rango de prueba, no en reemplazarla. Un plan de pricing "
        "que no contempla cómo se validará en el mercado está confiando en la investigación más allá de lo "
        "que la investigación puede sostener.",
    ],

    "06": [
        "La elasticidad describe cuánto cambia la cantidad demandada ante un cambio de precio, y en la "
        "práctica comercial casi nunca se conoce con precisión. Lo que sí puede conocerse son los factores "
        "que la aumentan o la reducen: existencia de alternativas conocidas, peso del gasto en el presupuesto "
        "del cliente, facilidad de comparación, urgencia y quién paga.",

        "La sensibilidad varía entre segmentos del mismo mercado, y esa variación es la base de toda "
        "segmentación de precios. Un cliente que compara tres cotizaciones es más sensible que uno que "
        "necesita resolver hoy. Tratarlos con el mismo precio y la misma política de descuento significa "
        "regalar margen al segundo y perder al primero.",

        "Estimar la elasticidad con datos históricos exige que haya habido variación de precio y que se "
        "puedan aislar otros factores, condiciones que rara vez se cumplen. Cuando se intenta igual, el "
        "resultado suele confundir efecto de precio con estacionalidad o con cambios de mezcla. Declarar esa "
        "limitación es más honesto que presentar un coeficiente con dos decimales.",

        "Una prueba de precio entrega evidencia limpia y expone a que clientes con precios distintos se "
        "enteren. En entornos B2B ese riesgo es alto y el daño de confianza puede superar el aprendizaje. La "
        "alternativa habitual es probar con clientes nuevos, con planes nuevos o en mercados geográficamente "
        "separados, declarando el criterio de separación.",

        "Toda prueba de precio debe respetar la igualdad de trato que la normativa exige y evitar "
        "discriminaciones sin justificación objetiva. Además, un cambio de precio a clientes vigentes tiene "
        "reglas contractuales propias. Antes de diseñar cualquier experimento de precio corresponde verificar "
        "el marco aplicable y las condiciones pactadas.",
    ],

    "07": [
        "Las técnicas de investigación de precio tienen un uso preciso: acotar el rango antes de probar, no "
        "determinar el precio. La técnica de Van Westendorp, por ejemplo, entrega un rango de aceptabilidad a "
        "partir de cuatro preguntas sobre percepción de caro y barato. Es simple de aplicar y su resultado "
        "depende por completo de que los encuestados conozcan la categoría.",

        "El rango aceptable y el punto óptimo que estas técnicas producen son artefactos del método, no "
        "propiedades del mercado. Presentarlos como «el precio que el mercado acepta» es sobreinterpretar. Su "
        "uso correcto es descartar niveles claramente fuera de rango y orientar el diseño de la prueba real.",

        "La medición exige que el encuestado tenga contexto suficiente: qué recibe, con qué alcance, "
        "comparado con qué. Preguntar por el precio de algo que la persona no comprende produce respuestas "
        "aleatorias con apariencia de dato. La ficha registra qué descripción se mostró, porque cambiar la "
        "descripción cambia el resultado más que cualquier ajuste metodológico.",

        "Estas técnicas son baratas y por eso se aplican donde no corresponde. En mercados B2B con universos "
        "pequeños y decisión por comité, la pregunta de precio a una persona no representa a la organización. "
        "El costo de aplicar la técnica es bajo; el costo de decidir con su resultado en un contexto "
        "inadecuado, alto.",

        "Ninguna técnica de investigación reemplaza la validación con compras reales. Su papel es reducir el "
        "espacio de búsqueda y hacer más eficiente la prueba posterior. Un plan de precios que termina en la "
        "investigación y no contempla validación de mercado está tomando una decisión de ingresos sobre "
        "declaraciones.",
    ],

    "08": [
        "Una barrera de precio es la condición que permite cobrar distinto a segmentos distintos sin que "
        "quien paga más pueda acceder al precio menor. Sin barrera, toda segmentación de precios se derrumba "
        "por arbitraje. Las barreras válidas son verificables y objetivas: volumen, plazo de contrato, canal, "
        "alcance funcional, tipo de cliente.",

        "El versionado es la barrera más común en productos digitales: se ofrecen configuraciones distintas "
        "con precios distintos. Su diseño falla cuando la diferencia entre versiones no corresponde a algo "
        "que el segmento de menor disposición no necesita. Si la única diferencia es artificial, el cliente "
        "lo percibe y la barrera se convierte en un motivo de molestia.",

        "El arbitraje entre segmentos se detecta observando migraciones inesperadas: clientes que cambian de "
        "categoría, que se dividen en unidades menores o que compran a través de un canal que no les "
        "corresponde. Registrar esas anomalías por trimestre permite detectar barreras que están fallando "
        "antes de que el efecto sea grande.",

        "Barreras más estrictas capturan mejor y aumentan la fricción y la percepción de arbitrariedad. "
        "Barreras laxas son cómodas y filtran mal. El criterio de diseño es la legitimidad: una barrera que "
        "el cliente entiende y considera razonable —pagar menos por comprometerse a más plazo— se sostiene; "
        "una que no puede explicarse genera conflicto cada vez que se aplica.",

        "La segmentación de precios opera dentro de límites legales que prohíben la discriminación "
        "arbitraria, especialmente en relaciones de consumo. Una barrera debe responder a un criterio "
        "objetivo y aplicarse de forma consistente. Antes de implementar una estructura segmentada "
        "corresponde revisar su compatibilidad con la normativa vigente.",
    ],

    "09": [
        "El ingreso recurrente cambia la economía del negocio: el valor de un cliente ya no está en la venta "
        "sino en la permanencia, y eso justifica invertir en adquisición más de lo que el primer pago "
        "recupera. La condición para que esa lógica funcione es que la permanencia sea real y medida, no "
        "supuesta por el modelo de contrato.",

        "El periodo de recuperación es el indicador que gobierna la velocidad de crecimiento sostenible: "
        "cuántos meses tarda el margen del cliente en cubrir lo que costó adquirirlo. Un periodo mayor que la "
        "permanencia media significa que cada cliente nuevo destruye valor, y ese diagnóstico —como en el caso "
        "de Ruta Andina— puede convivir con un crecimiento aparente de ingresos.",

        "La contracción es la reducción de ingreso de clientes que permanecen, y suele medirse mal o no "
        "medirse. Un negocio puede tener baja tasa de bajas y perder ingreso porque los clientes reducen su "
        "consumo. Por eso la medición correcta separa churn de clientes, churn de ingreso y contracción, y "
        "reporta las tres.",

        "La renovación automática mejora la retención declarada y traslada el costo de la decisión al "
        "cliente, que puede sentirse atrapado. En Chile, además, las condiciones de renovación automática "
        "están reguladas en relaciones de consumo. La decisión de usarla exige verificar el marco aplicable y "
        "diseñar un aviso previo genuino, no un cumplimiento formal.",

        "El modelo recurrente supone que el cliente obtiene valor de forma continua. Cuando el valor es "
        "episódico —se usa dos veces al año— el modelo genera resentimiento y bajas. En esos casos, un "
        "esquema por uso o por proyecto se alinea mejor con la percepción, aunque produzca ingresos menos "
        "predecibles.",
    ],

    "10": [
        "Freemium y prueba gratuita resuelven problemas distintos. La prueba acota en el tiempo y sirve "
        "cuando el valor se percibe rápido; el plan gratuito permanente sirve cuando el valor requiere "
        "acumulación o cuando el usuario gratuito aporta algo —datos, red, contenido—. Elegir mal produce "
        "costos de servir sin conversión o pruebas que terminan antes de que el cliente entienda el "
        "producto.",

        "El costo marginal de servir gratis es la variable que decide la viabilidad y con frecuencia se "
        "supone cero. En software puede ser bajo pero no nulo: soporte, infraestructura y atención comercial "
        "consumen recursos reales. Calcularlo por usuario gratuito y proyectarlo al volumen esperado es un "
        "ejercicio obligatorio antes de lanzar un plan libre.",

        "El gatillo de conversión debe construirse alrededor del valor y no del tiempo. Un límite que se "
        "alcanza cuando el usuario ya obtuvo resultado convierte; uno que expira antes, frustra. La ficha de "
        "medición debe registrar qué proporción de usuarios gratuitos alcanza el momento de valor y cuál de "
        "esos convierte, porque son dos problemas distintos con soluciones distintas.",

        "Un plan gratuito generoso acelera la adopción y puede eliminar la razón para pagar. Uno restrictivo "
        "protege la conversión y reduce el alcance. El ajuste correcto se determina observando qué usan los "
        "que convierten y qué usan los que no, y ubicando el límite en el punto donde esas conductas se "
        "separan.",

        "El modelo gratuito supone que existe un camino de autoservicio hacia el valor. Cuando el producto "
        "requiere implementación, configuración o cambio de proceso, el usuario gratuito nunca llegará al "
        "momento de valor y el plan libre sólo generará costo. Verificar esa condición antes de lanzarlo "
        "ahorra un año de conclusiones equivocadas.",
    ],

    "11": [
        "Un descuento sin contrapartida es una transferencia de margen sin retorno. La disciplina básica del "
        "descuento es que siempre se intercambia por algo verificable: plazo mayor, pago anticipado, volumen "
        "comprometido, caso de referencia autorizado, reducción de alcance. Cuando no hay contrapartida, lo "
        "que se está pagando es la incomodidad de sostener el precio.",

        "La autoridad de descuento debe estar escrita y escalonada, y su ausencia se paga en dispersión: cada "
        "vendedor concede lo que su carácter y su presión de cuota permiten. Una política clara —hasta cierto "
        "porcentaje decide el vendedor, más allá decide la jefatura— no elimina el descuento pero deja "
        "registro y hace visible el patrón.",

        "La erosión de precio se mide con el precio realizado promedio y su evolución, no con la lista. La "
        "cascada —de precio de lista a precio de bolsillo— muestra dónde se pierde: descuento comercial, "
        "condiciones de pago, servicios regalados, penalizaciones no cobradas. Construirla una vez suele "
        "revelar varios puntos porcentuales de margen que nadie estaba mirando.",

        "Un descuento cierra el negocio de hoy y fija el precio de referencia de la próxima renovación. Ese "
        "precedente es el costo oculto: el cliente que obtuvo veinte por ciento esperará al menos lo mismo la "
        "vez siguiente. Antes de conceder conviene declarar explícitamente si es por única vez y bajo qué "
        "condición, y dejarlo por escrito en la propuesta.",

        "La política de descuentos debe aplicarse de forma consistente para no incurrir en discriminación "
        "arbitraria, y las condiciones especiales deben quedar documentadas. En operaciones con sector "
        "público, además, las reglas del procedimiento limitan qué puede ofrecerse y cuándo. La verificación "
        "del marco aplicable precede a cualquier concesión.",
    ],

    "12": [
        "La economía unitaria responde una pregunta simple y decisiva: ¿cada cliente adicional aporta o "
        "consume valor? Si el margen de contribución por cliente supera el costo de adquirirlo dentro de su "
        "permanencia esperada, crecer tiene sentido; si no, crecer acelera la pérdida. Muchos negocios "
        "descubren esa relación demasiado tarde porque miran ingreso total y no unidad.",

        "El costo de adquisición completo incluye lo que casi siempre se omite: sueldos del equipo comercial "
        "y de marketing, herramientas, comisiones y el costo de las oportunidades perdidas en el proceso. Un "
        "cálculo que sólo considera el gasto en medios subestima el costo real por un factor considerable y "
        "produce decisiones de inversión equivocadas.",

        "El margen de contribución por cliente exige imputar el costo de servir, que varía mucho entre "
        "cuentas. La ficha debe registrar qué costos se imputaron, cómo se distribuyeron los compartidos y "
        "qué periodo cubre. Dos cálculos con supuestos distintos no son comparables, y la mayor parte de las "
        "discusiones sobre unit economics son en realidad discusiones sobre supuestos no declarados.",

        "Mejorar la economía unitaria puede lograrse subiendo precio, bajando costo de servir o alargando la "
        "permanencia. Las tres palancas tienen efectos cruzados: subir precio puede acortar la permanencia; "
        "bajar costo de servir puede deteriorar el resultado del cliente. Modelar el efecto conjunto, aunque "
        "sea de forma gruesa, evita optimizar una variable destruyendo otra.",

        "La economía unitaria es una proyección basada en permanencia esperada, y esa esperanza es el "
        "supuesto más frágil. En negocios jóvenes no hay historia suficiente para estimarla, y usar el "
        "supuesto optimista es la forma habitual de justificar inversión. La práctica honesta declara el "
        "supuesto, muestra la sensibilidad y define qué señal obligaría a revisarlo.",
    ],

    "13": [
        "Experimentar con precios es distinto de experimentar con una página: el precio afecta a clientes "
        "reales, deja precedentes y puede tener implicancias contractuales. Por eso el diseño exige más "
        "cuidado que un test de conversión habitual, y por eso muchas empresas terminan cambiando precio sin "
        "medir, que es el peor de los mundos.",

        "El grupo de comparación es lo que convierte un cambio en un experimento. Sin él, la variación "
        "observada puede deberse a estacionalidad, a una campaña o al mercado. En pricing, construir el grupo "
        "de comparación suele requerir separar por cohorte de ingreso o por mercado geográfico, y esa "
        "decisión debe documentarse antes de empezar.",

        "Las métricas guardarraíl son obligatorias en pruebas de precio: además del ingreso, hay que vigilar "
        "tasa de conversión, mezcla de planes, volumen de reclamos y bajas. Un alza que mejora el ingreso del "
        "mes y dispara las bajas del trimestre siguiente aparece como éxito si sólo se mira la primera "
        "métrica. La ventana de evaluación debe cubrir el efecto rezagado.",

        "Detener un experimento cuando el resultado es favorable es el error más frecuente y el más "
        "costoso, porque garantiza quedarse con los falsos positivos. La disciplina exige fijar la duración y "
        "el tamaño antes de empezar y respetarlos. En pricing esa disciplina cuesta más porque la presión "
        "por consolidar un buen número es alta.",

        "Un resultado de experimento de precio vale para el segmento, el momento y el contexto competitivo en "
        "que se obtuvo. Extenderlo a toda la base o a otro mercado es una nueva hipótesis. Además, si el "
        "experimento implicó condiciones distintas para clientes comparables, corresponde revisar su "
        "legitimidad antes de repetirlo a escala.",
    ],

    "14": [
        "Una arquitectura de monetización integra las decisiones que las clases anteriores tomaron por "
        "separado: qué se cobra, con qué unidad, en qué niveles, con qué barreras y con qué política de "
        "excepción. Su valor está en la coherencia: cada pieza debe ser explicable en relación con el valor "
        "que el cliente recibe, y las que no lo son suelen ser herencias que nadie revisó.",

        "La coherencia precio-valor se audita con una revisión concreta: para cada nivel de la estructura, "
        "verificar que el salto de precio corresponde a un salto de valor perceptible. Cuando un plan cuesta "
        "el doble y aporta una funcionalidad marginal, el cliente lo detecta y la estructura pierde "
        "credibilidad completa, no sólo en ese nivel.",

        "El gobierno de precios define quién puede cambiar qué, con qué proceso y con qué registro. Sin "
        "gobierno, la estructura diseñada se degrada por acumulación de excepciones hasta que nadie sabe cuál "
        "es el precio real. Una revisión anual del precio realizado por segmento, comparado con la lista, es "
        "el control mínimo.",

        "Una arquitectura simple se comunica y se administra bien y captura menos valor; una compleja captura "
        "mejor y aumenta el costo de venta, de facturación y de soporte. El límite práctico es la capacidad "
        "del equipo comercial de explicarla sin material de apoyo: si no puede, la complejidad se pagará en "
        "errores y en descuentos para compensar la confusión.",

        "La proyección de ingreso que se construye sobre la arquitectura hereda todos sus supuestos: mezcla "
        "de planes, tasa de conversión entre niveles, permanencia. Presentarla como pronóstico sin declarar "
        "esos supuestos convierte un ejercicio de diseño en una promesa financiera. La versión honesta "
        "acompaña la proyección con su sensibilidad a los dos supuestos más frágiles.",
    ],
}
