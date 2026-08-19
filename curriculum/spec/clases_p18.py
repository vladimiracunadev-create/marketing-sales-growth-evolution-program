# -*- coding: utf-8 -*-
"""Parte 18 — Customer experience, success y fidelización."""

CLASES = [
    dict(
        n="01",
        slug="experiencia-de-cliente",
        titulo="Experiencia de cliente",
        tesis=(
            "La experiencia de cliente es la suma de percepciones acumuladas en todas las interacciones, "
            "incluidas las que la empresa no diseñó: una factura confusa, un cobro inesperado, una espera. "
            "Dixon y su equipo mostraron que el motor principal de lealtad no es el deleite sino la "
            "reducción de esfuerzo: los clientes castigan la fricción más de lo que premian la sorpresa. "
            "Eso reordena las prioridades de inversión."
        ),
        conceptos=[
            ("experiencia acumulada", "percepción formada por el conjunto de interacciones a lo largo de la relación"),
            ("esfuerzo del cliente", "cantidad de pasos, tiempo y energía que exige resolver algo"),
            ("interacción no diseñada", "punto de contacto que existe sin haber sido considerado por la empresa"),
            ("deleite frente a reducción de esfuerzo", "comparación entre superar expectativas y eliminar fricción"),
        ],
        metodo=[
            "inventariar todos los puntos de contacto, incluidos los administrativos",
            "medir el esfuerzo percibido en los críticos",
            "priorizar la eliminación de fricción sobre la sorpresa",
            "corregir primero lo que produce contacto no deseado",
            "medir el efecto en retención y en volumen de soporte",
        ],
        senales=[
            ("esfuerzo percibido", "puntuación declarada por el cliente tras una interacción, con escala uniforme"),
            ("contactos evitables", "consultas causadas por procesos deficientes, sobre consultas totales"),
            ("relación esfuerzo-retención", "retención comparada entre clientes con alto y bajo esfuerzo declarado"),
        ],
        caso=(
            "Ruta Andina invirtió en un programa de regalos de bienvenida mientras su proceso de cambio de "
            "datos de facturación exige tres correos y cinco días."
        ),
        limite=(
            "Reducir esfuerzo tiene un piso: algunas verificaciones son necesarias por seguridad o por norma. "
            "El objetivo es eliminar la fricción que no protege a nadie."
        ),
        libros=["dixon-effort", "reichheld", "krug", "mehta"],
        error=("Invertir en deleite antes de eliminar fricción",
               "Identifica los contactos evitables y corrige sus causas antes de agregar gestos de sorpresa."),
    ),
    dict(
        n="02",
        slug="onboarding",
        titulo="Onboarding",
        tesis=(
            "El onboarding decide gran parte de la retención futura. Su objetivo no es que el cliente conozca "
            "el producto sino que obtenga un primer resultado. Hulick lo formula con precisión: el usuario no "
            "quiere aprender la herramienta, quiere lograr algo. Un onboarding que enseña funcionalidades sin "
            "producir un resultado deja al cliente informado y sin razón para volver."
        ),
        conceptos=[
            ("primer resultado", "logro concreto que el cliente obtiene y reconoce como valioso"),
            ("hito de activación", "acción que marca el inicio del uso efectivo del producto"),
            ("carga cognitiva", "cantidad de información nueva que el cliente debe procesar al inicio"),
            ("abandono temprano", "cliente que deja de usar antes de alcanzar el primer resultado"),
        ],
        metodo=[
            "definir cuál es el primer resultado para cada segmento",
            "identificar el camino más corto hacia él",
            "eliminar todo lo que no conduzca a ese resultado",
            "medir la tasa de activación y el tiempo hasta el primer resultado",
            "intervenir donde se concentra el abandono temprano",
        ],
        senales=[
            ("tasa de activación", "clientes que alcanzan el hito de activación, sobre clientes incorporados"),
            ("tiempo hasta el primer resultado", "días entre la firma y el primer resultado verificado, mediana"),
            ("abandono en los primeros 30 días", "bajas en el primer mes, sobre incorporaciones del periodo"),
        ],
        caso=(
            "El 61 % de las bajas de Ruta Andina nunca completó la carga inicial de datos. El onboarding "
            "consiste en un video de 40 minutos que recorre todos los módulos."
        ),
        limite=(
            "Un onboarding demasiado guiado puede frustrar a usuarios avanzados. Conviene ofrecer una ruta "
            "rápida además de la guiada."
        ),
        libros=["hulick", "mehta", "cagan", "dixon-effort"],
        error=("Enseñar funcionalidades en lugar de producir un resultado",
               "Define el primer resultado por segmento y elimina del onboarding todo lo que no conduzca a él."),
    ),
    dict(
        n="03",
        slug="time-to-value",
        titulo="Time to value",
        tesis=(
            "El tiempo hasta el primer valor es el indicador más predictivo de retención en modelos "
            "recurrentes. Cada día adicional aumenta la probabilidad de que el cliente pierda impulso, cambie "
            "de prioridad o encuentre otra solución. Reducirlo suele exigir decisiones incómodas: eliminar "
            "pasos de configuración, ofrecer plantillas por defecto o asumir parte del trabajo inicial."
        ),
        conceptos=[
            ("primer valor", "momento en que el cliente obtiene un beneficio verificable del producto"),
            ("tiempo hasta el primer valor", "días entre la contratación y ese momento"),
            ("bloqueador de implementación", "obstáculo que retrasa la obtención del primer valor"),
            ("valor por defecto", "configuración inicial que produce beneficio sin trabajo del cliente"),
        ],
        metodo=[
            "definir el evento que representa el primer valor",
            "medir el tiempo actual por segmento",
            "identificar los bloqueadores más frecuentes",
            "reducir el trabajo inicial exigido al cliente",
            "verificar el efecto sobre retención a 90 días",
        ],
        senales=[
            ("tiempo hasta el primer valor", "días entre contratación y primer valor, mediana por segmento"),
            ("bloqueadores por implementación", "obstáculos registrados, sobre implementaciones iniciadas"),
            ("retención por tiempo hasta el valor", "retención a 90 días, comparada entre tramos de tiempo hasta el valor"),
        ],
        caso=(
            "Los clientes de Ruta Andina que activan el módulo de pagos en las dos primeras semanas retienen "
            "3,2 veces más. El proceso actual toma en promedio 34 días."
        ),
        limite=(
            "Acelerar la implementación puede trasladar costo a la empresa. La decisión requiere comparar ese "
            "costo contra el valor de la retención adicional."
        ),
        libros=["hulick", "mehta", "croll-yoskovitz", "cagan"],
        error=("Delegar en el cliente todo el trabajo de configuración",
               "Ofrece configuraciones por defecto y asume los pasos que bloquean el primer valor."),
    ),
    dict(
        n="04",
        slug="customer-success",
        titulo="Customer Success",
        tesis=(
            "Customer Success es una función proactiva orientada a que el cliente alcance el resultado por el "
            "que pagó. Se distingue del soporte, que es reactivo y resuelve incidencias. Confundirlos "
            "produce equipos que apagan incendios y no previenen bajas. Su diseño exige definir cartera, "
            "criterios de intervención y responsabilidad sobre renovación y expansión."
        ),
        conceptos=[
            ("función proactiva", "trabajo iniciado por el proveedor antes de que el cliente reporte un problema"),
            ("resultado del cliente", "beneficio comprometido expresado en la métrica del cliente"),
            ("modelo de cobertura", "forma de atender la cartera: dedicada, agrupada o digital"),
            ("responsabilidad sobre renovación", "asignación explícita de quién responde por la continuidad de la cuenta"),
        ],
        metodo=[
            "definir el resultado esperado por segmento",
            "elegir el modelo de cobertura según valor de la cuenta",
            "establecer criterios de intervención proactiva",
            "asignar responsabilidad sobre renovación y expansión",
            "medir resultado acreditado y no actividad",
        ],
        senales=[
            ("cuentas con resultado acreditado", "cuentas con evidencia de resultado logrado, sobre cuentas activas"),
            ("proporción de contactos proactivos", "interacciones iniciadas por la empresa, sobre interacciones totales"),
            ("retención neta por modelo de cobertura", "ingreso neto retenido, comparado entre modelos de atención"),
        ],
        caso=(
            "El equipo de éxito de cliente de Ruta Andina dedica el 92 % de su tiempo a resolver tickets. "
            "Nadie ha definido qué significa que una cuenta esté bien."
        ),
        limite=(
            "El modelo dedicado no es viable para cuentas de ticket bajo. Para esos segmentos, la alternativa "
            "es cobertura digital con intervención por excepción."
        ),
        libros=["mehta", "fader", "reichheld", "dixon-effort"],
        error=("Medir éxito de cliente por tickets resueltos",
               "Sustituye el indicador por resultado acreditado y retención neta de la cartera."),
    ),
    dict(
        n="05",
        slug="health-score",
        titulo="Health score",
        tesis=(
            "Un puntaje de salud estima el riesgo de baja combinando uso, resultado, relación y señales "
            "comerciales. Su valor depende de la validación: un puntaje que no predice la baja produce falsa "
            "tranquilidad. La construcción correcta parte de analizar qué distinguió a las cuentas que se "
            "fueron de las que se quedaron, y no de una ponderación inventada en una reunión."
        ),
        conceptos=[
            ("componente de uso", "señal de actividad en el producto que refleja adopción real"),
            ("componente de resultado", "evidencia de que el cliente logra el beneficio comprometido"),
            ("validación predictiva", "contraste entre el puntaje asignado y la baja efectiva"),
            ("umbral de intervención", "nivel de puntaje que activa una acción definida"),
        ],
        metodo=[
            "analizar qué distinguió a las cuentas perdidas",
            "construir el puntaje con esos componentes",
            "validar su capacidad predictiva con datos históricos",
            "definir umbrales y acciones asociadas",
            "recalibrar cada semestre con datos nuevos",
        ],
        senales=[
            ("capacidad predictiva del puntaje", "tasa de baja en el tramo de riesgo alto frente al tramo bajo"),
            ("cobertura de la intervención", "cuentas en riesgo con acción ejecutada, sobre cuentas en riesgo"),
            ("bajas sin señal previa", "bajas de cuentas clasificadas como sanas, sobre bajas totales"),
        ],
        caso=(
            "El puntaje de salud de Ruta Andina se calcula con la percepción del ejecutivo. El 44 % de las "
            "bajas del último trimestre estaba clasificado como saludable."
        ),
        limite=(
            "Un puntaje predictivo sin capacidad de intervención sólo anticipa la pérdida. Debe existir una "
            "acción posible para cada nivel de riesgo."
        ),
        libros=["mehta", "provost", "fader", "croll-yoskovitz"],
        error=("Construir el puntaje con percepciones del equipo",
               "Deriva los componentes del análisis de cuentas perdidas y valida su capacidad predictiva."),
    ),
    dict(
        n="06",
        slug="nps-csat-y-ces",
        titulo="NPS, CSAT y CES",
        tesis=(
            "Cada indicador de percepción responde una pregunta distinta: la recomendación probable, la "
            "satisfacción con una interacción específica y el esfuerzo requerido. Reichheld advierte contra "
            "el uso más común y más dañino: convertir el NPS en meta de compensación, lo que induce a "
            "manipular la pregunta en lugar de mejorar el servicio. Su valor está en el comentario y en la "
            "acción posterior, no en el número."
        ),
        conceptos=[
            ("indicador de recomendación", "medida de la disposición declarada a recomendar"),
            ("satisfacción transaccional", "evaluación de una interacción específica y reciente"),
            ("indicador de esfuerzo", "medida de la dificultad percibida para resolver algo"),
            ("cierre del circuito", "acción de responder al cliente sobre lo que se hizo con su comentario"),
        ],
        metodo=[
            "elegir el indicador según la pregunta a responder",
            "aplicar con método y momento consistentes",
            "priorizar el análisis del comentario abierto",
            "cerrar el circuito con quien respondió",
            "evitar vincular el indicador a compensación individual",
        ],
        senales=[
            ("tasa de respuesta", "respuestas obtenidas, sobre encuestas enviadas, por punto de medición"),
            ("proporción de comentarios accionables", "comentarios con acción derivada, sobre comentarios recibidos"),
            ("tasa de cierre de circuito", "clientes contactados tras responder, sobre respondentes con comentario"),
        ],
        caso=(
            "Ruta Andina mide NPS trimestral y publica el número en la reunión. Nadie lee los comentarios ni "
            "contacta a quienes puntuaron bajo."
        ),
        limite=(
            "Los indicadores de percepción tienen sesgo de respuesta: contestan quienes tienen una opinión "
            "intensa. No representan a la base completa."
        ),
        libros=["reichheld", "dixon-effort", "mehta", "malhotra"],
        error=("Convertir el indicador en meta de compensación",
               "Usa el indicador para diagnosticar y actuar; nunca lo vincules a incentivo individual."),
    ),
    dict(
        n="07",
        slug="churn",
        titulo="Churn",
        tesis=(
            "El churn se mide de varias formas —de clientes, de ingreso, bruto y neto— y cada una responde "
            "una pregunta distinta. Confundirlas produce diagnósticos falsos: una empresa puede perder pocas "
            "cuentas y mucho ingreso si las que se van son las grandes. Además, el motivo declarado rara vez "
            "es el real: la causa suele estar meses antes, en la venta o en el onboarding."
        ),
        conceptos=[
            ("churn de clientes", "cuentas perdidas sobre cuentas activas al inicio del periodo"),
            ("churn de ingreso", "ingreso recurrente perdido sobre ingreso recurrente al inicio del periodo"),
            ("motivo declarado frente a causa raíz", "distinción entre lo que el cliente dice y lo que originó la baja"),
            ("cohorte de baja", "grupo de clientes que se dio de baja en el mismo periodo de incorporación"),
        ],
        metodo=[
            "definir y calcular cada tipo de churn por separado",
            "analizar por cohorte de incorporación y por segmento",
            "recoger motivo declarado y buscar la causa raíz",
            "identificar el momento del proceso donde se originó",
            "intervenir en el origen y no en el síntoma",
        ],
        senales=[
            ("churn de ingreso mensual", "ingreso recurrente perdido, sobre ingreso recurrente al inicio del mes"),
            ("churn por cohorte", "tasa de baja por cohorte de incorporación, seguida en el tiempo"),
            ("concentración de bajas por segmento", "bajas del segmento, sobre bajas totales, comparado con su peso en la base"),
        ],
        caso=(
            "Ruta Andina pierde 3,4 % de cuentas al mes. El churn de ingreso es 5,1 % porque las cuentas que "
            "se van son las de mayor facturación."
        ),
        limite=(
            "Reducir el churn a cero no es un objetivo razonable: algunos clientes nunca debieron ser "
            "vendidos. La meta correcta considera la calidad del cliente ganado."
        ),
        libros=["mehta", "fader", "croll-yoskovitz", "reichheld"],
        error=("Reportar sólo churn de clientes",
               "Calcula churn de clientes y de ingreso por separado y analiza por cohorte y segmento."),
    ),
    dict(
        n="08",
        slug="retention",
        titulo="Retención",
        tesis=(
            "La retención es el motor silencioso de los modelos recurrentes: una mejora de dos puntos "
            "porcentuales puede valer más que un aumento equivalente en adquisición, porque compone. "
            "Trabajarla exige distinguir sus componentes: activación insuficiente, valor no percibido, "
            "problemas de servicio y decisiones ajenas al proveedor, como el cierre del negocio del cliente."
        ),
        conceptos=[
            ("curva de retención", "evolución de la proporción de clientes activos a lo largo del tiempo"),
            ("retención estabilizada", "nivel en que la curva se aplana y deja de caer"),
            ("componente controlable", "causa de baja sobre la que la empresa puede actuar"),
            ("efecto compuesto", "acumulación del beneficio de retener a lo largo de varios periodos"),
        ],
        metodo=[
            "construir curvas de retención por cohorte y segmento",
            "separar causas controlables de las que no lo son",
            "estimar el valor de una mejora de dos puntos",
            "intervenir sobre la causa controlable dominante",
            "medir el efecto en la curva de las cohortes posteriores",
        ],
        senales=[
            ("retención a 3, 6 y 12 meses", "clientes activos en cada hito, sobre clientes de la cohorte inicial"),
            ("nivel de estabilización", "porcentaje en que la curva de retención se aplana, por segmento"),
            ("valor de la mejora", "ingreso adicional estimado de una mejora de dos puntos en retención"),
        ],
        caso=(
            "Las cohortes de Ruta Andina caen sin estabilizarse hasta el mes 9. Ninguna cohorte muestra el "
            "aplanamiento que indicaría un núcleo de clientes con encaje."
        ),
        limite=(
            "La retención tiene un techo determinado por la categoría y por el ciclo de vida del cliente. "
            "Compararse con referencias de otra industria induce metas irreales."
        ),
        libros=["fader", "mehta", "croll-yoskovitz", "ellis-brown"],
        error=("Trabajar retención sin separar causas controlables",
               "Clasifica las bajas por causa y concentra el esfuerzo en las que la empresa puede modificar."),
    ),
    dict(
        n="09",
        slug="cohortes",
        titulo="Análisis de cohortes",
        tesis=(
            "El análisis de cohortes agrupa clientes por periodo de incorporación y sigue su comportamiento "
            "en el tiempo. Es la herramienta que revela si la empresa está mejorando: si cada cohorte nueva "
            "retiene mejor que la anterior, algo está funcionando. Los promedios agregados esconden "
            "exactamente esa información, porque mezclan clientes con antigüedades distintas."
        ),
        conceptos=[
            ("cohorte", "grupo de clientes que comparte el periodo de incorporación"),
            ("seguimiento longitudinal", "observación del mismo grupo a lo largo de varios periodos"),
            ("efecto de mezcla", "distorsión del promedio provocada por la combinación de cohortes distintas"),
            ("mejora entre cohortes", "diferencia de comportamiento entre grupos incorporados en periodos sucesivos"),
        ],
        metodo=[
            "definir el criterio de cohorte y la métrica a seguir",
            "construir la tabla de cohortes con datos propios",
            "comparar cohortes sucesivas en el mismo hito",
            "atribuir las diferencias a cambios conocidos",
            "usar el análisis para evaluar intervenciones",
        ],
        senales=[
            ("retención por cohorte en el mismo hito", "retención al mes N, comparada entre cohortes sucesivas"),
            ("ingreso acumulado por cohorte", "ingreso acumulado por cliente de cada cohorte, a lo largo del tiempo"),
            ("tendencia entre cohortes", "dirección y magnitud del cambio entre cohortes consecutivas"),
        ],
        caso=(
            "El promedio de retención de Ruta Andina se mantiene estable. Al analizar por cohorte se ve que "
            "las cohortes recientes retienen peor y el promedio se sostiene por las antiguas."
        ),
        limite=(
            "Las cohortes recientes tienen poca historia y sus proyecciones son inciertas. Comparar sólo en "
            "hitos con datos completos evita conclusiones falsas."
        ),
        libros=["croll-yoskovitz", "fader", "provost", "kaushik"],
        error=("Evaluar retención con promedios agregados",
               "Compara cohortes sucesivas en el mismo hito de antigüedad."),
    ),
    dict(
        n="10",
        slug="renewal",
        titulo="Renovación",
        tesis=(
            "La renovación no es un evento administrativo: es la evaluación que hace el cliente sobre si el "
            "gasto se justifica. Gestionarla exige anticipación —el trabajo empieza meses antes—, evidencia "
            "del resultado obtenido y una conversación honesta sobre lo que no funcionó. Enterarse de un "
            "riesgo en la semana del vencimiento significa que el sistema de salud de cuenta no funciona."
        ),
        conceptos=[
            ("ciclo de renovación", "secuencia de actividades que precede al vencimiento del contrato"),
            ("evidencia de resultado", "documentación del beneficio obtenido durante el periodo"),
            ("riesgo de renovación", "probabilidad estimada de no continuidad, detectada con anticipación"),
            ("renovación automática informada", "continuidad sujeta al deber de informar y a la facilidad de cancelar"),
        ],
        metodo=[
            "iniciar el ciclo con anticipación suficiente",
            "documentar la evidencia del resultado obtenido",
            "detectar y trabajar los riesgos identificados",
            "sostener la conversación de valor antes del vencimiento",
            "cumplir el deber de información sobre la renovación",
        ],
        senales=[
            ("tasa de renovación", "contratos renovados, sobre contratos con vencimiento en el periodo"),
            ("anticipación del ciclo", "días entre el inicio de la gestión y el vencimiento, mediana"),
            ("renovaciones con evidencia de resultado", "renovaciones con documentación de resultado, sobre renovaciones gestionadas"),
        ],
        caso=(
            "Ruta Andina gestiona la renovación la semana previa al vencimiento. El 38 % de las cuentas ya "
            "tomó su decisión antes de esa conversación."
        ),
        limite=(
            "La renovación automática es legítima si se informa con claridad y la cancelación es simple. "
            "Dificultar la baja para retener produce reclamos y sanciones."
        ),
        libros=["mehta", "reichheld", "fader-ltv", "dixon-effort"],
        error=("Gestionar la renovación en la semana del vencimiento",
               "Inicia el ciclo con al menos 90 días de anticipación y documenta la evidencia de resultado."),
    ),
    dict(
        n="11",
        slug="expansion-revenue",
        titulo="Ingreso por expansión",
        tesis=(
            "La expansión —más usuarios, más módulos, más locales— es la fuente de crecimiento más eficiente "
            "porque opera sobre clientes que ya confían. Su condición es no negociable: el resultado inicial "
            "debe estar cumplido. Vender expansión sobre una base insatisfecha adelanta ingreso y multiplica "
            "el churn futuro, porque amplía la exposición del cliente a un producto que no le sirve."
        ),
        conceptos=[
            ("expansión legítima", "aumento de ingreso en una cuenta que obtuvo el resultado comprometido"),
            ("señal de expansión", "indicio de uso o crecimiento que sugiere una oportunidad ampliada"),
            ("ingreso neto retenido", "ingreso del mismo grupo de clientes tras bajas, contracciones y expansiones"),
            ("expansión prematura", "venta adicional sobre una cuenta que aún no logra el resultado inicial"),
        ],
        metodo=[
            "verificar el resultado inicial antes de proponer",
            "identificar señales de expansión con datos de uso",
            "diseñar la propuesta desde el resultado obtenido",
            "medir el ingreso neto retenido por cohorte",
            "prohibir la expansión sobre cuentas en riesgo",
        ],
        senales=[
            ("ingreso neto retenido", "ingreso del mismo grupo 12 meses después, sobre ingreso inicial"),
            ("tasa de expansión", "cuentas con aumento de ingreso, sobre cuentas activas del periodo"),
            ("churn posterior a expansión", "bajas de cuentas expandidas, comparadas con las no expandidas"),
        ],
        caso=(
            "Ruta Andina vendió módulos adicionales a 30 cuentas para cumplir la meta del trimestre. Doce de "
            "ellas estaban clasificadas en riesgo y ocho se dieron de baja en 90 días."
        ),
        limite=(
            "La expansión tiene un techo natural por tamaño del cliente. Presionarla más allá deteriora la "
            "relación y produce contracción en el ciclo siguiente."
        ),
        libros=["mehta", "fader-ltv", "croll-yoskovitz", "reichheld"],
        error=("Expandir sobre cuentas en riesgo",
               "Exige resultado inicial acreditado y estado saludable antes de habilitar cualquier venta adicional."),
    ),
    dict(
        n="12",
        slug="advocacy-y-referidos",
        titulo="Advocacy y referidos",
        tesis=(
            "Un cliente que recomienda entrega credibilidad que ninguna campaña compra. Convertir esa "
            "disposición en un flujo sistemático exige identificar a quienes obtuvieron resultado, pedir en "
            "el momento adecuado y facilitar el acto. La tentación de incentivar económicamente debe "
            "manejarse con cuidado: un incentivo no declarado convierte la recomendación en publicidad "
            "encubierta."
        ),
        conceptos=[
            ("promotor", "cliente con resultado acreditado y disposición a recomendar"),
            ("momento de la petición", "instante en que el cliente acaba de reconocer el valor obtenido"),
            ("facilitación de la referencia", "material y proceso que reducen el esfuerzo de referir"),
            ("transparencia del incentivo", "declaración de cualquier beneficio entregado por la recomendación"),
        ],
        metodo=[
            "identificar promotores con evidencia de resultado",
            "definir el momento de la petición",
            "facilitar el acto con material listo",
            "declarar cualquier incentivo entregado",
            "medir conversión y agradecer el resultado",
        ],
        senales=[
            ("proporción de clientes que refieren", "clientes con al menos una referencia en 12 meses, sobre clientes activos"),
            ("conversión de referidos", "referidos convertidos en clientes, sobre referidos recibidos"),
            ("costo por cliente referido", "costo del programa, dividido por clientes ganados por referencia"),
        ],
        caso=(
            "El 21 % del margen de Ruta Andina viene de referidos y no existe ningún proceso para "
            "solicitarlos. Llegan por iniciativa espontánea de los clientes."
        ),
        limite=(
            "Un programa de referidos mal diseñado puede incentivar recomendaciones de baja calidad que "
            "deterioran la conversión y la confianza."
        ),
        libros=["reichheld", "cialdini", "mehta", "godin"],
        error=("Incentivar referencias sin declarar el beneficio",
               "Declara cualquier incentivo en la comunicación pública de la referencia."),
    ),
    dict(
        n="13",
        slug="voice-of-customer-continuo",
        titulo="Voice of Customer continuo",
        tesis=(
            "Escuchar al cliente una vez al año produce una foto; escuchar de forma continua produce una "
            "película. El sistema continuo combina encuestas transaccionales, análisis de tickets, "
            "entrevistas de baja y observación de uso. Su valor aparece cuando la información llega a quien "
            "puede actuar y se cierra el circuito con quien la entregó."
        ),
        conceptos=[
            ("captura continua", "recolección permanente de la voz del cliente en múltiples puntos"),
            ("entrevista de baja", "conversación estructurada con quien se va, para identificar causa raíz"),
            ("enrutamiento a decisión", "mecanismo que lleva el hallazgo a quien puede modificar el producto o el proceso"),
            ("sesgo de quienes hablan", "sobrerrepresentación de opiniones intensas en los canales abiertos"),
        ],
        metodo=[
            "definir los puntos de captura y su periodicidad",
            "estructurar la entrevista de baja y ejecutarla siempre",
            "clasificar los hallazgos con taxonomía estable",
            "enrutar a responsables con capacidad de actuar",
            "cerrar el circuito y medir el efecto de los cambios",
        ],
        senales=[
            ("cobertura de entrevistas de baja", "bajas con entrevista realizada, sobre bajas totales"),
            ("hallazgos con acción asignada", "hallazgos con responsable y acción, sobre hallazgos registrados"),
            ("cambios implementados por voz de cliente", "modificaciones de producto o proceso originadas en el sistema, por trimestre"),
        ],
        caso=(
            "Ruta Andina no entrevista a quienes se van. El motivo registrado en el CRM es «precio» en el 70 "
            "% de los casos porque es la primera opción del formulario."
        ),
        limite=(
            "Quien se fue puede no querer conversar y quien responde puede racionalizar. La entrevista aporta "
            "hipótesis, que deben contrastarse con datos de comportamiento."
        ),
        libros=["portigal", "mehta", "dixon-effort", "reichheld"],
        error=("Registrar el motivo de baja con una lista cerrada",
               "Ejecuta entrevistas estructuradas y contrasta el motivo declarado con datos de uso previos."),
    ),
    dict(
        n="14",
        slug="sistema-de-retencion-y-expansion",
        titulo="Sistema de retención y expansión",
        tesis=(
            "Esta clase integra la parte en un sistema: onboarding con primer resultado definido, salud de "
            "cuenta validada, ciclo de renovación anticipado, expansión condicionada y voz de cliente "
            "continua. La prueba de calidad es predictiva: el sistema debe permitir anticipar las bajas del "
            "próximo trimestre con un margen de error conocido."
        ),
        conceptos=[
            ("sistema de retención", "conjunto de procesos, indicadores y responsables que sostiene la base de clientes"),
            ("capacidad predictiva", "anticipación de las bajas con un margen de error conocido"),
            ("responsabilidad por cartera", "asignación explícita de quién responde por cada grupo de cuentas"),
            ("ritmo de revisión", "calendario de revisiones de salud, riesgo y renovación"),
        ],
        metodo=[
            "consolidar onboarding, salud, renovación y expansión",
            "asignar responsabilidad por cartera",
            "establecer el ritmo de revisión",
            "validar la capacidad predictiva del sistema",
            "medir ingreso neto retenido como resultado agregado",
        ],
        senales=[
            ("ingreso neto retenido", "ingreso del mismo grupo 12 meses después, sobre ingreso inicial"),
            ("precisión de la predicción de bajas", "diferencia entre bajas previstas y observadas, por trimestre"),
            ("cuentas con responsable asignado", "cuentas con dueño definido, sobre cuentas activas"),
        ],
        caso=(
            "Ruta Andina debe llevar su ingreso neto retenido de 84 % a más de 100 % en 12 meses. Hoy no "
            "puede anticipar qué cuentas se irán el próximo trimestre."
        ),
        limite=(
            "Un sistema de retención no compensa un problema de encaje: si el segmento no obtiene valor, la "
            "solución está en la calificación comercial y en el producto."
        ),
        libros=["mehta", "fader-ltv", "reichheld", "croll-yoskovitz"],
        error=("Construir el sistema sin validar su capacidad predictiva",
               "Compara las bajas previstas con las observadas cada trimestre y recalibra el modelo."),
    ),
]
