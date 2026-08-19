---
title: "Parte 17 — Marketing automation y revenue operations"
type: part-index
language: es
part: 17
updated: 2026-08-19
---

# Parte 17 — Marketing automation y revenue operations

Esta parte trabaja el nivel **Operación de ingresos** del programa y su propósito es que llegues a poder **integrar marketing, ventas y servicio en un solo modelo de datos y de proceso**. Llegas desde la parte 16, *CRM, pipeline y sales operations*, y lo que allí quedó resuelto se da por sabido aquí. Lo que produzcas aquí es material de entrada para la parte 18, *Customer experience, success y fidelización*.

Son 14 clases, alrededor de 35 horas de estudio dirigido, y todas empujan hacia la misma pregunta:

> **¿Qué automatizo porque mejora el sistema y qué estaría solo escalando un desorden?**

Esa pregunta no es retórica: al final de la parte tienes que poder responderla con un artefacto en la mano —operating model de RevOps con lifecycle, scoring, SLA, integraciones y observabilidad— y no con una opinión.

## Sobre qué caso vas a trabajar

Marketing entrega 300 leads mensuales y ventas trabaja 60. Cada área tiene su propio informe y ambos son correctos según su definición.

Todo el programa ocurre en la misma empresa, **Ruta Andina SpA**: Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público. Trabajar siempre sobre el mismo caso permite comparar decisiones tomadas en partes distintas y ver cuáles se contradicen entre sí.

## Qué vas a saber hacer

Las competencias que se desarrollan aquí son **automatización con propósito**, **modelo de datos de ingresos** y **gobernanza operativa**. Con ellas la parte habilita para el trabajo de Marketing ops, RevOps manager y Sales ops, que es donde estas decisiones se toman de verdad.

## Cómo avanza la parte, clase a clase

Las clases van en orden y cada una supone la anterior. Esta es la secuencia y los conceptos que introduce cada sesión:

| # | Clase | Conceptos que introduce |
|---|---|---|
| 01 | [Automatización con propósito](class-01-automatizacion-con-proposito.md) | proceso estandarizado, modo de falla, detección de falla |
| 02 | [Etapas de ciclo de vida](class-02-lifecycle-stages.md) | etapa de ciclo de vida, criterio de transición, flujo entre etapas |
| 03 | [Lead scoring](class-03-lead-scoring.md) | puntaje de ajuste, puntaje de comportamiento, validación del modelo |
| 04 | [Enrutamiento de leads](class-04-lead-routing.md) | regla de asignación, tiempo de asignación, cobertura de asignación |
| 05 | [Nurturing](class-05-nurturing.md) | secuencia de maduración, pertinencia por etapa, avance de etapa |
| 06 | [Workflows](class-06-workflows.md) | condición de entrada, condición de salida, prueba en ambiente controlado |
| 07 | [Acuerdo de servicio entre marketing y ventas](class-07-sla-marketing-ventas.md) | definición compartida de lead calificado, compromiso de volumen, compromiso de atención |
| 08 | [Modelo de datos de RevOps](class-08-modelo-de-datos-revops.md) | entidad, fuente autoritativa, estado válido |
| 09 | [Integraciones](class-09-integraciones.md) | dirección de sincronización, latencia, manejo de errores |
| 10 | [Embudo de ingresos](class-10-revenue-funnel.md) | embudo unificado, definición compartida por etapa, pérdida por tramo |
| 11 | [Forecast unificado](class-11-forecast-unificado.md) | ingreso nuevo, renovación, expansión y contracción |
| 12 | [Calidad y observabilidad](class-12-calidad-y-observabilidad.md) | indicador de salud del sistema, alerta accionable, detección por reclamo |
| 13 | [Gobernanza de automatizaciones](class-13-gobernanza-de-automatizaciones.md) | autoridad de cambio, registro de tratamiento, revisión periódica |
| 14 | [Operating model de RevOps](class-14-operating-model-revops.md) | modelo operativo de ingresos, cifra única, responsabilidad por proceso |

## Dónde se practica y cómo se evalúa

Leer la parte no la acredita. Los [laboratorios](../../labs/part-17/) te hacen ejecutar el método sobre el caso; la [evaluación de la parte](../../assessments/part-17-assessment.md) comprueba que puedes sostener las decisiones sin el material delante; el [caso extendido](../../cases/) exige integrar lo aprendido en una recomendación completa, y en [`templates/`](../../templates/) están los formatos que se usan para producir el artefacto. El resultado que va a tu portafolio es **operating model de RevOps con lifecycle, scoring, SLA, integraciones y observabilidad**.

## Qué puede salir mal

Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño. Antes de llevar cualquier recomendación de esta parte a una operación real, revisa el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) y las [reglas sobre datos personales](../../docs/DATOS-PERSONALES-Y-ETICA.md): la norma vigente manda sobre el material pedagógico.

## Bibliografía de la parte

Estas son las obras sobre las que se apoya la parte, con lo que aporta cada una y en cuántas de sus 14 clases aparece. Está comprobado que cada obra existe y cuál es la edición —el título enlaza a su localizador—; que la idea atribuida esté en el capítulo que indica cada clase es la lectura del programa y está para que la contrastes. La columna «Acceso» dice de antemano qué puedes leer sin pagar.

| Obra | Qué aporta | Clases | Localizador | Acceso |
|---|---|---:|---|---|
| Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010) | principios de aprendizaje: conocimiento previo, práctica y retroalimentación | 14 | ISBN 9780470484104 | comprar o biblioteca |
| Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014) | recuperación espaciada, intercalado y dificultad deseable | 14 | ISBN 9780674419377 | comprar o biblioteca |
| Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016) | práctica deliberada con criterios explícitos y retroalimentación inmediata | 14 | ISBN 9781473513143 | comprar o biblioteca |
| Stephen G. Diorio y Chris K. Hummel — [*Revenue Operations*](https://openlibrary.org/isbn/9781119871132) (2022) | integración de datos, procesos y equipos que producen ingreso como un solo sistema | 14 | ISBN 9781119871132 | comprar o biblioteca |
| William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada) | análisis de casos: problema, decisión, evidencia y recomendación | 14 | ISBN 9781633696150 | comprar o biblioteca |
| Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.) | diseño inverso desde el desempeño observable | 14 | ISBN 9781416600350 | comprar o biblioteca |
| Andrew S. Grove — [*High Output Management*](https://openlibrary.org/isbn/9780394532349) (1983) | output gerencial, indicadores adelantados y reuniones como herramienta de producción | 7 | ISBN 9780394532349 | comprar o biblioteca |
| Mark Roberge — [*The Sales Acceleration Formula*](https://openlibrary.org/isbn/9781119047018) (2015) | contratación, formación, gestión y demanda comercial gobernadas por datos | 7 | ISBN 9781119047018 | comprar o biblioteca |
| Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) | pensamiento analítico: formulación del problema, evaluación y valor esperado | 6 | ISBN 9781449374280 | comprar o biblioteca |
| NIST — [*AI Risk Management Framework 1.0*](https://doi.org/10.6028/NIST.AI.100-1) (2023) | gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar | 5 | DOI 10.6028/NIST.AI.100-1 | gratis |
| Alistair Croll y Benjamin Yoskovitz — [*Lean Analytics*](https://openlibrary.org/isbn/9781449335670) (2013) | una métrica que importa por etapa y por modelo de negocio | 3 | ISBN 9781449335670 | comprar o biblioteca |
| Robert S. Kaplan y David P. Norton — [*The Balanced Scorecard*](https://openlibrary.org/isbn/9780875846514) (1996) | traducción de la estrategia en indicadores causalmente conectados | 3 | ISBN 9780875846514 | comprar o biblioteca |
| Nick Mehta, Dan Steinman y Lincoln Murphy — [*Customer Success*](https://openlibrary.org/isbn/9781119168294) (2016) | disciplina operativa de éxito de cliente: salud, renovación y expansión | 2 | ISBN 9781119168294 | comprar o biblioteca |
| Cathy O'Neil — [*Weapons of Math Destruction*](https://openlibrary.org/isbn/9780141985428) (2016) | daños de los modelos opacos a escala y necesidad de auditoría | 2 | ISBN 9780141985428 | comprar o biblioteca |
| Dave Chaffey y Fiona Ellis-Chadwick — [*Digital Marketing*](https://openlibrary.org/isbn/9781292400990) (2022, 8.ª ed.) | planificación digital integrada: canales, medición y gobierno | 1 | ISBN 9781292400990 | comprar o biblioteca |
| Ann Handley — [*Everybody Writes*](https://openlibrary.org/isbn/9781119854319) (2022, 2.ª ed.) | estándar editorial: claridad, utilidad y empatía en la escritura comercial | 1 | ISBN 9781119854319 | comprar o biblioteca |
| ISO — *ISO 31000: Gestión del riesgo* (2018) | vocabulario y proceso de gestión de riesgo aplicable a decisiones comerciales | 1 | fuente primaria | de pago |
| Aaron Ross y Marylou Tyler — [*Predictable Revenue*](https://openlibrary.org/isbn/9780984380213) (2011) | especialización de roles comerciales y generación de pipeline predecible | 1 | ISBN 9780984380213 | comprar o biblioteca |
| Patrick Lencioni — [*The Five Dysfunctions of a Team*](https://openlibrary.org/isbn/9780787960759) (2002) | confianza, conflicto productivo, compromiso, accountability y resultados | 1 | ISBN 9780787960759 | comprar o biblioteca |
| Seth Godin — [*This Is Marketing*](https://openlibrary.org/isbn/9780525540830) (2018) | marketing como servicio a un público mínimo viable y construcción de confianza | 1 | ISBN 9780525540830 | comprar o biblioteca |
| Donald J. Wheeler — [*Understanding Variation*](https://openlibrary.org/isbn/9780945320531) (2000) | distinguir variación común de variación especial antes de reaccionar a un KPI | 1 | ISBN 9780945320531 | comprar o biblioteca |

De todas ellas, las que ordenan el criterio de esta parte son Stephen G. Diorio y Chris K. Hummel (*Revenue Operations*), Mark Roberge (*The Sales Acceleration Formula*), Andrew S. Grove (*High Output Management*), Robert S. Kaplan y David P. Norton (*The Balanced Scorecard*), Foster Provost y Tom Fawcett (*Data Science for Business*) y NIST (*AI Risk Management Framework 1.0*). Si sólo puedes leer una, empieza por Stephen G. Diorio y Chris K. Hummel — *Revenue Operations*.

La bibliografía completa del programa, con el uso de cada obra clase a clase, está en [`docs/BIBLIOGRAFIA.md`](../../docs/BIBLIOGRAFIA.md); el registro con los localizadores comprobables, en [`sources/bibliography.json`](../../sources/bibliography.json).

---

[⬅ Índice del currículo](../README.md) · [Programa](../../README.md)
