# -*- coding: utf-8 -*-
"""Especificación de las rutas profesionales por rol.

Cada entrada describe un puesto real del mercado comercial: qué es, cómo es el
día a día, qué hay que saber, qué recorrido del programa lo prepara, qué
artefactos lo acreditan, cómo progresa y qué mitos lo rodean.

Las páginas de `rutas/` se generan desde aquí con `tools/build_rutas.py`.

Los rangos salariales son **orientativos**: varían por sector, tamaño de
empresa, industria y experiencia. Son referencia de mercado, no promesa.
"""

# Bloques salariales reutilizables, en formato de tabla de texto.
SALARIO_ENTRADA = """Región                      Entrada               Con 3–5 años
--------------------------  --------------------  ------------------------
Chile                       CLP 900k – 1,4M/mes   CLP 1,8M – 2,8M/mes
LATAM (regional)            USD 800 – 1.500/mes   USD 1.800 – 3.200/mes
España                      EUR 22k – 30k/año     EUR 33k – 45k/año
Remoto (USD)                USD 30k – 50k/año     USD 55k – 90k/año"""

SALARIO_MEDIO = """Región                      Con 3–5 años          Senior / liderazgo
--------------------------  --------------------  ------------------------
Chile                       CLP 1,8M – 2,8M/mes   CLP 3,2M – 5,0M/mes
LATAM (regional)            USD 1.800 – 3.200/mes USD 3.500 – 6.000/mes
España                      EUR 33k – 45k/año     EUR 48k – 70k/año
Remoto (USD)                USD 55k – 90k/año     USD 95k – 150k/año"""

SALARIO_DIRECCION = """Región                      Gerencia              Dirección (CMO/CRO)
--------------------------  --------------------  ------------------------
Chile                       CLP 4,0M – 6,5M/mes   CLP 7,0M – 12M/mes
LATAM (regional)            USD 4.000 – 7.000/mes USD 8.000 – 15.000/mes
España                      EUR 55k – 80k/año     EUR 90k – 150k/año
Remoto (USD)                USD 110k – 170k/año   USD 160k – 260k/año"""

ROLES = [
    # ------------------------------------------------------------------ 01
    dict(
        slug="analista-de-marketing",
        emoji="📊",
        titulo="Analista de marketing y de ingresos",
        familia="Analítica",
        resumen=(
            "El perfil que convierte datos comerciales dispersos en decisiones defendibles. No es quien hace "
            "gráficos: es quien determina si una cifra significa lo que el equipo cree que significa, y quien "
            "detiene una inversión de millones cuando la evidencia no la sostiene."
        ),
        nivel="Entrada a intermedio; es la puerta más accesible al área comercial para perfiles analíticos",
        foco="Definición de métricas, cohortes, atribución, economía unitaria y tableros",
        credencial="Google Analytics · SQL · una prueba de incrementalidad ejecutada",
        que_es=[
            "En casi toda empresa mediana hay tres versiones del mismo número. Marketing reporta 300 leads, "
            "ventas trabaja 60, finanzas ve un ingreso que no cuadra con ninguno de los dos. El analista es "
            "quien resuelve eso: no inventando un cuarto informe, sino estableciendo qué cuenta cada cifra, "
            "sobre qué base y en qué ventana.",
            "El trabajo tiene dos mitades. La primera es técnica: construir el dato, cruzarlo, calcular "
            "cohortes, estimar incrementalidad. La segunda es más difícil y es la que se paga: decir que no. "
            "Cuando el director pide el retorno de una campaña y la atribución de último clic le está "
            "asignando ventas que habrían ocurrido igual, el analista tiene que explicarlo sin volverse "
            "irrelevante.",
            "Es un rol con apalancamiento desproporcionado. Una definición de costo de adquisición que excluye "
            "sueldos comerciales puede sostener una decisión de escalar que destruye caja durante un año. "
            "Corregir esa definición cuesta una tarde y cambia el resultado del negocio.",
        ],
        dia=[
            "**Revisión de coherencia:** compruebas que los tableros del día cuadren entre sí. Si el ingreso "
            "del CRM y el de facturación difieren, eso se investiga antes que cualquier otra cosa.",
            "**Consultas del equipo:** alguien pregunta por qué cayó la conversión. Antes de responder, "
            "verificas si la variación está dentro del rango normal o si es señal real.",
            "**Análisis de cohortes:** sigues las cohortes de incorporación para ver si las nuevas retienen "
            "mejor que las anteriores. Es lo único que dice si el equipo está mejorando de verdad.",
            "**Diseño de medición:** una campaña nueva necesita instrumentación. Defines qué eventos se "
            "registran, con qué nombre y cómo se reconciliarán con el CRM.",
            "**Documentación de definiciones:** actualizas el diccionario de métricas. Cada término que no "
            "esté escrito volverá como discusión en tres semanas.",
        ],
        tecnico=[
            "**Definición operacional de métricas.** Numerador, denominador, ventana, fuente. Es la habilidad "
            "central: sin ella todo lo demás es aritmética sobre arena.",
            "**Análisis de cohortes.** Comparar en el mismo hito de antigüedad y no en la misma fecha "
            "calendario. Distinguir mejora real de efecto de mezcla.",
            "**Economía unitaria.** Costo de adquisición con alcance completo, margen de contribución, "
            "periodo de recuperación y valor de vida presentado como rango, no como cifra.",
            "**Atribución e incrementalidad.** Entender que ningún modelo de atribución establece causalidad y "
            "saber diseñar la prueba que sí lo hace.",
            "**Diseño de experimentos.** Tamaño de muestra, potencia, métricas guardarraíl y las trampas "
            "clásicas: detención temprana y comparaciones múltiples.",
            "**Variación común frente a especial.** Saber cuándo un número que bajó 12 % no significa nada.",
            "**SQL y hojas de cálculo.** La herramienta importa menos que la disciplina, pero hay que poder "
            "extraer el dato sin depender de nadie.",
        ],
        herramientas=(
            "Analítica web:    Google Analytics, herramientas de producto\n"
            "Datos:            SQL, hojas de cálculo, Python con pandas\n"
            "CRM y ventas:     HubSpot, Salesforce, Pipedrive\n"
            "Experimentación:  calculadoras de tamaño de muestra, pruebas A/B\n"
            "Visualización:    Looker Studio, Power BI, Metabase\n"
            "Documentación:    diccionario de métricas versionado"
        ),
        blandas=[
            "**Decir que no con evidencia.** El valor del rol aparece cuando contradice a alguien con más "
            "autoridad y lo sostiene con datos.",
            "**Traducir sin simplificar.** Explicar un intervalo de confianza a un comité sin convertirlo en "
            "una certeza falsa.",
            "**Honestidad epistémica.** Declarar qué no se puede concluir con los datos disponibles es más "
            "valioso que producir una conclusión cómoda.",
            "**Rigor documental.** Una cifra sin trazabilidad hasta su fuente no debería llegar a una "
            "presentación.",
        ],
        ruta=[
            ("01", "el motor de ingresos como sistema: sin este mapa, cada métrica flota sin contexto"),
            ("20", "**el núcleo del rol**: árbol de métricas, cohortes, atribución, incrementalidad y tableros"),
            ("16", "cómo se produce el dato comercial y por qué el pipeline miente cuando no hay criterios de etapa"),
            ("18", "retención, cohortes y el ingreso neto retenido, que es el indicador que más pesa"),
            ("12", "medición digital, plan de instrumentación y límites de cobertura por privacidad"),
            ("19", "diseño de experimentos y priorización con criterio previo"),
            ("14", "economía de medios: CPA, CAC, ROAS y por qué se confunden"),
        ],
        clases=[
            ("20", "01", "Árbol de métricas: la descomposición que conecta cada trabajo con el ingreso"),
            ("20", "02", "Conversión y embudos: por qué la misma etapa reporta 12 % o 34 %"),
            ("20", "03", "Costo de adquisición: el error de excluir sueldos comerciales"),
            ("20", "07", "Análisis de cohortes aplicado: distinguir mejora real de efecto de mezcla"),
            ("20", "09", "Incrementalidad: la única pregunta que importa para decidir presupuesto"),
            ("20", "10", "A/B testing: por qué la mayoría de las mejoras declaradas no se replican"),
            ("16", "07", "Forecast: método declarado, sesgo medido y corrección aplicada"),
            ("18", "09", "Cohortes: comparar en el mismo hito de antigüedad"),
        ],
        labs=["20", "16", "18"],
        artefactos=[
            "Árbol de métricas con responsable por rama y aritmética verificada",
            "Diccionario de métricas con ficha completa por indicador",
            "Análisis de cohortes con lectura de mejora entre cohortes sucesivas",
            "Caso analítico integral con recomendación de asignación y condición de revisión",
        ],
        credenciales=[
            "**Google Analytics** — certificación gratuita; acredita vocabulario, no criterio.",
            "**SQL** — no hay credencial que importe; lo que se evalúa es una consulta resuelta en entrevista.",
            "**Portafolio** — un análisis con datos reales, método declarado y límites reconocidos pesa más "
            "que cualquier certificado del área.",
        ],
        progresion=(
            "Analista → analista senior o especialista en un dominio (growth, retención, medios) → "
            "**RevOps** o **jefatura de analítica** → dirección de datos comerciales. Es también la mejor "
            "rampa hacia [growth](growth-manager.md) y [RevOps](revops.md), porque ambos exigen la misma base "
            "de rigor con el dato."
        ),
        salario=SALARIO_ENTRADA,
        mitos=[
            ("«Es hacer dashboards.»",
             "El tablero es la salida. El trabajo es decidir qué se mide, cómo y qué no se puede concluir."),
            ("«Necesito ser experto en estadística.»",
             "Necesitas entender variación, muestra e intervalo. La mayoría de los errores caros son de "
             "definición, no de método estadístico."),
            ("«Los datos hablan por sí solos.»",
             "Nunca lo hacen. La misma serie sostiene dos recomendaciones opuestas según cómo se segmente."),
            ("«Con más datos se decide mejor.»",
             "Con mejores definiciones se decide mejor. Más datos mal definidos multiplican el error."),
        ],
        honestidad=(
            "El programa te da criterio analítico y práctica sobre datos sintéticos, no experiencia con la "
            "infraestructura de datos de una empresa real. Para postular a este rol conviene complementar con "
            "SQL sobre una base propia y, si el puesto lo pide, con la herramienta de analítica que use la "
            "organización."
        ),
    ),
    # ------------------------------------------------------------------ 02
    dict(
        slug="marketing-manager",
        emoji="🎯",
        titulo="Marketing manager",
        familia="Marketing",
        resumen=(
            "El perfil que decide dónde compite la empresa y con qué diferencia, y después responde por que "
            "esa elección produzca demanda. Es el puesto más generalista del área y, por eso mismo, el que "
            "más fácilmente se convierte en gestor de proveedores si no sostiene criterio propio."
        ),
        nivel="Intermedio; suele pedir 3 a 5 años en marketing o en un rol adyacente",
        foco="Posicionamiento, plan de adquisición, marca, contenido y presupuesto",
        credencial="Un plan de adquisición ejecutado con economía verificable",
        que_es=[
            "Marketing manager es un título que cubre realidades muy distintas. En una empresa de veinte "
            "personas es quien hace todo: escribe, compra medios, arma el sitio y responde por los leads. En "
            "una de doscientas es quien coordina especialistas y responde por el presupuesto y por la "
            "coherencia de la marca.",
            "En ambos casos el trabajo central es el mismo: elegir a quién servir, con qué diferencia "
            "comprobable, y sostener esa elección frente a la presión constante de hacer un poco de todo. La "
            "mayoría de los planes de marketing de pyme son listas de actividades sin diagnóstico, y por eso "
            "no pueden evaluarse.",
            "El puesto tiene una tensión permanente entre el corto y el largo plazo. La activación produce "
            "resultado medible este mes; la construcción de marca reduce el costo de adquisición dentro de "
            "dos años y es difícil de defender ante un comité que pide números trimestrales. Saber sostener "
            "ese equilibrio con evidencia es lo que separa a un manager de un ejecutor.",
        ],
        dia=[
            "**Revisión de resultados:** qué canal está produciendo oportunidades calificadas y a qué costo, "
            "no cuántas visitas trajo.",
            "**Coordinación con ventas:** qué leads llegaron, cuáles se trabajaron y por qué se rechazaron "
            "los demás. Sin esta conversación, cada área optimiza su métrica y el sistema pierde.",
            "**Producción y aprobación:** revisar piezas, verificar que cada afirmación tenga respaldo y que "
            "la promesa del anuncio aparezca en la página de destino.",
            "**Presupuesto:** decidir reasignaciones con criterio escrito y no reaccionar a la variación de "
            "una semana.",
            "**Investigación:** hablar con clientes o revisar grabaciones de venta. El vocabulario del cliente "
            "no se descubre en una reunión interna.",
        ],
        tecnico=[
            "**Segmentación, targeting y posicionamiento.** Elegir a quién servir y declarar qué se descarta. "
            "Sin descarte no hay estrategia.",
            "**Propuesta de valor probada.** Una afirmación falsable que un cliente pueda repetir con sus "
            "palabras, no un eslogan.",
            "**Economía de canales.** Costo por oportunidad calificada, margen por canal y dependencia de "
            "plataforma.",
            "**Construcción de marca.** Disponibilidad mental y física, activos distintivos y la evidencia "
            "empírica de que la penetración es el motor del crecimiento.",
            "**Medición honesta.** Distinguir demanda creada de demanda capturada, y tráfico de marca de "
            "tráfico genérico.",
            "**Cumplimiento.** Información veraz al consumidor y tratamiento lícito de datos personales como "
            "restricción de diseño, no como revisión final.",
        ],
        herramientas=(
            "Analítica:        Google Analytics, Looker Studio\n"
            "Medios pagados:   Google Ads, Meta Ads, LinkedIn Ads\n"
            "Automatización:   HubSpot, Mailchimp, ActiveCampaign\n"
            "Sitio y CRO:      CMS, mapas de calor, pruebas A/B\n"
            "Contenido:        calendario editorial, guía de estilo\n"
            "Investigación:    entrevistas, encuestas, escucha de conversaciones"
        ),
        blandas=[
            "**Sostener una elección.** El foco se erosiona por peticiones internas razonables una por una.",
            "**Traducir a lenguaje de negocio.** «Aumenté el tráfico» vale menos que «bajé el costo por "
            "oportunidad calificada de X a Y, y aquí está el cálculo».",
            "**Trabajar con ventas sin subordinarse.** El acuerdo de servicio entre ambas áreas es una "
            "negociación permanente.",
            "**Resistir la moda.** Cada trimestre aparece un canal que hay que usar «porque sí».",
        ],
        ruta=[
            ("01", "el sistema comercial completo: sin él, marketing optimiza una etapa y daña el resultado"),
            ("02", "expediente de cliente con evidencia: la base de todo mensaje que funcione"),
            ("04", "**el núcleo estratégico**: segmentación, targeting y posicionamiento comprobable"),
            ("06", "marca como activo que reduce el costo de adquisición futuro"),
            ("12", "**el núcleo operativo**: plan de adquisición digital y auditoría"),
            ("13", "sistema editorial: qué se publica, por qué y con qué control de afirmaciones"),
            ("14", "medios pagados con economía verificable y salvaguardas"),
            ("20", "analítica: para no reportar retorno sobre ingreso que habría ocurrido igual"),
        ],
        clases=[
            ("04", "11", "Declaración de posicionamiento: el criterio que permite rechazar ideas"),
            ("04", "06", "Targeting: por qué declarar foco sin cambiar la asignación de recursos no sirve"),
            ("06", "01", "Qué es una marca: disponibilidad mental y física, no el logo"),
            ("12", "01", "Estrategia digital: activo propio frente a audiencia alquilada"),
            ("12", "13", "Plan de adquisición: supuestos explícitos y capacidad de atención"),
            ("14", "10", "CPA, CAC y ROAS: tres cosas distintas que se confunden a diario"),
            ("13", "01", "Estrategia de contenidos: publicar para la audiencia, no para la empresa"),
            ("20", "09", "Incrementalidad: qué habría pasado sin esta inversión"),
        ],
        labs=["04", "12", "14"],
        artefactos=[
            "Arquitectura STP con criterios de atractivo y accesibilidad",
            "Declaración de posicionamiento probada con comprensión y recuerdo medidos",
            "Plan de adquisición con supuestos, umbrales y reglas de reasignación",
            "Auditoría de marketing digital con hallazgos priorizados por efecto y costo",
        ],
        credenciales=[
            "**Google Ads / Meta Blueprint** — acreditan operación de plataforma. Útiles para pasar filtros "
            "de RRHH; no acreditan criterio estratégico.",
            "**HubSpot Academy** — gratuita y razonable para vocabulario de inbound y automatización.",
            "**Portafolio** — un plan con economía verificable y una auditoría real pesan más que ambas.",
        ],
        progresion=(
            "Especialista → marketing manager → **head of marketing** o **[CMO](cmo.md)**. Los desvíos "
            "frecuentes son hacia [product marketing](product-marketing.md) —si el interés es la oferta y el "
            "posicionamiento— o hacia [growth](growth-manager.md) —si el interés es el sistema y la "
            "experimentación—."
        ),
        salario=SALARIO_MEDIO,
        mitos=[
            ("«Marketing es creatividad.»",
             "La creatividad ejecuta una elección estratégica. Sin esa elección, produce piezas bonitas que "
             "no mueven nada."),
            ("«Hay que estar en todos los canales.»",
             "Cada canal adicional divide el presupuesto y la atención. La dispersión es el error más común "
             "del rol."),
            ("«La marca no se puede medir.»",
             "Se mide con notoriedad espontánea, consideración y prima de precio sostenida. Lo que no se "
             "puede es medirla trimestralmente como una campaña."),
            ("«El objetivo es generar leads.»",
             "El objetivo es generar oportunidades que ventas pueda cerrar con margen. Trescientos leads que "
             "nadie trabaja son un costo, no un resultado."),
        ],
        honestidad=(
            "El programa entrega criterio estratégico y método de medición. No entrega experiencia operando "
            "cuentas publicitarias reales con presupuesto propio, que es lo que muchas ofertas piden. "
            "Complementa con una cuenta real, aunque sea pequeña, y documenta la economía de lo que ejecutes."
        ),
    ),
    # ------------------------------------------------------------------ 03
    dict(
        slug="product-marketing",
        emoji="🧩",
        titulo="Product marketing manager",
        familia="Marketing",
        resumen=(
            "El puente entre lo que el producto hace y lo que el mercado entiende. Responde por el "
            "posicionamiento, por el relato comercial y por que el equipo de ventas tenga argumentos que "
            "resistan preguntas técnicas."
        ),
        nivel="Intermedio a senior; suele venir de marketing, de producto o de ventas",
        foco="Investigación de cliente, posicionamiento, oferta, lanzamientos y habilitación comercial",
        credencial="Una oferta lista para vender que otra persona pueda presentar sin inventar nada",
        que_es=[
            "Product marketing existe porque hay una brecha permanente entre lo que produce ingeniería y lo "
            "que el mercado compra. El producto entrega capacidades; el cliente compra resultados. Traducir "
            "una en otra, con evidencia y sin exagerar, es el trabajo.",
            "Es un rol de investigación antes que de comunicación. Antes de escribir una línea hay que saber "
            "qué progreso intenta lograr el cliente, contra qué alternativa compara y qué objeción aparece "
            "primero. Sin eso, el relato se construye sobre lo que el equipo cree, que casi nunca coincide "
            "con lo que el cliente dice.",
            "Su prueba de calidad es operativa: un ejecutivo comercial que no participó del diseño debe poder "
            "presentar la oferta, responder las cinco objeciones más frecuentes y cerrar sin prometer nada "
            "que la operación no pueda entregar.",
        ],
        dia=[
            "**Entrevistas y escucha:** conversaciones con clientes ganados y perdidos, y revisión de "
            "grabaciones de venta. El vocabulario del mercado se recoge, no se inventa.",
            "**Trabajo de posicionamiento:** revisar si la promesa actual sigue siendo diferenciadora o si el "
            "competidor ya la iguala.",
            "**Habilitación comercial:** producir el material que ventas necesita y verificar que se use. Un "
            "documento que nadie abre no habilita nada.",
            "**Coordinación de lanzamiento:** asegurar que el equipo interno esté listo antes de comunicar "
            "hacia afuera. El fracaso típico de un lanzamiento es de preparación, no de mensaje.",
            "**Análisis competitivo:** entender el modelo económico del competidor, no sólo su lista de "
            "funcionalidades.",
        ],
        tecnico=[
            "**Jobs to Be Done.** El progreso que el cliente intenta lograr en una circunstancia concreta, "
            "con sus fuerzas de resistencia.",
            "**Investigación cualitativa rigurosa.** Preguntar por comportamiento pasado y no por intención "
            "futura; buscar activamente el caso que refuta.",
            "**Posicionamiento y puntos de paridad.** Distinguir lo que hay que acreditar para ser "
            "considerado de lo que inclina la elección.",
            "**Diseño de oferta.** Alcance, exclusiones, garantía y llamado a la acción; qué se excluye "
            "deliberadamente.",
            "**Habilitación de ventas.** Guiones de discovery, biblioteca de objeciones y materiales que "
            "circulan sin su autor.",
            "**Lanzamientos.** Criterios de listeza interna antes de la comunicación externa.",
        ],
        herramientas=(
            "Investigación:    entrevistas, encuestas, análisis de grabaciones\n"
            "Posicionamiento:  mapas perceptuales, pruebas de mensaje\n"
            "Habilitación:     bibliotecas de contenido, plantillas de propuesta\n"
            "Competencia:      seguimiento de precios, análisis de ofertas\n"
            "Coordinación:     planes de lanzamiento con criterios de listeza"
        ),
        blandas=[
            "**Escuchar sin conducir.** Una entrevista que confirma la hipótesis propia no produjo "
            "información.",
            "**Escribir para el escéptico.** El documento llegará a finanzas o al área técnica del cliente.",
            "**Coordinar sin autoridad.** El rol depende de producto, ventas y marketing, y no manda sobre "
            "ninguno.",
            "**Decir que la promesa no se puede sostener.** Es la conversación más incómoda y la más "
            "valiosa.",
        ],
        ruta=[
            ("02", "**la base del rol**: cliente, unidad de decisión, jobs y fricciones"),
            ("03", "investigación con método: muestra, sesgo y trazabilidad"),
            ("04", "posicionamiento y diferenciación comprobable frente a la alternativa real"),
            ("05", "**el núcleo**: propuesta de valor, diseño de oferta y encaje producto-mercado"),
            ("09", "venta consultiva: para producir material que sirva en un negocio real"),
            ("22", "go-to-market y lanzamientos con criterios de listeza"),
        ],
        clases=[
            ("02", "03", "Jobs to Be Done: circunstancia, fuerzas de progreso y de resistencia"),
            ("02", "11", "Objeciones antes de comprar: el registro que corrige la oferta"),
            ("05", "02", "Value Proposition Canvas: encaje verificado, no supuesto"),
            ("05", "14", "Oferta lista para vender: la prueba de traspaso"),
            ("04", "09", "Puntos de paridad y de diferencia: el orden correcto del mensaje"),
            ("03", "03", "Diseño de entrevistas: preguntar por comportamiento pasado"),
            ("22", "09", "Lanzamientos: listeza interna antes de comunicación externa"),
        ],
        labs=["02", "05", "22"],
        artefactos=[
            "Expediente de cliente con ICP, unidad de decisión y journey documentados",
            "Propuesta de valor con prueba de comprensión superada",
            "Oferta operativa con alcance, exclusiones y biblioteca de objeciones",
            "Plan de lanzamiento con criterios de listeza verificados",
        ],
        credenciales=[
            "**Pragmatic Institute / Product Marketing Alliance** — reconocidas en el gremio; su valor real "
            "es el marco compartido, no el diploma.",
            "**Portafolio** — un expediente de cliente con evidencia y una oferta con prueba de traspaso "
            "acreditan mejor que cualquier curso.",
        ],
        progresion=(
            "Product marketing → **head of product marketing** → [CMO](cmo.md) o dirección de producto. "
            "También es una rampa natural hacia [go-to-market](head-of-gtm.md) en empresas que expanden a "
            "nuevos segmentos o mercados."
        ),
        salario=SALARIO_MEDIO,
        mitos=[
            ("«Es escribir el mensaje.»",
             "El mensaje es la última parte. Antes hay investigación, posicionamiento y diseño de oferta."),
            ("«Basta con conocer el producto.»",
             "Conocer el producto sin conocer la alternativa contra la que compite produce material que sólo "
             "convence internamente."),
            ("«El lanzamiento es un evento.»",
             "Es un proceso cuyo fracaso más común ocurre adentro: ventas sin capacitar y soporte sin "
             "documentación."),
        ],
        honestidad=(
            "El programa cubre el método completo del rol. Lo que no puede darte es acceso a clientes reales "
            "para entrevistar, que es donde el músculo se construye. Consigue diez conversaciones reales, "
            "aunque sea en un proyecto propio, y documéntalas con el método de la parte 03."
        ),
    ),
    # ------------------------------------------------------------------ 04
    dict(
        slug="growth-manager",
        emoji="🚀",
        titulo="Growth manager",
        familia="Growth",
        resumen=(
            "El perfil que instala un motor de experimentación sobre todo el recorrido del cliente, incluido "
            "el producto. No es marketing con otro nombre: sin acceso a producto y a datos, el rol se degrada "
            "a optimización de campañas."
        ),
        nivel="Intermedio a senior; exige base analítica y capacidad de coordinar con producto",
        foco="Activación, retención, bucles de crecimiento, experimentación y economía del modelo",
        credencial="Un growth model con tres experimentos que refutaron su hipótesis",
        que_es=[
            "Growth es un método de trabajo, no un canal. Consiste en aplicar experimentación sistemática a "
            "todo el recorrido —adquisición, activación, retención, referencia e ingreso— y acumular "
            "aprendizaje en lugar de acumular campañas.",
            "Su decisión más contraintuitiva es de orden: en la mayoría de los negocios conviene trabajar "
            "retención y activación antes que adquisición, porque invertir en tráfico con una curva de "
            "retención que no se estabiliza es llenar un estanque con fuga. La presión organizacional siempre "
            "empuja en la dirección contraria.",
            "El requisito estructural es el alcance de intervención. Un equipo de growth que sólo puede "
            "modificar landings y correos no puede tocar el onboarding, que suele ser el mayor punto de "
            "fuga. Antes de aceptar el puesto conviene preguntar qué palancas se pueden mover.",
        ],
        dia=[
            "**Revisión del modelo:** qué palanca movió el resultado la semana pasada y si el efecto se "
            "sostiene o fue variación normal.",
            "**Diseño de experimentos:** formular la hipótesis con su criterio de refutación **antes** de "
            "ejecutar. Sin ese criterio previo, cualquier resultado se lee como confirmación.",
            "**Coordinación con producto:** los cambios que más mueven la aguja están dentro del producto, y "
            "eso exige prioridad compartida.",
            "**Análisis de activación:** qué acción, en qué plazo, predice la permanencia. Es el análisis de "
            "mayor retorno del rol.",
            "**Documentación de aprendizajes:** un experimento sin conclusión registrada es dinero gastado "
            "sin capitalizar.",
        ],
        tecnico=[
            "**Métrica estrella y sus entradas.** Un indicador que represente valor entregado y correlacione "
            "con ingreso, descompuesto en palancas accionables.",
            "**Activación.** Identificar con datos el evento que predice retención y rediseñar el inicio para "
            "producirlo antes.",
            "**Retención por cohorte.** Verificar si la curva se estabiliza antes de escalar cualquier gasto.",
            "**Bucles de crecimiento.** Distinguir un bucle real —output del usuario visible para terceros— "
            "de un embudo con nombre nuevo.",
            "**Diseño estadístico.** Tamaño de muestra, potencia, guardarraíles y las trampas de la detención "
            "temprana.",
            "**Economía del modelo.** Periodo de recuperación frente a vida media del cliente; sin eso, "
            "escalar destruye caja.",
        ],
        herramientas=(
            "Analítica de producto: herramientas de eventos y embudos\n"
            "Experimentación:       banderas de funcionalidad, pruebas A/B\n"
            "Datos:                 SQL, cohortes, calculadoras de potencia\n"
            "Adquisición:           plataformas de medios, correo, referidos\n"
            "Gestión:               backlog de experimentos con hipótesis y criterio"
        ),
        blandas=[
            "**Tolerancia al resultado negativo.** La mayoría de los experimentos no confirma la hipótesis, y "
            "ese es el funcionamiento normal.",
            "**Negociar prioridad con producto.** El rol no manda sobre el roadmap y depende de él.",
            "**Resistir la presión de escalar.** Decir «todavía no» cuando la retención no se estabiliza es "
            "la contribución más valiosa y la menos popular.",
            "**Comunicar incertidumbre.** Un resultado con muestra insuficiente no es un resultado.",
        ],
        ruta=[
            ("01", "el sistema completo, para no optimizar una etapa dañando el conjunto"),
            ("18", "**retención primero**: si la curva no se estabiliza, adquirir es tirar dinero"),
            ("19", "**el núcleo**: métrica estrella, bucles, activación y backlog de experimentos"),
            ("20", "el rigor analítico que separa un aprendizaje de una casualidad"),
            ("12", "adquisición digital, conversión y medición"),
            ("15", "comercio digital, donde el embudo es medible de punta a punta"),
            ("21", "IA aplicada con evaluación y guardarraíles"),
        ],
        clases=[
            ("19", "02", "North Star Metric: elegir un indicador que represente valor real"),
            ("19", "05", "Activación: el evento que predice permanencia"),
            ("19", "06", "Crecimiento centrado en retención: el orden que casi nadie respeta"),
            ("19", "04", "Growth loops: por qué el bucle compone y el embudo se agota"),
            ("19", "11", "Diseño de experimentos: las trampas que invalidan la conclusión"),
            ("20", "10", "A/B testing: por qué la mayoría de las mejoras no se replican"),
            ("18", "03", "Time to value: el indicador más predictivo de retención"),
        ],
        labs=["19", "18", "20"],
        artefactos=[
            "Growth model con palancas, sensibilidad y aprendizajes acumulados",
            "Análisis de activación con evento identificado y verificado experimentalmente",
            "Backlog de experimentos con hipótesis, criterio previo y resultados",
            "Curvas de retención por cohorte con lectura de mejora entre cohortes",
        ],
        credenciales=[
            "**Reforge / CXL** — formación reconocida en el gremio, de pago y bastante buena.",
            "**Portafolio** — tres experimentos documentados con criterio previo, incluidos los que "
            "fracasaron, acreditan más que cualquier curso.",
        ],
        progresion=(
            "Growth manager → **head of growth** → [CRO](cro.md) o dirección de producto. Es también un "
            "camino frecuente hacia [founder](founder.md), porque el método de validación es el mismo."
        ),
        salario=SALARIO_MEDIO,
        mitos=[
            ("«Growth es hacer trucos de adquisición.»",
             "Los trucos se agotan. El método consiste en encontrar y reforzar el mecanismo que hace que el "
             "crecimiento se retroalimente."),
            ("«Hay que experimentar todo el tiempo.»",
             "Con poco tráfico, un test no alcanza potencia estadística. La alternativa honesta es decidir "
             "con investigación cualitativa y declararlo."),
            ("«El equipo de growth es marketing.»",
             "Sin acceso al producto no puede tocar activación ni retención, que es donde está el mayor "
             "punto de fuga."),
            ("«Un experimento ganador se implementa y listo.»",
             "Si sostiene una decisión importante, hay que replicarlo. Muchas mejoras declaradas no "
             "sobreviven a la segunda medición."),
        ],
        honestidad=(
            "El programa entrega el método completo y la disciplina estadística. Lo que no puede simular es "
            "la negociación real de prioridad con un equipo de producto, que es la mitad del trabajo. "
            "Documenta experimentos reales aunque sean pequeños: importa el criterio previo, no el tamaño."
        ),
    ),
]

# Segundo bloque: venta, operación de ingresos y dirección.
from spec.roles_b import ROLES_B  # noqa: E402

ROLES = ROLES + ROLES_B

FAMILIAS = ["Analítica", "Marketing", "Growth", "Adquisición", "Ventas",
            "Retención", "Operación de ingresos", "Dirección"]


def por_slug(slug):
    for rol in ROLES:
        if rol["slug"] == slug:
            return rol
    raise KeyError("Rol inexistente: {}".format(slug))
