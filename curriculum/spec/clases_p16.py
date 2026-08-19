# -*- coding: utf-8 -*-
"""Parte 16 — CRM, pipeline y sales operations."""

CLASES = [
    dict(
        n="01",
        slug="crm-como-sistema-de-trabajo",
        titulo="El CRM como sistema de trabajo",
        tesis=(
            "Un CRM puede ser una herramienta de control o un sistema de trabajo, y esa diferencia determina "
            "la calidad del dato. Cuando sólo sirve para que la jefatura revise, el vendedor registra lo "
            "mínimo y el forecast se construye sobre ficción. Cuando ayuda a trabajar —recuerda "
            "compromisos, prepara reuniones, muestra el estado de la cuenta— el registro se vuelve natural. "
            "El diseño debe partir de esa premisa, no de la lista de reportes que la gerencia quiere ver."
        ),
        conceptos=[
            ("sistema de trabajo", "configuración que ayuda a ejecutar la tarea diaria y no sólo a reportarla"),
            ("costo de registro", "tiempo y esfuerzo que el sistema impone a quien ingresa la información"),
            ("valor devuelto", "beneficio concreto que el usuario obtiene del sistema al registrar"),
            ("dato de gestión", "información necesaria para dirigir que sólo existe si alguien la registra"),
        ],
        metodo=[
            "identificar las tareas diarias del equipo comercial",
            "configurar el sistema para facilitar esas tareas",
            "reducir el costo de registro al mínimo necesario",
            "verificar que cada campo obligatorio tiene un uso real",
            "medir adopción y calidad del dato, no sólo cumplimiento",
        ],
        senales=[
            ("adopción efectiva", "usuarios que registran actividad al menos tres veces por semana, sobre usuarios activos"),
            ("costo de registro", "minutos diarios dedicados al sistema, por vendedor"),
            ("campos obligatorios sin uso", "campos requeridos sin aparecer en ningún informe, sobre campos requeridos"),
        ],
        caso=(
            "El CRM de Ruta Andina exige 23 campos obligatorios y no muestra al vendedor qué debe hacer hoy. "
            "Los vendedores mantienen su propia planilla paralela."
        ),
        limite=(
            "Facilitar el trabajo no elimina la necesidad de disciplina. Un sistema cómodo con reglas "
            "inexistentes produce datos incompletos igual que uno incómodo."
        ),
        libros=["roberge", "diorio", "grove", "provost"],
        error=("Diseñar el CRM desde los reportes de gerencia",
               "Parte de las tareas diarias del vendedor y verifica que cada campo obligatorio tenga uso real."),
    ),
    dict(
        n="02",
        slug="diseno-del-pipeline",
        titulo="Diseño del pipeline",
        tesis=(
            "El pipeline modela el proceso comercial y por lo tanto lo condiciona: las etapas que se definen "
            "son las que el equipo ejecutará. Un buen diseño tiene pocas etapas, definidas por el "
            "comportamiento del cliente, con criterios de salida verificables y con probabilidades derivadas "
            "de datos históricos y no de la intuición de quien lo configuró."
        ),
        conceptos=[
            ("etapa del pipeline", "estado definido por evidencia observable del avance del cliente"),
            ("probabilidad por etapa", "tasa histórica de cierre de las oportunidades que alcanzaron esa etapa"),
            ("criterio de salida", "condición verificable para avanzar a la etapa siguiente"),
            ("granularidad", "número de etapas, que debe equilibrar información y costo de mantenimiento"),
        ],
        metodo=[
            "reconstruir el proceso real desde negocios ganados",
            "definir etapas por evidencia del cliente",
            "calcular la probabilidad histórica de cada etapa",
            "escribir criterios de salida verificables",
            "revisar las probabilidades cada semestre con datos nuevos",
        ],
        senales=[
            ("probabilidad real por etapa", "negocios ganados, sobre negocios que alcanzaron la etapa, por cohorte"),
            ("desviación entre probabilidad asignada y real", "diferencia entre la probabilidad configurada y la observada"),
            ("oportunidades por etapa", "distribución del número y valor de oportunidades entre etapas"),
        ],
        caso=(
            "El pipeline de Ruta Andina tiene ocho etapas con probabilidades de 10 % a 90 % asignadas al "
            "configurar el sistema. La probabilidad real de la etapa «propuesta» es 22 %, no 60 %."
        ),
        limite=(
            "Las probabilidades históricas suponen que el proceso y el mercado no cambiaron. Tras un cambio "
            "de oferta o de segmento deben recalcularse."
        ),
        libros=["roberge", "miller-heiman", "grove", "provost"],
        error=("Asignar probabilidades por intuición",
               "Calcula la tasa histórica de cierre por etapa y actualízala con datos cada semestre."),
    ),
    dict(
        n="03",
        slug="etapas-y-criterios-de-salida",
        titulo="Etapas y criterios de salida",
        tesis=(
            "Sin criterios de salida verificables, las etapas describen el optimismo del vendedor. El "
            "criterio debe ser un hecho observable del cliente —compartió datos, presentó al comité, "
            "confirmó presupuesto— y no una intención del vendedor. Esa disciplina es la que hace posible un "
            "forecast confiable: sin ella, cada avance de etapa significa cosas distintas según quién lo "
            "registró."
        ),
        conceptos=[
            ("evidencia de avance", "hecho verificable del cliente que justifica el cambio de etapa"),
            ("avance sin evidencia", "cambio de etapa basado en la percepción del vendedor"),
            ("retroceso de etapa", "corrección que devuelve la oportunidad a un estado anterior cuando la evidencia falla"),
            ("auditoría de etapas", "revisión periódica de que las oportunidades cumplen el criterio de su etapa"),
        ],
        metodo=[
            "definir un hecho del cliente por cada criterio de salida",
            "registrar la evidencia junto al cambio de etapa",
            "permitir y normalizar el retroceso de etapa",
            "auditar una muestra cada mes",
            "corregir el criterio si resulta inaplicable",
        ],
        senales=[
            ("avances con evidencia registrada", "cambios de etapa con evidencia documentada, sobre cambios de etapa"),
            ("tasa de retroceso", "oportunidades que retroceden de etapa, sobre oportunidades activas"),
            ("hallazgos de auditoría", "oportunidades que no cumplen el criterio de su etapa, sobre oportunidades auditadas"),
        ],
        caso=(
            "En Ruta Andina hay tres definiciones distintas de «propuesta enviada»: propuesta redactada, "
            "propuesta enviada por correo y propuesta presentada en reunión."
        ),
        limite=(
            "Criterios demasiado exigentes pueden dejar el pipeline vacío y desmotivar el registro. El "
            "criterio debe ser verificable y alcanzable."
        ),
        libros=["roberge", "miller-heiman", "grove", "keenan"],
        error=("Permitir avances de etapa sin evidencia",
               "Exige el registro del hecho del cliente que justifica cada cambio de etapa."),
    ),
    dict(
        n="04",
        slug="lead-contact-account-y-opportunity",
        titulo="Lead, contacto, cuenta y oportunidad",
        tesis=(
            "El modelo de datos define qué se puede analizar. Confundir un contacto con una cuenta impide "
            "ver cuántas oportunidades hay en una misma organización; confundir un lead con una oportunidad "
            "infla el pipeline. Las definiciones deben ser explícitas, compartidas entre marketing y ventas, "
            "y sostenidas por reglas del sistema y no sólo por acuerdos verbales."
        ),
        conceptos=[
            ("lead", "persona o empresa con interés potencial aún no calificada"),
            ("contacto", "persona identificada asociada a una cuenta"),
            ("cuenta", "organización cliente o potencial cliente como entidad única"),
            ("oportunidad", "posibilidad de venta calificada con valor, etapa y fecha estimada"),
        ],
        metodo=[
            "definir cada entidad por escrito y con ejemplos",
            "establecer las reglas de conversión entre entidades",
            "configurar el sistema para impedir duplicaciones",
            "capacitar al equipo con casos límite",
            "auditar la consistencia del modelo cada trimestre",
        ],
        senales=[
            ("duplicados de cuenta", "cuentas duplicadas detectadas, sobre cuentas totales"),
            ("oportunidades sin cuenta asociada", "oportunidades huérfanas, sobre oportunidades activas"),
            ("consistencia de conversión", "leads convertidos según la regla definida, sobre leads convertidos"),
        ],
        caso=(
            "La cadena de 14 locales aparece como 14 cuentas distintas en el CRM de Ruta Andina. Nadie puede "
            "ver el ingreso total ni el riesgo de concentración."
        ),
        limite=(
            "Un modelo de datos muy estricto puede no representar estructuras reales como grupos "
            "empresariales o franquicias. Debe existir un mecanismo de jerarquía."
        ),
        libros=["diorio", "roberge", "provost", "ross"],
        error=("Registrar sucursales como cuentas independientes",
               "Define la jerarquía de cuentas y consolida las sucursales bajo la organización matriz."),
    ),
    dict(
        n="05",
        slug="higiene-de-datos",
        titulo="Higiene de datos",
        tesis=(
            "Los datos comerciales se degradan de forma continua: personas cambian de trabajo, empresas "
            "cierran, correos rebotan. Sin un proceso de higiene, la base pierde valor cada mes y las "
            "decisiones se toman sobre información obsoleta. La higiene incluye además una obligación legal: "
            "mantener datos exactos y eliminarlos cuando ya no son necesarios para la finalidad declarada."
        ),
        conceptos=[
            ("degradación de datos", "pérdida progresiva de vigencia de la información de contacto"),
            ("deduplicación", "proceso de identificar y consolidar registros repetidos"),
            ("exactitud", "correspondencia entre el dato registrado y la realidad actual"),
            ("retención de datos", "periodo durante el cual se conserva la información según su finalidad"),
        ],
        metodo=[
            "medir el estado actual de completitud y exactitud",
            "establecer rutinas de deduplicación y verificación",
            "definir la política de retención y eliminación",
            "asignar responsables por tipo de dato",
            "reportar el estado de la base cada trimestre",
        ],
        senales=[
            ("tasa de datos obsoletos", "registros con rebote o contacto fallido, sobre registros contactados"),
            ("duplicados por trimestre", "duplicados detectados y consolidados, por trimestre"),
            ("cumplimiento de la política de retención", "registros eliminados según política, sobre registros que la cumplían"),
        ],
        caso=(
            "La base de Ruta Andina tiene 12.400 contactos, 31 % con rebote y registros de personas que "
            "solicitaron eliminación hace ocho meses."
        ),
        limite=(
            "La eliminación de datos puede entrar en tensión con obligaciones de conservación tributaria o "
            "contractual. La política debe distinguir tipos de dato y finalidad."
        ),
        libros=["diorio", "provost", "roberge", "oneil"],
        error=("No eliminar datos tras una solicitud del titular",
               "Implementa un procedimiento verificable de eliminación con plazo y registro de cumplimiento."),
    ),
    dict(
        n="06",
        slug="actividades-comerciales",
        titulo="Actividades comerciales",
        tesis=(
            "Las actividades —llamadas, reuniones, correos, propuestas— son los indicadores adelantados del "
            "resultado comercial. Su valor está en la relación con el resultado, no en el volumen absoluto: "
            "medir actividad sin conocer su conversión produce equipos ocupados y pipelines vacíos. Grove "
            "insistió en gestionar con indicadores adelantados, pero sólo los que predicen."
        ),
        conceptos=[
            ("indicador adelantado", "actividad que precede y predice el resultado comercial"),
            ("actividad de calidad", "interacción que cumple criterios definidos y no sólo un registro"),
            ("relación actividad-resultado", "proporción histórica entre volumen de actividad y negocios ganados"),
            ("actividad de vanidad", "registro que aumenta sin relación con el resultado"),
        ],
        metodo=[
            "definir qué cuenta como actividad de calidad",
            "medir la relación histórica entre actividad y resultado",
            "fijar metas de actividad derivadas de esa relación",
            "revisar la relación cuando cambia el proceso",
            "eliminar del seguimiento las actividades sin poder predictivo",
        ],
        senales=[
            ("actividades de calidad por vendedor", "interacciones que cumplen criterio, por vendedor y semana"),
            ("relación actividad-oportunidad", "oportunidades creadas, sobre actividades de calidad realizadas"),
            ("correlación actividad-resultado", "asociación observada entre volumen de actividad y negocios ganados"),
        ],
        caso=(
            "Ruta Andina exige 40 llamadas diarias. El equipo registra 40 llamadas y el 60 % dura menos de "
            "20 segundos."
        ),
        limite=(
            "Las metas de actividad pueden inducir el comportamiento que miden sin producir el resultado. "
            "Deben acompañarse de criterios de calidad y de revisión."
        ),
        libros=["grove", "roberge", "blount", "zoltners"],
        error=("Fijar metas de actividad sin criterio de calidad",
               "Define qué cuenta como actividad válida y verifica su relación real con el resultado."),
    ),
    dict(
        n="07",
        slug="forecast",
        titulo="Forecast",
        tesis=(
            "Un forecast es un compromiso sobre el futuro con un método declarado. Los tres enfoques "
            "habituales —ponderación por etapa, juicio del vendedor y análisis de cohortes históricas— "
            "tienen sesgos distintos y conviene contrastarlos. Lo que hace confiable a un forecast no es la "
            "sofisticación del cálculo sino la calidad de los criterios de etapa y la honestidad con que se "
            "revisan las desviaciones."
        ),
        conceptos=[
            ("método de forecast", "regla explícita que convierte el estado del pipeline en una proyección"),
            ("sesgo de optimismo", "tendencia sistemática a proyectar más de lo que se cierra"),
            ("precisión del forecast", "diferencia entre lo proyectado y lo efectivamente cerrado"),
            ("compromiso frente a mejor caso", "distinción entre lo que se asegura y lo que podría ocurrir"),
        ],
        metodo=[
            "declarar el método y su alcance",
            "separar compromiso, probable y mejor caso",
            "contrastar con al menos un método alternativo",
            "medir la precisión de cada ciclo",
            "corregir el método con el sesgo observado",
        ],
        senales=[
            ("precisión del forecast", "diferencia porcentual entre proyección y cierre real, por trimestre"),
            ("sesgo sistemático", "promedio de la desviación con signo, por vendedor y por periodo"),
            ("cobertura del pipeline", "valor del pipeline, sobre la meta del periodo"),
        ],
        caso=(
            "El forecast de Ruta Andina proyecta CLP 84 millones y cierra CLP 51 millones. La desviación se "
            "repite hace cuatro trimestres y nadie ha ajustado el método."
        ),
        limite=(
            "Ningún método corrige un pipeline con criterios de etapa débiles. La precisión del forecast es "
            "consecuencia de la disciplina de calificación, no de la fórmula."
        ),
        libros=["roberge", "grove", "provost", "wheeler-dv"],
        error=("Mantener el método pese a un sesgo sistemático",
               "Mide la desviación con signo por trimestre y corrige el método con ese factor."),
    ),
    dict(
        n="08",
        slug="cuotas-y-territorios",
        titulo="Cuotas y territorios",
        tesis=(
            "Una cuota mal calibrada produce comportamiento perverso: si es inalcanzable, el equipo "
            "desiste; si es demasiado baja, se deja negocio sobre la mesa. Los territorios mal repartidos "
            "generan desigualdad de oportunidad que ninguna habilidad compensa. Zoltners documenta que el "
            "diseño de cuotas y territorios explica una parte importante de la varianza de desempeño que "
            "suele atribuirse a las personas."
        ),
        conceptos=[
            ("cuota", "meta individual de resultado asignada para un periodo"),
            ("territorio", "conjunto de cuentas o zona asignada a un vendedor"),
            ("equidad de oportunidad", "grado en que los territorios ofrecen potencial comparable"),
            ("alcanzabilidad", "proporción del equipo que puede alcanzar la cuota con desempeño normal"),
        ],
        metodo=[
            "estimar el potencial por territorio con datos",
            "distribuir territorios buscando equidad de potencial",
            "derivar la cuota del potencial y no del deseo",
            "verificar la alcanzabilidad histórica",
            "revisar la asignación cada año con datos de resultado",
        ],
        senales=[
            ("proporción del equipo que alcanza la cuota", "vendedores que cumplen, sobre vendedores con cuota"),
            ("dispersión de potencial entre territorios", "diferencia de potencial estimado entre el mayor y el menor territorio"),
            ("rotación por territorio", "salidas del equipo, por territorio, en 12 meses"),
        ],
        caso=(
            "En Ruta Andina dos vendedores tienen la Región Metropolitana y cuatro se reparten el resto del "
            "país. Todos tienen la misma cuota."
        ),
        limite=(
            "La equidad perfecta de territorios no existe. El objetivo es que las diferencias sean conocidas y "
            "compensadas explícitamente en la cuota."
        ),
        libros=["zoltners", "roberge", "grove", "collins"],
        error=("Asignar la misma cuota a territorios de potencial distinto",
               "Estima el potencial por territorio y ajusta la cuota proporcionalmente."),
    ),
    dict(
        n="09",
        slug="sales-capacity",
        titulo="Capacidad comercial",
        tesis=(
            "La capacidad comercial es la cantidad de negocio que el equipo puede trabajar con calidad, "
            "considerando el tiempo real disponible y el esfuerzo que exige cada tipo de oportunidad. "
            "Planificar crecimiento sin calcularla produce dos errores simétricos: generar demanda que nadie "
            "atiende o contratar personas para un pipeline que no existe."
        ),
        conceptos=[
            ("capacidad por vendedor", "número de oportunidades que una persona puede trabajar con calidad simultáneamente"),
            ("tiempo comercial efectivo", "horas realmente disponibles para actividad de venta tras descontar tareas internas"),
            ("rampa de productividad", "tiempo que tarda una incorporación en alcanzar desempeño pleno"),
            ("capacidad del sistema", "resultado agregado que la estructura actual puede producir"),
        ],
        metodo=[
            "medir el tiempo comercial efectivo del equipo",
            "estimar el esfuerzo por tipo de oportunidad",
            "calcular la capacidad actual del sistema",
            "considerar la rampa antes de proyectar contrataciones",
            "ajustar la generación de demanda a la capacidad",
        ],
        senales=[
            ("tiempo comercial efectivo", "horas de actividad comercial, sobre horas laborales totales, por vendedor"),
            ("oportunidades activas por vendedor", "oportunidades abiertas asignadas, por vendedor"),
            ("duración de la rampa", "meses hasta alcanzar el desempeño objetivo, por incorporación"),
        ],
        caso=(
            "Ruta Andina planea generar 400 oportunidades mensuales con un equipo de seis personas que "
            "dedica el 38 % de su tiempo a tareas administrativas."
        ),
        limite=(
            "La capacidad no es fija: depende del proceso, de las herramientas y del tipo de negocio. "
            "Mejorar el proceso puede aumentar la capacidad sin contratar."
        ),
        libros=["roberge", "zoltners", "grove", "ross"],
        error=("Proyectar crecimiento sin calcular capacidad",
               "Mide el tiempo comercial efectivo y la carga por oportunidad antes de comprometer metas."),
    ),
    dict(
        n="10",
        slug="sales-velocity",
        titulo="Velocidad comercial",
        tesis=(
            "La velocidad comercial combina cuatro variables: número de oportunidades, valor promedio, tasa "
            "de cierre y duración del ciclo. Su utilidad no está en el número final sino en el diagnóstico: "
            "muestra qué palanca produce más efecto. Reducir el ciclo un 20 % suele ser más barato que "
            "aumentar el número de oportunidades en la misma proporción, y casi nunca se intenta."
        ),
        conceptos=[
            ("velocidad comercial", "resultado de combinar oportunidades, valor, tasa de cierre y duración del ciclo"),
            ("palanca dominante", "variable cuya mejora produce mayor efecto sobre el resultado"),
            ("duración del ciclo", "tiempo entre la creación de la oportunidad y su cierre"),
            ("efecto compuesto", "resultado de mejorar varias variables simultáneamente"),
        ],
        metodo=[
            "calcular las cuatro variables con datos propios",
            "simular el efecto de mejorar cada una por separado",
            "identificar la palanca dominante y su costo",
            "intervenir sobre esa palanca",
            "medir el efecto y recalcular",
        ],
        senales=[
            ("duración mediana del ciclo", "días entre creación y cierre de la oportunidad, mediana por segmento"),
            ("valor promedio de oportunidad", "valor total de negocios ganados, sobre número de negocios ganados"),
            ("velocidad comercial calculada", "resultado del cálculo combinado, seguido por trimestre"),
        ],
        caso=(
            "El ciclo mediano de Ruta Andina es 71 días y el 44 % de ese tiempo transcurre entre el envío de "
            "la propuesta y la primera respuesta del cliente."
        ),
        limite=(
            "Acelerar el ciclo puede reducir la calidad del diagnóstico y aumentar el churn posterior. La "
            "velocidad debe evaluarse junto con la retención."
        ),
        libros=["roberge", "grove", "croll-yoskovitz", "miller-heiman"],
        error=("Buscar sólo más oportunidades",
               "Simula el efecto de reducir el ciclo y de mejorar la tasa de cierre antes de aumentar la generación."),
    ),
    dict(
        n="11",
        slug="dashboards-comerciales",
        titulo="Dashboards comerciales",
        tesis=(
            "Un tablero comercial debe responder tres preguntas: cómo vamos, qué está en riesgo y qué "
            "requiere decisión. Todo lo demás sobra. El error habitual es acumular gráficos hasta que nadie "
            "los mira: un tablero con treinta métricas no informa, distrae. La regla de diseño es que cada "
            "elemento debe tener una acción asociada cuando se sale de rango."
        ),
        conceptos=[
            ("métrica accionable", "indicador con una acción definida cuando se desvía de su rango"),
            ("jerarquía del tablero", "orden que refleja la importancia de las decisiones que informa"),
            ("rango esperado", "banda de variación normal que evita reaccionar al ruido"),
            ("audiencia del tablero", "rol específico para el que se diseña el conjunto de indicadores"),
        ],
        metodo=[
            "definir la audiencia y sus decisiones",
            "elegir las métricas que informan esas decisiones",
            "establecer rangos esperados y acciones asociadas",
            "eliminar todo lo que no tenga acción",
            "revisar el uso real del tablero cada trimestre",
        ],
        senales=[
            ("métricas con acción definida", "indicadores con acción asociada, sobre indicadores del tablero"),
            ("uso del tablero", "consultas registradas por usuario, mensual"),
            ("decisiones tomadas con el tablero", "decisiones documentadas que lo citan, por trimestre"),
        ],
        caso=(
            "El tablero comercial de Ruta Andina tiene 22 gráficos. En la reunión semanal se revisan dos y "
            "las decisiones se toman con una planilla aparte."
        ),
        limite=(
            "Un tablero no reemplaza la conversación de gestión. Su función es enfocar la discusión, no "
            "sustituir el juicio sobre casos particulares."
        ),
        libros=["kaushik", "grove", "kaplan-norton", "wheeler-dv"],
        error=("Acumular métricas sin acción asociada",
               "Elimina del tablero toda métrica que no tenga una acción definida cuando se sale de rango."),
    ),
    dict(
        n="12",
        slug="revision-de-pipeline",
        titulo="Revisión de pipeline",
        tesis=(
            "La revisión de pipeline es una rutina de gestión, no una auditoría de personas. Su propósito es "
            "mejorar la posición de los negocios y detectar riesgos temprano. Cuando se convierte en "
            "interrogatorio, el vendedor aprende a presentar sólo lo favorable y la reunión pierde su función "
            "informativa. La estructura importa: mismos criterios, misma frecuencia, decisiones registradas."
        ),
        conceptos=[
            ("rutina de revisión", "reunión periódica con estructura y criterios estables"),
            ("riesgo detectado", "señal de que una oportunidad no avanzará según lo previsto"),
            ("decisión de la revisión", "acuerdo sobre qué hacer con cada negocio revisado"),
            ("clima de la revisión", "condiciones que determinan si la información fluye o se oculta"),
        ],
        metodo=[
            "definir la estructura y los criterios de la revisión",
            "revisar por evidencia y no por sensación",
            "identificar riesgos y acordar acciones",
            "registrar las decisiones y sus responsables",
            "verificar el cumplimiento en la revisión siguiente",
        ],
        senales=[
            ("oportunidades revisadas por sesión", "oportunidades analizadas, sobre oportunidades relevantes del periodo"),
            ("acciones acordadas cumplidas", "acciones ejecutadas, sobre acciones acordadas en la revisión anterior"),
            ("riesgos detectados con anticipación", "negocios donde el riesgo se detectó antes del cierre previsto, sobre negocios perdidos"),
        ],
        caso=(
            "La revisión semanal de Ruta Andina dura dos horas y revisa 380 oportunidades sin criterio de "
            "selección. Nadie recuerda qué se acordó la semana anterior."
        ),
        limite=(
            "Revisar todo el pipeline cada semana es imposible y contraproducente. La revisión debe "
            "concentrarse en los negocios que concentran valor o riesgo."
        ),
        libros=["grove", "roberge", "miller-heiman", "lencioni"],
        error=("Revisar todo el pipeline sin criterio de selección",
               "Selecciona por valor y riesgo, y registra las decisiones con responsable y fecha."),
    ),
    dict(
        n="13",
        slug="gobierno-del-crm",
        titulo="Gobierno del CRM",
        tesis=(
            "Sin gobierno, un CRM acumula campos, automatizaciones y excepciones hasta volverse "
            "inmanejable. El gobierno define quién puede cambiar qué, cómo se solicitan modificaciones, "
            "cómo se documentan y con qué frecuencia se revisa el conjunto. También define la "
            "responsabilidad sobre datos personales: quién accede, para qué y con qué registro."
        ),
        conceptos=[
            ("responsable del sistema", "persona que decide sobre configuración y cambios"),
            ("procedimiento de cambio", "regla que ordena cómo se solicitan y aprueban modificaciones"),
            ("control de acceso", "definición de quién puede ver y modificar cada tipo de dato"),
            ("deuda de configuración", "acumulación de campos y reglas sin uso que degradan el sistema"),
        ],
        metodo=[
            "designar responsable y procedimiento de cambio",
            "documentar la configuración vigente",
            "definir el control de acceso por rol",
            "revisar y eliminar la deuda de configuración cada semestre",
            "auditar accesos y registro de tratamiento de datos",
        ],
        senales=[
            ("cambios documentados", "modificaciones con solicitud y aprobación registradas, sobre cambios realizados"),
            ("campos y reglas sin uso", "elementos de configuración sin uso, sobre elementos totales"),
            ("accesos revisados", "usuarios con permisos revisados en el último semestre, sobre usuarios activos"),
        ],
        caso=(
            "El CRM de Ruta Andina tiene 14 automatizaciones creadas por tres personas distintas. Dos se "
            "contradicen y nadie sabe quién las creó ni por qué."
        ),
        limite=(
            "Un gobierno demasiado rígido frena mejoras necesarias. El procedimiento debe ser proporcional al "
            "riesgo del cambio solicitado."
        ),
        libros=["diorio", "grove", "nist-airmf", "roberge"],
        error=("Permitir cambios sin registro ni responsable",
               "Designa un responsable del sistema y exige solicitud documentada para cada cambio de configuración."),
    ),
    dict(
        n="14",
        slug="diseno-de-sales-operations",
        titulo="Diseño de sales operations",
        tesis=(
            "Esta clase integra la parte en un diseño operativo: modelo de datos, pipeline con criterios, "
            "rutinas de gestión, forecast, cuotas, capacidad, tableros y gobierno. La prueba de calidad es "
            "la continuidad: el sistema debe funcionar cuando cambia la jefatura, cuando entra alguien nuevo "
            "y cuando el volumen crece un 50 %."
        ),
        conceptos=[
            ("diseño operativo", "conjunto documentado de procesos, datos, rutinas y responsabilidades comerciales"),
            ("escalabilidad", "capacidad del diseño de sostener un aumento de volumen sin rediseño completo"),
            ("continuidad", "funcionamiento del sistema con independencia de las personas específicas"),
            ("documentación viva", "registro que se mantiene actualizado con responsable y versión"),
        ],
        metodo=[
            "consolidar modelo de datos, pipeline y rutinas",
            "documentar forecast, cuotas y capacidad",
            "definir gobierno y responsables",
            "probar el diseño con un escenario de crecimiento",
            "establecer la revisión periódica del conjunto",
        ],
        senales=[
            ("precisión del forecast", "diferencia entre proyección y resultado, por trimestre"),
            ("tiempo de incorporación al sistema", "días hasta que una persona nueva opera con autonomía"),
            ("cobertura de documentación", "procesos documentados y vigentes, sobre procesos definidos"),
        ],
        caso=(
            "Ruta Andina proyecta duplicar su equipo comercial en 12 meses. Hoy el sistema no sobrevive a la "
            "ausencia de una persona clave."
        ),
        limite=(
            "Un diseño operativo pensado para el volumen actual puede fallar al escalar. La prueba de "
            "crecimiento debe ejecutarse antes de contratar, no después."
        ),
        libros=["roberge", "diorio", "grove", "zoltners"],
        error=("Diseñar la operación para el volumen actual",
               "Prueba el diseño con un escenario de crecimiento del 50 % antes de comprometer contrataciones."),
    ),
]
