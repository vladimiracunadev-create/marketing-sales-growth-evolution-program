# -*- coding: utf-8 -*-
"""Parte 02 — Cliente y comportamiento del consumidor."""

CLASES = [
    dict(
        n="01",
        slug="cliente-usuario-comprador-y-decisor",
        titulo="Cliente, usuario, comprador y decisor",
        tesis=(
            "La palabra «cliente» esconde al menos cuatro roles que pueden recaer en personas distintas con "
            "intereses opuestos: quien usa el producto todos los días, quien firma la orden de compra, quien "
            "paga la factura y quien puede vetar por riesgo o cumplimiento. Un mensaje que entusiasma al "
            "usuario puede alarmar al que paga; una demo brillante puede ser irrelevante para quien decide. "
            "Separar los roles no es un ejercicio académico: cambia a quién se entrevista, qué evidencia se "
            "prepara y en qué orden se conversa."
        ),
        conceptos=[
            ("usuario", "persona que interactúa con el producto y experimenta sus beneficios y fricciones cotidianas"),
            ("comprador económico", "persona con autoridad presupuestaria para aprobar el gasto y con responsabilidad sobre el retorno"),
            ("influenciador con veto", "actor que no decide la compra pero puede detenerla por riesgo técnico, legal o de cumplimiento"),
            ("criterio de decisión por rol", "conjunto de razones y evidencias que cada rol considera suficientes para avanzar"),
        ],
        metodo=[
            "listar a todas las personas que tocan la decisión",
            "asignar rol y criterio de decisión a cada una",
            "identificar conflictos entre criterios",
            "diseñar la evidencia específica que necesita cada rol",
            "definir el orden de conversaciones que reduce el riesgo de veto tardío",
        ],
        senales=[
            ("cobertura de roles por oportunidad", "roles críticos con al menos un contacto identificado dividido por roles críticos definidos, por oportunidad abierta"),
            ("negocios detenidos por veto tardío", "oportunidades bloqueadas después de la propuesta por un actor no contactado, sobre oportunidades perdidas"),
            ("tiempo hasta contactar al comprador económico", "días entre la primera reunión y la primera conversación con quien controla el presupuesto"),
        ],
        caso=(
            "En la cadena de 14 locales, Ruta Andina conversó ocho semanas con la jefa de operaciones —usuaria "
            "entusiasta— y nunca con el gerente de finanzas, que rechazó el proyecto en 15 minutos por el "
            "modelo de cobro por local."
        ),
        limite=(
            "En negocios pequeños los cuatro roles suelen recaer en una sola persona; forzar el mapa completo "
            "burocratiza una venta simple. El criterio es el valor del contrato y el riesgo percibido, no el "
            "tamaño del formulario."
        ),
        libros=["miller-heiman", "dixon-customer", "kotler", "solomon"],
        error=("Confundir entusiasmo del usuario con avance del negocio",
               "Exige evidencia de contacto con el comprador económico antes de considerar avanzada la oportunidad."),
    ),
    dict(
        n="02",
        slug="problemas-necesidades-y-resultados-deseados",
        titulo="Problemas, necesidades y resultados deseados",
        tesis=(
            "Los clientes no compran soluciones: compran resultados. Ulwick propuso expresar esos resultados "
            "como enunciados medibles —minimizar el tiempo necesario para X, reducir la probabilidad de Y— "
            "porque así se vuelven comparables, priorizables y verificables. La diferencia práctica es enorme: "
            "«queremos ser más eficientes» no permite diseñar nada, mientras que «reducir de 40 % a 15 % las "
            "horas perdidas por inasistencias» permite estimar valor, fijar precio y comprobar el "
            "cumplimiento."
        ),
        conceptos=[
            ("problema", "brecha entre el estado actual y el estado deseado que produce un costo tolerado o intolerable"),
            ("resultado deseado", "enunciado medible de lo que el cliente quiere lograr, en su propia unidad de medida"),
            ("importancia percibida", "cuánto le importa al cliente ese resultado en relación con sus otras prioridades"),
            ("insatisfacción actual", "grado en que la solución vigente falla en entregar ese resultado"),
        ],
        metodo=[
            "recoger los resultados en las palabras del cliente",
            "reescribirlos como enunciados medibles",
            "puntuar importancia e insatisfacción de cada uno",
            "priorizar donde la brecha es mayor",
            "traducir la brecha priorizada en requisito de oferta",
        ],
        senales=[
            ("brecha de oportunidad", "importancia más la diferencia entre importancia e satisfacción, calculada por resultado deseado y por segmento"),
            ("resultados formulados de forma medible", "enunciados con unidad, dirección y magnitud, sobre total de resultados recogidos"),
            ("coincidencia entre resultado prometido y entregado", "cuentas donde el resultado comprometido fue verificado, sobre cuentas implementadas"),
        ],
        caso=(
            "Ruta Andina pregunta en discovery «¿qué necesitas?» y recibe respuestas sobre funcionalidades. Al "
            "reformular hacia resultados, aparece que la prioridad real es cobrar antes y no agendar mejor."
        ),
        limite=(
            "No todos los resultados relevantes son cuantificables; algunos son sociales o emocionales, como "
            "verse profesional ante los clientes. Forzar una métrica sobre ellos empobrece el diagnóstico."
        ),
        libros=["ulwick", "christensen", "fitzpatrick", "osterwalder-vpd"],
        error=("Anotar funcionalidades pedidas como si fueran necesidades",
               "Pregunta qué haría el cliente con esa funcionalidad y qué resultado espera obtener."),
    ),
    dict(
        n="03",
        slug="jobs-to-be-done",
        titulo="Jobs to Be Done",
        tesis=(
            "Jobs to Be Done propone una unidad de análisis distinta: no el cliente ni el producto, sino el "
            "progreso que una persona intenta lograr en una circunstancia concreta. Christensen mostró que los "
            "productos son «contratados» para hacer un trabajo y «despedidos» cuando otro lo hace mejor. El "
            "valor del marco está en la circunstancia: la misma persona contrata soluciones distintas según el "
            "contexto. Su riesgo es volverse una etiqueta: escribir «el job de mi cliente es crecer» no "
            "aporta nada porque no describe circunstancia, ansiedad ni alternativa."
        ),
        conceptos=[
            ("job funcional", "tarea concreta que el cliente busca completar en una circunstancia específica"),
            ("dimensión social y emocional", "cómo quiere sentirse y ser percibido el cliente al resolver ese trabajo"),
            ("fuerzas de progreso", "empuje del problema y atracción de la nueva solución que impulsan el cambio"),
            ("fuerzas de resistencia", "ansiedad ante lo nuevo y hábito con lo actual que frenan el cambio"),
        ],
        metodo=[
            "reconstruir la línea de tiempo de una compra reciente",
            "identificar el evento disparador y la circunstancia",
            "nombrar el trabajo funcional, social y emocional",
            "mapear las cuatro fuerzas de progreso y resistencia",
            "diseñar la intervención que reduce ansiedad o hábito",
        ],
        senales=[
            ("frecuencia de disparadores por tipo", "eventos disparadores identificados por categoría, sobre entrevistas de compra realizadas"),
            ("tasa de abandono por ansiedad declarada", "oportunidades perdidas donde el cliente citó riesgo de migración o aprendizaje, sobre pérdidas totales"),
            ("tiempo desde disparador hasta búsqueda", "días entre el evento disparador y el primer contacto con una solución, mediana por segmento"),
        ],
        caso=(
            "Las entrevistas de Ruta Andina revelan un patrón: los talleres buscan solución la semana después "
            "de perder un cliente importante por una cita mal registrada. Nadie en marketing sabía que ese era "
            "el disparador."
        ),
        limite=(
            "JTBD no reemplaza la segmentación operativa ni el dimensionamiento de mercado: explica por qué "
            "alguien compra, no cuántos como él existen ni cómo alcanzarlos con un presupuesto dado."
        ),
        libros=["christensen", "ulwick", "fitzpatrick", "cagan"],
        error=("Enunciar el job en términos genéricos de negocio",
               "Reescribe el job incluyendo circunstancia, momento y alternativa desplazada."),
    ),
    dict(
        n="04",
        slug="buyer-persona-con-evidencia",
        titulo="Buyer persona con evidencia",
        tesis=(
            "Una buyer persona es útil sólo si cada afirmación tiene una fuente y una fecha. La versión "
            "decorativa —nombre inventado, foto de banco de imágenes, aficiones irrelevantes— produce falsa "
            "confianza y sirve para justificar decisiones que nadie verificó. La versión rigurosa documenta "
            "responsabilidades, presión bajo la que trabaja, criterios de evaluación, lenguaje que usa, "
            "objeciones típicas y fuentes de información, y marca explícitamente qué es hipótesis y qué está "
            "verificado."
        ),
        conceptos=[
            ("persona basada en evidencia", "perfil donde cada atributo indica fuente, número de observaciones y fecha"),
            ("atributo accionable", "característica que cambia mensaje, canal, oferta o proceso comercial"),
            ("hipótesis marcada", "afirmación aún no verificada que se declara como tal para evitar tratarla como hecho"),
            ("caducidad del perfil", "fecha a partir de la cual el perfil debe revalidarse por cambios de mercado"),
        ],
        metodo=[
            "definir qué decisiones debe informar la persona",
            "recolectar evidencia de entrevistas, CRM y analítica",
            "escribir sólo atributos accionables con su fuente",
            "marcar hipótesis pendientes y su plan de validación",
            "fijar fecha de revisión del perfil",
        ],
        senales=[
            ("proporción de atributos con fuente", "atributos con fuente y fecha registradas, sobre atributos totales del perfil"),
            ("uso efectivo del perfil", "piezas o guiones que citan explícitamente un atributo del perfil, sobre piezas producidas"),
            ("antigüedad del perfil", "meses desde la última validación con datos nuevos"),
        ],
        caso=(
            "Ruta Andina tiene tres personas documentadas con nombres, edad y hobbies. Ninguna indica cómo "
            "evalúan proveedores, qué objeción aparece primero ni de dónde salió el dato."
        ),
        limite=(
            "Una persona describe un patrón, no a un individuo. Usarla para justificar decisiones sobre un "
            "cliente concreto es un error de nivel de análisis."
        ),
        libros=["fitzpatrick", "portigal", "solomon", "kotler"],
        error=("Documentar rasgos irrelevantes para la decisión comercial",
               "Elimina todo atributo que no cambie mensaje, canal, oferta o proceso."),
    ),
    dict(
        n="05",
        slug="ideal-customer-profile",
        titulo="Ideal Customer Profile",
        tesis=(
            "El ICP describe la organización —no la persona— a la que la empresa puede servir mejor que nadie "
            "con la capacidad que hoy tiene. Se construye mirando hacia atrás: qué características comparten "
            "los clientes que obtuvieron resultado, renovaron y expandieron, y qué características comparten "
            "los que se fueron. Su función es doble: enfocar la prospección y, sobre todo, dar permiso "
            "explícito para descartar oportunidades que consumirán más de lo que aportarán."
        ),
        conceptos=[
            ("perfil de cliente ideal", "conjunto de características firmográficas y de comportamiento asociadas a resultado, permanencia y margen"),
            ("criterio de exclusión", "característica que predice fracaso y que autoriza a descartar una oportunidad"),
            ("ajuste técnico y operativo", "grado en que la operación actual puede entregar el resultado a ese tipo de cliente"),
            ("potencial de expansión", "capacidad estimada de la cuenta de aumentar su gasto sin nueva venta compleja"),
        ],
        metodo=[
            "separar la base entre clientes exitosos y perdidos",
            "comparar características de ambos grupos",
            "identificar los predictores de permanencia y margen",
            "escribir criterios de inclusión y de exclusión",
            "aplicar el ICP a la lista de prospección vigente y medir el efecto",
        ],
        senales=[
            ("permanencia por ajuste al ICP", "tasa de retención a 12 meses de cuentas que cumplen el ICP frente a las que no lo cumplen"),
            ("proporción de pipeline dentro del ICP", "valor de oportunidades abiertas que cumplen el ICP, sobre valor total del pipeline"),
            ("margen de contribución por ajuste", "margen promedio de cuentas dentro y fuera del ICP, comparado trimestralmente"),
        ],
        caso=(
            "Al cruzar retención con rubro y tamaño, Ruta Andina descubre que las cuentas de un solo local sin "
            "personal administrativo tienen 4,1 veces más probabilidad de darse de baja antes de seis meses."
        ),
        limite=(
            "Un ICP construido sólo con la base actual reproduce los sesgos de la prospección pasada. Debe "
            "contrastarse con segmentos aún no atendidos antes de convertirlo en política."
        ),
        libros=["moore", "ross", "fader", "roberge"],
        error=("Definir el ICP por deseo comercial y no por datos de resultado",
               "Construye el perfil desde la cohorte que efectivamente renovó y expandió."),
    ),
    dict(
        n="06",
        slug="unidad-de-decision-en-b2b",
        titulo="Unidad de decisión en B2B",
        tesis=(
            "La investigación de Adamson y Dixon documentó que el número de personas involucradas en una "
            "compra B2B creció hasta hacer del consenso interno —y no de la persuasión individual— el "
            "principal obstáculo. El vendedor rara vez está presente cuando se toma la decisión; lo que "
            "circula en su ausencia es el material que dejó y el relato de su contacto. De ahí que la tarea "
            "central sea habilitar a un mobilizer: alguien con voluntad y capacidad de mover el consenso "
            "interno."
        ),
        conceptos=[
            ("comité de compra", "conjunto de personas cuya aprobación explícita o tácita se requiere para avanzar"),
            ("mobilizer", "actor interno dispuesto a impulsar el cambio y con credibilidad para hacerlo"),
            ("consenso interno", "grado de acuerdo entre los miembros del comité sobre problema, solución y prioridad"),
            ("material habilitante", "documento diseñado para que el mobilizer defienda el proyecto sin el vendedor presente"),
        ],
        metodo=[
            "identificar a los miembros del comité y su postura inicial",
            "detectar quién puede y quiere movilizar el cambio",
            "diagnosticar dónde se rompe el consenso",
            "producir material específico para esa ruptura",
            "acordar un plan mutuo con hitos y responsables",
        ],
        senales=[
            ("tamaño del comité por negocio", "personas distintas del cliente involucradas en la decisión, promedio por negocio cerrado y perdido"),
            ("presencia de plan mutuo", "oportunidades con plan mutuo firmado por el cliente, sobre oportunidades en etapa avanzada"),
            ("tasa de estancamiento", "oportunidades sin avance de etapa en 60 días, sobre oportunidades abiertas del segmento"),
        ],
        caso=(
            "El negocio con la cadena involucra operaciones, finanzas, TI y un socio fundador. Ruta Andina "
            "preparó una sola presentación, pensada para operaciones, y la envió a los cuatro."
        ),
        limite=(
            "Un mobilizer entusiasta pero sin credibilidad interna puede empeorar la posición del proveedor. La "
            "evaluación debe considerar influencia real y no sólo disposición."
        ),
        libros=["dixon-customer", "miller-heiman", "rackham", "dixon-challenger"],
        error=("Enviar el mismo material a todo el comité",
               "Produce una pieza por preocupación dominante: riesgo, costo, operación e integración."),
    ),
    dict(
        n="07",
        slug="customer-journey",
        titulo="Customer journey",
        tesis=(
            "Un mapa de journey útil describe lo que hace y siente el cliente, no lo que hace la empresa. Su "
            "valor aparece cuando cada etapa registra: qué intenta lograr, qué información busca, con quién "
            "conversa, qué fricción encuentra y qué evidencia necesita para avanzar. Un mapa que sólo enumera "
            "canales propios es un organigrama disfrazado. El journey además no termina en la compra: la "
            "experiencia posterior determina renovación, referencia y reputación."
        ),
        conceptos=[
            ("etapa del journey", "momento definido por el objetivo del cliente y no por el canal que la empresa usa"),
            ("punto de dolor", "fricción concreta que aumenta esfuerzo, riesgo o tiempo del cliente en una etapa"),
            ("momento de la verdad", "interacción que define desproporcionadamente la percepción de toda la relación"),
            ("brecha de expectativa", "diferencia entre lo que el cliente esperaba y lo que efectivamente recibió"),
        ],
        metodo=[
            "definir las etapas desde la perspectiva del cliente",
            "documentar objetivo, información buscada y fricción por etapa",
            "identificar los momentos de la verdad",
            "medir esfuerzo o abandono en cada uno",
            "priorizar intervenciones por costo y efecto",
        ],
        senales=[
            ("esfuerzo percibido por etapa", "puntuación de esfuerzo declarada por el cliente al completar la etapa, escala uniforme y muestra mínima definida"),
            ("abandono por etapa", "clientes que no avanzan a la etapa siguiente, sobre los que ingresaron a la etapa actual"),
            ("brecha de expectativa en onboarding", "diferencia entre plazo prometido y plazo real de puesta en marcha, mediana en días"),
        ],
        caso=(
            "El journey documentado de Ruta Andina tiene cinco etapas y todas describen acciones internas: "
            "«enviar propuesta», «agendar demo». Ninguna describe qué intenta lograr el cliente."
        ),
        limite=(
            "El journey promedio puede no existir: si el mapa mezcla segmentos con recorridos distintos, "
            "producirá intervenciones que no sirven a ninguno."
        ),
        libros=["dixon-effort", "krug", "solomon", "kotler"],
        error=("Mapear el proceso interno y llamarlo journey",
               "Reescribe cada etapa empezando por el verbo del cliente, no por el de la empresa."),
    ),
    dict(
        n="08",
        slug="motivaciones-y-fricciones",
        titulo="Motivaciones y fricciones",
        tesis=(
            "Toda conversión es el resultado de una competencia entre motivación y fricción. Aumentar la "
            "motivación suele ser caro y lento; reducir fricción suele ser barato y rápido, pero tiene un "
            "límite: sin motivación suficiente, ninguna reducción de fricción produce acción. El diagnóstico "
            "correcto empieza determinando cuál de las dos domina. Confundirlas lleva a rediseñar un "
            "formulario cuando el problema era que la oferta no le importaba a nadie."
        ),
        conceptos=[
            ("motivación", "fuerza que impulsa a actuar, proveniente del valor esperado y de la urgencia del problema"),
            ("fricción", "costo de esfuerzo, tiempo, riesgo o confusión que impone el proceso"),
            ("umbral de acción", "punto en que la motivación supera a la fricción y el cliente avanza"),
            ("fricción productiva", "obstáculo deliberado que filtra clientes que no serán rentables o que protege al cliente"),
        ],
        metodo=[
            "medir dónde se produce el abandono con datos y no con supuestos",
            "distinguir si el abandono se explica por motivación o por fricción",
            "listar fricciones por costo de remoción",
            "eliminar la fricción de mayor efecto y menor costo",
            "verificar que la remoción no degradó la calidad del cliente ganado",
        ],
        senales=[
            ("tasa de finalización por paso", "usuarios que completan el paso, sobre usuarios que lo iniciaron, por dispositivo y por origen"),
            ("tiempo de finalización", "mediana de segundos u horas para completar el proceso, por segmento"),
            ("calidad del cliente ganado tras remover fricción", "tasa de retención a 90 días de la cohorte posterior al cambio, comparada con la anterior"),
        ],
        caso=(
            "Ruta Andina eliminó el registro de tarjeta en la prueba gratuita y triplicó los registros. A los "
            "90 días, la conversión a pago cayó de 18 % a 4 % y el equipo de soporte se saturó."
        ),
        limite=(
            "No toda fricción debe eliminarse: hay fricción que protege al cliente —confirmaciones, "
            "verificaciones— y fricción que protege la economía del negocio."
        ),
        libros=["krug", "laja", "eisenberg", "thaler"],
        error=("Eliminar fricción sin medir la calidad posterior",
               "Compara retención y conversión a pago de la cohorte nueva antes de declarar la mejora."),
    ),
    dict(
        n="09",
        slug="sesgos-cognitivos-y-decisiones",
        titulo="Sesgos cognitivos y decisiones",
        tesis=(
            "Kahneman documentó que las decisiones humanas operan con dos sistemas: uno rápido, asociativo y "
            "propenso a atajos, y otro lento y deliberado. Los sesgos no son defectos raros sino "
            "regularidades: anclaje, aversión a la pérdida, disponibilidad, statu quo. En marketing esto tiene "
            "dos usos y una frontera. El uso legítimo es diseñar información clara que ayude a decidir bien. "
            "El uso ilegítimo es explotar el sesgo para inducir una decisión que el cliente no tomaría "
            "informado. La frontera se cruza cuando el beneficio de la empresa depende del error del cliente."
        ),
        conceptos=[
            ("anclaje", "influencia desproporcionada de la primera cifra o referencia sobre el juicio posterior"),
            ("aversión a la pérdida", "tendencia a valorar más evitar una pérdida que obtener una ganancia equivalente"),
            ("sesgo de statu quo", "preferencia por mantener la situación actual aunque exista una alternativa superior"),
            ("prueba de reversibilidad", "verificación de si el cliente mantendría la decisión al conocer toda la información"),
        ],
        metodo=[
            "identificar qué sesgo está operando en la decisión analizada",
            "distinguir si el diseño ayuda o explota",
            "aplicar la prueba de reversibilidad",
            "documentar la elección y su justificación",
            "medir el efecto en arrepentimiento, reclamos y bajas",
        ],
        senales=[
            ("tasa de arrepentimiento temprano", "cancelaciones dentro de los primeros 30 días, sobre ventas del periodo"),
            ("reclamos por condiciones no comprendidas", "reclamos vinculados a términos, renovación o cobros, sobre transacciones del periodo"),
            ("diferencia de conversión con información completa", "conversión de la variante con información completa frente a la variante reducida"),
        ],
        caso=(
            "Un plan de Ruta Andina se renueva automáticamente y el aviso está en letra pequeña. La conversión "
            "sube 12 % y los reclamos por cobro no esperado suben 3,4 veces."
        ),
        limite=(
            "Conocer los sesgos no inmuniza contra ellos: el equipo comercial también decide bajo anclaje y "
            "aversión a la pérdida, especialmente al final del trimestre."
        ),
        libros=["kahneman", "thaler", "ariely", "cialdini"],
        error=("Usar el sesgo para ocultar una condición relevante",
               "Aplica la prueba de publicación: si la práctica no resistiría ser explicada al cliente, no se usa."),
    ),
    dict(
        n="10",
        slug="riesgo-percibido-y-confianza",
        titulo="Riesgo percibido y confianza",
        tesis=(
            "Antes de evaluar el beneficio, el cliente evalúa el riesgo: de perder dinero, de perder tiempo, "
            "de quedar mal ante otros, de que el proveedor desaparezca. En compras B2B ese riesgo es también "
            "personal para quien recomienda. La confianza es el mecanismo que reduce el riesgo percibido sin "
            "eliminarlo realmente, y se construye con señales verificables: casos comparables, garantías, "
            "transparencia sobre límites y consistencia entre lo dicho y lo hecho."
        ),
        conceptos=[
            ("riesgo percibido", "estimación subjetiva del cliente sobre la probabilidad y magnitud de un resultado adverso"),
            ("señal de confianza", "evidencia verificable que reduce la incertidumbre sobre el desempeño futuro del proveedor"),
            ("riesgo personal del recomendante", "consecuencia profesional que enfrenta quien impulsa la compra si el proyecto falla"),
            ("reversibilidad de la decisión", "facilidad y costo de deshacer la compra si el resultado no se cumple"),
        ],
        metodo=[
            "enumerar los riesgos percibidos por cada rol",
            "clasificarlos en económico, operativo, reputacional y personal",
            "asignar a cada riesgo una señal de confianza verificable",
            "aumentar la reversibilidad donde el riesgo es alto",
            "medir el efecto sobre avance y sobre calidad del cliente ganado",
        ],
        senales=[
            ("objeciones de riesgo por negocio", "objeciones clasificadas como riesgo, sobre objeciones totales registradas en el periodo"),
            ("uso de referencias en negocios ganados", "negocios donde se entregó una referencia verificable, sobre negocios cerrados"),
            ("tasa de conversión con garantía", "conversión de la oferta con garantía explícita frente a la oferta sin garantía"),
        ],
        caso=(
            "Los clientes de Ruta Andina temen perder el historial de citas al migrar. La empresa nunca "
            "documentó su proceso de migración ni ofreció rollback, y esa ausencia explica un tercio de las "
            "pérdidas."
        ),
        limite=(
            "Una garantía amplia mal diseñada puede atraer clientes que no lograrán resultado y trasladar el "
            "costo a la operación. La garantía debe acotarse a lo que la empresa controla."
        ),
        libros=["cialdini", "rackham", "dixon-effort", "godin"],
        error=("Responder al riesgo con más argumentos de beneficio",
               "Atiende el riesgo con evidencia y reversibilidad, no con entusiasmo adicional."),
    ),
    dict(
        n="11",
        slug="objeciones-antes-de-comprar",
        titulo="Objeciones antes de comprar",
        tesis=(
            "Una objeción es información: indica qué le falta al cliente para decidir. Tratarla como un "
            "obstáculo a sortear con técnica produce ventas frágiles; tratarla como diagnóstico produce "
            "mejores ofertas. Rackham observó que en ventas grandes las objeciones se previenen en la etapa de "
            "investigación, no se manejan en la de cierre: cuando el vendedor ayudó a dimensionar el problema, "
            "la objeción de precio aparece con mucha menor frecuencia."
        ),
        conceptos=[
            ("objeción real", "impedimento genuino que bloquea la decisión y puede formularse como pregunta verificable"),
            ("objeción de cortesía", "excusa socialmente aceptable que oculta la razón verdadera de no avanzar"),
            ("prevención de objeciones", "trabajo de diagnóstico previo que elimina la causa antes de que se formule"),
            ("registro de objeciones", "base estructurada de objeciones por segmento, etapa y resultado del negocio"),
        ],
        metodo=[
            "registrar la objeción textual y su etapa",
            "clasificarla como real o de cortesía con una pregunta de verificación",
            "identificar la causa raíz en oferta, precio, riesgo o proceso",
            "corregir el material o la etapa donde se origina",
            "medir si la frecuencia de esa objeción disminuye",
        ],
        senales=[
            ("frecuencia por tipo de objeción", "apariciones de cada objeción, sobre negocios trabajados en el periodo"),
            ("tasa de conversión posterior a la objeción", "negocios ganados después de registrar la objeción, sobre negocios donde apareció"),
            ("objeciones prevenidas", "reducción porcentual de una objeción específica tras modificar el material o el proceso"),
        ],
        caso=(
            "«Es caro» aparece en 63 % de los negocios perdidos de Ruta Andina. Al verificar con una pregunta "
            "de dimensionamiento, en 4 de cada 10 casos el problema real era el plazo de implementación."
        ),
        limite=(
            "No toda objeción debe resolverse: algunas indican que el cliente no pertenece al ICP y la respuesta "
            "correcta es descalificar la oportunidad temprano."
        ),
        libros=["rackham", "keenan", "blount", "cialdini"],
        error=("Responder «es caro» con un descuento",
               "Verifica primero si la objeción es de precio, de valor percibido o de plazo, con una pregunta de dimensionamiento."),
    ),
    dict(
        n="12",
        slug="contexto-cultural-y-social",
        titulo="Contexto cultural y social",
        tesis=(
            "Las decisiones de compra ocurren dentro de normas sociales, expectativas de rol y hábitos "
            "locales. En Chile eso incluye desde la desconfianza hacia la letra chica —heredada de casos "
            "públicos de abuso— hasta la importancia del boca a boca en gremios pequeños y la sensibilidad al "
            "trato en la atención. Ignorar ese contexto produce campañas técnicamente correctas y "
            "socialmente sordas. Considerarlo no significa estereotipar: significa verificar qué normas "
            "operan en el segmento concreto."
        ),
        conceptos=[
            ("norma social relevante", "expectativa compartida en el grupo del cliente que condiciona qué es aceptable comprar o decir"),
            ("grupo de referencia", "conjunto de personas cuya opinión el cliente considera al evaluar una decisión"),
            ("prueba social local", "evidencia de adopción proveniente de pares reconocibles del mismo contexto"),
            ("sensibilidad contextual", "capacidad de adaptar mensaje y práctica a la norma sin perder consistencia de marca"),
        ],
        metodo=[
            "identificar el grupo de referencia del segmento",
            "documentar normas y expectativas observadas, no supuestas",
            "revisar mensajes y prácticas contra esas normas",
            "usar prueba social local y verificable",
            "medir diferencias de respuesta por contexto",
        ],
        senales=[
            ("respuesta por origen geográfico o gremial", "tasa de respuesta y conversión segmentada por región y por rubro"),
            ("efecto de la prueba social local", "diferencia de conversión entre piezas con referencias del mismo rubro y piezas genéricas"),
            ("participación de referidos por gremio", "oportunidades originadas por referencia dentro del mismo gremio, sobre oportunidades del gremio"),
        ],
        caso=(
            "La campaña nacional de Ruta Andina usa testimonios de Santiago. En regiones la conversión es 42 % "
            "menor y las entrevistas muestran que los prospectos no reconocen a ninguno de los casos citados."
        ),
        limite=(
            "El contexto explica tendencias, no individuos. Usar rasgos culturales para predecir el "
            "comportamiento de una persona concreta es un error y puede ser discriminatorio."
        ),
        libros=["solomon", "sharp2", "cialdini", "godin"],
        error=("Trasladar mensajes de un contexto a otro sin verificar",
               "Prueba la pieza con al menos cinco personas del contexto de destino antes de escalarla."),
    ),
    dict(
        n="13",
        slug="segmentos-conductuales",
        titulo="Segmentos conductuales",
        tesis=(
            "Segmentar por comportamiento observado —frecuencia, recencia, gasto, uso de funcionalidades, "
            "canal de origen— suele predecir mejor que segmentar por atributos declarados. La razón es "
            "simple: el comportamiento ya ocurrió y está registrado, mientras que la intención declarada es "
            "una promesa. La segmentación conductual permite además accionar: se puede construir una lista, "
            "medir un efecto y comparar cohortes."
        ),
        conceptos=[
            ("segmento conductual", "grupo definido por acciones registradas y no por características declaradas"),
            ("recencia, frecuencia y valor", "tres dimensiones básicas de comportamiento de compra que ordenan la base de clientes"),
            ("cohorte", "conjunto de clientes que comparten el mismo periodo de inicio y que se sigue en el tiempo"),
            ("accionabilidad del segmento", "posibilidad real de alcanzar y tratar de forma distinta a ese grupo"),
        ],
        metodo=[
            "definir las acciones que se registrarán como señal",
            "construir los segmentos con datos existentes",
            "verificar que cada segmento sea alcanzable y suficientemente grande",
            "diseñar un tratamiento distinto por segmento",
            "medir el efecto diferencial y descartar segmentos sin respuesta",
        ],
        senales=[
            ("tamaño y estabilidad del segmento", "clientes en el segmento y porcentaje que permanece en él entre dos periodos consecutivos"),
            ("diferencial de respuesta", "diferencia de conversión o retención entre segmentos ante el mismo tratamiento"),
            ("valor promedio por segmento", "ingreso y margen promedio por cliente en cada segmento conductual"),
        ],
        caso=(
            "Ruta Andina segmenta por rubro. Al segmentar por uso del módulo de pagos aparece una división más "
            "predictiva: quienes lo activan en las dos primeras semanas retienen 3,2 veces más."
        ),
        limite=(
            "Los segmentos conductuales cambian con el producto: cada cambio relevante de funcionalidad puede "
            "invalidar la segmentación y obliga a recalcularla."
        ),
        libros=["fader", "croll-yoskovitz", "kaushik", "flint"],
        error=("Crear segmentos que no se pueden alcanzar",
               "Verifica que exista un canal y un dato de contacto para tratar al segmento de forma distinta."),
    ),
    dict(
        n="14",
        slug="sintesis-expediente-de-cliente-accionable",
        titulo="Síntesis: expediente de cliente accionable",
        tesis=(
            "Esta clase integra la parte en un expediente único: quién es el cliente, qué progreso busca, "
            "quién decide, qué lo frena, qué riesgo percibe y qué evidencia necesita. La prueba de calidad no "
            "es la extensión sino la utilidad: un ejecutivo comercial nuevo debería poder preparar una "
            "conversación con ese documento, y un equipo de marketing debería poder escribir una pieza sin "
            "inventar nada."
        ),
        conceptos=[
            ("expediente de cliente", "documento único que integra ICP, roles, jobs, journey, fricciones y objeciones con sus fuentes"),
            ("trazabilidad de la evidencia", "posibilidad de identificar de dónde salió cada afirmación del expediente"),
            ("prueba de uso", "verificación de que una persona ajena puede tomar una decisión concreta con el documento"),
            ("ciclo de actualización", "rutina definida que mantiene el expediente vigente con datos nuevos"),
        ],
        metodo=[
            "consolidar los hallazgos de las 13 clases anteriores",
            "marcar el nivel de evidencia de cada afirmación",
            "someter el expediente a prueba de uso con una persona ajena",
            "corregir lo que no resultó accionable",
            "fijar responsable y frecuencia de actualización",
        ],
        senales=[
            ("proporción de afirmaciones con fuente", "afirmaciones con fuente y fecha, sobre afirmaciones totales del expediente"),
            ("resultado de la prueba de uso", "decisiones que la persona ajena logró tomar sin consultar, sobre decisiones planteadas"),
            ("frecuencia de uso del expediente", "referencias al expediente en materiales y guiones producidos en el trimestre"),
        ],
        caso=(
            "Ruta Andina debe incorporar dos ejecutivos comerciales el próximo mes. Hoy el conocimiento de "
            "cliente está en la cabeza de dos personas y en conversaciones de chat."
        ),
        limite=(
            "Un expediente extenso que nadie lee equivale a no tenerlo. Si excede lo que una persona puede "
            "revisar antes de una reunión, hay que producir una versión operativa de una página."
        ),
        libros=["fitzpatrick", "osterwalder-vpd", "christensen", "roberge"],
        error=("Producir un documento sin prueba de uso",
               "Entrega el expediente a alguien ajeno y verifica qué decisiones logra tomar sin ayuda."),
    ),
]
