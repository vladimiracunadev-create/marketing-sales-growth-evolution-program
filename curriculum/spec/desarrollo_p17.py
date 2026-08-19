# -*- coding: utf-8 -*-
"""Desarrollo escrito de la Parte 17 — Marketing automation y revenue operations."""

DESARROLLO = {

    "01": [
        "Automatizar un proceso desordenado produce desorden a mayor velocidad. La condición previa a "
        "cualquier automatización es que el proceso esté estandarizado: que se sepa qué pasos existen, quién "
        "los ejecuta y qué se hace con las excepciones. Saltarse ese paso es la causa más frecuente de "
        "automatizaciones que hay que desactivar meses después.",

        "El modo de falla debe anticiparse antes de implementar: qué ocurre si el dato de entrada está "
        "incompleto, si el sistema externo no responde, si la condición se cumple dos veces. Un flujo sin "
        "manejo de excepciones no falla ruidosamente: falla en silencio, y el problema se detecta cuando "
        "alguien nota que algo no ocurrió durante semanas.",

        "La detección de falla exige un mecanismo activo. Confiar en que alguien lo notará equivale a "
        "descubrir los problemas por reclamo del cliente, que es la forma más cara. Un control mínimo "
        "verifica periódicamente que los volúmenes procesados estén dentro de un rango esperado y alerta "
        "cuando no lo están.",

        "Automatizar más libera tiempo y aumenta la superficie de fallas silenciosas y la dependencia de "
        "configuraciones que pocos entienden. Automatizar menos conserva control y consume tiempo en tareas "
        "repetitivas. El criterio razonable automatiza lo repetitivo y de bajo riesgo, y mantiene revisión "
        "humana donde el error tiene consecuencias para el cliente.",

        "La reversibilidad debe estar contemplada: cómo se detiene un flujo, cómo se corrige lo que ya "
        "ejecutó, quién tiene autoridad para hacerlo. Una automatización que envió mil comunicaciones "
        "erróneas necesita un procedimiento de contención definido antes del incidente, no improvisado "
        "durante.",
    ],

    "02": [
        "Las etapas de ciclo de vida describen la relación con una persona u organización a lo largo del "
        "tiempo, más allá de una oportunidad puntual. Su función es permitir que cada área sepa en qué "
        "estado está cada registro y qué corresponde hacer. Sin ellas, marketing y ventas operan sobre la "
        "misma base con criterios distintos.",

        "El criterio de transición entre etapas debe ser explícito y automatizable, o no se aplicará de forma "
        "consistente. «Cuando muestra interés» no es un criterio; «cuando solicita una demostración o "
        "descarga el documento de precios» sí lo es. La precisión aquí determina la utilidad de todos los "
        "informes de embudo.",

        "El estado terminal —qué pasa con quien no avanza— es la parte que suele faltar. Sin él, los "
        "registros se acumulan indefinidamente en etapas intermedias y las métricas de conversión se "
        "deterioran sin que nadie entienda por qué. Definir cuándo un registro sale del ciclo y a dónde va es "
        "parte del diseño.",

        "Más etapas entregan visibilidad y aumentan el mantenimiento y la probabilidad de inconsistencia; "
        "menos etapas simplifican y ocultan transiciones relevantes. La cantidad debe responder a qué "
        "decisiones se toman en cada punto: una etapa que no dispara ninguna acción distinta no justifica "
        "existir.",

        "El modelo de ciclo de vida describe un recorrido idealizado. Las personas retroceden, se van y "
        "vuelven, cambian de organización. Forzar un avance lineal produce datos que no reflejan la realidad. "
        "El diseño debe permitir retrocesos y registrarlos, porque esa información es diagnóstica.",
    ],

    "03": [
        "El puntaje de leads intenta responder a quién atender primero. Su utilidad depende por completo de "
        "que se valide contra resultados reales: si los leads con puntaje alto no convierten mejor que los de "
        "puntaje bajo, el modelo no está informando nada y su uso es peor que no tener modelo, porque "
        "transmite falsa confianza.",

        "El puntaje de ajuste y el de comportamiento miden cosas distintas y deben mantenerse separados. El "
        "ajuste describe si la organización corresponde al perfil; el comportamiento, si hay señales de "
        "interés activo. Una empresa perfecta sin actividad y una empresa fuera de perfil muy activa "
        "requieren tratamientos opuestos, y un puntaje único los confunde.",

        "La validación se hace comparando la tasa de conversión real por tramo de puntaje. Si los tramos no "
        "se separan, el modelo no discrimina. Esa verificación debe repetirse periódicamente porque el "
        "comportamiento cambia: un modelo validado hace dos años puede haber dejado de funcionar sin que "
        "nadie lo note.",

        "Un modelo más complejo puede capturar mejor las señales y se vuelve imposible de explicar al equipo "
        "comercial, que entonces lo ignora. Uno simple se entiende y se usa, aunque discrimine algo menos. En "
        "la práctica, un modelo simple que el equipo comprende suele producir mejores resultados que uno "
        "sofisticado que nadie cree.",

        "Un modelo entrenado con datos históricos reproduce los sesgos de la operación pasada: si "
        "históricamente sólo se atendió a cierto tipo de cuenta, el modelo aprenderá que ese tipo convierte. "
        "Esa retroalimentación puede cerrar el mercado sin que nadie lo decida. Revisar qué segmentos quedan "
        "sistemáticamente con puntaje bajo es un control necesario.",
    ],

    "04": [
        "El enrutamiento define quién atiende cada contacto y en cuánto tiempo, y su efecto sobre la "
        "conversión es directo. Un lead calificado que espera dos días pierde una parte importante de su "
        "valor. Las reglas deben estar escritas, automatizadas y monitoreadas, no depender de la "
        "disponibilidad de quien esté mirando.",

        "El tiempo de asignación y el tiempo de primer contacto son métricas distintas y ambas importan. Un "
        "sistema puede asignar en segundos y el vendedor contactar al día siguiente. Medir sólo la primera "
        "produce la ilusión de un proceso rápido; la que importa comercialmente es la segunda.",

        "La cobertura de asignación —qué proporción de los contactos recibió efectivamente atención dentro "
        "del plazo comprometido— es el indicador de salud del sistema. Cuando cae, la causa suele ser "
        "capacidad insuficiente y no falla técnica, y la solución correcta es ajustar el umbral de traspaso "
        "o la capacidad, no insistir con recordatorios.",

        "Reglas más finas asignan mejor y aumentan la complejidad y los casos sin regla aplicable. Reglas "
        "simples cubren todo y reparten peor. Toda configuración necesita una regla por defecto explícita "
        "para los casos no previstos, porque los casos no previstos siempre aparecen y sin regla quedan sin "
        "atender.",

        "El escalamiento debe estar definido: qué ocurre si el asignado no contacta en el plazo. Sin esa "
        "regla, los contactos no atendidos permanecen asignados indefinidamente y el sistema reporta "
        "cobertura completa mientras nadie los trabaja. Es una de las fallas silenciosas más comunes.",
    ],

    "05": [
        "El acompañamiento por contenido busca sostener la relación con quien todavía no está listo para "
        "comprar. Funciona cuando cada envío aporta algo utilizable; se vuelve contraproducente cuando "
        "consiste en recordar la existencia de la empresa. La diferencia se refleja en la evolución de las "
        "bajas y de la interacción a lo largo de la secuencia.",

        "La pertinencia por etapa exige que el contenido corresponda al momento del destinatario. Enviar "
        "material de comparación de proveedores a quien recién descubre el problema es tan inútil como enviar "
        "contenido introductorio a quien ya está evaluando alternativas. Esa correspondencia es lo que "
        "distingue una secuencia diseñada de una lista de envíos.",

        "El avance de etapa es la métrica que evalúa la secuencia: qué proporción de quienes entran progresa "
        "a la etapa siguiente en un plazo definido. Medir sólo aperturas y clics evalúa el correo, no el "
        "programa. Y cuando el avance es cercano a cero, el problema suele estar en la audiencia y no en el "
        "contenido.",

        "Secuencias más largas mantienen presencia y aumentan la fatiga; más cortas respetan y pueden "
        "perder a quien necesitaba más tiempo. La duración debe corresponder al ciclo de compra observado y "
        "no a la cantidad de contenido disponible, que es lo que suele determinarla.",

        "La comunicación debe corresponder a la finalidad para la que la persona entregó sus datos. Usar una "
        "suscripción a contenido técnico para enviar promociones excede esa finalidad y, además de deteriorar "
        "la relación, puede constituir un incumplimiento normativo. La revisión del marco vigente es previa "
        "al diseño de la secuencia.",
    ],

    "06": [
        "Un flujo automatizado se define por sus condiciones de entrada y de salida, y ambas deben ser "
        "explícitas. Un flujo sin condición de salida clara puede mantener a una persona recibiendo "
        "comunicaciones indefinidamente, incluso después de haberse convertido en cliente, que es una de las "
        "fallas más visibles para quien la sufre.",

        "La prueba en ambiente controlado antes de activar es una práctica básica y frecuentemente omitida "
        "por presión de tiempo. Consiste en ejecutar el flujo con registros de prueba que cubran los casos "
        "límite: dato faltante, condición cumplida dos veces, persona ya en otro flujo. Esa prueba toma horas "
        "y evita incidentes que toman semanas de reparación.",

        "La documentación del flujo debe existir fuera de la herramienta: qué hace, por qué se creó, quién lo "
        "pidió, qué se espera de él y cuándo revisarlo. Sin esa documentación, en dos años nadie sabrá si un "
        "flujo activo sigue siendo necesario, y la opción cómoda —dejarlo— es la que acumula deuda.",

        "Flujos más elaborados cubren más casos y son más difíciles de depurar y de modificar. Flujos simples "
        "se entienden y dejan casos sin cubrir. La recomendación práctica es preferir varios flujos simples y "
        "documentados a uno complejo con muchas ramas, aunque la segunda opción parezca más elegante.",

        "Toda automatización que se comunica con personas debe tener un responsable identificable y un "
        "mecanismo de detención inmediata. Cuando ocurre un error, la pregunta «quién puede apagar esto» "
        "debe tener respuesta en segundos. Verificarlo antes de activar es parte del procedimiento y no una "
        "formalidad.",
    ],

    "07": [
        "El acuerdo de servicio entre marketing y ventas convierte una discusión recurrente en un compromiso "
        "medible. Define qué es un lead calificado, cuántos se entregarán, en qué plazo se contactarán y qué "
        "información se devolverá. Sin ese acuerdo, cada área atribuye a la otra las pérdidas del embudo y la "
        "conversación se repite cada trimestre.",

        "La definición compartida de lead calificado es la pieza central y la más difícil de acordar, porque "
        "determina quién cumple su objetivo. Debe construirse con datos: qué características tenían los leads "
        "que efectivamente se convirtieron. Esa evidencia desplaza la discusión desde las preferencias hacia "
        "los hechos.",

        "El compromiso debe ser bilateral y medido en ambas direcciones: marketing entrega volumen y calidad, "
        "ventas atiende en plazo y devuelve información de calificación. Medir sólo un lado convierte el "
        "acuerdo en una exigencia unilateral que la otra parte dejará de cumplir en cuanto tenga presión.",

        "Un acuerdo exigente mejora la disciplina y puede volverse rígido cuando cambian las condiciones del "
        "mercado. Debe incluir una cláusula de revisión con periodicidad definida y un mecanismo para "
        "ajustarlo sin conflicto, porque las condiciones cambian y un acuerdo que no se puede ajustar se "
        "incumple en silencio.",

        "El acuerdo describe compromisos entre áreas y no reemplaza la responsabilidad compartida por el "
        "resultado. Cuando se convierte en un instrumento para asignar culpa —«cumplimos nuestra parte»— ha "
        "dejado de servir. Su función es coordinar, y esa función exige que ambas partes respondan también "
        "por el resultado conjunto.",
    ],

    "08": [
        "El modelo de datos de ingresos define qué entidades existen, cómo se relacionan y cuál es la fuente "
        "autoritativa de cada dato. Es la decisión de arquitectura con mayor efecto sobre la capacidad "
        "analítica de la organización, y suele tomarse implícitamente al configurar la primera herramienta.",

        "La fuente autoritativa debe ser única por dato: si el ingreso puede consultarse en el CRM, en "
        "facturación y en una planilla, las tres cifras diferirán y ninguna será confiable. Declarar cuál "
        "manda y hacer que las demás la reflejen es un trabajo tedioso que resuelve la mayoría de las "
        "discusiones sobre números.",

        "El estado válido de cada entidad debe estar definido y restringido: qué combinaciones de campos son "
        "posibles y cuáles no. Sin esas restricciones, el sistema acumula registros en estados imposibles "
        "—oportunidades cerradas sin fecha de cierre, cuentas activas sin contacto— que después distorsionan "
        "todo análisis.",

        "Un modelo rico permite responder más preguntas y exige disciplina de registro y mantenimiento. Uno "
        "simple se sostiene y limita el análisis. La decisión debe partir de las preguntas de gestión "
        "efectivas y no de las capacidades de la herramienta, que siempre ofrecerán más de lo necesario.",

        "La deuda de datos se acumula con cada excepción no resuelta y con cada campo agregado sin "
        "definición. Se paga con intereses cuando hay que migrar de sistema o construir un análisis nuevo. "
        "Medirla —proporción de registros con campos críticos vacíos o inconsistentes— la vuelve visible y "
        "gestionable.",
    ],

    "09": [
        "Las integraciones son el punto donde los sistemas comerciales dejan de ser islas, y también donde se "
        "originan la mayoría de los problemas de datos. Cada integración es un acuerdo sobre qué información "
        "fluye, en qué dirección, con qué frecuencia y qué ocurre cuando falla.",

        "La dirección de sincronización debe definirse por campo y no por sistema. Un mismo registro puede "
        "tener campos cuya fuente autoritativa es el CRM y otros cuya fuente es facturación. Sincronizar todo "
        "en ambas direcciones produce conflictos donde el último en escribir gana, que es la peor regla "
        "posible.",

        "El manejo de errores debe estar diseñado: qué pasa con un registro que no se pudo sincronizar, dónde "
        "queda, quién lo revisa. Sin ese diseño, los errores se acumulan en un registro que nadie mira y la "
        "divergencia entre sistemas crece silenciosamente hasta que alguien nota una diferencia grande.",

        "Sincronizar más datos entrega una visión completa y multiplica los puntos de falla y el costo de "
        "mantenimiento. Sincronizar menos simplifica y obliga a consultar varios sistemas. La decisión debe "
        "basarse en qué datos se necesitan efectivamente en cada sistema para tomar decisiones allí, no en "
        "la aspiración de tenerlo todo en todas partes.",

        "El monitoreo de integraciones debe ser activo y con alerta: volumen procesado, tasa de error, "
        "latencia. Descubrir una integración caída porque alguien notó que faltaban datos es descubrirla "
        "tarde. Ese monitoreo es barato de implementar y es la diferencia entre un problema de horas y uno "
        "de semanas.",
    ],

    "10": [
        "El embudo de ingresos unifica en una sola vista lo que marketing, ventas y éxito de cliente miden "
        "por separado. Su valor está en hacer visible el ciclo completo: no sólo cuántos entran sino cuántos "
        "permanecen y cuánto expanden. Sin esa vista, cada área optimiza su tramo y el conjunto puede "
        "deteriorarse.",

        "La definición compartida por etapa es la condición para que el embudo signifique algo. Cuando "
        "marketing cuenta contactos y ventas cuenta oportunidades con criterios distintos, la conversión "
        "entre ambas es un número sin interpretación. Acordar esas definiciones es trabajo previo a construir "
        "cualquier tablero.",

        "La pérdida por tramo debe medirse en unidades y en valor, porque un tramo con alta pérdida "
        "porcentual sobre pocas unidades puede importar menos que uno con pérdida moderada sobre muchas. "
        "Presentar sólo porcentajes conduce sistemáticamente a priorizar mal.",

        "Una vista unificada facilita la coordinación y puede diluir la responsabilidad: cuando todos "
        "responden por el embudo completo, nadie responde por su tramo. El diseño debe mantener "
        "responsabilidad por tramo y visibilidad del conjunto, no sustituir la primera por la segunda.",

        "El embudo unificado supone que el recorrido es secuencial, y en negocios con expansión y recompra no "
        "lo es: un cliente puede estar simultáneamente en renovación y en una nueva oportunidad. Forzar la "
        "linealidad simplifica el tablero y distorsiona la realidad. Reconocer el límite y complementar con "
        "vistas específicas es preferible.",
    ],

    "11": [
        "Un pronóstico unificado separa los componentes del ingreso porque cada uno se comporta distinto: "
        "ingreso nuevo, renovación, expansión y contracción tienen predictibilidad y responsables diferentes. "
        "Sumarlos en una sola cifra oculta que el error de pronóstico puede venir de un solo componente.",

        "La renovación es el componente más predecible y el que menos atención recibe en el proceso de "
        "pronóstico, porque suele darse por supuesta. Modelarla explícitamente —con tasa histórica por "
        "segmento y por antigüedad— mejora la precisión total más que refinar el pronóstico de ingreso "
        "nuevo.",

        "La precisión por componente debe medirse por separado. Un pronóstico global con error aceptable "
        "puede estar compensando una sobreestimación de nuevo con una subestimación de renovación, y esa "
        "compensación no se repetirá. Medir por componente permite corregir donde está el problema.",

        "Un proceso de pronóstico detallado mejora la precisión y consume tiempo de muchas personas cada "
        "periodo. La inversión se justifica cuando las decisiones dependen del pronóstico —contratación, "
        "inversión, compromisos financieros— y no cuando el pronóstico sólo se reporta.",

        "La contracción —clientes que reducen su consumo sin irse— es el componente que más se omite y que "
        "puede explicar una parte relevante de la desviación. Su medición exige comparar el mismo cliente "
        "consigo mismo en el tiempo, no comparar totales. Incorporarla al pronóstico suele revelar un "
        "deterioro que el ingreso agregado ocultaba.",
    ],

    "12": [
        "La observabilidad del sistema comercial consiste en poder detectar que algo dejó de funcionar antes "
        "de que lo note el cliente. Sin ella, los problemas se descubren por reclamo, que además de ser la "
        "vía más costosa es la que más daña la relación.",

        "El indicador de salud del sistema debe medir el flujo y no sólo el estado: cuántos registros se "
        "procesaron, cuántos correos se enviaron, cuántas asignaciones ocurrieron. Un descenso abrupto en "
        "esos volúmenes es la señal más temprana de una falla, y detectarlo requiere conocer el rango "
        "normal.",

        "La alerta accionable se distingue del ruido por una condición: quien la recibe sabe qué hacer. Un "
        "sistema que emite muchas alertas de bajo valor entrena al equipo a ignorarlas, y entonces la alerta "
        "importante también se ignora. Menos alertas y mejor calibradas es casi siempre la configuración "
        "correcta.",

        "Monitorear más entrega mayor cobertura y aumenta el ruido y el costo de mantenimiento del propio "
        "monitoreo. La regla práctica es monitorear aquello cuya falla tiene consecuencia para el cliente o "
        "para el ingreso, y aceptar que lo demás se detectará por revisión periódica.",

        "El tiempo medio de recuperación es la métrica que resume la capacidad de respuesta: cuánto pasa "
        "entre que algo falla y que vuelve a funcionar. Medirlo obliga a registrar los incidentes, y ese "
        "registro es lo que permite identificar fallas recurrentes que merecen una corrección estructural en "
        "lugar de una reparación repetida.",
    ],

    "13": [
        "La gobernanza de las automatizaciones responde a una pregunta que se vuelve urgente con el tiempo: "
        "quién puede crear, modificar o apagar un proceso que se comunica con clientes. Sin autoridad "
        "definida, las automatizaciones se multiplican y nadie tiene la visión del conjunto ni la capacidad "
        "de detenerlas.",

        "El registro de tratamiento —qué datos se usan, para qué finalidad, durante cuánto tiempo, con qué "
        "base de licitud— es una obligación normativa y también una herramienta de gestión. Mantenerlo "
        "actualizado obliga a saber qué automatizaciones existen, lo que resuelve indirectamente el problema "
        "del inventario.",

        "La revisión periódica debe cubrir tres preguntas por cada automatización activa: sigue siendo "
        "necesaria, sigue funcionando como se diseñó, sigue cumpliendo el marco normativo. Sin esa revisión, "
        "el sistema acumula procesos que hacen cosas que nadie recuerda haber decidido.",

        "Controles estrictos reducen el riesgo y ralentizan la operación, empujando a las áreas a construir "
        "soluciones fuera del sistema gobernado, que es el peor resultado. El diseño equilibrado define "
        "niveles: cambios de bajo riesgo con registro posterior, cambios que afectan comunicación con "
        "clientes con aprobación previa.",

        "El retiro de automatizaciones es tan importante como su creación y casi nunca se planifica. Una "
        "automatización creada para una campaña terminada que sigue activa puede producir comunicaciones "
        "incoherentes durante años. Incluir una fecha de revisión obligatoria al momento de crear resuelve "
        "buena parte del problema.",
    ],

    "14": [
        "Un modelo operativo de ingresos describe cómo trabajan juntas las áreas que producen ingreso: qué "
        "procesos existen, quién responde por cada uno, con qué información y con qué ritmo. Es el documento "
        "que permite que la coordinación no dependa de las relaciones personales entre jefaturas.",

        "La cifra única es el acuerdo de que existe una fuente autoritativa para cada indicador relevante y "
        "que todas las áreas la usan. Parece obvio y es raro: en la mayoría de las organizaciones, marketing, "
        "ventas y finanzas reportan cifras distintas del mismo concepto, y las reuniones empiezan "
        "reconciliando.",

        "La responsabilidad por proceso debe estar asignada de extremo a extremo y no por tramo. Cuando cada "
        "área responde por su parte, los traspasos quedan sin dueño y ahí es donde se pierde la mayor parte "
        "del valor. Nombrar un responsable del proceso completo, aunque no dirija a todos los equipos, "
        "cambia la dinámica.",

        "Un modelo operativo detallado alinea y puede volverse burocrático si no se ajusta al tamaño de la "
        "organización. En equipos pequeños, la formalización excesiva consume más de lo que aporta. El "
        "criterio es formalizar lo que ya produce fricción y dejar lo demás en acuerdos simples.",

        "El ritmo de gestión —qué se revisa semanalmente, mensualmente, trimestralmente— es parte del modelo "
        "y no un detalle de calendario. Un sistema sin ritmo definido revisa cuando hay problemas, que es "
        "siempre tarde. Definir el ritmo y sostenerlo es una de las pocas prácticas cuya ausencia se nota "
        "inmediatamente en los resultados.",
    ],
}
