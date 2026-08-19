# -*- coding: utf-8 -*-
"""Desarrollo escrito de la Parte 16 — CRM, pipeline y sales operations."""

DESARROLLO = {

    "01": [
        "Un CRM no es una base de datos de contactos: es el sistema donde ocurre el trabajo comercial. Esa "
        "distinción determina su diseño. Si el sistema se concibe como repositorio para que la gerencia "
        "reporte, se llenará con el mínimo esfuerzo y con datos de baja calidad. Si se concibe como "
        "herramienta que ayuda a vender, el registro se vuelve un subproducto del trabajo.",

        "El costo de registro es real y se puede calcular: minutos por oportunidad multiplicados por el "
        "volumen y por el costo de la hora comercial. En equipos medianos esa cifra sorprende. Ponerla sobre "
        "la mesa cambia la discusión sobre qué campos exigir, porque convierte una preferencia en una "
        "decisión de inversión.",

        "El valor devuelto es lo que justifica el costo: recordatorios útiles, información del cliente "
        "disponible antes de una llamada, historial que evita repetir preguntas. Medirlo es difícil; lo que "
        "sí se puede medir es la adopción voluntaria de funciones que nadie obliga a usar, que es un buen "
        "indicador de si el sistema sirve.",

        "Exigir más registro mejora la información disponible y consume tiempo comercial y buena voluntad. "
        "La solución no es un punto medio arbitrario sino eliminar todo campo que no alimente una decisión "
        "concreta. Ese ejercicio, hecho con honestidad, suele reducir a la mitad los campos obligatorios.",

        "Un CRM contiene datos personales de contactos y está sujeto a obligaciones de finalidad, "
        "conservación y derechos del titular. La configuración debe permitir localizar, exportar y suprimir "
        "la información de una persona. Verificar esa capacidad antes de necesitarla es parte del diseño, no "
        "una tarea posterior.",
    ],

    "02": [
        "Diseñar un pipeline es decidir cómo se representa el avance de una compra. La decisión de fondo es "
        "si las etapas describen lo que hace el vendedor o lo que ocurre en el cliente. La segunda opción "
        "produce pronósticos utilizables; la primera produce oportunidades que avanzan porque se enviaron "
        "documentos.",

        "La probabilidad por etapa sólo tiene sentido si se calcula con datos históricos propios y se revisa. "
        "Los porcentajes que vienen por defecto en las herramientas describen a otra empresa. Calcular la "
        "tasa real de conversión de cada etapa al cierre, con al menos un año de datos, convierte el "
        "pronóstico ponderado en algo que se puede defender.",

        "La granularidad debe corresponder a la duración del ciclo. Un pipeline de siete etapas para un ciclo "
        "de dos semanas produce registros que nadie mantiene; uno de tres etapas para un ciclo de nueve meses "
        "no permite ver dónde está el problema. La regla práctica es que cada etapa debe durar lo suficiente "
        "como para que actualizar tenga sentido.",

        "Más etapas entregan visibilidad y aumentan el costo de mantenimiento y la probabilidad de que los "
        "datos no reflejen la realidad. Menos etapas se mantienen mejor y ocultan problemas intermedios. La "
        "decisión debe considerar qué preguntas de gestión debe responder el pipeline, y descartar las "
        "etapas que no responden ninguna.",

        "El pipeline es un modelo del proceso de compra y todos los modelos simplifican. En compras con "
        "comité, la oportunidad puede estar simultáneamente en dos estados según el interlocutor. Forzar un "
        "estado único produce una representación cómoda y falsa; reconocer el límite y complementar con el "
        "mapa de cuenta es más honesto.",
    ],

    "03": [
        "El criterio de salida es lo que impide que el pipeline se convierta en una lista de deseos. Define "
        "qué evidencia debe existir para que una oportunidad pase a la etapa siguiente, y esa evidencia tiene "
        "que ser verificable por alguien distinto del vendedor. Sin ese requisito, el avance de etapa mide "
        "optimismo.",

        "El avance sin evidencia es un fenómeno predecible: cuando la etapa determina el pronóstico y el "
        "pronóstico determina la evaluación, hay incentivo para avanzar. Reconocerlo permite diseñar contra "
        "él en lugar de apelar a la honestidad individual. Los criterios verificables son ese diseño.",

        "El retroceso de etapa debe ser normal y no penalizado. Un negocio que vuelve atrás porque apareció "
        "un nuevo decisor está reflejando la realidad, y castigar ese registro garantiza que la próxima vez "
        "no se haga. La proporción de oportunidades que retrocede es, de hecho, un indicador de honestidad "
        "del sistema.",

        "Criterios estrictos mejoran la calidad del pronóstico y reducen el pipeline reportado, lo que genera "
        "resistencia inmediata en un equipo con cuota. La transición debe manejarse explícitamente: "
        "reconocer que el pipeline va a caer, explicar por qué y comparar contra la nueva base a partir de "
        "ahí.",

        "La auditoría de etapas —revisar una muestra de oportunidades y verificar si cumplen el criterio "
        "declarado— es el control que mantiene vivo el sistema. Sin ella, los criterios se relajan "
        "gradualmente hasta desaparecer. Una revisión trimestral de veinte oportunidades al azar suele "
        "bastar para detectar la deriva.",
    ],

    "04": [
        "Lead, contacto, cuenta y oportunidad son entidades distintas y su confusión es la causa más común de "
        "datos comerciales inutilizables. Un lead es una persona que aún no se ha calificado; un contacto, "
        "una persona asociada a una cuenta; una cuenta, una organización; una oportunidad, un negocio "
        "concreto con esa organización.",

        "La distinción importa porque las métricas se calculan sobre entidades distintas. La tasa de "
        "conversión de leads no es comparable con la de oportunidades, y sumarlas produce números sin "
        "significado. Cuando dos áreas reportan cifras diferentes del mismo embudo, la causa suele estar "
        "aquí y no en el cálculo.",

        "El modelo debe definir explícitamente las transiciones: cuándo un lead se convierte en contacto y "
        "cuenta, qué pasa con los duplicados, cómo se maneja una persona que cambia de empresa. Esas reglas "
        "parecen técnicas y determinan la calidad de todo el análisis posterior.",

        "Un modelo de datos rico permite análisis sofisticado y exige disciplina de registro que el equipo "
        "puede no sostener. Uno simple se mantiene y limita las preguntas que se pueden responder. La "
        "decisión debe partir de las decisiones de gestión que se quieren tomar, no de las capacidades de la "
        "herramienta.",

        "Las definiciones deben acordarse con las áreas afectadas antes de implementarse, porque determinan "
        "atribución de resultados y por lo tanto compensación. Un cambio en la definición de oportunidad "
        "calificada modifica quién cumple su objetivo. Tratarlo como decisión técnica genera conflictos que "
        "después se atribuyen a otras causas.",
    ],

    "05": [
        "Los datos comerciales se degradan de forma continua: las personas cambian de cargo, las empresas "
        "cambian de nombre, los correos dejan de existir. Una base sin mantenimiento pierde una proporción "
        "significativa de su validez cada año. Ese deterioro es predecible y por lo tanto planificable, "
        "aunque casi nunca se planifica.",

        "La deduplicación es un problema técnico con consecuencias comerciales: dos registros de la misma "
        "cuenta producen contactos duplicados, atribuciones erróneas y la impresión de desorganización ante "
        "el cliente. Su prevención está en las reglas de creación de registros, no en las limpiezas "
        "periódicas, que sólo corrigen el síntoma.",

        "La exactitud se mide con muestreo: tomar un conjunto de registros al azar y verificar campo por "
        "campo contra la realidad. Es un trabajo manual y acotado que entrega una tasa de error por campo. "
        "Esa tasa permite decidir qué campos merecen inversión en corrección y cuáles ya no son confiables "
        "para decidir.",

        "Mantener la calidad exige tiempo que compite con la actividad comercial. Automatizar ayuda y "
        "también introduce errores sistemáticos cuando las reglas están mal definidas. La combinación "
        "razonable automatiza la detección y deja la corrección de casos ambiguos a una persona, con un "
        "tiempo asignado explícito.",

        "La conservación de datos personales tiene límites de plazo y de finalidad. Mantener indefinidamente "
        "registros de contactos que nunca avanzaron no sólo deteriora la base: puede incumplir obligaciones "
        "de conservación. Definir políticas de retención y aplicarlas técnicamente es parte de la higiene, no "
        "un asunto separado.",
    ],

    "06": [
        "La actividad comercial es un indicador adelantado: predice el resultado antes de que ocurra. Andrew "
        "Grove lo formuló en términos generales de producción, y la lógica se aplica directamente al "
        "pipeline: cuando el resultado ya cayó, es tarde para corregir; cuando cae la actividad, todavía hay "
        "tiempo.",

        "La actividad de calidad se distingue de la actividad de vanidad por su relación con el resultado. "
        "Número de llamadas es actividad; número de conversaciones con un decisor calificado es actividad de "
        "calidad. Medir la primera produce equipos que llaman mucho; medir la segunda produce equipos que "
        "preparan sus llamadas.",

        "La relación actividad-resultado debe establecerse con datos propios y revisarse: cuántas "
        "conversaciones producen cuántas oportunidades, cuántas oportunidades producen cuántos cierres. Esa "
        "relación cambia con el mercado y con la saturación de la lista, y usarla desactualizada produce "
        "objetivos de actividad que ya no corresponden.",

        "Exigir más actividad aumenta el volumen y puede deteriorar la calidad si el equipo optimiza el "
        "número. Ese efecto es predecible y por eso todo indicador de actividad debería estar pareado con "
        "uno de calidad. Medir sólo cantidad produce exactamente el comportamiento que la métrica premia.",

        "Los indicadores de actividad son medios y no fines, y confundirlos es el error clásico de la "
        "gestión comercial. Un vendedor que alcanza el resultado con menos actividad no está incumpliendo: "
        "está siendo más eficiente. La actividad se gestiona cuando el resultado falla o cuando se necesita "
        "anticipar, no como objetivo en sí mismo.",
    ],

    "07": [
        "El pronóstico comercial es una estimación con incertidumbre y debería presentarse como tal. La "
        "práctica habitual de reportar un número único esconde el rango y produce conversaciones sobre "
        "precisión que no corresponden. Un pronóstico con rango declarado y supuestos explícitos es más útil "
        "y más honesto.",

        "El sesgo de optimismo está documentado y es sistemático: los pronósticos comerciales tienden a "
        "sobreestimar. Corregirlo con un factor derivado del historial propio —cuánto se sobreestimó en los "
        "últimos ocho trimestres— es más efectivo que pedir realismo, porque actúa sobre el dato y no sobre "
        "la intención.",

        "La precisión del pronóstico se mide y se mejora: error absoluto medio por trimestre, comparado en el "
        "tiempo y por vendedor. Sin esa medición, no hay forma de saber si el pronóstico está mejorando ni de "
        "identificar quién sistemáticamente sobreestima. Es un dato que casi ninguna organización lleva y que "
        "es fácil de construir.",

        "Un pronóstico conservador protege de sorpresas y puede producir decisiones de inversión demasiado "
        "cautelosas; uno optimista habilita inversión y arriesga compromisos que no se cumplen. La solución "
        "es separar el compromiso —lo que se sostiene— del mejor caso, y usar cada uno para decisiones "
        "distintas.",

        "El método de pronóstico debe corresponder a la madurez de los datos. Un modelo ponderado por etapa "
        "requiere probabilidades históricas confiables; sin ellas, produce precisión aparente sobre supuestos "
        "arbitrarios. En operaciones jóvenes, el juicio estructurado con criterios explícitos suele ser "
        "superior al modelo.",
    ],

    "08": [
        "Las cuotas y los territorios determinan la conducta del equipo comercial más que cualquier discurso "
        "de dirección. Una cuota inalcanzable produce desmotivación y rotación; una demasiado baja deja "
        "resultado sobre la mesa. El diseño debe partir del potencial real del territorio y no de la "
        "necesidad de la empresa.",

        "La equidad de oportunidad es la condición para que la comparación entre vendedores signifique algo. "
        "Si un territorio tiene el doble de potencial que otro, la diferencia de resultados no informa sobre "
        "desempeño. Medir el potencial por territorio, aunque sea de forma aproximada, es lo que permite "
        "evaluar con justicia.",

        "La alcanzabilidad se verifica con el historial: qué proporción del equipo alcanzó la cuota en los "
        "últimos periodos. Cuando esa proporción es muy baja de forma sostenida, el problema es de diseño y "
        "no de capacidad. Cuando es muy alta, la cuota dejó de cumplir su función de exigencia.",

        "Cuotas más exigentes empujan el esfuerzo y aumentan el riesgo de conductas indeseadas: descuentos "
        "excesivos al cierre del periodo, ventas a clientes que no calificaban, adelanto de negocios. Ese "
        "efecto es predecible y debe contrapesarse con indicadores de calidad del negocio vendido.",

        "El diseño de territorios y cuotas afecta a las personas de forma directa y su modificación tiene "
        "consecuencias que exceden lo comercial. Los cambios deben comunicarse con anticipación, explicarse "
        "con criterios y, cuando reducen el potencial de alguien, considerarse en el diseño de la transición.",
    ],

    "09": [
        "La capacidad comercial es una restricción física que casi nunca se calcula: cuántas oportunidades "
        "puede atender bien una persona en un periodo. Planificar sobre una capacidad inexistente produce "
        "pipelines saturados, oportunidades mal atendidas y la conclusión errónea de que el equipo no rinde.",

        "El tiempo comercial efectivo es la porción del tiempo que se dedica realmente a actividades con "
        "clientes, y suele ser mucho menor de lo que se supone. Medirlo durante dos semanas —aunque sea de "
        "forma aproximada— revela cuánto se va en tareas administrativas, reuniones internas y coordinación. "
        "Esa medición justifica inversiones en automatización mejor que cualquier argumento.",

        "La rampa de productividad es el tiempo que tarda una persona nueva en alcanzar el desempeño "
        "esperado, y es un dato que debe conocerse para planificar contrataciones. Contratar tres meses antes "
        "de necesitar la capacidad no es previsión excesiva si la rampa es de cuatro meses: es la única forma "
        "de tener la capacidad cuando se necesita.",

        "Aumentar la capacidad contratando produce resultado con retraso y compromete costo fijo inmediato. "
        "Aumentarla mejorando la eficiencia es más lento y no agrega costo estructural. La decisión debe "
        "considerar la rampa, la certeza de la demanda y la reversibilidad, porque revertir una contratación "
        "tiene costos humanos y económicos.",

        "La capacidad del sistema está limitada por el eslabón más restringido, que no siempre es ventas: "
        "puede ser implementación, soporte o producción. Aumentar la capacidad comercial cuando el cuello "
        "está aguas abajo produce ventas que la operación no puede cumplir, lo que es peor que no venderlas.",
    ],

    "10": [
        "La velocidad comercial combina número de oportunidades, valor medio, tasa de cierre y duración del "
        "ciclo en una sola expresión. Su utilidad no está en el número resultante sino en la descomposición: "
        "permite ver cuál de los cuatro factores explica un cambio y cuál ofrece más margen de mejora.",

        "La palanca dominante rara vez es la que el equipo intuye. Reducir el ciclo suele tener un efecto "
        "mayor que aumentar el volumen, y es más barato. Identificarla exige calcular el efecto de una "
        "mejora porcentual equivalente en cada factor, ejercicio simple que cambia la prioridad de las "
        "iniciativas.",

        "La duración del ciclo debe medirse con la mediana y por segmento, porque el promedio se distorsiona "
        "con pocos negocios muy largos. Además, medirla sólo sobre negocios ganados produce un sesgo: los "
        "perdidos también consumieron tiempo, y ese consumo es parte del costo del sistema.",

        "Acelerar el ciclo puede lograrse presionando, lo que deteriora la calidad de la decisión del cliente "
        "y aumenta las bajas posteriores. La aceleración legítima viene de eliminar esperas del proceso "
        "propio: tiempos de respuesta, aprobaciones internas, generación de propuestas. Esa distinción es "
        "importante y suele omitirse.",

        "La velocidad comercial es un indicador agregado y su mejora puede deberse a un cambio de mezcla y "
        "no a una mejora real. Un aumento por mayor proporción de negocios pequeños y rápidos no significa "
        "que el sistema mejoró. Toda lectura debe acompañarse de la evolución de la mezcla.",
    ],

    "11": [
        "Un tablero comercial existe para producir decisiones y no para mostrar información. La prueba es "
        "directa: por cada indicador, preguntar qué decisión cambia según su valor. Los que no responden esa "
        "pregunta ocupan espacio y desvían la atención de los que sí.",

        "La jerarquía del tablero debe corresponder a la audiencia. El indicador que un vendedor necesita a "
        "diario no es el que la dirección necesita mensualmente. Un tablero único para todos termina siendo "
        "demasiado detallado para unos y demasiado agregado para otros, y nadie lo usa.",

        "El rango esperado es lo que convierte un número en información. Un valor sin contexto —sin periodo "
        "anterior, sin meta, sin banda de variación normal— no permite saber si hay que actuar. Incorporar "
        "límites de variación calculados con los propios datos evita reaccionar ante fluctuaciones normales.",

        "Más indicadores entregan más visibilidad y diluyen la atención; menos concentran y pueden ocultar "
        "problemas. La regla práctica es que un tablero de gestión no debería exigir desplazamiento para "
        "verse completo, y que cada indicador debe tener un responsable que actúe cuando se desvía.",

        "Los tableros heredan la calidad de los datos que los alimentan. Un indicador construido sobre un "
        "campo que el equipo completa de forma inconsistente produce una cifra precisa e inexacta. Antes de "
        "publicar un tablero conviene verificar la calidad de sus fuentes, porque una vez publicado se "
        "usará como si fuera confiable.",
    ],

    "12": [
        "La revisión de pipeline es una rutina de gestión y su formato determina su utilidad. Cuando consiste "
        "en recorrer todas las oportunidades una por una, consume horas y produce poco; cuando se concentra "
        "en las que presentan riesgo o requieren decisión, produce acciones. Esa selección debe hacerse antes "
        "de la reunión, no durante.",

        "El riesgo detectado debe nombrarse con precisión: falta de acceso al decisor, ausencia de siguiente "
        "paso, competencia con ventaja, presupuesto no confirmado. Una lista de tipos de riesgo permite "
        "clasificar rápido y evita que la conversación derive hacia el relato de cada negocio.",

        "La decisión de la revisión es su producto: qué se hace con cada oportunidad en riesgo, quién lo hace "
        "y cuándo. Una revisión que termina sin decisiones registradas es una actualización de estado con "
        "otro nombre, y el equipo lo percibe rápidamente como pérdida de tiempo.",

        "Revisiones frecuentes detectan problemas antes y consumen tiempo comercial; espaciadas liberan "
        "tiempo y dejan que los problemas maduren. La frecuencia debe corresponder a la duración del ciclo, y "
        "no a la ansiedad de la dirección, que es lo que suele determinarla en la práctica.",

        "El clima de la revisión determina la calidad de la información. Si señalar un riesgo tiene costo "
        "personal, el equipo aprenderá a no señalarlo y la reunión funcionará con datos optimistas. "
        "Construir un ambiente donde el problema declarado a tiempo se valore más que el problema oculto es "
        "responsabilidad de quien conduce, y es una condición del sistema, no un detalle cultural.",
    ],

    "13": [
        "El gobierno del CRM define quién puede cambiar qué y con qué procedimiento. Su ausencia produce un "
        "sistema que crece por acumulación: campos agregados por proyectos terminados, automatizaciones que "
        "nadie recuerda haber creado, reglas que se contradicen. Ese desorden tiene un costo operativo real y "
        "difícil de revertir.",

        "El responsable del sistema debe estar nombrado y tener tiempo asignado. Cuando la administración del "
        "CRM es una tarea adicional de alguien con otras prioridades, se atienden las urgencias y no el "
        "mantenimiento. Esa configuración produce, en dos o tres años, un sistema que nadie entiende "
        "completo.",

        "El procedimiento de cambio debe distinguir entre modificaciones locales de bajo impacto y cambios "
        "que afectan definiciones, reportes o integraciones. Los primeros deben poder hacerse rápido; los "
        "segundos requieren revisión. Sin esa distinción, o todo se traba o todo se cambia sin control.",

        "Un gobierno estricto protege la integridad y ralentiza la adaptación, lo que empuja a las áreas a "
        "construir soluciones paralelas fuera del sistema. Uno laxo permite agilidad y produce deuda de "
        "configuración. El equilibrio pasa por definir qué es de bajo riesgo y delegarlo explícitamente.",

        "El control de acceso es una obligación además de una buena práctica: los datos comerciales incluyen "
        "información personal y, en algunos casos, información sensible del cliente. Los permisos deben "
        "revisarse periódicamente, especialmente tras cambios de rol y salidas, y esa revisión debe quedar "
        "registrada.",
    ],

    "14": [
        "Diseñar sales operations es construir la infraestructura que permite que el equipo comercial trabaje "
        "sin fricción: procesos, herramientas, datos y reglas. Su valor no se ve cuando funciona; se ve "
        "cuando falta, en forma de tiempo perdido, información inconsistente y decisiones tomadas sobre "
        "supuestos.",

        "La escalabilidad se prueba con una pregunta concreta: qué se rompería si el equipo comercial se "
        "duplicara. Los procesos que dependen de que una persona conozca las excepciones, las reglas no "
        "escritas y las planillas paralelas son los primeros en fallar. Identificarlos antes de crecer es más "
        "barato que descubrirlos durante el crecimiento.",

        "La continuidad exige que el conocimiento esté documentado y no en la cabeza de quien administra el "
        "sistema. La prueba es directa: si esa persona no estuviera disponible durante un mes, qué se "
        "detendría. La respuesta suele señalar exactamente qué documentar primero.",

        "Estandarizar procesos mejora la consistencia y reduce la flexibilidad local que ciertos segmentos "
        "necesitan. Un proceso único para venta a pymes y a sector público obliga a uno de los dos a operar "
        "con un procedimiento que no le sirve. La decisión debe declarar qué se estandariza porque afecta al "
        "resultado y qué se permite variar.",

        "La documentación viva es la que se actualiza porque alguien la usa. Un manual que se escribe una vez "
        "y se archiva contradice la práctica en seis meses y erosiona la confianza en toda la documentación. "
        "Vincular la actualización al procedimiento de cambio —no se aprueba un cambio sin actualizar la "
        "documentación— es el mecanismo que lo mantiene vigente.",
    ],
}
