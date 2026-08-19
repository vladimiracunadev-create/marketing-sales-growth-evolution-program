# -*- coding: utf-8 -*-
"""Parte 10 — Negociación comercial."""

CLASES = [
    dict(
        n="01",
        slug="preparacion-de-una-negociacion",
        titulo="Preparación de una negociación",
        tesis=(
            "El resultado de una negociación se determina en gran medida antes de sentarse. Malhotra y "
            "Bazerman muestran que la preparación analítica —intereses propios y ajenos, alternativas, rango "
            "de acuerdo, criterios objetivos— explica más del resultado que la habilidad conversacional. "
            "Improvisar no es flexibilidad: es ceder a quien preparó mejor. La preparación también define de "
            "antemano el punto de retirada, que es la única protección real contra la presión del momento."
        ),
        conceptos=[
            ("interés", "necesidad o preocupación subyacente que explica por qué una parte pide lo que pide"),
            ("alternativa fuera de la mesa", "mejor resultado alcanzable si no hay acuerdo con esta contraparte"),
            ("punto de retirada", "condición mínima bajo la cual conviene no cerrar el acuerdo"),
            ("criterio objetivo", "estándar externo e independiente que legitima una propuesta"),
        ],
        metodo=[
            "listar intereses propios y estimar los de la contraparte",
            "evaluar y mejorar la alternativa fuera de la mesa",
            "definir el punto de retirada por escrito",
            "reunir criterios objetivos que respalden la posición",
            "planificar concesiones y sus contrapartidas",
        ],
        senales=[
            ("negociaciones con preparación documentada", "negociaciones con ficha de preparación completa, sobre negociaciones realizadas"),
            ("desviación respecto del punto de retirada", "acuerdos cerrados bajo el mínimo definido, sobre acuerdos cerrados"),
            ("valor conservado", "diferencia entre el resultado obtenido y el objetivo inicial, ponderada por ingreso"),
        ],
        caso=(
            "El ejecutivo de Ruta Andina llega a la reunión con compras sin conocer los plazos de pago "
            "estándar de la cadena ni el costo financiero de 90 días para su propia empresa."
        ),
        limite=(
            "La preparación excesiva puede volverse rigidez. El plan debe incluir qué información nueva "
            "obligaría a revisar la estrategia durante la conversación."
        ),
        libros=["malhotra-neg", "fisher-ury", "shell", "voss"],
        error=("Entrar a negociar sin punto de retirada escrito",
               "Define y documenta el mínimo aceptable antes de la reunión y compártelo con tu jefatura."),
    ),
    dict(
        n="02",
        slug="intereses-versus-posiciones",
        titulo="Intereses versus posiciones",
        tesis=(
            "Una posición es lo que la parte dice querer; un interés es la razón por la que lo quiere. Fisher "
            "y Ury mostraron que negociar sobre posiciones produce regateo y acuerdos subóptimos, mientras "
            "que explorar intereses abre opciones que ninguna parte había considerado. La técnica es simple y "
            "difícil: preguntar por qué y para qué, en lugar de contraofertar de inmediato."
        ),
        conceptos=[
            ("posición", "demanda concreta que una parte formula en la mesa"),
            ("interés subyacente", "necesidad, temor o restricción que explica esa demanda"),
            ("opción de valor conjunto", "alternativa que satisface intereses de ambas partes sin ceder lo esencial"),
            ("intercambio de prioridades", "acuerdo donde cada parte cede en lo que valora menos y obtiene lo que valora más"),
        ],
        metodo=[
            "registrar las posiciones enunciadas por ambas partes",
            "indagar el interés detrás de cada posición",
            "identificar prioridades distintas entre las partes",
            "generar opciones antes de evaluar cualquiera",
            "elegir la combinación que maximiza valor conjunto",
        ],
        senales=[
            ("opciones generadas por negociación", "alternativas distintas planteadas antes de decidir, por negociación"),
            ("acuerdos con intercambio de prioridades", "acuerdos donde ambas partes cedieron en distinto atributo, sobre acuerdos cerrados"),
            ("satisfacción declarada post acuerdo", "puntuación de satisfacción de ambas partes al cierre, con muestra definida"),
        ],
        caso=(
            "La cadena exige 30 % de descuento. El interés detrás es mostrar ahorro en su presupuesto anual, "
            "algo que también se logra con un plan de pagos distinto y un año de precio fijo."
        ),
        limite=(
            "No todos los intereses son compatibles. Cuando el conflicto es distributivo real, explorar "
            "intereses ayuda a entender pero no elimina la necesidad de repartir."
        ),
        libros=["fisher-ury", "malhotra-neg", "ury", "shell"],
        error=("Contraofertar antes de entender el interés",
               "Formula al menos dos preguntas sobre el porqué de la demanda antes de responder con una cifra."),
    ),
    dict(
        n="03",
        slug="batna",
        titulo="BATNA",
        tesis=(
            "La mejor alternativa a un acuerdo negociado es la fuente real del poder en una negociación: "
            "define el punto bajo el cual no conviene cerrar. Su valor práctico es doble. Primero, conocer la "
            "propia obliga a decidir con criterio y no con miedo. Segundo, estimar la de la contraparte "
            "corrige la ilusión de que el otro no tiene opciones. La palanca más eficaz no es negociar mejor: "
            "es mejorar la alternativa antes de negociar."
        ),
        conceptos=[
            ("alternativa propia", "mejor resultado alcanzable sin acuerdo con esta contraparte, valorizado"),
            ("alternativa de la contraparte", "estimación de las opciones reales de la otra parte"),
            ("mejora de la alternativa", "acción previa que aumenta el poder al ampliar las opciones propias"),
            ("valor de reserva", "monto o condición mínima derivada de la alternativa propia"),
        ],
        metodo=[
            "identificar y valorizar la alternativa propia",
            "actuar para mejorarla antes de negociar",
            "estimar la alternativa de la contraparte con evidencia",
            "derivar el valor de reserva del análisis",
            "revisar la estimación si aparece información nueva",
        ],
        senales=[
            ("cobertura de pipeline alternativo", "valor de oportunidades alternativas disponibles, sobre el valor del negocio en negociación"),
            ("acuerdos bajo el valor de reserva", "acuerdos cerrados bajo el mínimo, sobre acuerdos cerrados"),
            ("mejora de alternativa documentada", "acciones ejecutadas para ampliar opciones antes de negociar, por negociación relevante"),
        ],
        caso=(
            "Ruta Andina negocia con la cadena en el último mes del trimestre y sin otras oportunidades "
            "grandes en el pipeline. Su alternativa es débil y la contraparte lo percibe."
        ),
        limite=(
            "Sobreestimar la propia alternativa lleva a rechazar acuerdos razonables. La estimación debe ser "
            "honesta y revisada con datos, no con optimismo."
        ),
        libros=["fisher-ury", "malhotra-neg", "shell", "ury"],
        error=("Negociar sin alternativas y con presión de plazo",
               "Construye pipeline alternativo antes de entrar a la negociación grande y evita depender del cierre de periodo."),
    ),
    dict(
        n="04",
        slug="zopa",
        titulo="ZOPA",
        tesis=(
            "La zona de posible acuerdo es el rango entre el valor de reserva de cada parte. Si no existe "
            "superposición, no hay acuerdo posible sin cambiar el alcance o las condiciones. Determinar si "
            "hay ZOPA temprano evita negociaciones largas y estériles: cuando no la hay, la conversación "
            "productiva es sobre qué elementos del acuerdo pueden modificarse para crearla."
        ),
        conceptos=[
            ("zona de posible acuerdo", "rango entre el mínimo aceptable de una parte y el máximo aceptable de la otra"),
            ("ausencia de zona", "situación en que los valores de reserva no se superponen y el acuerdo es imposible sin cambios"),
            ("ampliación del alcance", "modificación de atributos del acuerdo que crea una zona donde no existía"),
            ("estimación de la reserva ajena", "aproximación al mínimo de la contraparte basada en evidencia y no en supuestos"),
        ],
        metodo=[
            "definir el valor de reserva propio",
            "estimar el de la contraparte con evidencia disponible",
            "verificar si existe superposición",
            "si no existe, modificar alcance, plazo o condiciones",
            "cerrar dentro de la zona y documentar los supuestos",
        ],
        senales=[
            ("negociaciones sin zona identificada", "negociaciones abandonadas por ausencia de zona, sobre negociaciones iniciadas"),
            ("tiempo hasta detectar ausencia de zona", "días entre el inicio de la negociación y la conclusión de que no hay acuerdo posible"),
            ("acuerdos con alcance modificado", "acuerdos cerrados tras modificar alcance o condiciones, sobre acuerdos cerrados"),
        ],
        caso=(
            "La cadena tiene un techo presupuestario de CLP 1,2 millones mensuales y el costo de servir de "
            "Ruta Andina a 14 locales es CLP 1,4 millones. No hay zona con el alcance actual."
        ),
        limite=(
            "La estimación de la reserva ajena siempre tiene error. Actuar como si fuera exacta produce "
            "rupturas innecesarias o concesiones excesivas."
        ),
        libros=["malhotra-neg", "fisher-ury", "shell", "nagle"],
        error=("Insistir en una negociación sin zona posible",
               "Verifica temprano la superposición y, si no existe, propone modificar el alcance en lugar de bajar el precio."),
    ),
    dict(
        n="05",
        slug="anclaje",
        titulo="Anclaje",
        tesis=(
            "La primera cifra que entra a la conversación ejerce una influencia desproporcionada sobre el "
            "resultado, incluso entre negociadores expertos. Eso hace del anclaje una decisión estratégica: "
            "anclar primero conviene cuando se tiene buena información del valor; esperar conviene cuando la "
            "incertidumbre es alta. Ante un ancla extrema, la respuesta no es contraofertar de inmediato sino "
            "reencuadrar sobre criterios objetivos."
        ),
        conceptos=[
            ("ancla", "primera cifra o condición que fija el marco de referencia de la negociación"),
            ("ancla extrema", "propuesta inicial deliberadamente alejada de lo razonable"),
            ("reencuadre", "reconducción de la conversación hacia criterios objetivos en lugar de responder al ancla"),
            ("rango justificado", "propuesta acompañada de la razón que la sostiene"),
        ],
        metodo=[
            "decidir si conviene anclar primero según información disponible",
            "preparar el ancla con su justificación",
            "ante un ancla extrema, no contraofertar de inmediato",
            "reencuadrar con criterios objetivos",
            "registrar el efecto del anclaje en el resultado",
        ],
        senales=[
            ("diferencia entre ancla y cierre", "distancia porcentual entre la primera cifra y el acuerdo final"),
            ("frecuencia de anclaje propio", "negociaciones donde la empresa fijó la primera cifra, sobre negociaciones realizadas"),
            ("resultado por estrategia de anclaje", "precio efectivo promedio de cierre, comparado entre negociaciones donde ancló la empresa y donde ancló la contraparte"),
        ],
        caso=(
            "Compras abre con «necesitamos 40 % de descuento». El ejecutivo de Ruta Andina responde con 20 % "
            "y la negociación queda anclada en un rango que destruye el margen."
        ),
        limite=(
            "Un ancla extrema propia puede terminar la negociación o dañar la relación de largo plazo. La "
            "agresividad debe calibrarse según el valor de la relación futura."
        ),
        libros=["malhotra-neg", "kahneman", "voss", "ariely"],
        error=("Contraofertar de inmediato ante un ancla extrema",
               "Reencuadra primero con criterios objetivos y pide la justificación de la cifra recibida."),
    ),
    dict(
        n="06",
        slug="concesiones",
        titulo="Concesiones",
        tesis=(
            "Cada concesión enseña algo a la contraparte. Conceder rápido enseña que había margen; conceder "
            "sin pedir nada enseña que basta insistir; conceder en montos crecientes enseña que conviene "
            "esperar. La disciplina consiste en planificar las concesiones antes, hacerlas decrecientes, "
            "condicionarlas siempre a una contrapartida y declararlas como esfuerzo real."
        ),
        conceptos=[
            ("concesión planificada", "cesión definida de antemano con su contrapartida asociada"),
            ("patrón de concesión", "secuencia de magnitudes que comunica cuánto margen queda"),
            ("condicionalidad", "vínculo explícito entre una cesión propia y una contrapartida de la otra parte"),
            ("señal de agotamiento", "comunicación creíble de que se llegó al límite"),
        ],
        metodo=[
            "listar concesiones posibles y su costo real",
            "asignar a cada una la contrapartida exigida",
            "planificar magnitudes decrecientes",
            "condicionar explícitamente cada cesión",
            "documentar lo concedido y lo obtenido",
        ],
        senales=[
            ("razón concesión-contrapartida", "concesiones con contrapartida obtenida, sobre concesiones otorgadas"),
            ("magnitud de la última concesión", "porcentaje de la última cesión frente a la primera, por negociación"),
            ("valor obtenido en contrapartidas", "valor monetario de las contrapartidas obtenidas, sobre valor monetario de las concesiones otorgadas"),
        ],
        caso=(
            "En la negociación con la cadena, Ruta Andina concedió 8 %, luego 12 % y luego 6 %. La secuencia "
            "creciente indicó que había más margen y compras siguió pidiendo."
        ),
        limite=(
            "La rigidez absoluta puede costar el negocio cuando la contraparte necesita mostrar un logro. La "
            "clave es que la concesión tenga contrapartida, no que no exista."
        ),
        libros=["malhotra-neg", "fisher-ury", "shell", "nagle"],
        error=("Conceder en magnitudes crecientes",
               "Planifica concesiones decrecientes y exige contrapartida en cada una."),
    ),
    dict(
        n="07",
        slug="negociacion-de-precio",
        titulo="Negociación de precio",
        tesis=(
            "Negociar precio sin haber establecido valor es una discusión que se pierde por definición: sin "
            "referencia, cualquier monto parece alto. La secuencia correcta ubica la conversación de precio "
            "después del diagnóstico cuantificado, y usa criterios objetivos —costo del problema, costo "
            "total, comparables— en lugar de regateo. Cuando la presión aumenta, la palanca es el alcance, no "
            "el descuento."
        ),
        conceptos=[
            ("referencia de valor", "cifra del cliente que da sentido al precio propuesto"),
            ("palanca de alcance", "ajuste del contenido del acuerdo como alternativa a bajar el precio"),
            ("costo total de propiedad", "suma de precio, implementación, operación y salida durante la vida del contrato"),
            ("precio efectivo", "monto realmente cobrado después de descuentos, bonificaciones y condiciones"),
        ],
        metodo=[
            "establecer la referencia de valor antes de hablar de precio",
            "presentar el costo total y no sólo el precio de lista",
            "usar la palanca de alcance ante presión de descuento",
            "condicionar cualquier rebaja a una contrapartida",
            "documentar el precio efectivo y sus condiciones",
        ],
        senales=[
            ("descuento promedio por segmento", "diferencia entre precio de lista y efectivo, ponderada por ingreso"),
            ("uso de la palanca de alcance", "negociaciones resueltas con ajuste de alcance, sobre negociaciones con presión de precio"),
            ("margen conservado", "margen de contribución de los negocios negociados, frente al margen estándar"),
        ],
        caso=(
            "Ante la exigencia de 30 %, Ruta Andina puede reducir alcance —menos locales, sin migración "
            "asistida, soporte estándar— en lugar de bajar el precio unitario y crear precedente."
        ),
        limite=(
            "Reducir alcance puede afectar el resultado del cliente y generar churn. La palanca debe usarse "
            "sobre elementos que no comprometen el valor central."
        ),
        libros=["nagle", "malhotra-neg", "fisher-ury", "simon"],
        error=("Negociar precio antes de establecer valor",
               "Posterga la conversación de precio hasta tener el costo del problema cuantificado por el cliente."),
    ),
    dict(
        n="08",
        slug="negociacion-de-alcance",
        titulo="Negociación de alcance",
        tesis=(
            "El alcance es la variable más flexible y la peor gestionada: se amplía en conversaciones "
            "informales y nunca se documenta. Negociar alcance con disciplina significa que cada elemento "
            "tiene un costo conocido y que agregar algo implica retirar otra cosa o ajustar el precio. La "
            "ausencia de esa disciplina produce proyectos que se implementan con pérdida."
        ),
        conceptos=[
            ("línea base de alcance", "conjunto documentado de entregables acordados y sus exclusiones"),
            ("cambio de alcance", "modificación posterior que altera esfuerzo, costo o plazo"),
            ("costo unitario de cada elemento", "valorización interna de cada componente del alcance"),
            ("procedimiento de cambio", "regla que define cómo se aprueba y se cobra una modificación"),
        ],
        metodo=[
            "documentar la línea base con exclusiones explícitas",
            "valorizar internamente cada elemento",
            "definir el procedimiento de cambio antes de firmar",
            "aplicar el procedimiento sin excepciones informales",
            "medir la desviación de alcance por proyecto",
        ],
        senales=[
            ("desviación de alcance", "horas ejecutadas por sobre lo acordado, sobre horas presupuestadas, por proyecto"),
            ("cambios documentados", "cambios de alcance con aprobación registrada, sobre cambios ejecutados"),
            ("margen real por proyecto", "ingreso menos costo real de ejecución, sobre ingreso del proyecto"),
        ],
        caso=(
            "En tres proyectos de Ruta Andina el alcance creció en promedio 38 % sin cobro. Cada ampliación se "
            "acordó por chat entre el cliente y el implementador."
        ),
        limite=(
            "Un procedimiento de cambio rígido en proyectos pequeños puede deteriorar la relación por montos "
            "menores. El umbral de aplicación debe ser proporcional."
        ),
        libros=["fisher-ury", "nagle", "malhotra-neg", "grove"],
        error=("Aceptar ampliaciones informales de alcance",
               "Aplica el procedimiento de cambio a toda modificación que supere el umbral definido."),
    ),
    dict(
        n="09",
        slug="terminos-y-condiciones",
        titulo="Términos y condiciones",
        tesis=(
            "Los términos —plazos de pago, niveles de servicio, penalidades, propiedad de datos, "
            "renovación, salida— pueden valer más que el precio. Un 30 % de descuento con pago a 30 días "
            "puede ser mejor que un 10 % con pago a 120. Negociar términos exige conocer su costo real: el "
            "financiero de los plazos, el operativo de los niveles de servicio y el legal de las cláusulas."
        ),
        conceptos=[
            ("costo financiero del plazo", "valor del dinero durante el periodo entre entrega y cobro"),
            ("nivel de servicio comprometido", "estándar de disponibilidad o respuesta con consecuencia definida"),
            ("cláusula de salida", "condición que regula la terminación anticipada y sus efectos"),
            ("propiedad y tratamiento de datos", "definición de quién es responsable y qué se puede hacer con la información del cliente"),
        ],
        metodo=[
            "valorizar el costo de cada término solicitado",
            "priorizar qué términos son negociables y cuáles no",
            "verificar la coherencia con la capacidad operativa",
            "revisar el cumplimiento normativo de las cláusulas",
            "documentar el acuerdo completo y sus anexos",
        ],
        senales=[
            ("plazo de cobro promedio", "días entre facturación y cobro efectivo, ponderado por monto"),
            ("cumplimiento de niveles de servicio", "casos dentro del estándar comprometido, sobre casos aplicables"),
            ("contratos con cláusulas fuera de política", "contratos con condiciones no estándar, sobre contratos firmados"),
        ],
        caso=(
            "La cadena propone pago a 90 días. Para Ruta Andina, que paga sueldos mensuales, eso equivale a "
            "financiar dos meses de operación de esa cuenta."
        ),
        limite=(
            "Las cláusulas que limitan derechos del consumidor o el tratamiento de datos personales están "
            "sujetas a normas imperativas: no todo lo acordado es exigible."
        ),
        libros=["fisher-ury", "malhotra-neg", "nagle", "iso-31000"],
        error=("Negociar precio ignorando el costo de los términos",
               "Valoriza plazos, niveles de servicio y penalidades antes de ceder en precio."),
    ),
    dict(
        n="10",
        slug="compras-y-procurement",
        titulo="Negociar con compras y procurement",
        tesis=(
            "Cuando la negociación pasa a compras, el criterio cambia: la conversación deja de ser sobre "
            "valor y pasa a ser sobre condiciones comparables. La preparación adecuada consiste en llegar con "
            "el área usuaria alineada, con el costo total documentado y con contrapartidas listas. Un error "
            "frecuente es tratar a compras como adversario: su mandato es legítimo y su criterio es "
            "predecible."
        ),
        conceptos=[
            ("mandato de compras", "objetivo formal con que se evalúa al área, normalmente ahorro y control de riesgo"),
            ("comparabilidad forzada", "presión por evaluar ofertas distintas bajo un mismo formato"),
            ("alianza con el área usuaria", "respaldo interno que sostiene el valor durante la negociación de condiciones"),
            ("paquete de contrapartidas", "conjunto de concesiones preparadas con su exigencia asociada"),
        ],
        metodo=[
            "alinear al área usuaria antes de la intervención de compras",
            "documentar el costo total y los diferenciales",
            "preparar el paquete de contrapartidas",
            "responder a la comparabilidad forzada con criterios objetivos",
            "cerrar con acuerdo escrito y condiciones claras",
        ],
        senales=[
            ("diferencia de margen con y sin intervención de compras", "margen promedio de negocios con compras frente a los sin compras"),
            ("respaldo del área usuaria", "negociaciones con participación activa del usuario, sobre negociaciones con compras"),
            ("contrapartidas obtenidas", "valor de las contrapartidas conseguidas, sobre el valor de las concesiones otorgadas"),
        ],
        caso=(
            "Compras de la cadena pide igualar la oferta del competidor. La jefa de operaciones sabe que esa "
            "oferta no incluye migración ni soporte en terreno, pero no fue invitada a la reunión."
        ),
        limite=(
            "En procesos públicos y en algunas corporaciones, el contacto con el área usuaria durante la "
            "evaluación está restringido. Las reglas del proceso mandan."
        ),
        libros=["malhotra-neg", "fisher-ury", "shell", "nagle"],
        error=("Negociar con compras sin respaldo del área usuaria",
               "Alinea al usuario antes y solicita su participación en la conversación de condiciones."),
    ),
    dict(
        n="11",
        slug="tacticas-dificiles",
        titulo="Tácticas difíciles",
        tesis=(
            "Existen tácticas diseñadas para desequilibrar: presión de tiempo artificial, autoridad limitada "
            "fingida, ultimátum, escalamiento de demandas después del acuerdo. Ury propone no responder en el "
            "mismo registro sino nombrar la táctica y reconducir hacia el problema. Nombrarla suele bastar "
            "para desactivarla, porque su eficacia depende de que no sea reconocida."
        ),
        conceptos=[
            ("táctica de presión", "maniobra que busca ventaja alterando el estado emocional o el tiempo disponible"),
            ("autoridad limitada", "afirmación de no poder decidir, usada para obtener concesiones sin reciprocidad"),
            ("escalamiento posterior", "petición de condiciones adicionales después de un acuerdo aparente"),
            ("nombrar la táctica", "hacer explícita la maniobra para reconducir la conversación al problema"),
        ],
        metodo=[
            "reconocer la táctica y no responder en el mismo registro",
            "nombrarla de forma neutra",
            "reconducir hacia criterios objetivos",
            "reafirmar el punto de retirada si corresponde",
            "documentar lo ocurrido para futuras negociaciones",
        ],
        senales=[
            ("frecuencia de tácticas registradas", "negociaciones con tácticas de presión documentadas, sobre negociaciones realizadas"),
            ("concesiones bajo presión", "concesiones otorgadas en los últimos tres días del periodo, sobre concesiones totales"),
            ("acuerdos reabiertos", "acuerdos con demandas adicionales tras el cierre, sobre acuerdos cerrados"),
        ],
        caso=(
            "A dos días del cierre trimestral, compras de la cadena informa que «el directorio exige 5 % "
            "adicional o no se firma». El acuerdo ya estaba cerrado en lo sustantivo."
        ),
        limite=(
            "Nombrar la táctica puede tensionar la relación si se hace en tono acusatorio. La formulación debe "
            "ser descriptiva y orientada al problema, no a la persona."
        ),
        libros=["ury", "voss", "malhotra-neg", "shell"],
        error=("Ceder ante el escalamiento posterior al acuerdo",
               "Reafirma el acuerdo original, nombra la maniobra y condiciona cualquier cambio a una contrapartida."),
    ),
    dict(
        n="12",
        slug="negociacion-intercultural",
        titulo="Negociación intercultural",
        tesis=(
            "Las diferencias culturales afectan el ritmo, la formalidad, el papel del contrato y la manera de "
            "expresar desacuerdo. En expansión regional esto es concreto: lo que en Chile se lee como "
            "eficiencia puede leerse como descortesía en otro mercado, y lo que allá es cortesía puede "
            "leerse aquí como falta de compromiso. La regla práctica es verificar, no asumir: preguntar cómo "
            "se toman las decisiones en esa organización."
        ),
        conceptos=[
            ("norma de interacción", "expectativa cultural sobre ritmo, formalidad y forma de expresar desacuerdo"),
            ("rol del contrato", "grado en que el documento escrito se considera el acuerdo definitivo o un punto de partida"),
            ("señal ambigua", "gesto o expresión cuyo significado difiere entre contextos culturales"),
            ("verificación explícita", "práctica de confirmar entendimiento en lugar de suponerlo"),
        ],
        metodo=[
            "investigar las normas del contexto antes de negociar",
            "preguntar explícitamente cómo se decide en esa organización",
            "ajustar ritmo y formalidad sin cambiar los criterios",
            "verificar entendimiento por escrito en cada hito",
            "registrar aprendizajes para futuras negociaciones en ese mercado",
        ],
        senales=[
            ("malentendidos registrados", "aclaraciones necesarias por diferencias de interpretación, por negociación internacional"),
            ("ciclo de negociación por mercado", "días hasta acuerdo, mediana por país o región"),
            ("acuerdos con confirmación escrita por hito", "hitos confirmados por escrito, sobre hitos acordados"),
        ],
        caso=(
            "En su primera negociación en Perú, Ruta Andina interpretó como cierre lo que era una "
            "conversación exploratoria y comprometió recursos de implementación por adelantado."
        ),
        limite=(
            "Las generalizaciones culturales son promedios y pueden convertirse en estereotipos. La "
            "organización concreta y las personas concretas mandan sobre el promedio nacional."
        ),
        libros=["shell", "fisher-ury", "malhotra-neg", "solomon"],
        error=("Asumir que el acuerdo verbal significa lo mismo en todos los contextos",
               "Confirma por escrito cada hito y pregunta explícitamente qué falta para considerar cerrado el acuerdo."),
    ),
    dict(
        n="13",
        slug="cierre-y-documentacion",
        titulo="Cierre y documentación",
        tesis=(
            "Un acuerdo no documentado es una fuente futura de conflicto. El cierre profesional incluye "
            "resumen escrito de lo acordado, confirmación de ambas partes, definición de responsables y "
            "fechas, y archivo accesible. La regla práctica es enviar el resumen dentro de las 24 horas: la "
            "memoria de la conversación diverge rápidamente y quien documenta primero fija el marco."
        ),
        conceptos=[
            ("resumen de acuerdo", "documento breve que registra lo convenido, sus condiciones y sus responsables"),
            ("confirmación bilateral", "aceptación explícita de ambas partes sobre el contenido del resumen"),
            ("trazabilidad del acuerdo", "posibilidad de reconstruir qué se acordó, cuándo y con quién"),
            ("divergencia de memoria", "diferencia progresiva entre lo que cada parte recuerda haber acordado"),
        ],
        metodo=[
            "resumir por escrito dentro de las 24 horas",
            "detallar condiciones, exclusiones y responsables",
            "solicitar confirmación explícita",
            "archivar en el sistema accesible para operación",
            "revisar el cumplimiento en los hitos definidos",
        ],
        senales=[
            ("acuerdos con resumen enviado", "acuerdos con resumen dentro de 24 horas, sobre acuerdos alcanzados"),
            ("tasa de confirmación bilateral", "resúmenes confirmados por la contraparte, sobre resúmenes enviados"),
            ("conflictos por interpretación", "disputas sobre lo acordado, sobre contratos vigentes"),
        ],
        caso=(
            "Ruta Andina y la cadena discuten si el soporte en terreno estaba incluido. La conversación "
            "ocurrió en una reunión sin acta y ambas partes recuerdan versiones distintas."
        ),
        limite=(
            "Un resumen demasiado extenso desincentiva la confirmación. Debe ser breve, específico y "
            "verificable, con anexos para el detalle."
        ),
        libros=["fisher-ury", "malhotra-neg", "grove", "ellet"],
        error=("Cerrar sin resumen escrito confirmado",
               "Envía el resumen dentro de 24 horas y solicita confirmación explícita antes de iniciar la ejecución."),
    ),
    dict(
        n="14",
        slug="simulacion-integral-de-negociacion",
        titulo="Simulación integral de negociación",
        tesis=(
            "Esta clase integra la parte en una simulación completa con roles, información asimétrica y "
            "presión de tiempo. La evaluación no se limita al resultado económico: incluye preparación "
            "documentada, calidad de las preguntas, uso de criterios objetivos, manejo de tácticas y "
            "documentación final. Un buen resultado obtenido con presión indebida se evalúa como fracaso."
        ),
        conceptos=[
            ("simulación con información asimétrica", "ejercicio donde cada parte conoce datos que la otra desconoce"),
            ("evaluación de proceso", "revisión de cómo se negoció y no sólo del resultado obtenido"),
            ("valor conjunto creado", "beneficio total generado por el acuerdo para ambas partes"),
            ("integridad del acuerdo", "cumplimiento de estándares éticos y legales durante la negociación"),
        ],
        metodo=[
            "preparar con ficha completa antes de la simulación",
            "ejecutar la negociación con roles e información asimétrica",
            "documentar el acuerdo alcanzado",
            "evaluar proceso, resultado e integridad",
            "extraer aprendizajes para el playbook comercial",
        ],
        senales=[
            ("valor conjunto del acuerdo", "suma del valor obtenido por ambas partes, comparada con el máximo posible del ejercicio"),
            ("uso de criterios objetivos", "argumentos respaldados por estándares externos, sobre argumentos totales registrados"),
            ("cumplimiento del punto de retirada", "acuerdos dentro de los límites definidos, sobre acuerdos alcanzados"),
        ],
        caso=(
            "La simulación reproduce la negociación con la cadena: 30 % de descuento exigido, pago a 90 días, "
            "exclusividad y un competidor con oferta más barata pero de menor alcance."
        ),
        limite=(
            "Una simulación no reproduce las consecuencias reales de una relación comercial de años. Sirve para "
            "entrenar proceso, no para predecir resultados."
        ),
        libros=["malhotra-neg", "fisher-ury", "ury", "shell"],
        error=("Evaluar la simulación sólo por el precio obtenido",
               "Incluye preparación, criterios objetivos, integridad y documentación en la rúbrica de evaluación."),
    ),
]
