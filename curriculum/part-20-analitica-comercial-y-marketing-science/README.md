---
title: "Parte 20 — Analítica comercial y marketing science"
type: part-index
language: es
part: 20
updated: 2026-08-19
---

# Parte 20 — Analítica comercial y marketing science

**Nivel:** Crecimiento y analítica · **Clases:** 14 · **Carga estimada:** 35 horas de estudio dirigido

## Resultado de la parte

Al terminar esta parte debes poder **sostener decisiones de ingreso con métricas correctamente construidas**.

> **Pregunta rectora:** ¿Esta cifra mide lo que creo que mide, y qué decisión cambiaría si estuviera equivocada?

## Caso de la parte

El CAC reportado por Ruta Andina excluye sueldos comerciales y el LTV usa un margen bruto que nunca fue validado con contabilidad.

El caso persistente del programa es **Ruta Andina SpA**: Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

## Competencias que desarrolla

- construcción de métricas
- análisis de cohortes
- diseño de experimentos y atribución

**Roles a los que habilita:** Marketing analyst, Revenue analyst y Data-driven marketer.

## Clases

| # | Clase | Conceptos centrales |
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

## Práctica y evaluación

| Recurso | Ruta |
|---|---|
| Laboratorios | [`labs/part-20/`](../../labs/part-20/) |
| Evaluación de la parte | [`assessments/part-20-assessment.md`](../../assessments/part-20-assessment.md) |
| Caso extendido | [`cases/case-20-*.md`](../../cases/) |
| Plantillas | [`templates/`](../../templates/) |

**Artefacto de portafolio:** caso analítico integral con árbol de métricas, cohortes, incrementalidad y dashboard ejecutivo.

## Riesgo a vigilar

Escalar inversión sobre una economía unitaria que no resiste una revisión financiera. Revisa `docs/MAPA-REGULATORIO-CHILE.md` y `docs/DATOS-PERSONALES-Y-ETICA.md` antes de llevar cualquier recomendación a una operación real.

## Bibliografía rectora de la parte

- Avinash Kaushik — *Web Analytics 2.0* (2009) — medición orientada a decisión, segmentación y crítica del dato de vanidad.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — una métrica que importa por etapa y por modelo de negocio.
- Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) — diseño estadístico de experimentos, métricas guardrail y trampas de interpretación.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — pensamiento analítico: formulación del problema, evaluación y valor esperado.
- Donald J. Wheeler — *Understanding Variation* (2000) — distinguir variación común de variación especial antes de reaccionar a un KPI.
- Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) — medir lo que parece inmedible: valor de la información y reducción de incertidumbre.

---

[⬅ Índice del currículo](../README.md) · [Programa](../../README.md)
