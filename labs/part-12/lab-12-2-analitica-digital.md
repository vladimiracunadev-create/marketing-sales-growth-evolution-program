---
title: "Lab 12.2 — Analítica digital"
type: lab
language: es
part: 12
lab: 2
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-19
---

# Lab 12.2 — Analítica digital

**Parte 12 · Marketing digital y adquisición** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** El tablero de Ruta Andina tiene 34 métricas. En la reunión mensual se revisan tres y ninguna cambia una decisión.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **plan de adquisición digital con arquitectura de sitio, canales, medición y auditoría inicial**, aplicando en particular **analítica digital** y **plan de adquisición**.

> **Pregunta que debe quedar respondida:** ¿Qué activo digital genera demanda propia y qué parte del resultado es alquilada?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-12-marketing-digital-y-adquisicion/`](../../curriculum/part-12-marketing-digital-y-adquisicion/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Definir las decisiones que la analítica debe informar.
2. Traducirlas a preguntas y métricas con definición operacional.
3. Instrumentar sólo lo necesario y verificar la calidad.
4. Analizar por segmento y no sólo el agregado.
5. Revisar el plan cada semestre y eliminar lo que no se usa.
6. Calcular o diseñar la captura de **decisiones informadas por analítica**, **calidad de la instrumentación** y **métricas activas sin uso**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Optimizar métricas de vanidad y desatender consentimiento, cookies y datos personales.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **decisiones informadas por analítica** | decisiones documentadas que citan un análisis, por trimestre |
| **calidad de la instrumentación** | eventos que registran correctamente, sobre eventos auditados |
| **métricas activas sin uso** | métricas en tableros sin uso documentado, sobre métricas totales |
| **desviación frente a supuestos** | diferencia entre costo por oportunidad real y estimado, por canal |
| **utilización de la capacidad comercial** | oportunidades trabajadas, sobre capacidad definida del equipo |
| **reasignaciones ejecutadas** | movimientos de presupuesto realizados según la regla, por trimestre |

Cada ficha debe indicar además: fuente del dato, frecuencia de cálculo, responsable, lectura permitida y lectura prohibida. Si el dato no existe, se diseña el mecanismo de captura y se declara su costo.

## Entregables

1. `memo-decision.md` — problema, evidencia, dos alternativas, recomendación y gobierno.
2. `calculo.md` o notebook — cálculos con supuestos explícitos y fuentes.
3. `ficha-metricas.md` — definiciones operacionales completas.
4. `escenario-adverso.md` — recálculo bajo la restricción indicada.
5. `riesgo-y-cumplimiento.md` — verificación del riesgo de la parte y de la normativa aplicable.
6. Resumen ejecutivo de una página para defensa de cinco minutos.

## Rúbrica (100 puntos)

| Criterio | Puntos | Qué se evalúa |
|---|---:|---|
| Encuadre del problema | 15 | La decisión está formulada antes que la herramienta. |
| Calidad de la evidencia | 20 | Datos pertinentes con fuente, línea base y límites declarados. |
| Aplicación del método | 15 | Ejecución completa de la secuencia con trazabilidad por paso. |
| Medición | 20 | Fichas operacionales completas y cálculos verificables. |
| Decisión y trade-offs | 15 | Dos alternativas reales, costo de oportunidad y condición de revisión. |
| Riesgo y cumplimiento | 10 | Verificación del riesgo de la parte y de la normativa aplicable. |
| Comunicación | 5 | Resumen ejecutivo comprensible por alguien ajeno al trabajo. |

**Aprobación:** 80/100 y ningún criterio bajo el 60 % de su puntaje.

## Errores que invalidan el laboratorio

- Instrumentar todo sin plan de medición. Parte de las decisiones y elimina del tablero toda métrica que no informe una de ellas.
- Planificar volumen sin verificar capacidad de atención. Ajusta la meta de generación a la capacidad real del equipo comercial.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Avinash Kaushik — *Web Analytics 2.0* (2009) — medición orientada a decisión, segmentación y crítica del dato de vanidad.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — pensamiento analítico: formulación del problema, evaluación y valor esperado.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — una métrica que importa por etapa y por modelo de negocio.

---

[⬅ Laboratorios de la parte 12](./) · [Clases](../../curriculum/part-12-marketing-digital-y-adquisicion/README.md) · [Evaluación](../../assessments/part-12-assessment.md)
