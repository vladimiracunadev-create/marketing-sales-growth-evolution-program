# Auditoría previa — Commercial Evidence Pack

Auditoría de la conexión entre mercado, conocimiento del cliente, economía comercial y forecast. El alcance
es fortalecer el programa existente sin añadir clases ni convertirlo en un curso general de creación de
empresas.

## Fuente de verdad y superficies revisadas

La fuente de verdad pedagógica real es `curriculum/spec/`. Las clases publicadas, los laboratorios, las
evaluaciones, los casos, los proyectos, el Capstone, las rutas y buena parte de la documentación son salidas
de los generadores de `tools/`. Por eso, cualquier cambio sustantivo debe entrar por la especificación o por
el generador correspondiente y después regenerarse.

Se revisaron antes de editar contenido: `README.md`; las 336 clases y sus 24 partes mediante la
especificación completa y el índice generado; `curriculum/spec/`; todos los generadores; 48 laboratorios;
24 evaluaciones; 17 rutas por rol; glosario; fórmulas y métricas; catálogo bibliográfico y registro de
localizadores; validadores; pruebas; y los cinco workflows de CI.

Inventario previo verificado: 336 clases, 24 partes, 48 laboratorios, 24 evaluaciones, 24 casos, 12 proyectos,
17 rutas, 20 plantillas y 5 workflows.

## Matriz previa obligatoria

| Concepto | Cobertura existente | Ubicación principal | Brecha observada | Acción mínima decidida |
|---|---|---|---|---|
| Mercado y categoría | Alta: definición de categoría, demanda, competencia y dimensionamiento | 01.03, 03.01–03.14, 22.02 | La síntesis final no exige una vista ejecutiva continua de inteligencia comercial | Ampliar el informe existente de 03.14; no crear otra clase ni otro informe paralelo |
| Segmentos | Alta: B2C/B2B, conductual, STP, atractivo y accesibilidad | 02.13, parte 04 | La conexión entre segmento y las decisiones posteriores queda distribuida | Hacer obligatoria la cadena segmento → ICP → evidencia → propuesta → mensaje → oferta → canal → venta en 02.14 |
| ICP | Alta y operacional, con inclusión, exclusión, permanencia y margen | 02.05, plantilla `customer/icp-scorecard.md` | No siempre queda explícito qué evidencia originó cada criterio | Exigir origen controlado y estado de validación en el expediente de cliente |
| Persona | Alta y explícitamente basada en evidencia | 02.04 | El origen se resume como fuente, pero no distingue siempre entrevista, observación, comportamiento, encuesta o hipótesis | Normalizar esos cinco orígenes en la síntesis y en el artefacto integrador |
| JTBD | Alta, con fuerzas, disparadores y límite frente a segmentación | 02.03 | No se fuerza su transferencia hasta mensaje, oferta, canal y venta | Integrarlo en la cadena decisional de 02.14 y en el Commercial Evidence Pack |
| Voice of Customer | Alta en oferta y ciclo continuo de cliente | 05.12, 18.13 | Queda separado del expediente inicial y de la trazabilidad del mensaje | Conectar citas/patrones con propuesta, mensaje y oferta dentro del paquete integrador |
| Entrevistas | Alta: diseño, conducta pasada, saturación y sesgos | 03.03, 03.06, plantilla de entrevista | Falta un vocabulario común de procedencia a lo largo de todos los artefactos | Usar la taxonomía de origen común y conservar fuente, fecha y nivel de validación |
| Mapa de empatía | No aparece como instrumento formal | Sin artefacto equivalente | Puede ayudar a sintetizar, pero corre riesgo de sustituir investigación con imaginación | Incorporarlo como vista opcional y derivada; prohibir que cree afirmaciones nuevas |
| Competidores y sustitutos | Alta: competencia directa/funcional, cinco fuerzas y movimientos probables | 01.03, 03.10 | La comparación no exige todas las dimensiones solicitadas ni prueba por celda | Ampliar 03.09–03.10 con matriz reproducible y evidencia observable |
| Benchmarks | Media-alta: brechas por atributo y costo de paridad | 03.09 | Falta protocolo uniforme para propuesta, segmento, posicionamiento, precio, packaging, canal, experiencia, fortalezas y debilidades | Incorporar esas dimensiones, fuente, fecha, comparabilidad y `no observable` |
| TAM, SAM y SOM | Alta, bottom-up, escenarios y capacidad | 03.08 | Puede confundirse SOM con cuota observada o cifra cierta | Exigir separación entre dato, estimación, hipótesis e inferencia; cuota sólo con fuente confiable |
| Tendencias y señales de demanda | Media-alta: social listening, señales débiles y entrada a mercado | 03.11, 22.02 | No están consolidadas con canales y precios observables en el informe ejecutivo | Integrarlas en 03.14 con vigencia y umbral de acción |
| Precios observables y WTP | Alta: referencias, pricing competitivo, valor, WTP y pruebas reales | partes 03, 05 y 07 | La evidencia de precio no llega de forma uniforme al informe de mercado y al forecast | Enlazar precio observado, WTP y supuesto de ticket en el paquete, sin duplicar pricing |
| CAC | Alta y con alcance completo por canal/segmento | 14.10, 20.03 | Está bien definido pero fragmentado respecto de forecast y capacidad | Referenciarlo como supuesto económico obligatorio del paquete y del forecast |
| LTV y unit economics | Alta: cohortes, margen, payback y sensibilidad | 07.12, 20.04–20.06, 24.04 | No existe una sola superficie que muestre cómo condicionan adquisición y proyección comercial | Integrarlos como restricción, no desarrollar un programa financiero paralelo |
| Pipeline y sales cycle | Alta: etapas, criterios, higiene, cobertura, velocidad y revisión | parte 16 | La cobertura se expresa como razón, pero no siempre muestra capacidad y confianza juntas | Integrar cobertura, duración, capacidad y precisión en el forecast comercial |
| Funnel B2B | Alta hasta renovación, con definiciones compartidas | 17.10 | No exige explícitamente visitas/leads → MQL → SQL → oportunidades → cierres → clientes → ingreso | Hacer visible la cadena completa, permitiendo omitir MQL/SQL cuando no aplican |
| Modelos no B2B | Parcial: e-commerce, PLG, canales y cohortes existen en otras partes | partes 15, 18, 19 y 22 | El forecast unificado no prescribe alternativas para e-commerce, suscripción, PLG o canal indirecto | Añadir modelos alternativos con la misma lógica de unidades, conversiones, valor y retención |
| Conversión, ticket y frecuencia | Alta pero distribuida | partes 01, 15, 16, 17 y 20 | No se ensamblan obligatoriamente en una proyección de clientes e ingreso | Exigir diccionario de etapas, tasas, ticket/frecuencia y ecuación de ingreso por modelo |
| Retención y churn | Alta, por cuentas, ingreso y cohortes | parte 18, 20.04, 17.11 | El forecast nuevo y el de base instalada pueden verse por separado | Consolidar nuevo, renovación, expansión, contracción y churn sin ocultar incertidumbre |
| Sales capacity | Alta y explícita | 16.09, 22.04, 22.14 | No siempre limita matemáticamente el forecast de demanda | Incorporar capacidad como techo y declarar ramp-up y carga sostenible |
| Forecast comercial | Alta en pipeline, forecast unificado, analítica y dirección | 16.07, 17.11, 20.11, 23.08 | Falta una proyección operable de extremo a extremo y una etiqueta explícita de confianza | Fortalecer las clases existentes; no crear una nueva clase de forecast |
| Forecast confidence | Parcial: precisión histórica, sesgo, rangos y categorías | 16.07, 20.11, 23.08 | La confianza no está definida como juicio calibrado por evidencia, cobertura y estabilidad | Definir confianza como evaluación auditable, nunca como certeza |
| RevOps | Alta: datos, SLA, lifecycle, funnel, forecast y gobierno | partes 01 y 17, ruta RevOps | El artefacto final prioriza la cifra única, pero no reúne mercado, cliente y economía | Conectar el operating model con el Commercial Evidence Pack |
| Commercial Evidence Pack | No existe con ese nombre; hay equivalentes parciales | artefactos 02, 03, 07, 16, 17, 20 y Capstone 24 | Evidencia y supuestos están fragmentados; no hay índice único de incertidumbres | Crear una plantilla integradora y ampliar 24.11/Capstone, sin convertirla en modelo financiero |

## Diagnóstico de no duplicación

No se justifican clases nuevas: las materias ya existen y tienen clases, prácticas, métricas y bibliografía.
Los cambios deben concentrarse en las síntesis 02.14 y 03.14, los métodos competitivos 03.09–03.10, el
forecast/RevOps existente en 16.07 y 17.10–17.14, y la integración del Capstone en 24.11. El entregable
ejecutivo de inteligencia de mercado ya tiene equivalente en el informe de oportunidad de mercado y en el
resumen ejecutivo de los laboratorios; se ampliará ese artefacto en vez de crear otro.

## Línea base ejecutada

- `python tools/build_curriculum.py --check`: 24/24 partes con especificación.
- `python tools/validate_repository.py`: 10.050 comprobaciones superadas.
- `python tools/validate_depth.py`: 336 clases, 48 laboratorios, 24 evaluaciones y 24 casos sobre mínimos.
- `python tools/audit_fuentes.py`: 336/336 clases con anclaje; 1.345 citas y 97 obras.
- `python scripts/verify_sources.py`: 97 entradas, 95 verificadas y 2 pendientes declaradas.
- `python tools/check_links.py`: 7.775 enlaces internos válidos.
- `.venv\\Scripts\\python.exe -m pytest -q -p no:cacheprovider --basetemp .pytest-run-20261001-audit`:
  90 pruebas aprobadas. El intérprete global no tenía `pytest`; se usó el entorno del repositorio.

## Matriz después

| Conexión | Antes | Después | Evidencia de integración |
|---|---|---|---|
| Inteligencia de mercado | Mercado, TAM/SAM/SOM, social listening y competencia existían, pero la síntesis ejecutiva no exigía un sistema común | 03.09–03.10 aplican comparación reproducible y 03.14 produce un informe ejecutivo de 1–2 páginas con anexo auditable | Mercado, categoría, segmentos, competidores, sustitutos, tendencias, benchmarks, cuota sólo con fuente confiable, señales, canales y precios observables; cada afirmación se marca como dato, estimación, hipótesis o inferencia |
| Evidencia de cliente | ICP, persona, JTBD, entrevistas y VoC tenían buena cobertura, pero su procedencia y transferencia estaban dispersas | 02.14 y el paquete hacen trazable segmento → ICP → entrevistas → JTBD → pains/gains → propuesta → mensaje → oferta → canal → venta | Cada elemento declara entrevista, observación, dato de comportamiento, encuesta o hipótesis no validada; el mapa de empatía queda como vista opcional derivada, nunca como investigación |
| Competencia y benchmarks | Había benchmarking por atributos y análisis de competencia, sin dimensiones ni prueba uniformes | 03.09–03.10 y sus prácticas exigen un método comparable, fecha, fuente y `no observable` | Propuesta, segmento, posicionamiento, precio, packaging, canal, experiencia, fortalezas y debilidades observables; incluye competidor directo, sustituto y no hacer nada |
| Economía comercial | Pricing, WTP, CAC, LTV y unit economics existían en sus partes especializadas | El paquete los referencia como restricciones de adquisición y forecast, sin duplicar la formación financiera | Precio observado, WTP, ticket, frecuencia, CAC, LTV, margen y payback quedan conectados a supuestos y decisiones |
| Forecast comercial | Pipeline, sales cycle, cobertura, capacidad y forecast existían, pero no había una cadena extrema a extremo ni confianza calibrada explícita | 16.07 define confianza auditable; 17.10–17.14 conectan demanda, etapas, clientes, ingreso, base instalada y operación RevOps | Cadena visitas/leads → MQL cuando aplica → SQL → oportunidades → cierres → clientes → ingreso; alternativas e-commerce, suscripción, PLG y canal indirecto; rangos, escenarios, capacidad, cobertura y calidad de datos |
| Artefacto integrador | Los entregables estaban repartidos entre las partes 02, 03, 07, 16, 17, 20 y 24 | `templates/strategy/commercial-evidence-pack.md` funciona como índice integrador y 24.11/Capstone lo exige | Diez bloques: mercado, cliente, competencia, propuesta, precio, adquisición, conversiones, forecast, supuestos, evidencias e incertidumbres; prepara una proyección financiera posterior sin sustituirla |

## Brechas cerradas y límites conservados

- Se cerró la falta de trazabilidad entre observación y decisión comercial con dos taxonomías explícitas:
  estado epistemológico y origen de evidencia del cliente.
- Se cerró la falta de un benchmark repetible con dimensiones, fuente, fecha, comparabilidad y ausencia de
  evidencia declarada.
- Se cerró el salto entre demanda e ingreso con un modelo B2B completo y variantes para negocios que no usan
  ese funnel.
- Se cerró la fragmentación de artefactos con una plantilla integradora; no se trasladó a este repositorio el
  modelado de estados financieros, caja, balance ni valoración.
- Permanecen como incertidumbres legítimas los valores que cada alumno deberá investigar: cuota, WTP,
  conversiones, churn, capacidad y precisión. El programa enseña a declararlos y actualizarlos, no los inventa.
- La bibliografía conserva 2 localizadores pendientes ya declarados de la línea base; no se añadieron fuentes
  ni afirmaciones que requirieran una obra nueva.

## Modificaciones realizadas

- Fuente de verdad: ampliaciones en `curriculum/spec/` para las partes 02, 03, 16, 17 y 24, sus desarrollos,
  artefactos de parte y rutas por rol.
- Práctica generada: laboratorios, evaluaciones, casos, proyectos y Capstone reforzados desde los generadores.
- Artefacto: nueva plantilla `templates/strategy/commercial-evidence-pack.md` y enlace desde el Capstone.
- Control: prueba estructural del paquete, documentación de auditoría y corrección del contador único de páginas
  del portal.
- Salidas: currículo, rutas, documentación, bibliografía, estado y portal regenerados desde sus fuentes.

## Validación posterior

- Estructura preservada: 336 clases, 24 partes, 48 laboratorios, 24 evaluaciones, 24 casos, 12 proyectos,
  17 rutas, 21 plantillas y 5 workflows.
- `python tools/build_curriculum.py --check`: 24/24 partes con especificación.
- `python tools/validate_repository.py`: 10.050 comprobaciones superadas.
- `python tools/validate_depth.py`: 336 clases, 48 laboratorios, 24 evaluaciones y 24 casos sobre mínimos;
  1.804.905 palabras curriculares.
- `python tools/audit_fuentes.py`: 336/336 clases con anclaje; 1.345 citas y 97 obras.
- `python scripts/verify_sources.py`: 97 entradas, 95 verificadas y 2 pendientes declaradas.
- `python tools/check_links.py`: 7.782 enlaces internos válidos.
- `python tools/validate_site.py`: 638 páginas HTML y 16 comprobaciones superadas.
- `.venv\\Scripts\\python.exe -m pytest`: 91 pruebas aprobadas.
- `python -m py_compile` sobre especificaciones, generadores y prueba modificados: sin errores.
- `git diff --check`: sin errores de espacios.
- Segunda regeneración completa: 1.280 archivos derivados conservaron exactamente el mismo SHA-256.

## Evidencia de no duplicación

No se creó ninguna clase, parte, ruta, laboratorio, evaluación, caso ni proyecto adicional. El conteo antes y
después permanece en 336 clases y 24 partes, y también se conservan los demás conteos pedagógicos. El informe
03.14, el expediente 02.14, el forecast 16.07/17.10–17.14 y el artefacto 24.11 fueron ampliados en su ubicación
original. La única pieza nueva de contenido es una plantilla transversal que ordena entregables existentes;
no constituye una materia ni replica `modern-business-creation-program`.
