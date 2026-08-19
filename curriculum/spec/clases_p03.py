# -*- coding: utf-8 -*-
"""Parte 03 — Investigación de mercados e inteligencia competitiva."""

CLASES = [
    dict(
        n="01",
        slug="preguntas-de-investigacion-y-decisiones",
        titulo="Preguntas de investigación y decisiones",
        tesis=(
            "Toda investigación empieza por una decisión pendiente, no por una curiosidad. Si nadie puede "
            "nombrar qué haría distinto según el resultado, el estudio no debería financiarse. Hubbard "
            "propone una prueba económica: estimar el valor de la información antes de comprarla, es decir, "
            "cuánto se pierde por decidir sin ella. Esa disciplina evita el patrón más común en pymes y "
            "startups: encuestas largas que confirman lo que el equipo ya creía y que no cambian ninguna "
            "asignación de recursos."
        ),
        conceptos=[
            ("decisión pendiente", "elección concreta con alternativas definidas que la investigación debe informar"),
            ("pregunta de investigación", "formulación que puede responderse con evidencia y que discrimina entre alternativas"),
            ("valor de la información", "reducción esperada de pérdida por decidir con evidencia en lugar de sin ella"),
            ("umbral de suficiencia", "nivel de evidencia a partir del cual seguir investigando ya no cambia la decisión"),
        ],
        metodo=[
            "escribir la decisión pendiente y sus alternativas",
            "declarar qué resultado favorecería a cada alternativa",
            "estimar el costo de equivocarse en esa decisión",
            "definir el umbral de evidencia suficiente",
            "elegir el método más barato que alcance ese umbral",
        ],
        senales=[
            ("decisiones modificadas por investigación", "decisiones cuyo curso cambió tras el estudio, sobre estudios realizados en el periodo"),
            ("costo por estudio frente a valor en juego", "costo directo del estudio dividido por el monto de la decisión que informa"),
            ("tiempo entre pregunta y respuesta", "días entre la formulación de la pregunta y la entrega de evidencia utilizable"),
        ],
        caso=(
            "Ruta Andina encargó un estudio de mercado de CLP 6 millones sobre «percepción de marca». El "
            "informe llegó a los tres meses, nadie identificó qué decisión cambiaba y quedó archivado."
        ),
        limite=(
            "Algunas investigaciones exploratorias no informan una decisión inmediata y aun así son valiosas para "
            "detectar problemas no formulados. La regla del valor de la información aplica al gasto grande, no a "
            "la conversación con clientes."
        ),
        libros=["hubbard", "malhotra", "fitzpatrick", "provost"],
        error=("Financiar investigación sin decisión asociada",
               "Exige por escrito qué alternativa se descartaría según cada resultado posible antes de aprobar el gasto."),
    ),
    dict(
        n="02",
        slug="fuentes-primarias-y-secundarias",
        titulo="Fuentes primarias y secundarias",
        tesis=(
            "Las fuentes secundarias —informes sectoriales, estadísticas oficiales, estudios publicados— son "
            "baratas y rápidas, pero fueron construidas para responder la pregunta de otro. Las fuentes "
            "primarias responden la pregunta propia y cuestan tiempo. El error frecuente no es elegir mal sino "
            "no declarar la diferencia: citar una cifra de un informe sin registrar quién la produjo, con qué "
            "muestra y en qué año. En Chile hay fuentes oficiales de calidad —INE, SII, Banco Central, "
            "SUBTEL— cuya metodología está publicada y debe leerse antes de citar."
        ),
        conceptos=[
            ("fuente primaria", "evidencia recogida directamente por la empresa para su propia pregunta"),
            ("fuente secundaria", "dato producido por un tercero con un propósito y una metodología ajenos"),
            ("trazabilidad de la cifra", "registro de origen, metodología, muestra, periodo y fecha de consulta"),
            ("vigencia del dato", "periodo durante el cual la cifra sigue siendo representativa del fenómeno"),
        ],
        metodo=[
            "buscar primero si la pregunta ya fue respondida por una fuente confiable",
            "leer la metodología antes de usar la cifra",
            "registrar origen, muestra, periodo y fecha de consulta",
            "identificar qué parte de la pregunta sigue sin respuesta",
            "diseñar la recolección primaria sólo para ese remanente",
        ],
        senales=[
            ("cifras citadas con trazabilidad completa", "cifras con origen, metodología y fecha registrados, sobre cifras usadas en el informe"),
            ("antigüedad mediana de las fuentes", "meses transcurridos desde la publicación de las fuentes citadas"),
            ("costo evitado por reutilización", "estimación del costo de recolección primaria evitado al usar fuentes existentes"),
        ],
        caso=(
            "El plan de Ruta Andina afirma que «el 78 % de las pymes chilenas no está digitalizada». Nadie "
            "sabe de dónde salió el dato ni de qué año es; el número circula en tres presentaciones distintas."
        ),
        limite=(
            "Las fuentes oficiales tienen rezago y niveles de agregación que pueden no servir para un segmento "
            "estrecho. Su autoridad no las hace aplicables a cualquier pregunta."
        ),
        libros=["malhotra", "hubbard", "provost", "porter"],
        error=("Citar cifras sin metodología ni fecha",
               "Incluye en cada cifra origen, muestra, periodo y fecha de consulta, o elimínala del informe."),
    ),
    dict(
        n="03",
        slug="diseno-de-entrevistas",
        titulo="Diseño de entrevistas",
        tesis=(
            "La entrevista es la herramienta más barata y la más fácil de arruinar. Fitzpatrick formuló la "
            "regla central: preguntar por comportamiento pasado y hechos concretos, nunca por opiniones sobre "
            "el futuro ni por la propia idea. «¿Comprarías esto?» genera cortesía; «¿qué hiciste la última vez "
            "que tuviste este problema y cuánto te costó?» genera datos. Una buena entrevista termina con "
            "hechos, no con validación emocional."
        ),
        conceptos=[
            ("pregunta conductual", "pregunta sobre lo que la persona efectivamente hizo, cuándo y con qué consecuencia"),
            ("sesgo de complacencia", "tendencia del entrevistado a responder lo que cree que el entrevistador quiere oír"),
            ("compromiso verificable", "señal costosa —tiempo, dinero, presentación a un jefe— que confirma interés real"),
            ("saturación", "punto en que nuevas entrevistas dejan de aportar categorías nuevas"),
        ],
        metodo=[
            "definir qué hipótesis debe refutar la entrevista",
            "escribir preguntas sobre comportamiento pasado",
            "eliminar preguntas que anticipan la respuesta deseada",
            "buscar un compromiso verificable al cierre",
            "registrar hechos y citas textuales, no interpretaciones",
        ],
        senales=[
            ("proporción de hechos sobre opiniones", "afirmaciones sobre comportamiento pasado registradas, sobre afirmaciones totales por entrevista"),
            ("tasa de compromiso obtenido", "entrevistados que aceptaron un siguiente paso costoso, sobre entrevistas realizadas"),
            ("entrevistas hasta saturación", "número de entrevistas tras el cual no aparecen categorías nuevas, por segmento"),
        ],
        caso=(
            "El equipo de Ruta Andina entrevistó a 20 dueños de taller y todos dijeron que la idea «se ve "
            "buenísima». Ninguno aceptó agendar una prueba y el equipo reportó la investigación como "
            "validación."
        ),
        limite=(
            "Las entrevistas no dimensionan mercado ni miden frecuencia poblacional. Sirven para descubrir "
            "mecanismos y vocabulario, no para estimar cuántos hay."
        ),
        libros=["fitzpatrick", "portigal", "blank", "malhotra"],
        error=("Presentar la idea antes de conocer el comportamiento",
               "Deja la presentación de la solución para el final y sólo después de haber registrado hechos."),
    ),
    dict(
        n="04",
        slug="diseno-de-encuestas",
        titulo="Diseño de encuestas",
        tesis=(
            "Una encuesta traduce un concepto en preguntas y una escala en un número. Cada traducción "
            "introduce error: preguntas que sugieren respuesta, escalas sin punto medio claro, opciones que no "
            "cubren todos los casos, orden que arrastra. La encuesta sirve para medir prevalencia una vez que "
            "el vocabulario y las categorías fueron descubiertos cualitativamente; usarla antes produce "
            "números precisos sobre preguntas equivocadas."
        ),
        conceptos=[
            ("validez de constructo", "grado en que la pregunta mide efectivamente el concepto que dice medir"),
            ("pregunta sesgada", "formulación que orienta la respuesta por su redacción, orden u opciones"),
            ("escala", "conjunto ordenado de opciones con significado uniforme para todos los respondentes"),
            ("tasa de respuesta", "proporción de personas invitadas que completaron el instrumento"),
        ],
        metodo=[
            "definir el concepto a medir y su definición operacional",
            "redactar preguntas neutras y probarlas con cinco personas",
            "elegir escalas consistentes y evitar preguntas dobles",
            "pilotear y depurar antes de terreno",
            "documentar tasa de respuesta y perfil de quienes no respondieron",
        ],
        senales=[
            ("tasa de respuesta", "cuestionarios completos, sobre invitaciones enviadas, por canal"),
            ("tasa de abandono por pregunta", "abandonos en cada pregunta, sobre respondentes que llegaron a ella"),
            ("consistencia interna", "correlación entre preguntas que miden el mismo constructo"),
        ],
        caso=(
            "La encuesta de satisfacción de Ruta Andina pregunta «¿qué tan satisfecho estás con nuestra "
            "excelente atención?». El 92 % responde positivamente y el churn no baja."
        ),
        limite=(
            "Una encuesta bien diseñada con muestra sesgada sigue siendo inútil. El diseño del instrumento no "
            "compensa un problema de muestreo."
        ),
        libros=["malhotra", "hubbard", "provost", "kaushik"],
        error=("Preguntar y medir sin haber descubierto las categorías",
               "Ejecuta entrevistas cualitativas antes de fijar las opciones de respuesta de la encuesta."),
    ),
    dict(
        n="05",
        slug="muestreo-y-sesgos",
        titulo="Muestreo y sesgos",
        tesis=(
            "El error más caro de la investigación comercial no está en el análisis sino en quién quedó "
            "dentro de la muestra. Encuestar a la base de clientes actuales para entender por qué el mercado "
            "no compra es un ejemplo de sesgo de supervivencia. La muestra por conveniencia no es "
            "necesariamente inválida, pero obliga a declarar sus límites y a no extrapolar a la población. Un "
            "informe honesto describe a quién representa y a quién no."
        ),
        conceptos=[
            ("marco muestral", "lista o mecanismo desde el cual se seleccionan los participantes"),
            ("sesgo de selección", "diferencia sistemática entre quienes participan y quienes no, relacionada con la variable estudiada"),
            ("sesgo de supervivencia", "error de observar sólo los casos que permanecieron y concluir sobre todos"),
            ("no respuesta informativa", "situación en que quienes no responden difieren sistemáticamente de quienes sí responden"),
        ],
        metodo=[
            "definir la población objetivo con precisión",
            "describir el marco muestral y sus exclusiones",
            "elegir el método de selección y justificarlo",
            "estimar quién queda fuera y cómo podría diferir",
            "declarar los límites de extrapolación en el informe",
        ],
        senales=[
            ("cobertura del marco muestral", "unidades de la población objetivo presentes en el marco, sobre población estimada"),
            ("diferencia entre respondentes y no respondentes", "comparación de variables conocidas entre ambos grupos"),
            ("intervalo de confianza declarado", "amplitud del intervalo de confianza, en puntos porcentuales, sobre cada estimación principal"),
        ],
        caso=(
            "Ruta Andina concluye que «el precio no es un problema» a partir de una encuesta enviada sólo a "
            "clientes activos. Los que se fueron por precio, por definición, no estaban en la lista."
        ),
        limite=(
            "En segmentos B2B pequeños la aleatorización pura suele ser imposible. La alternativa correcta no es "
            "fingirla sino documentar el criterio de selección y sus consecuencias."
        ),
        libros=["malhotra", "provost", "hubbard", "kohavi"],
        error=("Extrapolar desde la base de clientes al mercado",
               "Incluye no clientes y clientes perdidos en el marco muestral cuando la pregunta es sobre el mercado."),
    ),
    dict(
        n="06",
        slug="investigacion-cualitativa",
        titulo="Investigación cualitativa",
        tesis=(
            "La investigación cualitativa responde preguntas de mecanismo: por qué ocurre, cómo se decide, qué "
            "significa para el cliente. Su rigor no viene del tamaño de muestra sino del método: registro "
            "textual, codificación de categorías, contraste entre analistas y búsqueda deliberada de casos que "
            "contradigan la interpretación. Presentada como porcentaje —«el 70 % de los entrevistados dijo»— "
            "pierde su valor y adquiere una precisión que no tiene."
        ),
        conceptos=[
            ("codificación", "proceso de asignar categorías a fragmentos de texto para hacer comparables los hallazgos"),
            ("caso negativo", "observación que contradice la interpretación emergente y obliga a revisarla"),
            ("triangulación", "contraste de un hallazgo con una fuente o método distinto"),
            ("insight accionable", "hallazgo que cambia una decisión concreta y puede formularse como hipótesis"),
        ],
        metodo=[
            "registrar la evidencia en su forma original",
            "codificar de forma abierta y luego consolidar categorías",
            "buscar activamente casos negativos",
            "triangular con datos operativos o cuantitativos",
            "formular hipótesis verificables a partir de las categorías",
        ],
        senales=[
            ("número de categorías estables", "categorías que se repiten en al menos tres fuentes distintas"),
            ("casos negativos documentados", "observaciones contradictorias registradas, sobre hallazgos principales"),
            ("acuerdo entre analistas", "coincidencia en la codificación de una misma muestra entre dos personas"),
        ],
        caso=(
            "Ruta Andina resume 18 entrevistas en tres bullets sin citas ni codificación. Cuando alguien "
            "pregunta de dónde salió una conclusión, no hay forma de reconstruirla."
        ),
        limite=(
            "Lo cualitativo no mide magnitud. Una categoría fuerte en entrevistas puede ser marginal en la "
            "población y requiere verificación cuantitativa antes de dimensionar inversión."
        ),
        libros=["portigal", "fitzpatrick", "malhotra", "christensen"],
        error=("Reportar hallazgos cualitativos como porcentajes",
               "Presenta frecuencia de categorías y citas textuales; reserva los porcentajes para muestras diseñadas."),
    ),
    dict(
        n="07",
        slug="investigacion-cuantitativa",
        titulo="Investigación cuantitativa",
        tesis=(
            "La investigación cuantitativa responde preguntas de magnitud y de relación: cuántos, con qué "
            "frecuencia, qué tan asociado. Su valor depende de tres cosas que suelen omitirse en informes "
            "comerciales: definición operacional de la variable, tamaño de muestra suficiente y declaración de "
            "incertidumbre. Un número sin intervalo ni denominador es retórica con apariencia de dato."
        ),
        conceptos=[
            ("variable operacionalizada", "concepto traducido en una medición reproducible con unidad y fuente"),
            ("tamaño de muestra suficiente", "número de observaciones necesario para detectar el efecto que importaría"),
            ("incertidumbre declarada", "rango dentro del cual se espera que esté el valor real"),
            ("asociación frente a causalidad", "distinción entre variables que se mueven juntas y variables donde una produce la otra"),
        ],
        metodo=[
            "definir las variables y su forma de medición",
            "calcular el tamaño de muestra según el efecto mínimo relevante",
            "recolectar con procedimiento uniforme",
            "reportar estimación e incertidumbre",
            "distinguir explícitamente asociación de causalidad",
        ],
        senales=[
            ("potencia del estudio", "probabilidad de detectar el efecto mínimo relevante con la muestra disponible, calculada antes de recolectar"),
            ("proporción de resultados con intervalo reportado", "estimaciones con intervalo de confianza, sobre estimaciones presentadas"),
            ("consistencia entre olas", "diferencia entre mediciones sucesivas del mismo indicador con el mismo método"),
        ],
        caso=(
            "El informe de Ruta Andina afirma que «los clientes del sur convierten 15 % más». La diferencia "
            "proviene de 11 observaciones y ningún intervalo acompaña la cifra."
        ),
        limite=(
            "Más muestra no arregla una variable mal definida. Precisión sin validez sólo produce error con más "
            "decimales."
        ),
        libros=["provost", "kohavi", "malhotra", "wheeler-dv"],
        error=("Reportar diferencias sin denominador ni incertidumbre",
               "Acompaña toda comparación con tamaño de muestra e intervalo, o preséntala como observación exploratoria."),
    ),
    dict(
        n="08",
        slug="tam-sam-y-som",
        titulo="TAM, SAM y SOM",
        tesis=(
            "El dimensionamiento de mercado no busca un número impresionante sino una estimación defendible "
            "con supuestos visibles. TAM es el mercado total del problema; SAM el que la oferta puede servir "
            "con su modelo actual; SOM el que puede alcanzarse con la capacidad comercial existente en un "
            "horizonte definido. El método correcto es bottom-up —unidades por precio, con fuentes— y el "
            "resultado correcto es un rango con escenarios, no una cifra única."
        ),
        conceptos=[
            ("TAM", "gasto total anual del universo que tiene el problema, si toda la solución fuera provista"),
            ("SAM", "porción del TAM alcanzable con el modelo, la geografía y el idioma actuales"),
            ("SOM", "porción del SAM capturable con la capacidad comercial y el presupuesto disponibles en el horizonte definido"),
            ("estimación bottom-up", "cálculo construido desde unidades observables y precios reales, con fuente por variable"),
        ],
        metodo=[
            "definir la unidad de consumo y su precio realista",
            "estimar el número de unidades con fuentes citadas",
            "acotar por modelo, geografía y capacidad",
            "construir escenarios conservador, base y optimista",
            "declarar los tres supuestos que más mueven el resultado",
        ],
        senales=[
            ("dispersión entre escenarios", "diferencia porcentual entre escenario conservador y optimista"),
            ("supuestos críticos identificados", "variables cuyo cambio de 10 % altera el resultado en más de 20 %"),
            ("cobertura de fuentes", "variables del cálculo con fuente citada, sobre variables totales del modelo"),
        ],
        caso=(
            "El plan de Ruta Andina declara un TAM de «USD 400 millones» tomado de un informe regional. Nadie "
            "puede explicar qué unidades incluye ni si considera empresas que ya tienen solución."
        ),
        limite=(
            "El TAM no predice ingreso: una empresa puede tener un mercado enorme y cero capacidad de "
            "alcanzarlo. Para decisiones operativas, el SOM y su supuesto de capacidad importan más."
        ),
        libros=["moore", "hubbard", "malhotra", "osterwalder-bmg"],
        error=("Estimar top-down desde un informe sectorial",
               "Reconstruye la cifra bottom-up con unidades y precios verificables antes de usarla para decidir."),
    ),
    dict(
        n="09",
        slug="benchmarking-competitivo",
        titulo="Benchmarking competitivo",
        tesis=(
            "Comparar con competidores es útil para detectar brechas y peligroso para definir estrategia: si "
            "todos copian a todos, la industria converge y el margen se erosiona. Porter advirtió que la "
            "eficacia operativa no es estrategia; alcanzar la frontera de las mejores prácticas es necesario "
            "pero no diferencia. El benchmarking correcto compara elementos específicos con criterio "
            "explícito y separa lo que es tabla de entrada de lo que es diferencia real."
        ),
        conceptos=[
            ("tabla de entrada", "atributo que todos los competidores ofrecen y cuya ausencia descalifica"),
            ("punto de diferencia", "atributo donde la empresa supera de forma perceptible y sostenible a las alternativas"),
            ("brecha de desempeño", "diferencia medida entre la empresa y el mejor competidor en un atributo concreto"),
            ("costo de cierre de brecha", "recursos necesarios para alcanzar el nivel del competidor en ese atributo"),
        ],
        metodo=[
            "elegir los atributos que el cliente usa para decidir",
            "medir a la empresa y a los competidores en cada uno",
            "clasificar cada atributo como tabla de entrada o diferencia",
            "estimar el costo de cerrar cada brecha relevante",
            "decidir dónde igualar y dónde diferenciarse deliberadamente",
        ],
        senales=[
            ("brecha por atributo crítico", "diferencia medida entre la empresa y el mejor competidor en cada atributo de decisión"),
            ("tasa de pérdida por atributo", "negocios perdidos donde el atributo fue citado como razón, sobre pérdidas totales"),
            ("costo estimado de paridad", "inversión requerida para alcanzar el nivel competitivo en los atributos de tabla de entrada"),
        ],
        caso=(
            "Ruta Andina compara funcionalidades con dos competidores y concluye que necesita 14 desarrollos. "
            "Ninguno de los 14 aparece entre las razones de compra citadas por sus clientes ganados."
        ),
        limite=(
            "El benchmarking mira el presente del competidor, no su dirección. Igualar hoy puede significar "
            "llegar tarde mañana si el competidor está construyendo otra cosa."
        ),
        libros=["porter", "porter-hbr", "kim-mauborgne", "ries-trout"],
        error=("Convertir el benchmarking en un plan de desarrollo",
               "Filtra los atributos por su presencia en las razones de compra y de pérdida documentadas."),
    ),
    dict(
        n="10",
        slug="analisis-de-competencia",
        titulo="Análisis de competencia",
        tesis=(
            "Analizar competencia no es listar competidores: es entender su modelo económico, sus "
            "restricciones y sus movimientos probables. Un competidor con capital de riesgo y presión de "
            "crecimiento se comportará distinto de uno familiar con caja propia. Porter estructuró el análisis "
            "en fuerzas —proveedores, compradores, entrantes, sustitutos y rivalidad— que explican por qué "
            "algunas industrias son rentables y otras no, independientemente del esfuerzo individual."
        ),
        conceptos=[
            ("modelo económico del competidor", "forma en que gana dinero, su estructura de costos y su presión de retorno"),
            ("restricción del competidor", "limitación de capital, capacidad, contrato o tecnología que acota lo que puede hacer"),
            ("movimiento probable", "acción esperable del competidor dada su situación, no la que sería óptima en abstracto"),
            ("intensidad competitiva", "grado en que la rivalidad erosiona el margen disponible en la categoría"),
        ],
        metodo=[
            "reconstruir el modelo económico de los dos competidores principales",
            "identificar sus restricciones observables",
            "anticipar sus movimientos probables en 12 meses",
            "evaluar el efecto de esos movimientos sobre el margen propio",
            "definir la respuesta y su condición de activación",
        ],
        senales=[
            ("participación en negocios enfrentados", "negocios ganados frente a cada competidor, sobre negocios donde estuvo presente"),
            ("cambios de precio del competidor", "variaciones de lista detectadas por trimestre y su efecto en la tasa de descuento propia"),
            ("velocidad de respuesta", "días entre un movimiento del competidor y la respuesta documentada de la empresa"),
        ],
        caso=(
            "El competidor regional de Ruta Andina levantó capital y bajó precios 30 %. La reacción propuesta "
            "es igualar el precio, sin considerar que el competidor puede sostener pérdidas y Ruta Andina no."
        ),
        limite=(
            "La inteligencia competitiva tiene límites legales y éticos: no incluye obtener información "
            "confidencial por medios engañosos ni coordinar precios, práctica sancionada por la libre "
            "competencia en Chile."
        ),
        libros=["porter", "rumelt", "kim-mauborgne", "porter-hbr"],
        error=("Reaccionar a un precio sin comparar estructuras de costo",
               "Modela cuánto tiempo puede sostener cada parte esa política antes de responder."),
    ),
    dict(
        n="11",
        slug="social-listening-y-senales-de-mercado",
        titulo="Social listening y señales de mercado",
        tesis=(
            "Las conversaciones públicas —reseñas, foros, grupos gremiales, reclamos— son una fuente continua "
            "y barata de vocabulario, objeciones y disparadores. Su límite es la representatividad: quienes "
            "escriben públicamente son una minoría con motivación intensa, generalmente negativa o "
            "entusiasta. El uso correcto es descubrir categorías y detectar cambios; el uso incorrecto es "
            "medir prevalencia o tratar tres comentarios como tendencia."
        ),
        conceptos=[
            ("señal débil", "indicio temprano de un cambio que aún no aparece en los datos agregados"),
            ("sesgo de voz", "sobrerrepresentación de opiniones extremas en canales públicos"),
            ("vocabulario del cliente", "términos concretos con que el mercado nombra su problema y sus soluciones"),
            ("umbral de acción", "criterio explícito que convierte una señal en decisión de investigar o intervenir"),
        ],
        metodo=[
            "definir qué fuentes se monitorean y con qué frecuencia",
            "clasificar los hallazgos por tema y por intensidad",
            "distinguir señal débil de ruido con un umbral escrito",
            "triangular con datos propios antes de actuar",
            "documentar la decisión tomada y su resultado",
        ],
        senales=[
            ("volumen y tono por tema", "menciones por tema y proporción negativa, positiva y neutra, por periodo"),
            ("tiempo de detección", "días entre la aparición pública de un tema y su registro interno"),
            ("tasa de confirmación", "señales que se confirmaron con datos propios, sobre señales escaladas"),
        ],
        caso=(
            "En un grupo gremial de talleres aparecen ocho comentarios sobre fallas de facturación de un "
            "competidor. Ruta Andina puede leerlo como oportunidad o como ruido; no tiene criterio escrito "
            "para decidirlo."
        ),
        limite=(
            "El monitoreo de conversaciones debe respetar la privacidad y los términos de cada plataforma. "
            "Recolectar y almacenar datos personales de personas identificables exige base legal."
        ),
        libros=["kaushik", "godin", "chaffey", "solomon"],
        error=("Tomar comentarios aislados como tendencia",
               "Fija un umbral de menciones y una verificación con datos propios antes de escalar la señal."),
    ),
    dict(
        n="12",
        slug="sintesis-de-insights",
        titulo="Síntesis de insights",
        tesis=(
            "Un insight no es un dato ni una observación: es una explicación que cambia lo que la empresa haría. "
            "Tiene tres partes: qué se observó, por qué ocurre y qué implica para la decisión. La mayoría de "
            "los informes se detiene en la primera. La síntesis exige jerarquizar: de veinte hallazgos, "
            "normalmente dos o tres alteran la estrategia y el resto es contexto."
        ),
        conceptos=[
            ("hallazgo", "observación registrada con su fuente y su nivel de evidencia"),
            ("insight", "explicación del mecanismo detrás del hallazgo que cambia una decisión"),
            ("implicancia", "acción concreta que se deriva del insight, con responsable y horizonte"),
            ("jerarquía de evidencia", "orden que distingue dato verificado, patrón observado, hipótesis y opinión"),
        ],
        metodo=[
            "consolidar los hallazgos con su nivel de evidencia",
            "agrupar por mecanismo y no por fuente",
            "formular el insight como explicación falsable",
            "derivar la implicancia concreta y su responsable",
            "descartar explícitamente los hallazgos que no cambian nada",
        ],
        senales=[
            ("insights que modificaron una decisión", "insights con decisión asociada documentada, sobre insights presentados"),
            ("proporción de hallazgos descartados", "hallazgos marcados como no accionables, sobre hallazgos totales"),
            ("tiempo desde hallazgo hasta implicancia", "días entre el registro del hallazgo y la decisión que produjo"),
        ],
        caso=(
            "El informe de investigación de Ruta Andina tiene 42 láminas y 19 hallazgos, todos con el mismo "
            "peso visual. El comité no logra identificar qué debe hacer distinto el lunes."
        ),
        limite=(
            "Sintetizar implica perder matices. La versión ejecutiva debe conservar un enlace al detalle para "
            "que la simplificación no se convierta en distorsión."
        ),
        libros=["ellet", "provost", "rumelt", "hubbard"],
        error=("Presentar todos los hallazgos con la misma jerarquía",
               "Limita el informe a tres insights con implicancia y mueve el resto a anexo."),
    ),
    dict(
        n="13",
        slug="validacion-de-hipotesis-comerciales",
        titulo="Validación de hipótesis comerciales",
        tesis=(
            "Una hipótesis comercial es una apuesta explícita: si hacemos X con el segmento Y, ocurrirá Z en un "
            "plazo T. Validarla exige definir de antemano qué resultado la refutaría; sin ese criterio, "
            "cualquier resultado se interpreta como confirmación. Ries formalizó el ciclo construir-medir-"
            "aprender, pero el paso que suele omitirse es el primero: escribir la hipótesis antes de "
            "ejecutar."
        ),
        conceptos=[
            ("hipótesis falsable", "afirmación que especifica condición, efecto esperado, magnitud y plazo"),
            ("criterio de refutación", "resultado definido de antemano que obligaría a abandonar la hipótesis"),
            ("prueba mínima", "experimento más barato capaz de producir evidencia suficiente para decidir"),
            ("aprendizaje validado", "conclusión respaldada por evidencia que modifica la siguiente decisión"),
        ],
        metodo=[
            "escribir la hipótesis con magnitud y plazo",
            "definir el criterio de refutación antes de ejecutar",
            "diseñar la prueba más barata que discrimine",
            "ejecutar sin modificar el criterio a mitad de camino",
            "registrar el aprendizaje y la decisión resultante",
        ],
        senales=[
            ("hipótesis con criterio previo", "hipótesis con criterio de refutación escrito antes de la prueba, sobre hipótesis probadas"),
            ("tasa de refutación", "hipótesis refutadas, sobre hipótesis probadas en el periodo"),
            ("costo por aprendizaje", "costo total de las pruebas dividido por número de aprendizajes documentados"),
        ],
        caso=(
            "Ruta Andina probó un descuento de lanzamiento en un vertical nuevo. Al no alcanzar la meta, el "
            "equipo concluyó que «faltó tiempo» y extendió la prueba dos veces sin criterio previo."
        ),
        limite=(
            "No todo puede probarse antes: algunas decisiones son irreversibles o el costo de la prueba supera "
            "el de equivocarse. En esos casos corresponde decidir con juicio explícito y dejar traza."
        ),
        libros=["ries-lean", "kohavi", "blank", "hubbard"],
        error=("Cambiar el criterio de éxito después de ver el resultado",
               "Registra el criterio en un documento fechado antes de iniciar la prueba."),
    ),
    dict(
        n="14",
        slug="informe-de-oportunidad-de-mercado",
        titulo="Informe de oportunidad de mercado",
        tesis=(
            "Esta clase integra la parte en un informe que un comité pueda usar para decidir. Sus componentes "
            "no son negociables: decisión que informa, método y muestra, hallazgos jerarquizados, "
            "dimensionamiento con supuestos, análisis competitivo, riesgos y recomendación con condiciones de "
            "revisión. La prueba de calidad es que un lector escéptico pueda reconstruir el razonamiento y "
            "señalar exactamente dónde discrepa."
        ),
        conceptos=[
            ("informe decisional", "documento estructurado alrededor de la decisión que debe informar y no del proceso realizado"),
            ("declaración de método", "sección que describe fuentes, muestra, límites y fecha de la evidencia"),
            ("recomendación condicionada", "propuesta que explicita bajo qué supuestos es válida y qué la invalidaría"),
            ("auditabilidad", "posibilidad de que un tercero verifique cada afirmación hasta su fuente"),
        ],
        metodo=[
            "abrir con la decisión y la recomendación",
            "declarar método, muestra y límites",
            "presentar tres insights con su implicancia",
            "dimensionar la oportunidad con escenarios",
            "cerrar con riesgos, condiciones de revisión y responsables",
        ],
        senales=[
            ("afirmaciones trazables", "afirmaciones del informe con fuente verificable, sobre afirmaciones totales"),
            ("tiempo de lectura hasta la recomendación", "minutos que tarda un lector en encontrar la recomendación y sus condiciones"),
            ("decisiones tomadas con el informe", "decisiones formalizadas que citan el informe, en los 60 días posteriores"),
        ],
        caso=(
            "El comité de Ruta Andina debe decidir entre abrir el vertical de centros médicos o profundizar en "
            "talleres. Tiene 40 minutos y necesita un documento que soporte preguntas duras."
        ),
        limite=(
            "Un informe no reemplaza la decisión ni la responsabilidad de quien decide. Su función es hacer "
            "explícito el razonamiento, no eliminar la incertidumbre."
        ),
        libros=["ellet", "malhotra", "hubbard", "rumelt"],
        error=("Estructurar el informe por proceso y no por decisión",
               "Abre con la recomendación y sus condiciones; el método va después, no antes."),
    ),
]
