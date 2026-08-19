# -*- coding: utf-8 -*-
"""Parte 23 — Dirección comercial: CMO, VP Sales y CRO."""

CLASES = [
    dict(
        n="01",
        slug="diseno-de-la-organizacion-comercial",
        titulo="Diseño de la organización comercial",
        tesis=(
            "La estructura comercial no es un organigrama: es una decisión sobre cómo se divide el trabajo, "
            "quién responde por qué resultado y dónde ocurren las transferencias. Cada división crea una "
            "frontera y toda frontera es un punto de pérdida. La especialización aumenta la productividad y "
            "el número de traspasos; el criterio es el volumen y la complejidad, no la moda organizacional."
        ),
        conceptos=[
            ("especialización", "división del trabajo comercial en roles con foco definido"),
            ("frontera organizacional", "punto donde el trabajo pasa de un equipo a otro y puede perderse contexto"),
            ("responsabilidad por resultado", "asignación explícita de quién responde por cada número"),
            ("costo de coordinación", "esfuerzo adicional que exige mantener alineados a los equipos especializados"),
        ],
        metodo=[
            "mapear el trabajo comercial completo",
            "decidir el nivel de especialización según volumen y complejidad",
            "identificar las fronteras y su mecanismo de traspaso",
            "asignar responsabilidad por resultado a cada rol",
            "medir la pérdida en cada frontera",
        ],
        senales=[
            ("pérdida por frontera", "oportunidades o contexto perdidos en cada traspaso, por periodo"),
            ("productividad por rol", "resultado generado, por persona y por tipo de rol"),
            ("costo de coordinación", "horas de reuniones y alineamiento, sobre horas totales del equipo"),
        ],
        caso=(
            "Ruta Andina quiere separar prospección, venta e implementación con seis personas. Cada frontera "
            "adicional exige traspasos que hoy nadie documenta."
        ),
        limite=(
            "La especialización requiere volumen suficiente para justificar cada rol. En equipos pequeños "
            "produce personas subutilizadas y traspasos innecesarios."
        ),
        libros=["ross", "roberge", "grove", "zoltners"],
        error=("Especializar sin volumen que lo justifique",
               "Calcula la carga por rol antes de dividir; si no llena una posición, no crees la frontera."),
    ),
    dict(
        n="02",
        slug="roles-y-responsabilidades",
        titulo="Roles y responsabilidades",
        tesis=(
            "La ambigüedad de responsabilidades es una de las causas más frecuentes de bajo desempeño "
            "comercial y una de las más fáciles de corregir. Definir un rol implica declarar qué resultado "
            "produce, qué decisiones puede tomar sin consultar, con quién debe coordinar y cómo se mide. "
            "Cuando dos personas creen ser responsables de lo mismo, nadie lo es."
        ),
        conceptos=[
            ("resultado del rol", "output medible por el que la persona responde"),
            ("derecho de decisión", "conjunto de decisiones que el rol puede tomar sin autorización"),
            ("interfaz de coordinación", "personas o equipos con quienes el rol debe coordinar por diseño"),
            ("ambigüedad de responsabilidad", "situación en que un resultado no tiene un dueño único"),
        ],
        metodo=[
            "definir el resultado medible de cada rol",
            "declarar los derechos de decisión",
            "mapear las interfaces de coordinación",
            "identificar resultados sin dueño único",
            "revisar la definición cuando cambia la estructura",
        ],
        senales=[
            ("resultados con dueño único", "indicadores con un solo responsable, sobre indicadores del área"),
            ("decisiones escaladas innecesariamente", "consultas sobre decisiones que el rol podía tomar, por periodo"),
            ("conflictos de responsabilidad", "casos de responsabilidad disputada registrados, por trimestre"),
        ],
        caso=(
            "En Ruta Andina, marketing y ventas se atribuyen la responsabilidad sobre la conversión de leads. "
            "Cuando el número cae, cada área explica por qué no le corresponde."
        ),
        limite=(
            "Las definiciones muy detalladas producen rigidez y comportamiento defensivo. El objetivo es "
            "eliminar la ambigüedad crítica, no describir cada tarea."
        ),
        libros=["grove", "lencioni", "zoltners", "roberge"],
        error=("Dejar indicadores con responsabilidad compartida",
               "Asigna un dueño único a cada indicador y declara quiénes contribuyen sin responder por él."),
    ),
    dict(
        n="03",
        slug="contratacion",
        titulo="Contratación comercial",
        tesis=(
            "Contratar bien en ventas es una de las decisiones de mayor impacto y una de las peor "
            "ejecutadas. Roberge propuso construir el perfil desde datos: qué características distinguen a "
            "quienes tuvieron éxito en esta empresa concreta, no en abstracto. El proceso debe evaluar "
            "capacidades verificables con ejercicios reales, no impresiones de entrevista."
        ),
        conceptos=[
            ("perfil basado en datos", "conjunto de características derivadas del desempeño observado en la empresa"),
            ("evaluación por desempeño", "ejercicio que reproduce una tarea real del rol"),
            ("costo de un error de contratación", "gasto total de un mal reclutamiento, incluidos tiempo, oportunidad y clima"),
            ("sesgo de entrevista", "influencia de impresiones no predictivas sobre la decisión de contratar"),
        ],
        metodo=[
            "analizar qué distinguió a quienes tuvieron éxito",
            "construir el perfil con esas características",
            "diseñar ejercicios que reproduzcan tareas reales",
            "estructurar la entrevista para reducir sesgos",
            "medir la correlación entre evaluación y desempeño posterior",
        ],
        senales=[
            ("desempeño de las incorporaciones", "cumplimiento de cuota a 12 meses, por cohorte de contratación"),
            ("rotación temprana", "salidas antes de 12 meses, sobre incorporaciones del periodo"),
            ("correlación evaluación-desempeño", "asociación entre el puntaje de selección y el resultado posterior"),
        ],
        caso=(
            "Ruta Andina contrata por entrevista y referencias. Su rotación comercial anual es 62 % y nadie "
            "ha analizado qué distinguió a los dos vendedores que sí funcionaron."
        ),
        limite=(
            "Un perfil derivado de pocos casos exitosos puede reproducir sesgos y estrechar la diversidad del "
            "equipo. Debe revisarse con criterio y no aplicarse mecánicamente."
        ),
        libros=["roberge", "collins", "zoltners", "lencioni"],
        error=("Contratar por impresión de entrevista",
               "Incorpora un ejercicio que reproduzca una tarea real y mide su correlación con el desempeño."),
    ),
    dict(
        n="04",
        slug="onboarding-de-equipos",
        titulo="Onboarding de equipos comerciales",
        tesis=(
            "El tiempo hasta la productividad plena es un costo directo: cada mes de rampa es salario sin "
            "resultado. Un onboarding estructurado —producto, cliente, proceso, herramientas, práctica "
            "supervisada— reduce ese tiempo de forma medible. La alternativa habitual, aprender observando, "
            "produce rampas largas y reproduce los defectos del vendedor que acompaña."
        ),
        conceptos=[
            ("rampa de productividad", "tiempo hasta alcanzar el desempeño objetivo del rol"),
            ("certificación", "verificación de que la persona domina un componente antes de avanzar"),
            ("práctica supervisada", "ejecución real con acompañamiento y retroalimentación inmediata"),
            ("costo de la rampa", "gasto acumulado durante el periodo de baja productividad"),
        ],
        metodo=[
            "definir los componentes que la persona debe dominar",
            "estructurar la secuencia con certificaciones",
            "incorporar práctica supervisada temprana",
            "medir la duración de la rampa por cohorte",
            "corregir el programa con los datos de desempeño",
        ],
        senales=[
            ("duración de la rampa", "meses hasta alcanzar el desempeño objetivo, por incorporación"),
            ("certificaciones aprobadas en plazo", "componentes certificados dentro del plazo previsto, sobre componentes del programa"),
            ("desempeño a 6 meses", "cumplimiento de cuota al medio año, por cohorte de incorporación"),
        ],
        caso=(
            "Las incorporaciones de Ruta Andina acompañan a un vendedor senior durante dos semanas y luego "
            "trabajan solas. La rampa promedio es siete meses."
        ),
        limite=(
            "Un onboarding demasiado largo retrasa el aporte y desmotiva. La estructura debe combinar "
            "formación con práctica real desde temprano."
        ),
        libros=["roberge", "ericsson", "grove", "ambrose"],
        error=("Formar por observación sin certificación",
               "Define componentes con verificación explícita y combina formación con práctica supervisada."),
    ),
    dict(
        n="05",
        slug="compensacion-e-incentivos",
        titulo="Compensación e incentivos",
        tesis=(
            "El esquema de compensación es la declaración más honesta de lo que la empresa realmente quiere. "
            "Zoltners documenta que los incentivos producen exactamente el comportamiento que premian, "
            "incluidos los efectos no deseados: premiar sólo ingreso nuevo produce descuentos agresivos y "
            "clientes que no renuevan. El diseño debe incluir contrapesos y ser simple de entender."
        ),
        conceptos=[
            ("estructura de compensación", "combinación de fijo, variable y aceleradores del esquema"),
            ("efecto no deseado", "comportamiento perverso inducido por el diseño del incentivo"),
            ("contrapeso", "componente que penaliza el resultado obtenido a costa de otro objetivo"),
            ("comprensibilidad", "capacidad del vendedor de calcular su propia remuneración"),
        ],
        metodo=[
            "declarar qué comportamiento se quiere producir",
            "diseñar el esquema y simular sus efectos",
            "identificar los efectos no deseados posibles",
            "incorporar contrapesos sobre margen y retención",
            "verificar que el esquema sea comprensible y estable",
        ],
        senales=[
            ("dispersión de descuentos", "descuento promedio otorgado, por vendedor y periodo"),
            ("retención de clientes por vendedor", "retención a 12 meses de los clientes que cada vendedor cerró"),
            ("comprensión del esquema", "vendedores que calculan correctamente su remuneración, en verificación"),
        ],
        caso=(
            "La comisión de Ruta Andina paga sobre ingreso firmado sin considerar margen ni permanencia. El "
            "descuento promedio de cierre de mes es 22 % y esos clientes retienen la mitad."
        ),
        limite=(
            "Un esquema con demasiados componentes deja de orientar el comportamiento porque nadie entiende "
            "qué maximiza. La simplicidad tiene valor propio."
        ),
        libros=["zoltners", "grove", "roberge", "collins"],
        error=("Compensar sólo ingreso firmado",
               "Incorpora contrapesos de margen y permanencia, y verifica que el esquema siga siendo comprensible."),
    ),
    dict(
        n="06",
        slug="presupuesto",
        titulo="Presupuesto comercial",
        tesis=(
            "El presupuesto comercial traduce la estrategia en asignación de recursos. Su calidad se mide "
            "por la explicitación de supuestos: cuántas oportunidades por peso invertido, qué conversión, "
            "qué capacidad. Un presupuesto construido con porcentajes del año anterior no permite discutir "
            "prioridades ni evaluar desviaciones."
        ),
        conceptos=[
            ("supuesto presupuestario", "estimación declarada que sostiene cada línea del presupuesto"),
            ("presupuesto base cero", "construcción desde la necesidad y no desde el histórico"),
            ("flexibilidad presupuestaria", "capacidad de reasignar durante el periodo según resultados"),
            ("desviación explicada", "diferencia entre lo planificado y lo ejecutado con su causa identificada"),
        ],
        metodo=[
            "derivar el presupuesto de la meta y de los supuestos",
            "declarar cada supuesto y su fuente",
            "definir reglas de reasignación durante el periodo",
            "medir la desviación y explicarla",
            "usar el aprendizaje para el ciclo siguiente",
        ],
        senales=[
            ("desviación presupuestaria", "diferencia entre gasto planificado y ejecutado, por línea"),
            ("supuestos verificados", "supuestos que se cumplieron, sobre supuestos declarados"),
            ("reasignaciones ejecutadas", "movimientos entre líneas realizados según regla, por trimestre"),
        ],
        caso=(
            "El presupuesto de Ruta Andina para el próximo año repite el del anterior con un aumento del 12 "
            "%. Ningún supuesto está declarado."
        ),
        limite=(
            "Un presupuesto demasiado rígido impide aprovechar oportunidades. La flexibilidad debe estar "
            "definida en reglas, no en excepciones informales."
        ),
        libros=["grove", "doerr", "kaplan-norton", "croll-yoskovitz"],
        error=("Construir el presupuesto como porcentaje del año anterior",
               "Deriva cada línea de la meta y declara el supuesto que la sostiene."),
    ),
    dict(
        n="07",
        slug="okr-y-kpi",
        titulo="OKR y KPI",
        tesis=(
            "Los indicadores describen el estado del negocio; los objetivos con resultados clave describen "
            "lo que se quiere cambiar. Confundirlos produce dos patologías: convertir todos los indicadores "
            "en metas, lo que dispersa el foco, o fijar objetivos sin indicadores que permitan verificarlos. "
            "Doerr insiste en pocos objetivos y en resultados clave medibles, no en actividades."
        ),
        conceptos=[
            ("indicador de estado", "métrica que describe cómo está el negocio de forma continua"),
            ("resultado clave", "cambio medible que se busca producir en un periodo"),
            ("objetivo", "propósito cualitativo que orienta los resultados clave"),
            ("confusión meta-indicador", "error de convertir toda métrica en objetivo del periodo"),
        ],
        metodo=[
            "separar indicadores de estado de objetivos del periodo",
            "definir pocos objetivos con resultados clave medibles",
            "verificar que los resultados clave sean resultados y no actividades",
            "revisar el avance con periodicidad definida",
            "cerrar el ciclo evaluando el aprendizaje",
        ],
        senales=[
            ("número de objetivos activos", "objetivos vigentes por equipo, comparados con el máximo definido"),
            ("resultados clave medibles", "resultados clave con métrica y línea base, sobre resultados clave definidos"),
            ("cumplimiento por ciclo", "resultados clave alcanzados, sobre resultados clave comprometidos"),
        ],
        caso=(
            "El equipo comercial de Ruta Andina tiene 14 objetivos trimestrales, la mayoría formulados como "
            "actividades: «implementar CRM», «lanzar campaña»."
        ),
        limite=(
            "Los objetivos ambiciosos vinculados a compensación inducen conservadurismo. Doerr recomienda "
            "separar el sistema de objetivos del sistema de remuneración."
        ),
        libros=["doerr", "grove", "kaplan-norton", "collins"],
        error=("Formular resultados clave como actividades",
               "Reescribe cada resultado clave como un cambio medible con línea base y meta."),
    ),
    dict(
        n="08",
        slug="forecast-ejecutivo",
        titulo="Forecast ejecutivo",
        tesis=(
            "El forecast que llega a la dirección debe distinguir con claridad qué está comprometido, qué es "
            "probable y qué es el mejor caso, con el método declarado y la precisión histórica visible. Un "
            "forecast presentado como cifra única sin historial de precisión no permite decidir: obliga a la "
            "dirección a aplicar su propio descuento mental, distinto en cada persona."
        ),
        conceptos=[
            ("categoría de forecast", "clasificación entre comprometido, probable y mejor caso"),
            ("precisión histórica", "registro de la desviación entre proyección y resultado en periodos anteriores"),
            ("supuesto de la proyección", "condición declarada que sostiene la estimación"),
            ("descuento mental", "ajuste informal que cada ejecutivo aplica a un forecast poco confiable"),
        ],
        metodo=[
            "clasificar el pipeline en categorías con criterios",
            "declarar el método y sus supuestos",
            "presentar la precisión histórica junto a la proyección",
            "identificar los negocios que concentran el riesgo",
            "actualizar con frecuencia definida y registrar los cambios",
        ],
        senales=[
            ("precisión histórica del forecast", "desviación entre proyección y resultado, últimos cuatro trimestres"),
            ("concentración del riesgo", "valor de los tres negocios mayores, sobre el valor total de la proyección del periodo"),
            ("variación entre actualizaciones", "cambio de la proyección entre actualizaciones sucesivas del mismo periodo"),
        ],
        caso=(
            "El forecast de Ruta Andina llega al directorio como una cifra única. En los últimos cuatro "
            "trimestres se desvió entre 28 % y 41 % y esa información nunca se presenta."
        ),
        limite=(
            "Un forecast conservador sistemático también es un problema: induce decisiones de inversión más "
            "tímidas que las que el negocio permite."
        ),
        libros=["grove", "roberge", "wheeler-dv", "kaplan-norton"],
        error=("Presentar el forecast sin precisión histórica",
               "Acompaña cada proyección con la desviación de los cuatro periodos anteriores."),
    ),
    dict(
        n="09",
        slug="reuniones-operativas",
        titulo="Reuniones operativas",
        tesis=(
            "Grove describió las reuniones como una herramienta de producción gerencial, no como un costo "
            "inevitable. Una reunión comercial efectiva tiene propósito único, participantes necesarios, "
            "información previa distribuida y decisiones registradas. El ritmo importa tanto como el "
            "contenido: un calendario de revisiones estable produce disciplina sin necesidad de "
            "supervisión constante."
        ),
        conceptos=[
            ("propósito de la reunión", "resultado específico que la reunión debe producir"),
            ("información previa", "material distribuido antes para que el tiempo se use en decidir"),
            ("decisión registrada", "acuerdo documentado con responsable y fecha"),
            ("ritmo de gestión", "calendario estable de reuniones que sostiene la operación"),
        ],
        metodo=[
            "definir el propósito y los participantes necesarios",
            "distribuir la información con anticipación",
            "usar el tiempo en decisiones y no en informar",
            "registrar decisiones con responsable y fecha",
            "verificar el cumplimiento en la reunión siguiente",
        ],
        senales=[
            ("decisiones por reunión", "acuerdos registrados, por reunión realizada"),
            ("cumplimiento de acuerdos", "acuerdos ejecutados en plazo, sobre acuerdos registrados"),
            ("tiempo en reuniones", "horas semanales en reuniones, por persona del equipo comercial"),
        ],
        caso=(
            "La reunión comercial semanal de Ruta Andina dura dos horas, se dedica a informar cifras que ya "
            "están en el tablero y no registra acuerdos."
        ),
        limite=(
            "Reducir reuniones sin sustituir su función de coordinación produce desalineamiento. El criterio "
            "es mejorar su diseño, no eliminarlas."
        ),
        libros=["grove", "lencioni", "doerr", "collins"],
        error=("Usar la reunión para informar lo que ya está publicado",
               "Distribuye la información antes y usa el tiempo exclusivamente en decisiones."),
    ),
    dict(
        n="10",
        slug="coaching-comercial",
        titulo="Coaching comercial",
        tesis=(
            "El acompañamiento comercial produce más mejora que la formación en aula, con una condición: "
            "debe ser específico, frecuente y basado en observación real. Ericsson mostró que la práctica "
            "deliberada requiere criterios explícitos y retroalimentación inmediata. Un acompañamiento que "
            "sólo revisa números no es coaching: es control disfrazado."
        ),
        conceptos=[
            ("observación real", "presencia en la interacción con el cliente o revisión de su registro"),
            ("retroalimentación específica", "comentario sobre un comportamiento concreto y observable"),
            ("práctica deliberada", "ejercicio focalizado en una habilidad con criterio y corrección"),
            ("frecuencia de acompañamiento", "regularidad con que ocurre la sesión de desarrollo"),
        ],
        metodo=[
            "observar interacciones reales con regularidad",
            "identificar una habilidad específica por ciclo",
            "entregar retroalimentación sobre comportamiento observable",
            "practicar la habilidad en un ejercicio dirigido",
            "verificar la mejora en la siguiente observación",
        ],
        senales=[
            ("sesiones de acompañamiento por vendedor", "sesiones realizadas, por vendedor y por mes"),
            ("mejora en la habilidad trabajada", "cambio observable en el comportamiento entre observaciones sucesivas"),
            ("relación acompañamiento-desempeño", "diferencia de resultado entre vendedores con más y menos acompañamiento"),
        ],
        caso=(
            "La jefatura comercial de Ruta Andina dedica sus reuniones individuales a revisar el pipeline. "
            "Nunca ha escuchado una llamada completa de su equipo."
        ),
        limite=(
            "El acompañamiento requiere tiempo de jefatura que compite con la gestión. Sin proteger ese "
            "tiempo en el calendario, no ocurre."
        ),
        libros=["ericsson", "roberge", "grove", "rackham"],
        error=("Confundir revisión de pipeline con coaching",
               "Reserva sesiones específicas de desarrollo basadas en observación real de interacciones."),
    ),
    dict(
        n="11",
        slug="gestion-de-desempeno",
        titulo="Gestión de desempeño",
        tesis=(
            "Gestionar desempeño exige distinguir tres causas de resultado insuficiente: falta de capacidad, "
            "falta de claridad o condiciones del territorio. Cada una requiere una intervención distinta y "
            "confundirlas produce injusticia y rotación innecesaria. Un vendedor con territorio pobre no "
            "mejora con más presión, y uno sin claridad de proceso no mejora con más formación genérica."
        ),
        conceptos=[
            ("diagnóstico de causa", "identificación de si el problema es de capacidad, claridad o condiciones"),
            ("condiciones del territorio", "potencial y dificultad del mercado asignado a la persona"),
            ("plan de mejora", "acuerdo con objetivos, apoyo y plazo definidos"),
            ("decisión de salida", "conclusión de que la persona no puede desempeñarse en el rol"),
        ],
        metodo=[
            "diagnosticar la causa con datos y observación",
            "descartar condiciones de territorio antes de evaluar a la persona",
            "acordar un plan de mejora con apoyo y plazo",
            "verificar el avance en los hitos definidos",
            "tomar la decisión con criterio previo y registro",
        ],
        senales=[
            ("desempeño ajustado por potencial de territorio", "resultado obtenido, sobre potencial estimado del territorio"),
            ("planes de mejora con resultado", "personas que superan el estándar tras el plan, sobre planes ejecutados"),
            ("rotación no deseada", "salidas de personas con buen desempeño, sobre salidas totales"),
        ],
        caso=(
            "Ruta Andina puso en plan de mejora a dos vendedores de regiones. Su territorio tiene un tercio "
            "del potencial del territorio metropolitano y la cuota es la misma."
        ),
        limite=(
            "Postergar una decisión de salida necesaria daña al equipo y a la persona. El plan de mejora "
            "debe tener plazo y consecuencia definidos."
        ),
        libros=["grove", "zoltners", "lencioni", "collins"],
        error=("Evaluar desempeño sin ajustar por potencial de territorio",
               "Normaliza el resultado por el potencial asignado antes de concluir sobre la persona."),
    ),
    dict(
        n="12",
        slug="etica-y-cultura",
        titulo="Ética y cultura comercial",
        tesis=(
            "La cultura comercial se define por lo que la organización tolera bajo presión, no por lo que "
            "declara en sus valores. Un equipo que cierra el trimestre con promesas imposibles aprendió que "
            "eso está permitido. La dirección construye cultura con tres actos: qué premia, qué sanciona y "
            "qué hace cuando el resultado depende de cruzar una línea."
        ),
        conceptos=[
            ("cultura efectiva", "conjunto de comportamientos que la organización realmente tolera y premia"),
            ("prueba de presión", "situación en que cumplir la meta exige comprometer un principio"),
            ("consecuencia visible", "acción de la dirección ante un incumplimiento ético, observada por el equipo"),
            ("costo de la tolerancia", "efecto acumulado de permitir prácticas indebidas por resultado"),
        ],
        metodo=[
            "declarar las líneas que no se cruzan, con ejemplos concretos",
            "revisar qué premia y qué sanciona el sistema actual",
            "actuar visiblemente ante el primer incumplimiento",
            "revisar los casos límite con el equipo",
            "medir señales de deterioro: reclamos, promesas incumplidas, rotación",
        ],
        senales=[
            ("reclamos por promesas incumplidas", "reclamos vinculados a compromisos comerciales, sobre ventas del periodo"),
            ("casos de incumplimiento con consecuencia", "incumplimientos con acción documentada, sobre incumplimientos detectados"),
            ("rotación asociada a clima", "salidas cuyo motivo declarado es clima o prácticas, sobre salidas totales"),
        ],
        caso=(
            "Un vendedor de Ruta Andina cerró el trimestre prometiendo una integración inexistente. La "
            "gerencia celebró el resultado y el equipo tomó nota."
        ),
        limite=(
            "Una cultura estricta sin criterio produce parálisis y ocultamiento. Debe existir un mecanismo "
            "para plantear casos límite sin costo para quien los plantea."
        ),
        libros=["lencioni", "collins", "cialdini", "oneil"],
        error=("Premiar un resultado obtenido cruzando una línea",
               "Actúa visiblemente ante el primer caso: la ausencia de consecuencia es la política real."),
    ),
    dict(
        n="13",
        slug="board-reporting",
        titulo="Reporte al directorio",
        tesis=(
            "Reportar al directorio exige seleccionar: qué debe saber quien no está en la operación diaria "
            "para cumplir su rol de supervisión y decisión. Un buen reporte presenta resultado frente a "
            "plan, las tres o cuatro causas del desvío, las decisiones que requieren aprobación y los "
            "riesgos relevantes. Ocultar malas noticias es la falla más grave: destruye la confianza que "
            "hace posible el rol."
        ),
        conceptos=[
            ("resultado frente a plan", "comparación del desempeño con el compromiso previo"),
            ("causa del desvío", "explicación verificable de la diferencia entre lo planificado y lo logrado"),
            ("decisión que requiere aprobación", "asunto que excede la autoridad de la gerencia"),
            ("transparencia sobre riesgos", "declaración anticipada de los problemas relevantes"),
        ],
        metodo=[
            "presentar resultado frente a plan con contexto",
            "explicar las causas principales del desvío",
            "declarar los riesgos antes de que se materialicen",
            "solicitar explícitamente las decisiones que requieren aprobación",
            "registrar los acuerdos y hacer seguimiento",
        ],
        senales=[
            ("anticipación de riesgos", "riesgos reportados antes de materializarse, sobre riesgos materializados"),
            ("decisiones resueltas en sesión", "decisiones solicitadas y resueltas, sobre decisiones presentadas"),
            ("consistencia entre reportes", "coherencia de las cifras entre sesiones sucesivas"),
        ],
        caso=(
            "La gerencia comercial de Ruta Andina reportó el churn por primera vez cuando ya afectaba el "
            "presupuesto anual. El directorio lo interpretó como ocultamiento."
        ),
        limite=(
            "Un reporte exhaustivo consume el tiempo del directorio en detalle operativo. La selección es "
            "parte del trabajo de dirección."
        ),
        libros=["grove", "kaplan-norton", "collins", "doerr"],
        error=("Reportar un riesgo cuando ya se materializó",
               "Declara los riesgos relevantes en el reporte anterior a su posible materialización."),
    ),
    dict(
        n="14",
        slug="operating-system-del-cro",
        titulo="Operating system del CRO",
        tesis=(
            "Esta clase integra la parte en un sistema de dirección: estructura, roles, plan, presupuesto, "
            "objetivos, ritmo de gestión, incentivos, desarrollo, gobierno y reporte. La prueba de calidad "
            "es la independencia: el sistema debe producir resultados sin que la dirección esté presente en "
            "cada decisión, y debe permitir detectar problemas antes de que aparezcan en los estados "
            "financieros."
        ),
        conceptos=[
            ("sistema de dirección", "conjunto de estructuras, rutinas e indicadores que gobiernan la función de ingresos"),
            ("independencia del sistema", "capacidad de operar sin intervención permanente de la dirección"),
            ("detección temprana", "identificación de problemas antes de su efecto financiero"),
            ("ritmo institucional", "calendario de revisiones y decisiones que sostiene la operación"),
        ],
        metodo=[
            "consolidar estructura, roles y responsabilidades",
            "documentar plan, presupuesto y objetivos",
            "establecer el ritmo de gestión y sus reuniones",
            "definir incentivos, desarrollo y gobierno",
            "verificar la independencia con una prueba de ausencia",
        ],
        senales=[
            ("decisiones tomadas sin escalamiento", "decisiones resueltas en el nivel correspondiente, sobre decisiones tomadas"),
            ("detección temprana de desvíos", "desvíos detectados antes del cierre del periodo, sobre desvíos ocurridos"),
            ("continuidad ante ausencias", "cumplimiento de rutinas durante ausencias de la dirección"),
        ],
        caso=(
            "El directorio pide a Ruta Andina duplicar ingresos en 18 meses. La propuesta inicial es "
            "contratar seis vendedores sin modificar proceso, oferta ni retención."
        ),
        limite=(
            "Un sistema de dirección maduro no compensa una estrategia equivocada: ejecuta con disciplina una "
            "dirección que puede ser incorrecta."
        ),
        libros=["grove", "doerr", "collins", "kaplan-norton"],
        error=("Escalar el equipo sin corregir el motor comercial",
               "Verifica proceso, oferta y retención antes de comprometer contrataciones de escala."),
    ),
]
