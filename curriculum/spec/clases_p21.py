# -*- coding: utf-8 -*-
"""Parte 21 — IA aplicada a marketing, ventas y servicio."""

CLASES = [
    dict(
        n="01",
        slug="mapa-de-ia-comercial",
        titulo="Mapa de IA comercial",
        tesis=(
            "La inteligencia artificial aplicada a lo comercial cubre tareas muy distintas: generación de "
            "texto, clasificación, predicción, recuperación de información y automatización de acciones. "
            "Cada una tiene requisitos, riesgos y formas de evaluación propias. Tratar todo como «usar IA» "
            "impide decidir: la pregunta correcta es qué tarea concreta mejora, con qué evidencia y quién "
            "responde cuando falla."
        ),
        conceptos=[
            ("tarea automatizable", "actividad concreta con entrada y salida definidas que un sistema puede ejecutar"),
            ("tipo de sistema", "clasificación según lo que hace: genera, clasifica, predice, recupera o actúa"),
            ("criterio de éxito", "definición operacional de qué significa que el sistema funcione bien"),
            ("responsabilidad humana", "persona que responde por el resultado con independencia de la automatización"),
        ],
        metodo=[
            "inventariar tareas comerciales candidatas",
            "clasificar cada una por tipo de sistema requerido",
            "definir el criterio de éxito y el costo del error",
            "asignar responsable humano por cada uso",
            "priorizar por valor y por riesgo controlable",
        ],
        senales=[
            ("casos de uso con criterio de éxito", "usos con métrica de evaluación definida, sobre usos activos"),
            ("costo del error por caso", "consecuencia estimada de una salida incorrecta, por caso de uso"),
            ("usos con responsable asignado", "casos con responsable humano nombrado, sobre casos activos"),
        ],
        caso=(
            "Ruta Andina «adoptó IA» activando un asistente en soporte, un generador de textos y un modelo de "
            "puntuación. Ninguno tiene criterio de éxito ni responsable definido."
        ),
        limite=(
            "La IA no resuelve problemas de proceso ni de datos: los amplifica. Automatizar sobre información "
            "de mala calidad produce errores más rápido."
        ),
        libros=["russell-norvig", "nist-airmf", "provost", "ng-mlyearning"],
        error=("Adoptar herramientas sin definir la tarea ni el criterio de éxito",
               "Declara la tarea, su métrica de evaluación y su responsable antes de activar cualquier sistema."),
    ),
    dict(
        n="02",
        slug="prompting-con-contexto-comercial",
        titulo="Prompting con contexto comercial",
        tesis=(
            "La calidad de una salida generativa depende del contexto entregado: rol, objetivo, audiencia, "
            "restricciones, ejemplos y criterios de aceptación. Un prompt vago produce texto genérico que "
            "requiere más trabajo de edición que escribir desde cero. En contexto comercial hay una "
            "restricción adicional: el contexto entregado puede incluir datos de clientes, y eso exige "
            "verificar qué información puede compartirse con un servicio externo."
        ),
        conceptos=[
            ("contexto suficiente", "información mínima que el sistema necesita para producir una salida útil"),
            ("criterio de aceptación", "condiciones que la salida debe cumplir para considerarse válida"),
            ("plantilla reutilizable", "estructura de instrucción documentada que produce resultados consistentes"),
            ("dato sensible en el contexto", "información de clientes o del negocio que no debe compartirse externamente"),
        ],
        metodo=[
            "definir objetivo, audiencia y restricciones",
            "verificar qué datos pueden incluirse en el contexto",
            "incorporar ejemplos y criterios de aceptación",
            "documentar la plantilla que funciona",
            "revisar la salida contra los criterios antes de usarla",
        ],
        senales=[
            ("tasa de aceptación de salidas", "salidas usables sin edición mayor, sobre salidas generadas"),
            ("tiempo de edición posterior", "minutos de corrección por pieza generada"),
            ("plantillas documentadas", "instrucciones estandarizadas en uso, sobre casos de uso activos"),
        ],
        caso=(
            "Un ejecutivo de Ruta Andina pegó la lista completa de clientes con sus datos de contacto en una "
            "herramienta externa para que redactara correos personalizados."
        ),
        limite=(
            "Mejores instrucciones no corrigen un modelo que carece de la información necesaria. Cuando el "
            "conocimiento no está disponible, el sistema inventará una respuesta plausible."
        ),
        libros=["ng-mlyearning", "nist-airmf", "handley", "russell-norvig"],
        error=("Incluir datos de clientes en el contexto sin verificar la política de tratamiento",
               "Define qué categorías de datos pueden compartirse y anonimiza antes de usar servicios externos."),
    ),
    dict(
        n="03",
        slug="investigacion-asistida-por-ia",
        titulo="Investigación asistida por IA",
        tesis=(
            "Los sistemas generativos aceleran la revisión de información y producen afirmaciones plausibles "
            "que pueden ser falsas. En investigación comercial eso es especialmente peligroso: una cifra de "
            "mercado inventada puede sostener una decisión de inversión. La regla operativa es simple y no "
            "negociable: toda afirmación factual usada en una decisión debe verificarse en su fuente "
            "primaria."
        ),
        conceptos=[
            ("afirmación plausible", "salida que suena correcta y puede no corresponder a ningún hecho"),
            ("verificación en fuente primaria", "comprobación de la afirmación en el documento original"),
            ("uso legítimo", "tareas donde el error es barato de detectar y corregir"),
            ("trazabilidad de la evidencia", "registro de qué afirmación provino de qué fuente verificada"),
        ],
        metodo=[
            "usar el sistema para ordenar y explorar, no para establecer hechos",
            "marcar toda afirmación factual como pendiente de verificación",
            "verificar en fuente primaria antes de usarla en una decisión",
            "registrar la fuente junto a la afirmación",
            "descartar lo que no se pudo verificar",
        ],
        senales=[
            ("afirmaciones verificadas", "afirmaciones comprobadas en fuente primaria, sobre afirmaciones usadas"),
            ("tasa de error detectado", "afirmaciones incorrectas encontradas en la verificación, sobre afirmaciones verificadas"),
            ("tiempo de verificación", "minutos de comprobación por afirmación factual"),
        ],
        caso=(
            "Un informe de Ruta Andina incluía tres cifras de mercado generadas por un asistente. Ninguna "
            "correspondía a una fuente real y una llegó a una presentación al directorio."
        ),
        limite=(
            "La verificación tiene costo y no todas las afirmaciones lo justifican. El criterio es el costo "
            "del error: cuanto más pesa en la decisión, más rigurosa debe ser la comprobación."
        ),
        libros=["ng-mlyearning", "oneil", "hubbard", "provost"],
        error=("Usar cifras generadas sin verificar la fuente",
               "Marca toda afirmación factual y verifícala en fuente primaria antes de incorporarla a un informe."),
    ),
    dict(
        n="04",
        slug="generacion-de-contenido-con-controles",
        titulo="Generación de contenido con controles",
        tesis=(
            "Generar contenido con IA multiplica el volumen y también el riesgo: afirmaciones sin respaldo, "
            "promesas comerciales que la empresa no puede cumplir, textos que infringen normas de publicidad. "
            "El control no puede ser posterior y aleatorio: debe ser un paso obligatorio del flujo, con "
            "criterios explícitos y responsable identificado."
        ),
        conceptos=[
            ("control de afirmaciones", "verificación obligatoria del respaldo de cada afirmación antes de publicar"),
            ("responsable de publicación", "persona que responde por el contenido con independencia de quién lo generó"),
            ("riesgo de escala", "amplificación del daño cuando el error se replica en muchas piezas"),
            ("registro de origen", "documentación de qué contenido fue generado o asistido por un sistema"),
        ],
        metodo=[
            "definir qué tipos de contenido pueden generarse asistidamente",
            "establecer el control de afirmaciones como paso obligatorio",
            "asignar responsable humano de publicación",
            "registrar el origen de cada pieza",
            "auditar una muestra publicada cada mes",
        ],
        senales=[
            ("piezas con control aplicado", "contenidos revisados antes de publicar, sobre contenidos publicados"),
            ("afirmaciones corregidas en control", "correcciones realizadas, sobre piezas revisadas"),
            ("incidentes por contenido publicado", "reclamos o correcciones posteriores, sobre piezas publicadas"),
        ],
        caso=(
            "Ruta Andina publicó 40 artículos generados en un mes. Tres afirmaban compatibilidades "
            "inexistentes y uno prometía un plazo de implementación que la operación no cumple."
        ),
        limite=(
            "El control humano tiene capacidad limitada. Si el volumen generado supera la capacidad de "
            "revisión, la solución es reducir el volumen y no relajar el control."
        ),
        libros=["handley", "nist-airmf", "oneil", "godin"],
        error=("Publicar contenido generado sin control de afirmaciones",
               "Instala la revisión como paso obligatorio y ajusta el volumen a la capacidad real de control."),
    ),
    dict(
        n="05",
        slug="personalizacion",
        titulo="Personalización",
        tesis=(
            "La personalización mejora la pertinencia y puede cruzar rápidamente hacia lo invasivo. El "
            "límite no es técnico sino de expectativa: usar información que el cliente no sabe que la "
            "empresa posee produce desconfianza, aunque su obtención haya sido lícita. La regla práctica es "
            "personalizar con datos que el cliente entregó conscientemente y para la finalidad que conoce."
        ),
        conceptos=[
            ("pertinencia percibida", "grado en que el cliente considera útil la adaptación del mensaje"),
            ("expectativa de privacidad", "supuesto del cliente sobre qué información tiene la empresa y para qué"),
            ("finalidad declarada", "uso informado al momento de recoger el dato"),
            ("efecto inquietante", "reacción negativa ante una personalización que revela información inesperada"),
        ],
        metodo=[
            "identificar qué datos entregó el cliente conscientemente",
            "verificar la finalidad declarada al recogerlos",
            "diseñar la personalización dentro de esa expectativa",
            "probar la reacción con un grupo pequeño",
            "medir efecto en conversión y en bajas",
        ],
        senales=[
            ("efecto en conversión", "diferencia de conversión entre versión personalizada y estándar"),
            ("tasa de baja tras personalización", "bajas solicitadas, sobre destinatarios de la versión personalizada"),
            ("consultas sobre uso de datos", "consultas de clientes sobre el origen de la información, por periodo"),
        ],
        caso=(
            "Ruta Andina envió un correo mencionando la cantidad de citas canceladas de cada taller. Varios "
            "clientes preguntaron cómo obtuvieron ese dato y dos solicitaron eliminación."
        ),
        limite=(
            "La normativa de datos personales exige finalidad determinada e información al titular. La "
            "personalización basada en inferencias no declaradas es especialmente riesgosa."
        ),
        libros=["thaler", "oneil", "nist-airmf", "cialdini"],
        error=("Personalizar con datos fuera de la finalidad declarada",
               "Limita la personalización a datos entregados conscientemente y para el uso informado."),
    ),
    dict(
        n="06",
        slug="lead-research",
        titulo="Investigación de prospectos asistida",
        tesis=(
            "La investigación asistida de prospectos ahorra tiempo real: resume información pública, "
            "identifica señales y prepara contexto para el contacto. Sus riesgos son dos: afirmaciones "
            "inventadas sobre una empresa concreta, que dañan la credibilidad del vendedor en el primer "
            "contacto, y recolección excesiva de información personal sin finalidad legítima."
        ),
        conceptos=[
            ("señal verificable", "hecho comprobable sobre el prospecto que justifica el contacto"),
            ("afirmación no verificada", "dato generado que no fue comprobado antes de usarse"),
            ("proporcionalidad de la recolección", "límite de información recabada según la finalidad del contacto"),
            ("verificación previa al contacto", "comprobación de los datos antes de mencionarlos al prospecto"),
        ],
        metodo=[
            "definir qué señales importan para el perfil objetivo",
            "usar el sistema para reunir y resumir información pública",
            "verificar cada dato antes de mencionarlo",
            "limitar la recolección a lo proporcional",
            "medir el efecto en la tasa de respuesta",
        ],
        senales=[
            ("datos verificados antes del contacto", "datos comprobados, sobre datos mencionados en el contacto"),
            ("tasa de respuesta con investigación asistida", "respuestas obtenidas, comparadas con contactos sin investigación"),
            ("errores factuales detectados", "datos incorrectos encontrados en la verificación, sobre datos generados"),
        ],
        caso=(
            "Un correo de Ruta Andina felicitaba a un taller por una expansión que nunca ocurrió. El dato "
            "provino de un resumen generado y nadie lo verificó."
        ),
        limite=(
            "La información pública sobre personas sigue siendo dato personal. Su tratamiento requiere "
            "finalidad legítima y no se vuelve libre por estar disponible."
        ),
        libros=["blount", "nist-airmf", "oneil", "provost"],
        error=("Mencionar datos generados sin verificarlos",
               "Verifica cada hecho antes de citarlo en un contacto comercial."),
    ),
    dict(
        n="07",
        slug="lead-scoring-asistido",
        titulo="Lead scoring asistido por modelos",
        tesis=(
            "Un modelo predictivo puede superar a las reglas manuales cuando hay volumen suficiente y datos "
            "de calidad. Sus riesgos son conocidos: aprende de la historia y reproduce sus sesgos; si la "
            "prospección pasada ignoró un segmento, el modelo lo seguirá subvalorando. Requiere validación "
            "periódica, explicabilidad suficiente para que ventas confíe y supervisión humana."
        ),
        conceptos=[
            ("sesgo histórico", "reproducción de patrones del pasado que pueden ser injustos o subóptimos"),
            ("explicabilidad", "capacidad de indicar qué factores influyeron en la puntuación"),
            ("deriva del modelo", "pérdida de precisión por cambios en el mercado o en el proceso"),
            ("supervisión humana", "revisión de decisiones del modelo por una persona responsable"),
        ],
        metodo=[
            "verificar volumen y calidad de datos antes de modelar",
            "evaluar el desempeño frente a la regla manual actual",
            "revisar el sesgo por segmento",
            "monitorear la deriva y recalibrar",
            "mantener supervisión humana sobre las decisiones",
        ],
        senales=[
            ("desempeño frente a la regla actual", "diferencia de precisión entre el modelo y la regla manual"),
            ("desempeño por segmento", "precisión del modelo, comparada entre segmentos"),
            ("deriva observada", "variación de la precisión del modelo entre periodos sucesivos"),
        ],
        caso=(
            "El modelo de Ruta Andina asigna puntajes bajos a los talleres de regiones porque históricamente "
            "se les prospectó menos, no porque conviertan peor."
        ),
        limite=(
            "Un modelo que no puede explicarse no será usado por el equipo comercial. La explicabilidad no es "
            "un lujo: determina la adopción."
        ),
        libros=["provost", "ng-mlyearning", "oneil", "nist-airmf"],
        error=("Desplegar el modelo sin revisar el sesgo por segmento",
               "Compara el desempeño entre segmentos y corrige antes de usarlo para priorizar."),
    ),
    dict(
        n="08",
        slug="copilotos-de-ventas",
        titulo="Copilotos de ventas",
        tesis=(
            "Un copiloto comercial asiste en tareas concretas: preparar reuniones, redactar seguimientos, "
            "resumir conversaciones, sugerir siguientes pasos. Su valor es real y su riesgo también: si "
            "produce contenido que el vendedor envía sin revisar, la empresa queda comprometida por "
            "afirmaciones que nadie verificó. La regla es que el humano responde por lo que envía."
        ),
        conceptos=[
            ("asistencia en tarea", "apoyo en una actividad específica sin sustituir la decisión"),
            ("revisión obligatoria", "verificación humana antes de enviar cualquier salida al cliente"),
            ("compromiso derivado", "obligación que nace de lo afirmado en una comunicación comercial"),
            ("registro de la asistencia", "documentación de qué fue generado y quién lo aprobó"),
        ],
        metodo=[
            "definir en qué tareas se permite la asistencia",
            "establecer la revisión humana obligatoria antes del envío",
            "capacitar sobre los errores típicos del sistema",
            "registrar el origen de las comunicaciones",
            "medir tiempo ahorrado y errores evitados",
        ],
        senales=[
            ("comunicaciones revisadas antes del envío", "salidas verificadas por una persona, sobre salidas enviadas"),
            ("errores detectados en revisión", "correcciones realizadas, sobre salidas revisadas"),
            ("tiempo ahorrado verificado", "horas liberadas medidas, comparadas con las estimadas"),
        ],
        caso=(
            "Un vendedor de Ruta Andina envió una propuesta generada que incluía una integración inexistente. "
            "El cliente firmó por esa razón."
        ),
        limite=(
            "La asistencia puede degradar la habilidad del equipo si sustituye la práctica del diagnóstico. "
            "Conviene reservar la asistencia para tareas mecánicas."
        ),
        libros=["nist-airmf", "roberge", "ng-mlyearning", "rackham"],
        error=("Enviar salidas generadas sin revisión humana",
               "Instala la revisión obligatoria antes de cualquier comunicación al cliente."),
    ),
    dict(
        n="09",
        slug="agentes-comerciales",
        titulo="Agentes comerciales automatizados",
        tesis=(
            "Un agente no sólo genera texto: ejecuta acciones —enviar correos, actualizar registros, agendar—. "
            "Eso cambia el perfil de riesgo: un error ya no produce un borrador malo sino una acción real "
            "sobre un cliente real. Su diseño exige límites explícitos de autoridad, registro de acciones, "
            "capacidad de detención inmediata y responsable identificado."
        ),
        conceptos=[
            ("autoridad del agente", "conjunto de acciones que el sistema puede ejecutar sin aprobación humana"),
            ("registro de acciones", "traza completa de qué hizo el sistema, cuándo y sobre qué registro"),
            ("mecanismo de detención", "capacidad de interrumpir la operación del agente de inmediato"),
            ("acción irreversible", "operación cuyo efecto no puede deshacerse, como enviar una comunicación"),
        ],
        metodo=[
            "definir la autoridad del agente por tipo de acción",
            "excluir las acciones irreversibles de la autonomía",
            "instrumentar el registro completo de acciones",
            "habilitar la detención inmediata y probarla",
            "revisar el registro periódicamente con responsable",
        ],
        senales=[
            ("acciones ejecutadas por el agente", "operaciones automáticas realizadas, por tipo y periodo"),
            ("acciones revertidas", "operaciones corregidas manualmente, sobre acciones ejecutadas"),
            ("tiempo de detención", "minutos entre la detección de un problema y la interrupción efectiva"),
        ],
        caso=(
            "Un agente de Ruta Andina envió 400 correos de reactivación a clientes que habían solicitado no "
            "ser contactados, porque la regla de exclusión no estaba implementada."
        ),
        limite=(
            "La responsabilidad legal y comercial siempre recae en la empresa, no en el sistema. La "
            "automatización no traslada la responsabilidad a nadie más."
        ),
        libros=["russell-norvig", "nist-airmf", "iso-31000", "oneil"],
        error=("Otorgar autoridad sobre acciones irreversibles",
               "Excluye envíos y compromisos de la autonomía del agente y exige aprobación humana."),
    ),
    dict(
        n="10",
        slug="conversation-intelligence",
        titulo="Inteligencia de conversaciones",
        tesis=(
            "El análisis automatizado de llamadas y reuniones produce información valiosa: qué objeciones "
            "aparecen, cuánto habla el vendedor, qué temas correlacionan con el cierre. Su condición previa "
            "es legal y ética: grabar conversaciones requiere informar y, según el caso, obtener "
            "consentimiento. Usarlo para vigilancia individual en lugar de mejora del proceso destruye la "
            "confianza del equipo."
        ),
        conceptos=[
            ("consentimiento de grabación", "autorización informada de los participantes para registrar la conversación"),
            ("análisis agregado", "estudio de patrones del conjunto en lugar de vigilancia individual"),
            ("patrón asociado al resultado", "comportamiento conversacional que correlaciona con el cierre"),
            ("uso para desarrollo", "aplicación orientada a mejorar la habilidad y no a sancionar"),
        ],
        metodo=[
            "verificar el marco legal y obtener consentimiento",
            "definir qué se analizará y para qué",
            "priorizar el análisis agregado sobre el individual",
            "usar los hallazgos para formación y no para sanción",
            "revisar el efecto sobre el desempeño del equipo",
        ],
        senales=[
            ("cobertura de consentimiento", "conversaciones grabadas con consentimiento registrado, sobre grabaciones"),
            ("patrones identificados", "comportamientos con correlación verificada con el cierre, sobre comportamientos analizados en el periodo"),
            ("uso en formación", "sesiones de formación basadas en hallazgos, por trimestre"),
        ],
        caso=(
            "Ruta Andina activó grabación automática de llamadas sin informar a los clientes ni al equipo, y "
            "la jefatura empezó a usar los resúmenes en evaluaciones individuales."
        ),
        limite=(
            "El análisis conversacional identifica correlaciones, no causas. Imponer un patrón conversacional "
            "sin entender su mecanismo puede empeorar el resultado."
        ),
        libros=["nist-airmf", "provost", "rackham", "roberge"],
        error=("Grabar sin informar ni obtener consentimiento",
               "Verifica el marco legal, informa a todas las partes y obtén el consentimiento antes de grabar."),
    ),
    dict(
        n="11",
        slug="ia-en-customer-success",
        titulo="IA en customer success",
        tesis=(
            "En éxito de cliente la IA se usa para predecir riesgo de baja, priorizar cartera y asistir "
            "respuestas. Su riesgo específico es la automatización de la empatía: responder con un sistema "
            "las consultas de un cliente frustrado suele empeorar la situación. La regla práctica es "
            "automatizar el diagnóstico y la priorización, y mantener humana la conversación difícil."
        ),
        conceptos=[
            ("predicción de riesgo", "estimación automatizada de la probabilidad de baja de una cuenta"),
            ("priorización de cartera", "ordenamiento de cuentas por riesgo y valor para asignar atención"),
            ("automatización de la respuesta", "sustitución de la interacción humana por un sistema"),
            ("momento de escalamiento", "condición que obliga a que una persona tome la conversación"),
        ],
        metodo=[
            "usar modelos para predecir y priorizar",
            "definir el momento de escalamiento a una persona",
            "mantener humana la conversación de riesgo o reclamo",
            "medir efecto en retención y en satisfacción",
            "revisar los casos escalados para corregir el diseño",
        ],
        senales=[
            ("precisión de la predicción de baja", "bajas correctamente anticipadas, sobre bajas del periodo"),
            ("tasa de escalamiento a persona", "conversaciones derivadas a un humano, sobre conversaciones iniciadas"),
            ("satisfacción por tipo de atención", "puntuación comparada entre atención automatizada y humana"),
        ],
        caso=(
            "El asistente automático de Ruta Andina respondió tres veces con el mismo texto a un cliente que "
            "llevaba dos semanas sin poder facturar. El cliente se dio de baja."
        ),
        limite=(
            "Un modelo predictivo sin capacidad de intervención sólo anticipa la pérdida. La predicción debe "
            "estar acompañada de una acción posible y de capacidad para ejecutarla."
        ),
        libros=["mehta", "dixon-effort", "provost", "nist-airmf"],
        error=("Automatizar la conversación con clientes en riesgo",
               "Define el escalamiento obligatorio a una persona ante señales de frustración o de riesgo."),
    ),
    dict(
        n="12",
        slug="evaluacion-y-guardrails",
        titulo="Evaluación y guardrails",
        tesis=(
            "Un sistema de IA sin evaluación es una apuesta. Evaluar significa definir un conjunto de casos "
            "representativos con respuesta esperada, medir el desempeño antes de desplegar y monitorearlo "
            "después. Los guardarraíles son las restricciones que impiden comportamientos inaceptables aunque "
            "el sistema los proponga. El marco de gestión de riesgo del NIST ordena esto en cuatro "
            "funciones: mapear, medir, gestionar y gobernar."
        ),
        conceptos=[
            ("conjunto de evaluación", "casos representativos con resultado esperado que permiten medir el desempeño"),
            ("guardarraíl", "restricción que impide un comportamiento inaceptable del sistema"),
            ("monitoreo posterior", "medición continua del desempeño tras el despliegue"),
            ("umbral de aceptación", "nivel de desempeño mínimo que autoriza el uso en producción"),
        ],
        metodo=[
            "construir el conjunto de evaluación con casos reales",
            "definir el umbral de aceptación antes de probar",
            "implementar guardarraíles sobre los riesgos identificados",
            "monitorear el desempeño en producción",
            "documentar incidentes y ajustar el sistema",
        ],
        senales=[
            ("desempeño en el conjunto de evaluación", "casos resueltos correctamente, sobre casos del conjunto"),
            ("incidentes por guardarraíl activado", "activaciones del guardarraíl, sobre solicitudes procesadas por el sistema, por mes"),
            ("deriva de desempeño", "variación del resultado en el conjunto de evaluación entre periodos"),
        ],
        caso=(
            "Ruta Andina desplegó su asistente sin conjunto de evaluación. Descubrió que prometía "
            "funcionalidades inexistentes cuando un cliente reclamó por escrito."
        ),
        limite=(
            "Ningún conjunto de evaluación cubre todos los casos posibles. Los guardarraíles y el monitoreo "
            "son necesarios precisamente porque la evaluación previa es incompleta."
        ),
        libros=["nist-airmf", "ng-mlyearning", "kohavi", "iso-31000"],
        error=("Desplegar sin conjunto de evaluación ni umbral",
               "Construye casos representativos con respuesta esperada y define el umbral antes del despliegue."),
    ),
    dict(
        n="13",
        slug="privacidad-y-propiedad-intelectual",
        titulo="Privacidad y propiedad intelectual",
        tesis=(
            "El uso comercial de IA plantea dos frentes legales. En datos personales, la Ley 21.719 refuerza "
            "obligaciones de finalidad, información, seguridad y derechos del titular, incluidos los casos de "
            "decisiones automatizadas. En propiedad intelectual, el contenido generado puede reproducir obras "
            "protegidas y su titularidad no siempre es clara. Ambos frentes exigen política escrita, no "
            "criterio individual."
        ),
        conceptos=[
            ("finalidad del tratamiento", "propósito declarado que legitima el uso de los datos personales"),
            ("decisión automatizada", "resolución que afecta a una persona tomada sin intervención humana significativa"),
            ("titularidad del contenido", "definición de quién posee derechos sobre lo generado"),
            ("política de uso", "documento que define qué está permitido, qué no y quién autoriza excepciones"),
        ],
        metodo=[
            "inventariar qué datos se tratan en cada caso de uso",
            "verificar finalidad, base de licitud e información al titular",
            "definir la política de uso de contenido generado",
            "documentar las decisiones automatizadas y su supervisión",
            "revisar la política cuando cambia la normativa o las herramientas",
        ],
        senales=[
            ("casos de uso con base legal documentada", "usos con finalidad y base registradas, sobre usos activos"),
            ("decisiones automatizadas identificadas", "procesos con decisión automatizada documentada, sobre procesos automatizados"),
            ("incidentes de privacidad", "eventos con datos personales comprometidos, por periodo"),
        ],
        caso=(
            "Ruta Andina usa un modelo para decidir qué clientes reciben una oferta de retención. Esa "
            "decisión automatizada afecta a personas y no está documentada ni supervisada."
        ),
        limite=(
            "La normativa evoluciona y las herramientas cambian sus condiciones de servicio. La política debe "
            "tener fecha de revisión y responsable, no ser un documento único."
        ),
        libros=["nist-airmf", "oneil", "iso-31000", "russell-norvig"],
        error=("Operar decisiones automatizadas sin documentación ni supervisión",
               "Identifica las decisiones automatizadas que afectan a personas y documenta su supervisión humana."),
    ),
    dict(
        n="14",
        slug="operating-model-humano-ia",
        titulo="Operating model humano-IA",
        tesis=(
            "Esta clase integra la parte en un modelo operativo: qué tareas se asisten, qué se automatiza, "
            "qué queda humano, con qué evaluación, qué guardarraíles, qué registro y quién responde. La "
            "prueba de calidad es la rendición de cuentas: ante un error, la empresa debe poder explicar qué "
            "sistema actuó, con qué datos, bajo qué autorización y quién era responsable."
        ),
        conceptos=[
            ("modelo operativo humano-IA", "distribución documentada de tareas entre personas y sistemas"),
            ("rendición de cuentas", "capacidad de explicar qué ocurrió, con qué datos y bajo qué responsabilidad"),
            ("registro de incidentes", "documentación de fallas, su causa y su corrección"),
            ("revisión periódica", "evaluación programada del modelo completo y sus resultados"),
        ],
        metodo=[
            "clasificar tareas en asistidas, automatizadas y humanas",
            "documentar evaluación y guardarraíles por caso de uso",
            "asignar responsable por cada sistema activo",
            "instalar el registro de incidentes",
            "revisar el modelo completo cada semestre",
        ],
        senales=[
            ("casos de uso documentados", "usos con evaluación, guardarraíl y responsable, sobre usos activos"),
            ("incidentes registrados y corregidos", "incidentes con causa raíz documentada, sobre incidentes ocurridos"),
            ("tiempo de rendición de cuentas", "horas entre el reporte del incidente y la reconstrucción completa de lo ocurrido, mediana"),
        ],
        caso=(
            "Un cliente reclama por escrito una promesa que hizo el asistente automático de Ruta Andina. La "
            "empresa no puede determinar qué versión respondió ni quién la autorizó."
        ),
        limite=(
            "Un modelo operativo maduro exige capacidad dedicada. En equipos pequeños conviene menos casos de "
            "uso bien gobernados que muchos sin control."
        ),
        libros=["nist-airmf", "iso-31000", "russell-norvig", "diorio"],
        error=("No poder reconstruir qué hizo el sistema ante un incidente",
               "Instala el registro de acciones y versiones, y designa responsable por cada sistema activo."),
    ),
]
