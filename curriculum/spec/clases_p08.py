# -*- coding: utf-8 -*-
"""Parte 08 — Fundamentos profesionales de ventas."""

CLASES = [
    dict(
        n="01",
        slug="proceso-comercial-reproducible",
        titulo="Proceso comercial reproducible",
        tesis=(
            "Un proceso comercial es reproducible cuando dos personas distintas, ante la misma situación, "
            "ejecutan pasos equivalentes y obtienen resultados comparables. Eso exige etapas definidas por el "
            "comportamiento del cliente —no por la actividad del vendedor—, criterios de salida verificables "
            "y materiales asociados. Roberge mostró que la formación y la gestión comercial mejoran cuando el "
            "proceso está escrito: sin él, cada incorporación reinventa el método y el desempeño depende del "
            "talento individual."
        ),
        conceptos=[
            ("etapa comercial", "estado de la oportunidad definido por lo que el cliente ha hecho, no por lo que el vendedor intentó"),
            ("criterio de salida", "condición verificable que debe cumplirse para avanzar a la etapa siguiente"),
            ("playbook", "documento que asocia a cada etapa sus objetivos, preguntas, materiales y errores frecuentes"),
            ("variabilidad del desempeño", "dispersión de resultados entre vendedores que ejecutan el mismo proceso"),
        ],
        metodo=[
            "reconstruir el proceso real que siguen los negocios ganados",
            "definir etapas por comportamiento del cliente",
            "escribir criterios de salida verificables",
            "asociar materiales y preguntas a cada etapa",
            "medir dispersión de desempeño y corregir el proceso, no sólo a la persona",
        ],
        senales=[
            ("conversión por etapa", "oportunidades que avanzan a la etapa siguiente, sobre las que ingresaron a la etapa"),
            ("dispersión de desempeño", "desviación estándar de la tasa de cierre entre vendedores del mismo segmento"),
            ("cumplimiento de criterios de salida", "oportunidades avanzadas con criterio cumplido, sobre oportunidades avanzadas"),
        ],
        caso=(
            "En Ruta Andina dos vendedores concentran el 70 % del cierre. Cuando uno toma vacaciones el "
            "pipeline se detiene y nadie puede describir qué hacen distinto."
        ),
        limite=(
            "Un proceso demasiado rígido ahoga la lectura situacional del vendedor. El criterio es estandarizar "
            "las decisiones repetibles y dejar libertad en la conversación."
        ),
        libros=["roberge", "weinberg-sales", "rackham", "grove"],
        error=("Definir etapas por actividad del vendedor",
               "Reescribe cada etapa según lo que el cliente hizo: aceptó reunión, compartió datos, presentó a su comité."),
    ),
    dict(
        n="02",
        slug="prospeccion",
        titulo="Prospección",
        tesis=(
            "Prospectar es originar conversaciones con personas que probablemente tengan el problema que la "
            "empresa resuelve. Blount insiste en que el determinante principal es la disciplina de actividad "
            "sostenida, porque el pipeline responde con retardo: la sequía de hoy se originó en la falta de "
            "prospección de hace dos meses. La calidad de la lista y la relevancia del mensaje multiplican esa "
            "actividad, pero no la sustituyen."
        ),
        conceptos=[
            ("actividad de prospección", "número de intentos de contacto de calidad realizados en un periodo"),
            ("lista objetivo", "conjunto acotado de organizaciones que cumplen el perfil de cliente ideal"),
            ("retardo del pipeline", "desfase entre la actividad de prospección y su efecto en oportunidades cerradas"),
            ("relevancia del mensaje", "grado en que el contacto demuestra conocimiento del problema específico del destinatario"),
        ],
        metodo=[
            "construir la lista objetivo desde el perfil de cliente ideal",
            "definir el volumen de actividad semanal necesario",
            "personalizar el mensaje con evidencia del problema",
            "sostener la cadencia aunque el pipeline esté lleno",
            "medir el retardo real entre actividad y cierre",
        ],
        senales=[
            ("intentos de contacto por semana", "contactos de calidad realizados, por vendedor y por semana"),
            ("tasa de conversación obtenida", "conversaciones sostenidas, sobre intentos de contacto realizados"),
            ("retardo observado", "días entre el primer contacto y el cierre, mediana por segmento"),
        ],
        caso=(
            "El equipo de Ruta Andina prospecta sólo cuando el pipeline baja. El resultado es un ciclo de "
            "abundancia y sequía con 40 % de variación trimestral en cierres."
        ),
        limite=(
            "Volumen sin calidad de lista produce ruido y daña la reputación del dominio. La disciplina de "
            "actividad supone que la lista ya fue filtrada por perfil."
        ),
        libros=["blount", "weinberg-sales", "ross", "bertuzzi"],
        error=("Prospectar sólo cuando falta pipeline",
               "Fija una cadencia semanal mínima e inamovible, calculada desde el retardo observado."),
    ),
    dict(
        n="03",
        slug="apertura-y-rapport",
        titulo="Apertura y rapport",
        tesis=(
            "La apertura de una conversación comercial cumple tres funciones: establecer legitimidad, "
            "explicitar el propósito y acordar la agenda. El rapport genuino no proviene de simpatía forzada "
            "sino de demostrar preparación: haber investigado, formular una hipótesis del problema y "
            "reconocer el tiempo del interlocutor. Rackham observó que dedicar la apertura a hablar del "
            "propio producto reduce la calidad de la información obtenida después."
        ),
        conceptos=[
            ("legitimidad", "razón creíble por la que esta conversación merece el tiempo del cliente"),
            ("acuerdo de agenda", "explicitación de objetivo, duración y siguiente paso al inicio de la reunión"),
            ("hipótesis de problema", "suposición informada sobre la dificultad del cliente, presentada para ser corregida"),
            ("escucha calibrada", "capacidad de sostener el silencio y repreguntar en lugar de completar la respuesta"),
        ],
        metodo=[
            "investigar antes de la reunión y formular una hipótesis",
            "abrir con propósito, duración y acuerdo de agenda",
            "presentar la hipótesis pidiendo corrección",
            "escuchar sin ofrecer solución prematura",
            "cerrar la apertura con permiso explícito para indagar",
        ],
        senales=[
            ("proporción de tiempo hablado por el cliente", "minutos del cliente sobre minutos totales de la reunión, medido en grabaciones"),
            ("reuniones con agenda acordada", "reuniones con agenda explicitada al inicio, sobre reuniones sostenidas"),
            ("tasa de avance tras la primera reunión", "reuniones que producen un siguiente paso acordado, sobre reuniones realizadas"),
        ],
        caso=(
            "Las grabaciones de Ruta Andina muestran que el vendedor habla el 78 % del tiempo en la primera "
            "reunión y presenta el producto en el minuto tres."
        ),
        limite=(
            "El rapport no reemplaza el ajuste: una relación excelente con un cliente que no pertenece al perfil "
            "produce un negocio que fracasará en la implementación."
        ),
        libros=["rackham", "voss", "keenan", "cialdini"],
        error=("Presentar el producto en los primeros minutos",
               "Reserva la presentación hasta después del diagnóstico y acuerda agenda al inicio."),
    ),
    dict(
        n="04",
        slug="discovery",
        titulo="Discovery",
        tesis=(
            "El discovery es la etapa donde se determina si existe un problema que valga la pena resolver, "
            "cuánto cuesta hoy y qué pasaría si no se resuelve. Rackham demostró que en ventas complejas las "
            "preguntas de implicación son las que más se asocian al éxito. La razón es que construyen la "
            "urgencia sobre evidencia del propio cliente y no sobre presión del vendedor. Un diagnóstico sin "
            "cifra estimada por el cliente deja la conversación de precio sin referencia y la convierte en "
            "regateo."
        ),
        conceptos=[
            ("situación actual", "descripción factual del proceso y los recursos que el cliente usa hoy"),
            ("problema declarado", "dificultad que el cliente reconoce explícitamente"),
            ("implicación", "consecuencia del problema en costo, riesgo, tiempo o reputación"),
            ("costo de no actuar", "pérdida cuantificada que el cliente asume si mantiene la situación actual"),
        ],
        metodo=[
            "documentar la situación actual con datos del cliente",
            "identificar el problema en las palabras del cliente",
            "explorar implicaciones sin sugerir la solución",
            "cuantificar el costo de no actuar",
            "confirmar el diagnóstico por escrito antes de proponer",
        ],
        senales=[
            ("costo de no actuar cuantificado", "oportunidades con cifra estimada por el cliente, sobre oportunidades calificadas"),
            ("preguntas de implicación por reunión", "preguntas de consecuencia registradas, sobre preguntas totales, en grabaciones"),
            ("tasa de cierre con diagnóstico confirmado", "negocios ganados con diagnóstico escrito confirmado, sobre negocios con diagnóstico"),
        ],
        caso=(
            "Un taller de Valparaíso pierde seis citas semanales. El vendedor de Ruta Andina nunca preguntó "
            "cuánto factura una cita ni qué pasa cuando el cliente no vuelve."
        ),
        limite=(
            "El discovery excesivo agota al cliente. En negocios pequeños, tres preguntas bien elegidas superan "
            "a un cuestionario de veinte."
        ),
        libros=["rackham", "keenan", "dixon-challenger", "fitzpatrick"],
        error=("Proponer solución antes de cuantificar el problema",
               "Exige una cifra estimada por el cliente antes de pasar a la demostración."),
    ),
    dict(
        n="05",
        slug="calificacion-de-oportunidades",
        titulo="Calificación de oportunidades",
        tesis=(
            "Calificar es decidir en qué invertir tiempo comercial, que es el recurso más escaso del equipo. "
            "Una buena calificación descalifica temprano y sin drama: reconoce que no hay problema "
            "suficiente, presupuesto, autoridad o plazo. El costo de no descalificar no es sólo el tiempo "
            "perdido: es un forecast inflado que induce decisiones equivocadas de contratación y de gasto."
        ),
        conceptos=[
            ("criterio de calificación", "condición verificable que debe cumplirse para invertir tiempo comercial"),
            ("descalificación temprana", "cierre deliberado de una oportunidad que no cumple criterios, antes de invertir esfuerzo"),
            ("costo de oportunidad comercial", "valor de los negocios no trabajados por dedicar tiempo a los no calificados"),
            ("evidencia de calificación", "dato observable que respalda cada criterio y no la impresión del vendedor"),
        ],
        metodo=[
            "definir los criterios mínimos y su evidencia",
            "aplicar la calificación en la primera reunión",
            "descalificar explícitamente lo que no cumple",
            "revisar mensualmente la precisión de la calificación",
            "ajustar los criterios con datos de resultado",
        ],
        senales=[
            ("tasa de descalificación temprana", "oportunidades cerradas por descalificación antes de la propuesta, sobre oportunidades creadas"),
            ("precisión de la calificación", "negocios ganados entre los calificados, comparado con ganados entre los no calificados"),
            ("tiempo comercial en no calificados", "horas dedicadas a oportunidades sin criterios cumplidos, sobre horas comerciales totales"),
        ],
        caso=(
            "El pipeline de Ruta Andina tiene 380 oportunidades abiertas; 44 % sin actividad en 30 días. "
            "Nadie las cierra porque «podrían reactivarse»."
        ),
        limite=(
            "Una calificación demasiado estricta descarta negocios que podrían desarrollarse. El criterio debe "
            "distinguir entre no calificado hoy y no calificado nunca."
        ),
        libros=["miller-heiman", "roberge", "keenan", "ross"],
        error=("Mantener abiertas oportunidades sin actividad",
               "Fija una regla de cierre automático por inactividad y revisa su efecto en la precisión del forecast."),
    ),
    dict(
        n="06",
        slug="demostracion-de-valor",
        titulo="Demostración de valor",
        tesis=(
            "Una demostración no es un recorrido por funcionalidades: es la representación de cómo cambia el "
            "día del cliente. La regla operativa es mostrar sólo lo que responde al diagnóstico confirmado y "
            "en el orden de prioridad del cliente. Una demo genérica trasmite un mensaje involuntario: que el "
            "vendedor no escuchó, o que el producto es igual para todos."
        ),
        conceptos=[
            ("demo diagnóstica", "demostración construida a partir del problema confirmado del cliente"),
            ("escenario del cliente", "situación real y datos del cliente utilizados durante la demostración"),
            ("orden de prioridad", "secuencia de temas que refleja lo que el cliente declaró más importante"),
            ("compromiso posterior", "siguiente paso concreto acordado al finalizar la demostración"),
        ],
        metodo=[
            "confirmar el diagnóstico antes de agendar la demo",
            "construir el escenario con datos del cliente",
            "mostrar sólo lo que responde al diagnóstico",
            "verificar comprensión durante la demostración",
            "cerrar con un compromiso posterior explícito",
        ],
        senales=[
            ("tasa de avance post demostración", "oportunidades que avanzan de etapa, sobre demostraciones realizadas"),
            ("demostraciones con escenario del cliente", "demos que usaron datos del cliente, sobre demos realizadas"),
            ("duración media de la demostración", "minutos por demostración, comparados con la tasa de avance"),
        ],
        caso=(
            "La demo estándar de Ruta Andina dura 45 minutos y recorre nueve módulos. La conversión posterior "
            "es 31 %; en las cinco demos personalizadas del último trimestre fue 60 %."
        ),
        limite=(
            "Personalizar cada demostración es costoso. En segmentos de ticket bajo conviene una versión breve "
            "y estandarizada, con dos o tres variantes por caso de uso."
        ),
        libros=["rackham", "keenan", "dixon-challenger", "krug"],
        error=("Recorrer todas las funcionalidades",
               "Muestra sólo lo que responde al diagnóstico confirmado y verifica comprensión en el camino."),
    ),
    dict(
        n="07",
        slug="presentaciones-comerciales",
        titulo="Presentaciones comerciales",
        tesis=(
            "Una presentación comercial debe poder circular sin su autor, porque casi siempre lo hará: el "
            "contacto la reenviará a personas que no estuvieron en la reunión. Eso obliga a estructurarla "
            "alrededor del problema del cliente, con evidencia, opciones y consecuencias, y no alrededor de "
            "la historia de la empresa. La primera lámina debe permitir a un tercero entender de qué se trata "
            "la decisión."
        ),
        conceptos=[
            ("documento autónomo", "material que se comprende sin la presencia de quien lo elaboró"),
            ("estructura decisional", "orden que va del problema a las opciones y a la recomendación"),
            ("evidencia citada", "dato con fuente que respalda cada afirmación relevante"),
            ("audiencia secundaria", "personas que leerán el documento sin haber participado en la conversación"),
        ],
        metodo=[
            "definir la decisión que la presentación debe habilitar",
            "estructurar desde el problema del cliente",
            "incluir evidencia y opciones con consecuencias",
            "probar la comprensión con alguien ajeno al negocio",
            "medir si el documento circula y con qué efecto",
        ],
        senales=[
            ("tasa de circulación interna", "negocios donde el documento llegó a personas no presentes, sobre negocios con propuesta"),
            ("comprensión por audiencia secundaria", "personas ajenas que explican correctamente la propuesta, en prueba con muestra definida"),
            ("tiempo hasta respuesta del comité", "días entre el envío del documento y la respuesta formal del cliente"),
        ],
        caso=(
            "La presentación de Ruta Andina dedica 8 de 14 láminas a la historia de la empresa. El gerente de "
            "finanzas de la cadena la revisó sin contexto y no encontró el costo total."
        ),
        limite=(
            "Un documento completamente autónomo tiende a ser largo. La solución es una versión ejecutiva de "
            "una página con anexo, no un documento único que intente todo."
        ),
        libros=["ellet", "heath", "handley", "dixon-customer"],
        error=("Estructurar la presentación desde la empresa",
               "Abre con el problema del cliente y su costo, y deja la credencial institucional en anexo."),
    ),
    dict(
        n="08",
        slug="propuestas-comerciales",
        titulo="Propuestas comerciales",
        tesis=(
            "Una propuesta comercial es un documento con consecuencias contractuales: define alcance, precio, "
            "plazos, supuestos y exclusiones. Su ambigüedad se paga después, en implementación y en reclamos. "
            "En Chile, además, las condiciones ofrecidas obligan al proveedor: la información entregada al "
            "consumidor debe ser veraz, oportuna y comprobable, y las cláusulas abusivas son inoponibles."
        ),
        conceptos=[
            ("alcance explícito", "descripción de lo incluido y lo excluido, con sus condiciones"),
            ("supuesto declarado", "condición que se asume verdadera y que altera el precio o el plazo si no se cumple"),
            ("vigencia de la oferta", "periodo durante el cual las condiciones ofrecidas se mantienen"),
            ("obligación derivada", "compromiso jurídico que nace de lo ofrecido por escrito"),
        ],
        metodo=[
            "redactar alcance, exclusiones y supuestos",
            "definir precio, forma de pago y vigencia",
            "revisar coherencia con la capacidad operativa",
            "verificar cumplimiento normativo de las condiciones",
            "obtener aceptación escrita y archivarla",
        ],
        senales=[
            ("propuestas con alcance completo", "propuestas con inclusiones, exclusiones y supuestos, sobre propuestas emitidas"),
            ("desviación entre propuesta e implementación", "casos con alcance ampliado sin cobro, sobre proyectos implementados"),
            ("tasa de aceptación dentro de vigencia", "aceptaciones dentro del plazo de vigencia, sobre propuestas emitidas"),
        ],
        caso=(
            "Las propuestas de Ruta Andina no mencionan la migración de datos. El 40 % de los proyectos la "
            "ejecuta igual, sin cobro, consumiendo 9 horas por cliente."
        ),
        limite=(
            "Una propuesta exhaustiva puede volverse ilegible. La solución es una página comercial clara con "
            "anexo de condiciones, no eliminar las condiciones."
        ),
        libros=["nagle", "fisher-ury", "ellet", "handley"],
        error=("Omitir exclusiones para no complicar el cierre",
               "Declara exclusiones y supuestos en la propuesta: lo omitido se cobra después en operación o en reclamo."),
    ),
    dict(
        n="09",
        slug="manejo-de-objeciones",
        titulo="Manejo de objeciones",
        tesis=(
            "El manejo de objeciones no es una batalla verbal: es un procedimiento de clarificación. La "
            "secuencia útil es reconocer, entender la causa, verificar si es la razón real, responder con "
            "evidencia y confirmar si quedó resuelta. Rackham encontró que en ventas grandes la cantidad de "
            "objeciones se asocia negativamente al éxito: son consecuencia de un diagnóstico débil, no una "
            "etapa inevitable."
        ),
        conceptos=[
            ("causa raíz de la objeción", "razón subyacente que explica la resistencia y que puede diferir de lo enunciado"),
            ("pregunta de verificación", "consulta que confirma si la objeción declarada es el impedimento real"),
            ("respuesta con evidencia", "contestación basada en dato, caso o garantía verificable"),
            ("confirmación de resolución", "verificación explícita de que la objeción dejó de ser un obstáculo"),
        ],
        metodo=[
            "reconocer la objeción sin discutir",
            "indagar la causa raíz con preguntas abiertas",
            "verificar si es el impedimento real",
            "responder con evidencia verificable",
            "confirmar la resolución y registrar el caso",
        ],
        senales=[
            ("objeciones por negocio", "objeciones registradas, sobre negocios trabajados en el periodo"),
            ("tasa de resolución confirmada", "objeciones con confirmación explícita de resolución, sobre objeciones registradas"),
            ("reaparición de la misma objeción", "objeciones repetidas en etapas posteriores, sobre objeciones resueltas"),
        ],
        caso=(
            "«Lo voy a conversar internamente» aparece en el 70 % de los negocios de Ruta Andina que luego se "
            "estancan. Nadie pregunta con quién ni qué necesita esa persona."
        ),
        limite=(
            "Insistir ante una objeción real y bien fundada deteriora la relación. Algunas objeciones son "
            "señales correctas de que el negocio no debe avanzar."
        ),
        libros=["rackham", "voss", "keenan", "cialdini"],
        error=("Responder la objeción declarada sin verificar la real",
               "Formula una pregunta de verificación antes de responder cualquier objeción."),
    ),
    dict(
        n="10",
        slug="seguimiento",
        titulo="Seguimiento",
        tesis=(
            "El seguimiento es donde se pierden más negocios que en el cierre. Un seguimiento profesional "
            "aporta valor en cada contacto —un dato, una respuesta, un caso comparable— y tiene un ritmo "
            "acordado con el cliente. El seguimiento sin aporte —«te escribo para saber si viste mi correo»— "
            "consume credibilidad y entrena al cliente a no responder."
        ),
        conceptos=[
            ("contacto con aporte", "comunicación de seguimiento que entrega algo útil independientemente de la respuesta"),
            ("ritmo acordado", "frecuencia y canal de seguimiento pactados explícitamente con el cliente"),
            ("siguiente paso comprometido", "acción concreta con fecha acordada al cierre de cada interacción"),
            ("regla de cierre", "criterio que define cuándo dejar de insistir y cerrar la oportunidad"),
        ],
        metodo=[
            "acordar el siguiente paso y su fecha en cada interacción",
            "definir el ritmo de seguimiento con el cliente",
            "preparar un aporte concreto para cada contacto",
            "registrar cada intento y su resultado",
            "aplicar la regla de cierre cuando corresponda",
        ],
        senales=[
            ("oportunidades con siguiente paso agendado", "oportunidades abiertas con fecha comprometida, sobre oportunidades abiertas"),
            ("tasa de respuesta al seguimiento", "respuestas obtenidas, sobre contactos de seguimiento realizados"),
            ("edad media del pipeline", "días promedio desde la creación de las oportunidades abiertas"),
        ],
        caso=(
            "El 44 % de las oportunidades de Ruta Andina no tiene actividad en 30 días y ninguna tiene "
            "siguiente paso agendado en el CRM."
        ),
        limite=(
            "Un seguimiento excesivo puede constituir hostigamiento y afecta la reputación. La frecuencia debe "
            "ser acordada y respetar la solicitud de no contacto."
        ),
        libros=["blount", "weinberg-sales", "roberge", "ross"],
        error=("Hacer seguimiento sin aporte",
               "Prepara un dato, un caso o una respuesta concreta para cada contacto de seguimiento."),
    ),
    dict(
        n="11",
        slug="cierre",
        titulo="Cierre",
        tesis=(
            "El cierre no es una técnica de presión sino la consecuencia natural de un proceso bien "
            "ejecutado: si el problema fue cuantificado, la solución fue verificada y el comité fue "
            "involucrado, el cierre es un trámite. Rackham mostró que las técnicas de cierre agresivo "
            "aumentan la conversión en ventas pequeñas y la reducen en ventas grandes, donde generan "
            "desconfianza."
        ),
        conceptos=[
            ("cierre natural", "acuerdo que resulta de haber resuelto problema, valor, riesgo y proceso"),
            ("señal de compra", "comportamiento del cliente que indica disposición a avanzar"),
            ("plan mutuo", "cronograma acordado con el cliente que detalla pasos, responsables y fechas hasta la firma"),
            ("presión indebida", "técnica que induce a decidir sin información suficiente o con urgencia artificial"),
        ],
        metodo=[
            "verificar que las condiciones previas están resueltas",
            "acordar el plan mutuo con el cliente",
            "identificar y confirmar señales de compra",
            "solicitar la decisión de forma directa y respetuosa",
            "documentar el acuerdo y sus condiciones",
        ],
        senales=[
            ("tasa de cierre por etapa de origen", "negocios ganados, sobre oportunidades que alcanzaron cada etapa"),
            ("negocios con plan mutuo", "negocios cerrados con plan mutuo acordado, sobre negocios cerrados"),
            ("tiempo entre propuesta y decisión", "días entre el envío de la propuesta y la respuesta, mediana"),
        ],
        caso=(
            "El equipo de Ruta Andina cierra con descuentos de última hora y plazos artificiales. Los clientes "
            "de la cadena ya esperan esa oferta y postergan la decisión hasta fin de mes."
        ),
        limite=(
            "La urgencia artificial y las condiciones que caducan sin razón real pueden constituir prácticas "
            "engañosas y deterioran la relación con el gremio."
        ),
        libros=["rackham", "fisher-ury", "keenan", "cialdini"],
        error=("Crear urgencia artificial para cerrar",
               "Sustituye el plazo inventado por un plan mutuo con hitos reales acordados con el cliente."),
    ),
    dict(
        n="12",
        slug="handoff-a-implementacion",
        titulo="Handoff a implementación",
        tesis=(
            "El traspaso de ventas a implementación es uno de los puntos de fuga más caros: allí se pierde el "
            "contexto que costó semanas construir y aparecen las promesas no documentadas. Un handoff "
            "profesional transfiere diagnóstico, expectativas, riesgos y compromisos por escrito, con una "
            "reunión conjunta y un responsable identificado en cada lado."
        ),
        conceptos=[
            ("documento de traspaso", "registro estructurado de diagnóstico, compromisos, riesgos y contactos"),
            ("compromiso no documentado", "promesa verbal del proceso de venta que la operación desconoce"),
            ("expectativa transferida", "resultado que el cliente espera y que debe ser conocido por quien implementa"),
            ("responsable de continuidad", "persona designada en cada lado para sostener la relación tras la firma"),
        ],
        metodo=[
            "documentar diagnóstico, alcance y compromisos al cierre",
            "realizar una reunión conjunta con el cliente",
            "identificar riesgos de implementación y su mitigación",
            "designar responsables de continuidad",
            "medir la fidelidad del traspaso a los 30 días",
        ],
        senales=[
            ("traspasos con documento completo", "cierres con documento de traspaso, sobre cierres del periodo"),
            ("incidencias por promesa no documentada", "casos de implementación con compromisos no registrados, sobre proyectos iniciados"),
            ("satisfacción a 30 días", "puntuación de satisfacción de clientes nuevos al mes de la firma"),
        ],
        caso=(
            "El 61 % de las bajas tempranas de Ruta Andina corresponde a clientes cuya implementación no supo "
            "qué se les había prometido durante la venta."
        ),
        limite=(
            "Un traspaso burocrático que agrega reuniones sin transferir contexto no resuelve el problema. Lo "
            "esencial es el documento y la reunión conjunta con el cliente presente."
        ),
        libros=["mehta", "roberge", "hulick", "diorio"],
        error=("Traspasar sin reunión conjunta con el cliente",
               "Incluye al cliente en la reunión de traspaso para verificar expectativas frente a ambas partes."),
    ),
    dict(
        n="13",
        slug="disciplina-crm",
        titulo="Disciplina de CRM",
        tesis=(
            "El CRM sólo vale lo que vale su dato. La disciplina de registro no es burocracia: es la condición "
            "para que exista forecast, análisis de conversión y continuidad cuando alguien sale del equipo. "
            "El error de gestión más frecuente es exigir registro sin devolver valor al vendedor: si el "
            "sistema sólo sirve para controlar, el dato se degrada de inmediato."
        ),
        conceptos=[
            ("campo crítico", "dato sin el cual no puede calcularse forecast ni conversión"),
            ("higiene de datos", "conjunto de reglas que mantiene el registro completo, actualizado y sin duplicados"),
            ("valor devuelto al usuario", "beneficio concreto que el vendedor obtiene del sistema por registrar bien"),
            ("registro oportuno", "actualización realizada dentro del plazo definido tras cada interacción"),
        ],
        metodo=[
            "definir el conjunto mínimo de campos críticos",
            "eliminar los campos que nadie usa",
            "devolver valor al vendedor con vistas y alertas útiles",
            "medir completitud y oportunidad del registro",
            "corregir el proceso antes de sancionar a la persona",
        ],
        senales=[
            ("completitud de campos críticos", "registros con todos los campos críticos completos, sobre registros creados"),
            ("oportunidad del registro", "interacciones registradas dentro del plazo definido, sobre interacciones registradas"),
            ("duplicados detectados", "registros duplicados, sobre registros totales de la base"),
        ],
        caso=(
            "El CRM de Ruta Andina exige 23 campos obligatorios. Los vendedores completan con datos falsos "
            "para poder guardar y el forecast se construye sobre esa base."
        ),
        limite=(
            "Más campos no es más control: cada campo obligatorio adicional reduce la calidad del conjunto. "
            "La disciplina se sostiene con pocos campos que realmente se usan."
        ),
        libros=["roberge", "diorio", "grove", "provost"],
        error=("Exigir registro sin devolver valor",
               "Reduce los campos obligatorios al mínimo y entrega vistas que el vendedor use para trabajar."),
    ),
    dict(
        n="14",
        slug="playbook-comercial-basico",
        titulo="Playbook comercial básico",
        tesis=(
            "Esta clase integra la parte en un playbook operativo: etapas, criterios de salida, guiones de "
            "discovery, materiales por etapa, objeciones frecuentes con respuesta y reglas de CRM. La prueba "
            "de calidad es que una persona nueva pueda ejecutar su primer negocio con el playbook y sin "
            "acompañamiento constante."
        ),
        conceptos=[
            ("playbook operativo", "documento que permite ejecutar el proceso comercial sin depender del conocimiento tácito"),
            ("guion de discovery", "conjunto de preguntas ordenadas por objetivo, no un cuestionario rígido"),
            ("biblioteca de objeciones", "registro de objeciones frecuentes con su verificación y su respuesta con evidencia"),
            ("prueba de incorporación", "verificación de que una persona nueva ejecuta correctamente con el documento"),
        ],
        metodo=[
            "consolidar etapas, criterios y materiales",
            "documentar guiones y objeciones con evidencia",
            "definir las reglas mínimas de CRM",
            "ejecutar la prueba con una persona nueva",
            "corregir lo que no resultó ejecutable y versionar el documento",
        ],
        senales=[
            ("tiempo hasta el primer negocio", "días desde la incorporación hasta el primer cierre, por vendedor"),
            ("uso del playbook", "materiales del playbook utilizados en negocios activos, sobre materiales disponibles"),
            ("reducción de dispersión de desempeño", "desviación estándar de la tasa de cierre entre vendedores, comparada entre el trimestre previo y el posterior"),
        ],
        caso=(
            "Ruta Andina incorpora dos ejecutivos comerciales el próximo mes. Hoy el proceso vive en la "
            "memoria de dos personas y en conversaciones de chat."
        ),
        limite=(
            "Un playbook desactualizado es peor que ninguno porque induce errores con autoridad. Necesita "
            "responsable, versión y revisión trimestral."
        ),
        libros=["roberge", "weinberg-sales", "rackham", "bertuzzi"],
        error=("Publicar el playbook sin prueba de incorporación",
               "Haz que una persona nueva ejecute un negocio completo con el documento antes de darlo por válido."),
    ),
]
