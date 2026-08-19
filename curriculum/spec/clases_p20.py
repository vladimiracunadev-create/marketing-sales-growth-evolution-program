# -*- coding: utf-8 -*-
"""Parte 20 — Analítica comercial y marketing science."""

CLASES = [
    dict(
        n="01",
        slug="arbol-de-metricas",
        titulo="Árbol de métricas",
        tesis=(
            "Un árbol de métricas descompone el resultado de negocio en factores multiplicativos hasta "
            "llegar a variables sobre las que alguien puede actuar. Su valor es doble: muestra cómo se "
            "conecta cada trabajo con el ingreso y evita discusiones sobre métricas que nadie puede mover. "
            "Kaplan y Norton insistieron en que los indicadores deben estar causalmente conectados, no sólo "
            "agrupados en un tablero."
        ),
        conceptos=[
            ("descomposición multiplicativa", "expresión del resultado como producto de factores medibles"),
            ("variable accionable", "factor del árbol que alguien puede modificar con una decisión"),
            ("nivel de agregación", "grado de detalle en que se descompone cada rama"),
            ("conexión causal", "relación explícita entre un factor y el resultado que afecta"),
        ],
        metodo=[
            "definir el resultado en la cima del árbol",
            "descomponer en factores multiplicativos verificables",
            "continuar hasta llegar a variables accionables",
            "asignar responsable a cada rama",
            "verificar la aritmética con datos reales",
        ],
        senales=[
            ("cobertura del árbol", "ramas con métrica instrumentada, sobre ramas definidas"),
            ("consistencia aritmética", "diferencia entre el resultado calculado por el árbol y el real"),
            ("ramas con responsable", "ramas con dueño asignado, sobre ramas del árbol"),
        ],
        caso=(
            "El tablero de Ruta Andina muestra 34 métricas sin relación entre sí. Nadie puede explicar cómo "
            "el trabajo de contenido afecta el ingreso recurrente."
        ),
        limite=(
            "No todos los factores son multiplicativos ni independientes. Un árbol demasiado simple puede "
            "esconder interacciones importantes entre variables."
        ),
        libros=["kaplan-norton", "croll-yoskovitz", "provost", "kaushik"],
        error=("Agrupar métricas sin conexión causal",
               "Construye la descomposición aritmética y verifica que el cálculo reproduzca el resultado real."),
    ),
    dict(
        n="02",
        slug="conversion-y-funnels",
        titulo="Conversión y embudos",
        tesis=(
            "Una tasa de conversión sin numerador, denominador y ventana definidos es un número sin "
            "significado. La misma etapa puede reportar 12 % o 34 % según se cuente sobre visitas, sesiones "
            "o personas únicas. La disciplina de definición operacional es lo que permite comparar entre "
            "periodos, entre canales y entre equipos sin discutir de qué se está hablando."
        ),
        conceptos=[
            ("definición operacional", "especificación de numerador, denominador, ventana y fuente"),
            ("unidad de análisis", "elección entre visitas, sesiones, personas o cuentas como base del cálculo"),
            ("ventana de conversión", "periodo dentro del cual se considera que la conversión ocurrió"),
            ("comparabilidad", "condición que permite contrastar cifras entre periodos o canales"),
        ],
        metodo=[
            "definir la unidad de análisis y justificarla",
            "especificar numerador, denominador y ventana",
            "documentar la fuente de cada componente",
            "verificar la comparabilidad antes de contrastar",
            "publicar las definiciones junto con las cifras",
        ],
        senales=[
            ("conversión con definición documentada", "métricas con definición publicada, sobre métricas reportadas"),
            ("diferencia entre unidades de análisis", "variación de la tasa según la unidad usada, en el mismo periodo"),
            ("consistencia entre informes", "diferencia entre la misma tasa reportada por dos áreas"),
        ],
        caso=(
            "Marketing reporta 3,2 % de conversión sobre sesiones y ventas calcula 0,9 % sobre personas "
            "únicas. Ambos hablan del mismo embudo en la misma reunión."
        ),
        limite=(
            "Las definiciones no pueden cambiarse retroactivamente sin recalcular la serie. Un cambio de "
            "definición rompe la comparabilidad histórica y debe declararse."
        ),
        libros=["kaushik", "croll-yoskovitz", "provost", "wheeler-dv"],
        error=("Reportar tasas sin unidad de análisis declarada",
               "Publica numerador, denominador, ventana y fuente junto a cada tasa."),
    ),
    dict(
        n="03",
        slug="cac",
        titulo="Costo de adquisición de cliente",
        tesis=(
            "El costo de adquisición debe incluir todo el gasto necesario para conseguir un cliente nuevo: "
            "medios, herramientas, sueldos comerciales y de marketing, comisiones. Excluir sueldos es el "
            "error más común y el más caro, porque produce una economía aparente que no resiste una revisión "
            "financiera. El cálculo debe hacerse por segmento y por canal, no sólo agregado."
        ),
        conceptos=[
            ("alcance del costo", "conjunto de gastos incluidos en el cálculo, declarado por escrito"),
            ("costo por canal", "gasto atribuible dividido por clientes nuevos originados en ese canal"),
            ("periodo de atribución", "desfase entre el gasto y la incorporación del cliente que produce"),
            ("costo mixto", "promedio que combina canales con economías muy distintas"),
        ],
        metodo=[
            "declarar el alcance del cálculo por escrito",
            "atribuir el gasto a canales y segmentos",
            "considerar el desfase entre gasto e incorporación",
            "calcular por canal y por segmento",
            "conciliar el total con la contabilidad",
        ],
        senales=[
            ("costo de adquisición por canal", "gasto atribuible dividido por clientes nuevos, por canal"),
            ("dispersión entre canales", "diferencia entre el canal más caro y el más barato"),
            ("conciliación con contabilidad", "diferencia entre el gasto usado en el cálculo y el registrado contablemente"),
        ],
        caso=(
            "Ruta Andina reporta un costo de adquisición de CLP 310.000. Al incluir los sueldos del equipo "
            "comercial y de marketing, la cifra real supera CLP 700.000."
        ),
        limite=(
            "El costo promedio esconde diferencias entre canales. Escalar sobre el promedio puede significar "
            "aumentar el gasto en el canal menos eficiente."
        ),
        libros=["croll-yoskovitz", "provost", "fader-ltv", "kaushik"],
        error=("Excluir sueldos del cálculo",
               "Declara el alcance completo, incluye remuneraciones y concilia con contabilidad."),
    ),
    dict(
        n="04",
        slug="ltv",
        titulo="Valor de vida del cliente",
        tesis=(
            "El valor de vida es una proyección del margen que un cliente aportará durante su relación. Sus "
            "componentes son margen, permanencia esperada y expansión, y cada uno introduce incertidumbre. "
            "Fader advierte contra el uso de fórmulas simples con supuestos de retención constante: la "
            "retención varía por cohorte y por segmento, y el promedio agregado distorsiona la estimación."
        ),
        conceptos=[
            ("margen de contribución del cliente", "ingreso menos costos variables de servirlo, por periodo"),
            ("permanencia esperada", "duración estimada de la relación, derivada de curvas de retención"),
            ("heterogeneidad", "diferencia sustantiva de valor entre clientes del mismo segmento aparente"),
            ("tasa de descuento", "ajuste que refleja el valor temporal del dinero en la proyección"),
        ],
        metodo=[
            "calcular el margen de contribución con costos completos",
            "estimar permanencia desde curvas de retención por cohorte",
            "incorporar expansión y contracción observadas",
            "aplicar tasa de descuento y declarar supuestos",
            "presentar el resultado como rango y no como cifra única",
        ],
        senales=[
            ("valor de vida por segmento", "margen acumulado esperado, por segmento y cohorte"),
            ("dispersión dentro del segmento", "diferencia entre percentiles de valor dentro del mismo segmento"),
            ("sensibilidad a la retención", "variación del valor de vida ante un cambio de un punto en retención"),
        ],
        caso=(
            "El valor de vida que usa Ruta Andina supone retención constante de 96 % mensual. Sus cohortes "
            "reales muestran caídas de 8 % en los primeros meses y estabilización posterior."
        ),
        limite=(
            "Con cohortes jóvenes, la proyección tiene error alto. Presentarla como cifra única induce "
            "decisiones de inversión sobre una precisión inexistente."
        ),
        libros=["fader-ltv", "fader", "provost", "croll-yoskovitz"],
        error=("Proyectar con retención constante",
               "Deriva la permanencia de curvas por cohorte y presenta el resultado como rango."),
    ),
    dict(
        n="05",
        slug="payback",
        titulo="Periodo de recuperación",
        tesis=(
            "El periodo de recuperación indica cuántos meses tarda el margen de un cliente en cubrir su costo "
            "de adquisición. Es más útil que la relación entre valor de vida y costo para decidir ritmo de "
            "inversión, porque habla directamente de caja. Una empresa con recuperación de 18 meses y caja "
            "para 6 no puede escalar aunque su valor de vida sea excelente."
        ),
        conceptos=[
            ("periodo de recuperación", "meses hasta que el margen acumulado iguala el costo de adquisición"),
            ("restricción de caja", "límite de inversión impuesto por la liquidez disponible"),
            ("ritmo sostenible de adquisición", "volumen de clientes nuevos que la caja permite financiar"),
            ("relación con la vida del cliente", "comparación entre recuperación y permanencia esperada"),
        ],
        metodo=[
            "calcular el margen mensual por cliente",
            "determinar el periodo de recuperación por segmento",
            "compararlo con la vida media observada",
            "estimar el ritmo sostenible según la caja disponible",
            "ajustar la meta de adquisición a esa restricción",
        ],
        senales=[
            ("periodo de recuperación por segmento", "meses hasta recuperar el costo de adquisición, por segmento"),
            ("relación recuperación-permanencia", "periodo de recuperación dividido por vida media del cliente"),
            ("clientes financiables por periodo", "caja disponible del periodo, dividida por el costo de adquisición por cliente del segmento"),
        ],
        caso=(
            "Ruta Andina recupera su inversión en 14 meses y su vida media de cliente es 11. Cada cliente "
            "nuevo destruye caja antes de aportar."
        ),
        limite=(
            "El periodo de recuperación ignora el valor posterior. Un negocio con recuperación larga puede ser "
            "excelente si la permanencia es muy alta y hay financiamiento."
        ),
        libros=["croll-yoskovitz", "fader-ltv", "provost", "simon"],
        error=("Escalar con recuperación mayor que la vida del cliente",
               "Compara ambos indicadores por segmento antes de aumentar la inversión en adquisición."),
    ),
    dict(
        n="06",
        slug="contribution-margin",
        titulo="Margen de contribución",
        tesis=(
            "El margen de contribución es lo que queda del ingreso después de los costos variables y es la "
            "base de cualquier análisis comercial serio. Su cálculo exige decidir qué costos son "
            "efectivamente variables: soporte, implementación, comisiones y despacho suelen serlo aunque se "
            "registren como gasto fijo. Un margen mal calculado invalida todo lo que se construya encima."
        ),
        conceptos=[
            ("costo variable", "gasto que cambia con el volumen de clientes o de transacciones"),
            ("margen de contribución", "ingreso menos costos variables, en monto y en porcentaje"),
            ("costo escalonado", "gasto que se comporta como fijo en tramos y salta al superar un umbral"),
            ("margen por segmento", "contribución calculada separadamente para cada grupo de clientes"),
        ],
        metodo=[
            "clasificar cada costo como variable, escalonado o fijo",
            "atribuir los costos variables a clientes y segmentos",
            "calcular el margen por segmento y por producto",
            "identificar los segmentos con margen negativo",
            "validar el resultado con contabilidad",
        ],
        senales=[
            ("margen de contribución por segmento", "ingreso menos costos variables, sobre ingreso, por segmento"),
            ("segmentos con margen negativo", "segmentos con contribución bajo cero, sobre segmentos activos"),
            ("diferencia con la contabilidad", "brecha entre el margen calculado y el reportado contablemente"),
        ],
        caso=(
            "El plan más vendido de Ruta Andina muestra 62 % de margen bruto. Al incluir las 9 horas de "
            "migración y el soporte del primer trimestre, la contribución real es 12 %."
        ),
        limite=(
            "La distinción entre costo fijo y variable depende del horizonte. En el largo plazo, casi todos "
            "los costos son variables y el análisis debe declarar su horizonte."
        ),
        libros=["croll-yoskovitz", "provost", "nagle", "simon"],
        error=("Tratar soporte e implementación como costo fijo",
               "Atribuye las horas de servicio a los clientes que las consumen y recalcula el margen por segmento."),
    ),
    dict(
        n="07",
        slug="cohort-analysis",
        titulo="Análisis de cohortes aplicado",
        tesis=(
            "El análisis de cohortes es la herramienta que permite distinguir mejora real de efecto de "
            "mezcla. Aplicado a ingreso, muestra si las cohortes nuevas valen más que las anteriores; "
            "aplicado a comportamiento, revela si los cambios de producto funcionan. Su exigencia es "
            "metodológica: comparar en el mismo hito de antigüedad y no en la misma fecha calendario."
        ),
        conceptos=[
            ("hito de antigüedad", "punto de comparación medido desde la incorporación y no desde la fecha"),
            ("efecto de mezcla", "distorsión del agregado producida por cambios en la composición de la base"),
            ("cohorte de comportamiento", "agrupación por acción realizada y no sólo por fecha de ingreso"),
            ("maduración", "tiempo necesario para que una cohorte permita conclusiones confiables"),
        ],
        metodo=[
            "definir el criterio de cohorte según la pregunta",
            "construir la matriz de cohortes con datos propios",
            "comparar en el mismo hito de antigüedad",
            "atribuir diferencias a cambios conocidos",
            "declarar qué cohortes aún no maduran",
        ],
        senales=[
            ("valor acumulado por cohorte", "margen acumulado por cliente, por cohorte y hito"),
            ("tendencia entre cohortes", "dirección del cambio entre cohortes sucesivas en el mismo hito"),
            ("cohortes con datos suficientes", "cohortes con antigüedad mínima para concluir, sobre cohortes analizadas"),
        ],
        caso=(
            "El ingreso promedio por cliente de Ruta Andina sube. Al analizar por cohorte se ve que las "
            "cohortes nuevas valen menos y el promedio sube porque las antiguas expandieron."
        ),
        limite=(
            "El análisis de cohortes requiere volumen suficiente por grupo. Con pocas incorporaciones "
            "mensuales, conviene agrupar por trimestre."
        ),
        libros=["croll-yoskovitz", "fader", "provost", "kaushik"],
        error=("Comparar cohortes en la misma fecha calendario",
               "Compara siempre en el mismo hito de antigüedad desde la incorporación."),
    ),
    dict(
        n="08",
        slug="attribution-models",
        titulo="Modelos de atribución",
        tesis=(
            "Los modelos de atribución reparten el crédito entre puntos de contacto según una regla "
            "convencional. Ninguno mide causalidad: describen correlación con una convención declarada. Su "
            "uso correcto es comparativo —ver cómo cambia la lectura según el modelo— y su uso incorrecto es "
            "tratarlos como verdad para asignar presupuesto sin verificación causal."
        ),
        conceptos=[
            ("modelo basado en reglas", "convención fija que reparte el crédito según posición o decaimiento"),
            ("modelo basado en datos", "asignación derivada del análisis de recorridos observados"),
            ("ventana de contacto", "periodo dentro del cual se consideran los puntos de contacto"),
            ("límite causal", "imposibilidad de establecer causalidad con datos observacionales de atribución"),
        ],
        metodo=[
            "declarar el modelo y la ventana utilizados",
            "comparar la lectura bajo al menos dos modelos",
            "identificar los canales cuyo crédito varía más",
            "diseñar verificación causal para los casos críticos",
            "publicar las limitaciones junto con los resultados",
        ],
        senales=[
            ("variación de crédito entre modelos", "diferencia del crédito asignado a cada canal según modelo"),
            ("cobertura de recorridos completos", "conversiones con recorrido registrado completo, sobre conversiones totales"),
            ("decisiones respaldadas por verificación causal", "decisiones de presupuesto con prueba causal, sobre decisiones mayores"),
        ],
        caso=(
            "Bajo último clic, la búsqueda de marca de Ruta Andina recibe 61 % del crédito; bajo un modelo "
            "lineal, 28 %. El presupuesto se asigna con el primero sin discusión."
        ),
        limite=(
            "La reducción de cobertura de rastreo por privacidad afecta a todos los modelos. Los recorridos "
            "incompletos sesgan sistemáticamente hacia los canales de último contacto."
        ),
        libros=["kaushik", "kohavi", "provost", "binet-field"],
        error=("Tratar la atribución como evidencia causal",
               "Compara modelos y valida con experimentos los canales donde la decisión es costosa."),
    ),
    dict(
        n="09",
        slug="incrementalidad",
        titulo="Incrementalidad",
        tesis=(
            "La incrementalidad responde la única pregunta que importa para decidir presupuesto: qué habría "
            "pasado sin esta inversión. Se estima con experimentos —grupos de control geográficos, "
            "suspensión de campañas, asignación aleatoria— y casi siempre revela que el efecto real es menor "
            "que el atribuido. Su costo es la complejidad; su beneficio es evitar escalar lo que no funciona."
        ),
        conceptos=[
            ("efecto incremental", "resultado que no habría ocurrido sin la intervención"),
            ("grupo de control", "conjunto comparable que no recibe la intervención"),
            ("prueba de suspensión", "experimento que apaga una inversión para medir su efecto real"),
            ("costo del experimento", "ingreso resignado durante la prueba para obtener la información"),
        ],
        metodo=[
            "identificar la inversión cuyo efecto se quiere verificar",
            "diseñar el grupo de control comparable",
            "calcular la duración necesaria para detectar el efecto",
            "ejecutar y medir la diferencia con intervalo",
            "decidir la asignación con el resultado obtenido",
        ],
        senales=[
            ("efecto incremental estimado", "diferencia entre grupo tratado y control, con intervalo de confianza"),
            ("proporción de resultado incremental", "efecto incremental, sobre resultado atribuido por el modelo de atribución"),
            ("costo del experimento", "ingreso resignado durante la prueba, comparado con el presupuesto en revisión"),
        ],
        caso=(
            "Ruta Andina suspendió su campaña de marca durante cuatro semanas en dos regiones comparables. "
            "El ingreso cayó 4 %, no el 38 % que la atribución le asignaba."
        ),
        limite=(
            "Los experimentos de incrementalidad tienen costo real y requieren volumen. En presupuestos "
            "pequeños, la información puede costar más que la decisión que informa."
        ),
        libros=["kohavi", "provost", "kaushik", "binet-field"],
        error=("Asignar presupuesto sin verificación de incrementalidad en las decisiones mayores",
               "Diseña una prueba de suspensión para los canales que concentran el gasto."),
    ),
    dict(
        n="10",
        slug="a-b-testing",
        titulo="A/B testing",
        tesis=(
            "El A/B test es la herramienta más confiable para establecer causalidad en marketing digital y "
            "también la más mal usada. Los errores frecuentes son conocidos: muestras insuficientes, "
            "detención temprana, comparaciones múltiples y contaminación. Kohavi documenta que la mayoría de "
            "las mejoras declaradas en la industria no se replican, lo que sugiere un problema sistemático "
            "de método más que de suerte."
        ),
        conceptos=[
            ("significancia estadística", "probabilidad de observar el resultado si no existiera efecto real"),
            ("efecto mínimo detectable", "magnitud más pequeña que el test puede identificar con la muestra"),
            ("comparaciones múltiples", "aumento de falsos positivos al evaluar varias métricas o variantes"),
            ("replicación", "confirmación del resultado al repetir el experimento"),
        ],
        metodo=[
            "definir hipótesis, métrica principal y guardarraíles",
            "calcular muestra y duración antes de iniciar",
            "ejecutar sin mirar resultados parciales",
            "analizar con el criterio previo y corregir por comparaciones múltiples",
            "replicar los resultados que sostienen decisiones importantes",
        ],
        senales=[
            ("potencia calculada antes de iniciar", "tests con cálculo previo de muestra, sobre tests ejecutados"),
            ("tasa de replicación", "resultados confirmados al repetir, sobre resultados positivos"),
            ("tests detenidos anticipadamente", "pruebas interrumpidas antes del plazo, sobre pruebas ejecutadas"),
        ],
        caso=(
            "Ruta Andina evaluó siete métricas en un mismo test y declaró victoria por la única que resultó "
            "favorable. Con siete comparaciones, ese resultado es esperable por azar."
        ),
        limite=(
            "Un test bien ejecutado establece causalidad sólo en el contexto probado. Extrapolar a otro "
            "segmento, canal o temporada exige una nueva verificación."
        ),
        libros=["kohavi", "provost", "laja", "wheeler-dv"],
        error=("Evaluar múltiples métricas y declarar victoria por la favorable",
               "Declara una métrica principal antes de iniciar y corrige por comparaciones múltiples."),
    ),
    dict(
        n="11",
        slug="forecasting",
        titulo="Proyección de resultados",
        tesis=(
            "Proyectar resultados comerciales exige distinguir tendencia, estacionalidad y ruido. El error "
            "habitual es extrapolar el último trimestre, que confunde variación aleatoria con dirección. "
            "Wheeler ofrece el criterio operativo: antes de proyectar, determinar si el proceso es estable; "
            "si no lo es, ninguna proyección es válida."
        ),
        conceptos=[
            ("tendencia", "dirección sostenida de una serie más allá de la variación aleatoria"),
            ("estacionalidad", "patrón recurrente asociado al calendario"),
            ("estabilidad del proceso", "condición en que la variación se mantiene dentro de límites previsibles"),
            ("intervalo de proyección", "rango dentro del cual se espera el resultado futuro"),
        ],
        metodo=[
            "verificar la estabilidad de la serie histórica",
            "separar tendencia, estacionalidad y ruido",
            "elegir el método de proyección según los datos disponibles",
            "presentar el resultado como intervalo",
            "medir la precisión de las proyecciones anteriores",
        ],
        senales=[
            ("precisión de proyecciones previas", "diferencia entre proyectado y real, por periodo"),
            ("amplitud del intervalo", "rango de la proyección, comparado con la magnitud del valor proyectado"),
            ("estabilidad de la serie", "puntos dentro de los límites de variación esperada, sobre puntos totales de la serie"),
        ],
        caso=(
            "Ruta Andina proyecta el año extrapolando el mejor trimestre de su historia, que coincidió con "
            "una campaña puntual que no se repetirá."
        ),
        limite=(
            "Ningún método proyecta cambios estructurales: la entrada de un competidor o un cambio "
            "regulatorio invalidan la serie histórica."
        ),
        libros=["wheeler-dv", "provost", "hubbard", "croll-yoskovitz"],
        error=("Extrapolar el último periodo",
               "Verifica la estabilidad de la serie y presenta la proyección como intervalo con supuestos declarados."),
    ),
    dict(
        n="12",
        slug="marketing-mix-modeling-fundamentos",
        titulo="Fundamentos de marketing mix modeling",
        tesis=(
            "El modelado de mezcla de marketing estima el efecto de cada inversión sobre las ventas usando "
            "datos agregados y series temporales, sin depender de identificadores individuales. Eso lo hace "
            "atractivo en un contexto de restricciones de privacidad. Sus exigencias son altas: requiere "
            "historia suficiente, variación real en las inversiones y control de factores externos. Sin esas "
            "condiciones, produce coeficientes sin sentido."
        ),
        conceptos=[
            ("modelo agregado", "estimación basada en series temporales y no en datos individuales"),
            ("variación necesaria", "cambios en el gasto que permiten identificar el efecto de cada canal"),
            ("factor externo", "variable no controlada que afecta las ventas y debe incluirse"),
            ("saturación", "punto donde la inversión adicional produce retornos decrecientes"),
        ],
        metodo=[
            "verificar la disponibilidad de historia y de variación",
            "identificar los factores externos relevantes",
            "estimar el modelo con validación fuera de muestra",
            "interpretar los coeficientes con cautela",
            "contrastar con experimentos de incrementalidad",
        ],
        senales=[
            ("historia disponible", "meses de datos comparables, comparados con el mínimo requerido"),
            ("variación del gasto por canal", "coeficiente de variación de la inversión mensual, por canal"),
            ("capacidad predictiva fuera de muestra", "error de predicción en periodos no usados para estimar"),
        ],
        caso=(
            "Ruta Andina tiene 19 meses de historia y ha mantenido el mismo presupuesto por canal todo ese "
            "tiempo. Sin variación, el modelo no puede identificar efectos separados."
        ),
        limite=(
            "El modelado agregado requiere volumen y estabilidad organizacional. En empresas pequeñas con "
            "pocos meses de historia, la inversión no se justifica."
        ),
        libros=["provost", "kohavi", "binet-field", "hubbard"],
        error=("Estimar el modelo sin variación en las inversiones",
               "Verifica que exista variación suficiente por canal antes de invertir en el modelado."),
    ),
    dict(
        n="13",
        slug="dashboards-ejecutivos",
        titulo="Dashboards ejecutivos",
        tesis=(
            "Un tablero ejecutivo debe responder en un minuto: cómo vamos frente al plan, qué cambió y qué "
            "decisión se requiere. Su diseño exige jerarquía, contexto —comparación con periodo anterior y "
            "con meta— y rangos de variación esperada. Un tablero sin contexto convierte cada fluctuación "
            "normal en una alarma y agota la capacidad de atención de la dirección."
        ),
        conceptos=[
            ("contexto comparativo", "referencia frente a periodo anterior, meta o límite esperado"),
            ("jerarquía visual", "orden que refleja la importancia de las decisiones que informa"),
            ("banda de variación esperada", "rango dentro del cual la fluctuación no requiere acción"),
            ("decisión requerida", "acción que el tablero solicita explícitamente cuando algo se desvía"),
        ],
        metodo=[
            "definir las decisiones que el tablero debe habilitar",
            "seleccionar pocos indicadores con contexto",
            "establecer bandas de variación esperada",
            "señalar explícitamente qué requiere decisión",
            "verificar el uso real con la dirección",
        ],
        senales=[
            ("tiempo de lectura", "minutos que tarda un ejecutivo en identificar el estado y las decisiones"),
            ("indicadores con banda definida", "métricas con rango esperado, sobre métricas del tablero"),
            ("decisiones tomadas con el tablero", "decisiones documentadas que lo citan, por trimestre"),
        ],
        caso=(
            "El tablero que Ruta Andina presenta al directorio tiene 18 gráficos sin metas ni comparaciones. "
            "La reunión se consume preguntando si cada variación es buena o mala."
        ),
        limite=(
            "Un tablero ejecutivo no reemplaza el análisis: señala dónde mirar. Las decisiones complejas "
            "requieren un documento con contexto y alternativas."
        ),
        libros=["kaplan-norton", "wheeler-dv", "kaushik", "grove"],
        error=("Presentar cifras sin meta ni comparación",
               "Agrega contexto comparativo y banda de variación esperada a cada indicador."),
    ),
    dict(
        n="14",
        slug="caso-analitico-integral",
        titulo="Caso analítico integral",
        tesis=(
            "Esta clase integra la parte en un análisis completo: árbol de métricas, economía unitaria por "
            "segmento, cohortes, atribución contrastada, incrementalidad donde corresponda y una "
            "recomendación de asignación. La prueba de calidad es la auditabilidad: cada cifra debe poder "
            "rastrearse hasta su fuente y cada supuesto debe estar declarado."
        ),
        conceptos=[
            ("análisis auditable", "estudio donde cada cifra puede rastrearse hasta su fuente"),
            ("supuesto declarado", "afirmación no verificada que se explicita junto al resultado"),
            ("recomendación de asignación", "propuesta de distribución de recursos derivada del análisis"),
            ("condición de revisión", "resultado que obligaría a modificar la recomendación"),
        ],
        metodo=[
            "construir el árbol y la economía unitaria por segmento",
            "analizar cohortes y contrastar modelos de atribución",
            "verificar causalidad donde la decisión lo justifique",
            "formular la recomendación con supuestos declarados",
            "definir la condición que la haría cambiar",
        ],
        senales=[
            ("cifras trazables", "cifras con fuente identificada, sobre cifras del análisis"),
            ("supuestos declarados", "supuestos explicitados, sobre supuestos utilizados"),
            ("decisiones adoptadas", "decisiones formalizadas que citan el análisis, en 60 días"),
        ],
        caso=(
            "El directorio de Ruta Andina debe decidir la asignación de CLP 120 millones entre adquisición, "
            "retención y producto. Requiere un análisis que resista preguntas de un director financiero."
        ),
        limite=(
            "Un análisis impecable no elimina la incertidumbre ni sustituye la decisión. Su función es hacer "
            "explícito el razonamiento y sus límites."
        ),
        libros=["provost", "croll-yoskovitz", "kohavi", "hubbard"],
        error=("Presentar conclusiones sin trazabilidad de las cifras",
               "Adjunta la fuente de cada cifra y la lista de supuestos con su nivel de evidencia."),
    ),
]
