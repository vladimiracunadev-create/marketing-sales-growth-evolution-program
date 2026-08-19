# -*- coding: utf-8 -*-
"""Desarrollo escrito de la Parte 15 — E-commerce y marketplaces."""

DESARROLLO = {

    "01": [
        "El comercio digital se evalúa por pedido y no por venta total. Esa unidad de análisis revela lo que "
        "el ingreso agregado oculta: cuánto cuesta procesar, preparar y entregar cada pedido, y cuánto queda "
        "después. Un negocio que crece en ventas y pierde margen por pedido está acelerando hacia un problema "
        "que el tablero de ingresos no muestra.",

        "El modelo de cumplimiento —stock propio, despacho de terceros, cruce directo— determina la "
        "estructura de costos y el control sobre la experiencia. Cada modelo tiene un punto de equilibrio "
        "distinto y una sensibilidad distinta al volumen. Elegirlo sin ese análisis produce operaciones que "
        "funcionan a escala pequeña y se vuelven inviables al crecer, o al revés.",

        "El margen por pedido debe calcularse con todos los costos variables dentro: producto, embalaje, "
        "picking, despacho, comisión de medio de pago, devoluciones esperadas y atención posventa asociada. "
        "Esa cifra, por categoría, suele revelar que parte del catálogo se vende con margen negativo, y esa "
        "información cambia decisiones de promoción y de surtido.",

        "Crecer en volumen mejora el poder de compra y la absorción de costos fijos, y puede deteriorar el "
        "margen si el crecimiento viene de categorías de bajo margen o de pedidos pequeños. La decisión de "
        "impulsar volumen debe declarar de qué segmento se espera que venga, no tratarlo como un objetivo "
        "indiferenciado.",

        "El punto de equilibrio operativo se mueve con la estacionalidad y con los cambios de tarifa "
        "logística. Calcularlo una vez y usarlo todo el año produce decisiones basadas en supuestos "
        "obsoletos. Revisarlo trimestralmente, o cuando cambia una tarifa relevante, es parte del "
        "mantenimiento de la operación.",
    ],

    "02": [
        "El catálogo es la interfaz principal de un comercio digital y su calidad determina cuánto se "
        "encuentra y cuánto se compra. Una taxonomía construida desde la lógica interna —por proveedor, por "
        "código de sistema— obliga al cliente a aprender la organización de la empresa. Una construida desde "
        "cómo busca el cliente reduce el esfuerzo y aumenta la descubribilidad.",

        "La calidad del dato de producto es la base de todo lo demás: títulos consistentes, atributos "
        "completos, imágenes que muestran lo que importa. Un producto sin atributos no aparece en los filtros "
        "y por lo tanto no existe para quien navega filtrando. Medir la completitud de atributos por "
        "categoría es un diagnóstico rápido y revelador.",

        "La descubribilidad se mide con datos propios: qué proporción de los productos del catálogo recibió "
        "al menos una visita en el periodo, y qué proporción de las búsquedas internas terminó sin "
        "resultados. Ese segundo dato es especialmente valioso porque indica demanda expresada que la "
        "operación no está capturando.",

        "Un catálogo amplio ofrece más opciones y dificulta la elección, además de multiplicar el costo de "
        "mantener datos actualizados. Uno acotado facilita la decisión y deja demanda sin atender. La "
        "decisión debe considerar la capacidad real de mantener la calidad del dato: un catálogo grande con "
        "información deficiente rinde peor que uno pequeño y bien descrito.",

        "La información del producto obliga: características, compatibilidades, plazos y condiciones "
        "publicadas forman parte de lo ofrecido. En Chile, la normativa de consumo exige información veraz y "
        "oportuna, y los errores en fichas de producto generan responsabilidad. El control de calidad del "
        "dato no es sólo una cuestión de conversión.",
    ],

    "03": [
        "La página de producto tiene que responder todas las preguntas que impiden comprar, y esas preguntas "
        "son conocidas: qué es exactamente, si sirve para mi caso, cuánto cuesta en total, cuándo llega, qué "
        "pasa si no me sirve. Una página que responde cuatro de las cinco pierde a quien tenía la duda "
        "restante.",

        "La información suficiente varía por categoría y se determina observando las consultas de preventa. "
        "Si soporte responde repetidamente la misma pregunta sobre un producto, esa pregunta debería estar "
        "respondida en la ficha. Ese circuito —de las consultas al contenido— es barato y casi nunca está "
        "sistematizado.",

        "El precio total incluye despacho e impuestos, y mostrarlo tarde es la causa principal del abandono "
        "en el paso final. Estimar el costo de envío antes del checkout, aunque sea de forma aproximada, "
        "reduce ese abandono. Además, en operaciones con consumidores existen obligaciones de información de "
        "precio que deben verificarse en la normativa vigente.",

        "Más información responde más dudas y alarga la página, con lo que lo esencial se diluye. La "
        "estructura que funciona presenta lo decisivo arriba y organiza el detalle en secciones "
        "consultables. La decisión sobre qué va arriba debe basarse en las preguntas reales y no en la "
        "importancia que el equipo interno atribuye a cada atributo.",

        "La garantía legal existe con independencia de lo que la página declare, y la información sobre "
        "devoluciones y retracto debe corresponder a lo que la ley establece y a lo que la operación puede "
        "cumplir. Publicar condiciones más restrictivas que las legales no las hace aplicables y sí genera "
        "exposición.",
    ],

    "04": [
        "El proceso de pago es donde se pierde la mayor proporción de intención de compra ya formada. Quien "
        "llegó ahí quería comprar, de modo que cada punto de abandono es una pérdida directa y evitable. Por "
        "esa razón es el lugar del sitio con mayor retorno por unidad de esfuerzo de optimización.",

        "El costo sorpresa es la causa más documentada de abandono: un cargo por despacho o un impuesto que "
        "aparece en el último paso rompe la expectativa construida. La solución no es ocultarlo mejor sino "
        "mostrarlo antes. Un cliente que conoce el costo total desde el principio y avanza es un cliente que "
        "ya lo aceptó.",

        "La fricción de registro obligatorio es un obstáculo cuyo costo suele superar su beneficio. Ofrecer "
        "compra como invitado y proponer la creación de cuenta después de la compra conserva ambas cosas. "
        "Medir la diferencia es sencillo y en la mayoría de los casos favorece claramente la opción sin "
        "registro previo.",

        "Menos pasos aceleran y pueden generar inseguridad si la información se pide toda junta sin "
        "contexto. Más pasos permiten guiar y aumentan las oportunidades de abandono. Lo que la evidencia "
        "sostiene con claridad es que cada campo innecesario cuesta, de modo que la revisión debería empezar "
        "por eliminar campos antes que por reorganizar pasos.",

        "Las señales de seguridad importan en el momento del pago y deben ser reales: certificados vigentes, "
        "medios de pago reconocidos, información de contacto verificable. Mostrar sellos sin respaldo es "
        "contraproducente si el cliente los verifica, y la información sobre tratamiento de datos de pago "
        "debe corresponder a lo que efectivamente ocurre.",
    ],

    "05": [
        "Los medios de pago determinan qué proporción de las intenciones de compra se convierte efectivamente "
        "en ingreso. La tasa de aprobación —cuántas transacciones intentadas se completan— es una métrica "
        "operativa que rara vez se monitorea y que puede explicar pérdidas significativas sin que nadie las "
        "atribuya a esa causa.",

        "El falso rechazo es una transacción legítima bloqueada por un control antifraude demasiado "
        "estricto. Su costo es doble: se pierde la venta y se daña la relación con un cliente que no hizo "
        "nada mal. Ajustar los umbrales de control exige comparar el costo del fraude aceptado con el de las "
        "ventas rechazadas, y ese cálculo casi nunca se hace.",

        "El costo de la transacción varía por medio de pago y puede representar una porción relevante del "
        "margen en categorías de ticket bajo. Calcular el margen neto por medio de pago permite decidir "
        "cuáles promover y cuáles ofrecer con condiciones distintas, dentro de lo que la normativa "
        "permite.",

        "Ofrecer más medios de pago aumenta la conversión y multiplica la complejidad operativa, de "
        "conciliación y de soporte. Cada medio adicional exige integración, monitoreo y procedimientos de "
        "excepción. La decisión debe considerar qué proporción de la demanda quedaría sin atender sin ese "
        "medio, dato estimable con encuestas breves en el checkout.",

        "El tratamiento de datos de pago está sujeto a estándares específicos de seguridad y a obligaciones "
        "normativas. La operación no debe almacenar información sensible de tarjetas salvo bajo condiciones "
        "muy determinadas. La verificación de esos requisitos con el proveedor de pagos y con asesoría "
        "especializada es previa a cualquier implementación.",
    ],

    "06": [
        "El cumplimiento de la promesa de entrega es el momento donde la experiencia de compra se confirma o "
        "se rompe. Todo el trabajo comercial previo se juega en si el paquete llega cuando se dijo. Y a "
        "diferencia de otras variables, esta es verificable por el cliente sin ambigüedad: llegó o no llegó "
        "en la fecha.",

        "La promesa de entrega debe construirse con datos de desempeño real y no con el plazo teórico del "
        "operador logístico. Prometer el plazo óptimo produce incumplimientos sistemáticos; prometer el plazo "
        "que se cumple en la gran mayoría de los casos produce confianza. La diferencia entre ambos suele ser "
        "de uno o dos días y de mucho reclamo.",

        "El cumplimiento del plazo se mide por proporción de pedidos entregados dentro de lo prometido, "
        "segmentado por zona y por operador. El promedio nacional oculta que ciertas regiones tienen "
        "desempeño muy distinto, y esa segmentación permite ajustar la promesa por zona en lugar de degradar "
        "la promesa general.",

        "Prometer plazos cortos mejora la conversión y aumenta el incumplimiento, que se paga en reclamos, "
        "costo de atención y bajas. Prometer plazos holgados reduce la conversión y protege la experiencia. "
        "El cálculo correcto compara la ganancia en conversión con el costo total del incumplimiento, "
        "incluido el de reputación.",

        "La incidencia logística es inevitable a cierta escala y lo que se controla es la respuesta. Un "
        "procedimiento definido —cómo se detecta, en qué plazo se avisa al cliente, qué se ofrece— convierte "
        "un problema en una demostración de servicio. Sin ese procedimiento, cada incidencia se resuelve "
        "improvisando y el resultado depende de quién atienda.",
    ],

    "07": [
        "El embudo de comercio digital tiene etapas identificables y medibles: visita, vista de producto, "
        "agregado al carro, inicio de pago, compra. Analizarlo exige mirar la pérdida absoluta y no sólo la "
        "porcentual, porque la etapa con peor porcentaje no siempre es donde se pierde más gente.",

        "La segmentación de la conversión es indispensable: móvil y escritorio, tráfico nuevo y recurrente, "
        "categorías distintas tienen tasas que no son comparables. Una tasa global de conversión es un "
        "promedio de poblaciones distintas y su movimiento puede deberse por completo a un cambio de mezcla "
        "sin que nada haya mejorado ni empeorado.",

        "La hipótesis de causa debe formularse antes de intervenir. Observar una caída en el paso al carro no "
        "indica qué hacer: puede ser precio, disponibilidad, información insuficiente o un error técnico. La "
        "investigación previa —grabaciones, encuestas breves, revisión técnica— es lo que convierte la "
        "observación en un plan.",

        "Optimizar la conversión de una etapa puede empeorar la siguiente: facilitar el agregado al carro sin "
        "resolver las dudas de producto traslada el abandono al pago. Por eso la medición debe seguir la "
        "cadena completa y no celebrar mejoras locales que no llegan a la compra.",

        "Las mejoras de conversión tienen un techo determinado por la calidad del tráfico y por la oferta. "
        "Cuando el problema es que el precio no es competitivo o el producto no corresponde a lo que la gente "
        "busca, ninguna optimización de interfaz lo resuelve. Verificar ese techo antes de invertir en "
        "optimización evita meses de trabajo con retorno marginal.",
    ],

    "08": [
        "El abandono de carro no es un solo fenómeno. Mezcla a quien usa el carro como lista de deseos, a "
        "quien compara precios, a quien se topó con un costo sorpresa y a quien tuvo un problema técnico. "
        "Tratarlos con la misma acción de recuperación produce resultados mediocres y molestia en quienes "
        "nunca tuvieron intención inmediata.",

        "El obstáculo real se identifica combinando datos y consulta directa. Una encuesta breve al abandonar "
        "—una sola pregunta— entrega información que ningún análisis de comportamiento produce. La "
        "distribución de respuestas suele mostrar que la causa principal no era la que el equipo suponía.",

        "La recuperación se mide con incrementalidad y no con conversiones atribuidas: una parte de quienes "
        "vuelven habría vuelto igual. Sin un grupo de comparación que no recibe el recordatorio, la cifra "
        "reportada sobreestima el efecto, a veces de forma considerable. Ese diseño es sencillo y rara vez se "
        "implementa.",

        "Recordar más veces recupera más y aumenta la molestia y las bajas. La frecuencia debe fijarse "
        "observando no sólo la recuperación sino también las solicitudes de baja y las marcas como no "
        "deseado. Optimizar únicamente la primera métrica lleva a una cadencia que deteriora la base.",

        "El envío de recordatorios de carro implica tratar datos de una persona que no completó una compra, y "
        "requiere base de licitud y finalidad declarada. La existencia técnica del dato no autoriza su uso. "
        "Verificar el marco aplicable antes de implementar la recuperación es un paso previo obligatorio.",
    ],

    "09": [
        "Subir el ticket promedio es una palanca de margen que no requiere más tráfico, y por eso suele ser "
        "la más rentable en operaciones con costo de adquisición alto. Sus mecanismos habituales —paquetes, "
        "umbrales de envío gratuito, recomendaciones— funcionan cuando son pertinentes y molestan cuando no "
        "lo son.",

        "El paquete pertinente combina productos que efectivamente se usan juntos, y esa combinación se "
        "descubre en los datos de compra y no en la lógica de catálogo. Un paquete armado por conveniencia de "
        "inventario se percibe como intento de colocar lo que no se vende, y esa percepción daña más que el "
        "ingreso que produce.",

        "El umbral de beneficio —el monto a partir del cual se ofrece una ventaja— debe fijarse con el "
        "análisis de la distribución de tickets: un poco por encima de donde se concentra la mayoría, para "
        "que sea alcanzable. Fijarlo muy arriba no mueve a nadie; muy abajo regala margen a quien ya habría "
        "superado ese monto.",

        "Empujar el ticket puede reducir la conversión si el mecanismo introduce fricción o si el cliente "
        "percibe presión. La medición correcta observa el ingreso total por visitante y no el ticket "
        "promedio aislado, porque un ticket mayor con menos compradores puede significar menos ingreso.",

        "Estas técnicas operan sobre la decisión del cliente y tienen un límite: la recomendación debe ser "
        "genuinamente útil. Cuando el mecanismo lleva sistemáticamente a comprar más de lo necesario, el "
        "efecto aparece en devoluciones y en la relación de largo plazo, y en operaciones de consumo puede "
        "constituir una práctica cuestionable.",
    ],

    "10": [
        "La venta cruzada y la incremental son mecanismos distintos: la primera ofrece algo complementario, "
        "la segunda una versión superior. Ambas dependen de la pertinencia, y la pertinencia depende de "
        "conocer el contexto de uso. Una recomendación basada sólo en lo que otros compraron produce "
        "sugerencias obvias o absurdas.",

        "El momento de la oferta importa tanto como su contenido. Una sugerencia antes de que el cliente haya "
        "decidido el producto principal introduce ruido; después de agregarlo al carro, se percibe como "
        "complemento. Esa diferencia se puede probar y suele tener un efecto mayor que cambiar los productos "
        "recomendados.",

        "La recomendación basada en comportamiento se construye con datos propios de compra conjunta y de "
        "secuencia. Su calidad se mide por la tasa de aceptación y, sobre todo, por la tasa de devolución de "
        "lo recomendado: una recomendación aceptada y devuelta indica que fue persuasiva y no pertinente.",

        "Recomendar más aumenta las oportunidades de venta adicional y la carga cognitiva de la decisión, "
        "además de restar espacio a la información del producto principal. La cantidad óptima suele ser "
        "pequeña y se determina probando, no llenando el espacio disponible.",

        "La recomendación personalizada implica tratar datos de comportamiento y en algunos casos inferir "
        "características de la persona. Esa inferencia tiene límites: recomendaciones que revelan "
        "información sensible o que producen incomodidad dañan la relación aunque sean técnicamente "
        "correctas. La finalidad del tratamiento debe estar declarada y la personalización debe poder "
        "desactivarse.",
    ],

    "11": [
        "Vender en un marketplace es acceder a demanda existente a cambio de comisión y de pérdida de "
        "relación con el cliente. Ese intercambio puede ser excelente al inicio y problemático al escalar, "
        "porque la dependencia crece y el poder de negociación se desplaza hacia la plataforma.",

        "La comisión efectiva incluye más que el porcentaje declarado: costos de publicidad interna "
        "necesarios para tener visibilidad, promociones obligatorias, costos logísticos del programa. "
        "Calcularla completa suele mostrar una diferencia relevante respecto de la comisión nominal, y esa "
        "cifra es la que debe compararse con el costo de adquirir el mismo cliente por canal propio.",

        "La pérdida de relación es el costo estratégico: sin datos del cliente, no hay retención posible y "
        "cada venta es una transacción aislada. Medir qué proporción del ingreso proviene de canales donde "
        "no se posee la relación es un indicador de riesgo estructural que debería estar en la revisión de "
        "dirección.",

        "Aumentar la presencia en marketplaces acelera el volumen y consolida la dependencia; reducirla "
        "protege la relación y sacrifica acceso a demanda. La estrategia razonable define un techo de "
        "dependencia aceptable y trabaja activamente en canales propios mientras el marketplace financia la "
        "operación.",

        "Las reglas de la plataforma pueden cambiar unilateralmente: comisiones, visibilidad, condiciones de "
        "participación. Una operación cuya viabilidad depende de esas reglas está expuesta a decisiones "
        "ajenas. Ese riesgo debe declararse y monitorearse, y el plan debe contemplar qué se hace si las "
        "condiciones cambian de forma adversa.",
    ],

    "12": [
        "La posventa es donde se decide si habrá segunda compra, y en comercio digital la segunda compra es "
        "lo que hace viable el costo de adquisición. Una operación que trata la posventa como centro de costo "
        "está optimizando el gasto de la actividad que sostiene su economía.",

        "El esfuerzo del cliente es el mejor predictor de deterioro de la relación: cuántos contactos "
        "necesitó, cuántas veces repitió su información, cuánto esperó. Reducir ese esfuerzo tiene más efecto "
        "sobre la lealtad que superar expectativas en casos aislados, según la evidencia recogida por Matthew "
        "Dixon y su equipo.",

        "La recuperación de servicio bien ejecutada puede dejar una relación más fuerte que la ausencia de "
        "problemas. Sus condiciones son concretas: reconocer rápido, resolver sin que el cliente tenga que "
        "insistir y compensar de forma proporcional. Medir el resultado de las recuperaciones —qué proporción "
        "de esos clientes vuelve a comprar— indica si el procedimiento funciona.",

        "Una política de devoluciones amplia mejora la conversión y aumenta el costo operativo y el abuso. "
        "Una restrictiva protege el costo y frena la compra, especialmente en categorías donde el cliente no "
        "puede evaluar antes. El cálculo debe comparar el aumento de conversión con el costo total de las "
        "devoluciones adicionales.",

        "El derecho a retracto y la garantía legal existen con independencia de la política comercial y no "
        "pueden restringirse. En Chile, la normativa de consumo establece condiciones específicas para el "
        "comercio a distancia. La política publicada debe cumplirlas como piso y su redacción debe "
        "verificarse con la norma vigente.",
    ],

    "13": [
        "La economía de un comercio digital se entiende cuando se distingue entre negocio de compra única y "
        "negocio de recompra. En el primero, el costo de adquisición debe recuperarse en la primera "
        "transacción; en el segundo, puede amortizarse en el tiempo. Confundirlos lleva a invertir en "
        "adquisición como si hubiera recompra cuando no la hay.",

        "La frecuencia de recompra se mide por cohorte y no en agregado: qué proporción de quienes compraron "
        "en un mes vuelve a comprar en los siguientes seis. Ese análisis, hecho una vez, define la estrategia "
        "completa de inversión. En muchas operaciones revela que la recompra es mucho menor de lo que el "
        "ingreso total sugería.",

        "La contribución por pedido debe calcularse antes de decidir cualquier inversión en adquisición. Si "
        "la contribución media es menor que el costo de conseguir un pedido, crecer destruye valor. Esa "
        "cuenta es simple y su ausencia explica una parte importante de los fracasos en comercio digital.",

        "Invertir en adquisición produce crecimiento visible; invertir en recompra produce crecimiento más "
        "lento y más rentable. La presión organizativa favorece lo primero porque se ve. Cambiar esa "
        "prioridad requiere que el indicador de gestión incluya el valor del cliente y no sólo el volumen de "
        "pedidos nuevos.",

        "El valor del cliente en comercio digital es una proyección basada en frecuencia y margen "
        "observados, y su principal fragilidad es suponer que la conducta pasada se mantiene. Cambios de "
        "precio, de surtido o de competencia alteran esa proyección. Declarar el supuesto y su sensibilidad "
        "es la única forma honesta de usarla para decidir.",
    ],

    "14": [
        "Modelar la rentabilidad de una tienda consiste en construir la cadena completa desde el tráfico "
        "hasta la contribución, con cada supuesto explícito y verificable. El valor del ejercicio no está en "
        "el número final sino en descubrir qué variable domina el resultado, porque ahí es donde conviene "
        "concentrar el esfuerzo.",

        "El análisis de sensibilidad se hace moviendo cada supuesto en un rango razonable y observando el "
        "efecto sobre el resultado. Casi siempre una o dos variables explican la mayor parte de la variación, "
        "y esas son las que hay que medir mejor. Las demás pueden estimarse con menos precisión sin afectar "
        "la decisión.",

        "La variable crítica en comercio digital suele ser la tasa de recompra o el margen por pedido, no el "
        "tráfico, que es donde se concentra la atención. Descubrirlo cambia la asignación de esfuerzo: "
        "invertir en mejorar la variable crítica rinde más que optimizar las demás, aunque sea menos "
        "visible.",

        "Un modelo detallado captura más matices y se vuelve difícil de auditar y de mantener; uno simple se "
        "revisa y omite interacciones. Para decidir, un modelo simple con supuestos declarados suele ser "
        "superior a uno complejo cuyos supuestos están enterrados en fórmulas que nadie revisa.",

        "El escenario de estrés —qué pasa si el costo de adquisición sube, si la conversión baja, si un "
        "canal se encarece— debe formar parte del modelo y no ser un ejercicio opcional. Su función es "
        "identificar en qué punto la operación deja de ser viable y con cuánta anticipación se podría "
        "detectar, que es una información de gestión y no un pesimismo.",
    ],
}
