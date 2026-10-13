# -*- coding: utf-8 -*-
"""Ampliaciones transversales de clases existentes.

La numeración y la arquitectura curricular permanecen intactas. Cada entrada
agrega una subsección pedagógica a su clase principal y declara referencias
cruzadas para evitar repetir la misma explicación en varias partes.
"""


def metrica(nombre, numerador, denominador, ventana, fuente, responsable, lectura, limite):
    return dict(
        nombre=nombre,
        numerador=numerador,
        denominador=denominador,
        ventana=ventana,
        fuente=fuente,
        responsable=responsable,
        lectura=lectura,
        limite=limite,
    )


def ia(objetivo, datos, prompt, resultado, validacion, riesgos, alternativa):
    return dict(
        objetivo=objetivo,
        datos=datos,
        prompt=prompt,
        resultado=resultado,
        validacion=validacion,
        riesgos=riesgos,
        limites="La salida es una hipótesis de trabajo; no constituye investigación, predicción ni decisión validada por sí sola.",
        alternativa=alternativa,
    )


AMPLIACIONES = {
    "05.02": [dict(
        eje="A", titulo="Creación, percepción y captura de valor",
        conceptos=[
            ("valor percibido", "balance subjetivo y contextual entre beneficios esperados y sacrificios percibidos por quien decide"),
            ("sacrificio percibido", "precio monetario más costos de transacción, aprendizaje, cambio y riesgos financieros, funcionales o reputacionales"),
            ("valor creado", "beneficio total que la oferta hace posible para cliente, organización y otras partes afectadas"),
            ("valor capturado", "porción del valor creado que la empresa retiene como ingreso, margen, aprendizaje o activo estratégico"),
        ],
        teoria=[
            "El modelo `valor percibido = beneficios percibidos − sacrificios percibidos` ordena la conversación, pero no es una fórmula monetaria universal. La percepción depende del rol, la alternativa, el momento y la confianza: sumar una garantía puede mover más valor que agregar una funcionalidad, y un costo de migración puede anular una ventaja de precio.",
            "Distingue característica, ventaja y beneficio. Una característica describe la oferta; una ventaja compara su mecanismo con una alternativa; un beneficio expresa el resultado para el cliente. El análisis debe separar beneficios funcionales, emocionales, sociales y económicos, y comprobar si el valor creado permite capturar margen sin destruir confianza ni sostenibilidad.",
        ],
        marco=[
            ("Beneficio intrínseco", "resultado producido por el uso", "medir desempeño o resultado observado"),
            ("Beneficio extrínseco", "señal externa, servicio o conveniencia", "probar si cambia elección o permanencia"),
            ("Beneficio simbólico", "identidad, pertenencia o reputación", "investigar lenguaje y contexto, no inferirlo"),
            ("Sacrificio total", "precio, tiempo, aprendizaje, cambio y riesgo", "hacer visibles costos fuera de la factura"),
            ("Captura sostenible", "ingreso y margen compatibles con resultado y confianza", "contrastar disposición a pagar, costo de servir y retención"),
        ],
        actividad=dict(
            consigna="Compara tres ofertas de Ruta Andina: A cuesta CLP 39.000 con autoservicio y migración manual; B cuesta CLP 89.000 con migración asistida, capacitación y garantía de puesta en marcha; C cuesta CLP 69.000 con más funciones, contrato anual y soporte sólo por correo.",
            pasos=["puntuar beneficios por rol sin mezclarlos", "estimar precio, transacción, aprendizaje, cambio y riesgos", "declarar incertidumbre y sensibilidad", "recomendar por segmento, no una ganadora universal"],
            solucion="Para una pyme sin personal administrativo, B puede superar a C pese al mayor precio: reduce migración, aprendizaje y riesgo de interrupción. Para un equipo técnico con datos limpios, C podría capturar más valor. A domina sólo si la capacidad interna vuelve tolerable el sacrificio operativo. La respuesta correcta es condicional y separa precio de costo total percibido.",
            evidencia="matriz de tres ofertas, supuestos por rol, recomendación y dato que podría invertirla",
            rubrica="30 % distinción beneficio/sacrificio; 25 % evidencia; 25 % trade-off valor/precio/margen; 20 % límites y transferencia",
        ),
        metricas=[metrica("tasa de valor validado", "beneficios priorizados confirmados con conducta o resultado", "beneficios priorizados sometidos a prueba", "por cohorte y trimestre", "entrevistas, pilotos, uso y CRM", "Product Marketing", "compara qué beneficios sostienen elección y permanencia", "no convierte percepciones en equivalentes monetarios ni demuestra causalidad")],
        ia=ia("comparar propuestas sin inventar evidencia", "matriz anonimizada de beneficios, sacrificios y fuente de cada celda", "Actúa como revisor escéptico. Compara A, B y C por rol. Marca cada afirmación como dato, inferencia o hipótesis; no completes celdas faltantes. Devuelve sensibilidad y preguntas para validar.", "tabla de comparación y agenda de validación", "un responsable contrasta cada celda con la fuente y rehace el cálculo", "falsa precisión, preferencia inducida por el prompt y exposición de precios sensibles", "usar una hoja de cálculo con ponderaciones y revisión por pares"),
        transferencias=["B2C: conveniencia y riesgo percibido", "B2B: costo total, adopción y veto", "B2G: trazabilidad, continuidad y cumplimiento"],
        referencias=["01.06", "07.04", "13.05", "18.03"],
    )],
    "02.04": [dict(
        eje="B", titulo="Buyer Persona como hipótesis, investigación y sistema vivo",
        conceptos=[
            ("persona hipotética", "perfil provisional compuesto por supuestos marcados que todavía no tiene evidencia suficiente"),
            ("persona sustentada", "patrón respaldado por evidencia cualitativa y cuantitativa trazable"),
            ("persona validada", "perfil revisado contra conducta posterior, casos negativos y una fecha de actualización"),
            ("segmentación contextual", "agrupación por circunstancia de decisión, uso o restricción, no sólo por rasgos estables"),
        ],
        teoria=[
            "Segmento, ICP y Buyer Persona responden preguntas distintas: el segmento agrupa un mercado, el ICP prioriza organizaciones con ajuste y rentabilidad, y la persona modela patrones de roles humanos dentro de una decisión. En B2B y B2G deben convivir usuario, comprador, decisor, prescriptor y veto; en B2C también pueden separarse comprador, usuario y pagador.",
            "Las variables demográficas, geográficas, psicográficas, conductuales y contextuales sólo entran si cambian targeting, posicionamiento, canal, experiencia u oferta. Se busca evidencia sobre motivaciones, aspiraciones, frustraciones, necesidades explícitas y latentes, hábitos, criterios, objeciones y fuentes de información. La IA puede organizar evidencia; nunca fabricar entrevistas ni presentar síntesis simuladas como hallazgos reales.",
        ],
        marco=[
            ("Hipotético", "supuestos y datos secundarios", "usar para planificar investigación, no para afirmar mercado"),
            ("Sustentado", "patrones con citas, conteos, fuente y casos discordantes", "adaptar mensajes y oferta con confianza declarada"),
            ("Validado", "conducta observada y revisión temporal", "incorporar a targeting y operación con monitoreo"),
            ("Caducado", "cambio de mercado o evidencia contradictoria", "suspender uso y revalidar"),
        ],
        actividad=dict(
            consigna="Clasifica 20 afirmaciones de la persona actual de Ruta Andina como evidencia, inferencia o supuesto; elimina rasgos decorativos y diseña una muestra que incluya ganados, perdidos, abandonos y no compradores.",
            pasos=["separar segmento, ICP y roles", "vincular cada atributo a una fuente", "buscar sesgo de selección", "definir criterio de validación y caducidad"],
            solucion="Una edad sin efecto en la decisión se elimina; la objeción de migración se conserva si aparece en citas trazables y pérdidas; la preferencia de canal queda como hipótesis hasta contrastarla con conducta. El nivel final se asigna atributo por atributo, no a la ficha completa.",
            evidencia="matriz atributo–fuente–estado–decisión–próxima validación",
            rubrica="25 % distinciones; 30 % trazabilidad y representatividad; 25 % accionabilidad; 20 % caducidad y límites",
        ),
        metricas=[metrica("proporción de atributos validados", "atributos con dos fuentes convergentes y conducta posterior compatible", "atributos accionables de la ficha", "revisión trimestral o cambio de mercado", "repositorio de investigación, CRM y analítica", "Research Lead", "indica madurez del perfil y dónde investigar", "no mide representatividad del mercado por sí sola")],
        ia=ia("agrupar patrones provisionales", "extractos anonimizados con identificador, fecha y contexto", "Agrupa sólo afirmaciones presentes. Para cada patrón cita los identificadores que lo sostienen, casos contrarios y nivel de confianza. No inventes frecuencias ni atributos.", "mapa provisional de patrones y contradicciones", "dos investigadores recodifican una muestra y revisan desacuerdos", "alucinación, homogeneización de minorías y filtración de datos personales", "codificación manual con tabla de afinidad"),
        transferencias=["consumidor final", "pequeña empresa", "comité corporativo", "comprador institucional"],
        referencias=["02.01", "02.05", "02.06", "04.01", "04.06"],
    )],
    "03.03": [dict(
        eje="C", titulo="Entrevistas comerciales e investigación del cliente",
        conceptos=[
            ("entrevista no dirigida", "conversación donde el entrevistador explora conducta pasada sin conducir hacia su solución"),
            ("pregunta de seguimiento", "indagación que pide ejemplo, secuencia, costo, actor o consecuencia de una respuesta"),
            ("codificación temática", "asignación reproducible de etiquetas a fragmentos para identificar patrones y excepciones"),
            ("triangulación", "contraste de un hallazgo con métodos, fuentes o investigadores diferentes"),
        ],
        teoria=[
            "La guía reutilizable parte de diez áreas: día típico, desafíos, características relevantes, formación, trayectoria, fuentes de información, forma de compra, elección de proveedor, valor esperado y objetivo de la compra. No se recitan como encuesta: se formulan sobre un episodio real y se profundizan con «¿qué ocurrió después?», «¿quién participó?» y «¿qué evidencia conserva?».",
            "SPIN sirve en discovery comercial; JTBD reconstruye la cronología del cambio; la entrevista de problema explora severidad y alternativas. Encuestas cuantifican patrones definidos, focus groups observan interacción social y la observación contextual detecta trabajo invisible. El diseño declara propósito exploratorio, descriptivo o causal; ninguna entrevista aislada demuestra causalidad.",
        ],
        marco=[
            ("Abrir", "propósito, consentimiento, uso y derecho a detenerse", "obtener permiso antes de registrar"),
            ("Reconstruir", "episodio, secuencia, actores, alternativas y consecuencias", "escuchar y seguir evidencia"),
            ("Profundizar", "situación, problema, implicación, necesidad y fuerzas JTBD", "evitar vender durante la exploración"),
            ("Analizar", "códigos, patrones, casos negativos y saturación", "preservar citas y trazabilidad"),
            ("Triangular", "CRM, analítica, encuesta u observación", "declarar convergencia y contradicción"),
        ],
        actividad=dict(
            consigna="Realiza una simulación de 25 minutos sobre la última compra de software de una pyme. Usa las diez áreas, cinco seguimientos y una secuencia SPIN o JTBD; después codifica sin incluir nombres ni datos identificables.",
            pasos=["preparar consentimiento", "preguntar por conducta pasada", "registrar señales de compra y contradicciones", "codificar por dos personas", "triangular una conclusión"],
            solucion="La síntesis suficiente distingue cita de interpretación, conserva un caso que contradice el patrón, declara cobertura de la muestra y convierte el hallazgo en una hipótesis de decisión, no en una verdad poblacional.",
            evidencia="guion, registro anonimizado, libro de códigos, tabla de hallazgos y memo de límites",
            rubrica="20 % consentimiento; 25 % calidad de preguntas y escucha; 25 % codificación; 20 % triangulación; 10 % privacidad",
        ),
        metricas=[metrica("cobertura de perspectivas", "roles y estados de relación entrevistados", "roles y estados definidos en el plan muestral", "por ronda de investigación", "registro de reclutamiento", "Research Lead", "muestra qué voces faltan", "no convierte una muestra intencional en representativa"), metrica("saturación temática declarada", "entrevistas consecutivas sin tema accionable nuevo", "entrevistas consecutivas revisadas", "ventana móvil de cinco entrevistas", "libro de códigos", "Research Lead", "ayuda a decidir si seguir recolectando", "depende del alcance y no prueba exhaustividad")],
        ia=ia("asistir la codificación temática", "transcripciones anonimizadas y consentimiento compatible con el uso", "Codifica fragmentos con este libro de códigos. Devuelve cita, código, confianza, alternativa y caso contradictorio. No infieras atributos sensibles.", "borrador auditable de codificación", "revisión humana fragmento por fragmento y acuerdo entre codificadores", "datos sensibles, pérdida de contexto y sesgo de confirmación", "codificar manualmente en una hoja compartida"),
        transferencias=["entrevista remota", "discovery comercial", "investigación de abandono", "inteligencia competitiva con fuentes públicas"],
        referencias=["02.03", "03.04", "03.05", "09.02", "21.03"],
    )],
    "02.14": [dict(
        eje="D", titulo="Ficha integral de Buyer Persona sustentada en evidencia",
        conceptos=[
            ("nivel de confianza del hallazgo", "grado explícito de respaldo según cantidad, calidad, convergencia y vigencia de la evidencia"),
            ("cita verificable", "fragmento anonimizado enlazado al registro consentido del que proviene"),
            ("factor de abandono", "condición observable asociada a no iniciar, no adoptar o terminar la relación"),
            ("mensaje por evidencia", "afirmación comercial cuyo beneficio, lenguaje y límite derivan de hallazgos trazables"),
        ],
        teoria=[
            "La ficha integral registra identificador y contexto, antecedentes relevantes, objetivos, necesidades, desafíos, frustraciones, motivaciones, canales, hábitos, criterios, objeciones, citas verificables, confianza, mensaje, propuesta de valor, elevator pitch, evidencia, hipótesis, fecha, rol decisional, recorrido, atención, abandono, servicio, sensibilidad al precio y beneficios esperados. Cada campo admite `no aplica` o `sin evidencia`; nunca relleno imaginado.",
            "Los ejemplos cambian por contexto: consumidor final enfatiza uso, riesgo y conveniencia; pequeña empresa mezcla usuario y pagador; comprador corporativo separa champion, finanzas, seguridad y procurement; comprador institucional exige bases, presupuesto, transparencia y continuidad. La misma plantilla preserva comparabilidad sin fingir que los procesos son iguales.",
        ],
        marco=[
            ("Consumidor final", "persona, hogar, ocasión y sensibilidad", "probar comprensión, confianza y recompra"),
            ("Pequeña empresa", "dueño-operador, caja, tiempo y adopción", "mostrar costo total y puesta en marcha"),
            ("Corporativo", "comité, riesgo, integración y business case", "evidencia distinta por rol"),
            ("Institucional", "mandato, compra formal, trazabilidad y continuidad", "alinear valor público y cumplimiento"),
        ],
        actividad=dict(
            consigna="Construye cuatro fichas mínimas para Ruta Andina usando la misma evidencia base y marca qué campos cambian por tipo de comprador. Escribe un mensaje y un elevator pitch que no excedan lo que sostienen las fuentes.",
            pasos=["completar campos con fuente", "marcar confianza e hipótesis", "separar roles decisionales", "adaptar propuesta y pitch", "programar revisión"],
            solucion="Una ficha corporativa no hereda la sensibilidad al precio del usuario; una institucional no usa una cita de pyme como evidencia equivalente. El pitch menciona resultado, mecanismo y límite. Los campos sin evidencia quedan visibles como backlog de investigación.",
            evidencia="cuatro fichas, matriz de diferencias y registro de hipótesis pendientes",
            rubrica="30 % completitud razonada; 30 % trazabilidad; 20 % distinción por contexto; 20 % mensaje y límites",
        ),
        metricas=[metrica("calidad de ficha Buyer Persona", "puntos logrados en completitud, trazabilidad, vigencia, contradicciones y accionabilidad", "puntos posibles de la rúbrica", "en cada revisión trimestral", "ficha y repositorio de evidencia", "Product Marketing", "prioriza brechas concretas de investigación", "una nota alta no garantiza representatividad ni eficacia comercial")],
        ia=ia("proponer huecos y contradicciones de la ficha", "campos y fuentes anonimizadas", "Revisa esta ficha. No completes datos. Enumera contradicciones, campos sin fuente, hipótesis y preguntas de validación por rol decisional.", "lista priorizada de brechas", "el propietario de investigación decide qué preguntas son pertinentes", "atributos inventados y estereotipos", "revisión cruzada con la lista de campos y las fuentes"),
        transferencias=["B2C", "pyme", "enterprise", "B2G"],
        referencias=["02.04", "02.06", "02.07", "05.02", "09.07"],
    )],
    "05.11": [dict(
        eje="E", titulo="Desarrollo y gestión estratégica de productos",
        conceptos=[
            ("experiencia–propósito–oportunidad", "intersección entre experiencia observada, cambio que el producto pretende causar y oportunidad viable de negocio"),
            ("Product Discovery", "reducción continua de riesgo de valor, usabilidad, factibilidad y viabilidad antes y durante la entrega"),
            ("Product Delivery", "construcción, despliegue y operación confiable de cambios priorizados"),
            ("gobierno de producto", "derechos de decisión, criterios, evidencia y cadencias que conectan estrategia, roadmap, backlog y retiro"),
        ],
        teoria=[
            "La experiencia actual revela fricciones; el propósito delimita qué cambio merece producirse; la oportunidad exige un segmento, resultado, disposición a cambiar y economía viable. Ninguna de las tres piezas basta sola. La estrategia de producto declara visión, misión, problema, ventaja, modelo y decisiones que no se tomarán.",
            "Discovery y Delivery son trabajos conectados, no fases que se entregan documentos. El roadmap expresa resultados y supuestos; el backlog ordena opciones de trabajo. Se prioriza por valor, esfuerzo, riesgo e impacto, con stakeholders y requerimientos trazables. Marketing, ventas, implementación, operaciones y posventa participan antes del lanzamiento, y adopción, uso, rentabilidad y retiro cierran el ciclo.",
        ],
        marco=[
            ("Descubrir", "problema, necesidad y experiencia actual", "entrevistas, observación y datos de uso"),
            ("Definir", "propósito, segmento, resultado y oportunidad", "estrategia y criterios de no hacer"),
            ("Probar", "prototipo, MVP, concepto y viabilidad comercial", "compromiso y aprendizaje validado"),
            ("Entregar", "backlog, requerimientos, calidad y operación", "incrementos utilizables y observables"),
            ("Gestionar", "adopción, portafolio, rentabilidad y retiro", "decisiones periódicas con evidencia"),
        ],
        actividad=dict(
            consigna="Convierte la petición «construir IA para agendar» en un roadmap de resultados para Ruta Andina. Define problema, propósito, oportunidad, cuatro riesgos, MVP, backlog priorizado, GTM, adopción y criterio de retiro.",
            pasos=["formular resultado", "mapear riesgos y stakeholders", "comparar prototipo, concierge y desarrollo", "priorizar con valor/esfuerzo/riesgo/impacto", "conectar lanzamiento y posventa"],
            solucion="El primer hito no es una función de IA sino reducir el tiempo de confirmación sin aumentar errores. Un servicio manual puede probar valor; el backlog nace de fallas observadas. Ventas no promete antes de la listeza, soporte define escalamiento y el retiro se activa si uso, seguridad o margen no alcanzan umbrales.",
            evidencia="product brief, mapa de riesgos, roadmap de resultados, backlog y plan de retiro",
            rubrica="25 % problema y oportunidad; 25 % evidencia y riesgos; 20 % priorización; 20 % integración comercial-operativa; 10 % retiro",
        ),
        metricas=[metrica("adopción del resultado de producto", "cuentas objetivo que completan la conducta de valor", "cuentas objetivo habilitadas", "cohortes de 30 y 90 días", "eventos de producto y CRM", "Product Manager", "compara adopción por segmento y versión", "uso no demuestra por sí solo valor, causalidad ni rentabilidad")],
        ia=ia("redactar y cuestionar opciones de roadmap", "evidencia anonimizada, restricciones y criterios", "Genera tres opciones de experimento para el resultado indicado. Para cada una declara hipótesis, riesgo que reduce, costo aproximado, criterio de refutación y dependencia. No priorices sin datos.", "opciones comparables, no un roadmap definitivo", "producto, tecnología, ventas, operaciones y riesgo revisan supuestos", "optimizar por texto plausible y filtrar estrategia confidencial", "taller presencial con matriz valor–esfuerzo–riesgo–impacto"),
        transferencias=["producto físico", "producto digital", "servicio", "portafolio híbrido"],
        referencias=["05.03", "05.04", "05.05", "05.09", "19.10", "22.09"],
    )],
    "03.10": [dict(
        eje="F", titulo="Entorno de negocios y estrategia competitiva",
        conceptos=[
            ("PESTEL", "barrido estructurado de factores políticos, económicos, sociales, tecnológicos, ambientales y legales que pueden cambiar una decisión"),
            ("cinco fuerzas", "análisis de rivalidad, entrantes, sustitutos y poder de compradores y proveedores que condiciona rentabilidad"),
            ("ventaja competitiva", "sistema de actividades difícil de replicar que permite costo menor, diferenciación o enfoque sostenible"),
            ("modelo de negocio", "lógica conectada de propuesta de valor, clientes, actividades, recursos, socios, costos e ingresos"),
        ],
        teoria=[
            "PESTEL detecta cambios externos; las cinco fuerzas explican presiones sobre la rentabilidad; las estrategias genéricas obligan a elegir costo, diferenciación o enfoque y sus actividades coherentes. Un listado de tendencias no es estrategia hasta que cambia una asignación, un riesgo o una hipótesis.",
            "El Business Model Canvas conecta propuesta de valor y modelo de ingresos con capacidades y costos. La inteligencia de mercado y el benchmarking comparan alternativas y mecanismos, no copian funcionalidades. El análisis influye en producto, precio, canal, marca, barreras, entrada y crecimiento; marca, producto y empresa se distinguen para diseñar una arquitectura coherente.",
        ],
        marco=[
            ("Entorno", "PESTEL con evidencia, horizonte y probabilidad", "registrar impacto y señal temprana"),
            ("Industria", "fuerzas, barreras, sustitutos y poder", "identificar mecanismo sobre margen"),
            ("Posición", "costo, diferenciación o enfoque", "verificar sistema de actividades"),
            ("Modelo", "valor, ingresos, costos y capacidades", "hacer análisis de sensibilidad"),
            ("Riesgo", "escenario, exposición y reversibilidad", "decidir entrar, probar, asociarse o abandonar"),
        ],
        actividad=dict(
            consigna="Construye para Ruta Andina un PESTEL de seis hechos, un mapa de cinco fuerzas y dos modelos de negocio alternativos. Elige una estrategia y muestra qué producto, canal o segmento se descarta.",
            pasos=["citar hechos", "traducirlos a mecanismos", "comparar escenarios", "elegir sistema de actividades", "definir señales de revisión"],
            solucion="Una nueva exigencia de datos no es sólo amenaza legal: puede elevar barreras si Ruta Andina convierte cumplimiento en capacidad. Competir por costo sin escala es incoherente; el enfoque en pymes reguladas puede justificar onboarding y soporte especializados, siempre que margen y tamaño accesible lo sostengan.",
            evidencia="memo PESTEL, mapa de fuerzas, Canvas comparados y recomendación con descarte",
            rubrica="25 % fuentes y mecanismos; 25 % análisis competitivo; 25 % coherencia del modelo; 25 % decisión y riesgos",
        ),
        metricas=[metrica("señales externas con respuesta definida", "señales PESTEL con umbral, responsable y acción", "señales externas priorizadas", "revisión mensual y escenario trimestral", "registro de inteligencia de mercado", "Strategy Lead", "mide preparación para escenarios", "no predice que los escenarios ocurrirán")],
        ia=ia("ordenar evidencia competitiva", "fuentes públicas con fecha y jurisdicción", "Clasifica estas evidencias en PESTEL y cinco fuerzas. Distingue hecho, inferencia y supuesto; cita el identificador de origen y propone una evidencia que refute cada inferencia.", "matriz auditable de entorno", "el analista abre las fuentes primarias y verifica vigencia", "fuentes obsoletas, contenido promocional y alucinación de competidores", "matriz manual y revisión por especialista sectorial"),
        transferencias=["mercado local", "expansión regional", "categoría regulada", "plataforma multilateral"],
        referencias=["01.03", "04.08", "06.07", "22.02", "22.10"],
    )],
    "01.09": [dict(
        eje="G", titulo="Marketing estratégico y táctico integrado",
        conceptos=[
            ("orientación de marketing", "lógica dominante que prioriza producto, cliente, relación, datos o automatización al decidir"),
            ("marketing mix 7P", "decisiones coordinadas sobre producto, precio, plaza, promoción, personas, procesos y evidencia física"),
            ("omnicanalidad", "diseño coherente de información, identidad, contexto y continuidad entre puntos de contacto"),
            ("alineación marketing–ventas", "acuerdo operativo sobre segmento, definiciones, traspasos, capacidad, feedback y resultados"),
        ],
        teoria=[
            "La evolución desde orientación al producto hacia cliente, relación, datos, digital e IA no elimina los enfoques anteriores: cambia cuándo dominan y qué riesgos introducen. La estrategia elige segmento, resultado y posición; la táctica coordina el mix. Campañas, contenido y demanda ejecutan esa elección, no la sustituyen.",
            "4P alcanza para una oferta simple; 7P hace visibles personas, procesos y evidencia física en servicios. La distribución y los canales deben cuadrar con margen y experiencia. La medición conecta actividad, conversión, calidad, ingreso y retención sin repetir el detalle de marketing digital cubierto en las partes 12–14.",
        ],
        marco=[
            ("STP", "segmentar, priorizar y posicionar", "fijar foco y diferencia"),
            ("Oferta", "producto/servicio y precio", "conectar resultado, disposición y margen"),
            ("Acceso", "plaza, canal y proceso", "hacer comprable y entregable la promesa"),
            ("Comunicación", "promoción, contenido y marca", "explicar valor con evidencia"),
            ("Experiencia", "personas y evidencia física", "cumplir la promesa en cada contacto"),
        ],
        actividad=dict(
            consigna="Diseña un mix 7P para el plan municipal de Ruta Andina y compáralo con el plan pyme. Indica tres decisiones que marketing no puede tomar sin ventas, operaciones o producto.",
            pasos=["reafirmar STP", "diseñar 7P coherentes", "mapear canales y capacidad", "definir traspasos", "conectar indicadores con decisiones"],
            solucion="El plan institucional requiere proceso de compra, evidencia, implementación y continuidad distintos; no basta cambiar el anuncio. Si ventas no puede cubrir licitaciones o soporte no puede cumplir SLA, promoción adicional empeora el sistema.",
            evidencia="tabla 7P comparada, mapa omnicanal, SLA marketing–ventas y árbol de resultados",
            rubrica="25 % coherencia STP; 25 % mix; 20 % canales; 20 % alineación; 10 % medición",
        ),
        metricas=[metrica("conversión aceptada por ventas", "oportunidades aceptadas que cumplen criterios", "traspasos realizados por marketing", "mes calendario por segmento", "automatización y CRM", "Revenue Operations", "mide calidad del acuerdo y del targeting", "no atribuye por sí sola ingreso a marketing")],
        ia=ia("detectar incoherencias del mix", "brief, restricciones, capacidad y evidencia sin datos personales", "Revisa estas 7P. Señala contradicciones entre promesa, precio, canal, personas y proceso. No propongas claims nuevos; formula preguntas para las celdas sin evidencia.", "lista priorizada de incoherencias", "dueños de marketing, ventas, producto y operaciones acuerdan correcciones", "recomendaciones genéricas y automatización de claims", "revisión cruzada con checklist 7P"),
        transferencias=["B2C", "venta consultiva B2B", "servicio profesional", "compra pública"],
        referencias=["04.14", "06.12", "12.12", "17.07", "22.14"],
    )],
    "05.09": [dict(
        eje="H", titulo="Ciclo de vida del producto como hipótesis de gestión",
        conceptos=[
            ("etapa de ciclo de vida", "patrón diagnosticado con adopción, crecimiento, competencia, margen y comportamiento, no edad del producto"),
            ("canibalización", "ventas o uso de una oferta nueva que desplazan una oferta propia existente"),
            ("renovación de producto", "cambio de propuesta, segmento, tecnología o modelo que busca reabrir crecimiento"),
            ("retiro gestionado", "decisión planificada de descontinuar protegiendo clientes, datos, contratos y reputación"),
        ],
        teoria=[
            "Introducción, crecimiento, madurez, saturación, declive, renovación, reposicionamiento y retiro describen patrones posibles, no una secuencia natural obligatoria. Distintos segmentos pueden estar en etapas distintas y una tecnología sustituta puede comprimirlas. La matriz BCG aporta una vista de portafolio, pero participación y crecimiento no reemplazan margen, sinergias ni opcionalidad.",
            "Cada etapa cambia inversión, riesgo, precio, canal, capacidad, innovación incremental y medición. Extender línea puede aumentar cobertura o canibalizar. La decisión se apoya en adopción, participación, retención, recompra, costos y rentabilidad; nunca en una curva dibujada sin evidencia.",
        ],
        marco=[
            ("Introducir", "aprender y reducir riesgo", "adopción inicial y time to value"),
            ("Crecer", "escalar sin degradar", "retención, capacidad y margen"),
            ("Madurar", "defender, segmentar y eficientar", "recompra, share y contribución"),
            ("Renovar", "reposicionar o sustituir", "incrementalidad y canibalización"),
            ("Retirar", "cerrar obligaciones y migrar", "cobertura de transición e incidentes"),
        ],
        actividad=dict(
            consigna="Diagnostica por separado SaaS, hardware y contratos institucionales de Ruta Andina. Propón invertir, mantener, renovar o retirar y calcula un escenario de canibalización del nuevo plan.",
            pasos=["diagnosticar con cinco evidencias", "comparar BCG con economía", "modelar canibalización", "definir estrategia por etapa", "preparar transición"],
            solucion="La edad no basta: hardware puede estar maduro y rentable; SaaS puede crecer con retención frágil; institucional puede seguir en introducción. Un plan nuevo se aprueba por ingreso y margen incremental netos del desplazamiento, no por ventas brutas.",
            evidencia="diagnóstico por línea, matriz de portafolio, escenario y plan de transición",
            rubrica="25 % diagnóstico; 25 % economía; 20 % riesgo y canibalización; 20 % estrategia; 10 % límites",
        ),
        metricas=[metrica("rentabilidad incremental de extensión", "margen incremental nuevo menos margen desplazado y costos de transición", "inversión incremental de la extensión", "cohortes de 6 y 12 meses", "facturación, costos y CRM", "Portfolio Manager", "compara extensiones con base homogénea", "depende del contrafactual y no debe usar ventas brutas como incrementalidad")],
        ia=ia("simular escenarios de portafolio", "supuestos de adopción, margen, canibalización y costos", "Calcula tres escenarios sin alterar los supuestos. Devuelve fórmulas, sensibilidad y punto donde cambia la recomendación. Marca datos faltantes.", "tabla reproducible de escenarios", "finanzas recompone una muestra y producto revisa supuestos", "falsa precisión y ocultamiento del contrafactual", "hoja de cálculo con análisis de sensibilidad"),
        transferencias=["bien durable", "SaaS", "servicio recurrente", "tecnología sustituida"],
        referencias=["05.10", "06.12", "07.12", "18.08", "20.09"],
    )],
    "07.14": [dict(
        eje="I", titulo="Pricing, monetización y rentabilidad comercial integrada",
        conceptos=[
            ("precio basado en valor", "precio establecido con evidencia de valor diferencial y disposición a pagar dentro de una arquitectura sostenible"),
            ("Revenue Management", "asignación de precio y capacidad por segmento, momento o condición con reglas y controles"),
            ("unit economics", "relación entre ingreso, costo variable, adquisición, servicio, retención y recuperación a nivel de unidad"),
            ("rentabilidad segmentada", "margen atribuible calculado por cliente, segmento o producto con alcance de costos declarado"),
        ],
        teoria=[
            "Costo, competencia y valor son lentes complementarios: costo fija viabilidad, competencia informa alternativas y valor acota captura. Elasticidad y sensibilidad no son sinónimos de disposición a pagar. Descuentos, precios dinámicos, psicológicos, bundling, freemium y suscripción cambian conducta y economía; cada uno requiere reglas contra discriminación, erosión y complejidad.",
            "Margen bruto, contribución, punto de equilibrio, CAC, LTV y payback forman un sistema. El LTV no rescata una cohorte que no estabiliza retención y un descuento que mejora cierre puede destruir margen y referencia de precio. Las decisiones se toman por escenario, con sensibilidad y costo de servir completo.",
        ],
        marco=[
            ("Piso", "costo y capacidad", "evitar vender crecimiento con contribución negativa no financiada"),
            ("Referencia", "alternativas y competencia", "normalizar alcance y servicio"),
            ("Techo", "valor y disposición", "investigar por segmento y contexto"),
            ("Arquitectura", "métrica, planes, fences y descuentos", "alinear precio con valor y costo"),
            ("Control", "margen, CAC, LTV, payback y abandono", "decidir con cohortes y sensibilidad"),
        ],
        actividad=dict(
            consigna="Para 100 cuentas, compara tres escenarios: CLP 89.000 sin descuento; 15 % de descuento con 20 % más cierres; bundle de CLP 109.000 con CLP 12.000 de costo variable adicional y 10 % menos churn. Usa CAC CLP 310.000 y declara todos los supuestos.",
            pasos=["calcular ingreso y contribución", "estimar punto de equilibrio", "calcular payback", "hacer sensibilidad de retención", "recomendar con riesgos"],
            solucion="El 15 % de descuento no gana por cerrar más: debe compensar la contribución perdida y el anclaje futuro. El bundle puede dominar si la mejora de retención es incremental y el costo de servicio permanece dentro del supuesto. Sin prueba causal, la reducción de churn se presenta como escenario, no como hecho.",
            evidencia="modelo con fórmulas, sensibilidad, recomendación y política de descuento",
            rubrica="35 % aritmética; 20 % supuestos; 20 % valor y segmentación; 15 % riesgos; 10 % comunicación",
        ),
        metricas=[metrica("margen de contribución por segmento", "ingreso neto menos costos variables y de servicio atribuibles", "ingreso neto del segmento", "mes y cohorte de 12 meses", "facturación, costos y soporte", "Finance / Revenue Operations", "compara calidad económica con alcance homogéneo", "no incluye costos fijos ni prueba causalidad del precio")],
        ia=ia("revisar escenarios de precio", "tabla de supuestos no confidenciales o entorno aprobado", "Recalcula los escenarios mostrando cada fórmula. No inventes costos ni elasticidades. Ejecuta sensibilidad de ±20 % y marca qué supuesto cambia la decisión.", "cálculos auditables y sensibilidad", "finanzas verifica fórmulas y comercial revisa comportamiento plausible", "filtración de precios, errores aritméticos y supuestos implícitos", "modelo reproducible en hoja de cálculo"),
        transferencias=["venta unitaria", "suscripción", "freemium", "capacidad perecedera"],
        referencias=["07.04", "07.06", "07.11", "07.12", "20.03", "20.06"],
    )],
    "19.09": [dict(
        eje="J", titulo="Agilidad aplicada a producto y trabajo comercial",
        conceptos=[
            ("marco ágil", "conjunto de roles, eventos y reglas que orienta la gestión del trabajo bajo incertidumbre"),
            ("práctica ágil", "técnica puntual como retrospectiva, visualización, WIP o slicing que puede usarse dentro de distintos marcos"),
            ("métrica de flujo", "medida de tiempo de ciclo, throughput, trabajo en progreso o antigüedad que describe el sistema de entrega"),
            ("hipótesis de negocio", "predicción refutable que conecta intervención, población, resultado y criterio temporal"),
        ],
        teoria=[
            "El Manifiesto Ágil aporta valores y principios; Scrum es un marco; Kanban es un método de gestión del flujo; Lean elimina desperdicio y mejora el sistema; Lean Startup organiza aprendizaje mediante hipótesis y experimentos. Herramientas como tableros o dailies no convierten por sí solas un equipo en ágil.",
            "Producto puede usar backlog, Sprint Planning, Daily Scrum, Sprint Review y retrospectiva cuando existe un producto y un equipo estable. Ventas y marketing no deben adoptar Scrum por reflejo: Kanban, límites WIP y cadencias de revisión suelen encajar mejor con demanda continua. La coordinación entre marketing, ventas, producto y tecnología se gobierna con definiciones de terminado, impedimentos y aprendizaje compartido.",
        ],
        marco=[
            ("Scrum", "objetivo de producto y sprint con inspección", "equipo estable y trabajo que admite incrementos"),
            ("Kanban", "flujo visual, políticas y WIP", "demanda continua e interrupciones"),
            ("Lean", "valor, flujo y desperdicio", "mejora de procesos y capacidad"),
            ("Lean Startup", "construir, medir y aprender", "incertidumbre de negocio y experimento"),
            ("Híbrido explícito", "prácticas seleccionadas con razón", "dependencias entre tipos de trabajo"),
        ],
        actividad=dict(
            consigna="Diseña el sistema de trabajo para lanzar un plan de Ruta Andina con equipo de producto estable, cola de leads continua y campaña con fecha. Elige marco o prácticas por flujo y justifica qué no usarás.",
            pasos=["clasificar incertidumbre y demanda", "visualizar flujo", "fijar WIP y definiciones", "establecer cadencias", "medir y retrospectar"],
            solucion="Producto puede operar con Scrum; operaciones de leads con Kanban; la campaña usa hitos y revisiones. Una daily para todos agrega costo sin resolver dependencias. El tablero compartido muestra bloqueos y el review prueba el resultado con usuarios y ventas.",
            evidencia="diseño de flujo, políticas WIP, cadencias, backlog e hipótesis",
            rubrica="25 % elección contextual; 25 % flujo y WIP; 20 % hipótesis; 20 % coordinación; 10 % mejora",
        ),
        metricas=[metrica("tiempo de ciclo comercial priorizado", "días acumulados desde entrada lista hasta evidencia de decisión", "unidades terminadas del tipo definido", "mediana semanal y percentil 85 mensual", "tablero de trabajo", "Flow Manager", "detecta cuellos de botella y capacidad", "no mide valor entregado ni productividad individual")],
        ia=ia("identificar cuellos de botella", "historial anonimizado de estados, tiempos y bloqueos", "Analiza flujo por tipo de trabajo. Calcula mediana, P85, WIP y antigüedad; separa dato de hipótesis y no evalúes personas.", "diagnóstico del sistema y preguntas", "el equipo verifica eventos y discute causas en retrospectiva", "vigilancia laboral, causalidad espuria y optimización local", "diagrama de flujo acumulado y revisión manual"),
        transferencias=["equipo de producto", "operación comercial", "marketing de campaña", "mejora de servicio"],
        referencias=["05.11", "16.09", "17.06", "19.10", "19.11"],
    )],
    "21.05": [dict(
        eje="K", titulo="Personalización comercial con incrementalidad, privacidad y confianza",
        conceptos=[
            ("personalización contextual", "adaptación a situación, canal, etapa o necesidad observable con datos proporcionales"),
            ("hiperpersonalización", "adaptación individual de alta granularidad basada en múltiples señales y automatización"),
            ("fatiga de personalización", "caída de respuesta o confianza causada por repetición, intensidad o sensación de vigilancia"),
            ("incrementalidad de personalización", "diferencia causal entre resultado con personalización y contrafactual comparable"),
        ],
        teoria=[
            "Segmentar adapta una propuesta a grupos; personalizar decide para una persona o cuenta. Puede ser básica, contextual, conductual, psicográfica, por etapa u omnicanal. En B2B se personalizan cuenta, rol y momento; en B2C, necesidad y contexto. Recomendaciones y mensajes adaptativos deben explicar qué se usó y permitir control razonable.",
            "Más detalle no implica más eficacia: puede producir fatiga, vigilancia, discriminación o manipulación. Consentimiento, minimización, transparencia y explicabilidad son requisitos de diseño. Las cifras de «37 % más eficacia» y «2,5 veces más recomendación» no se usan como hechos mientras no exista fuente original verificada con población, método, año, contexto, magnitud y limitaciones.",
        ],
        marco=[
            ("Básica", "dato declarado y cambio visible", "saludo, idioma o preferencia"),
            ("Contextual", "situación y etapa", "siguiente acción pertinente"),
            ("Conductual", "acciones observadas", "recomendación con control y caducidad"),
            ("Psicográfica", "motivación investigada", "evitar inferir rasgos sensibles"),
            ("Hiperpersonalizada", "múltiples señales y modelo", "exigir necesidad, prueba y guardarraíles superiores"),
        ],
        actividad=dict(
            consigna="Diseña un experimento A/B para recomendar onboarding por segmento en Ruta Andina. Incluye control, unidad de asignación, métrica primaria, guardarraíles de queja/abandono/privacidad, costo y criterio de detención.",
            pasos=["definir necesidad y dato mínimo", "explicar la adaptación", "aleatorizar o justificar alternativa", "medir incrementalidad y costos", "revisar efectos adversos"],
            solucion="Conversión sola no basta: la personalización gana si mejora activación incremental sin elevar quejas, abandono ni incidentes y cubre su costo. Si no hay muestra, se usa prueba cualitativa y se declara que no estima efecto causal.",
            evidencia="protocolo experimental, DPIA ligera, mensajes, resultados y decisión",
            rubrica="20 % diseño; 20 % privacidad; 25 % incrementalidad; 20 % guardarraíles; 15 % límites",
        ),
        metricas=[metrica("incrementalidad neta de personalización", "resultado del grupo tratado menos resultado contrafactual, menos costo atribuible", "población elegible o inversión según la decisión", "ventana predefinida por experimento", "asignación, eventos, CRM y costos", "Experiment Owner", "estima efecto bajo el diseño y supuestos declarados", "no se generaliza fuera de población, canal o periodo")],
        ia=ia("proponer mensajes adaptados bajo restricciones", "atributos permitidos, etapa y propuesta aprobada", "Genera tres variantes usando sólo los atributos permitidos. Explica qué dato cambia cada variante, evita inferencias sensibles y conserva la misma promesa verificable.", "variantes para probar, no mensajes aprobados", "legal, marca y dueño de canal revisan y se prueba con usuarios", "perfilado sensible, manipulación y opacidad", "reglas deterministas por etapa y segmento"),
        transferencias=["recomendador B2C", "mensajería de cuenta B2B", "onboarding", "recuperación de abandono"],
        referencias=["12.12", "17.05", "20.09", "20.10", "21.13"],
    )],
    "18.14": [dict(
        eje="L", titulo="Relaciones humanas, experiencia y fidelización",
        conceptos=[
            ("momento de la verdad", "interacción donde la experiencia confirma o contradice una expectativa importante"),
            ("recuperación de servicio", "secuencia de reconocer, resolver, compensar cuando corresponda y prevenir repetición"),
            ("voz del cliente", "sistema continuo que recoge, vincula y devuelve acción sobre percepciones y conducta"),
            ("fidelización", "aumento sostenible de permanencia, recompra o recomendación basado en valor y confianza, no encierro"),
        ],
        teoria=[
            "Atención individualizada, empatía, comunicación directa, trato cercano y calidad consistente crean confianza cuando cumplen promesas. Customer Experience diseña percepciones a través de contactos; Customer Success gestiona resultados; posventa, reclamos y recuperación protegen la relación cuando falla el sistema.",
            "Journey mapping, momentos de la verdad y expectativas conectan operación con emoción. Lealtad, beneficios y referidos deben medir retención, recompra, calidad, costo y riesgo de selección. NPS, CSAT y correlaciones no demuestran causalidad; un experimento o diseño cuasiexperimental necesita supuestos explícitos.",
        ],
        marco=[
            ("Prometer", "expectativa clara y alcanzable", "registrar alcance y exclusiones"),
            ("Entregar", "calidad y consistencia", "medir resultado y esfuerzo"),
            ("Escuchar", "VoC y conducta", "cerrar el ciclo con dueño"),
            ("Recuperar", "resolver y prevenir", "separar síntoma de causa"),
            ("Fidelizar", "valor acumulado y confianza", "evitar incentivos que compran conducta sin lealtad"),
        ],
        actividad=dict(
            consigna="Mapea el journey de una cuenta de Ruta Andina que falla durante onboarding. Diseña contacto, recuperación, prevención y seguimiento; compara programa de beneficios con programa de referidos.",
            pasos=["reconstruir expectativa y hecho", "ubicar momento de verdad", "resolver y comunicar", "eliminar causa", "medir relación y economía"],
            solucion="Un descuento sin corregir migración compra silencio y puede aumentar churn posterior. La recuperación suficiente reconoce impacto, fija responsable y plazo, verifica resultado y cambia el proceso. Un referido cuenta sólo si el nuevo cliente retiene y no genera reclamo fundado.",
            evidencia="journey, guion de recuperación, análisis causal y diseño de programa",
            rubrica="25 % experiencia y expectativa; 25 % recuperación; 20 % prevención; 20 % medición; 10 % ética",
        ),
        metricas=[metrica("recuperación sostenible de servicio", "casos resueltos sin reincidencia del mismo modo de falla en 90 días", "casos de recuperación cerrados con seguimiento", "cohorte móvil de 90 días", "soporte, producto y CRM", "Customer Experience Lead", "mide resolución y prevención conjunta", "no demuestra que la recuperación causó retención")],
        ia=ia("clasificar causas y preparar respuestas", "tickets anonimizados, política y contexto operativo", "Clasifica causa, impacto, urgencia y promesa aplicable. Propón respuesta empática sin inventar compensaciones ni plazos; marca decisiones que requieren humano.", "borrador y agrupación de causas", "soporte verifica hechos, autoridad y tono antes de enviar", "automatizar empatía sin resolver, datos sensibles y promesas falsas", "plantillas de respuesta y revisión diaria de causas"),
        transferencias=["servicio presencial", "SaaS", "e-commerce", "contrato institucional"],
        referencias=["02.07", "08.12", "18.01", "18.06", "18.12"],
    )],
    "23.14": [dict(
        eje="M", titulo="Productividad comercial y gestión de resultados",
        conceptos=[
            ("productividad comercial", "resultado de calidad producido por unidad de capacidad y costo, sin trasladar daño a otra etapa"),
            ("gestión de cartera y territorio", "asignación de cuentas, potencial, cobertura y esfuerzo con reglas explícitas"),
            ("cuello de botella comercial", "restricción que limita el throughput del sistema aunque otras etapas aumenten actividad"),
            ("forecast accionable", "proyección con método, error, sesgo, capacidad y decisiones asociadas"),
        ],
        teoria=[
            "La productividad individual no se infiere de actividad bruta y la del equipo no es la suma de rankings. Territorios, carteras, tiempo, pipeline, capacidad, automatización y coaching forman un sistema. Win rate, velocidad, ciclo, ticket, conversión y rentabilidad se interpretan por segmento y etapa.",
            "CRM y Revenue Operations entregan definiciones; forecast y planificación de capacidad traducen demanda a recursos. KPI monitorea desempeño, OKR coordina cambio y Balanced Scorecard equilibra perspectivas. Incentivos y evaluación deben premiar resultados controlables y calidad, no manipulación del pipeline. Cada métrica debe activar una decisión concreta.",
        ],
        marco=[
            ("Demanda", "volumen y mezcla", "segmentar entrada y potencial"),
            ("Capacidad", "personas, tiempo y restricciones", "modelar cobertura real"),
            ("Flujo", "conversión, ciclo y WIP", "ubicar cuello de botella"),
            ("Economía", "ticket, margen, CAC y costo comercial", "optimizar contribución, no actividad"),
            ("Gestión", "forecast, coaching, incentivos y mejora", "cerrar aprendizaje"),
        ],
        actividad=dict(
            consigna="Diagnostica un trimestre de Ruta Andina: leads +30 %, reuniones estables, propuestas −10 %, win rate estable y ciclo +20 %. Decide si contratar, redistribuir territorios, automatizar o mejorar discovery.",
            pasos=["reconciliar definiciones", "localizar restricción", "calcular capacidad y velocidad", "comparar intervenciones", "definir coaching e indicador"],
            solucion="Más leads no resuelve una restricción entre reunión y propuesta. Contratar antes de medir carga y criterios puede amplificar desperdicio. Se audita discovery y tiempo por etapa, se redistribuye capacidad si hay mezcla desigual y se automatiza sólo trabajo repetible con control de calidad.",
            evidencia="árbol de diagnóstico, modelo de capacidad, plan de 90 días y tablero",
            rubrica="30 % diagnóstico sistémico; 25 % cálculos; 20 % decisión; 15 % personas e incentivos; 10 % revisión",
        ),
        metricas=[metrica("throughput comercial con calidad", "negocios ganados que cumplen margen, perfil y handoff", "capacidad comercial disponible en horas equivalentes", "mes y trimestre por territorio", "CRM, facturación y capacidad", "Revenue Operations", "compara rendimiento sistémico con calidad", "no debe usarse como ranking individual sin controlar mezcla y territorio")],
        ia=ia("detectar anomalías y simular capacidad", "datos agregados por etapa, territorio y cohorte", "Calcula conversión, ciclo, velocidad y capacidad. Marca anomalías sin atribuir culpa; propone tres explicaciones rivales y los datos para distinguirlas.", "diagnóstico provisional y escenarios", "RevOps reconcilia con CRM y líderes revisan contexto", "vigilancia, sesgo por territorio y datos incompletos", "revisión de pipeline con hoja de cálculo"),
        transferencias=["equipo inbound", "ventas enterprise", "territorio geográfico", "canal de socios"],
        referencias=["16.07", "16.09", "16.10", "17.14", "23.07", "23.10"],
    )],
    "05.13": [dict(
        eje="N", titulo="Innovación y desarrollo disciplinado de oportunidades",
        conceptos=[
            ("tipo de innovación", "cambio incremental o radical en producto, servicio, proceso o modelo de negocio con novedad y resultado observables"),
            ("deseabilidad–factibilidad–viabilidad", "prueba conjunta de valor para personas, posibilidad técnica-operativa y sostenibilidad económica"),
            ("sesgo del superviviente", "error de aprender sólo de iniciativas visibles o exitosas e ignorar abandonos y fracasos"),
            ("abandono oportuno", "decisión previa de detener una iniciativa cuando evidencia, riesgo o costo superan el valor de seguir"),
        ],
        teoria=[
            "La innovación puede ser incremental, radical o disruptiva, y ocurrir en producto, servicio, proceso o modelo. Design Thinking organiza empatía, definición, ideación, prototipado y prueba; divergencia produce opciones y convergencia aplica criterios. Creatividad sin oportunidad ni validación es inventario de ideas.",
            "Deseabilidad, factibilidad, viabilidad y escalabilidad se prueban por separado y luego juntas. La adopción tecnológica requiere cambio de procesos, capacidades e incentivos. La cultura de innovación aprende de intentos fallidos documentados; perseverar no es virtud cuando el criterio de abandono ya se cumplió.",
        ],
        marco=[
            ("Explorar", "señales, problemas y oportunidades", "incluir casos fallidos y no usuarios"),
            ("Divergir", "múltiples mecanismos y modelos", "separar generación de selección"),
            ("Converger", "criterios de deseo, factibilidad, viabilidad y riesgo", "hacer trade-offs visibles"),
            ("Prototipar", "representación suficiente para aprender", "elegir fidelidad por hipótesis"),
            ("Decidir", "perseverar, pivotar o abandonar", "usar criterio previo y documentar fracaso"),
        ],
        actividad=dict(
            consigna="Genera seis oportunidades para reducir inasistencias en Ruta Andina: dos de producto, dos de servicio y dos de modelo de negocio. Selecciona dos, prototipa una y ejecuta un pre-mortem con criterio de abandono.",
            pasos=["investigar problema", "divergir sin evaluar", "converger con cuatro criterios", "prototipar y probar", "registrar aprendizaje, incluido fracaso"],
            solucion="Una solución tecnológicamente novedosa no domina si exige datos no disponibles o empeora confianza. Un servicio simple puede validar deseabilidad. La iniciativa se abandona si no aparece compromiso costoso en la muestra definida o si el riesgo de datos supera el beneficio bajo controles razonables.",
            evidencia="mapa de oportunidades, matriz de selección, prototipo, plan de prueba y post-mortem",
            rubrica="20 % investigación; 20 % diversidad de opciones; 25 % criterios; 20 % experimento; 15 % aprendizaje y abandono",
        ),
        metricas=[metrica("tasa de aprendizaje de innovación", "hipótesis críticas resueltas con evidencia y decisión", "hipótesis críticas sometidas a prueba", "por ciclo y portafolio trimestral", "registro de experimentos y decisiones", "Innovation Lead", "mide reducción de incertidumbre, incluidos abandonos", "no equivale a tasa de éxito comercial ni premia experimentar sin decisión")],
        ia=ia("ampliar opciones y atacar supuestos", "problema, restricciones y evidencia anonimizada", "Propón opciones en producto, servicio, proceso y modelo. Para cada una declara supuesto crítico, prueba barata, riesgo, criterio de abandono y alternativa no tecnológica.", "portafolio de hipótesis para revisar", "equipo diverso elimina duplicados y confronta con evidencia y afectados", "ideas homogéneas, sesgo cultural y entusiasmo tecnológico", "brainwriting individual, matriz morfológica y pre-mortem"),
        transferencias=["innovación incremental", "nuevo modelo de negocio", "adopción tecnológica", "mejora de proceso"],
        referencias=["03.13", "05.03", "05.04", "19.11", "21.12"],
    )],
}


def aplicar(parte, clases):
    """Adjunta las ampliaciones y sus conceptos/métricas una sola vez."""
    for clase in clases:
        ref = "{}.{}".format(parte, clase["n"])
        ampliaciones = AMPLIACIONES.get(ref, [])
        if not ampliaciones or clase.get("_ampliaciones_aplicadas"):
            continue
        clase["ampliaciones"] = ampliaciones
        for ampliacion in ampliaciones:
            clase["conceptos"].extend(ampliacion["conceptos"])
            for ficha in ampliacion["metricas"]:
                definicion = (
                    "numerador: {numerador}; denominador: {denominador}; ventana: {ventana}; "
                    "fuente: {fuente}; responsable: {responsable}; lectura permitida: {lectura}; "
                    "limitación: {limite}"
                ).format(**ficha)
                clase["senales"].append((ficha["nombre"], definicion))
        clase["_ampliaciones_aplicadas"] = True
    return clases

