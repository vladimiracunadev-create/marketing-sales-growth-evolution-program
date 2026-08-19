# -*- coding: utf-8 -*-
"""Desarrollo escrito de la Parte 21 — IA aplicada a marketing, ventas y servicio."""

DESARROLLO = {

    "01": [
        "Antes de decidir qué automatizar con inteligencia artificial hay que describir la tarea con "
        "precisión: qué entra, qué sale, cómo se sabe si el resultado es correcto y quién responde si no lo "
        "es. Stuart Russell y Peter Norvig plantean esa descripción como definición de agente racional, y su "
        "utilidad práctica es que obliga a explicitar la medida de desempeño antes de elegir tecnología.",

        "El tipo de sistema importa: no es lo mismo un modelo que clasifica, uno que genera texto y uno que "
        "ejecuta acciones. Cada uno tiene modos de falla distintos y exige controles distintos. Tratar todos "
        "los usos bajo la misma categoría produce políticas que son excesivas para unos e insuficientes para "
        "otros.",

        "El criterio de éxito debe definirse antes y ser medible con datos que existan. «Mejorar la "
        "productividad» no es un criterio; «reducir el tiempo de preparación de una propuesta manteniendo la "
        "tasa de errores por debajo del nivel actual» sí lo es. Sin criterio previo, cualquier resultado se "
        "interpretará como éxito.",

        "Automatizar más libera tiempo y traslada el error a un lugar menos visible: un sistema que se "
        "equivoca de forma consistente produce daño a escala antes de que alguien lo note. La decisión debe "
        "considerar el costo del error multiplicado por el volumen, no sólo el ahorro de tiempo.",

        "La responsabilidad humana no se transfiere al sistema. Quien despliega una herramienta responde por "
        "sus resultados frente al cliente y frente al regulador. Esa asignación debe ser explícita y "
        "nominal antes del despliegue, porque después del incidente la discusión sobre quién respondía se "
        "vuelve estéril.",
    ],

    "02": [
        "Un buen prompt comercial es una especificación: contexto suficiente, tarea concreta, formato "
        "esperado y criterio de aceptación. La diferencia entre una instrucción vaga y una especificada es "
        "la misma que entre un encargo mal hecho a una persona y uno bien hecho, y produce el mismo tipo de "
        "resultados.",

        "El contexto suficiente incluye lo que el sistema no puede saber: quién es el cliente, qué se "
        "acordó antes, qué restricciones existen, qué no se puede prometer. Omitirlo produce resultados "
        "genéricos que después hay que reescribir, y esa reescritura consume el tiempo que la herramienta "
        "prometía ahorrar.",

        "El criterio de aceptación debe ser verificable por quien recibe el resultado: extensión, elementos "
        "obligatorios, prohibiciones explícitas. Sin él, la revisión es una impresión y la calidad varía "
        "según quién revise. Convertir ese criterio en una lista de verificación es lo que hace repetible el "
        "proceso.",

        "Plantillas más específicas producen mejores resultados y limitan la adaptación a casos nuevos; más "
        "genéricas son flexibles y producen salidas que requieren más edición. La biblioteca práctica combina "
        "ambas: plantillas específicas para las tareas frecuentes y una guía general para el resto.",

        "El dato sensible no debe entrar en estas herramientas sin verificar el marco de tratamiento: dónde "
        "se procesa, si se usa para entrenamiento, cuánto se conserva. Incluir información de clientes en un "
        "servicio externo es una transferencia de datos con obligaciones específicas, y esa verificación es "
        "previa al uso, no posterior.",
    ],

    "03": [
        "Usar asistentes para investigar acelera el trabajo y cambia el tipo de error posible: en lugar de no "
        "encontrar información, se obtiene información plausible que puede ser incorrecta. Esa diferencia es "
        "crítica porque el error plausible pasa las revisiones superficiales y se propaga.",

        "La verificación en fuente primaria deja de ser una buena práctica y se convierte en un requisito. "
        "Toda afirmación factual obtenida por esta vía —una cifra, una norma, un dato de mercado— debe "
        "contrastarse con la fuente original antes de usarse. Sin esa regla, el material del equipo acumula "
        "errores que nadie puede rastrear.",

        "La trazabilidad de la evidencia exige registrar de dónde salió cada dato, y ese registro debe "
        "sobrevivir al documento. Un informe que cita una cifra sin origen es indefendible ante la primera "
        "pregunta, y la respuesta «lo obtuve con una herramienta» no es una fuente.",

        "Investigar con asistencia es más rápido y crea la ilusión de haber cubierto el tema. La cobertura "
        "aparente puede ocultar que no se consultaron fuentes clave o que la síntesis omitió posiciones "
        "contrarias. Complementar con búsqueda dirigida en fuentes conocidas es lo que evita ese sesgo de "
        "completitud.",

        "El uso legítimo del material obtenido tiene límites de derechos de autor y de licencia. Reproducir "
        "contenido protegido, aunque haya sido intermediado por una herramienta, sigue siendo reproducción. "
        "La regla del programa es producir texto propio y citar fuentes, no reutilizar párrafos ajenos.",
    ],

    "04": [
        "Generar contenido con asistencia cambia la economía de la producción y no cambia la "
        "responsabilidad. Lo que se publica compromete a la empresa igual que si lo hubiera escrito una "
        "persona, y esa equivalencia es el punto de partida de cualquier política de uso.",

        "El control de afirmaciones se vuelve más importante, no menos: el volumen aumenta y la propensión "
        "del sistema a producir afirmaciones plausibles exige una verificación explícita. Cada dato, cifra o "
        "referencia normativa debe tener un responsable que la comprobó, y ese control no se puede "
        "automatizar con la misma herramienta que generó el texto.",

        "El responsable de publicación debe estar nominado por pieza. Cuando el contenido se produce a mayor "
        "velocidad, la revisión tiende a diluirse entre varias personas y termina sin dueño. Nombrar a quien "
        "responde por cada publicación es un control simple que sostiene el estándar cuando el volumen "
        "crece.",

        "Producir más contenido amplía la presencia y multiplica el riesgo de que un error se propague antes "
        "de detectarse. La decisión sobre el volumen debe considerar la capacidad de revisión disponible, y "
        "no sólo la capacidad de producción, que ahora es prácticamente ilimitada.",

        "El registro de origen —qué se produjo con asistencia y qué no— tiene valor operativo y en algunos "
        "contextos es exigible. Sirve para auditar cuando aparece un error, para evaluar la calidad relativa "
        "y para cumplir obligaciones de transparencia donde existan. Implementarlo desde el inicio es más "
        "fácil que reconstruirlo después.",
    ],

    "05": [
        "La personalización mejora la pertinencia y cruza un umbral a partir del cual produce incomodidad. "
        "Ese umbral no depende de la tecnología sino de la expectativa: cuando el mensaje revela un "
        "conocimiento que la persona no recuerda haber entregado, la reacción es de invasión aunque el dato "
        "sea público.",

        "La expectativa de privacidad es el criterio operativo. Antes de usar un dato para personalizar, la "
        "pregunta es si la persona esperaría que se usara así. Cuando la respuesta es dudosa, la salida "
        "profesional es no usarlo o declarar explícitamente su origen, que suele desactivar la incomodidad.",

        "La finalidad declarada limita el uso: los datos recogidos para una finalidad no pueden usarse para "
        "otra sin nueva base de licitud. Esa restricción es normativa y también práctica, porque el uso "
        "fuera de la finalidad es exactamente lo que produce el efecto inquietante que destruye la "
        "confianza.",

        "Personalizar más aumenta la relevancia y el costo de producción, la complejidad operativa y el "
        "riesgo. Personalizar menos es más simple y menos efectivo. La proporción razonable personaliza "
        "aquello que mejora claramente la experiencia y deja el resto estándar, en lugar de personalizar por "
        "capacidad técnica.",

        "La arquitectura de la decisión —cómo se presentan las opciones— nunca es neutra, y la "
        "personalización la vuelve individual. Esa combinación exige un control ético explícito: si el "
        "destinatario conociera el mecanismo, ¿lo consideraría legítimo? Cuando la respuesta es no, la "
        "técnica está operando contra la persona a la que dice servir.",
    ],

    "06": [
        "Investigar prospectos con asistencia permite preparar más contactos en menos tiempo y multiplica el "
        "riesgo de incluir afirmaciones no verificadas en un mensaje comercial. Un dato incorrecto sobre la "
        "empresa del destinatario destruye la credibilidad del contacto de forma inmediata e irreversible.",

        "La señal verificable debe distinguirse de la inferencia. Que la herramienta indique que una empresa "
        "está expandiéndose no lo convierte en un hecho; conviene rastrear la fuente antes de mencionarlo. La "
        "regla operativa es no afirmar en un mensaje nada que no se pueda citar.",

        "La proporcionalidad de la recolección es un criterio normativo y también de sentido común: recoger "
        "sobre una persona más información de la necesaria para el propósito comercial excede lo legítimo "
        "aunque sea técnicamente accesible. La finalidad debe definir el alcance de la investigación, no la "
        "capacidad de la herramienta.",

        "Investigar más produce mensajes más relevantes y consume tiempo y aumenta la exposición. Con "
        "asistencia, el costo baja y el volumen sube, lo que hace más importante —no menos— definir qué "
        "información se busca y cuál no. Sin ese límite, la recolección crece por defecto.",

        "Los modelos entrenados con datos históricos reproducen los sesgos de la operación previa: si "
        "históricamente se contactó a cierto perfil, el sistema priorizará ese perfil y reforzará la "
        "exclusión de otros. Revisar qué segmentos quedan sistemáticamente fuera es un control necesario y "
        "que casi nunca se implementa.",
    ],

    "07": [
        "Un modelo de calificación entrenado con datos propios puede superar a las reglas manuales y "
        "arrastra un problema que las reglas no tienen: reproduce lo que la empresa hizo, incluidos sus "
        "errores. Si históricamente se descartó un segmento por prejuicio, el modelo aprenderá que ese "
        "segmento no convierte porque nunca se le vendió.",

        "El sesgo histórico se detecta comparando la distribución de puntajes por segmento con la "
        "distribución de resultados reales en los casos donde sí se intentó. Cuando un segmento tiene puntaje "
        "sistemáticamente bajo y pocos intentos, la conclusión no es que no convierte: es que no hay "
        "evidencia.",

        "La explicabilidad no es una preferencia estética: si el equipo comercial no entiende por qué una "
        "cuenta tiene puntaje alto, no sabrá cómo aprovechar esa información y terminará ignorándola. Un "
        "modelo que entrega los tres factores que más pesaron en cada caso se usa; uno que entrega sólo un "
        "número, no.",

        "Un modelo más preciso puede ser menos explicable y menos adoptado, con lo que su precisión superior "
        "no se traduce en resultado. En la práctica comercial, la adopción importa más que la exactitud "
        "marginal, y esa consideración debe entrar en la elección del método.",

        "La deriva del modelo —la pérdida de validez a medida que cambian las condiciones— es inevitable y "
        "debe monitorearse. Un modelo que funcionó bien puede dejar de discriminar sin aviso. Definir una "
        "revisión periódica y un umbral de desempeño que obligue a reentrenar es parte del despliegue, no "
        "una tarea posterior.",
    ],

    "08": [
        "Un asistente de ventas cambia dónde ocurre el error: en lugar de que el vendedor olvide algo, el "
        "sistema puede sugerir algo incorrecto con confianza. Esa diferencia exige un control distinto: la "
        "revisión obligatoria antes de que cualquier salida llegue al cliente.",

        "La asistencia en tarea funciona mejor que la sustitución: resumir una llamada, preparar un borrador, "
        "recordar compromisos previos son usos donde el sistema aporta y el humano decide. Los usos donde el "
        "sistema decide —qué precio ofrecer, qué prometer— requieren controles mucho más estrictos y "
        "raramente se justifican.",

        "El compromiso derivado es el riesgo específico: si el asistente redacta una propuesta con una "
        "condición que la operación no puede cumplir y alguien la envía, la empresa queda obligada. La "
        "revisión obligatoria debe cubrir específicamente los elementos que generan obligación: plazos, "
        "alcances, precios, garantías.",

        "Usar más asistencia aumenta la productividad y puede degradar la habilidad del equipo, que deja de "
        "practicar lo que el sistema hace. En funciones donde el criterio se construye con práctica —el "
        "descubrimiento, la negociación— esa degradación tiene costo de mediano plazo que conviene "
        "considerar.",

        "El registro de la asistencia —qué produjo el sistema, qué modificó la persona— tiene valor para "
        "auditar y para mejorar. Cuando aparece un error en una propuesta, poder distinguir si venía del "
        "borrador o se introdujo después determina qué corregir. Ese registro debe existir desde el "
        "despliegue.",
    ],

    "09": [
        "Un agente que ejecuta acciones comerciales de forma autónoma —enviar comunicaciones, actualizar "
        "registros, agendar— introduce una categoría de riesgo distinta: los errores no se quedan en una "
        "sugerencia, se materializan. Por eso su autoridad debe estar acotada explícitamente y no definirse "
        "por lo que técnicamente puede hacer.",

        "La autoridad del agente debe declararse por acción: qué puede hacer sin supervisión, qué requiere "
        "confirmación y qué está prohibido. Esa lista debe existir antes del despliegue y revisarse cuando "
        "se amplían las capacidades. Un agente cuya autoridad nunca se definió la tiene ilimitada por "
        "omisión.",

        "El registro de acciones es la condición mínima de auditabilidad: qué hizo el agente, cuándo, con qué "
        "información y con qué resultado. Sin ese registro, un incidente no puede reconstruirse y la "
        "responsabilidad no puede establecerse, lo que expone tanto a la empresa como a las personas "
        "involucradas.",

        "Mayor autonomía produce más eficiencia y reduce los puntos donde un humano puede detectar un error. "
        "El equilibrio no es una preferencia sino una función del costo del error: acciones reversibles y de "
        "bajo impacto admiten autonomía; las irreversibles o con efecto sobre el cliente exigen "
        "confirmación.",

        "El mecanismo de detención debe existir, ser conocido y estar probado. La pregunta «quién puede "
        "apagar esto y en cuánto tiempo» debe tener respuesta antes de activar el sistema, y la respuesta "
        "debe verificarse con una prueba real, no suponerse a partir de la documentación.",
    ],

    "10": [
        "El análisis de conversaciones comerciales permite identificar patrones que ningún acompañamiento "
        "manual detectaría: qué preguntas se asocian con avance, cuánto habla cada parte, qué objeciones "
        "aparecen. Su valor es agregado y de mejora de proceso; usarlo para evaluar individualmente cambia su "
        "naturaleza y su aceptación.",

        "El consentimiento de grabación es previo y no negociable: todas las partes deben conocer que la "
        "conversación se registra y para qué se usará. En Chile hay obligaciones específicas al respecto que "
        "deben verificarse en su fuente vigente. Un análisis construido sobre grabaciones sin consentimiento "
        "es inutilizable además de riesgoso.",

        "El patrón asociado al resultado es una correlación y no una receta. Que las llamadas exitosas tengan "
        "cierta proporción de habla no significa que forzar esa proporción produzca éxito. Confundir "
        "asociación con causa lleva a entrenar al equipo en conductas superficiales que imitan el síntoma y "
        "no la causa.",

        "Analizar más conversaciones entrega mejores patrones y aumenta la sensación de vigilancia, que "
        "puede alterar la conducta que se pretende medir. Declarar explícitamente el uso agregado y "
        "respetarlo es lo que permite que el equipo colabore en lugar de adaptarse a la medición.",

        "El uso para desarrollo y el uso para evaluación deben separarse y declararse. Un sistema presentado "
        "como herramienta de mejora que después alimenta la evaluación de desempeño destruye la confianza de "
        "forma permanente. Esa decisión debe tomarse y comunicarse al inicio, no cuando resulte conveniente.",
    ],

    "11": [
        "Aplicar modelos predictivos al éxito de cliente permite anticipar riesgo de baja y priorizar la "
        "atención. Su utilidad depende de dos condiciones: que la predicción llegue con tiempo suficiente "
        "para intervenir y que exista una intervención disponible. Un modelo que predice bien lo inevitable "
        "no aporta nada.",

        "La priorización de cartera es el uso más valioso: con capacidad limitada, atender primero a quien "
        "más lo necesita y donde la intervención puede cambiar el resultado. Eso exige combinar la "
        "probabilidad de baja con el valor de la cuenta y con la probabilidad de que la intervención "
        "funcione, que es el factor que casi nunca se modela.",

        "La automatización de la respuesta tiene un límite claro: una cuenta en riesgo que recibe un correo "
        "automático percibe exactamente lo contrario de lo que la intervención pretendía. La automatización "
        "sirve para detectar y para preparar, no para responder en situaciones donde la relación está "
        "deteriorada.",

        "Confiar más en el modelo libera tiempo de análisis y arriesga desatender cuentas que el modelo "
        "clasifica como seguras. Esa profecía autocumplida es un riesgo real: si nadie visita a las cuentas "
        "de bajo riesgo, algunas se volverán de alto riesgo sin que el modelo lo detecte hasta tarde.",

        "El momento de escalamiento a una persona debe estar definido: qué nivel de riesgo, qué valor de "
        "cuenta o qué tipo de señal obliga a que intervenga alguien con autoridad. Sin esa regla, las "
        "situaciones graves se gestionan con el mismo procedimiento automatizado que las rutinarias, y el "
        "resultado es previsible.",
    ],

    "12": [
        "Evaluar un sistema de inteligencia artificial exige un conjunto de casos que represente el uso real "
        "y no el uso ideal. Un modelo que funciona bien con ejemplos limpios puede fallar con la información "
        "desordenada que existe en la operación. Construir ese conjunto de evaluación es trabajo previo al "
        "despliegue y no una verificación posterior.",

        "El guardarraíl es una restricción que el sistema no debe cruzar aunque mejore su métrica principal: "
        "no prometer plazos, no mencionar precios, no afirmar sobre normativa, no procesar ciertos datos. "
        "Definir esos límites y verificarlos con casos de prueba específicos es más efectivo que confiar en "
        "instrucciones generales.",

        "El monitoreo posterior es indispensable porque el desempeño se degrada: cambian los datos de "
        "entrada, cambia el contexto, cambia el modelo subyacente si es de un tercero. Un sistema evaluado "
        "una vez al desplegarse y nunca más es un sistema cuya calidad actual nadie conoce.",

        "Evaluaciones más exhaustivas detectan más problemas y retrasan el despliegue. El equilibrio debe "
        "hacerse según la consecuencia del error: un asistente que redacta borradores internos admite una "
        "evaluación ligera; uno que se comunica con clientes, no. Esa gradación debe estar en la política y "
        "no decidirse caso a caso.",

        "El marco de gestión de riesgos publicado por el NIST propone organizar el trabajo en cuatro "
        "funciones —mapear, medir, gestionar y gobernar— y esa estructura es útil precisamente porque separa "
        "la evaluación técnica de la responsabilidad organizativa. Adoptarla exige verificar su texto vigente "
        "y adaptarla al contexto, no aplicarla como plantilla.",
    ],

    "13": [
        "El uso de estas herramientas en operaciones comerciales toca dos marcos normativos distintos: "
        "protección de datos personales y propiedad intelectual. Confundirlos lleva a resolver uno y dejar "
        "el otro abierto. Ambos deben revisarse antes de incorporar una herramienta al flujo de trabajo.",

        "La finalidad del tratamiento debe declararse y limitarse. Incorporar datos de clientes a un servicio "
        "externo es una transferencia con obligaciones específicas: dónde se procesan, quién más accede, "
        "cuánto se conservan, si se usan para entrenar. Esas preguntas deben responderse con el proveedor y "
        "documentarse.",

        "La decisión automatizada que produce efectos jurídicos o significativos sobre una persona tiene "
        "regulación propia, incluido el derecho a intervención humana. Un sistema que rechaza solicitudes, "
        "asigna condiciones o excluye de una oferta puede caer en esa categoría. Verificarlo antes de "
        "desplegar es obligatorio.",

        "Restringir el uso protege y reduce la productividad; permitirlo ampliamente acelera y expone. La "
        "política razonable define categorías de datos —públicos, internos, de cliente, sensibles— y qué "
        "puede usarse con qué herramienta, en lugar de una prohibición general que el equipo incumplirá en "
        "silencio.",

        "La titularidad del contenido generado y el riesgo de infringir derechos de terceros dependen de la "
        "jurisdicción y de los términos del proveedor, y ambos cambian. Este material entrega la estructura "
        "de las preguntas; las respuestas requieren revisión legal actualizada y no pueden darse por "
        "sabidas.",
    ],

    "14": [
        "Un modelo operativo humano-máquina define qué hace cada uno, dónde está la frontera y cómo se "
        "escala cuando algo sale mal. Sin esa definición, la frontera se establece por costumbre y termina "
        "donde la herramienta permite llegar, que no es un criterio de gestión.",

        "La rendición de cuentas debe ser nominal: por cada proceso asistido, una persona responde por el "
        "resultado. Esa asignación no puede diluirse en el área ni en el sistema. Cuando ocurre un incidente, "
        "la existencia de un responsable identificado es la diferencia entre corregir y buscar culpables.",

        "El registro de incidentes es la memoria del sistema: qué falló, con qué consecuencia, qué se hizo. "
        "Su valor aparece con el tiempo, cuando permite ver patrones y distinguir un error puntual de una "
        "falla estructural. Empezarlo desde el primer despliegue cuesta poco; reconstruirlo después es "
        "imposible.",

        "Un modelo con más control humano reduce el riesgo y el beneficio de productividad; uno con más "
        "autonomía multiplica ambos. La gradación debe corresponder a la consecuencia del error y a la "
        "reversibilidad, y debe revisarse a medida que se acumula evidencia sobre el desempeño real.",

        "La revisión periódica del modelo operativo es necesaria porque la tecnología, la normativa y las "
        "capacidades cambian con rapidez. Un modelo definido hace un año puede estar restringiendo usos ya "
        "seguros o permitiendo otros que dejaron de serlo. Fijar una frecuencia de revisión y un responsable "
        "es parte del diseño.",
    ],
}
