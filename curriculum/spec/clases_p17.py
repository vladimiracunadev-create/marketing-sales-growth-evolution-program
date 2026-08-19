# -*- coding: utf-8 -*-
"""Parte 17 — Marketing automation y revenue operations."""

CLASES = [
    dict(
        n="01",
        slug="automatizacion-con-proposito",
        titulo="Automatización con propósito",
        tesis=(
            "Automatizar un proceso desordenado produce desorden a escala. La secuencia correcta es "
            "estandarizar, simplificar y sólo entonces automatizar. Antes de configurar cualquier flujo hay "
            "que responder tres preguntas: qué problema resuelve, qué pasa si falla y quién se entera. La "
            "automatización comercial tiene consecuencias directas sobre personas reales, y un flujo mal "
            "configurado envía mensajes equivocados a clientes reales."
        ),
        conceptos=[
            ("proceso estandarizado", "flujo con pasos definidos y resultado consistente antes de ser automatizado"),
            ("modo de falla", "forma en que la automatización puede producir un resultado incorrecto"),
            ("detección de falla", "mecanismo que avisa cuando el flujo deja de funcionar como se esperaba"),
            ("reversibilidad", "capacidad de deshacer o corregir el efecto de una automatización errónea"),
        ],
        metodo=[
            "documentar el proceso manual y estandarizarlo",
            "eliminar pasos innecesarios antes de automatizar",
            "identificar los modos de falla y su consecuencia",
            "instalar detección y alerta antes de activar",
            "medir el efecto sobre el resultado y no sólo el ahorro de tiempo",
        ],
        senales=[
            ("flujos con detección de falla", "automatizaciones con alerta configurada, sobre automatizaciones activas"),
            ("incidentes por automatización", "errores atribuibles a flujos automatizados, por trimestre"),
            ("tiempo ahorrado verificado", "horas liberadas medidas, comparadas con las estimadas al automatizar"),
        ],
        caso=(
            "Ruta Andina automatizó el envío de bienvenida sin filtrar clientes que ya estaban en "
            "implementación. Cuarenta clientes recibieron instrucciones de un proceso que ya habían "
            "completado."
        ),
        limite=(
            "No todo lo automatizable debe automatizarse: hay interacciones donde el contacto humano es parte "
            "del valor y su reemplazo destruye la relación."
        ),
        libros=["diorio", "grove", "nist-airmf", "roberge"],
        error=("Automatizar un proceso sin estandarizarlo antes",
               "Documenta y simplifica el flujo manual; automatiza sólo cuando el resultado ya es consistente."),
    ),
    dict(
        n="02",
        slug="lifecycle-stages",
        titulo="Etapas de ciclo de vida",
        tesis=(
            "Las etapas de ciclo de vida clasifican a cada contacto según su relación con la empresa: "
            "desconocido, suscriptor, lead, oportunidad, cliente, cliente en riesgo, ex cliente. Su valor "
            "está en permitir tratamientos distintos y medir el flujo entre estados. Su condición es la "
            "misma que en el pipeline: definiciones compartidas y criterios verificables de transición."
        ),
        conceptos=[
            ("etapa de ciclo de vida", "estado que describe la relación actual del contacto con la empresa"),
            ("criterio de transición", "condición verificable que mueve a un contacto de una etapa a otra"),
            ("flujo entre etapas", "volumen de contactos que se mueve entre estados en un periodo"),
            ("estado terminal", "etapa desde la cual el contacto sale del ciclo activo"),
        ],
        metodo=[
            "definir las etapas y sus criterios de transición",
            "instrumentar el registro automático de transiciones",
            "medir volumen y velocidad de flujo entre etapas",
            "diseñar tratamiento diferenciado por etapa",
            "revisar las definiciones cada semestre",
        ],
        senales=[
            ("distribución por etapa", "contactos en cada etapa, sobre contactos totales de la base"),
            ("velocidad de transición", "días medianos de permanencia en cada etapa"),
            ("contactos sin etapa asignada", "registros sin clasificar, sobre registros activos"),
        ],
        caso=(
            "En Ruta Andina un mismo contacto aparece como lead en marketing y como cliente en soporte "
            "porque cada área usa su propia clasificación."
        ),
        limite=(
            "Demasiadas etapas producen una taxonomía que nadie mantiene. Seis o siete estados suelen bastar "
            "para operar."
        ),
        libros=["diorio", "roberge", "croll-yoskovitz", "provost"],
        error=("Mantener clasificaciones distintas por área",
               "Acuerda una taxonomía única con criterios verificables y aplícala en todos los sistemas."),
    ),
    dict(
        n="03",
        slug="lead-scoring",
        titulo="Lead scoring",
        tesis=(
            "Un modelo de puntuación estima la probabilidad de que un contacto se convierta en cliente. Su "
            "utilidad depende de que combine ajuste de perfil y señal de comportamiento, y de que se valide "
            "contra resultados reales. Un modelo construido con opiniones del equipo y nunca contrastado "
            "produce puntajes que nadie usa y una falsa sensación de rigor."
        ),
        conceptos=[
            ("puntaje de ajuste", "componente que evalúa la correspondencia con el perfil de cliente ideal"),
            ("puntaje de comportamiento", "componente que evalúa señales de interés y de intención"),
            ("validación del modelo", "contraste entre el puntaje asignado y la conversión efectiva"),
            ("decaimiento", "reducción del puntaje por inactividad, que evita puntajes eternos"),
        ],
        metodo=[
            "definir los componentes de ajuste y de comportamiento",
            "asignar pesos derivados de datos históricos",
            "aplicar decaimiento por inactividad",
            "validar contra conversión real cada trimestre",
            "recalibrar y documentar los cambios",
        ],
        senales=[
            ("conversión por tramo de puntaje", "clientes ganados, sobre leads de cada tramo de puntaje"),
            ("capacidad discriminante", "diferencia de conversión entre el tramo superior y el inferior"),
            ("uso del puntaje por ventas", "oportunidades priorizadas usando el puntaje, sobre oportunidades trabajadas"),
        ],
        caso=(
            "El modelo de Ruta Andina asigna 30 puntos por abrir tres correos y 10 por pertenecer al rubro "
            "objetivo. Los leads de mayor puntaje convierten igual que el promedio."
        ),
        limite=(
            "Los modelos aprenden del histórico y reproducen sus sesgos. Si la prospección pasada ignoró un "
            "segmento, el modelo seguirá subvalorándolo."
        ),
        libros=["provost", "roberge", "diorio", "oneil"],
        error=("No validar el modelo contra conversión real",
               "Compara la conversión por tramo de puntaje cada trimestre y recalibra los pesos."),
    ),
    dict(
        n="04",
        slug="lead-routing",
        titulo="Enrutamiento de leads",
        tesis=(
            "El enrutamiento define quién atiende cada contacto y en cuánto tiempo. Sus reglas deben ser "
            "explícitas, auditables y con responsable de excepción. Un enrutamiento defectuoso produce leads "
            "que nadie contacta y disputas internas sobre atribución. La velocidad importa: cada hora "
            "transcurrida reduce la probabilidad de contacto efectivo."
        ),
        conceptos=[
            ("regla de asignación", "criterio que determina quién recibe cada contacto"),
            ("tiempo de asignación", "minutos entre la creación del registro y su asignación efectiva"),
            ("cobertura de asignación", "proporción de contactos que llega efectivamente a un responsable"),
            ("regla de escalamiento", "acción automática cuando el asignado no responde en el plazo"),
        ],
        metodo=[
            "definir las reglas de asignación por segmento y territorio",
            "medir el tiempo de asignación y de primer contacto",
            "configurar escalamiento por falta de respuesta",
            "auditar los contactos no asignados",
            "revisar las reglas cuando cambia la estructura del equipo",
        ],
        senales=[
            ("tiempo de asignación", "minutos entre creación y asignación, mediana"),
            ("leads sin asignar", "registros sin responsable en 24 horas, sobre registros creados"),
            ("escalamientos ejecutados", "escalamientos activados, sobre casos que cumplían la condición"),
        ],
        caso=(
            "El 31 % de los leads entrantes de Ruta Andina nunca recibe contacto porque la regla de "
            "asignación depende de un campo que el formulario no captura."
        ),
        limite=(
            "Un enrutamiento muy sofisticado se vuelve frágil. Cada condición adicional aumenta la "
            "probabilidad de que un caso no encuentre ruta."
        ),
        libros=["roberge", "diorio", "ross", "grove"],
        error=("Configurar reglas que dependen de datos no capturados",
               "Verifica que cada condición de enrutamiento use un campo efectivamente registrado."),
    ),
    dict(
        n="05",
        slug="nurturing",
        titulo="Nurturing",
        tesis=(
            "El nurturing acompaña a quien todavía no está listo para comprar, entregando información "
            "pertinente hasta que aparece el momento. Funciona cuando el contenido responde a la etapa real "
            "del contacto y falla cuando repite mensajes promocionales. Su métrica correcta no es la "
            "apertura sino el avance: cuántos contactos pasan de una etapa a la siguiente."
        ),
        conceptos=[
            ("secuencia de maduración", "serie de comunicaciones diseñada para acompañar la evolución del contacto"),
            ("pertinencia por etapa", "correspondencia entre el contenido y el momento del contacto"),
            ("avance de etapa", "movimiento del contacto hacia un estado más cercano a la compra"),
            ("fatiga de comunicación", "pérdida de atención por exceso o repetición de mensajes"),
        ],
        metodo=[
            "definir las preguntas del contacto en cada etapa",
            "asignar contenido pertinente a cada una",
            "establecer el ritmo y el criterio de salida",
            "medir avance de etapa y no sólo apertura",
            "retirar de la secuencia a quien avanza o pide salir",
        ],
        senales=[
            ("tasa de avance de etapa", "contactos que avanzan, sobre contactos en la secuencia"),
            ("tasa de baja por secuencia", "bajas solicitadas, sobre contactos activos en la secuencia"),
            ("tiempo hasta avance", "días medianos entre el ingreso a la secuencia y el avance de etapa"),
        ],
        caso=(
            "La secuencia de Ruta Andina envía diez correos promocionales en tres semanas a contactos que "
            "sólo descargaron una guía. El 14 % se da de baja."
        ),
        limite=(
            "Ninguna secuencia crea urgencia donde no hay problema. El nurturing acompaña la maduración; no "
            "la produce."
        ),
        libros=["handley", "godin", "diorio", "chaffey"],
        error=("Medir nurturing por aperturas",
               "Evalúa por avance de etapa y retira de la secuencia a quien ya avanzó."),
    ),
    dict(
        n="06",
        slug="workflows",
        titulo="Workflows",
        tesis=(
            "Un flujo automatizado es código que actúa sobre clientes. Como todo código, necesita "
            "documentación, control de versiones, pruebas y un responsable. La práctica habitual —crear "
            "flujos sin registro, sin pruebas y sin dueño— produce sistemas donde nadie sabe por qué un "
            "cliente recibió un mensaje y nadie puede corregirlo con seguridad."
        ),
        conceptos=[
            ("condición de entrada", "criterio que determina qué registros ingresan al flujo"),
            ("condición de salida", "criterio que retira al registro del flujo"),
            ("prueba en ambiente controlado", "verificación del comportamiento antes de activar sobre datos reales"),
            ("documentación del flujo", "registro de propósito, condiciones, responsable y fecha de revisión"),
        ],
        metodo=[
            "documentar propósito y condiciones antes de construir",
            "probar con registros de prueba",
            "activar con volumen limitado y monitoreo",
            "registrar responsable y fecha de revisión",
            "auditar flujos activos cada semestre y retirar los obsoletos",
        ],
        senales=[
            ("flujos documentados", "automatizaciones con documentación completa, sobre automatizaciones activas"),
            ("flujos sin responsable", "automatizaciones sin dueño asignado, sobre automatizaciones activas"),
            ("errores detectados en pruebas", "problemas encontrados antes de activar, sobre flujos desplegados"),
        ],
        caso=(
            "Ruta Andina tiene 14 automatizaciones activas. Dos envían el mismo correo, una nunca se "
            "desactivó tras una campaña de 2025 y ninguna tiene responsable."
        ),
        limite=(
            "Probar todos los casos límite es imposible. El control complementario es el monitoreo posterior "
            "y la capacidad de detener el flujo rápidamente."
        ),
        libros=["diorio", "grove", "nist-airmf", "provost"],
        error=("Activar flujos sin prueba ni responsable",
               "Exige documentación, prueba controlada y dueño asignado antes de activar cualquier flujo."),
    ),
    dict(
        n="07",
        slug="sla-marketing-ventas",
        titulo="Acuerdo de servicio entre marketing y ventas",
        tesis=(
            "El conflicto entre marketing y ventas rara vez es de personas: es de definiciones y de "
            "compromisos no explicitados. Un acuerdo de servicio define qué es un lead calificado, cuántos "
            "se entregarán, en qué plazo se contactarán y qué información se devolverá. Sin ese acuerdo, cada "
            "área optimiza su métrica y el sistema completo pierde."
        ),
        conceptos=[
            ("definición compartida de lead calificado", "criterio único acordado entre ambas áreas"),
            ("compromiso de volumen", "cantidad de leads calificados que marketing se compromete a entregar"),
            ("compromiso de atención", "plazo en que ventas se compromete a contactar y calificar"),
            ("retroalimentación estructurada", "información que ventas devuelve sobre la calidad de lo recibido"),
        ],
        metodo=[
            "acordar la definición de lead calificado con ejemplos",
            "fijar compromisos de volumen y de plazo",
            "instrumentar la retroalimentación de ventas",
            "medir el cumplimiento de ambas partes",
            "revisar el acuerdo cada trimestre con datos",
        ],
        senales=[
            ("cumplimiento de volumen", "leads calificados entregados, sobre leads comprometidos"),
            ("cumplimiento de plazo de contacto", "leads contactados dentro del plazo, sobre leads entregados"),
            ("retroalimentación devuelta", "leads con evaluación de ventas registrada, sobre leads entregados"),
        ],
        caso=(
            "Marketing informa 300 leads y ventas trabaja 60. Ambas cifras son correctas según su propia "
            "definición y la reunión mensual se consume discutiendo cuál es la verdadera."
        ),
        limite=(
            "El acuerdo no resuelve conflictos de incentivos. Si la compensación de cada área premia "
            "comportamientos opuestos, el acuerdo se incumplirá."
        ),
        libros=["diorio", "roberge", "grove", "lencioni"],
        error=("Operar sin definición compartida de lead calificado",
               "Acuerda la definición con ejemplos concretos y mide el cumplimiento de ambas partes."),
    ),
    dict(
        n="08",
        slug="modelo-de-datos-revops",
        titulo="Modelo de datos de RevOps",
        tesis=(
            "El modelo de datos es la infraestructura invisible de las decisiones comerciales. Define qué "
            "entidades existen, cómo se relacionan, qué estados son válidos y de dónde proviene cada dato. "
            "Cuando no está diseñado, cada informe requiere reconciliación manual y cada pregunta nueva "
            "exige un proyecto. Diseñarlo es más barato que rehacerlo después de tres años de deuda."
        ),
        conceptos=[
            ("entidad", "objeto del modelo que representa algo real: cuenta, contacto, oportunidad, suscripción"),
            ("fuente autoritativa", "sistema que contiene la versión válida de cada dato"),
            ("estado válido", "conjunto de valores permitidos para un campo y sus transiciones posibles"),
            ("deuda de datos", "acumulación de inconsistencias que encarece cada análisis futuro"),
        ],
        metodo=[
            "inventariar entidades y sistemas actuales",
            "definir la fuente autoritativa de cada dato",
            "documentar estados válidos y transiciones",
            "resolver las inconsistencias más costosas primero",
            "establecer el proceso de cambio del modelo",
        ],
        senales=[
            ("datos con fuente autoritativa definida", "campos críticos con fuente única declarada, sobre campos críticos"),
            ("inconsistencias entre sistemas", "registros con valores divergentes, sobre registros comparados"),
            ("tiempo de respuesta a preguntas nuevas", "días transcurridos entre la consulta analítica no prevista y su respuesta, mediana por trimestre"),
        ],
        caso=(
            "El ingreso recurrente de Ruta Andina existe en el CRM, en la plataforma de facturación y en una "
            "planilla. Los tres números difieren y ninguno está declarado como autoritativo."
        ),
        limite=(
            "Un modelo perfecto que exige rehacer todos los sistemas no se implementa. El diseño debe "
            "priorizar lo que produce más valor con menos disrupción."
        ),
        libros=["diorio", "provost", "roberge", "kaplan-norton"],
        error=("Operar sin fuente autoritativa declarada",
               "Define para cada dato crítico cuál sistema manda y documenta la regla de reconciliación."),
    ),
    dict(
        n="09",
        slug="integraciones",
        titulo="Integraciones",
        tesis=(
            "Las integraciones conectan sistemas y crean dependencias. Cada una introduce puntos de falla, "
            "latencia y riesgo de duplicación. Las decisiones importantes son de dirección —qué sistema "
            "escribe y cuál lee—, de frecuencia y de manejo de errores. Sin monitoreo, una integración rota "
            "puede pasar semanas sin detección mientras los datos divergen."
        ),
        conceptos=[
            ("dirección de sincronización", "definición de qué sistema escribe y cuál recibe cada dato"),
            ("latencia", "tiempo entre el cambio en el origen y su reflejo en el destino"),
            ("manejo de errores", "comportamiento definido cuando la sincronización falla"),
            ("monitoreo de integración", "mecanismo que detecta y avisa cuando el flujo se interrumpe"),
        ],
        metodo=[
            "mapear los sistemas y los datos que comparten",
            "definir dirección y frecuencia de cada sincronización",
            "especificar el manejo de errores y reintentos",
            "instalar monitoreo con alerta",
            "revisar el mapa de integraciones cada semestre",
        ],
        senales=[
            ("tasa de error de sincronización", "operaciones fallidas, sobre operaciones intentadas, por integración"),
            ("latencia observada", "minutos entre el cambio en origen y su reflejo en destino"),
            ("tiempo de detección de falla", "horas entre la interrupción y la detección"),
        ],
        caso=(
            "La integración entre el CRM y la facturación de Ruta Andina se detuvo hace once días. Nadie lo "
            "notó hasta que un cliente reclamó por una factura duplicada."
        ),
        limite=(
            "Reducir integraciones simplifica pero puede obligar a trabajo manual. El criterio es el costo "
            "total, incluido el de mantener la integración."
        ),
        libros=["diorio", "provost", "grove", "nist-airmf"],
        error=("Operar integraciones sin monitoreo",
               "Configura alerta de falla y revisa el tiempo de detección como indicador operativo."),
    ),
    dict(
        n="10",
        slug="revenue-funnel",
        titulo="Embudo de ingresos",
        tesis=(
            "El embudo de ingresos unifica la vista de marketing, ventas y éxito de cliente en un solo "
            "recorrido con definiciones compartidas. Su valor es diagnóstico: permite ver dónde se pierde "
            "valor considerando el ciclo completo, incluida la retención. Un embudo que termina en la venta "
            "esconde el problema más caro de los modelos recurrentes."
        ),
        conceptos=[
            ("embudo unificado", "representación única del recorrido desde el descubrimiento hasta la renovación"),
            ("definición compartida por etapa", "criterio acordado entre áreas para cada estado del recorrido"),
            ("pérdida por tramo", "valor que se pierde en cada transición del embudo"),
            ("visión de ciclo completo", "inclusión de retención y expansión en el análisis del embudo"),
        ],
        metodo=[
            "definir las etapas del recorrido completo",
            "acordar criterios entre áreas",
            "medir volumen, conversión y valor por tramo",
            "identificar la mayor pérdida de valor",
            "asignar responsable por tramo",
        ],
        senales=[
            ("conversión por tramo", "unidades que avanzan, sobre unidades que ingresaron al tramo"),
            ("valor perdido por tramo", "ingreso anual estimado que se pierde en cada transición"),
            ("cobertura de definiciones compartidas", "etapas con criterio acordado entre áreas, sobre etapas totales"),
        ],
        caso=(
            "El embudo de Ruta Andina termina en la firma. La mayor pérdida de valor ocurre entre la firma y "
            "el día 90, y no aparece en ningún informe."
        ),
        limite=(
            "Un embudo unificado puede ocultar diferencias importantes entre segmentos o líneas de negocio. "
            "El análisis debe segmentarse."
        ),
        libros=["diorio", "croll-yoskovitz", "mehta", "kaplan-norton"],
        error=("Terminar el embudo en la venta",
               "Extiende el análisis hasta renovación y expansión, y mide el valor perdido en cada tramo."),
    ),
    dict(
        n="11",
        slug="forecast-unificado",
        titulo="Forecast unificado",
        tesis=(
            "Un forecast unificado proyecta ingreso nuevo, renovaciones, expansión y contracción en un mismo "
            "modelo. Sin esa vista, la empresa puede celebrar un trimestre récord de ventas nuevas mientras "
            "pierde más ingreso por bajas del que incorpora. La proyección debe declarar sus supuestos por "
            "componente y medir la precisión de cada uno por separado."
        ),
        conceptos=[
            ("ingreso nuevo", "ingreso incorporado por clientes que no existían al inicio del periodo"),
            ("renovación", "ingreso conservado de clientes existentes al vencer su contrato"),
            ("expansión y contracción", "aumento o reducción de ingreso en clientes que permanecen"),
            ("precisión por componente", "medición separada de la exactitud de cada parte de la proyección"),
        ],
        metodo=[
            "modelar cada componente por separado",
            "declarar los supuestos de cada uno",
            "consolidar la proyección de ingreso neto",
            "medir la precisión por componente",
            "corregir los supuestos con el sesgo observado",
        ],
        senales=[
            ("precisión por componente", "diferencia entre proyección y resultado, por componente y trimestre"),
            ("ingreso neto proyectado", "suma de nuevo, renovación, expansión menos contracción y bajas"),
            ("cobertura de renovaciones", "renovaciones gestionadas con anticipación, sobre renovaciones del periodo"),
        ],
        caso=(
            "Ruta Andina proyecta ventas nuevas con detalle y estima renovaciones con un porcentaje fijo "
            "heredado de 2025 que nadie ha vuelto a validar."
        ),
        limite=(
            "La proyección de renovaciones requiere cohortes maduras. En empresas jóvenes el error es alto y "
            "debe declararse como rango."
        ),
        libros=["mehta", "diorio", "croll-yoskovitz", "provost"],
        error=("Proyectar renovaciones con un porcentaje fijo",
               "Modela renovación por cohorte y segmento, y mide su precisión cada trimestre."),
    ),
    dict(
        n="12",
        slug="calidad-y-observabilidad",
        titulo="Calidad y observabilidad",
        tesis=(
            "La observabilidad es la capacidad de saber que algo se rompió antes de que lo note un cliente. "
            "En operaciones de ingreso eso significa monitorear flujos, integraciones, completitud de datos "
            "y coherencia entre sistemas. Sin observabilidad, los problemas se descubren por reclamo, que es "
            "la forma más cara y dañina de enterarse."
        ),
        conceptos=[
            ("indicador de salud del sistema", "métrica que refleja el correcto funcionamiento de un proceso automatizado"),
            ("alerta accionable", "aviso que indica qué se rompió y qué hacer"),
            ("detección por reclamo", "situación en que el problema se conoce porque un cliente lo informa"),
            ("tiempo medio de recuperación", "duración entre la detección del problema y su resolución"),
        ],
        metodo=[
            "identificar los procesos críticos y sus modos de falla",
            "definir indicadores de salud por proceso",
            "configurar alertas accionables con responsable",
            "medir tiempo de detección y de recuperación",
            "revisar incidentes y corregir causas raíz",
        ],
        senales=[
            ("proporción de incidentes detectados por monitoreo", "incidentes detectados por alerta, sobre incidentes totales"),
            ("tiempo medio de detección", "horas entre la falla y su detección"),
            ("tiempo medio de recuperación", "horas entre la detección y la resolución"),
        ],
        caso=(
            "El 80 % de los incidentes de Ruta Andina se descubre por reclamo de clientes. El tiempo medio de "
            "detección es cuatro días."
        ),
        limite=(
            "Demasiadas alertas producen desatención. El diseño debe priorizar pocas alertas realmente "
            "accionables sobre muchas informativas."
        ),
        libros=["grove", "nist-airmf", "diorio", "wheeler-dv"],
        error=("Enterarse de las fallas por reclamo del cliente",
               "Instala indicadores de salud por proceso crítico y mide el tiempo de detección."),
    ),
    dict(
        n="13",
        slug="gobernanza-de-automatizaciones",
        titulo="Gobernanza de automatizaciones",
        tesis=(
            "La gobernanza define quién puede crear, modificar y desactivar automatizaciones, con qué "
            "aprobación y con qué registro. Su ausencia produce sistemas donde nadie puede explicar por qué "
            "un cliente recibió un mensaje, lo que además es un problema de cumplimiento: la normativa de "
            "datos exige poder acreditar el tratamiento realizado."
        ),
        conceptos=[
            ("autoridad de cambio", "definición de quién puede modificar qué en el sistema automatizado"),
            ("registro de tratamiento", "documentación de qué datos se usaron, con qué finalidad y bajo qué base"),
            ("revisión periódica", "auditoría programada de las automatizaciones activas"),
            ("retiro de automatizaciones", "proceso de desactivar flujos que ya no cumplen función"),
        ],
        metodo=[
            "definir autoridad de cambio por tipo de automatización",
            "documentar propósito y base legal de cada flujo",
            "establecer la revisión periódica y su alcance",
            "retirar los flujos obsoletos",
            "mantener el registro de tratamiento actualizado",
        ],
        senales=[
            ("flujos con base legal documentada", "automatizaciones con finalidad y base registradas, sobre automatizaciones activas"),
            ("flujos retirados por revisión", "automatizaciones desactivadas por obsolescencia, por semestre"),
            ("cambios con aprobación registrada", "modificaciones con aprobación documentada, sobre modificaciones realizadas"),
        ],
        caso=(
            "Ruta Andina no puede explicar por qué un cliente recibió una comunicación de una campaña que "
            "terminó hace ocho meses, ni con qué base de datos se envió."
        ),
        limite=(
            "Una gobernanza pesada frena la operación. El nivel de control debe ser proporcional al riesgo: "
            "mayor para flujos que tratan datos personales o comprometen a la empresa."
        ),
        libros=["nist-airmf", "diorio", "iso-31000", "oneil"],
        error=("Mantener flujos activos sin propósito ni base documentada",
               "Audita las automatizaciones cada semestre y retira las que no tengan finalidad vigente."),
    ),
    dict(
        n="14",
        slug="operating-model-revops",
        titulo="Operating model de RevOps",
        tesis=(
            "Esta clase integra la parte en un modelo operativo de ingresos: definiciones compartidas, "
            "modelo de datos, ciclo de vida, automatizaciones gobernadas, acuerdos entre áreas, forecast "
            "unificado y observabilidad. La prueba de calidad es que una pregunta de negocio pueda "
            "responderse con una sola cifra, con su definición y su fuente."
        ),
        conceptos=[
            ("modelo operativo de ingresos", "conjunto de procesos, datos, acuerdos y responsabilidades que produce ingreso"),
            ("cifra única", "valor acordado para cada indicador con su definición y fuente"),
            ("responsabilidad por proceso", "asignación explícita de quién responde por cada tramo del sistema"),
            ("ritmo de gestión", "calendario de revisiones que sostiene la operación"),
        ],
        metodo=[
            "consolidar definiciones, datos y acuerdos",
            "documentar el modelo con responsables por proceso",
            "establecer el ritmo de revisiones",
            "verificar que cada indicador tenga cifra única",
            "revisar el modelo completo cada semestre",
        ],
        senales=[
            ("indicadores con definición única", "indicadores con definición y fuente acordadas, sobre indicadores usados"),
            ("procesos con responsable", "procesos del modelo con dueño asignado, sobre procesos definidos"),
            ("discrepancia entre informes", "diferencia porcentual entre el mismo indicador reportado por dos áreas"),
        ],
        caso=(
            "El directorio de Ruta Andina pregunta cuál es el ingreso recurrente. Tres áreas entregan tres "
            "cifras distintas y ninguna puede explicar la diferencia."
        ),
        limite=(
            "Un modelo operativo maduro exige capacidad dedicada. En equipos pequeños, la alternativa "
            "realista es un subconjunto bien mantenido en lugar de un modelo completo mal sostenido."
        ),
        libros=["diorio", "roberge", "kaplan-norton", "grove"],
        error=("Tolerar cifras distintas para el mismo indicador",
               "Declara la definición y la fuente única de cada indicador crítico y publícalas."),
    ),
]
