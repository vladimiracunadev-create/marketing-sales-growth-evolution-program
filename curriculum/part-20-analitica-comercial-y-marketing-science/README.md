---
title: "Parte 20 — Analítica comercial y marketing science"
type: part-index
language: es
part: 20
updated: 2026-08-19
---

# Parte 20 — Analítica comercial y marketing science

Esta parte trabaja el nivel **Crecimiento y analítica** del programa y su propósito es que llegues a poder **sostener decisiones de ingreso con métricas correctamente construidas**. Llegas desde la parte 19, *Growth marketing y growth engineering*, y lo que allí quedó resuelto se da por sabido aquí. Lo que produzcas aquí es material de entrada para la parte 21, *IA aplicada a marketing, ventas y servicio*.

Son 14 clases, alrededor de 35 horas de estudio dirigido, y todas empujan hacia la misma pregunta:

> **¿Esta cifra mide lo que creo que mide, y qué decisión cambiaría si estuviera equivocada?**

Esa pregunta no es retórica: al final de la parte tienes que poder responderla con un artefacto en la mano —caso analítico integral con árbol de métricas, cohortes, incrementalidad y dashboard ejecutivo— y no con una opinión.

## Sobre qué caso vas a trabajar

El CAC reportado por Ruta Andina excluye sueldos comerciales y el LTV usa un margen bruto que nunca fue validado con contabilidad.

Todo el programa ocurre en la misma empresa, **Ruta Andina SpA**: Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público. Trabajar siempre sobre el mismo caso permite comparar decisiones tomadas en partes distintas y ver cuáles se contradicen entre sí.

## Qué vas a saber hacer

Las competencias que se desarrollan aquí son **construcción de métricas**, **análisis de cohortes** y **diseño de experimentos y atribución**. Con ellas la parte habilita para el trabajo de Marketing analyst, Revenue analyst y Data-driven marketer, que es donde estas decisiones se toman de verdad.

## Cómo avanza la parte, clase a clase

Las clases van en orden y cada una supone la anterior. Esta es la secuencia y los conceptos que introduce cada sesión:

| # | Clase | Conceptos que introduce |
|---|---|---|
| 01 | [Árbol de métricas](class-01-arbol-de-metricas.md) | descomposición multiplicativa, variable accionable, nivel de agregación |
| 02 | [Conversión y embudos](class-02-conversion-y-funnels.md) | definición operacional, unidad de análisis, ventana de conversión |
| 03 | [Costo de adquisición de cliente](class-03-cac.md) | alcance del costo, costo por canal, periodo de atribución |
| 04 | [Valor de vida del cliente](class-04-ltv.md) | margen de contribución del cliente, permanencia esperada, heterogeneidad |
| 05 | [Periodo de recuperación](class-05-payback.md) | periodo de recuperación, restricción de caja, ritmo sostenible de adquisición |
| 06 | [Margen de contribución](class-06-contribution-margin.md) | costo variable, margen de contribución, costo escalonado |
| 07 | [Análisis de cohortes aplicado](class-07-cohort-analysis.md) | hito de antigüedad, efecto de mezcla, cohorte de comportamiento |
| 08 | [Modelos de atribución](class-08-attribution-models.md) | modelo basado en reglas, modelo basado en datos, ventana de contacto |
| 09 | [Incrementalidad](class-09-incrementalidad.md) | efecto incremental, grupo de control, prueba de suspensión |
| 10 | [A/B testing](class-10-a-b-testing.md) | significancia estadística, efecto mínimo detectable, comparaciones múltiples |
| 11 | [Proyección de resultados](class-11-forecasting.md) | tendencia, estacionalidad, estabilidad del proceso |
| 12 | [Fundamentos de marketing mix modeling](class-12-marketing-mix-modeling-fundamentos.md) | modelo agregado, variación necesaria, factor externo |
| 13 | [Dashboards ejecutivos](class-13-dashboards-ejecutivos.md) | contexto comparativo, jerarquía visual, banda de variación esperada |
| 14 | [Caso analítico integral](class-14-caso-analitico-integral.md) | análisis auditable, supuesto declarado, recomendación de asignación |

## Dónde se practica y cómo se evalúa

Leer la parte no la acredita. Los [laboratorios](../../labs/part-20/) te hacen ejecutar el método sobre el caso; la [evaluación de la parte](../../assessments/part-20-assessment.md) comprueba que puedes sostener las decisiones sin el material delante; el [caso extendido](../../cases/) exige integrar lo aprendido en una recomendación completa, y en [`templates/`](../../templates/) están los formatos que se usan para producir el artefacto. El resultado que va a tu portafolio es **caso analítico integral con árbol de métricas, cohortes, incrementalidad y dashboard ejecutivo**.

## Qué puede salir mal

Escalar inversión sobre una economía unitaria que no resiste una revisión financiera. Antes de llevar cualquier recomendación de esta parte a una operación real, revisa el [mapa regulatorio](../../docs/MAPA-REGULATORIO-CHILE.md) y las [reglas sobre datos personales](../../docs/DATOS-PERSONALES-Y-ETICA.md): la norma vigente manda sobre el material pedagógico.

## Bibliografía de la parte

Estas son las obras sobre las que se apoya la parte, con lo que aporta cada una y en cuántas de sus 14 clases aparece. Está comprobado que cada obra existe y cuál es la edición —el título enlaza a su localizador—; que la idea atribuida esté en el capítulo que indica cada clase es la lectura del programa y está para que la contrastes. La columna «Acceso» dice de antemano qué puedes leer sin pagar.

| Obra | Qué aporta | Clases | Localizador | Acceso |
|---|---|---:|---|---|
| Susan A. Ambrose et al. — [*How Learning Works*](https://openlibrary.org/isbn/9780470484104) (2010) | principios de aprendizaje: conocimiento previo, práctica y retroalimentación | 14 | ISBN 9780470484104 | comprar o biblioteca |
| Peter C. Brown, Henry L. Roediger III y Mark A. McDaniel — [*Make It Stick*](https://openlibrary.org/isbn/9780674419377) (2014) | recuperación espaciada, intercalado y dificultad deseable | 14 | ISBN 9780674419377 | comprar o biblioteca |
| Anders Ericsson y Robert Pool — [*Peak*](https://openlibrary.org/isbn/9781473513143) (2016) | práctica deliberada con criterios explícitos y retroalimentación inmediata | 14 | ISBN 9781473513143 | comprar o biblioteca |
| William Ellet — [*The Case Study Handbook*](https://openlibrary.org/isbn/9781633696150) (2018, ed. revisada) | análisis de casos: problema, decisión, evidencia y recomendación | 14 | ISBN 9781633696150 | comprar o biblioteca |
| Grant Wiggins y Jay McTighe — [*Understanding by Design*](https://openlibrary.org/isbn/9781416600350) (2005, 2.ª ed.) | diseño inverso desde el desempeño observable | 14 | ISBN 9781416600350 | comprar o biblioteca |
| Foster Provost y Tom Fawcett — [*Data Science for Business*](https://openlibrary.org/isbn/9781449374280) (2013) | pensamiento analítico: formulación del problema, evaluación y valor esperado | 13 | ISBN 9781449374280 | comprar o biblioteca |
| Alistair Croll y Benjamin Yoskovitz — [*Lean Analytics*](https://openlibrary.org/isbn/9781449335670) (2013) | una métrica que importa por etapa y por modelo de negocio | 9 | ISBN 9781449335670 | comprar o biblioteca |
| Avinash Kaushik — [*Web Analytics 2.0*](https://openlibrary.org/isbn/9780470596425) (2009) | medición orientada a decisión, segmentación y crítica del dato de vanidad | 7 | ISBN 9780470596425 | comprar o biblioteca |
| Ron Kohavi, Diane Tang y Ya Xu — [*Trustworthy Online Controlled Experiments*](https://openlibrary.org/isbn/9781108601375) (2020) | diseño estadístico de experimentos, métricas guardrail y trampas de interpretación | 5 | ISBN 9781108601375 | comprar o biblioteca |
| Donald J. Wheeler — [*Understanding Variation*](https://openlibrary.org/isbn/9780945320531) (2000) | distinguir variación común de variación especial antes de reaccionar a un KPI | 4 | ISBN 9780945320531 | comprar o biblioteca |
| Douglas W. Hubbard — [*How to Measure Anything*](https://openlibrary.org/isbn/9781118836446) (2014, 3.ª ed.) | medir lo que parece inmedible: valor de la información y reducción de incertidumbre | 3 | ISBN 9781118836446 | comprar o biblioteca |
| Peter Fader y Sarah Toms — [*The Customer Centricity Playbook*](https://openlibrary.org/isbn/9781613630914) (2018) | modelos de valor de vida del cliente y decisiones de inversión por cohorte | 3 | ISBN 9781613630914 | comprar o biblioteca |
| Les Binet y Peter Field — [*The Long and the Short of It*](https://openlibrary.org/isbn/9780852941348) (2013) | equilibrio entre construcción de marca a largo plazo y activación de ventas a corto plazo | 3 | ISBN 9780852941348 | comprar o biblioteca |
| Hermann Simon — [*Confessions of the Pricing Man*](https://openlibrary.org/isbn/9783319204000) (2015) | el precio como la palanca de utilidad más rápida y su relación con el valor percibido | 2 | ISBN 9783319204000 | comprar o biblioteca |
| Peter Fader — [*Customer Centricity*](https://openlibrary.org/isbn/9781613631447) (2020, 2.ª ed.) | valor heterogéneo del cliente y asignación de recursos por valor esperado | 2 | ISBN 9781613631447 | comprar o biblioteca |
| Robert S. Kaplan y David P. Norton — [*The Balanced Scorecard*](https://openlibrary.org/isbn/9780875846514) (1996) | traducción de la estrategia en indicadores causalmente conectados | 2 | ISBN 9780875846514 | comprar o biblioteca |
| Peep Laja y el equipo de CXL — [*Conversion Optimization Playbooks (CXL)*](https://cxl.com/institute/) (2024) | método CRO basado en investigación previa al test y validez estadística | 1 | fuente primaria | acceso limitado |
| Andrew S. Grove — [*High Output Management*](https://openlibrary.org/isbn/9780394532349) (1983) | output gerencial, indicadores adelantados y reuniones como herramienta de producción | 1 | ISBN 9780394532349 | comprar o biblioteca |
| Thomas T. Nagle y Georg Müller — [*The Strategy and Tactics of Pricing*](https://openlibrary.org/isbn/9781138737501) (2018, 6.ª ed.) | pricing basado en valor, estructura de precios, métrica de cobro y política de descuentos | 1 | ISBN 9781138737501 | comprar o biblioteca |

De todas ellas, las que ordenan el criterio de esta parte son Avinash Kaushik (*Web Analytics 2.0*), Alistair Croll y Benjamin Yoskovitz (*Lean Analytics*), Ron Kohavi, Diane Tang y Ya Xu (*Trustworthy Online Controlled Experiments*), Foster Provost y Tom Fawcett (*Data Science for Business*), Donald J. Wheeler (*Understanding Variation*) y Douglas W. Hubbard (*How to Measure Anything*). Si sólo puedes leer una, empieza por Avinash Kaushik — *Web Analytics 2.0*.

La bibliografía completa del programa, con el uso de cada obra clase a clase, está en [`docs/BIBLIOGRAFIA.md`](../../docs/BIBLIOGRAFIA.md); el registro con los localizadores comprobables, en [`sources/bibliography.json`](../../sources/bibliography.json).

---

[⬅ Índice del currículo](../README.md) · [Programa](../../README.md)
