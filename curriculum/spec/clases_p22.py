# -*- coding: utf-8 -*-
"""Parte 22 — Go-to-market, canales y expansión."""

CLASES = [
    dict(
        n="01",
        slug="que-es-una-estrategia-gtm",
        titulo="Qué es una estrategia go-to-market",
        tesis=(
            "Una estrategia de salida al mercado responde cinco preguntas encadenadas: a quién servimos, qué "
            "le ofrecemos, cómo lo alcanzamos, cómo lo convertimos y cómo lo retenemos. No es un plan de "
            "lanzamiento ni un calendario de campañas: es la elección del movimiento comercial completo y su "
            "economía. Su error más caro es la incoherencia entre valor del contrato y costo del movimiento "
            "elegido."
        ),
        conceptos=[
            ("movimiento comercial", "forma dominante en que la empresa adquiere clientes: autoservicio, venta interna, terreno o socios"),
            ("coherencia económica", "correspondencia entre el valor del contrato y el costo del movimiento"),
            ("segmento objetivo", "grupo específico al que se dirige el movimiento"),
            ("ciclo completo", "recorrido desde el descubrimiento hasta la renovación"),
        ],
        metodo=[
            "definir el segmento objetivo y su valor de contrato",
            "elegir el movimiento comercial coherente con ese valor",
            "calcular el costo del movimiento por cliente",
            "verificar la coherencia con la economía unitaria",
            "documentar la estrategia y sus supuestos",
        ],
        senales=[
            ("costo del movimiento por cliente", "gasto comercial del movimiento dividido por clientes ganados"),
            ("relación costo-valor de contrato", "costo de adquisición, sobre valor del primer año del contrato"),
            ("coherencia entre segmentos y movimientos", "segmentos atendidos con el movimiento correspondiente, sobre segmentos activos"),
        ],
        caso=(
            "Ruta Andina atiende con visitas en terreno a clientes de CLP 39.000 mensuales. El costo del "
            "movimiento supera el valor del primer año del contrato."
        ),
        limite=(
            "Una estrategia coherente puede fallar por ejecución. El diseño no garantiza el resultado: sólo "
            "evita el error de partida."
        ),
        libros=["moore", "rumelt", "bush-plg", "ross"],
        error=("Usar un movimiento caro para tickets bajos",
               "Compara el costo del movimiento con el valor del contrato antes de definir la estrategia por segmento."),
    ),
    dict(
        n="02",
        slug="market-entry",
        titulo="Entrada a un mercado",
        tesis=(
            "Entrar a un mercado nuevo exige responder tres preguntas antes de invertir: existe demanda "
            "verificable, la empresa puede servirla con su capacidad actual y hay un camino de acceso "
            "económicamente viable. Saltarse la tercera es el error más común: se confirma que hay demanda y "
            "se descubre después que alcanzarla cuesta más de lo que deja."
        ),
        conceptos=[
            ("demanda verificable", "evidencia de que existen clientes dispuestos a pagar en ese mercado"),
            ("capacidad de servir", "aptitud actual para entregar el resultado en ese contexto"),
            ("camino de acceso", "canal viable para alcanzar a esos clientes con costo compatible"),
            ("costo de entrada", "inversión necesaria antes de obtener el primer ingreso relevante"),
        ],
        metodo=[
            "verificar la demanda con evidencia primaria",
            "evaluar la capacidad actual de servir ese mercado",
            "identificar y costear el camino de acceso",
            "estimar el costo de entrada y el tiempo hasta el ingreso",
            "definir el criterio de abandono antes de invertir",
        ],
        senales=[
            ("evidencia de demanda", "señales verificables de disposición a pagar recogidas en el mercado objetivo"),
            ("costo estimado de acceso", "gasto necesario para generar una oportunidad calificada en ese mercado"),
            ("tiempo hasta el primer ingreso", "meses estimados entre el inicio de la inversión y el primer ingreso relevante"),
        ],
        caso=(
            "Ruta Andina quiere entrar a Perú. Confirmó que existen talleres con el mismo problema, pero no "
            "tiene canal, ni referencias locales, ni soporte en horario compatible."
        ),
        limite=(
            "La evidencia de demanda en un mercado no se traslada a otro: cambian competidores, normas, "
            "hábitos de pago y expectativas de servicio."
        ),
        libros=["moore", "porter", "rumelt", "blank"],
        error=("Verificar demanda sin costear el acceso",
               "Estima el costo de generar una oportunidad calificada en ese mercado antes de comprometer inversión."),
    ),
    dict(
        n="03",
        slug="beachhead-market",
        titulo="Beachhead market",
        tesis=(
            "El mercado cabeza de playa es el segmento inicial elegido no por su tamaño sino por su "
            "capacidad de producir una posición dominante rápida y de generar referencias hacia segmentos "
            "vecinos. Moore describió el error opuesto: dispersar recursos en muchos segmentos y no lograr "
            "masa crítica en ninguno, quedando sin referencias que sostengan la expansión."
        ),
        conceptos=[
            ("cabeza de playa", "segmento inicial elegido por su capacidad de generar dominancia y referencia"),
            ("masa crítica", "nivel de presencia que hace que la marca sea conocida dentro del segmento"),
            ("circulación de referencias", "grado en que los actores del segmento se comunican entre sí"),
            ("adyacencia", "segmento vecino accesible desde la posición conquistada"),
        ],
        metodo=[
            "evaluar segmentos por dominancia alcanzable y no por tamaño",
            "verificar la circulación interna de referencias",
            "concentrar recursos hasta alcanzar masa crítica",
            "medir participación dentro del segmento",
            "definir la condición que autoriza expandir a la adyacencia",
        ],
        senales=[
            ("participación en el segmento", "clientes atendidos, sobre universo estimado del segmento"),
            ("referencias internas", "oportunidades originadas por clientes del mismo segmento, sobre oportunidades del segmento"),
            ("concentración de recursos", "gasto comercial asignado al segmento, sobre gasto comercial total"),
        ],
        caso=(
            "Ruta Andina tiene 34 % de los talleres de Valparaíso y presencia marginal en otros cinco rubros. "
            "El debate es si profundizar o abrir un sexto frente."
        ),
        limite=(
            "Un segmento demasiado pequeño puede no sostener la operación mientras se construye la posición. "
            "El tamaño mínimo importa aunque no sea el criterio principal."
        ),
        libros=["moore", "rumelt", "godin", "porter-hbr"],
        error=("Elegir el segmento inicial por tamaño",
               "Prioriza dominancia alcanzable y circulación de referencias sobre tamaño absoluto."),
    ),
    dict(
        n="04",
        slug="sales-led-growth",
        titulo="Crecimiento liderado por ventas",
        tesis=(
            "En el modelo liderado por ventas, el equipo comercial origina, educa y cierra. Es apropiado "
            "cuando el ticket es alto, la decisión es compleja y el cliente necesita ayuda para definir su "
            "problema. Su economía exige tickets que sostengan el costo del equipo y su escalamiento depende "
            "de contratar, formar y gestionar personas, con toda la latencia que eso implica."
        ),
        conceptos=[
            ("costo del equipo comercial", "gasto total de remuneraciones, herramientas y gestión por vendedor"),
            ("productividad por vendedor", "ingreso nuevo generado por persona en un periodo"),
            ("latencia de escalamiento", "tiempo entre la decisión de contratar y la productividad plena"),
            ("umbral de ticket", "valor de contrato mínimo que hace viable el modelo"),
        ],
        metodo=[
            "calcular el costo total por vendedor",
            "medir la productividad actual por persona",
            "determinar el umbral de ticket viable",
            "estimar la latencia de escalamiento",
            "decidir el crecimiento del equipo con esos datos",
        ],
        senales=[
            ("productividad por vendedor", "ingreso nuevo generado, por vendedor y por año"),
            ("relación productividad-costo", "ingreso generado, sobre costo total del vendedor"),
            ("duración de la rampa", "meses hasta alcanzar la productividad objetivo, por incorporación"),
        ],
        caso=(
            "Cada vendedor de Ruta Andina cuesta CLP 24 millones anuales y genera CLP 41 millones de ingreso "
            "nuevo. La rampa es de siete meses y nadie la consideró en el plan de contratación."
        ),
        limite=(
            "El modelo escala de forma lineal con personas: duplicar ingreso suele exigir casi duplicar el "
            "equipo, con la latencia y el riesgo de rotación que eso implica."
        ),
        libros=["ross", "roberge", "zoltners", "moore"],
        error=("Planificar contrataciones sin considerar la rampa",
               "Incorpora la duración de la rampa y la rotación esperada al proyectar capacidad."),
    ),
    dict(
        n="05",
        slug="product-led-growth",
        titulo="Crecimiento liderado por producto",
        tesis=(
            "En el modelo liderado por producto, el propio producto adquiere, activa y expande sin "
            "intervención comercial. Su economía es atractiva: costo marginal bajo y escalamiento rápido. "
            "Sus condiciones son estrictas: valor perceptible sin ayuda, contratación autónoma y un producto "
            "que soporte el uso sin implementación asistida. Sin esas condiciones, el modelo produce una base "
            "grande que no convierte."
        ),
        conceptos=[
            ("adopción autónoma", "capacidad del usuario de contratar y obtener valor sin asistencia"),
            ("expansión por uso", "aumento de ingreso derivado del crecimiento natural del uso"),
            ("costo de servir en autoservicio", "gasto de producto y soporte por usuario del modelo"),
            ("condición de viabilidad", "requisitos que hacen posible el modelo en un producto concreto"),
        ],
        metodo=[
            "verificar que el producto permite adopción autónoma",
            "medir el tiempo hasta el valor sin asistencia",
            "definir los gatillos de conversión y de expansión",
            "calcular el costo de servir en autoservicio",
            "evaluar la economía completa antes de escalar",
        ],
        senales=[
            ("conversión autoservicio", "cuentas que pagan sin intervención, sobre cuentas registradas"),
            ("costo de servir por usuario", "gasto de soporte y producto, dividido por usuarios activos"),
            ("expansión por uso", "aumento de ingreso por crecimiento de uso, sobre ingreso de la cohorte"),
        ],
        caso=(
            "El plan self-service de Ruta Andina exige migrar datos históricos, tarea que hoy realiza una "
            "persona en cada cuenta. El modelo no es viable sin resolver eso."
        ),
        limite=(
            "El modelo traslada costo de ventas a producto y soporte. La economía total puede no mejorar si "
            "el producto exige inversión constante para sostener la autonomía."
        ),
        libros=["bush-plg", "cagan", "ellis-brown", "croll-yoskovitz"],
        error=("Lanzar autoservicio sin resolver la implementación asistida",
               "Verifica que el cliente pueda obtener valor sin intervención antes de habilitar el plan."),
    ),
    dict(
        n="06",
        slug="partner-led-growth",
        titulo="Crecimiento liderado por socios",
        tesis=(
            "Los socios aportan acceso, credibilidad e implementación a cambio de margen y de control. "
            "Funcionan cuando existe un incentivo económico real para el socio y cuando la empresa puede "
            "sostener su habilitación. El error frecuente es firmar muchos acuerdos y no activar ninguno: un "
            "socio sin incentivo, sin formación y sin apoyo comercial no vende."
        ),
        conceptos=[
            ("incentivo del socio", "beneficio económico que justifica su esfuerzo comercial"),
            ("habilitación", "formación, materiales y apoyo que permiten al socio vender y entregar"),
            ("socio activo", "aliado que generó negocio en el periodo, frente al que sólo firmó acuerdo"),
            ("conflicto de canal", "competencia entre el equipo propio y el socio por la misma cuenta"),
        ],
        metodo=[
            "definir el incentivo económico del socio",
            "diseñar el programa de habilitación",
            "establecer reglas de conflicto de canal",
            "medir socios activos y no acuerdos firmados",
            "concentrar el apoyo en los socios que producen",
        ],
        senales=[
            ("proporción de socios activos", "socios con negocio en el periodo, sobre socios con acuerdo firmado"),
            ("ingreso por socio activo", "ingreso generado, por socio con actividad"),
            ("conflictos de canal registrados", "disputas por cuenta entre equipo propio y socios, por trimestre"),
        ],
        caso=(
            "Ruta Andina firmó 22 acuerdos con estudios contables. Tres han generado negocio y ninguno "
            "recibió formación ni materiales."
        ),
        limite=(
            "El canal indirecto reduce el margen unitario y aleja la relación con el cliente final. Su "
            "conveniencia depende del costo de acceso directo a ese segmento."
        ),
        libros=["moore", "weinberg-traction", "porter", "ross"],
        error=("Firmar acuerdos sin programa de habilitación",
               "Mide socios activos y concentra formación e incentivos en los que producen negocio."),
    ),
    dict(
        n="07",
        slug="canales-directos-e-indirectos",
        titulo="Canales directos e indirectos",
        tesis=(
            "La elección entre vender directo o a través de terceros determina margen, control de la "
            "experiencia y acceso a información del cliente. La mayoría de las empresas opera modelos "
            "mixtos, y ahí surge el problema principal: las reglas de conflicto. Sin reglas escritas sobre "
            "quién atiende qué cuenta, el equipo propio y el canal compiten y el cliente recibe dos ofertas "
            "distintas."
        ),
        conceptos=[
            ("canal directo", "venta realizada por el equipo propio con relación directa con el cliente"),
            ("canal indirecto", "venta realizada por un tercero que se queda con parte del margen"),
            ("regla de conflicto", "criterio escrito que asigna cuentas y evita competencia interna"),
            ("visibilidad del cliente final", "acceso a información y relación con quien usa el producto"),
        ],
        metodo=[
            "definir qué segmentos corresponden a cada canal",
            "escribir las reglas de conflicto y de registro de cuentas",
            "comparar margen y costo por canal",
            "medir la visibilidad del cliente final en cada uno",
            "revisar la asignación anualmente con datos",
        ],
        senales=[
            ("margen por canal", "margen de contribución, sobre ingreso, por canal"),
            ("conflictos registrados", "disputas de cuenta, sobre cuentas trabajadas por ambos canales"),
            ("visibilidad del cliente final", "clientes con datos de contacto y uso disponibles, sobre clientes del canal"),
        ],
        caso=(
            "Un estudio contable socio de Ruta Andina y un vendedor propio contactaron a la misma cadena la "
            "misma semana, con precios distintos."
        ),
        limite=(
            "Reglas de conflicto muy restrictivas pueden desincentivar al canal. El equilibrio requiere "
            "registro de cuentas y protección temporal, no exclusividad permanente."
        ),
        libros=["moore", "porter", "nagle", "weinberg-traction"],
        error=("Operar canales mixtos sin reglas de conflicto",
               "Escribe el criterio de asignación de cuentas y el mecanismo de registro antes de activar el canal indirecto."),
    ),
    dict(
        n="08",
        slug="channel-economics",
        titulo="Economía de canales",
        tesis=(
            "Cada canal tiene una estructura económica propia: costo de adquisición, margen retenido, costo "
            "de habilitación y velocidad de escalamiento. Compararlos exige normalizar: un canal con menor "
            "margen unitario puede ser superior si su costo de adquisición es mucho menor. La decisión debe "
            "considerar además el costo de sostener el canal, que suele omitirse."
        ),
        conceptos=[
            ("margen retenido", "porcentaje del ingreso que queda tras comisiones y descuentos del canal"),
            ("costo de habilitación", "gasto de formación, materiales y apoyo necesario para sostener el canal"),
            ("velocidad de escalamiento", "rapidez con que el canal puede aumentar su producción"),
            ("costo total del canal", "suma de adquisición, habilitación y sostenimiento"),
        ],
        metodo=[
            "calcular el costo total por canal, incluido el sostenimiento",
            "normalizar por unidad de resultado comparable",
            "estimar la velocidad de escalamiento de cada uno",
            "asignar inversión según retorno y velocidad",
            "revisar la comparación cada semestre",
        ],
        senales=[
            ("costo total por cliente ganado por canal", "costo completo del canal, dividido por clientes ganados"),
            ("margen retenido por canal", "ingreso neto de comisiones, sobre ingreso bruto del canal"),
            ("tiempo de escalamiento", "meses transcurridos hasta duplicar las oportunidades generadas por el canal, desde su activación"),
        ],
        caso=(
            "El canal de socios de Ruta Andina retiene 70 % del margen y exige un gerente de alianzas de "
            "dedicación completa que nunca se costeó en la comparación."
        ),
        limite=(
            "Los canales interactúan: un cliente puede descubrir la marca por uno y comprar por otro. "
            "Evaluarlos de forma aislada sobreestima o subestima su aporte."
        ),
        libros=["nagle", "moore", "croll-yoskovitz", "porter"],
        error=("Comparar canales sin incluir el costo de sostenimiento",
               "Incorpora habilitación, gestión y soporte al costo total antes de comparar canales."),
    ),
    dict(
        n="09",
        slug="lanzamientos",
        titulo="Lanzamientos",
        tesis=(
            "Un lanzamiento coordina producto, comunicación, ventas y soporte alrededor de una fecha. Su "
            "fracaso más común no es de comunicación sino de preparación interna: el equipo comercial no "
            "sabe vender lo nuevo, soporte no sabe responder y la documentación no existe. La regla práctica "
            "es que la preparación interna debe estar lista antes de la comunicación externa."
        ),
        conceptos=[
            ("preparación interna", "estado de listeza del equipo comercial, de soporte y de la documentación"),
            ("criterio de listeza", "condiciones verificables que deben cumplirse antes de lanzar"),
            ("nivel de lanzamiento", "escala de la comunicación según la importancia del cambio"),
            ("plan de reversión", "acción definida si el lanzamiento produce problemas graves"),
        ],
        metodo=[
            "definir el criterio de listeza interna",
            "preparar equipo, materiales y documentación",
            "verificar la listeza antes de comunicar",
            "escalar la comunicación según el nivel del cambio",
            "medir adopción y problemas en las primeras semanas",
        ],
        senales=[
            ("listeza interna verificada", "criterios cumplidos antes del lanzamiento, sobre criterios definidos"),
            ("adopción en las primeras semanas", "clientes que usan lo lanzado, sobre clientes elegibles"),
            ("consultas de soporte por el lanzamiento", "tickets relacionados, sobre tickets totales del periodo"),
        ],
        caso=(
            "Ruta Andina lanzó su módulo de pagos con campaña nacional. El equipo comercial recibió la "
            "capacitación dos semanas después y soporte no tenía documentación."
        ),
        limite=(
            "Esperar la listeza perfecta retrasa indefinidamente. El criterio debe distinguir lo "
            "indispensable de lo deseable."
        ),
        libros=["moore", "cagan", "roberge", "handley"],
        error=("Comunicar antes de preparar al equipo interno",
               "Verifica los criterios de listeza interna antes de activar cualquier comunicación externa."),
    ),
    dict(
        n="10",
        slug="expansion-geografica",
        titulo="Expansión geográfica",
        tesis=(
            "Expandir a otra región o país multiplica costos que suelen subestimarse: soporte en horario "
            "local, cumplimiento normativo, medios de pago, logística y construcción de referencias desde "
            "cero. La regla práctica es tratar cada geografía como un mercado nuevo que requiere validación "
            "propia, no como una extensión del actual."
        ),
        conceptos=[
            ("costo de presencia local", "gasto necesario para operar con credibilidad en la nueva geografía"),
            ("cumplimiento local", "requisitos legales, tributarios y de consumo propios del territorio"),
            ("referencias locales", "casos y clientes de la zona que dan credibilidad ante nuevos prospectos"),
            ("secuencia de expansión", "orden de apertura que aprovecha adyacencias y capacidades"),
        ],
        metodo=[
            "validar demanda y camino de acceso en la nueva geografía",
            "identificar los requisitos de cumplimiento local",
            "estimar el costo de presencia y el tiempo hasta el primer ingreso",
            "construir referencias locales antes de escalar",
            "definir el criterio de abandono con anticipación",
        ],
        senales=[
            ("costo de entrada por geografía", "inversión acumulada hasta el primer ingreso relevante"),
            ("tiempo hasta la primera referencia local", "meses hasta obtener un caso verificable en la zona"),
            ("cumplimiento normativo verificado", "requisitos identificados y cumplidos, sobre requisitos aplicables"),
        ],
        caso=(
            "Ruta Andina abrió Perú y Chile simultáneamente en su plan. El equipo es el mismo, el soporte "
            "opera en horario chileno y la facturación local no está resuelta."
        ),
        limite=(
            "La cercanía cultural o idiomática no reduce los requisitos de cumplimiento ni la necesidad de "
            "referencias locales. Son frentes independientes."
        ),
        libros=["moore", "porter", "rumelt", "blank"],
        error=("Tratar la nueva geografía como extensión del mercado actual",
               "Valida demanda, acceso y cumplimiento como si fuera un mercado nuevo, con criterio de abandono definido."),
    ),
    dict(
        n="11",
        slug="expansion-por-segmento",
        titulo="Expansión por segmento",
        tesis=(
            "Expandir hacia un segmento adyacente aprovecha producto y reputación existentes, pero exige "
            "verificar tres cosas: que el problema sea equivalente, que la operación pueda servirlo y que "
            "las referencias actuales tengan valor allí. Moore advirtió que la credibilidad no se transfiere "
            "automáticamente: un caso de éxito en talleres puede no significar nada para un centro médico."
        ),
        conceptos=[
            ("adyacencia real", "cercanía verificada del problema, del proceso de compra y del contexto"),
            ("transferencia de credibilidad", "grado en que las referencias actuales tienen valor en el nuevo segmento"),
            ("ajuste operativo", "cambios necesarios en producto y servicio para atender al nuevo segmento"),
            ("costo de la adaptación", "inversión requerida para servir al segmento con calidad"),
        ],
        metodo=[
            "verificar la equivalencia del problema con evidencia",
            "evaluar si las referencias actuales transfieren credibilidad",
            "estimar el ajuste operativo necesario y su costo",
            "probar con un piloto acotado antes de comprometer",
            "decidir con criterio previo definido",
        ],
        senales=[
            ("similitud del problema", "coincidencia de resultados deseados entre segmentos, verificada en entrevistas"),
            ("valor de las referencias", "reconocimiento de los casos actuales por prospectos del nuevo segmento"),
            ("costo de adaptación estimado", "inversión estimada de producto y operación, sobre margen esperado del segmento en su primer año"),
        ],
        caso=(
            "Ruta Andina quiere abrir centros médicos. El problema de agendamiento se parece, pero exige "
            "requisitos de registro clínico y confidencialidad que su producto no cumple."
        ),
        limite=(
            "La adyacencia percibida por la empresa rara vez coincide con la percibida por el mercado. La "
            "verificación debe hacerse con prospectos del segmento nuevo."
        ),
        libros=["moore", "christensen", "rumelt", "cagan"],
        error=("Suponer que las referencias actuales tienen valor en el nuevo segmento",
               "Verifica con prospectos del segmento nuevo si reconocen los casos actuales como pertinentes."),
    ),
    dict(
        n="12",
        slug="internacionalizacion",
        titulo="Internacionalización",
        tesis=(
            "Internacionalizar agrega complejidad en cuatro frentes simultáneos: legal y tributario, "
            "operativo, comercial y organizacional. Cada uno puede detener el proyecto por sí solo. La "
            "decisión estratégica previa es el modo de entrada —exportación de servicio, socio local, "
            "filial— y cada modo tiene un perfil de control, costo y riesgo distinto."
        ),
        conceptos=[
            ("modo de entrada", "forma jurídica y operativa de operar en el mercado extranjero"),
            ("complejidad regulatoria", "requisitos legales, tributarios y de datos aplicables en el destino"),
            ("costo de coordinación", "esfuerzo de gestionar operaciones en husos, idiomas y culturas distintas"),
            ("criterio de continuidad", "condición que determina si se sostiene o se abandona la operación"),
        ],
        metodo=[
            "evaluar los modos de entrada y su perfil de riesgo",
            "identificar los requisitos regulatorios del destino",
            "estimar el costo de coordinación real",
            "definir hitos y criterio de continuidad",
            "revisar la decisión en cada hito con datos",
        ],
        senales=[
            ("costo acumulado de la operación internacional", "inversión total realizada, comparada con el plan"),
            ("cumplimiento de hitos", "hitos alcanzados en plazo, sobre hitos definidos"),
            ("contribución de la operación", "margen generado por la operación internacional, sobre su costo"),
        ],
        caso=(
            "Ruta Andina debe elegir entre operar desde Chile con soporte remoto, buscar un socio local o "
            "constituir una filial. Cada opción cambia el costo, el control y el riesgo tributario."
        ),
        limite=(
            "La internacionalización suele consumir más atención de la dirección de lo previsto, y esa "
            "atención se resta del mercado principal."
        ),
        libros=["porter", "moore", "rumelt", "iso-31000"],
        error=("Internacionalizar sin definir hitos ni criterio de continuidad",
               "Establece hitos verificables y la condición que gatillaría el abandono antes de invertir."),
    ),
    dict(
        n="13",
        slug="gtm-metrics",
        titulo="Métricas de go-to-market",
        tesis=(
            "Evaluar una estrategia de salida al mercado exige métricas que capturen eficiencia y no sólo "
            "crecimiento: costo de adquisición por movimiento, periodo de recuperación, productividad por "
            "persona, contribución por canal y velocidad de escalamiento. Crecer perdiendo eficiencia no es "
            "un éxito comercial: es una apuesta financiera que alguien deberá pagar."
        ),
        conceptos=[
            ("eficiencia del crecimiento", "relación entre el ingreso incremental y el gasto necesario para producirlo"),
            ("productividad por movimiento", "resultado obtenido por unidad de capacidad en cada movimiento comercial"),
            ("contribución por canal", "margen que aporta cada canal después de sus costos"),
            ("velocidad de escalamiento", "rapidez con que el movimiento puede aumentar su producción"),
        ],
        metodo=[
            "definir las métricas por movimiento y por canal",
            "medir eficiencia además de crecimiento",
            "comparar la eficiencia entre movimientos",
            "identificar dónde la eficiencia se deteriora al escalar",
            "ajustar la asignación según el resultado",
        ],
        senales=[
            ("eficiencia del crecimiento", "ingreso incremental del periodo, sobre gasto comercial incremental"),
            ("periodo de recuperación por movimiento", "meses hasta recuperar el costo de adquisición, por movimiento"),
            ("deterioro de eficiencia al escalar", "variación de la eficiencia entre tramos crecientes de inversión"),
        ],
        caso=(
            "Ruta Andina creció 40 % en ingreso y su gasto comercial creció 78 %. El plan celebra el "
            "crecimiento y no menciona el deterioro de eficiencia."
        ),
        limite=(
            "En etapas tempranas puede ser racional sacrificar eficiencia para ganar posición. Lo que no es "
            "racional es hacerlo sin declararlo ni medirlo."
        ),
        libros=["croll-yoskovitz", "ross", "bush-plg", "kaplan-norton"],
        error=("Reportar crecimiento sin reportar eficiencia",
               "Presenta el ingreso incremental junto al gasto incremental que lo produjo."),
    ),
    dict(
        n="14",
        slug="plan-gtm-completo",
        titulo="Plan go-to-market completo",
        tesis=(
            "Esta clase integra la parte en un plan completo: segmento cabeza de playa, propuesta, "
            "movimiento comercial, canales con su economía, plan de lanzamiento, métricas y criterios de "
            "expansión. La prueba de calidad es la coherencia: cada elección debe ser compatible con las "
            "demás y con la capacidad real de la organización."
        ),
        conceptos=[
            ("coherencia del plan", "compatibilidad entre segmento, propuesta, movimiento, canal y capacidad"),
            ("secuencia de expansión", "orden definido de segmentos y geografías con sus condiciones"),
            ("criterio de expansión", "condición verificable que autoriza abrir el frente siguiente"),
            ("capacidad comprometida", "recursos que el plan requiere frente a los disponibles"),
        ],
        metodo=[
            "consolidar segmento, propuesta y movimiento",
            "definir canales con su economía",
            "establecer la secuencia y los criterios de expansión",
            "verificar la coherencia con la capacidad disponible",
            "definir las métricas de seguimiento y su periodicidad",
        ],
        senales=[
            ("coherencia auditada", "elementos del plan compatibles entre sí, sobre elementos revisados"),
            ("capacidad comprometida frente a disponible", "recursos requeridos por el plan, sobre recursos existentes"),
            ("cumplimiento de criterios de expansión", "frentes abiertos con criterio cumplido, sobre frentes abiertos"),
        ],
        caso=(
            "Ruta Andina quiere abrir Perú, lanzar autoservicio y activar un programa de socios en el mismo "
            "año, con el mismo equipo de seis personas."
        ),
        limite=(
            "Un plan coherente sobre supuestos falsos sigue siendo un plan equivocado. La coherencia interna "
            "no reemplaza la validación de los supuestos."
        ),
        libros=["moore", "rumelt", "ross", "weinberg-traction"],
        error=("Abrir varios frentes simultáneos con la misma capacidad",
               "Define la secuencia y el criterio que autoriza abrir cada frente siguiente."),
    ),
]
