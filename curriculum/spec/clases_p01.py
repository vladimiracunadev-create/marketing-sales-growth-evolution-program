# -*- coding: utf-8 -*-
"""Parte 01 — Marketing y ventas: fundamentos del sistema comercial."""

CLASES = [
    dict(
        n="01",
        slug="marketing-ventas-y-crecimiento-como-sistema",
        titulo="Marketing, ventas y crecimiento como sistema",
        tesis=(
            "Marketing, ventas y éxito de cliente no son tres departamentos que se pasan trabajo: son tres "
            "momentos de un mismo sistema que convierte atención en ingreso y el ingreso en relación. Cuando "
            "se los gestiona por separado, cada área optimiza su métrica local —tráfico, cierres, tickets "
            "resueltos— y el sistema completo pierde margen. Drucker lo planteó antes de que existiera el "
            "vocabulario moderno: el propósito de una empresa es crear un cliente, y crear un cliente exige "
            "coordinar promesa, entrega y evidencia. El diagnóstico correcto empieza preguntando en qué "
            "eslabón se pierde valor y no qué área trabaja menos."
        ),
        conceptos=[
            ("sistema comercial", "conjunto de actividades, datos y decisiones que convierten a un desconocido en un cliente rentable y recurrente"),
            ("eslabón limitante", "la etapa cuya capacidad o calidad determina el resultado total, aunque las demás mejoren"),
            ("métrica local", "indicador que mide el desempeño de una etapa sin considerar su efecto sobre las siguientes"),
            ("calidad del ingreso", "combinación de margen, permanencia y costo de servir que distingue un peso vendido de otro"),
        ],
        metodo=[
            "dibujar el sistema completo de atención a renovación",
            "medir volumen, conversión y tiempo en cada eslabón",
            "identificar el eslabón limitante con datos y no con opinión",
            "estimar el efecto de mejorar ese eslabón frente a mejorar otro",
            "definir la intervención, su costo y la señal que la validaría",
        ],
        senales=[
            ("conversión etapa a etapa", "unidades que pasan de la etapa N a la N+1 dividido por las que entraron a N, en ventana de 30 días y por cohorte de origen"),
            ("ingreso neto retenido", "ingreso recurrente del mismo grupo de clientes 12 meses después, incluyendo bajas, contracciones y expansiones, dividido por el ingreso inicial"),
            ("costo por cliente ganado", "gasto total de marketing y ventas del periodo, incluidos sueldos, dividido por clientes nuevos del mismo periodo"),
        ],
        caso=(
            "El directorio de Ruta Andina exige «más marketing» porque las ventas se estancaron. Los datos "
            "muestran conversión de demo a cierre de 31 % —sana para el rubro— y una caída del 38 % de las "
            "cuentas nuevas antes del día 90. Cada peso adicional en adquisición está llenando un estanque roto."
        ),
        limite=(
            "El pensamiento sistémico no reemplaza la ejecución: identificar el eslabón limitante sin capacidad "
            "de intervenir en él sólo produce informes. Si el cuello está en producto u operaciones, la decisión "
            "correcta puede ser comercial únicamente en su cronograma."
        ),
        libros=["drucker", "kotler", "diorio", "croll-yoskovitz"],
        error=("Pedir más leads cuando el problema está en la retención",
               "Calcula el efecto de +20 % de leads frente a −20 % de churn sobre el ingreso a 12 meses antes de aprobar presupuesto."),
    ),
    dict(
        n="02",
        slug="necesidades-deseos-demanda-y-valor",
        titulo="Necesidades, deseos, demanda y valor",
        tesis=(
            "Una necesidad es un estado de carencia; un deseo es la forma culturalmente moldeada que toma esa "
            "carencia; la demanda es un deseo respaldado por capacidad y disposición de pago. Confundirlos "
            "produce dos errores caros y simétricos: construir para una necesidad real que nadie pagará, o "
            "estimular un deseo que la empresa no puede satisfacer. El valor, a su vez, no es una propiedad "
            "del producto sino un juicio comparativo del cliente entre beneficios percibidos y costos totales "
            "—dinero, tiempo, riesgo y esfuerzo de cambio— frente a la alternativa de no hacer nada."
        ),
        conceptos=[
            ("necesidad", "estado de carencia funcional, social o emocional que existe con independencia de la oferta"),
            ("demanda", "deseo específico respaldado por presupuesto asignado y autoridad para gastarlo"),
            ("valor percibido", "juicio del cliente sobre beneficio menos costo total, siempre relativo a una alternativa concreta"),
            ("costo de cambio", "esfuerzo, riesgo y pérdida temporal que asume el cliente al abandonar su solución actual"),
        ],
        metodo=[
            "describir la carencia en las palabras del cliente y no en las del producto",
            "identificar la alternativa real contra la que se compara, incluido no hacer nada",
            "verificar si existe presupuesto y quién lo controla",
            "cuantificar beneficio y costo total de cambio",
            "declarar qué evidencia convertiría el deseo en demanda medible",
        ],
        senales=[
            ("tasa de conversión de interés a presupuesto", "oportunidades con presupuesto confirmado dividido por oportunidades que declararon interés, por trimestre"),
            ("costo de cambio declarado", "horas de migración y capacitación estimadas por el cliente, recogidas en discovery y contrastadas con la implementación real"),
            ("razón de pérdida por inacción", "negocios perdidos ante «no hacer nada» dividido por total de negocios perdidos"),
        ],
        caso=(
            "Ruta Andina detecta que 61 % de sus oportunidades perdidas no se van a la competencia: se quedan "
            "con planillas y WhatsApp. El equipo comercial redactó una comparativa contra el competidor y "
            "ninguna contra el statu quo, que es el rival que realmente gana."
        ),
        limite=(
            "El valor percibido no es manipulable de forma indefinida: se puede comunicar mejor un beneficio real, "
            "pero inflar la percepción por encima de la experiencia produce churn y reclamos, y en Chile puede "
            "constituir publicidad engañosa."
        ),
        libros=["kotler", "christensen", "ariely", "nagle"],
        error=("Tratar «interés» como demanda en el forecast",
               "Exige presupuesto identificado y decisor nombrado antes de mover una oportunidad a etapa comprometida."),
    ),
    dict(
        n="03",
        slug="mercados-categorias-y-competencia",
        titulo="Mercados, categorías y competencia",
        tesis=(
            "Un mercado no es un dato objetivo que se descarga de un informe: es una definición que la empresa "
            "elige y que determina con quién se la compara. Definir la categoría como «software de "
            "agendamiento» convoca a competidores de software; definirla como «reducir inasistencias» convoca "
            "a recordatorios por WhatsApp, a la secretaria y a la sobreventa de horas. Levitt mostró que las "
            "industrias declinan cuando se definen por el producto que fabrican y no por el trabajo que "
            "resuelven. La elección de categoría condiciona precio de referencia, criterios de compra y hasta "
            "el presupuesto desde el cual se paga."
        ),
        conceptos=[
            ("categoría", "conjunto de alternativas que el cliente considera comparables para resolver el mismo trabajo"),
            ("competencia directa", "oferta que el cliente evalúa en el mismo proceso de compra y con los mismos criterios"),
            ("competencia funcional", "solución distinta en forma que sustituye el mismo resultado, incluido el proceso manual"),
            ("precio de referencia", "monto que el cliente considera normal para esa categoría y contra el cual juzga cualquier propuesta"),
        ],
        metodo=[
            "listar las alternativas que el cliente nombró espontáneamente en discovery",
            "clasificar cada alternativa como directa, funcional o statu quo",
            "identificar de qué presupuesto sale el dinero en cada caso",
            "estimar el precio de referencia asociado a esa categoría",
            "elegir la definición de categoría que se quiere ocupar y justificar el costo de esa elección",
        ],
        senales=[
            ("participación en la consideración", "oportunidades donde la empresa fue evaluada dividido por oportunidades detectadas en el segmento, por trimestre"),
            ("mezcla de competidores nombrados", "frecuencia de cada alternativa citada por el cliente en discovery, sobre el total de oportunidades del periodo"),
            ("dispersión de precio de cierre", "desviación entre el precio de lista y el precio efectivo por categoría de competidor enfrentado"),
        ],
        caso=(
            "Ruta Andina se compara con dos plataformas regionales y pierde en funcionalidades. En las "
            "entrevistas, los clientes mencionan primero «la secretaria y el cuaderno» y luego un servicio de "
            "recordatorios que cuesta la décima parte. La categoría en la que compite no es la que declara."
        ),
        limite=(
            "Redefinir la categoría es costoso: exige educar al mercado y sostener esa educación por años. Una "
            "empresa sin presupuesto de comunicación sostenido suele obtener mejores resultados diferenciándose "
            "dentro de una categoría existente que creando una nueva."
        ),
        libros=["levitt", "porter", "ries-trout", "moore"],
        error=("Definir la categoría desde la sala de producto",
               "Usa la lista de alternativas que los clientes nombraron y no la que el equipo considera relevante."),
    ),
    dict(
        n="04",
        slug="b2c-b2b-b2g-y-modelos-hibridos",
        titulo="B2C, B2B, B2G y modelos híbridos",
        tesis=(
            "La diferencia entre vender a personas, a empresas o al Estado no está en el producto sino en la "
            "estructura de la decisión: cuántas personas intervienen, qué riesgo asume cada una, qué evidencia "
            "exige el proceso y cuánto tarda el dinero en moverse. En B2C domina la decisión individual, el "
            "impulso y la escala. En B2B aparece un comité con incentivos distintos y un comprador que arriesga "
            "reputación. En B2G la regla es la formalidad: bases de licitación, plazos y requisitos que hacen "
            "irrelevante buena parte del arte comercial. La mayoría de las empresas reales opera híbridos y "
            "fracasa cuando aplica el manual de un modelo al otro."
        ),
        conceptos=[
            ("unidad de decisión", "conjunto de personas que influyen, vetan, usan, pagan y firman una compra"),
            ("riesgo personal del comprador", "consecuencia profesional que enfrenta quien recomienda la compra si el resultado falla"),
            ("ciclo de compra", "tiempo entre el primer contacto calificado y la firma, medido por mediana y no por promedio"),
            ("formalidad del proceso", "grado en que la compra está gobernada por bases, reglamentos o políticas escritas"),
        ],
        metodo=[
            "identificar quién usa, quién decide, quién paga y quién puede vetar",
            "estimar el riesgo personal de cada participante",
            "mapear el proceso formal exigido, si existe",
            "ajustar evidencia, materiales y plazos a esa estructura",
            "definir el movimiento comercial coherente con el valor del contrato",
        ],
        senales=[
            ("ciclo de compra mediano", "días entre oportunidad calificada y firma, mediana por segmento y por modelo de venta"),
            ("número de contactos por negocio ganado", "personas distintas del cliente con al menos una interacción registrada, promedio por negocio cerrado"),
            ("tasa de negocios detenidos por proceso formal", "oportunidades bloqueadas por requisitos administrativos dividido por oportunidades del segmento público"),
        ],
        caso=(
            "Ruta Andina vende en tres frentes con el mismo guion: peluquerías de un local, cadenas de 14 "
            "sucursales y municipios. En el frente municipal perdió tres procesos por no adjuntar boletas de "
            "garantía y en las cadenas presenta la misma demo de 20 minutos que usa con un local."
        ),
        limite=(
            "Los modelos son categorías analíticas, no compartimentos. Una cadena familiar puede decidir como B2C "
            "y un municipio pequeño puede comportarse como B2B; la estructura de decisión observada manda sobre "
            "la etiqueta."
        ),
        libros=["kotler", "miller-heiman", "rackham", "moore"],
        error=("Usar el mismo material comercial en los tres modelos",
               "Construye una versión por estructura de decisión y verifica qué evidencia pide cada rol."),
    ),
    dict(
        n="05",
        slug="funnel-flywheel-y-ciclo-de-compra",
        titulo="Funnel, flywheel y ciclo de compra",
        tesis=(
            "El embudo es un modelo contable útil: ordena etapas, permite medir conversión y detectar dónde se "
            "pierde volumen. Su defecto es que termina en la venta y sugiere que cada cliente se consigue desde "
            "cero. El flywheel corrige esa ceguera: modela cómo clientes satisfechos reducen el costo de "
            "adquirir a los siguientes mediante referencias, reputación y contenido. Ninguno de los dos describe "
            "lo que hace el cliente: el ciclo de compra parte de un disparador, atraviesa exploración y "
            "evaluación y termina en una decisión que puede ser no comprar. Usar los tres modelos a la vez es lo "
            "que evita optimizar un embudo que el cliente no está recorriendo."
        ),
        conceptos=[
            ("embudo", "representación de etapas internas con volúmenes y tasas de paso entre ellas"),
            ("flywheel", "modelo donde el resultado de los clientes actuales alimenta la adquisición de los siguientes"),
            ("disparador de compra", "evento en la vida del cliente que convierte un problema tolerado en un problema urgente"),
            ("fricción", "todo aquello que aumenta el esfuerzo o el riesgo percibido de avanzar a la siguiente etapa"),
        ],
        metodo=[
            "reconstruir el ciclo de compra desde el disparador y no desde el primer clic",
            "mapear las etapas internas que responden a ese ciclo",
            "medir volumen, conversión y tiempo por etapa",
            "identificar la fricción dominante en la etapa limitante",
            "decidir si conviene remover fricción o aumentar impulso",
        ],
        senales=[
            ("tiempo por etapa", "mediana de días que una oportunidad permanece en cada etapa, por segmento"),
            ("tasa de referidos activos", "clientes que originaron al menos una oportunidad en 12 meses dividido por clientes activos"),
            ("abandono por etapa", "oportunidades sin actividad en 30 días dividido por oportunidades abiertas en esa etapa"),
        ],
        caso=(
            "El embudo de Ruta Andina declara cinco etapas y el 44 % de las oportunidades lleva más de 30 días "
            "sin actividad. Al entrevistar clientes ganados aparece un disparador común: una fiscalización o un "
            "reclamo del SERNAC que obligó a ordenar el registro de atenciones."
        ),
        limite=(
            "El flywheel no aplica igual a todos los negocios: en compras de una sola vez y baja frecuencia, la "
            "referencia existe pero no compone. Antes de invertir en el bucle, verifica que la frecuencia de "
            "contacto lo haga posible."
        ),
        libros=["kotler", "ellis-brown", "sharp", "croll-yoskovitz"],
        error=("Optimizar el embudo sin conocer el disparador",
               "Entrevista a diez clientes ganados y pregunta qué pasó la semana anterior a que buscaran solución."),
    ),
    dict(
        n="06",
        slug="oferta-demanda-y-captura-de-valor",
        titulo="Oferta, demanda y captura de valor",
        tesis=(
            "Crear valor y capturarlo son problemas distintos. Una empresa puede generar un enorme beneficio "
            "para sus clientes y capturar una fracción mínima si su estructura de precios, su poder de "
            "negociación o su canal no lo permiten. La captura depende de tres cosas: cuánto valor se crea, "
            "cuánta alternativa tiene el cliente y qué parte del excedente permite la estructura de la industria. "
            "Porter llamó a esto la distribución del excedente entre proveedores, competidores y compradores. "
            "Para una pyme el corolario es duro: mejorar el producto sin cambiar la posición competitiva "
            "aumenta el valor creado y no necesariamente el capturado."
        ),
        conceptos=[
            ("valor creado", "diferencia entre la disposición a pagar del cliente y el costo de proveer el servicio"),
            ("valor capturado", "parte del valor creado que se convierte en margen para la empresa"),
            ("poder de negociación", "capacidad de una parte de imponer condiciones por la escasez de alternativas de la otra"),
            ("excedente del cliente", "diferencia entre lo que el cliente habría pagado y lo que efectivamente pagó"),
        ],
        metodo=[
            "estimar disposición a pagar del segmento con evidencia y no con intuición",
            "calcular el costo de servir completo, incluida la posventa",
            "identificar quién más se lleva parte del excedente en la cadena",
            "evaluar qué cambio en la oferta modifica la disposición a pagar",
            "elegir una palanca de captura y medir su efecto en margen y volumen",
        ],
        senales=[
            ("margen de contribución por cliente", "ingreso menos costos variables de servir, incluida atención y comisiones, por cliente y por mes"),
            ("brecha entre precio de lista y precio efectivo", "descuento promedio ponderado por ingreso, por segmento y trimestre"),
            ("costo de servir por segmento", "horas de soporte e implementación valorizadas dividido por clientes activos del segmento"),
        ],
        caso=(
            "El plan más vendido de Ruta Andina deja 12 % de margen de contribución porque incluye migración "
            "de datos «de cortesía» que consume 9 horas por cliente. El valor creado es alto y el capturado es "
            "marginal: el excedente se lo lleva la operación."
        ),
        limite=(
            "Maximizar la captura a corto plazo puede destruir la relación. En mercados pequeños y conectados como "
            "el chileno, un cliente que siente haber sido exprimido no vuelve y además lo comenta."
        ),
        libros=["porter", "nagle", "simon", "ramanujam"],
        error=("Confundir precio alto con captura de valor",
               "Compara margen de contribución por segmento, no precio de lista, antes de declarar rentabilidad."),
    ),
    dict(
        n="07",
        slug="propuesta-de-valor-inicial",
        titulo="Propuesta de valor inicial",
        tesis=(
            "Una propuesta de valor no es un eslogan: es una afirmación falsable sobre para quién es la oferta, "
            "qué problema resuelve, con qué mecanismo y contra qué alternativa. Su prueba no es que suene bien "
            "en la reunión sino que un cliente que no conoce a la empresa pueda repetirla con sus palabras y "
            "decir si le sirve. La versión inicial se construye con la evidencia disponible y se marca como "
            "hipótesis; su función es orientar experimentos, no adornar la página de inicio."
        ),
        conceptos=[
            ("propuesta de valor", "afirmación falsable sobre destinatario, problema, mecanismo y alternativa desplazada"),
            ("mecanismo", "explicación concreta de por qué la oferta produce el resultado prometido"),
            ("prueba de comprensión", "verificación de que un tercero puede reformular la propuesta sin ayuda"),
            ("promesa verificable", "afirmación que puede comprobarse con un dato o una experiencia del propio cliente"),
        ],
        metodo=[
            "escribir la propuesta en una frase con destinatario, problema y mecanismo",
            "nombrar explícitamente la alternativa que desplaza",
            "someterla a prueba de comprensión con cinco personas del segmento",
            "traducir la promesa en una evidencia comprobable",
            "registrar qué respuesta obligaría a reescribirla",
        ],
        senales=[
            ("tasa de comprensión sin ayuda", "personas que reformulan correctamente la propuesta dividido por personas expuestas, en prueba de cinco minutos"),
            ("tasa de avance tras la primera exposición", "reuniones que avanzan a la siguiente etapa dividido por primeras reuniones sostenidas"),
            ("consistencia entre canales", "porcentaje de piezas activas cuyo mensaje central coincide con la propuesta aprobada"),
        ],
        caso=(
            "La página de Ruta Andina dice «la plataforma todo-en-uno para tu negocio». En una prueba con ocho "
            "dueños de taller, seis no supieron decir qué hacía el producto y tres creyeron que era un sistema "
            "contable."
        ),
        limite=(
            "Una propuesta clara no compensa una oferta débil. Si el mecanismo no produce el resultado, mejorar la "
            "redacción sólo acelera la llegada de clientes que se irán antes."
        ),
        libros=["osterwalder-vpd", "heath", "ries-trout", "fitzpatrick"],
        error=("Escribir la propuesta para el equipo interno",
               "Prueba la comprensión con personas del segmento que nunca oyeron hablar de la empresa."),
    ),
    dict(
        n="08",
        slug="canales-comerciales-y-puntos-de-contacto",
        titulo="Canales comerciales y puntos de contacto",
        tesis=(
            "Un canal no es un lugar donde se publica: es un camino completo por el que fluyen información, "
            "decisión, dinero y servicio. Elegir canal implica aceptar su economía —costo por contacto, tasa de "
            "conversión típica, márgenes que exige un intermediario— y sus restricciones de control. Los puntos "
            "de contacto, en cambio, son los momentos concretos donde el cliente forma juicio: un correo, una "
            "ficha de producto, una llamada, una boleta. La coherencia entre puntos de contacto es la que "
            "produce confianza; la incoherencia se paga en conversión y en reclamos."
        ),
        conceptos=[
            ("canal", "ruta completa por la que la oferta llega al cliente, incluidos información, transacción y servicio"),
            ("punto de contacto", "momento observable en que el cliente interactúa con la empresa y actualiza su juicio"),
            ("economía del canal", "costo por contacto, tasa de conversión y margen que deja el canal después de comisiones"),
            ("control sobre la experiencia", "grado en que la empresa puede decidir qué ve, recibe y responde el cliente"),
        ],
        metodo=[
            "listar los canales activos y su participación real en ingreso",
            "calcular costo por oportunidad y margen neto por canal",
            "mapear los puntos de contacto críticos de cada canal",
            "detectar incoherencias entre promesa y experiencia",
            "decidir dónde concentrar y qué canal cerrar o rediseñar",
        ],
        senales=[
            ("costo por oportunidad calificada por canal", "gasto directo del canal dividido por oportunidades calificadas originadas por él, mensual"),
            ("margen neto por canal", "ingreso atribuible menos costo del canal y comisiones, dividido por ingreso atribuible"),
            ("índice de coherencia de mensaje", "puntos de contacto auditados que coinciden con la propuesta aprobada, sobre el total auditado"),
        ],
        caso=(
            "Ruta Andina opera seis canales. Marketplace representa 28 % de las unidades y 4 % del margen; el "
            "canal de referidos representa 9 % de las unidades y 21 % del margen. Nadie ha revisado esa "
            "asimetría porque el informe semanal sólo muestra unidades."
        ),
        limite=(
            "Cerrar un canal poco rentable puede ser un error si cumple una función de descubrimiento. Antes de "
            "eliminarlo, mide su efecto sobre canales posteriores, no sólo su margen directo."
        ),
        libros=["kotler", "weinberg-traction", "chaffey", "flint"],
        error=("Evaluar canales por volumen y no por margen",
               "Agrega costo de comisiones, despacho y devoluciones antes de comparar canales entre sí."),
    ),
    dict(
        n="09",
        slug="marketing-estrategico-versus-operativo",
        titulo="Marketing estratégico versus operativo",
        tesis=(
            "El marketing estratégico decide dónde competir y con qué diferencia; el operativo decide cómo "
            "ejecutar esa elección semana a semana. La confusión entre ambos produce dos patologías: equipos "
            "que ejecutan campañas impecables sobre una elección equivocada, y equipos que discuten "
            "posicionamiento durante meses sin poner nada en el mercado. Rumelt distingue el diagnóstico y la "
            "política rectora de la mera lista de aspiraciones; la mayoría de los «planes de marketing» de pyme "
            "son listas de actividades sin diagnóstico y por eso no pueden ser evaluados."
        ),
        conceptos=[
            ("diagnóstico", "explicación del obstáculo principal que enfrenta la empresa, con evidencia"),
            ("política rectora", "elección general que orienta la acción y descarta explícitamente otras opciones"),
            ("plan operativo", "conjunto de acciones, responsables, plazos y presupuestos coherentes con la política"),
            ("coherencia de acciones", "grado en que las actividades se refuerzan entre sí en lugar de competir por recursos"),
        ],
        metodo=[
            "formular el diagnóstico en una frase con evidencia que lo respalde",
            "declarar la política rectora y lo que se descarta",
            "derivar tres a cinco acciones coherentes con esa política",
            "asignar responsable, presupuesto y plazo a cada acción",
            "fijar la revisión que confirmaría o refutaría el diagnóstico",
        ],
        senales=[
            ("proporción de presupuesto alineado", "gasto de marketing asignado a acciones derivadas de la política rectora, sobre gasto total"),
            ("acciones activas sin dueño", "iniciativas en ejecución sin responsable nombrado, sobre total de iniciativas"),
            ("tiempo entre decisión y ejecución", "días entre la aprobación de una acción y su primera evidencia en el mercado"),
        ],
        caso=(
            "El plan anual de Ruta Andina enumera 23 iniciativas, ninguna descartada, con el mismo nivel de "
            "prioridad y un solo equipo de tres personas. No hay diagnóstico escrito y el presupuesto se asigna "
            "por orden de llegada."
        ),
        limite=(
            "Una buena estrategia mal ejecutada rinde menos que una estrategia mediocre bien ejecutada de forma "
            "sostenida. El objetivo no es un documento elegante sino una elección que el equipo pueda aplicar sin "
            "consultar en cada decisión."
        ),
        libros=["rumelt", "porter-hbr", "kotler", "doerr"],
        error=("Presentar una lista de actividades como estrategia",
               "Exige que el documento nombre el obstáculo principal y qué opciones quedan descartadas."),
    ),
    dict(
        n="10",
        slug="ventas-transaccionales-y-consultivas",
        titulo="Ventas transaccionales y consultivas",
        tesis=(
            "El modelo de venta debe ser proporcional al valor del contrato y a la complejidad de la decisión. "
            "Una venta transaccional optimiza velocidad y volumen: pocos pasos, información estandarizada, "
            "autoservicio donde sea posible. Una venta consultiva invierte tiempo en diagnóstico porque el "
            "cliente no puede especificar por sí solo lo que necesita. Rackham demostró que las técnicas que "
            "funcionan en ventas pequeñas —cierres de presión, manejo de objeciones agresivo— empeoran los "
            "resultados en ventas grandes. Aplicar el modelo equivocado destruye margen o eterniza el ciclo."
        ),
        conceptos=[
            ("venta transaccional", "proceso corto donde el cliente ya sabe qué quiere y compara principalmente precio y disponibilidad"),
            ("venta consultiva", "proceso donde el vendedor ayuda a definir el problema antes de proponer solución"),
            ("costo de adquisición admisible", "gasto máximo de venta compatible con el margen y el periodo de recuperación del contrato"),
            ("complejidad de decisión", "número de personas, riesgos y evidencias que exige el cliente para avanzar"),
        ],
        metodo=[
            "clasificar el negocio por valor del contrato y complejidad de decisión",
            "calcular el costo de adquisición admisible para ese ticket",
            "elegir el modelo de venta que cabe dentro de ese costo",
            "diseñar el proceso mínimo suficiente para ese modelo",
            "revisar la clasificación cuando cambian ticket o ciclo",
        ],
        senales=[
            ("costo de venta sobre valor del contrato", "horas comerciales valorizadas más gastos directos dividido por el valor del primer año del contrato"),
            ("ciclo mediano por modelo", "días entre oportunidad calificada y cierre, mediana separada por modelo transaccional y consultivo"),
            ("tasa de descuento por modelo", "descuento promedio ponderado por ingreso, comparado entre ambos modelos"),
        ],
        caso=(
            "Ruta Andina atiende con el mismo proceso de cinco reuniones a un cliente de CLP 39.000 mensuales y "
            "a una cadena de CLP 2,4 millones anuales. El primero consume más costo comercial del que aportará "
            "en dos años."
        ),
        limite=(
            "La clasificación no es permanente: un cliente pequeño puede convertirse en cuenta estratégica. El "
            "criterio debe revisarse cuando cambia el potencial de expansión, no sólo el ticket inicial."
        ),
        libros=["rackham", "roberge", "keenan", "moore"],
        error=("Atender todo con el proceso más caro",
               "Define umbrales de ticket y complejidad que determinan qué proceso se aplica, y audítalos cada trimestre."),
    ),
    dict(
        n="11",
        slug="customer-success-y-expansion",
        titulo="Customer Success y expansión",
        tesis=(
            "En modelos recurrentes la venta no termina en la firma: allí empieza el periodo donde el cliente "
            "decide si el gasto se justifica. Customer Success no es soporte reactivo ni un gesto de "
            "amabilidad; es la función que garantiza que el cliente alcance el resultado por el que pagó y que "
            "esa evidencia quede registrada. La expansión —más usuarios, más módulos, más locales— sólo es "
            "legítima cuando el resultado inicial se cumplió. Vender expansión sobre una base insatisfecha "
            "adelanta ingreso y multiplica el churn futuro."
        ),
        conceptos=[
            ("resultado deseado del cliente", "cambio concreto que el cliente esperaba lograr, expresado en su métrica y no en la del proveedor"),
            ("time-to-value", "tiempo entre la firma y la primera evidencia verificable de ese resultado"),
            ("salud de cuenta", "estimación del riesgo de baja construida con uso, resultado, relación y señales comerciales"),
            ("expansión legítima", "aumento de ingreso en una cuenta que ya obtuvo el resultado inicial comprometido"),
        ],
        metodo=[
            "definir el resultado deseado con el cliente antes de implementar",
            "instrumentar la señal que evidencia ese resultado",
            "medir el tiempo hasta el primer valor",
            "revisar salud de cuenta con criterios y no con impresiones",
            "proponer expansión sólo cuando el resultado inicial está acreditado",
        ],
        senales=[
            ("time-to-value mediano", "días entre firma y primer uso del módulo que produce el resultado comprometido, mediana por cohorte"),
            ("ingreso neto retenido", "ingreso del mismo grupo de clientes 12 meses después incluyendo bajas, contracciones y expansiones, sobre el inicial"),
            ("cobertura de resultado documentado", "cuentas con evidencia registrada del resultado logrado, sobre cuentas activas"),
        ],
        caso=(
            "El 61 % de las bajas de Ruta Andina nunca completó la carga inicial de datos. El equipo de éxito "
            "de cliente dedica su tiempo a resolver tickets y no tiene definido qué significa que una cuenta "
            "«esté bien»."
        ),
        limite=(
            "Customer Success no puede compensar un producto que no resuelve el problema ni una venta que prometió "
            "lo que no existe. Cuando el churn se concentra en un segmento específico, el diagnóstico probablemente "
            "esté en oferta o en calificación."
        ),
        libros=["mehta", "hulick", "fader", "dixon-effort"],
        error=("Medir éxito de cliente por tickets resueltos",
               "Sustituye el indicador por resultado acreditado y tiempo hasta el primer valor."),
    ),
    dict(
        n="12",
        slug="revenue-operations-como-integracion",
        titulo="Revenue Operations como integración",
        tesis=(
            "Revenue Operations existe porque los sistemas de marketing, ventas y servicio evolucionaron por "
            "separado y produjeron tres versiones incompatibles de la verdad. RevOps no es una herramienta ni "
            "un cargo: es la disciplina que define un modelo de datos común, acuerdos explícitos entre áreas y "
            "un único conjunto de definiciones para las métricas que gobiernan el negocio. Su valor no está en "
            "más reportes sino en que las decisiones dejen de discutirse sobre cifras que nadie puede "
            "reconciliar."
        ),
        conceptos=[
            ("modelo de datos de ingresos", "conjunto de entidades, estados y relaciones que representan el recorrido comercial completo"),
            ("definición única de métrica", "acuerdo escrito sobre numerador, denominador, ventana y fuente de cada indicador"),
            ("acuerdo de nivel de servicio interno", "compromiso explícito de tiempo y calidad entre dos áreas del motor de ingresos"),
            ("observabilidad del proceso", "capacidad de detectar que un flujo se rompió antes de que lo note un cliente"),
        ],
        metodo=[
            "inventariar las definiciones actuales de las métricas críticas",
            "acordar una definición única por métrica y documentarla",
            "modelar las entidades y estados que la sostienen",
            "establecer acuerdos de servicio entre áreas",
            "instalar alertas sobre las rupturas más caras",
        ],
        senales=[
            ("discrepancia entre informes", "diferencia porcentual entre el mismo indicador reportado por dos áreas, medida mensualmente"),
            ("completitud de campos críticos", "registros con todos los campos obligatorios completos, sobre registros creados en el periodo"),
            ("tiempo de detección de ruptura", "horas entre que un flujo automatizado falla y que alguien lo detecta"),
        ],
        caso=(
            "Marketing informa 300 leads mensuales y ventas trabaja 60. Ambos números son correctos según su "
            "propia definición de «lead». La reunión mensual de Ruta Andina se consume discutiendo cuál cifra "
            "es la verdadera."
        ),
        limite=(
            "RevOps no resuelve conflictos de incentivos. Si la compensación premia comportamientos "
            "contradictorios entre áreas, la integración de datos hará visible el conflicto pero no lo eliminará."
        ),
        libros=["diorio", "roberge", "grove", "provost"],
        error=("Comprar una herramienta antes de acordar definiciones",
               "Documenta las definiciones y los acuerdos de servicio primero; la herramienta después."),
    ),
    dict(
        n="13",
        slug="etica-comercial-y-confianza",
        titulo="Ética comercial y confianza",
        tesis=(
            "La confianza es un activo económico: reduce el costo de vender, acorta ciclos y sostiene precios. "
            "Se construye lentamente con coherencia entre lo prometido y lo entregado, y se destruye rápido con "
            "una sola incoherencia visible. La ética comercial no es un apéndice del marketing: es una "
            "restricción de diseño que determina qué tácticas están disponibles. En Chile esa restricción "
            "también es legal: la Ley 19.496 obliga a información veraz y oportuna, y el tratamiento de datos "
            "personales tiene reglas propias. Un equipo que sólo se detiene cuando la ley lo obliga ya llegó "
            "tarde."
        ),
        conceptos=[
            ("promesa verificable", "afirmación comercial que puede acreditarse con evidencia disponible"),
            ("asimetría de información", "ventaja de conocimiento del vendedor que el cliente no puede compensar por sí solo"),
            ("consentimiento informado", "autorización obtenida con información suficiente, libre y específica sobre el uso de los datos"),
            ("costo reputacional", "efecto acumulado de una práctica sobre la disposición futura del mercado a confiar"),
        ],
        metodo=[
            "revisar cada promesa comercial y su evidencia de respaldo",
            "identificar dónde la asimetría de información puede dañar al cliente",
            "verificar base legal y consentimiento del tratamiento de datos",
            "someter la táctica a la prueba de publicación: ¿resiste ser conocida?",
            "documentar la decisión y su responsable",
        ],
        senales=[
            ("tasa de reclamos por información", "reclamos vinculados a publicidad, precio o condiciones, sobre transacciones del periodo"),
            ("promesas sin respaldo documentado", "afirmaciones comerciales activas sin evidencia asociada, sobre total auditado"),
            ("bajas por expectativa incumplida", "bajas cuyo motivo declarado es diferencia entre lo prometido y lo recibido, sobre bajas totales"),
        ],
        caso=(
            "Un vendedor de Ruta Andina prometió por escrito integración con un sistema contable que está en el "
            "roadmap y no existe. El cliente firmó por esa razón. Cancelar cuesta CLP 1,8 millones; sostener la "
            "promesa cuesta la confianza del rubro completo."
        ),
        limite=(
            "La ética no es un catálogo de reglas cerrado: en casos límite hay que decidir con criterio y dejar "
            "traza. Lo que no es discutible es el mínimo legal ni la obligación de no trasladar al cliente un "
            "riesgo que no puede evaluar."
        ),
        libros=["cialdini", "thaler", "oneil", "godin"],
        error=("Tratar el cumplimiento como revisión final",
               "Incorpora la verificación de promesa y de datos en el diseño de la campaña, no en la aprobación."),
    ),
    dict(
        n="14",
        slug="mapa-completo-del-motor-de-ingresos",
        titulo="Mapa completo del motor de ingresos",
        tesis=(
            "Esta clase integra la parte en un artefacto: un mapa que muestra cómo entra la atención, cómo se "
            "convierte en oportunidad, en ingreso y en relación, con las métricas y los supuestos de cada "
            "tramo. Un buen mapa no es un diagrama bonito: permite señalar dónde se pierde valor, qué "
            "definición sostiene cada número y qué decisión está pendiente. Es el documento que permite que "
            "una persona nueva entienda el negocio en una hora y que el equipo discuta sobre la misma "
            "realidad."
        ),
        conceptos=[
            ("mapa del motor de ingresos", "representación de etapas, volúmenes, conversiones, costos y responsables del sistema comercial completo"),
            ("supuesto crítico", "afirmación no verificada de la que depende una parte importante del resultado esperado"),
            ("punto de fuga", "tramo donde se pierde volumen, margen o confianza de forma desproporcionada"),
            ("decisión pendiente", "elección identificada, con dueño y fecha, que el mapa deja explícita en lugar de esconder"),
        ],
        metodo=[
            "dibujar las etapas desde el disparador de compra hasta la renovación",
            "anotar volumen, conversión, tiempo y costo por etapa",
            "marcar los supuestos críticos y su nivel de evidencia",
            "identificar los tres puntos de fuga principales",
            "listar las decisiones pendientes con dueño y fecha",
        ],
        senales=[
            ("cobertura de métricas del mapa", "etapas con métrica definida y fuente identificada, sobre el total de etapas"),
            ("supuestos críticos sin evidencia", "supuestos marcados como no verificados, sobre supuestos totales del mapa"),
            ("valor en riesgo por punto de fuga", "ingreso anual estimado que se pierde en cada punto de fuga, ordenado de mayor a menor"),
        ],
        caso=(
            "Ruta Andina debe presentar al directorio un diagnóstico en una página antes de aprobar el "
            "presupuesto del próximo año. Hoy existen cuatro informes distintos y ninguno explica dónde se "
            "pierde el dinero."
        ),
        limite=(
            "El mapa envejece: refleja el sistema en un momento. Sin una revisión trimestral y un responsable, se "
            "convierte en un documento decorativo que da falsa sensación de control."
        ),
        libros=["diorio", "croll-yoskovitz", "kaplan-norton", "kotler"],
        error=("Construir el mapa sin dueños ni fechas",
               "Cada punto de fuga y cada decisión pendiente debe tener responsable y fecha de revisión."),
    ),
]
