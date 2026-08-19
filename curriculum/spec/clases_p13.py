# -*- coding: utf-8 -*-
"""Parte 13 — Contenido, copywriting y comunicación persuasiva."""

CLASES = [
    dict(
        n="01",
        slug="estrategia-de-contenidos",
        titulo="Estrategia de contenidos",
        tesis=(
            "Una estrategia de contenidos define para quién se produce, qué problema ayuda a resolver cada "
            "pieza y qué resultado comercial se espera. Pulizzi observó que las empresas que construyen "
            "audiencia propia antes de monetizar obtienen ventajas duraderas, pero eso exige constancia y "
            "foco. Publicar sobre todo lo que interesa a la empresa produce un archivo, no una audiencia."
        ),
        conceptos=[
            ("audiencia definida", "grupo específico para el que se produce contenido de forma consistente"),
            ("promesa editorial", "compromiso sobre qué tipo de utilidad entregará el contenido"),
            ("ritmo sostenible", "frecuencia de publicación que el equipo puede mantener durante años"),
            ("objetivo comercial del contenido", "resultado que la pieza debe habilitar: descubrimiento, evaluación o cierre"),
        ],
        metodo=[
            "definir la audiencia y su problema principal",
            "declarar la promesa editorial",
            "asignar a cada tipo de pieza un objetivo comercial",
            "fijar un ritmo sostenible con la capacidad real",
            "medir el efecto sobre demanda y sobre el proceso de venta",
        ],
        senales=[
            ("piezas con objetivo comercial declarado", "piezas con objetivo asignado, sobre piezas publicadas"),
            ("uso del contenido en ventas", "piezas utilizadas en negocios activos, sobre piezas producidas"),
            ("crecimiento de audiencia propia", "suscriptores netos ganados en el mes, sobre suscriptores al inicio del mes"),
        ],
        caso=(
            "El blog de Ruta Andina publica dos artículos semanales sobre tendencias digitales. Ninguno "
            "responde las cinco preguntas que aparecen en todas las llamadas de venta."
        ),
        limite=(
            "El contenido tiene retorno lento. Exigirle conversión inmediata induce a producir piezas "
            "promocionales que la audiencia ignora."
        ),
        libros=["pulizzi", "handley", "godin", "binet-field"],
        error=("Publicar sobre temas que interesan a la empresa",
               "Construye el calendario desde las preguntas registradas en llamadas y soporte."),
    ),
    dict(
        n="02",
        slug="pilares-de-contenido",
        titulo="Pilares de contenido",
        tesis=(
            "Los pilares son los tres o cuatro temas en los que la empresa quiere ser reconocida. Sirven para "
            "decidir qué no publicar, que es la función más valiosa. Un pilar bien elegido cumple tres "
            "condiciones: importa al segmento, la empresa tiene autoridad real para hablar de él y se conecta "
            "con lo que vende. Sin la tercera condición, se construye audiencia que no compra."
        ),
        conceptos=[
            ("pilar temático", "área en la que la empresa concentra su producción y busca ser reconocida"),
            ("autoridad real", "conocimiento o evidencia propia que respalda lo que la empresa afirma sobre el tema"),
            ("conexión comercial", "vínculo entre el tema y el problema que la oferta resuelve"),
            ("dispersión temática", "producción de contenido en demasiadas áreas, que impide construir reconocimiento"),
        ],
        metodo=[
            "listar los temas candidatos con evidencia de interés",
            "evaluar la autoridad propia en cada uno",
            "verificar la conexión con lo que se vende",
            "elegir tres pilares y descartar el resto por escrito",
            "auditar la producción contra los pilares cada trimestre",
        ],
        senales=[
            ("concentración en pilares", "piezas publicadas dentro de los pilares, sobre piezas totales"),
            ("reconocimiento por tema", "proporción de la audiencia que asocia la marca al pilar, en medición periódica"),
            ("conversión por pilar", "oportunidades originadas por contenido de cada pilar, sobre visitas del pilar"),
        ],
        caso=(
            "Ruta Andina publicó el último trimestre sobre inteligencia artificial, liderazgo, tendencias de "
            "consumo y agendamiento. Sólo el último se conecta con lo que vende."
        ),
        limite=(
            "Los pilares no pueden ser inamovibles: el mercado cambia y la autoridad se construye o se pierde. "
            "La revisión anual es parte del método."
        ),
        libros=["pulizzi", "godin", "handley", "keller-brand"],
        error=("Producir contenido en demasiadas áreas",
               "Define tres pilares, documenta lo descartado y audita la producción contra ellos."),
    ),
    dict(
        n="03",
        slug="aida",
        titulo="AIDA",
        tesis=(
            "Atención, interés, deseo y acción es un modelo antiguo y todavía útil como lista de verificación "
            "de una pieza persuasiva: si no hay atención, nada más importa; si hay interés sin deseo, no hay "
            "movimiento; si hay deseo sin acción clara, se pierde. Su límite es conocido: describe una "
            "secuencia lineal que rara vez ocurre así, y no dice nada sobre la verdad de la promesa."
        ),
        conceptos=[
            ("captura de atención", "elemento que detiene el desplazamiento y hace que la persona lea"),
            ("construcción de interés", "conexión entre el contenido y un problema que la persona reconoce"),
            ("deseo", "proyección concreta del beneficio en la situación del lector"),
            ("acción clara", "instrucción específica sobre qué hacer a continuación y con qué esfuerzo"),
        ],
        metodo=[
            "verificar que el inicio capta atención con algo relevante",
            "conectar con un problema reconocible en las primeras líneas",
            "concretar el beneficio en la situación del lector",
            "cerrar con una acción específica y de bajo esfuerzo",
            "probar la pieza con lectores del segmento",
        ],
        senales=[
            ("tasa de lectura completa", "lectores que llegan al final, sobre lectores que iniciaron"),
            ("tasa de clic en la acción", "clics en la acción principal, sobre impresiones de la pieza"),
            ("comprensión del siguiente paso", "lectores que identifican correctamente qué se les pide, en prueba con muestra"),
        ],
        caso=(
            "El correo de Ruta Andina abre con la historia de la empresa, describe siete funcionalidades y "
            "cierra con «quedamos atentos a cualquier consulta»."
        ),
        limite=(
            "AIDA no distingue persuasión legítima de manipulación. Una pieza puede cumplir el modelo y "
            "constituir publicidad engañosa."
        ),
        libros=["sugarman", "ogilvy", "heath", "cialdini"],
        error=("Cerrar sin una acción específica",
               "Sustituye las fórmulas de cortesía por una instrucción concreta y de bajo esfuerzo."),
    ),
    dict(
        n="04",
        slug="pas",
        titulo="PAS: problema, agitación, solución",
        tesis=(
            "La estructura problema-agitación-solución funciona porque parte de donde está el lector y no de "
            "donde está la empresa. La agitación —desarrollar las consecuencias del problema— es la parte "
            "eficaz y también la peligrosa: exagerar produce ansiedad artificial y, cuando se refiere a "
            "riesgos de salud, dinero o cumplimiento, puede constituir publicidad engañosa. La agitación "
            "legítima usa consecuencias reales y verificables."
        ),
        conceptos=[
            ("problema reconocible", "dificultad que el lector identifica como propia sin necesidad de explicación"),
            ("agitación", "desarrollo de las consecuencias reales del problema no resuelto"),
            ("solución proporcional", "propuesta cuyo alcance corresponde al problema descrito"),
            ("exageración indebida", "amplificación del riesgo más allá de lo que la evidencia sostiene"),
        ],
        metodo=[
            "formular el problema en las palabras del lector",
            "desarrollar consecuencias verificables",
            "verificar que la evidencia sostiene cada afirmación",
            "presentar la solución con alcance proporcional",
            "probar la pieza y medir reclamos o rechazo",
        ],
        senales=[
            ("tasa de respuesta de la pieza", "respuestas o clics obtenidos, sobre impresiones entregadas"),
            ("afirmaciones con respaldo", "afirmaciones con evidencia documentada, sobre afirmaciones de la pieza"),
            ("reclamos por contenido", "reclamos vinculados a la pieza, sobre impresiones entregadas"),
        ],
        caso=(
            "Una pieza de Ruta Andina afirma que «sin un sistema digital tu negocio desaparecerá en dos "
            "años». No hay evidencia que sostenga esa afirmación."
        ),
        limite=(
            "La agitación es especialmente riesgosa en categorías sensibles. En Chile, las afirmaciones "
            "comerciales deben ser veraces y comprobables."
        ),
        libros=["sugarman", "cialdini", "heath", "handley"],
        error=("Agitar con consecuencias no verificables",
               "Sustituye la afirmación catastrófica por una consecuencia documentada con fuente."),
    ),
    dict(
        n="05",
        slug="features-versus-benefits",
        titulo="Características versus beneficios",
        tesis=(
            "Una característica describe lo que el producto es; un beneficio describe lo que cambia para el "
            "cliente. La traducción no es cosmética: obliga a saber qué hace el cliente con esa "
            "característica y qué resultado obtiene. La versión completa agrega evidencia: característica, "
            "beneficio y prueba. Sin la prueba, el beneficio es una afirmación más entre muchas iguales."
        ),
        conceptos=[
            ("característica", "atributo verificable de lo que el producto hace o incluye"),
            ("beneficio", "cambio concreto en la situación del cliente que produce esa característica"),
            ("prueba", "evidencia que respalda la afirmación de beneficio"),
            ("beneficio genérico", "afirmación aplicable a cualquier competidor y por lo tanto sin valor diferenciador"),
        ],
        metodo=[
            "listar las características relevantes",
            "traducir cada una a un cambio concreto para el cliente",
            "descartar los beneficios que cualquier competidor podría afirmar",
            "asociar una prueba a cada beneficio",
            "verificar la traducción con clientes reales",
        ],
        senales=[
            ("beneficios con prueba asociada", "beneficios con evidencia documentada, sobre beneficios comunicados"),
            ("beneficios diferenciadores", "beneficios que el competidor no puede afirmar, sobre beneficios comunicados"),
            ("recuerdo del beneficio central", "personas que recuerdan el beneficio principal tras 24 horas, sobre expuestas"),
        ],
        caso=(
            "El material de Ruta Andina dice «plataforma en la nube, multiusuario y con reportes». Ningún "
            "cliente puede decir qué cambia en su día."
        ),
        limite=(
            "En audiencias técnicas la característica puede ser el beneficio: quien evalúa integración "
            "necesita el detalle técnico, no una traducción emocional."
        ),
        libros=["sugarman", "ogilvy", "handley", "heath"],
        error=("Comunicar beneficios genéricos sin prueba",
               "Descarta todo beneficio que un competidor podría afirmar y asocia evidencia al resto."),
    ),
    dict(
        n="06",
        slug="headlines",
        titulo="Titulares",
        tesis=(
            "El titular decide si el resto se lee. Ogilvy estimaba que la mayoría de los lectores no pasa de "
            "allí, y la lógica se mantiene en entornos digitales saturados. Un buen titular es específico, "
            "relevante para el destinatario y honesto respecto del contenido. El clickbait produce clics y "
            "destruye confianza: el costo aparece en la siguiente pieza, cuando ya nadie abre."
        ),
        conceptos=[
            ("especificidad", "nivel de concreción que distingue el titular de una afirmación genérica"),
            ("relevancia para el destinatario", "conexión inmediata con un problema o interés del lector"),
            ("honestidad del titular", "correspondencia entre lo prometido y lo que entrega el contenido"),
            ("costo del clickbait", "pérdida de confianza y de apertura futura por promesas incumplidas"),
        ],
        metodo=[
            "escribir al menos diez variantes antes de elegir",
            "verificar especificidad y relevancia de cada una",
            "descartar las que prometen más de lo que el contenido entrega",
            "probar dos variantes con muestra suficiente",
            "medir apertura y también permanencia en el contenido",
        ],
        senales=[
            ("tasa de apertura o clic", "aperturas o clics, sobre impresiones entregadas, por variante"),
            ("permanencia tras el clic", "tiempo medio en el contenido, comparado entre variantes de titular"),
            ("tasa de baja tras la apertura", "bajas solicitadas tras abrir, sobre aperturas de la pieza"),
        ],
        caso=(
            "El titular «No vas a creer lo que hace este software» de Ruta Andina obtuvo 34 % de apertura y "
            "la permanencia media fue de siete segundos."
        ),
        limite=(
            "El titular más eficaz para la apertura puede ser el peor para la conversión. La evaluación debe "
            "considerar el resultado final y no la métrica intermedia."
        ),
        libros=["ogilvy", "sugarman", "handley", "kohavi"],
        error=("Optimizar el titular sólo por apertura",
               "Evalúa apertura, permanencia y conversión antes de declarar ganadora una variante."),
    ),
    dict(
        n="07",
        slug="ofertas-y-cta",
        titulo="Ofertas y llamados a la acción",
        tesis=(
            "El llamado a la acción debe ser proporcional a la confianza construida. Pedir una compra a quien "
            "recién conoce la empresa produce rechazo; pedir sólo una descarga a quien ya evaluó produce "
            "retraso. La formulación importa: un botón que describe lo que ocurrirá —«ver precios», «agendar "
            "15 minutos»— convierte mejor que uno genérico, porque reduce la incertidumbre sobre el "
            "compromiso."
        ),
        conceptos=[
            ("proporcionalidad", "correspondencia entre lo que se pide y la confianza existente"),
            ("claridad del compromiso", "grado en que el destinatario sabe qué ocurrirá al actuar"),
            ("acción principal", "objetivo único de la pieza, sin alternativas que compitan"),
            ("costo percibido de la acción", "esfuerzo y riesgo que el destinatario atribuye a dar el paso"),
        ],
        metodo=[
            "identificar el nivel de confianza de la audiencia",
            "elegir una acción proporcional a ese nivel",
            "describir con precisión qué ocurrirá al actuar",
            "eliminar acciones que compitan en la misma pieza",
            "medir conversión y calidad del contacto generado",
        ],
        senales=[
            ("tasa de conversión de la acción", "acciones completadas, sobre impresiones de la pieza"),
            ("calidad del contacto generado", "contactos que cumplen criterios de perfil, sobre contactos generados"),
            ("abandono tras iniciar la acción", "abandonos en el proceso, sobre inicios registrados"),
        ],
        caso=(
            "La página de Ruta Andina ofrece simultáneamente «descargar guía», «agendar demo», «hablar por "
            "WhatsApp» y «ver precios». La conversión total es 1,1 %."
        ),
        limite=(
            "Reducir el compromiso solicitado aumenta el volumen y puede reducir la calidad. El criterio "
            "depende de la capacidad de atención del equipo comercial."
        ),
        libros=["eisenberg", "laja", "krug", "cialdini"],
        error=("Ofrecer varias acciones que compiten entre sí",
               "Define una acción principal por pieza y relega el resto a un lugar secundario."),
    ),
    dict(
        n="08",
        slug="landing-page-copy",
        titulo="Copy de landing page",
        tesis=(
            "El texto de una landing responde en orden: qué es, para quién, qué problema resuelve, por qué "
            "creerlo, cuánto cuesta y qué hacer ahora. Cada bloque debe poder eliminarse sin que se pierda "
            "otra información. La investigación previa determina el orden real: si la objeción dominante es "
            "el precio, ocultarlo hasta el final aumenta el abandono en lugar de reducirlo."
        ),
        conceptos=[
            ("jerarquía informativa", "orden de los bloques según las preguntas del visitante"),
            ("objeción dominante", "duda que más frecuentemente impide avanzar en ese segmento"),
            ("prueba en página", "evidencia visible que respalda la afirmación central"),
            ("redundancia útil", "repetición del llamado a la acción en los momentos de decisión"),
        ],
        metodo=[
            "documentar las preguntas y objeciones reales del segmento",
            "ordenar los bloques según esas preguntas",
            "incluir prueba visible junto a cada afirmación fuerte",
            "repetir el llamado a la acción en los puntos de decisión",
            "probar comprensión con usuarios del segmento",
        ],
        senales=[
            ("conversión por sección", "profundidad de desplazamiento y conversión, por bloque de la página"),
            ("objeciones resueltas en página", "objeciones documentadas con respuesta visible, sobre objeciones registradas"),
            ("consultas repetidas post visita", "consultas sobre información que la página ya contiene, sobre consultas totales"),
        ],
        caso=(
            "La landing de Ruta Andina no muestra precios. El 47 % de las consultas entrantes pregunta "
            "exactamente eso y el equipo comercial dedica su primera llamada a responderlo."
        ),
        limite=(
            "Mostrar precio puede reducir el volumen de contactos y aumentar su calidad. La decisión depende "
            "de la capacidad comercial y del modelo de venta."
        ),
        libros=["laja", "eisenberg", "handley", "krug"],
        error=("Ocultar información que el visitante busca",
               "Incluye la respuesta a la objeción dominante en la página, aunque reduzca el volumen de contactos."),
    ),
    dict(
        n="09",
        slug="email-copy",
        titulo="Copy de correo",
        tesis=(
            "El correo comercial compite con decenas en la bandeja. Su ventaja es el contexto: se puede "
            "personalizar con lo que se sabe del destinatario. La estructura eficaz es breve: razón del "
            "contacto, problema probable, evidencia mínima y petición proporcional. Todo lo demás resta. En "
            "correos a base propia, la coherencia con lo que la persona aceptó recibir es tanto una "
            "obligación legal como una condición de eficacia."
        ),
        conceptos=[
            ("contexto del destinatario", "información específica que hace pertinente este correo para esta persona"),
            ("brevedad funcional", "extensión mínima suficiente para que la petición se comprenda"),
            ("coherencia con el consentimiento", "correspondencia entre lo que la persona aceptó recibir y lo que recibe"),
            ("secuencia de valor", "orden de correos que entrega utilidad antes de pedir"),
        ],
        metodo=[
            "verificar qué aceptó recibir el destinatario",
            "identificar el contexto que hace pertinente el correo",
            "redactar con estructura breve y petición proporcional",
            "probar variantes de asunto y de petición",
            "medir respuesta, bajas y reclamos por segmento",
        ],
        senales=[
            ("tasa de respuesta por segmento", "respuestas recibidas, sobre correos entregados, por segmento"),
            ("tasa de baja por campaña", "bajas solicitadas, sobre correos entregados, por campaña"),
            ("ingreso atribuible por envío", "ingreso vinculado al envío, sobre costo del envío"),
        ],
        caso=(
            "Ruta Andina envía a su lista de suscriptores de contenido una promoción de hardware. Las bajas "
            "de esa campaña triplicaron el promedio."
        ),
        limite=(
            "La personalización excesiva puede resultar invasiva. Mencionar datos que el destinatario no sabe "
            "que la empresa posee genera desconfianza."
        ),
        libros=["handley", "sugarman", "godin", "chaffey"],
        error=("Enviar contenido distinto al consentido",
               "Segmenta por lo que cada persona aceptó recibir y respeta esa promesa en cada envío."),
    ),
    dict(
        n="10",
        slug="sales-copy-b2b",
        titulo="Copy comercial B2B",
        tesis=(
            "El texto comercial B2B tiene una audiencia doble: quien lo lee y quien lo recibirá reenviado. "
            "Eso exige precisión, evidencia y ausencia de exageración: un documento que circula por una "
            "organización será leído por alguien escéptico. La regla práctica es escribir para el más crítico "
            "de los lectores posibles, normalmente finanzas o el área técnica."
        ),
        conceptos=[
            ("lector escéptico", "persona del comité que evaluará el documento buscando debilidades"),
            ("precisión verificable", "afirmaciones que resisten comprobación por un tercero"),
            ("estructura de decisión", "orden que facilita evaluar problema, opciones y consecuencias"),
            ("lenguaje de la organización", "vocabulario que usa el cliente y no el que usa el proveedor"),
        ],
        metodo=[
            "identificar al lector más escéptico del comité",
            "escribir con precisión verificable y sin exageración",
            "estructurar por problema, opciones y consecuencias",
            "usar el vocabulario del cliente",
            "probar el documento con alguien ajeno al negocio",
        ],
        senales=[
            ("circulación interna del documento", "negocios donde el documento llegó a personas no presentes, sobre negocios con propuesta"),
            ("afirmaciones verificables", "afirmaciones con fuente o respaldo, sobre afirmaciones del documento"),
            ("preguntas de aclaración recibidas", "consultas del cliente sobre el documento, sobre documentos enviados"),
        ],
        caso=(
            "La propuesta de Ruta Andina para la cadena afirma «ahorro garantizado del 30 %» sin base de "
            "cálculo. Finanzas la rechazó por no poder verificar la cifra."
        ),
        limite=(
            "Escribir sólo para el escéptico puede producir documentos áridos que no movilizan al usuario. La "
            "solución es una versión ejecutiva y un anexo técnico."
        ),
        libros=["ellet", "dixon-customer", "handley", "heath"],
        error=("Usar cifras sin base de cálculo",
               "Adjunta el método de cálculo y sus supuestos a toda afirmación cuantitativa."),
    ),
    dict(
        n="11",
        slug="storytelling-comercial",
        titulo="Storytelling comercial",
        tesis=(
            "Un caso de cliente bien construido es la pieza comercial de mayor rendimiento porque combina "
            "evidencia y narrativa. Su estructura es estable: situación inicial con datos, obstáculo, "
            "decisión, implementación y resultado verificable. Su exigencia también: autorización del "
            "cliente, cifras comprobables y explicitación de qué parte del resultado es atribuible a la "
            "solución."
        ),
        conceptos=[
            ("caso verificable", "relato con datos, autorización y método de cálculo documentado"),
            ("atribución honesta", "declaración de qué parte del resultado corresponde a la solución y qué parte a otros factores"),
            ("protagonista reconocible", "cliente con el que el lector del segmento puede identificarse"),
            ("autorización de uso", "consentimiento escrito para publicar el nombre, los datos y las cifras"),
        ],
        metodo=[
            "seleccionar un cliente representativo del segmento",
            "documentar situación inicial y resultado con datos",
            "declarar el método de cálculo y sus supuestos",
            "obtener autorización escrita de uso",
            "medir el efecto de la pieza en el proceso comercial",
        ],
        senales=[
            ("casos con autorización documentada", "casos publicados con autorización escrita, sobre casos publicados"),
            ("uso en negocios activos", "negocios donde se compartió un caso, sobre negocios en etapa de evaluación"),
            ("efecto en avance de etapa", "diferencia de avance entre negocios con y sin caso compartido"),
        ],
        caso=(
            "El caso publicado por Ruta Andina cita «40 % más de ingresos» sin indicar periodo ni qué otros "
            "cambios hizo el cliente en ese lapso."
        ),
        limite=(
            "Un caso excepcional puede generar expectativas irreales. Publicar resultados atípicos sin "
            "declararlo como tal puede constituir publicidad engañosa."
        ),
        libros=["heath", "ellet", "handley", "ogilvy"],
        error=("Publicar resultados sin declarar otros factores",
               "Explicita qué parte del resultado es atribuible y qué otros cambios ocurrieron en el mismo periodo."),
    ),
    dict(
        n="12",
        slug="prueba-social",
        titulo="Prueba social",
        tesis=(
            "La prueba social funciona porque reduce incertidumbre: si otros como yo lo hicieron, el riesgo "
            "parece menor. Cialdini precisó la condición: la similitud importa más que la cantidad. Cien "
            "testimonios genéricos convencen menos que tres de pares reconocibles. Su límite es rotundo: "
            "reseñas falsas o testimonios inventados constituyen publicidad engañosa y destruyen la "
            "confianza cuando se descubren."
        ),
        conceptos=[
            ("similitud del referente", "grado en que quien testimonia se parece al destinatario del mensaje"),
            ("verificabilidad", "posibilidad de que un tercero compruebe que el testimonio es real"),
            ("prueba social negativa", "mensaje que comunica involuntariamente que pocos adoptan la solución"),
            ("transparencia de incentivos", "declaración de si el testimonio fue compensado de alguna forma"),
        ],
        metodo=[
            "seleccionar referentes similares al destinatario",
            "obtener testimonios verificables con autorización",
            "declarar cualquier incentivo entregado",
            "evitar formulaciones que comuniquen baja adopción",
            "medir el efecto por segmento",
        ],
        senales=[
            ("efecto de la prueba social", "diferencia de conversión entre piezas con y sin testimonio de pares"),
            ("testimonios verificables", "testimonios con identificación y autorización, sobre testimonios publicados"),
            ("similitud declarada", "testimonios del mismo rubro y tamaño que el destinatario, sobre testimonios usados"),
        ],
        caso=(
            "Ruta Andina muestra logos de 40 clientes en su página. Ninguno es de un taller, que es el "
            "segmento al que dirige su campaña actual."
        ),
        limite=(
            "En Chile, las reseñas o testimonios falsos y la publicidad encubierta están prohibidas. Los "
            "incentivos entregados deben declararse."
        ),
        libros=["cialdini", "sharp2", "godin", "reichheld"],
        error=("Usar testimonios de segmentos distintos al destinatario",
               "Selecciona referentes del mismo rubro y tamaño, con autorización verificable."),
    ),
    dict(
        n="13",
        slug="edicion-y-testing-de-mensajes",
        titulo="Edición y testing de mensajes",
        tesis=(
            "Editar es eliminar. Handley formula el criterio con precisión: la utilidad para el lector manda "
            "sobre la elegancia para el autor. Después de editar, el testing decide entre alternativas con "
            "evidencia y no con opinión. La condición es la misma que en cualquier experimento: muestra "
            "suficiente, una variable por vez y criterio definido antes de mirar los resultados."
        ),
        conceptos=[
            ("edición por utilidad", "eliminación de todo lo que no ayuda al lector a decidir"),
            ("variable aislada", "único elemento que cambia entre dos versiones a comparar"),
            ("criterio previo", "definición de qué resultado se considerará ganador, fijada antes del test"),
            ("validez de la conclusión", "grado en que el resultado se sostiene al repetir la medición"),
        ],
        metodo=[
            "editar eliminando lo que no aporta al lector",
            "definir la variable a probar y el criterio de éxito",
            "calcular la muestra necesaria",
            "ejecutar sin modificar el criterio",
            "documentar el aprendizaje en la guía editorial",
        ],
        senales=[
            ("reducción de extensión tras edición", "palabras eliminadas, sobre palabras del borrador original"),
            ("tests con criterio previo", "tests con criterio documentado antes de iniciar, sobre tests realizados"),
            ("aprendizajes incorporados a la guía", "aprendizajes documentados en la guía editorial, por trimestre"),
        ],
        caso=(
            "Ruta Andina probó tres variantes de correo simultáneamente cambiando asunto, cuerpo y llamado a "
            "la acción. No puede saber qué elemento produjo la diferencia."
        ),
        limite=(
            "Con volúmenes bajos, el testing no alcanza potencia. En ese caso, la edición fundamentada y la "
            "prueba cualitativa son mejores que un test sin validez."
        ),
        libros=["handley", "kohavi", "sugarman", "laja"],
        error=("Cambiar varias variables a la vez",
               "Aísla una variable por prueba y define el criterio de éxito antes de ejecutar."),
    ),
    dict(
        n="14",
        slug="sistema-editorial-completo",
        titulo="Sistema editorial completo",
        tesis=(
            "Esta clase integra la parte en un sistema editorial: pilares, calendario, guía de estilo, flujo "
            "de producción y aprobación, biblioteca de piezas y medición. La prueba de calidad es la "
            "continuidad: el sistema debe seguir produciendo con calidad cuando el responsable actual no "
            "esté, y debe impedir que salga publicada una afirmación sin respaldo."
        ),
        conceptos=[
            ("flujo de producción", "secuencia definida desde la idea hasta la publicación con responsables"),
            ("control de afirmaciones", "verificación obligatoria del respaldo de toda afirmación comercial"),
            ("biblioteca de piezas", "repositorio organizado que permite reutilizar contenido en ventas"),
            ("continuidad operativa", "capacidad del sistema de funcionar sin depender de una persona"),
        ],
        metodo=[
            "consolidar pilares, calendario y guía de estilo",
            "definir el flujo de producción y aprobación",
            "instalar el control de afirmaciones antes de publicar",
            "organizar la biblioteca para uso comercial",
            "medir producción, uso y efecto comercial",
        ],
        senales=[
            ("cumplimiento del calendario", "piezas publicadas en fecha, sobre piezas planificadas"),
            ("afirmaciones verificadas antes de publicar", "piezas con control de afirmaciones aplicado, sobre piezas publicadas"),
            ("uso comercial del contenido", "piezas utilizadas en negocios activos, sobre piezas de la biblioteca"),
        ],
        caso=(
            "Ruta Andina trabajará con una agencia externa el próximo trimestre. Hoy no existe guía de "
            "estilo, ni flujo de aprobación, ni control de afirmaciones."
        ),
        limite=(
            "Un flujo de aprobación con demasiados pasos mata la producción. El control debe concentrarse en "
            "las afirmaciones con riesgo, no en cada palabra."
        ),
        libros=["handley", "pulizzi", "godin", "wheeler"],
        error=("Publicar sin control de afirmaciones",
               "Instala una verificación obligatoria de respaldo para toda afirmación cuantitativa o comparativa."),
    ),
]
