# -*- coding: utf-8 -*-
"""Parte 09 — Venta consultiva y B2B compleja."""

CLASES = [
    dict(
        n="01",
        slug="venta-consultiva",
        titulo="Venta consultiva",
        tesis=(
            "La venta consultiva se justifica cuando el cliente no puede especificar por sí solo lo que "
            "necesita: el problema es difuso, las consecuencias son inciertas y la solución exige cambios "
            "internos. El vendedor aporta valor al estructurar el diagnóstico, no al describir el producto. "
            "Su riesgo es la consultoría gratuita indefinida: sin criterios de calificación, el modelo "
            "consume tiempo en cuentas que nunca comprarán."
        ),
        conceptos=[
            ("diagnóstico estructurado", "proceso ordenado que traduce síntomas en causas y consecuencias cuantificadas"),
            ("valor aportado en el proceso", "beneficio que el cliente obtiene de la conversación aunque no compre"),
            ("consultoría no remunerada", "trabajo de diagnóstico entregado sin contrapartida ni avance del negocio"),
            ("criterio de continuidad", "condición que debe cumplir el cliente para seguir recibiendo esfuerzo consultivo"),
        ],
        metodo=[
            "acordar el alcance del diagnóstico con el cliente",
            "estructurar síntomas, causas y consecuencias",
            "cuantificar el costo del problema con datos del cliente",
            "pedir una contrapartida proporcional al esfuerzo",
            "aplicar el criterio de continuidad antes de profundizar",
        ],
        senales=[
            ("horas consultivas por oportunidad", "horas invertidas en diagnóstico, por oportunidad y por segmento"),
            ("tasa de conversión de diagnóstico a propuesta", "propuestas emitidas, sobre diagnósticos realizados"),
            ("contrapartidas obtenidas", "oportunidades donde el cliente entregó datos, acceso o tiempo, sobre diagnósticos iniciados"),
        ],
        caso=(
            "Un ejecutivo de Ruta Andina dedicó 22 horas a diagnosticar los procesos de una cadena que nunca "
            "asignó presupuesto ni presentó el proyecto a su comité."
        ),
        limite=(
            "El modelo consultivo no cabe en tickets bajos: su costo por oportunidad puede superar el margen del "
            "primer año del contrato."
        ),
        libros=["rackham", "keenan", "dixon-challenger", "miller-heiman"],
        error=("Entregar diagnóstico completo sin contrapartida",
               "Solicita acceso a datos, participación del decisor o una sesión de trabajo antes de profundizar."),
    ),
    dict(
        n="02",
        slug="spin-selling",
        titulo="SPIN Selling",
        tesis=(
            "Rackham analizó miles de llamadas comerciales y encontró un patrón: en ventas grandes, los "
            "vendedores exitosos hacen más preguntas de implicación y de necesidad-beneficio, y menos "
            "descripciones de producto. La secuencia situación-problema-implicación-necesidad no es un guion "
            "rígido sino una progresión: primero contexto, luego dificultad, luego consecuencia y sólo "
            "entonces valor de resolver."
        ),
        conceptos=[
            ("pregunta de situación", "consulta sobre el contexto y los hechos actuales del cliente"),
            ("pregunta de problema", "consulta que hace explícita una dificultad o insatisfacción"),
            ("pregunta de implicación", "consulta que desarrolla las consecuencias del problema no resuelto"),
            ("pregunta de necesidad-beneficio", "consulta que lleva al cliente a enunciar el valor de resolverlo"),
        ],
        metodo=[
            "investigar antes para minimizar preguntas de situación",
            "identificar el problema con preguntas abiertas",
            "desarrollar implicaciones sin proponer solución",
            "conducir a que el cliente enuncie el beneficio",
            "resumir por escrito el diagnóstico acordado",
        ],
        senales=[
            ("proporción de preguntas por tipo", "preguntas de cada tipo registradas, sobre preguntas totales, en grabaciones"),
            ("enunciados de beneficio del cliente", "casos donde el cliente enuncia el valor de resolver, sobre reuniones de diagnóstico"),
            ("tasa de avance tras diagnóstico", "oportunidades que avanzan de etapa, sobre diagnósticos completados"),
        ],
        caso=(
            "Las grabaciones de Ruta Andina muestran 14 preguntas de situación y ninguna de implicación en la "
            "reunión típica. El cliente nunca dimensiona lo que pierde."
        ),
        limite=(
            "Las preguntas de situación excesivas irritan cuando la información está disponible públicamente. "
            "La investigación previa es parte del método, no un paso opcional."
        ),
        libros=["rackham", "keenan", "fitzpatrick", "dixon-challenger"],
        error=("Usar SPIN como guion literal",
               "Trátalo como progresión de objetivos: adapta la formulación y elimina lo que ya investigaste."),
    ),
    dict(
        n="03",
        slug="challenger-sale",
        titulo="Challenger Sale",
        tesis=(
            "Dixon y Adamson encontraron que el perfil comercial más efectivo en ventas complejas no es el "
            "constructor de relaciones sino el que enseña, adapta y toma el control: aporta una perspectiva "
            "que el cliente no tenía, la adapta a su realidad económica y conduce la conversación difícil de "
            "precio y de proceso. El requisito es real y exigente: sin un insight comercial verdadero, "
            "«desafiar» al cliente es sólo insolencia."
        ),
        conceptos=[
            ("insight comercial", "perspectiva basada en evidencia que cambia cómo el cliente entiende su problema"),
            ("reencuadre", "presentación del problema en términos distintos a los que el cliente traía"),
            ("adaptación económica", "traducción del insight a la realidad de costos y prioridades del cliente"),
            ("control constructivo", "capacidad de conducir la conversación de precio y proceso sin ceder ni imponer"),
        ],
        metodo=[
            "construir el insight con datos propios o de mercado",
            "reencuadrar el problema y verificar la reacción",
            "adaptar el insight a la economía del cliente",
            "conducir la conversación de decisión y proceso",
            "verificar si el reencuadre modificó el criterio del cliente",
        ],
        senales=[
            ("negocios con insight documentado", "oportunidades donde se presentó un insight verificable, sobre oportunidades trabajadas"),
            ("cambio de criterio del cliente", "casos donde el cliente incorporó un criterio nuevo, sobre reencuadres presentados"),
            ("tasa de cierre con reencuadre", "negocios ganados con reencuadre aplicado, frente a los sin reencuadre"),
        ],
        caso=(
            "Ruta Andina puede demostrar con sus datos que el costo real de las inasistencias en talleres "
            "supera al de la mano de obra ociosa: ese es un insight que el cliente no ha calculado."
        ),
        limite=(
            "El modelo exige una organización que produzca insights con evidencia. Sin ese soporte, el vendedor "
            "sólo tiene opinión y el enfoque se vuelve contraproducente."
        ),
        libros=["dixon-challenger", "dixon-customer", "rackham", "keenan"],
        error=("Desafiar sin evidencia que respalde el insight",
               "Construye el insight con datos verificables antes de cuestionar el criterio del cliente."),
    ),
    dict(
        n="04",
        slug="solution-selling",
        titulo="Solution Selling",
        tesis=(
            "La venta de soluciones organiza el proceso alrededor de la brecha entre el estado actual y el "
            "estado deseado del cliente, y compromete resultado. Su fortaleza es la alineación con el "
            "problema; su debilidad, documentada por Dixon, es que asume un cliente capaz de articular sus "
            "necesidades. Cuando el cliente no sabe qué necesita, la venta de soluciones se convierte en "
            "responder mal a un requerimiento mal formulado."
        ),
        conceptos=[
            ("estado actual", "situación operativa y económica verificable del cliente antes de la solución"),
            ("estado futuro", "resultado comprometido, expresado en métricas del cliente"),
            ("brecha", "diferencia cuantificada entre ambos estados que justifica la inversión"),
            ("requerimiento mal formulado", "petición del cliente que describe una solución en lugar del problema"),
        ],
        metodo=[
            "documentar el estado actual con datos verificables",
            "definir el estado futuro en métricas del cliente",
            "cuantificar la brecha y su valor",
            "cuestionar los requerimientos formulados como solución",
            "comprometer sólo lo que la operación puede sostener",
        ],
        senales=[
            ("brecha cuantificada por negocio", "oportunidades con brecha estimada en cifras del cliente, sobre oportunidades calificadas"),
            ("cumplimiento del estado futuro", "clientes que alcanzaron la métrica comprometida, sobre clientes implementados"),
            ("requerimientos reformulados", "casos donde el requerimiento inicial fue reformulado, sobre licitaciones y pedidos recibidos"),
        ],
        caso=(
            "Una cadena pidió a Ruta Andina «un sistema de turnos con pantalla». El problema real era la "
            "percepción de espera, que se resolvía con confirmación previa y no con hardware."
        ),
        limite=(
            "Comprometer un estado futuro que depende de la ejecución del cliente traslada un riesgo que el "
            "proveedor no controla. El compromiso debe acotarse a lo gobernable."
        ),
        libros=["keenan", "rackham", "dixon-challenger", "cagan"],
        error=("Responder al requerimiento sin cuestionar su formulación",
               "Reconstruye el problema detrás del pedido antes de cotizar la solución solicitada."),
    ),
    dict(
        n="05",
        slug="meddic-y-meddpicc",
        titulo="MEDDIC y MEDDPICC",
        tesis=(
            "MEDDIC es una lista de verificación de calificación para ventas complejas: métricas, comprador "
            "económico, criterios de decisión, proceso de decisión, dolor identificado y campeón. MEDDPICC "
            "agrega el papeleo —proceso formal— y la competencia. Su valor no está en el acrónimo sino en la "
            "obligación de escribir evidencia por cada elemento: un negocio donde tres campos están vacíos no "
            "pertenece al forecast comprometido."
        ),
        conceptos=[
            ("métrica del cliente", "indicador con el que el cliente medirá el éxito de la solución"),
            ("criterio de decisión", "conjunto de requisitos con que el cliente comparará las alternativas"),
            ("proceso de decisión", "secuencia formal de aprobaciones y plazos que el cliente debe recorrer"),
            ("campeón verificado", "persona con influencia interna que ha actuado a favor del proyecto, no sólo declarado apoyo"),
        ],
        metodo=[
            "completar cada elemento con evidencia y no con supuestos",
            "identificar los campos vacíos y planificar cómo llenarlos",
            "verificar al campeón con una acción concreta",
            "revisar el proceso formal y el papeleo requerido",
            "usar el nivel de completitud como criterio de forecast",
        ],
        senales=[
            ("completitud de calificación", "elementos con evidencia registrada, sobre elementos del marco, por oportunidad"),
            ("precisión del forecast por completitud", "tasa de cierre de negocios con alta completitud frente a baja completitud"),
            ("campeones verificados", "oportunidades con acción concreta del campeón, sobre oportunidades con campeón declarado"),
        ],
        caso=(
            "El negocio con la cadena aparece en el forecast comprometido de Ruta Andina con comprador "
            "económico desconocido, proceso de decisión sin documentar y campeón sin acción verificada."
        ),
        limite=(
            "El marco puede convertirse en burocracia si se aplica a negocios pequeños. Su uso corresponde a "
            "oportunidades cuyo valor justifica el esfuerzo de calificación."
        ),
        libros=["miller-heiman", "roberge", "dixon-customer", "rackham"],
        error=("Declarar campeón sin evidencia de acción",
               "Exige una acción concreta —agendar al decisor, compartir información interna— para validar al campeón."),
    ),
    dict(
        n="06",
        slug="bant-y-sus-limites",
        titulo="BANT y sus límites",
        tesis=(
            "BANT —presupuesto, autoridad, necesidad, plazo— nació en un contexto donde el comprador definía "
            "su necesidad y buscaba proveedor. En mercados donde la empresa debe crear la necesidad, "
            "descalificar por «no tiene presupuesto asignado» elimina oportunidades legítimas: el presupuesto "
            "aparece cuando el problema se dimensiona. BANT sigue siendo útil como verificación tardía, no "
            "como filtro de entrada."
        ),
        conceptos=[
            ("presupuesto asignado", "monto formalmente disponible para resolver ese problema en el periodo"),
            ("autoridad", "capacidad formal de comprometer el gasto"),
            ("necesidad reconocida", "problema que el cliente admite y prioriza"),
            ("momento de aplicación", "etapa del proceso en que el criterio de calificación es válido"),
        ],
        metodo=[
            "distinguir mercado de demanda existente y de demanda por crear",
            "aplicar BANT como verificación tardía",
            "usar dolor cuantificado como criterio temprano",
            "documentar la ruta de obtención de presupuesto",
            "revisar la precisión de la calificación con datos de cierre",
        ],
        senales=[
            ("negocios ganados sin presupuesto inicial", "negocios cerrados que no tenían presupuesto en la primera reunión, sobre cierres"),
            ("tiempo hasta asignación de presupuesto", "días entre el diagnóstico y la confirmación de presupuesto, mediana"),
            ("precisión de descalificación", "oportunidades descalificadas que luego compraron a un competidor, sobre descalificaciones"),
        ],
        caso=(
            "Ruta Andina descalifica automáticamente a quien no tiene presupuesto. Dos de sus tres mejores "
            "clientes actuales no lo tenían en la primera conversación."
        ),
        limite=(
            "Ignorar por completo el presupuesto produce pipeline inflado. El criterio no es abandonar BANT sino "
            "aplicarlo en el momento correcto del proceso."
        ),
        libros=["rackham", "keenan", "ross", "roberge"],
        error=("Descalificar por falta de presupuesto en el primer contacto",
               "Aplica el criterio después del dimensionamiento del problema, no antes."),
    ),
    dict(
        n="07",
        slug="buying-committee",
        titulo="Comité de compra",
        tesis=(
            "En ventas complejas la decisión rara vez la toma una persona: la toma un grupo con criterios "
            "distintos y con capacidad de bloqueo asimétrica. El trabajo comercial consiste en mapear el "
            "comité, entender el criterio de cada rol y anticipar dónde se romperá el consenso. Adamson "
            "documentó que el mayor obstáculo no es convencer a un individuo sino lograr que el grupo llegue "
            "a un acuerdo suficiente."
        ),
        conceptos=[
            ("mapa del comité", "representación de miembros, roles, criterios y postura frente al proyecto"),
            ("bloqueador", "miembro con capacidad de detener el proceso por riesgo, costo o preferencia"),
            ("punto de ruptura del consenso", "desacuerdo específico que impide que el grupo avance"),
            ("costo del no acuerdo", "consecuencia para el cliente de no tomar ninguna decisión"),
        ],
        metodo=[
            "identificar miembros, roles y criterios",
            "estimar postura y capacidad de bloqueo de cada uno",
            "detectar el punto probable de ruptura",
            "producir material específico para ese desacuerdo",
            "hacer visible el costo del no acuerdo",
        ],
        senales=[
            ("cobertura del comité", "miembros con contacto o evidencia de postura, sobre miembros identificados"),
            ("negocios detenidos por bloqueador", "oportunidades detenidas por un actor específico, sobre oportunidades estancadas"),
            ("tiempo de decisión por tamaño de comité", "días hasta la decisión, segmentados por número de participantes"),
        ],
        caso=(
            "En la cadena de 14 locales, TI exige integración con su ERP, finanzas exige plazo de pago y "
            "operaciones quiere implementar en enero. Ruta Andina trabaja sólo con operaciones."
        ),
        limite=(
            "El mapa del comité es una hipótesis: las posturas cambian y aparecen actores nuevos. Debe "
            "actualizarse en cada interacción relevante."
        ),
        libros=["dixon-customer", "miller-heiman", "rackham", "shell"],
        error=("Trabajar sólo con el contacto más accesible",
               "Planifica el acceso a cada rol crítico y registra la evidencia de su postura."),
    ),
    dict(
        n="08",
        slug="champion-y-economic-buyer",
        titulo="Champion y comprador económico",
        tesis=(
            "El campeón es quien impulsa el proyecto dentro de la organización del cliente; el comprador "
            "económico es quien autoriza el gasto. Confundirlos es el error de calificación más caro: se "
            "invierte en quien no puede decidir. Un campeón real se reconoce por sus actos —consigue "
            "reuniones, comparte información interna, defiende el proyecto en su ausencia— y no por su "
            "entusiasmo verbal."
        ),
        conceptos=[
            ("campeón", "persona interna con interés propio en el éxito del proyecto y credibilidad para defenderlo"),
            ("comprador económico", "persona con autoridad para aprobar el gasto y responsabilidad sobre el retorno"),
            ("prueba de campeón", "acción verificable que demuestra compromiso más allá de la declaración"),
            ("acceso al decisor", "posibilidad concreta de conversar con quien autoriza el gasto"),
        ],
        metodo=[
            "identificar el interés propio del campeón",
            "solicitar una acción que verifique su compromiso",
            "planificar el acceso al comprador económico",
            "preparar al campeón con material para defender el proyecto",
            "registrar la evidencia de ambos roles en el CRM",
        ],
        senales=[
            ("oportunidades con acceso al decisor", "oportunidades con al menos una conversación con el comprador económico, sobre oportunidades avanzadas"),
            ("acciones verificadas del campeón", "acciones concretas registradas, sobre campeones declarados"),
            ("tasa de cierre con y sin acceso", "tasa de cierre de negocios con acceso al decisor frente a los sin acceso"),
        ],
        caso=(
            "La jefa de operaciones de la cadena apoya el proyecto y nunca consiguió una reunión con el "
            "gerente de finanzas. El negocio lleva ocho semanas en la misma etapa."
        ),
        limite=(
            "Saltarse al campeón para llegar al decisor puede destruir la relación y el proyecto. El acceso se "
            "construye con el campeón, no a pesar de él."
        ),
        libros=["miller-heiman", "dixon-customer", "rackham", "shell"],
        error=("Confundir entusiasmo con capacidad de decisión",
               "Verifica el rol con una acción concreta y registra quién controla el presupuesto."),
    ),
    dict(
        n="09",
        slug="mapeo-de-cuentas",
        titulo="Mapeo de cuentas",
        tesis=(
            "Mapear una cuenta es entender su estructura de poder, sus prioridades declaradas, sus proyectos "
            "en curso y sus relaciones con proveedores. En cuentas grandes el mapa vale más que cualquier "
            "presentación: permite anticipar por dónde entra el proyecto, quién lo financia y qué iniciativa "
            "compite por el mismo presupuesto. Miller y Heiman formalizaron esta práctica como análisis de "
            "posición."
        ),
        conceptos=[
            ("estructura de poder", "distribución real de influencia, que no siempre coincide con el organigrama"),
            ("prioridad declarada", "objetivo público de la organización con presupuesto asociado"),
            ("competencia interna por presupuesto", "otras iniciativas que disputan el mismo fondo"),
            ("posición en la cuenta", "evaluación de la fortaleza relativa frente a competidores y frente al no hacer nada"),
        ],
        metodo=[
            "recolectar información pública y de conversaciones",
            "mapear estructura de poder y relaciones",
            "identificar prioridades con presupuesto asociado",
            "detectar iniciativas que compiten por el mismo fondo",
            "evaluar la posición y definir el movimiento siguiente",
        ],
        senales=[
            ("cobertura del mapa de cuenta", "roles críticos con información registrada, sobre roles identificados"),
            ("alineación con prioridad declarada", "oportunidades vinculadas a una prioridad con presupuesto, sobre oportunidades de la cuenta"),
            ("participación en la cuenta", "ingreso propio en la cuenta, sobre gasto estimado de la cuenta en la categoría"),
        ],
        caso=(
            "Ruta Andina descubre que la cadena está ejecutando un proyecto de punto de venta que consume el "
            "presupuesto de tecnología del año. Su propuesta compite con ese proyecto sin saberlo."
        ),
        limite=(
            "La información de cuenta debe obtenerse por medios legítimos. Presionar a empleados para obtener "
            "información confidencial es una práctica indebida y un riesgo legal."
        ),
        libros=["miller-heiman", "dixon-customer", "porter", "shell"],
        error=("Proponer sin conocer las iniciativas que compiten por el presupuesto",
               "Pregunta explícitamente qué otros proyectos disputan el mismo fondo y en qué estado están."),
    ),
    dict(
        n="10",
        slug="account-based-selling",
        titulo="Account-based selling",
        tesis=(
            "El enfoque basado en cuentas concentra recursos de marketing y ventas en un número acotado de "
            "organizaciones seleccionadas por su valor potencial. Su lógica es de eficiencia: en mercados "
            "donde diez cuentas representan la mitad del potencial, tratarlas como leads genéricos desperdicia "
            "la oportunidad. Su exigencia es alta: requiere coordinación real entre marketing y ventas y "
            "materiales específicos por cuenta."
        ),
        conceptos=[
            ("cuenta objetivo", "organización seleccionada por potencial y ajuste, con plan propio"),
            ("plan de cuenta", "documento con objetivos, actores, mensajes y acciones específicas para esa organización"),
            ("coordinación marketing-ventas", "trabajo conjunto sobre la misma lista con métricas compartidas"),
            ("penetración de cuenta", "grado de contacto y de participación logrado dentro de la organización objetivo"),
        ],
        metodo=[
            "seleccionar cuentas por potencial y ajuste con criterios escritos",
            "construir un plan por cuenta con actores y mensajes",
            "coordinar acciones de marketing y ventas sobre la misma lista",
            "medir penetración y avance por cuenta",
            "revisar la lista con datos de resultado cada trimestre",
        ],
        senales=[
            ("penetración por cuenta", "contactos activos en la cuenta, sobre roles críticos identificados"),
            ("avance de cuentas objetivo", "cuentas que avanzaron de etapa, sobre cuentas objetivo del periodo"),
            ("costo por cuenta objetivo", "inversión total de marketing y ventas asignada, dividido por cuentas trabajadas"),
        ],
        caso=(
            "Ruta Andina identificó 12 cadenas que representan el 40 % del potencial de su región. Hoy las "
            "trata igual que a los 900 talleres de su base de correos."
        ),
        limite=(
            "El enfoque exige capacidad. Con un equipo de tres personas, más de 15 o 20 cuentas objetivo "
            "produce planes que nadie ejecuta."
        ),
        libros=["miller-heiman", "ross", "dixon-customer", "bertuzzi"],
        error=("Declarar cuentas objetivo sin plan ni recursos asignados",
               "Limita la lista a lo que el equipo puede trabajar y exige plan escrito por cuenta."),
    ),
    dict(
        n="11",
        slug="rfp-y-procesos-formales",
        titulo="RFP y procesos formales",
        tesis=(
            "Responder una licitación cuyas bases fueron escritas con otro proveedor en mente es una forma "
            "cara de perder. La decisión de participar debe tomarse con criterios: si la empresa no influyó "
            "en las bases, no conoce al comprador económico y no puede diferenciarse dentro del formato, la "
            "probabilidad es baja. Cuando se participa, la disciplina de cumplimiento formal es "
            "innegociable."
        ),
        conceptos=[
            ("criterio de participación", "condiciones que deben cumplirse para invertir en responder"),
            ("influencia en las bases", "grado en que la empresa contribuyó a definir los requisitos"),
            ("cumplimiento formal", "satisfacción exacta de requisitos administrativos que habilitan la evaluación"),
            ("costo de responder", "horas y gastos que consume la preparación de la respuesta"),
        ],
        metodo=[
            "evaluar el criterio de participación antes de decidir",
            "identificar quién influyó en las bases",
            "verificar el cumplimiento formal antes del contenido",
            "diferenciarse dentro del formato permitido",
            "registrar el resultado y calibrar el criterio",
        ],
        senales=[
            ("tasa de adjudicación", "procesos ganados, sobre procesos en que se participó"),
            ("costo por respuesta", "horas y gastos por proceso, comparados con el valor esperado del contrato"),
            ("rechazos por incumplimiento formal", "ofertas descartadas por requisitos administrativos, sobre ofertas presentadas"),
        ],
        caso=(
            "Ruta Andina perdió tres licitaciones municipales por no adjuntar boleta de garantía. Ninguna "
            "evaluación llegó a revisar su propuesta técnica."
        ),
        limite=(
            "En compras públicas hay reglas estrictas de igualdad de trato y transparencia. Intentar influir en "
            "las bases fuera de los mecanismos formales es una infracción, no una técnica comercial."
        ),
        libros=["miller-heiman", "shell", "porter", "malhotra-neg"],
        error=("Participar en todo proceso que aparece",
               "Aplica el criterio de participación y documenta por qué se responde o no a cada licitación."),
    ),
    dict(
        n="12",
        slug="procurement-y-compras",
        titulo="Procurement y compras",
        tesis=(
            "El área de compras tiene incentivos propios: reducir precio, estandarizar condiciones y reducir "
            "riesgo de proveedor. No es un obstáculo sino un actor con criterios legítimos. La estrategia "
            "adecuada es doble: construir valor con el área usuaria antes de que compras intervenga, y llegar "
            "a la negociación con criterios objetivos —costo total, riesgo, plazos— y no sólo con precio."
        ),
        conceptos=[
            ("incentivo de compras", "objetivo con que se mide al área, normalmente ahorro y control de riesgo"),
            ("costo total de propiedad", "suma de precio, implementación, operación, cambio y salida durante la vida del contrato"),
            ("estandarización de condiciones", "presión por aplicar términos uniformes a todos los proveedores"),
            ("momento de intervención", "etapa en que compras entra al proceso y su efecto en el margen"),
        ],
        metodo=[
            "construir valor con el área usuaria antes de la intervención de compras",
            "preparar el costo total de propiedad con evidencia",
            "identificar los criterios con que se evalúa a compras",
            "negociar sobre criterios objetivos y no sólo precio",
            "documentar los acuerdos y sus condiciones",
        ],
        senales=[
            ("descuento exigido por compras", "diferencia entre precio ofrecido y precio final en negocios con intervención de compras"),
            ("negocios con costo total presentado", "oportunidades con análisis de costo total entregado, sobre oportunidades con compras"),
            ("plazo adicional por intervención", "días adicionales al ciclo cuando interviene compras, mediana"),
        ],
        caso=(
            "El área de compras de la cadena exige 30 % de descuento, pago a 90 días y exclusividad. El "
            "vendedor de Ruta Andina ya adelantó que «hay espacio para conversar»."
        ),
        limite=(
            "En algunas organizaciones compras tiene mandato absoluto sobre el precio. Ahí la palanca está en "
            "el costo total y en el riesgo, no en el descuento."
        ),
        libros=["fisher-ury", "malhotra-neg", "nagle", "shell"],
        error=("Anticipar concesiones antes de que las pidan",
               "Nunca declares margen disponible; prepara contrapartidas y criterios objetivos antes de negociar."),
    ),
    dict(
        n="13",
        slug="negocios-enterprise",
        titulo="Negocios enterprise",
        tesis=(
            "Un negocio enterprise combina ciclo largo, comité amplio, requisitos formales de seguridad y "
            "legales, y un valor que justifica todo ese esfuerzo. Su gestión exige plan mutuo, seguimiento "
            "estructurado, involucramiento de dirección y una evaluación honesta del costo de servir. Muchas "
            "empresas medianas ganan un contrato enterprise y descubren que no pueden sostenerlo."
        ),
        conceptos=[
            ("plan mutuo", "cronograma acordado con el cliente que detalla pasos, responsables y fechas hasta la firma"),
            ("requisito de habilitación", "condición técnica, legal o de seguridad que el proveedor debe cumplir para ser aceptado"),
            ("costo de servir enterprise", "recursos adicionales de soporte, cumplimiento y gestión que exige la cuenta"),
            ("riesgo de concentración", "dependencia excesiva del ingreso total en una sola cuenta"),
        ],
        metodo=[
            "evaluar si la empresa puede cumplir los requisitos de habilitación",
            "construir el plan mutuo con el cliente",
            "estimar el costo de servir completo",
            "involucrar a dirección en los hitos críticos",
            "evaluar el riesgo de concentración antes de firmar",
        ],
        senales=[
            ("cumplimiento de hitos del plan mutuo", "hitos cumplidos en fecha, sobre hitos acordados"),
            ("costo de servir de la cuenta", "horas y gastos atribuibles a la cuenta, sobre su ingreso"),
            ("concentración de ingreso", "ingreso de la mayor cuenta, sobre ingreso total de la empresa"),
        ],
        caso=(
            "La cadena representaría el 23 % del ingreso de Ruta Andina y exige disponibilidad 24/7, algo que "
            "la empresa no tiene ni ha costeado."
        ),
        limite=(
            "Un contrato enterprise mal costeado puede consumir la capacidad completa de la empresa y degradar "
            "el servicio al resto de la base."
        ),
        libros=["miller-heiman", "dixon-customer", "mehta", "zoltners"],
        error=("Firmar sin costear los requisitos de servicio",
               "Calcula el costo de cumplir los niveles de servicio exigidos antes de comprometer el contrato."),
    ),
    dict(
        n="14",
        slug="deal-review-completo",
        titulo="Deal review completo",
        tesis=(
            "Esta clase integra la parte en una revisión de negocio estructurada: diagnóstico, mapa de "
            "comité, calificación con evidencia, plan mutuo, riesgos y decisión de continuar o abandonar. La "
            "prueba de calidad es incómoda por diseño: la revisión debe poder concluir que el negocio no "
            "debe seguir trabajándose."
        ),
        conceptos=[
            ("revisión de negocio", "sesión estructurada que evalúa la posición real de una oportunidad con evidencia"),
            ("evidencia frente a supuesto", "distinción explícita entre lo verificado y lo asumido en el negocio"),
            ("decisión de abandono", "conclusión legítima de dejar de invertir tiempo en la oportunidad"),
            ("plan de acción", "conjunto de pasos con responsable y fecha derivados de la revisión"),
        ],
        metodo=[
            "presentar el diagnóstico y su evidencia",
            "revisar comité, calificación y proceso de decisión",
            "identificar los tres supuestos más riesgosos",
            "decidir continuar, ajustar o abandonar",
            "registrar el plan de acción con responsables y fechas",
        ],
        senales=[
            ("negocios revisados con evidencia completa", "revisiones con todos los elementos documentados, sobre revisiones realizadas"),
            ("tasa de abandono en revisión", "oportunidades cerradas tras la revisión, sobre oportunidades revisadas"),
            ("mejora de precisión del forecast", "diferencia entre forecast y resultado real, antes y después de instaurar revisiones"),
        ],
        caso=(
            "Ruta Andina debe revisar el negocio con la cadena antes del cierre trimestral. El forecast lo "
            "considera comprometido y tres elementos de calificación siguen vacíos."
        ),
        limite=(
            "Una revisión que se convierte en interrogatorio destruye la información: el vendedor aprende a "
            "ocultar. El propósito es mejorar la posición, no juzgar personas."
        ),
        libros=["miller-heiman", "roberge", "grove", "ellet"],
        error=("Usar la revisión para presionar en lugar de decidir",
               "Establece que una conclusión válida de la revisión es abandonar el negocio sin costo político."),
    ),
]
