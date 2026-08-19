# -*- coding: utf-8 -*-
"""Bibliografía maestra del programa.

Cada entrada declara autoría, obra, edición de referencia y el *lente* que
aporta: para qué sirve esa lectura dentro de una decisión comercial. El
repositorio no reproduce ni distribuye las obras; las cita y enseña a usarlas de
forma selectiva.

Clave -> (autoría, obra, edición de referencia, lente, categoría)
"""

LIBROS = {
    # --- Marketing y estrategia ---------------------------------------------
    "kotler": ("Philip Kotler, Kevin Lane Keller y Alexander Chernev", "Marketing Management", "2021, 16.ª ed.",
               "estructura canónica del marketing: análisis, STP, mezcla comercial y gestión de la demanda", "marketing"),
    "sharp": ("Byron Sharp", "How Brands Grow", "2010",
              "evidencia empírica sobre penetración, disponibilidad mental y física y crecimiento de marcas", "marketing"),
    "sharp2": ("Jenni Romaniuk y Byron Sharp", "How Brands Grow: Part 2", "2015",
               "activos distintivos de marca, alcance y aplicación de las leyes empíricas a mercados emergentes", "marketing"),
    "binet-field": ("Les Binet y Peter Field", "The Long and the Short of It", "2013",
                    "equilibrio entre construcción de marca a largo plazo y activación de ventas a corto plazo", "marketing"),
    "ries-trout": ("Al Ries y Jack Trout", "Positioning: The Battle for Your Mind", "2001, ed. revisada",
                   "posicionamiento como lugar en la mente del cliente y no como declaración interna", "marketing"),
    "porter": ("Michael E. Porter", "Competitive Strategy", "1980",
               "estructura de industria, fuerzas competitivas y elección de una posición defendible", "estrategia"),
    "porter-hbr": ("Michael E. Porter", "What Is Strategy? (Harvard Business Review)", "1996",
                   "estrategia como sistema de actividades coherentes y elección explícita de qué no hacer", "estrategia"),
    "rumelt": ("Richard Rumelt", "Good Strategy / Bad Strategy", "2011",
               "diagnóstico, política rectora y acción coherente frente a la estrategia decorativa", "estrategia"),
    "kim-mauborgne": ("W. Chan Kim y Renée Mauborgne", "Blue Ocean Strategy", "2015, ed. ampliada",
                      "reconstrucción de las fronteras del mercado y curva de valor", "estrategia"),
    "moore": ("Geoffrey A. Moore", "Crossing the Chasm", "2014, 3.ª ed.",
              "adopción tecnológica, beachhead market y el abismo entre visionarios y pragmáticos", "estrategia"),
    "drucker": ("Peter F. Drucker", "The Practice of Management", "1954",
                "el propósito de una empresa es crear un cliente; marketing e innovación como funciones centrales", "estrategia"),
    "levitt": ("Theodore Levitt", "Marketing Myopia (Harvard Business Review)", "1960",
               "definir el negocio por el trabajo del cliente y no por el producto que se fabrica", "marketing"),

    # --- Cliente, investigación y comportamiento -----------------------------
    "christensen": ("Clayton M. Christensen, Taddy Hall, Karen Dillon y David S. Duncan", "Competing Against Luck", "2016",
                    "Jobs to Be Done: el progreso que el cliente intenta lograr y el circuito de contratación", "cliente"),
    "ulwick": ("Anthony W. Ulwick", "Jobs to Be Done: Theory to Practice", "2016",
               "outcome-driven innovation: resultados deseados medibles y priorización por oportunidad", "cliente"),
    "fitzpatrick": ("Rob Fitzpatrick", "The Mom Test", "2013",
                    "entrevistas que producen datos y no cortesía; preguntar por comportamiento pasado", "investigacion"),
    "portigal": ("Steve Portigal", "Interviewing Users", "2023, 2.ª ed.",
                 "conducción de entrevistas, escucha activa y traducción de observación en decisión", "investigacion"),
    "blank": ("Steve Blank y Bob Dorf", "The Startup Owner's Manual", "2012",
              "customer discovery y validación fuera del edificio como proceso reproducible", "investigacion"),
    "osterwalder-vpd": ("Alexander Osterwalder, Yves Pigneur, Greg Bernarda y Alan Smith", "Value Proposition Design", "2014",
                        "encaje entre perfil del cliente y mapa de valor; prueba de propuestas antes de construir", "oferta"),
    "osterwalder-bmg": ("Alexander Osterwalder e Yves Pigneur", "Business Model Generation", "2010",
                        "modelo de negocio como sistema de nueve bloques interdependientes", "estrategia"),
    "kahneman": ("Daniel Kahneman", "Thinking, Fast and Slow", "2011",
                 "sistemas 1 y 2, heurísticas y sesgos aplicables a decisiones de compra y de gestión", "comportamiento"),
    "thaler": ("Richard H. Thaler y Cass R. Sunstein", "Nudge: The Final Edition", "2021",
               "arquitectura de decisión y límites éticos de la influencia sobre la elección", "comportamiento"),
    "cialdini": ("Robert B. Cialdini", "Influence: The Psychology of Persuasion, New and Expanded", "2021",
                 "principios de influencia y su uso ético en contextos comerciales", "comportamiento"),
    "ariely": ("Dan Ariely", "Predictably Irrational", "2008",
               "efectos de anclaje, gratuidad y comparación en la percepción de valor", "comportamiento"),
    "solomon": ("Michael R. Solomon", "Consumer Behavior: Buying, Having, and Being", "2019, 13.ª ed.",
                "marco académico del comportamiento del consumidor: cultura, identidad y proceso de decisión", "comportamiento"),
    "malhotra": ("Naresh K. Malhotra", "Marketing Research: An Applied Orientation", "2019, 7.ª ed.",
                 "diseño de investigación, muestreo, medición y análisis con rigor metodológico", "investigacion"),
    "krug": ("Steve Krug", "Don't Make Me Think, Revisited", "2014",
             "usabilidad, claridad y pruebas baratas con usuarios reales", "digital"),

    # --- Marca y comunicación ------------------------------------------------
    "aaker": ("David A. Aaker", "Building Strong Brands", "1996",
              "brand equity, identidad de marca y arquitectura de portafolio", "marca"),
    "keller-brand": ("Kevin Lane Keller y Vanitha Swaminathan", "Strategic Brand Management", "2019, 5.ª ed.",
                     "modelo CBBE: notoriedad, significado, respuesta y resonancia de marca", "marca"),
    "wheeler": ("Alina Wheeler y Rob Meyerson", "Designing Brand Identity", "2024, 6.ª ed.",
                "proceso de identidad de marca: investigación, diseño, aplicación y gobierno", "marca"),
    "heath": ("Chip Heath y Dan Heath", "Made to Stick", "2007",
              "ideas que se recuerdan: simplicidad, concreción, credibilidad y emoción", "comunicacion"),
    "godin": ("Seth Godin", "This Is Marketing", "2018",
              "marketing como servicio a un público mínimo viable y construcción de confianza", "marketing"),
    "handley": ("Ann Handley", "Everybody Writes", "2022, 2.ª ed.",
                "estándar editorial: claridad, utilidad y empatía en la escritura comercial", "contenido"),
    "pulizzi": ("Joe Pulizzi", "Content Inc.", "2021, 2.ª ed.",
                "construcción de audiencia propia antes de monetizar y modelo editorial sostenido", "contenido"),
    "sugarman": ("Joseph Sugarman", "The Adweek Copywriting Handbook", "2007",
                 "mecánica del copy persuasivo: ritmo, curiosidad y coherencia de la promesa", "contenido"),
    "ogilvy": ("David Ogilvy", "Ogilvy on Advertising", "1983",
               "disciplina publicitaria basada en investigación, oferta clara y respeto por el lector", "publicidad"),

    # --- Precio y monetización -----------------------------------------------
    "nagle": ("Thomas T. Nagle y Georg Müller", "The Strategy and Tactics of Pricing", "2018, 6.ª ed.",
              "pricing basado en valor, estructura de precios, métrica de cobro y política de descuentos", "precio"),
    "simon": ("Hermann Simon", "Confessions of the Pricing Man", "2015",
              "el precio como la palanca de utilidad más rápida y su relación con el valor percibido", "precio"),
    "ramanujam": ("Madhavan Ramanujam y Georg Tacke", "Monetizing Innovation", "2016",
                  "diseñar el producto alrededor del precio: disposición a pagar antes de construir", "precio"),
    "smith-pricing": ("Tim J. Smith", "Pricing Strategy", "2011",
                      "segmentación de precios, price fences y decisiones de estructura", "precio"),

    # --- Ventas ---------------------------------------------------------------
    "rackham": ("Neil Rackham", "SPIN Selling", "1988",
                "investigación conductual sobre venta compleja: situación, problema, implicación y necesidad-beneficio", "ventas"),
    "dixon-challenger": ("Matthew Dixon y Brent Adamson", "The Challenger Sale", "2011",
                         "enseñar, adaptar y tomar el control; el insight comercial como diferenciador", "ventas"),
    "dixon-customer": ("Brent Adamson y Matthew Dixon", "The Challenger Customer", "2015",
                       "comité de compra, mobilizer y construcción de consenso interno del cliente", "ventas"),
    "keenan": ("Keenan", "Gap Selling", "2018",
               "vender la brecha entre estado actual y estado futuro con diagnóstico riguroso", "ventas"),
    "blount": ("Jeb Blount", "Fanatical Prospecting", "2015",
               "disciplina de prospección, cadencia y gestión del rechazo", "ventas"),
    "weinberg-sales": ("Mike Weinberg", "New Sales. Simplified.", "2012",
                       "proceso de nueva venta: lista objetivo, relato comercial y actividad sostenida", "ventas"),
    "ross": ("Aaron Ross y Marylou Tyler", "Predictable Revenue", "2011",
             "especialización de roles comerciales y generación de pipeline predecible", "ventas"),
    "miller-heiman": ("Robert B. Miller y Stephen E. Heiman", "The New Strategic Selling", "2005",
                      "mapa de influencias, roles de compra y análisis de posición en cuentas complejas", "ventas"),
    "roberge": ("Mark Roberge", "The Sales Acceleration Formula", "2015",
                "contratación, formación, gestión y demanda comercial gobernadas por datos", "ventas"),
    "bertuzzi": ("Trish Bertuzzi", "The Sales Development Playbook", "2016",
                 "estructura, especialización y métricas del equipo de desarrollo de ventas", "ventas"),
    "vaynerchuk": ("Gary Vaynerchuk", "Jab, Jab, Jab, Right Hook", "2013",
                   "secuencia de aporte de valor antes de la petición comercial en canales sociales", "ventas"),

    # --- Negociación ----------------------------------------------------------
    "fisher-ury": ("Roger Fisher, William Ury y Bruce Patton", "Getting to Yes", "2011, 3.ª ed.",
                   "negociación por principios: intereses, opciones, criterios objetivos y BATNA", "negociacion"),
    "ury": ("William Ury", "Getting Past No", "2007",
            "manejo de tácticas duras, reencuadre y construcción de puentes", "negociacion"),
    "voss": ("Chris Voss y Tahl Raz", "Never Split the Difference", "2016",
             "empatía táctica, etiquetado y preguntas calibradas bajo presión", "negociacion"),
    "malhotra-neg": ("Deepak Malhotra y Max H. Bazerman", "Negotiation Genius", "2007",
                     "preparación analítica, ZOPA, valor creado frente a valor reclamado y ética negociadora", "negociacion"),
    "shell": ("G. Richard Shell", "Bargaining for Advantage", "2006",
              "estilos de negociación, autoridad y estándares de legitimidad", "negociacion"),

    # --- Digital, e-commerce y performance ------------------------------------
    "chaffey": ("Dave Chaffey y Fiona Ellis-Chadwick", "Digital Marketing", "2022, 8.ª ed.",
                "planificación digital integrada: canales, medición y gobierno", "digital"),
    "kaushik": ("Avinash Kaushik", "Web Analytics 2.0", "2009",
                "medición orientada a decisión, segmentación y crítica del dato de vanidad", "analitica"),
    "enge-seo": ("Eric Enge, Stephan Spencer y Jessie Stricchiola", "The Art of SEO", "2023, 4.ª ed.",
                 "arquitectura, contenido y autoridad como sistema de búsqueda orgánica", "digital"),
    "geddes": ("Brad Geddes", "Advanced Google AdWords", "2014, 3.ª ed.",
               "estructura de cuentas, subastas, calidad y control del gasto en búsqueda pagada", "publicidad"),
    "eisenberg": ("Bryan Eisenberg y Jeffrey Eisenberg", "Call to Action", "2005",
                  "optimización de conversión con hipótesis, escenarios y persuasión medible", "digital"),
    "laja": ("Peep Laja y el equipo de CXL", "Conversion Optimization Playbooks (CXL)", "2024",
             "método CRO basado en investigación previa al test y validez estadística", "digital"),
    "flint": ("Kevin Hillstrom", "Hillstrom's Multichannel Forensics", "2007",
              "diagnóstico de comportamiento de compra multicanal y migración de clientes", "ecommerce"),

    # --- Growth, producto y experimentación -----------------------------------
    "ellis-brown": ("Sean Ellis y Morgan Brown", "Hacking Growth", "2017",
                    "equipo multifuncional, ciclo de experimentación y aha moment", "growth"),
    "ries-lean": ("Eric Ries", "The Lean Startup", "2011",
                  "construir-medir-aprender, MVP y decisión de perseverar o pivotar", "growth"),
    "weinberg-traction": ("Gabriel Weinberg y Justin Mares", "Traction", "2015",
                          "diecinueve canales de tracción y el método bullseye de priorización", "growth"),
    "croll-yoskovitz": ("Alistair Croll y Benjamin Yoskovitz", "Lean Analytics", "2013",
                        "una métrica que importa por etapa y por modelo de negocio", "analitica"),
    "bush-plg": ("Wes Bush", "Product-Led Growth", "2019",
                 "el producto como principal vehículo de adquisición, activación y expansión", "growth"),
    "cagan": ("Marty Cagan", "Inspired", "2017, 2.ª ed.",
              "descubrimiento de producto y riesgos de valor, usabilidad, viabilidad y factibilidad", "producto"),
    "kohavi": ("Ron Kohavi, Diane Tang y Ya Xu", "Trustworthy Online Controlled Experiments", "2020",
               "diseño estadístico de experimentos, métricas guardrail y trampas de interpretación", "analitica"),
    "hulick": ("Samuel Hulick", "The Elements of User Onboarding", "2014",
               "diseño del primer valor percibido y reducción del time-to-value", "producto"),

    # --- Retención y éxito de cliente -----------------------------------------
    "mehta": ("Nick Mehta, Dan Steinman y Lincoln Murphy", "Customer Success", "2016",
              "disciplina operativa de éxito de cliente: salud, renovación y expansión", "retencion"),
    "reichheld": ("Fred Reichheld, Darci Darnell y Maureen Burns", "Winning on Purpose", "2021",
                  "lealtad, economía del cliente ganado y usos correctos e incorrectos del NPS", "retencion"),
    "fader": ("Peter Fader", "Customer Centricity", "2020, 2.ª ed.",
              "valor heterogéneo del cliente y asignación de recursos por valor esperado", "retencion"),
    "fader-ltv": ("Peter Fader y Sarah Toms", "The Customer Centricity Playbook", "2018",
                  "modelos de valor de vida del cliente y decisiones de inversión por cohorte", "retencion"),
    "dixon-effort": ("Matthew Dixon, Nick Toman y Rick DeLisi", "The Effortless Experience", "2013",
                     "reducción del esfuerzo del cliente como motor de lealtad frente al deleite", "retencion"),

    # --- Operaciones de ingresos y dirección ----------------------------------
    "diorio": ("Stephen G. Diorio y Chris K. Hummel", "Revenue Operations", "2022",
               "integración de datos, procesos y equipos que producen ingreso como un solo sistema", "revops"),
    "doerr": ("John Doerr", "Measure What Matters", "2018",
              "OKR como sistema de foco, alineamiento y seguimiento", "direccion"),
    "grove": ("Andrew S. Grove", "High Output Management", "1983",
              "output gerencial, indicadores adelantados y reuniones como herramienta de producción", "direccion"),
    "kaplan-norton": ("Robert S. Kaplan y David P. Norton", "The Balanced Scorecard", "1996",
                      "traducción de la estrategia en indicadores causalmente conectados", "direccion"),
    "zoltners": ("Andris A. Zoltners, Prabhakant Sinha y Sally E. Lorimer", "The Complete Guide to Sales Force Incentive Compensation", "2006",
                 "diseño de cuotas, territorios e incentivos sin efectos perversos", "direccion"),
    "sinek": ("Simon Sinek", "Start With Why", "2009",
              "propósito como articulador del relato interno y externo", "direccion"),
    "collins": ("Jim Collins", "Good to Great", "2001",
                "disciplina, personas correctas y concepto del erizo aplicados a la ejecución comercial", "direccion"),
    "lencioni": ("Patrick Lencioni", "The Five Dysfunctions of a Team", "2002",
                 "confianza, conflicto productivo, compromiso, accountability y resultados", "direccion"),

    # --- Datos, IA y ética ----------------------------------------------------
    "provost": ("Foster Provost y Tom Fawcett", "Data Science for Business", "2013",
                "pensamiento analítico: formulación del problema, evaluación y valor esperado", "analitica"),
    "wheeler-dv": ("Donald J. Wheeler", "Understanding Variation", "2000",
                   "distinguir variación común de variación especial antes de reaccionar a un KPI", "analitica"),
    "hubbard": ("Douglas W. Hubbard", "How to Measure Anything", "2014, 3.ª ed.",
                "medir lo que parece inmedible: valor de la información y reducción de incertidumbre", "analitica"),
    "oneil": ("Cathy O'Neil", "Weapons of Math Destruction", "2016",
              "daños de los modelos opacos a escala y necesidad de auditoría", "etica"),
    "russell-norvig": ("Stuart Russell y Peter Norvig", "Artificial Intelligence: A Modern Approach", "2021, 4.ª ed.",
                       "marco formal de agentes, entornos y medidas de desempeño", "ia"),
    "ng-mlyearning": ("Andrew Ng", "Machine Learning Yearning", "2018",
                      "diagnóstico de sistemas de aprendizaje y priorización de mejoras", "ia"),
    "nist-airmf": ("NIST", "AI Risk Management Framework 1.0", "2023",
                   "gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar", "ia"),
    "iso-31000": ("ISO", "ISO 31000: Gestión del riesgo", "2018",
                  "vocabulario y proceso de gestión de riesgo aplicable a decisiones comerciales", "etica"),

    # --- Pedagogía (estándar transversal del programa) ------------------------
    "ambrose": ("Susan A. Ambrose et al.", "How Learning Works", "2010",
                "principios de aprendizaje: conocimiento previo, práctica y retroalimentación", "pedagogia"),
    "brown-mis": ("Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel", "Make It Stick", "2014",
                  "recuperación espaciada, intercalado y dificultad deseable", "pedagogia"),
    "wiggins": ("Grant Wiggins y Jay McTighe", "Understanding by Design", "2005, 2.ª ed.",
                "diseño inverso desde el desempeño observable", "pedagogia"),
    "ericsson": ("Anders Ericsson y Robert Pool", "Peak", "2016",
                 "práctica deliberada con criterios explícitos y retroalimentación inmediata", "pedagogia"),
    "ellet": ("William Ellet", "The Case Study Handbook", "2018, ed. revisada",
              "análisis de casos: problema, decisión, evidencia y recomendación", "pedagogia"),
}

# Núcleo pedagógico citado al pie de todas las clases (estándar del programa).
NUCLEO_PEDAGOGICO = ["ambrose", "brown-mis", "wiggins", "ericsson", "ellet"]


def cita(clave):
    """Cita corta: 'Autoría — *Obra* (edición)'."""
    autor, obra, edicion, _lente, _cat = LIBROS[clave]
    return "{} — *{}* ({})".format(autor, obra, edicion)


def lente(clave):
    """Para qué sirve esa lectura dentro de una decisión comercial."""
    return LIBROS[clave][3]


def autor(clave):
    return LIBROS[clave][0]


def obra(clave):
    return LIBROS[clave][1]
