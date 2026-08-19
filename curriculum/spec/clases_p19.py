# -*- coding: utf-8 -*-
"""Parte 19 — Growth marketing y growth engineering."""

CLASES = [
    dict(
        n="01",
        slug="que-es-growth",
        titulo="Qué es growth",
        tesis=(
            "Growth no es un canal ni un conjunto de trucos: es un método de trabajo multifuncional que "
            "aplica experimentación sistemática a todo el recorrido del cliente, incluido el producto. Ellis "
            "y Brown lo describen como un ciclo —analizar, idear, priorizar, probar— ejecutado por un equipo "
            "con acceso a producto, datos y marketing. Sin ese acceso, growth se degrada a optimización de "
            "campañas."
        ),
        conceptos=[
            ("equipo multifuncional", "grupo con capacidad de modificar producto, datos y comunicación"),
            ("ciclo de experimentación", "rutina de analizar, idear, priorizar, probar y aprender"),
            ("alcance de intervención", "conjunto de palancas que el equipo puede efectivamente modificar"),
            ("aprendizaje acumulativo", "conocimiento documentado que hace más eficientes los experimentos siguientes"),
        ],
        metodo=[
            "definir el alcance real de intervención del equipo",
            "establecer el ritmo del ciclo de experimentación",
            "documentar cada experimento y su aprendizaje",
            "medir la tasa de aprendizajes y no sólo de victorias",
            "revisar el alcance si el equipo no puede modificar lo que importa",
        ],
        senales=[
            ("experimentos ejecutados por ciclo", "experimentos completados con conclusión registrada, por equipo y por mes"),
            ("tasa de aprendizajes documentados", "experimentos con conclusión registrada, sobre experimentos ejecutados"),
            ("alcance efectivo", "palancas que el equipo puede modificar, sobre palancas identificadas como relevantes"),
        ],
        caso=(
            "El equipo de growth de Ruta Andina sólo puede modificar landings y correos. Los mayores puntos "
            "de fuga están en el onboarding del producto, fuera de su alcance."
        ),
        limite=(
            "Growth no reemplaza la estrategia: optimizar la ejecución de una propuesta equivocada acelera la "
            "llegada al techo, no lo levanta."
        ),
        libros=["ellis-brown", "ries-lean", "cagan", "croll-yoskovitz"],
        error=("Formar un equipo de growth sin acceso al producto",
               "Define el alcance de intervención antes de constituir el equipo; sin acceso al producto, el método no aplica."),
    ),
    dict(
        n="02",
        slug="north-star-metric",
        titulo="North Star Metric",
        tesis=(
            "Una métrica estrella es el indicador que mejor representa el valor entregado al cliente y que, "
            "al crecer, arrastra al negocio. Su elección es una decisión estratégica: enfoca al equipo y "
            "excluye otras lecturas. Debe cumplir tres condiciones: reflejar valor para el cliente, ser "
            "influenciable por el equipo y correlacionar con el ingreso a mediano plazo."
        ),
        conceptos=[
            ("métrica estrella", "indicador único que representa el valor entregado y guía las decisiones"),
            ("métrica de entrada", "componente que alimenta la métrica estrella y sobre el que se actúa"),
            ("correlación con ingreso", "relación observada entre la métrica y el resultado financiero"),
            ("efecto de enfoque", "concentración del esfuerzo que produce elegir una sola métrica"),
        ],
        metodo=[
            "identificar el momento en que el cliente obtiene valor",
            "proponer candidatas y verificar su correlación con ingreso",
            "descomponer la métrica en sus entradas",
            "declarar la elección y comunicarla",
            "revisar la elección cuando cambia el modelo de negocio",
        ],
        senales=[
            ("valor de la métrica estrella", "valor del indicador elegido en el periodo, sobre su valor en el periodo anterior comparable"),
            ("correlación con ingreso", "asociación observada entre la métrica y el ingreso, con desfase estimado"),
            ("alineación de iniciativas", "iniciativas cuyo objetivo es mover la métrica estrella, sobre iniciativas activas"),
        ],
        caso=(
            "Ruta Andina usa «cuentas registradas» como métrica principal. Las cuentas que nunca activan el "
            "módulo de pagos no producen ingreso ni permanecen."
        ),
        limite=(
            "Una sola métrica no describe un negocio completo. Debe acompañarse de guardarraíles que impidan "
            "optimizarla dañando margen, retención o reputación."
        ),
        libros=["ellis-brown", "croll-yoskovitz", "doerr", "kaplan-norton"],
        error=("Elegir una métrica de volumen sin relación con el valor",
               "Verifica la correlación con ingreso y retención antes de declarar la métrica estrella."),
    ),
    dict(
        n="03",
        slug="aarrr",
        titulo="AARRR",
        tesis=(
            "El marco de adquisición, activación, retención, referencia e ingreso ordena el recorrido en "
            "etapas medibles y facilita localizar el cuello de botella. Su riesgo es tratarlo como secuencia "
            "obligatoria y trabajar la adquisición primero por costumbre. La regla práctica es la contraria: "
            "en la mayoría de los negocios, trabajar retención y activación antes que adquisición produce "
            "más efecto por peso invertido."
        ),
        conceptos=[
            ("etapa del marco", "estado medible del recorrido del cliente dentro del modelo"),
            ("cuello de botella", "etapa que limita el resultado agregado del sistema"),
            ("orden de intervención", "secuencia de trabajo derivada del diagnóstico y no de la costumbre"),
            ("métrica por etapa", "indicador con definición operacional propio de cada estado"),
        ],
        metodo=[
            "instrumentar una métrica por etapa",
            "medir volumen y conversión en cada una",
            "identificar el cuello de botella con datos",
            "estimar el efecto de mejorar cada etapa",
            "intervenir donde el efecto por peso invertido es mayor",
        ],
        senales=[
            ("conversión por etapa del marco", "unidades que avanzan, sobre unidades que ingresaron a la etapa"),
            ("efecto simulado por etapa", "cambio estimado en el resultado al mejorar cada etapa un 10 %"),
            ("cobertura de instrumentación", "etapas con métrica instrumentada, sobre etapas del marco"),
        ],
        caso=(
            "La activación de Ruta Andina es 39 % y su conversión de visita a registro es 2,1 %. Duplicar la "
            "activación produce más clientes activos que duplicar el tráfico, a un costo menor."
        ),
        limite=(
            "El marco supone un recorrido lineal que no siempre existe. En negocios con compra por comité o "
            "ciclos largos, algunas etapas se superponen."
        ),
        libros=["croll-yoskovitz", "ellis-brown", "kaushik", "bush-plg"],
        error=("Trabajar adquisición por costumbre",
               "Simula el efecto de mejorar cada etapa y prioriza por resultado esperado sobre costo."),
    ),
    dict(
        n="04",
        slug="growth-loops",
        titulo="Growth loops",
        tesis=(
            "Un bucle de crecimiento es un sistema donde el resultado de un ciclo alimenta el siguiente: "
            "clientes que producen contenido, referencias o datos que atraen a más clientes. A diferencia del "
            "embudo, que se agota, el bucle compone. Su construcción exige identificar qué output del cliente "
            "puede convertirse en input de adquisición sin intervención manual."
        ),
        conceptos=[
            ("bucle de crecimiento", "sistema donde el resultado de un ciclo alimenta la entrada del siguiente"),
            ("output del usuario", "producto de la actividad del cliente que puede atraer a otros"),
            ("velocidad del bucle", "tiempo que tarda un ciclo completo en producir nuevos usuarios"),
            ("factor de amplificación", "número de nuevos usuarios que genera cada usuario existente por ciclo"),
        ],
        metodo=[
            "identificar qué produce el usuario al usar el producto",
            "evaluar si ese output puede atraer a otros",
            "diseñar el mecanismo que cierra el bucle",
            "medir velocidad y factor de amplificación",
            "decidir si conviene invertir en el bucle o en canales directos",
        ],
        senales=[
            ("factor de amplificación", "nuevos usuarios generados por usuario existente, por ciclo"),
            ("velocidad del bucle", "días entre la incorporación de un usuario y la del usuario que trae, mediana por cohorte"),
            ("proporción de adquisición por bucle", "usuarios originados por el bucle, sobre usuarios nuevos totales"),
        ],
        caso=(
            "Cada cliente de Ruta Andina envía recordatorios de cita a sus propios clientes finales. Ese "
            "mensaje podría incluir una referencia visible y convertirse en un bucle."
        ),
        limite=(
            "No todos los negocios admiten bucles: si el output del usuario no es visible para terceros, no "
            "hay mecanismo posible y forzarlo produce experiencias intrusivas."
        ),
        libros=["ellis-brown", "bush-plg", "croll-yoskovitz", "weinberg-traction"],
        error=("Forzar un bucle donde el producto no lo permite",
               "Verifica que exista un output visible para terceros antes de invertir en el mecanismo."),
    ),
    dict(
        n="05",
        slug="activation",
        titulo="Activación",
        tesis=(
            "La activación es el momento en que el usuario experimenta el valor del producto por primera "
            "vez. Identificarla con precisión es una tarea analítica: consiste en encontrar qué acción, "
            "realizada en qué plazo, predice la permanencia. Una vez identificada, todo el diseño inicial "
            "debe orientarse a que ocurra lo antes posible."
        ),
        conceptos=[
            ("evento de activación", "acción cuya realización predice la permanencia del usuario"),
            ("ventana de activación", "plazo dentro del cual esa acción debe ocurrir para predecir retención"),
            ("análisis predictivo de activación", "método que identifica el evento a partir de datos históricos"),
            ("tasa de activación", "usuarios que realizan el evento en la ventana, sobre usuarios incorporados"),
        ],
        metodo=[
            "analizar qué acciones distinguen a quienes permanecen",
            "definir el evento y la ventana de activación",
            "medir la tasa actual por segmento y origen",
            "rediseñar el inicio para producir ese evento antes",
            "verificar el efecto sobre la retención de las cohortes nuevas",
        ],
        senales=[
            ("tasa de activación", "usuarios activados en la ventana, sobre usuarios incorporados"),
            ("retención por activación", "retención a 90 días de usuarios activados frente a no activados"),
            ("tiempo hasta la activación", "días entre el registro y el evento de activación, mediana"),
        ],
        caso=(
            "El análisis de Ruta Andina muestra que quienes cargan más de 20 clientes en la primera semana "
            "retienen 3,4 veces más. Sólo el 22 % lo hace."
        ),
        limite=(
            "La correlación entre el evento y la retención no prueba causalidad: puede que quienes ya estaban "
            "comprometidos hagan ambas cosas. Verificarlo requiere un experimento."
        ),
        libros=["ellis-brown", "hulick", "croll-yoskovitz", "kohavi"],
        error=("Confundir correlación con causalidad en el evento de activación",
               "Diseña un experimento que induzca el evento y verifica si la retención mejora."),
    ),
    dict(
        n="06",
        slug="retention-first-growth",
        titulo="Crecimiento centrado en retención",
        tesis=(
            "Invertir en adquisición con retención deficiente es llenar un estanque con fuga. El orden "
            "correcto es diagnóstico: si la curva de retención no se estabiliza, el problema es de encaje o "
            "de producto y ningún canal lo compensa. Esta es la decisión más contraintuitiva de growth, "
            "porque la presión organizacional siempre empuja hacia más leads."
        ),
        conceptos=[
            ("curva estabilizada", "retención que deja de caer y se aplana en un nivel positivo"),
            ("orden de inversión", "secuencia que prioriza retención antes que adquisición"),
            ("costo de la fuga", "ingreso perdido por invertir en adquisición sobre una base que no retiene"),
            ("umbral de escalamiento", "nivel de retención a partir del cual conviene escalar adquisición"),
        ],
        metodo=[
            "verificar si la curva de retención se estabiliza",
            "definir el umbral que autoriza escalar adquisición",
            "calcular el costo de la fuga actual",
            "priorizar intervenciones de retención",
            "escalar adquisición sólo tras superar el umbral",
        ],
        senales=[
            ("nivel de estabilización de la curva", "porcentaje en que la retención se aplana, por cohorte"),
            ("costo de la fuga", "ingreso perdido estimado por bajas de clientes adquiridos en el periodo"),
            ("relación inversión retención-adquisición", "presupuesto asignado a cada frente, por trimestre"),
        ],
        caso=(
            "Ruta Andina planea duplicar su inversión publicitaria. Sus cohortes pierden el 38 % de los "
            "clientes antes del día 90 y la curva no se ha estabilizado en ninguna cohorte."
        ),
        limite=(
            "Detener toda adquisición mientras se arregla la retención puede matar la caja. La decisión "
            "realista es sostener y no escalar hasta superar el umbral."
        ),
        libros=["ellis-brown", "fader", "croll-yoskovitz", "mehta"],
        error=("Escalar adquisición con retención no estabilizada",
               "Define el umbral de retención que autoriza escalar y respétalo como regla de inversión."),
    ),
    dict(
        n="07",
        slug="referral-loops",
        titulo="Bucles de referencia",
        tesis=(
            "Un bucle de referencia convierte a los clientes satisfechos en canal de adquisición. Para "
            "funcionar necesita tres condiciones: valor entregado, momento adecuado y facilidad de "
            "compartir. Los programas que fallan suelen incumplir la primera: incentivan a recomendar un "
            "producto que el cliente todavía no valora, produciendo referencias de baja calidad."
        ),
        conceptos=[
            ("condición de valor previo", "requisito de que el cliente haya obtenido resultado antes de referir"),
            ("mecanismo de compartir", "función que permite referir con esfuerzo mínimo"),
            ("incentivo bilateral", "beneficio para quien refiere y para quien es referido"),
            ("calidad del referido", "grado en que el referido corresponde al perfil de cliente ideal"),
        ],
        metodo=[
            "verificar el resultado del cliente antes de invitarlo a referir",
            "elegir el momento posterior a un logro reconocido",
            "diseñar el mecanismo de compartir con esfuerzo mínimo",
            "definir incentivo y declararlo con transparencia",
            "medir volumen y calidad de los referidos",
        ],
        senales=[
            ("tasa de participación", "clientes que refieren al menos una vez, sobre clientes elegibles"),
            ("calidad del referido", "referidos que cumplen el perfil objetivo, sobre referidos recibidos"),
            ("retención de clientes referidos", "retención a 12 meses de referidos frente a clientes de otros orígenes"),
        ],
        caso=(
            "Ruta Andina ofrece un mes gratis por referir. El 40 % de los referidos no pertenece al perfil "
            "objetivo y su retención es la mitad del promedio."
        ),
        limite=(
            "Los incentivos monetarios pueden atraer referencias de baja calidad. Un incentivo vinculado a la "
            "permanencia del referido corrige parcialmente ese sesgo."
        ),
        libros=["reichheld", "ellis-brown", "cialdini", "godin"],
        error=("Invitar a referir antes de que el cliente obtenga valor",
               "Condiciona la invitación al resultado acreditado y mide la calidad del referido."),
    ),
    dict(
        n="08",
        slug="viralidad",
        titulo="Viralidad",
        tesis=(
            "La viralidad ocurre cuando cada usuario trae en promedio más de uno nuevo dentro de un ciclo, "
            "produciendo crecimiento exponencial. Es rara y suele ser mal entendida: la mayoría de los "
            "productos tiene un coeficiente muy por debajo de uno, lo que no impide que la viralidad parcial "
            "reduzca el costo de adquisición. El error frecuente es diseñar mecanismos virales en productos "
            "donde el uso no es visible para terceros."
        ),
        conceptos=[
            ("coeficiente viral", "número promedio de usuarios nuevos que genera cada usuario existente"),
            ("tiempo de ciclo viral", "días entre la incorporación de un usuario y la de quienes trae"),
            ("viralidad parcial", "contribución del mecanismo que reduce el costo de adquisición sin ser exponencial"),
            ("visibilidad del uso", "grado en que terceros observan que alguien usa el producto"),
        ],
        metodo=[
            "medir el coeficiente y el tiempo de ciclo actuales",
            "evaluar la visibilidad del uso para terceros",
            "diseñar el mecanismo sólo si esa visibilidad existe",
            "medir el efecto sobre el costo de adquisición",
            "evitar mecanismos que degraden la experiencia",
        ],
        senales=[
            ("coeficiente viral", "usuarios nuevos generados por usuario existente, por ciclo"),
            ("tiempo de ciclo", "días entre la incorporación y la del usuario que trae"),
            ("efecto en costo de adquisición", "variación del costo por cliente ganado atribuible al mecanismo"),
        ],
        caso=(
            "Los recordatorios que Ruta Andina envía a los clientes finales de cada taller son vistos por "
            "miles de personas al mes: allí existe visibilidad real, a diferencia del panel de administración."
        ),
        limite=(
            "Los mecanismos virales intrusivos —acceso a contactos, envíos automáticos— dañan la reputación y "
            "pueden infringir normas de datos personales."
        ),
        libros=["ellis-brown", "bush-plg", "weinberg-traction", "godin"],
        error=("Diseñar mecanismos virales sin visibilidad del uso",
               "Verifica que terceros puedan observar el uso antes de invertir en el mecanismo."),
    ),
    dict(
        n="09",
        slug="experiment-backlog",
        titulo="Backlog de experimentos",
        tesis=(
            "Un backlog de experimentos convierte las ideas dispersas en una cola priorizada con hipótesis "
            "explícitas. Su valor está en la disciplina de formulación: cada entrada debe declarar qué se "
            "cree, por qué, qué se medirá y qué resultado la refutaría. Un backlog de ideas sin hipótesis es "
            "una lista de deseos que se ejecuta por simpatía."
        ),
        conceptos=[
            ("entrada del backlog", "experimento formulado con hipótesis, métrica y criterio de decisión"),
            ("fundamento de la hipótesis", "evidencia o razonamiento que sostiene la expectativa"),
            ("esfuerzo estimado", "recursos necesarios para ejecutar el experimento"),
            ("aprendizaje esperado", "valor de la información que producirá el resultado, gane o pierda"),
        ],
        metodo=[
            "formular cada idea como hipótesis con fundamento",
            "estimar esfuerzo y aprendizaje esperado",
            "priorizar con un criterio explícito",
            "ejecutar en orden y documentar el resultado",
            "revisar el backlog con los aprendizajes acumulados",
        ],
        senales=[
            ("entradas con hipótesis completa", "entradas con hipótesis, métrica y criterio, sobre entradas del backlog"),
            ("tasa de ejecución", "experimentos ejecutados, sobre experimentos priorizados en el periodo"),
            ("aprendizajes por experimento", "conclusiones documentadas, sobre experimentos ejecutados"),
        ],
        caso=(
            "El backlog de Ruta Andina tiene 62 ideas sin hipótesis. Se ejecuta lo que propone quien tiene "
            "más influencia en la reunión."
        ),
        limite=(
            "Un backlog muy formalizado puede frenar pruebas baratas y rápidas. El nivel de formalidad debe "
            "ser proporcional al costo del experimento."
        ),
        libros=["ellis-brown", "kohavi", "ries-lean", "cagan"],
        error=("Mantener ideas sin hipótesis en el backlog",
               "Exige hipótesis, métrica y criterio de refutación para cada entrada priorizada."),
    ),
    dict(
        n="10",
        slug="ice-rice-y-priorizacion",
        titulo="ICE, RICE y priorización",
        tesis=(
            "Los marcos de priorización convierten juicios en números comparables: impacto, confianza, "
            "esfuerzo y alcance. Su valor no está en la precisión —los puntajes son estimaciones— sino en "
            "hacer explícito el razonamiento y permitir la discusión. Su riesgo es la falsa objetividad: un "
            "número inventado con dos decimales sigue siendo una opinión."
        ),
        conceptos=[
            ("impacto estimado", "efecto esperado sobre la métrica objetivo si la hipótesis es correcta"),
            ("confianza", "grado de evidencia que respalda la expectativa de impacto"),
            ("esfuerzo", "recursos necesarios para ejecutar, expresados en una unidad comparable"),
            ("falsa objetividad", "apariencia de rigor que produce un puntaje basado en estimaciones subjetivas"),
        ],
        metodo=[
            "definir la escala de cada componente con criterios",
            "puntuar con participación de más de una persona",
            "revisar los casos donde el puntaje contradice la intuición",
            "ejecutar en orden y registrar el resultado",
            "calibrar las estimaciones con los resultados observados",
        ],
        senales=[
            ("calibración de estimaciones", "diferencia entre impacto estimado y observado, por experimento"),
            ("dispersión entre evaluadores", "diferencia de puntajes asignados por distintas personas al mismo ítem"),
            ("orden de ejecución respetado", "experimentos ejecutados según prioridad, sobre experimentos ejecutados"),
        ],
        caso=(
            "El equipo de Ruta Andina puntúa el impacto con una escala sin criterios. La misma iniciativa "
            "recibe 8 y 3 de dos personas distintas."
        ),
        limite=(
            "Ningún marco reemplaza el juicio estratégico. Iniciativas de alto valor y alto esfuerzo pueden "
            "quedar postergadas indefinidamente por un puntaje."
        ),
        libros=["ellis-brown", "hubbard", "cagan", "provost"],
        error=("Puntuar sin criterios definidos por escala",
               "Define qué significa cada valor de la escala y calibra las estimaciones con resultados reales."),
    ),
    dict(
        n="11",
        slug="experiment-design",
        titulo="Diseño de experimentos",
        tesis=(
            "Un experimento válido requiere hipótesis previa, asignación comparable, tamaño suficiente, "
            "duración que cubra el ciclo y métricas guardarraíl. Kohavi documenta las trampas más comunes: "
            "detención temprana, comparaciones múltiples sin corrección y contaminación entre grupos. Un "
            "experimento mal diseñado no es neutro: produce conclusiones falsas con apariencia de rigor."
        ),
        conceptos=[
            ("asignación comparable", "distribución de sujetos que hace equivalentes a los grupos"),
            ("tamaño mínimo detectable", "efecto más pequeño que el experimento puede identificar con la muestra"),
            ("métrica guardarraíl", "indicador que no debe deteriorarse aunque mejore la métrica principal"),
            ("contaminación", "situación en que el tratamiento afecta también al grupo de control"),
        ],
        metodo=[
            "formular la hipótesis y las métricas antes de iniciar",
            "calcular tamaño y duración necesarios",
            "verificar la comparabilidad de los grupos",
            "ejecutar sin detener anticipadamente",
            "analizar con el criterio previo y documentar",
        ],
        senales=[
            ("potencia del experimento", "probabilidad de detectar el efecto mínimo relevante con la muestra disponible, calculada antes de iniciar"),
            ("experimentos detenidos anticipadamente", "pruebas interrumpidas antes del plazo, sobre pruebas ejecutadas"),
            ("resultados replicados", "resultados confirmados al repetir la medición, sobre resultados positivos"),
        ],
        caso=(
            "Ruta Andina declaró ganadora una variante tras cuatro días con 120 usuarios por grupo. El efecto "
            "desapareció al mes siguiente."
        ),
        limite=(
            "En volúmenes bajos, la experimentación rigurosa es inviable. La alternativa honesta es decidir "
            "con investigación cualitativa y declarar la incertidumbre."
        ),
        libros=["kohavi", "provost", "laja", "wheeler-dv"],
        error=("Detener el experimento al ver un resultado favorable",
               "Fija duración y tamaño antes de iniciar y analiza sólo al finalizar el plazo definido."),
    ),
    dict(
        n="12",
        slug="growth-engineering",
        titulo="Growth engineering",
        tesis=(
            "Growth engineering es la capacidad técnica que permite experimentar rápido: instrumentación de "
            "eventos, infraestructura de asignación, banderas de funcionalidad y tableros de resultados. Sin "
            "ella, cada experimento requiere un proyecto de desarrollo y el ritmo de aprendizaje colapsa. "
            "Invertir en esta capacidad tiene retorno indirecto pero decisivo."
        ),
        conceptos=[
            ("instrumentación", "registro sistemático de eventos que permite medir sin desarrollo adicional"),
            ("bandera de funcionalidad", "mecanismo que permite activar o desactivar una variante sin desplegar código"),
            ("infraestructura de experimentos", "conjunto técnico que permite asignar, medir y analizar pruebas"),
            ("velocidad de aprendizaje", "número de experimentos válidos que el equipo puede ejecutar por periodo"),
        ],
        metodo=[
            "evaluar el costo actual de ejecutar un experimento",
            "instrumentar los eventos críticos del recorrido",
            "habilitar asignación y banderas de funcionalidad",
            "estandarizar el análisis de resultados",
            "medir la velocidad de aprendizaje antes y después",
        ],
        senales=[
            ("tiempo para lanzar un experimento", "días entre la aprobación y el inicio de la prueba"),
            ("experimentos por trimestre", "pruebas válidas ejecutadas, por trimestre"),
            ("cobertura de instrumentación", "eventos críticos instrumentados, sobre eventos identificados"),
        ],
        caso=(
            "Cada experimento en Ruta Andina requiere tres semanas de desarrollo. El equipo ejecuta dos "
            "pruebas por trimestre y ninguna con grupo de control."
        ),
        limite=(
            "La infraestructura tiene costo de construcción y de mantenimiento. En equipos pequeños puede "
            "convenir usar herramientas externas antes que construir."
        ),
        libros=["kohavi", "ellis-brown", "cagan", "provost"],
        error=("Experimentar sin instrumentación ni control",
               "Invierte primero en instrumentar los eventos críticos y en poder asignar grupos comparables."),
    ),
    dict(
        n="13",
        slug="product-led-growth",
        titulo="Product-led growth",
        tesis=(
            "En el crecimiento liderado por producto, el propio producto adquiere, activa y expande: prueba "
            "gratuita o plan libre, valor perceptible sin intervención comercial y expansión por uso. No "
            "aplica a todos los negocios: requiere un producto que pueda usarse sin implementación asistida y "
            "un valor que se perciba rápido. Adoptarlo sin esas condiciones produce una base grande que no "
            "convierte."
        ),
        conceptos=[
            ("autoservicio", "capacidad del cliente de contratar y usar sin intervención comercial"),
            ("valor perceptible sin ayuda", "beneficio que el usuario obtiene por su cuenta en poco tiempo"),
            ("expansión por uso", "aumento de ingreso que ocurre naturalmente al crecer el uso"),
            ("condición de aplicabilidad", "conjunto de requisitos que hacen viable el modelo"),
        ],
        metodo=[
            "verificar si el producto puede usarse sin asistencia",
            "medir el tiempo hasta el valor sin intervención",
            "definir el gatillo de conversión y de expansión",
            "instrumentar el recorrido completo",
            "evaluar la economía del modelo antes de escalarlo",
        ],
        senales=[
            ("tasa de conversión autoservicio", "cuentas que pagan sin intervención comercial, sobre cuentas registradas"),
            ("tiempo hasta el valor sin asistencia", "días hasta el primer resultado en cuentas autoservicio, mediana"),
            ("expansión por uso", "aumento de ingreso por crecimiento de uso, sobre ingreso de la cohorte"),
        ],
        caso=(
            "Ruta Andina quiere lanzar un plan self-service, pero su implementación exige migrar datos "
            "históricos que hoy hace una persona del equipo en cada cuenta."
        ),
        limite=(
            "El modelo reduce costo comercial y aumenta costo de producto y soporte. La economía debe "
            "evaluarse completa antes de decidir la transición."
        ),
        libros=["bush-plg", "ellis-brown", "cagan", "croll-yoskovitz"],
        error=("Adoptar el modelo sin verificar el autoservicio real",
               "Comprueba que un cliente pueda obtener valor sin intervención antes de lanzar el plan."),
    ),
    dict(
        n="14",
        slug="growth-model-completo",
        titulo="Growth model completo",
        tesis=(
            "Esta clase integra la parte en un modelo de crecimiento: métrica estrella con sus entradas, "
            "bucles identificados, diagnóstico por etapa, backlog priorizado, infraestructura de "
            "experimentación y aprendizajes documentados. La prueba de calidad es proyectiva: el modelo debe "
            "permitir estimar el efecto de mover cada palanca y decidir dónde invertir el próximo trimestre."
        ),
        conceptos=[
            ("modelo de crecimiento", "representación cuantitativa de las palancas y su efecto en el resultado"),
            ("palanca", "variable que el equipo puede modificar y que afecta la métrica estrella"),
            ("sensibilidad del modelo", "efecto en el resultado de variar cada palanca"),
            ("registro de aprendizajes", "documentación acumulada de experimentos y sus conclusiones"),
        ],
        metodo=[
            "construir el modelo con las palancas y sus relaciones",
            "calibrar con datos históricos",
            "ejecutar el análisis de sensibilidad",
            "priorizar el backlog con base en el modelo",
            "actualizar el modelo con cada aprendizaje",
        ],
        senales=[
            ("precisión del modelo", "diferencia entre el resultado proyectado y el observado, por trimestre"),
            ("palancas con efecto verificado", "palancas cuyo efecto fue medido experimentalmente, sobre palancas del modelo"),
            ("aprendizajes acumulados", "conclusiones documentadas con evidencia, sobre experimentos ejecutados en el trimestre"),
        ],
        caso=(
            "Ruta Andina debe presentar su plan de crecimiento para el próximo año. Hoy no puede estimar qué "
            "produciría mejorar la activación frente a duplicar la inversión publicitaria."
        ),
        limite=(
            "Un modelo con supuestos no verificados produce proyecciones falsas. Su valor depende de cuántas "
            "relaciones fueron medidas y no supuestas."
        ),
        libros=["ellis-brown", "croll-yoskovitz", "provost", "kohavi"],
        error=("Presentar un plan de crecimiento sin modelo cuantitativo",
               "Construye el modelo, declara qué relaciones fueron medidas y cuáles son supuestos."),
    ),
]
