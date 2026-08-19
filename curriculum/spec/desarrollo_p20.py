# -*- coding: utf-8 -*-
"""Desarrollo escrito de la Parte 20 — Analítica comercial y marketing science."""

DESARROLLO = {

    "01": [
        "Un árbol de métricas descompone el resultado en factores que se multiplican o se suman hasta llegar "
        "a variables sobre las que alguien puede actuar. Su valor está en la trazabilidad: permite responder "
        "por qué cambió el resultado sin recurrir a hipótesis, siguiendo la descomposición hasta el factor "
        "que se movió.",

        "La variable accionable es el punto donde el árbol debe detenerse. Descomponer hasta un nivel que "
        "nadie controla produce un diagrama elegante e inútil. La prueba es preguntar, en cada hoja del "
        "árbol, quién puede modificarla y con qué palanca; si no hay respuesta, hay que seguir descomponiendo "
        "o reconocer que es una variable externa.",

        "El nivel de agregación debe ser consistente en toda la descomposición: mezclar métricas mensuales "
        "con acumuladas, o de cliente con de transacción, produce árboles que no cierran aritméticamente. "
        "Verificar que las operaciones efectivamente reconstruyen el total es un control básico que revela "
        "errores de definición.",

        "Un árbol detallado permite diagnóstico fino y se vuelve difícil de mantener y de comunicar. Uno "
        "grueso se entiende y no localiza la causa. La solución practicable es un árbol de dos o tres "
        "niveles para gestión y ramas detalladas que se abren sólo cuando hay que diagnosticar un tramo "
        "específico.",

        "La conexión entre niveles del árbol es aritmética y no causal. Que el resultado se descomponga en "
        "esos factores no significa que actuar sobre uno produzca el efecto proporcional: pueden existir "
        "compensaciones. Confundir descomposición con causalidad lleva a prometer resultados que la "
        "aritmética sugiere y el sistema no entrega.",
    ],

    "02": [
        "Medir conversión exige tres definiciones previas: qué cuenta como entrada, qué cuenta como "
        "conversión y en qué ventana. Sin las tres, dos personas calculan cifras distintas de la misma "
        "operación y ambas tienen razón. La mayoría de las discusiones sobre tasas de conversión son en "
        "realidad discusiones sobre definiciones no explicitadas.",

        "La unidad de análisis determina qué significa el número: conversión por visita, por visitante o por "
        "sesión son métricas distintas que pueden moverse en direcciones opuestas. Elegir la unidad "
        "corresponde a la decisión que se quiere tomar, y esa elección debe declararse en la ficha junto con "
        "el resto.",

        "La comparabilidad entre periodos exige que la mezcla de tráfico sea similar. Una tasa que mejora "
        "porque aumentó la proporción de visitantes recurrentes no indica que la página mejorara. Segmentar "
        "por origen antes de comparar es lo que evita atribuir a la gestión lo que produjo el cambio de "
        "composición.",

        "Ventanas de conversión largas capturan más conversiones y atribuyen a un contacto efectos que "
        "pudieron tener otras causas; ventanas cortas subestiman. La elección debe corresponder al ciclo de "
        "compra observado, y ese dato hay que medirlo en lugar de adoptar el valor por defecto de la "
        "herramienta.",

        "Una tasa de conversión describe una relación entre dos conteos y no explica nada por sí sola. Su "
        "valor aparece en la comparación —con periodos anteriores, entre segmentos, contra una línea base— y "
        "siempre acompañada del volumen absoluto, porque una tasa excelente sobre pocas unidades puede ser "
        "irrelevante para el negocio.",
    ],

    "03": [
        "El costo de adquisición de cliente parece simple y es una de las métricas peor calculadas. Su "
        "definición exige decidir qué costos se incluyen —sólo medios, o también sueldos, herramientas y "
        "comisiones—, qué periodo se considera y cómo se atribuyen los costos compartidos entre canales.",

        "El alcance del costo debe ser completo si el número va a compararse con el valor del cliente. Un "
        "cálculo que sólo incluye gasto en medios subestima de forma considerable y produce decisiones de "
        "inversión equivocadas. La versión completa suele ser incómoda y es la única defendible.",

        "El costo por canal exige atribuir, y la atribución es imperfecta. Una forma honesta de manejarlo es "
        "reportar el costo mixto —total de gasto sobre total de clientes nuevos— junto con las estimaciones "
        "por canal, declarando el modelo de atribución usado. El costo mixto no se puede discutir; el por "
        "canal siempre es una estimación.",

        "Optimizar el costo de adquisición favorece los canales de captura de demanda existente y penaliza "
        "los que construyen demanda futura, cuyo efecto no aparece en la ventana de medición. Esa asimetría "
        "es estructural y debe compensarse con una decisión explícita de asignación, no esperando que los "
        "datos la corrijan.",

        "El costo de adquisición sólo significa algo comparado con el valor que ese cliente genera. Un costo "
        "alto puede ser excelente si la permanencia es larga, y uno bajo puede ser ruinoso si el cliente se "
        "va en tres meses. Presentar el costo sin su contraparte es una de las prácticas más engañosas de "
        "los tableros comerciales.",
    ],

    "04": [
        "El valor de vida del cliente es una proyección y no un dato. Se construye con supuestos sobre "
        "margen, permanencia y comportamiento futuro, y su precisión depende por completo de la calidad de "
        "esos supuestos. Presentarlo como una cifra exacta oculta que es un modelo, y los modelos se "
        "discuten por sus supuestos.",

        "La heterogeneidad es el punto que Peter Fader ha insistido en subrayar: los clientes no valen lo "
        "mismo y el promedio describe a pocos. Un valor de vida medio calculado sobre una base con "
        "distribución muy dispersa induce decisiones equivocadas, porque lleva a tratar igual a clientes cuyo "
        "valor difiere en un orden de magnitud.",

        "La permanencia esperada es el supuesto más frágil y debe estimarse con datos de cohortes y no con "
        "una tasa de baja promedio invertida. Ese atajo —dividir uno entre la tasa de baja— supone una tasa "
        "constante que casi nunca se cumple, porque el riesgo de baja es mayor al principio y disminuye "
        "después.",

        "Un modelo más elaborado captura mejor la heterogeneidad y es más difícil de explicar y de mantener. "
        "Uno simple se comunica y sobreestima o subestima según el caso. La decisión debe considerar para qué "
        "se usará: para decidir cuánto invertir en adquisición basta un modelo grueso con rango; para "
        "priorizar cuentas individuales hace falta más.",

        "Todo cálculo de valor de vida debe declarar sus supuestos y su sensibilidad. Un cambio pequeño en la "
        "permanencia esperada modifica el resultado de forma considerable, y esa fragilidad es la "
        "información más importante que el análisis puede entregar. Sin ella, la cifra se usa como si fuera "
        "un hecho.",
    ],

    "05": [
        "El periodo de recuperación —cuánto tarda el margen de un cliente en cubrir lo que costó "
        "adquirirlo— es la métrica que gobierna la velocidad sostenible de crecimiento. Un negocio puede "
        "tener una relación favorable entre valor y costo y aun así quebrar, si el dinero tarda demasiado en "
        "volver.",

        "La restricción de caja es lo que hace de esta métrica una decisión y no un dato: con recursos "
        "limitados, el periodo de recuperación determina cuántos clientes nuevos se pueden financiar por "
        "periodo. En el caso de Ruta Andina, catorce meses de recuperación contra once de permanencia "
        "describe un sistema que consume caja con cada venta.",

        "El cálculo debe usar margen de contribución y no ingreso, e incluir el costo de servir. Usar ingreso "
        "produce un periodo aparentemente corto que no corresponde a la realidad de la caja. La ficha debe "
        "declarar qué se incluyó, porque la diferencia entre ambas versiones puede ser de varios meses.",

        "Reducir el periodo de recuperación puede lograrse subiendo precio, cobrando por adelantado o "
        "bajando el costo de adquisición. Cada opción tiene efectos secundarios: el cobro anticipado mejora "
        "la caja y puede reducir la conversión. Modelar ese intercambio antes de decidir evita resolver un "
        "problema creando otro.",

        "La métrica supone que la permanencia se mantiene durante el periodo de recuperación, y ese supuesto "
        "hay que verificarlo. Cuando el periodo excede la permanencia mediana, el negocio está estructurado "
        "para perder dinero con cada cliente, y ninguna optimización de canal lo corrige.",
    ],

    "06": [
        "El margen de contribución es lo que queda de cada peso vendido después de los costos que varían con "
        "esa venta. Es la base de casi toda decisión comercial —qué promover, qué descontar, a quién "
        "servir— y su cálculo depende de clasificar correctamente los costos, tarea menos obvia de lo que "
        "parece.",

        "El costo escalonado complica el análisis: hay costos que no varían con cada unidad pero sí saltan "
        "al superar un umbral —una persona más de soporte, un servidor adicional—. Tratarlos como fijos "
        "subestima el costo del crecimiento; tratarlos como variables lo sobreestima. Registrar dónde están "
        "los escalones es la forma correcta.",

        "El margen por segmento suele revelar diferencias grandes que el promedio esconde. Un segmento con "
        "buen precio y alto costo de servir puede tener margen menor que otro más barato y autónomo. Ese "
        "análisis, hecho una vez, suele reordenar la prioridad comercial más que cualquier estudio de "
        "mercado.",

        "Maximizar el margen unitario puede reducir el margen total si el volumen cae más de lo "
        "proporcional. La decisión correcta optimiza la contribución total y no el porcentaje, distinción "
        "que se pierde con facilidad cuando el indicador de gestión es el margen porcentual.",

        "El margen de contribución no incluye costos fijos y por lo tanto no indica rentabilidad. Un negocio "
        "puede tener margen de contribución positivo en todas sus líneas y perder dinero. Presentarlo como "
        "medida de rentabilidad es un error frecuente en presentaciones comerciales y produce decisiones de "
        "portafolio equivocadas.",
    ],

    "07": [
        "El análisis por cohortes aplicado a la operación comercial responde preguntas que el agregado no "
        "puede: si los clientes nuevos se comportan mejor o peor que los anteriores, si una intervención "
        "cambió algo, si el deterioro observado es real o sólo efecto de mezcla. Ninguna de esas preguntas "
        "tiene respuesta en un promedio, porque el promedio mezcla grupos con historias distintas y presenta "
        "el resultado como si describiera a un cliente típico que no existe.",

        "El efecto de mezcla es el fenómeno que más conclusiones falsas produce en analítica comercial: un "
        "indicador agregado puede mejorar mientras todos los grupos empeoran, si cambia la proporción entre "
        "grupos. Detectarlo requiere descomponer siempre por cohorte antes de concluir sobre una tendencia.",

        "El hito de antigüedad es la unidad de comparación correcta: comparar todas las cohortes en su tercer "
        "mes, no en el mes calendario. Esa alineación permite ver si las cohortes recientes rinden mejor, que "
        "es la pregunta de gestión relevante. Compararlas en el mismo mes calendario mezcla antigüedades y no "
        "informa.",

        "Cohortes más finas entregan mayor resolución y grupos más pequeños donde el ruido domina. Con "
        "volúmenes bajos, la agregación trimestral o semestral produce lecturas más estables. La elección "
        "debe basarse en el volumen disponible y declararse, porque cambiar la granularidad cambia la "
        "apariencia de los resultados.",

        "El análisis por cohortes describe lo ocurrido y su capacidad predictiva supone continuidad de las "
        "condiciones. Cambios de precio, de segmento o de producto rompen la comparabilidad entre cohortes "
        "anteriores y posteriores. Registrar esos cambios en la misma vista es lo que permite interpretar las "
        "diferencias correctamente.",
    ],

    "08": [
        "Los modelos de atribución reparten el crédito de una conversión entre los contactos que la "
        "precedieron. Ninguno es verdadero: son convenciones con supuestos distintos. Elegir uno es aceptar "
        "un sesgo determinado, y lo profesional es declararlo en lugar de presentar el resultado como un "
        "hecho.",

        "Los modelos basados en reglas —último clic, primero, lineal, con decaimiento— son transparentes y "
        "arbitrarios. Los basados en datos son menos arbitrarios y opacos, y requieren volumen suficiente "
        "para entrenarse. La elección debe considerar quién usará el resultado: un modelo que nadie puede "
        "explicar no sostiene una decisión de presupuesto.",

        "La ventana de contacto define qué interacciones se consideran parte del recorrido. Una ventana corta "
        "en un ciclo largo excluye los contactos iniciales y sobreatribuye al cierre. Ajustarla al ciclo "
        "observado es un cambio simple que suele modificar sustancialmente la imagen de contribución de los "
        "canales.",

        "Modelos más sofisticados reparten mejor y consumen tiempo de implementación y mantenimiento, además "
        "de exigir datos de calidad. En operaciones con volúmenes moderados, la sofisticación no compensa: "
        "es preferible un modelo simple con la ventana correcta y una prueba de incrementalidad para las "
        "decisiones grandes.",

        "La atribución mide asociación temporal y no causa. Ningún modelo responde qué habría pasado sin esa "
        "inversión, que es la pregunta de gestión. Cuando la decisión es significativa, la atribución debe "
        "complementarse con un diseño experimental, y ese límite hay que declararlo cada vez que se presenta "
        "un informe de atribución.",
    ],

    "09": [
        "La incrementalidad responde la pregunta que la atribución no puede: cuántas de esas conversiones no "
        "habrían ocurrido sin la inversión. Su medición requiere un grupo que no reciba el tratamiento, y esa "
        "condición es la que la vuelve incómoda: implica renunciar deliberadamente a alcanzar a una parte de "
        "la audiencia.",

        "La prueba de suspensión —dejar de invertir en un canal o zona durante un periodo y comparar— es el "
        "diseño más accesible. Su costo es real y calculable: el ingreso perdido durante la prueba. Ese costo "
        "debe compararse con el valor de saber si la inversión sostenida durante todo el año está "
        "produciendo efecto.",

        "El grupo de control debe ser comparable en composición y estar sujeto a las mismas condiciones "
        "externas. Separar por zona geográfica es lo más común y exige verificar que las zonas eran "
        "comparables antes del experimento, comparándolas en el periodo previo.",

        "Medir incrementalidad con frecuencia entrega mejor información y consume ingreso y tiempo. La "
        "práctica razonable la reserva para las inversiones grandes y sostenidas, donde un error de "
        "atribución tiene consecuencias significativas, y acepta la atribución convencional para el resto.",

        "Un resultado de incrementalidad vale para el periodo, el mercado y el nivel de inversión en que se "
        "midió. La incrementalidad no es constante: puede ser alta con inversión baja y caer al aumentar el "
        "gasto. Extrapolarla a otro nivel de inversión es un supuesto adicional que debe declararse.",
    ],

    "10": [
        "Las pruebas comparativas son la herramienta más confiable para establecer causa en marketing "
        "digital, y también la más maltratada. Los problemas rara vez son de fórmula: son de diseño, de "
        "ejecución y de interpretación. Una prueba mal ejecutada produce un número con apariencia "
        "estadística y sin validez.",

        "La significancia estadística indica la probabilidad de observar esa diferencia si no hubiera "
        "efecto real; no indica magnitud ni importancia práctica. Una diferencia significativa puede ser "
        "irrelevante para el negocio, y una no significativa puede deberse a muestra insuficiente. Reportar "
        "ambas cosas —el efecto estimado y su incertidumbre— es la práctica correcta.",

        "Las comparaciones múltiples aumentan la probabilidad de encontrar un resultado por azar. Probar "
        "cinco variantes y quedarse con la mejor produce falsos positivos con frecuencia mucho mayor de la "
        "que sugiere el umbral nominal. Corregirlo requiere ajustar el criterio o reducir el número de "
        "comparaciones.",

        "Detener una prueba al ver un resultado favorable garantiza quedarse con los falsos positivos. La "
        "disciplina de fijar duración y tamaño antes y respetarlos cuesta, porque siempre hay presión por "
        "consolidar un buen número. Esa disciplina es lo que distingue un programa de experimentación de una "
        "serie de anécdotas.",

        "La replicación es lo que separa un hallazgo de una casualidad. Una proporción significativa de "
        "resultados positivos no se sostiene al repetirse. Los cambios importantes deberían replicarse antes "
        "de incorporarse como conocimiento establecido, y esa práctica es rara precisamente porque los "
        "resultados favorables no se cuestionan.",
    ],

    "11": [
        "Proyectar resultados exige separar tendencia, estacionalidad y ruido. La mayoría de las "
        "proyecciones comerciales fallan por confundir los tres: se toma una racha favorable como tendencia y "
        "se extrapola. Donald Wheeler propuso una disciplina básica que evita ese error: distinguir "
        "variación común de variación especial antes de interpretar.",

        "La estabilidad del proceso es la condición para proyectar. Si la serie muestra variación especial "
        "—cambios de nivel, saltos, rachas fuera de los límites naturales— la proyección basada en el "
        "promedio no tiene sentido. Verificar la estabilidad antes de proyectar es un paso que casi nunca se "
        "ejecuta.",

        "El intervalo de proyección es tan importante como el valor central y debe presentarse siempre. Una "
        "proyección puntual induce una precisión que el dato no tiene y produce compromisos que después no se "
        "cumplen. La versión honesta declara el rango y la probabilidad asociada.",

        "Proyecciones más elaboradas capturan mejor los patrones y son más difíciles de auditar y de "
        "explicar. En contextos comerciales, un modelo simple con supuestos visibles suele producir mejores "
        "decisiones que uno complejo, porque permite discutir los supuestos en lugar de confiar en el "
        "resultado.",

        "Toda proyección supone que las condiciones se mantienen, y ese supuesto es el que falla. Un cambio "
        "de competencia, de regulación o de comportamiento invalida el modelo sin previo aviso. Declarar qué "
        "condiciones se suponen y qué señales indicarían que dejaron de cumplirse convierte la proyección en "
        "una herramienta de gestión y no en una predicción.",
    ],

    "12": [
        "El modelado de la mezcla de marketing estima la contribución de cada inversión al resultado usando "
        "datos agregados en el tiempo, sin depender del seguimiento individual. Esa independencia lo ha "
        "vuelto atractivo con las restricciones crecientes de medición, y también reintroduce dificultades "
        "que el seguimiento individual permitía ignorar.",

        "La variación necesaria es su condición fundamental: si la inversión en un canal fue constante "
        "durante todo el periodo, el modelo no puede estimar su efecto. Esa limitación es matemática y no se "
        "resuelve con más datos. Planificar variación deliberada en la inversión es lo que hace posible el "
        "modelado posterior.",

        "Los factores externos —estacionalidad, precio, competencia, contexto económico— deben incorporarse o "
        "el modelo atribuirá al marketing lo que produjeron ellos. En Chile, además, los efectos "
        "estacionales de enero y febrero son marcados en varios sectores y omitirlos distorsiona cualquier "
        "estimación.",

        "Un modelo agregado captura efectos de largo plazo que el seguimiento individual pierde, y no permite "
        "optimizar a nivel de campaña. Ambos enfoques son complementarios y responden preguntas distintas. "
        "Presentar uno como sustituto del otro produce expectativas que no se cumplirán.",

        "La saturación —el punto donde la inversión adicional rinde cada vez menos— es uno de los aportes "
        "más útiles del método y también uno de los más sensibles a la especificación. Estimarla exige haber "
        "observado niveles de inversión suficientemente distintos; sin esa variación, la curva estimada es "
        "poco más que el supuesto que se impuso.",
    ],

    "13": [
        "Un tablero ejecutivo tiene un propósito distinto del operativo: no sirve para gestionar el día sino "
        "para detectar desviaciones que requieren decisión de dirección. Esa diferencia determina qué "
        "contiene, con qué frecuencia se actualiza y con qué nivel de agregación se presenta.",

        "El contexto comparativo es lo que convierte un número en información: periodo anterior, meta, banda "
        "de variación esperada. Un valor solo no permite saber si hay que actuar. Incorporar límites "
        "calculados a partir de la propia variación histórica evita que la dirección reaccione ante "
        "fluctuaciones normales.",

        "La decisión requerida debería estar explícita en el tablero: qué se espera que decida quien lo mira. "
        "Un tablero que sólo informa produce reuniones de revisión sin acuerdos. Incluir, junto a cada "
        "desviación relevante, la decisión pendiente y su responsable transforma el instrumento.",

        "Más información entrega contexto y diluye la atención de quien tiene poco tiempo; menos concentra y "
        "puede ocultar. Para dirección, la regla práctica es una vista que se lea en pocos minutos, con "
        "capacidad de profundizar bajo demanda. Un tablero ejecutivo que requiere explicación no cumple su "
        "función.",

        "Los tableros heredan la calidad de sus fuentes y la de las definiciones. Un indicador construido "
        "sobre un campo inconsistente produce una cifra precisa e inexacta que la dirección usará como si "
        "fuera confiable. Documentar la definición y la fuente de cada indicador es parte del tablero y no "
        "un anexo.",
    ],

    "14": [
        "Un análisis comercial integral se juzga por su auditabilidad: si otra persona, con los mismos datos, "
        "puede reconstruir el camino y llegar a conclusiones comparables. Esa propiedad exige conservar los "
        "pasos intermedios y no sólo el resultado, y es lo que distingue un análisis de una presentación.",

        "El supuesto declarado es la unidad de honestidad del análisis. Todo trabajo relevante contiene "
        "supuestos —de atribución, de permanencia, de comparabilidad— y ocultarlos no los elimina, sólo "
        "impide discutirlos. Listarlos al inicio, con su justificación, mejora la calidad de la discusión y "
        "protege al analista.",

        "La recomendación de asignación debe expresarse como decisión y no como observación: cuánto mover, "
        "desde dónde, hacia dónde y con qué criterio de revisión. Un análisis que termina describiendo la "
        "situación deja la parte difícil a quien tiene menos información, que es exactamente al revés de lo "
        "que corresponde.",

        "Un análisis exhaustivo cubre más y llega tarde; uno rápido llega a tiempo y omite. Como las "
        "decisiones tienen fecha, la profundidad debe ajustarse al plazo disponible y las omisiones deben "
        "declararse. Entregar tarde un análisis perfecto es una forma de no participar en la decisión.",

        "La condición de revisión cierra el trabajo: qué evidencia futura obligaría a revisar la "
        "recomendación y cuándo se volverá a mirar. Sin ella, la decisión queda vigente por inercia y el "
        "análisis se convierte en una justificación permanente en lugar de una recomendación con horizonte.",
    ],
}
