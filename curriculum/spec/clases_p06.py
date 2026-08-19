# -*- coding: utf-8 -*-
"""Parte 06 — Marca, branding y comunicación estratégica."""

CLASES = [
    dict(
        n="01",
        slug="que-es-una-marca",
        titulo="Qué es una marca",
        tesis=(
            "Una marca no es un logo ni un conjunto de colores: es la estructura de memoria que existe en la "
            "cabeza de las personas y que se activa cuando aparece una necesidad. Sharp y Romaniuk lo "
            "formularon en términos operativos: la marca crece cuando aumenta su disponibilidad mental —ser "
            "recordada en la situación de compra— y su disponibilidad física —estar donde y cuando el cliente "
            "quiere comprar—. Eso convierte al branding en una inversión medible y no en un ejercicio "
            "estético."
        ),
        conceptos=[
            ("disponibilidad mental", "probabilidad de que la marca sea recordada en una situación de compra concreta"),
            ("disponibilidad física", "facilidad con que el cliente puede encontrar y comprar la marca cuando decide"),
            ("estructura de memoria", "red de asociaciones entre la marca y las situaciones, necesidades y señales que la evocan"),
            ("activo de marca", "elemento distintivo que el mercado asocia de forma única con la marca"),
        ],
        metodo=[
            "identificar las situaciones de compra en que la marca debería aparecer",
            "medir el recuerdo espontáneo en esas situaciones",
            "auditar la disponibilidad física en los canales relevantes",
            "priorizar la brecha mayor entre ambas disponibilidades",
            "definir la inversión y su métrica de seguimiento",
        ],
        senales=[
            ("recuerdo espontáneo por situación", "personas que nombran la marca ante la situación de compra, sobre personas encuestadas del segmento"),
            ("cobertura de canales", "canales relevantes donde la marca está disponible, sobre canales identificados"),
            ("participación en la consideración", "oportunidades donde la marca fue evaluada, sobre oportunidades detectadas"),
        ],
        caso=(
            "Ruta Andina cambió su identidad visual dos veces en 18 meses. En una encuesta a 60 dueños de "
            "taller, sólo 4 recordaron el nombre sin ayuda."
        ),
        limite=(
            "La marca no compensa una oferta que no resuelve el problema. Aumentar el recuerdo de un producto "
            "insatisfactorio acelera la difusión de la insatisfacción."
        ),
        libros=["sharp", "sharp2", "keller-brand", "aaker"],
        error=("Medir marca por gusto del logo",
               "Mide recuerdo espontáneo ante la situación de compra y disponibilidad en canal, no preferencia estética."),
    ),
    dict(
        n="02",
        slug="identidad-versus-imagen",
        titulo="Identidad versus imagen",
        tesis=(
            "La identidad es lo que la empresa quiere significar; la imagen es lo que el mercado efectivamente "
            "percibe. La distancia entre ambas es el diagnóstico de marca. Aaker insistió en que la identidad "
            "debe ser una guía interna con contenido —qué promete, qué representa, qué rechaza— y no un "
            "documento decorativo. Cuando la distancia es grande, el problema puede estar en la comunicación, "
            "en la experiencia o en una identidad que nunca fue realista."
        ),
        conceptos=[
            ("identidad de marca", "conjunto de asociaciones que la empresa aspira a construir y sostener"),
            ("imagen de marca", "conjunto de asociaciones que el mercado efectivamente mantiene"),
            ("brecha identidad-imagen", "distancia medida entre lo aspirado y lo percibido"),
            ("evidencia de coherencia", "experiencia real del cliente que confirma o desmiente la identidad declarada"),
        ],
        metodo=[
            "documentar la identidad con atributos y rechazos explícitos",
            "medir la imagen con una muestra del segmento",
            "calcular la brecha por atributo",
            "diagnosticar si la causa es comunicación o experiencia",
            "priorizar la intervención según costo y efecto",
        ],
        senales=[
            ("brecha por atributo", "diferencia entre la puntuación aspirada y la percibida, por atributo de identidad"),
            ("consistencia entre puntos de contacto", "puntos auditados que reflejan la identidad, sobre puntos auditados"),
            ("evolución de la brecha", "variación de la brecha entre dos olas de medición"),
        ],
        caso=(
            "Ruta Andina declara identidad «cercana y simple». Los clientes describen la experiencia como "
            "«rápida pero impersonal» y citan la falta de un contacto humano al implementar."
        ),
        limite=(
            "Una identidad puede ser aspiracional, pero no arbitraria: si contradice la experiencia que la "
            "operación puede entregar, la brecha se convierte en desconfianza."
        ),
        libros=["aaker", "keller-brand", "wheeler", "sharp2"],
        error=("Declarar identidad sin medir imagen",
               "Levanta una medición de percepción antes de definir cualquier plan de marca."),
    ),
    dict(
        n="03",
        slug="proposito-promesa-y-personalidad",
        titulo="Propósito, promesa y personalidad",
        tesis=(
            "El propósito responde para qué existe la empresa más allá de vender; la promesa, qué se "
            "compromete a entregar; la personalidad, cómo se comporta al hacerlo. Los tres deben ser "
            "verificables en la operación: un propósito que no cambia ninguna decisión es publicidad interna. "
            "La prueba de un propósito real es que alguna vez llevó a rechazar un negocio rentable."
        ),
        conceptos=[
            ("propósito", "razón de existencia que orienta decisiones más allá del resultado financiero inmediato"),
            ("promesa de marca", "compromiso concreto que el cliente puede exigir y verificar"),
            ("personalidad", "conjunto de rasgos consistentes en el trato, el tono y las decisiones"),
            ("prueba de renuncia", "decisión documentada en que el propósito llevó a rechazar una oportunidad"),
        ],
        metodo=[
            "formular propósito, promesa y personalidad por separado",
            "verificar que cada uno tenga consecuencia operativa",
            "buscar la prueba de renuncia en el historial",
            "traducir la personalidad a reglas de tono y trato",
            "auditar coherencia en tres puntos de contacto reales",
        ],
        senales=[
            ("decisiones alineadas al propósito", "decisiones documentadas que citan el propósito como criterio, por semestre"),
            ("cumplimiento de la promesa", "casos donde la promesa se cumplió sin escalamiento, sobre casos aplicables"),
            ("consistencia de tono", "piezas y respuestas que cumplen la guía de tono, sobre muestras auditadas"),
        ],
        caso=(
            "Ruta Andina declara propósito «democratizar la gestión para pymes» y su plan más barato excluye "
            "el módulo que las pymes de un local más necesitan."
        ),
        limite=(
            "El propósito no debe usarse como argumento de venta si no es verificable: el escrutinio público "
            "castiga con dureza el propósito declarado y no practicado."
        ),
        libros=["sinek", "godin", "aaker", "collins"],
        error=("Declarar propósito sin consecuencia operativa",
               "Documenta al menos una decisión concreta donde el propósito cambió el curso de acción."),
    ),
    dict(
        n="04",
        slug="naming",
        titulo="Naming",
        tesis=(
            "Un nombre debe ser pronunciable, memorable, disponible legalmente y capaz de crecer con la "
            "empresa. La disponibilidad no es un trámite posterior: en Chile, el registro de marcas ante "
            "INAPI y la verificación de dominios y redes deben ocurrir antes de invertir en identidad. Un "
            "nombre descriptivo facilita la comprensión inicial y dificulta la protección legal y la "
            "expansión; uno abstracto exige más inversión para significar algo."
        ),
        conceptos=[
            ("distintividad", "capacidad del nombre de identificar el origen comercial y de ser registrable"),
            ("memorabilidad", "facilidad con que el nombre se retiene y se reproduce correctamente"),
            ("extensibilidad", "capacidad del nombre de acompañar nuevas categorías o mercados"),
            ("disponibilidad legal", "situación registral del signo en las clases y territorios relevantes"),
        ],
        metodo=[
            "definir criterios y territorio de uso antes de generar opciones",
            "generar alternativas y filtrar por pronunciación y memoria",
            "verificar disponibilidad registral y digital",
            "probar comprensión y recuerdo con el segmento",
            "decidir y proteger el signo elegido",
        ],
        senales=[
            ("recuerdo correcto del nombre", "personas que reproducen el nombre sin error tras 24 horas, sobre expuestas"),
            ("disponibilidad registral", "clases y territorios donde el signo está disponible, sobre los requeridos"),
            ("errores de escritura en búsquedas", "búsquedas con el nombre mal escrito, sobre búsquedas de marca"),
        ],
        caso=(
            "Ruta Andina descubre que un tercero registró un signo similar en la misma clase para servicios "
            "informáticos. La campaña de marca ya está contratada."
        ),
        limite=(
            "Un buen nombre no salva una posición débil ni una experiencia deficiente; sólo reduce la fricción "
            "para construir memoria."
        ),
        libros=["wheeler", "ries-trout", "keller-brand", "heath"],
        error=("Invertir en identidad antes de verificar el registro",
               "Consulta la disponibilidad en INAPI y en dominios antes de comprometer presupuesto de marca."),
    ),
    dict(
        n="05",
        slug="identidad-verbal",
        titulo="Identidad verbal",
        tesis=(
            "La identidad verbal es el sistema que define cómo habla la marca: vocabulario propio, tono, "
            "estructuras preferidas, qué se dice y qué se evita. Es más determinante que la identidad visual "
            "porque la mayor parte de las interacciones comerciales son texto: correos, propuestas, "
            "respuestas de soporte. Una guía verbal útil da ejemplos concretos de antes y después, no "
            "adjetivos abstractos."
        ),
        conceptos=[
            ("tono", "actitud consistente con que la marca se dirige a su audiencia en cada contexto"),
            ("vocabulario propio", "términos que la marca usa y evita de forma deliberada"),
            ("guía verbal", "documento con reglas y ejemplos que permite escribir sin consultar"),
            ("consistencia verbal", "grado en que distintas personas producen textos reconocibles como de la misma marca"),
        ],
        metodo=[
            "auditar textos existentes y detectar inconsistencias",
            "definir tono por contexto: venta, soporte, cobranza, crisis",
            "fijar vocabulario preferido y prohibido",
            "escribir ejemplos de antes y después",
            "medir consistencia en una muestra tras la implementación",
        ],
        senales=[
            ("consistencia verbal auditada", "textos que cumplen la guía, sobre textos auditados por canal"),
            ("claridad percibida", "puntuación de comprensión declarada por clientes en mensajes clave"),
            ("consultas de clarificación", "respuestas del cliente pidiendo aclaración, sobre mensajes enviados"),
        ],
        caso=(
            "Los correos de cobranza de Ruta Andina son formales y fríos; los de marketing usan tuteo y "
            "emojis. El cliente recibe ambos la misma semana."
        ),
        limite=(
            "La consistencia no significa uniformidad: el tono debe adaptarse al contexto, especialmente en "
            "situaciones de reclamo o de error propio."
        ),
        libros=["handley", "heath", "wheeler", "sugarman"],
        error=("Escribir la guía verbal con adjetivos abstractos",
               "Sustituye «cercano y profesional» por ejemplos concretos de antes y después."),
    ),
    dict(
        n="06",
        slug="identidad-visual-criterios",
        titulo="Identidad visual: criterios",
        tesis=(
            "La identidad visual se evalúa por función, no por gusto: debe ser reconocible a baja atención, "
            "distintiva frente a los competidores, aplicable en todos los soportes y accesible para personas "
            "con baja visión o daltonismo. Romaniuk mostró que lo que produce reconocimiento no es la belleza "
            "sino la consistencia de los activos distintivos a lo largo del tiempo."
        ),
        conceptos=[
            ("activo distintivo", "elemento visual que el mercado asocia únicamente con la marca"),
            ("reconocimiento a baja atención", "capacidad de identificar la marca en una exposición breve y parcial"),
            ("aplicabilidad", "funcionamiento del sistema visual en todos los soportes y tamaños reales"),
            ("accesibilidad visual", "contraste y legibilidad suficientes para personas con distintas capacidades"),
        ],
        metodo=[
            "identificar los activos distintivos actuales y su nivel de asociación",
            "evaluar reconocimiento en exposición breve",
            "verificar aplicabilidad en los soportes reales",
            "comprobar contraste y accesibilidad",
            "decidir qué conservar antes de qué cambiar",
        ],
        senales=[
            ("asociación de activos", "personas que atribuyen correctamente el activo a la marca, sobre expuestas"),
            ("reconocimiento en dos segundos", "identificaciones correctas en exposición breve, sobre exposiciones"),
            ("cumplimiento de contraste", "elementos que cumplen el mínimo de contraste, sobre elementos evaluados"),
        ],
        caso=(
            "El nuevo manual visual de Ruta Andina usa texto gris claro sobre blanco. En pantallas de taller, "
            "con luz directa, el 40 % de los usuarios no logra leer el estado de las citas."
        ),
        limite=(
            "Un rediseño destruye activos acumulados. Antes de cambiar, hay que medir qué elementos ya poseen "
            "asociación y cuál sería el costo de reconstruirla."
        ),
        libros=["sharp2", "wheeler", "aaker", "krug"],
        error=("Rediseñar sin medir los activos existentes",
               "Mide la asociación de cada activo antes de decidir qué se conserva y qué se reemplaza."),
    ),
    dict(
        n="07",
        slug="arquitectura-de-marca",
        titulo="Arquitectura de marca",
        tesis=(
            "La arquitectura de marca define cuántas marcas se sostienen y cómo se relacionan: casa de marca "
            "única, marcas independientes o modelos intermedios. La decisión tiene consecuencias económicas "
            "directas: cada marca adicional exige inversión propia para construir memoria. La regla práctica "
            "para empresas medianas es conservadora: sólo se crea una marca nueva cuando el público, la "
            "promesa o el riesgo son incompatibles con la marca existente."
        ),
        conceptos=[
            ("casa de marca única", "modelo donde todos los productos se comunican bajo la misma marca"),
            ("marca respaldada", "marca propia que menciona a la marca madre como aval"),
            ("costo de construcción de marca", "inversión necesaria para instalar recuerdo y significado de una marca nueva"),
            ("riesgo de contaminación", "posibilidad de que un problema en una línea afecte a las demás bajo la misma marca"),
        ],
        metodo=[
            "mapear las marcas y submarcas activas",
            "evaluar si públicos y promesas son compatibles",
            "estimar el costo de sostener cada marca",
            "elegir el modelo y documentar las reglas de uso",
            "definir criterios para crear una marca nueva",
        ],
        senales=[
            ("inversión por marca", "gasto de comunicación asignado a cada marca, sobre inversión total"),
            ("reconocimiento por marca", "recuerdo espontáneo de cada marca en su público objetivo"),
            ("confusión entre marcas", "clientes que atribuyen erróneamente productos entre marcas, en prueba de comprensión"),
        ],
        caso=(
            "Ruta Andina lanzó «Andina Pagos» como marca separada para el módulo de cobros. Ninguna de las dos "
            "marcas alcanza recuerdo relevante y la inversión se dividió."
        ),
        limite=(
            "La arquitectura debe seguir a la estrategia y no al organigrama. Crear marcas para reflejar "
            "divisiones internas confunde al mercado sin beneficio."
        ),
        libros=["aaker", "keller-brand", "sharp2", "kotler"],
        error=("Crear marcas nuevas por razones internas",
               "Aplica el criterio de incompatibilidad de público, promesa o riesgo antes de aprobar una marca nueva."),
    ),
    dict(
        n="08",
        slug="storytelling",
        titulo="Storytelling",
        tesis=(
            "Un relato comercial no es adorno: es un mecanismo de memoria y de sentido. Heath documentó que "
            "las ideas que perduran son concretas, inesperadas, creíbles y emocionales. Aplicado a marketing, "
            "esto significa reemplazar afirmaciones abstractas por situaciones específicas con protagonista, "
            "obstáculo y consecuencia. El límite es la veracidad: un relato que exagera resultados es "
            "publicidad engañosa aunque esté bien contado."
        ),
        conceptos=[
            ("estructura narrativa", "secuencia de situación, tensión y resolución que organiza la atención"),
            ("concreción", "uso de detalles verificables en lugar de abstracciones"),
            ("credibilidad del relato", "coherencia entre lo narrado y la evidencia disponible"),
            ("protagonista correcto", "elección del cliente y no de la empresa como centro del relato"),
        ],
        metodo=[
            "elegir una situación real y documentada",
            "definir protagonista, obstáculo y consecuencia",
            "reemplazar abstracciones por detalles verificables",
            "verificar autorización y exactitud de los datos citados",
            "probar recuerdo y comprensión con el segmento",
        ],
        senales=[
            ("recuerdo del relato", "personas que reproducen los elementos centrales tras 24 horas, sobre expuestas"),
            ("atribución correcta", "personas que asocian el relato con la marca correcta, sobre expuestas"),
            ("efecto en avance comercial", "diferencia de avance de etapa entre materiales con relato y sin relato"),
        ],
        caso=(
            "El caso de éxito publicado por Ruta Andina cita «40 % más de ingresos» sin indicar periodo, base "
            "de comparación ni autorización del cliente."
        ),
        limite=(
            "Todo testimonio o caso requiere autorización del cliente y exactitud verificable. Los datos deben "
            "poder acreditarse ante una fiscalización o un reclamo."
        ),
        libros=["heath", "godin", "sugarman", "handley"],
        error=("Publicar resultados sin base de comparación ni autorización",
               "Documenta periodo, base, método de cálculo y autorización escrita antes de publicar un caso."),
    ),
    dict(
        n="09",
        slug="brand-equity",
        titulo="Brand equity",
        tesis=(
            "El valor de marca es el efecto diferencial que el conocimiento de la marca produce en la "
            "respuesta del cliente. Keller lo estructuró en niveles: notoriedad, significado, respuesta y "
            "resonancia. Su manifestación económica es concreta: menor costo de adquisición, mayor tasa de "
            "conversión, prima de precio sostenida y mayor tolerancia ante un error. Medirlo exige separar el "
            "efecto de la marca del efecto de la promoción vigente."
        ),
        conceptos=[
            ("notoriedad", "nivel y calidad del recuerdo de la marca en su categoría"),
            ("significado asociado", "atributos y beneficios que el mercado vincula con la marca"),
            ("prima de precio", "diferencia de precio sostenible frente a alternativas equivalentes"),
            ("resonancia", "intensidad del vínculo que produce lealtad y recomendación activa"),
        ],
        metodo=[
            "medir notoriedad y asociaciones con muestra del segmento",
            "estimar la prima de precio observada frente a competidores",
            "aislar el efecto de promociones vigentes",
            "seguir la evolución con olas comparables",
            "vincular la métrica de marca con costo de adquisición",
        ],
        senales=[
            ("costo de adquisición por origen de marca", "costo por cliente ganado en tráfico de marca frente a tráfico genérico"),
            ("prima de precio sostenida", "diferencia porcentual de precio efectivo frente al competidor, en el tiempo"),
            ("tasa de recomendación activa", "clientes que originaron una referencia en 12 meses, sobre clientes activos"),
        ],
        caso=(
            "Ruta Andina no distingue en su medición el tráfico de marca del genérico, por lo que atribuye a "
            "sus campañas conversiones de personas que ya la buscaban por nombre."
        ),
        limite=(
            "El valor de marca se construye en años y se mide con ruido. Exigir demostración trimestral de "
            "retorno induce a desmantelar la inversión de largo plazo."
        ),
        libros=["keller-brand", "aaker", "binet-field", "sharp"],
        error=("Atribuir a campañas el tráfico de marca",
               "Separa tráfico de marca y genérico en la medición antes de calcular retorno."),
    ),
    dict(
        n="10",
        slug="confianza-y-reputacion",
        titulo="Confianza y reputación",
        tesis=(
            "La reputación es el juicio acumulado del mercado sobre la fiabilidad de una empresa; la "
            "confianza es la disposición a asumir riesgo con ella. Se construyen con consistencia y se "
            "destruyen con incoherencia visible, especialmente en el manejo de errores. La respuesta ante una "
            "falla propia informa más sobre la empresa que cualquier campaña: reconocer, reparar y prevenir "
            "produce más confianza que negar."
        ),
        conceptos=[
            ("reputación", "juicio acumulado del mercado basado en el comportamiento observado en el tiempo"),
            ("manejo de errores", "protocolo de reconocimiento, reparación y prevención ante una falla propia"),
            ("coherencia observable", "correspondencia entre lo declarado y lo que el cliente experimenta"),
            ("costo de recuperación", "esfuerzo necesario para restablecer la confianza después de un incidente"),
        ],
        metodo=[
            "monitorear señales públicas de reputación",
            "definir el protocolo de respuesta ante incidentes",
            "reconocer y reparar antes de comunicar",
            "documentar la causa raíz y la prevención",
            "medir la recuperación en indicadores de confianza",
        ],
        senales=[
            ("tiempo de respuesta ante incidente", "horas entre la detección del incidente y la comunicación al cliente afectado"),
            ("tasa de reclamos resueltos en primera instancia", "reclamos cerrados sin escalamiento, sobre reclamos recibidos"),
            ("evolución de menciones negativas", "variación del volumen de menciones negativas tras el incidente"),
        ],
        caso=(
            "Una caída de ocho horas dejó a 120 clientes de Ruta Andina sin agenda. La empresa no comunicó "
            "nada hasta que los reclamos aparecieron en un grupo gremial."
        ),
        limite=(
            "La comunicación no sustituye la reparación. Un protocolo impecable sobre un problema no resuelto "
            "acelera la pérdida de confianza."
        ),
        libros=["reichheld", "godin", "dixon-effort", "cialdini"],
        error=("Comunicar antes de reparar",
               "Define el protocolo: contención, reparación, comunicación y prevención documentada, en ese orden."),
    ),
    dict(
        n="11",
        slug="employer-y-personal-branding",
        titulo="Employer branding y marca personal",
        tesis=(
            "La marca empleadora y la marca personal de quienes venden son activos comerciales reales, "
            "especialmente en B2B: el comprador investiga a la empresa y a la persona antes de responder. "
            "Ambas se construyen con evidencia pública consistente —contenido útil, trayectoria verificable, "
            "trato coherente— y ambas tienen un límite: no pueden sostener una promesa que la empresa no "
            "cumple internamente."
        ),
        conceptos=[
            ("marca empleadora", "percepción del mercado laboral sobre cómo es trabajar en la empresa"),
            ("marca personal comercial", "reputación pública de quien vende, construida con evidencia verificable"),
            ("coherencia interna-externa", "correspondencia entre la promesa al mercado laboral y la experiencia real del equipo"),
            ("prueba pública", "contenido o antecedente verificable que sostiene la reputación declarada"),
        ],
        metodo=[
            "auditar la presencia pública actual de la empresa y del equipo comercial",
            "verificar la coherencia con la experiencia interna real",
            "definir qué evidencia pública se producirá y con qué frecuencia",
            "acordar límites de uso de datos y de clientes",
            "medir efecto en respuesta comercial y en atracción de talento",
        ],
        senales=[
            ("tasa de respuesta por perfil", "respuestas obtenidas, sobre contactos realizados, comparada entre perfiles con y sin presencia pública"),
            ("origen de candidatos", "postulaciones espontáneas, sobre postulaciones totales, por periodo"),
            ("rotación temprana", "salidas antes de seis meses, sobre incorporaciones del periodo"),
        ],
        caso=(
            "Ruta Andina publica que es «el mejor lugar para crecer» y su rotación comercial anual es 62 %. "
            "Dos ex vendedores lo comentaron públicamente."
        ),
        limite=(
            "La marca personal del vendedor puede volverse un riesgo de concentración: si el activo es la "
            "persona y no la empresa, la salida se lleva la relación."
        ),
        libros=["godin", "handley", "collins", "lencioni"],
        error=("Comunicar cultura que no existe",
               "Verifica indicadores internos de rotación y clima antes de publicar promesas de marca empleadora."),
    ),
    dict(
        n="12",
        slug="coherencia-omnicanal",
        titulo="Coherencia omnicanal",
        tesis=(
            "El cliente no distingue canales: distingue empresas. Si el precio de la tienda difiere del "
            "marketplace, si el correo promete algo que soporte desconoce, o si el vendedor ofrece "
            "condiciones que el sistema no permite, el cliente concluye desorden. La coherencia omnicanal es "
            "un problema operativo antes que comunicacional: exige una fuente única de precios, condiciones y "
            "estado del cliente."
        ),
        conceptos=[
            ("fuente única de verdad", "sistema donde reside el dato válido de precio, condición y estado del cliente"),
            ("continuidad de la conversación", "capacidad de retomar la interacción sin que el cliente repita información"),
            ("incoherencia visible", "diferencia entre canales que el cliente puede detectar y que erosiona la confianza"),
            ("gobierno de canal", "reglas que definen qué puede prometerse y modificarse en cada canal"),
        ],
        metodo=[
            "auditar precio, condiciones y mensajes en todos los canales",
            "identificar la fuente única de verdad para cada dato",
            "corregir las incoherencias visibles primero",
            "definir reglas de gobierno por canal",
            "medir la recurrencia de incoherencias",
        ],
        senales=[
            ("incoherencias detectadas por auditoría", "diferencias encontradas entre canales, sobre elementos auditados"),
            ("consultas por información contradictoria", "contactos de clientes citando contradicciones, sobre contactos totales"),
            ("tiempo de propagación de un cambio", "horas entre un cambio de precio o condición y su reflejo en todos los canales"),
        ],
        caso=(
            "El precio del lector de tarjetas de Ruta Andina es CLP 89.900 en su tienda y CLP 79.900 en "
            "marketplace. Los clientes lo notaron y el equipo de soporte improvisa respuestas."
        ),
        limite=(
            "La coherencia no obliga a precios idénticos: los canales tienen costos distintos. Lo que exige es "
            "que las diferencias sean explicables y no arbitrarias."
        ),
        libros=["chaffey", "flint", "krug", "kotler"],
        error=("Corregir la comunicación sin corregir el dato",
               "Establece la fuente única de verdad antes de rediseñar mensajes."),
    ),
    dict(
        n="13",
        slug="medicion-de-marca",
        titulo="Medición de marca",
        tesis=(
            "Medir marca exige indicadores que no se confundan con actividad de campaña: notoriedad "
            "espontánea y asistida, asociación de atributos, consideración, preferencia y prima de precio. "
            "Binet y Field mostraron que las métricas de corto plazo sobrerrepresentan la activación y "
            "subestiman la construcción de marca, lo que sesga la asignación de presupuesto hacia lo "
            "inmediato."
        ),
        conceptos=[
            ("notoriedad espontánea", "proporción que nombra la marca sin ayuda ante la categoría o la situación"),
            ("consideración", "proporción que incluiría la marca en su conjunto de evaluación"),
            ("ola de medición", "levantamiento periódico con método idéntico que permite comparar en el tiempo"),
            ("efecto de largo plazo", "resultado que se manifiesta más allá del periodo de la campaña"),
        ],
        metodo=[
            "definir los indicadores de marca y su método",
            "establecer la línea base con la primera ola",
            "mantener método idéntico entre olas",
            "separar efecto de marca y efecto de activación",
            "vincular la evolución con costo de adquisición y precio",
        ],
        senales=[
            ("notoriedad espontánea por ola", "proporción que nombra la marca sin ayuda, por ola y por segmento"),
            ("consideración por ola", "proporción que incluiría la marca en su evaluación, por ola"),
            ("relación marca-costo de adquisición", "correlación observada entre indicadores de marca y costo por cliente ganado"),
        ],
        caso=(
            "Ruta Andina mide su marca sólo con seguidores y alcance en redes. No tiene línea base de "
            "notoriedad ni forma de saber si la inversión mueve algo."
        ),
        limite=(
            "Las mediciones de marca tienen ruido y costo. En empresas pequeñas conviene una ola semestral "
            "acotada antes que ninguna medición o que un tablero de vanidad."
        ),
        libros=["binet-field", "keller-brand", "sharp", "kaushik"],
        error=("Usar métricas de redes como métricas de marca",
               "Levanta notoriedad y consideración con método comparable entre olas."),
    ),
    dict(
        n="14",
        slug="brand-book-minimo-viable",
        titulo="Brand book mínimo viable",
        tesis=(
            "Esta clase integra la parte en un manual breve y utilizable: posicionamiento, promesa, activos "
            "distintivos, guía verbal, reglas de aplicación y sistema de medición. La prueba de calidad es "
            "operativa: una persona nueva debe poder producir una pieza correcta sin preguntar, y una agencia "
            "externa debe poder ejecutar sin reinterpretar."
        ),
        conceptos=[
            ("manual operativo de marca", "documento breve que permite producir piezas correctas sin consulta"),
            ("regla de aplicación", "instrucción concreta sobre uso de activos en un soporte específico"),
            ("sistema de medición de marca", "conjunto de indicadores, método y periodicidad definidos"),
            ("prueba de producción", "verificación de que una persona ajena produce una pieza conforme"),
        ],
        metodo=[
            "consolidar posicionamiento, promesa y activos",
            "escribir reglas de aplicación con ejemplos",
            "incluir la guía verbal con antes y después",
            "definir el sistema de medición y su periodicidad",
            "ejecutar la prueba de producción con alguien ajeno",
        ],
        senales=[
            ("resultado de la prueba de producción", "piezas conformes producidas sin consulta, sobre piezas solicitadas"),
            ("tiempo de producción de una pieza", "horas desde el encargo hasta la pieza aprobada, antes y después del manual"),
            ("consistencia auditada", "piezas conformes al manual, sobre piezas auditadas por trimestre"),
        ],
        caso=(
            "Ruta Andina trabajará con una agencia externa el próximo trimestre. Hoy no existe documento que "
            "permita ejecutar sin reuniones de interpretación."
        ),
        limite=(
            "Un manual extenso no se usa. Si supera lo que una persona puede consultar en cinco minutos, hay "
            "que producir una versión operativa de una página."
        ),
        libros=["wheeler", "aaker", "handley", "sharp2"],
        error=("Producir un manual extenso sin prueba de producción",
               "Entrega el manual a una persona ajena y verifica si produce una pieza conforme sin ayuda."),
    ),
]
