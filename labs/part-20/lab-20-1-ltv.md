---
title: "Lab 20.1 — Valor de vida del cliente"
type: lab
language: es
part: 20
lab: 1
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-19
---

# Lab 20.1 — Valor de vida del cliente

**Parte 20 · Analítica comercial y marketing science** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** El valor de vida que usa Ruta Andina supone retención constante de 96 % mensual. Sus cohortes reales muestran caídas de 8 % en los primeros meses y estabilización posterior.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **caso analítico integral con árbol de métricas, cohortes, incrementalidad y dashboard ejecutivo**, aplicando en particular **valor de vida del cliente** y **análisis de cohortes aplicado**.

> **Pregunta que debe quedar respondida:** ¿Esta cifra mide lo que creo que mide, y qué decisión cambiaría si estuviera equivocada?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-20-analitica-comercial-y-marketing-science/`](../../curriculum/part-20-analitica-comercial-y-marketing-science/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Calcular el margen de contribución con costos completos.
2. Estimar permanencia desde curvas de retención por cohorte.
3. Incorporar expansión y contracción observadas.
4. Aplicar tasa de descuento y declarar supuestos.
5. Presentar el resultado como rango y no como cifra única.
6. Calcular o diseñar la captura de **valor de vida por segmento**, **dispersión dentro del segmento** y **sensibilidad a la retención**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **valor de vida por segmento** | margen acumulado esperado, por segmento y cohorte |
| **dispersión dentro del segmento** | diferencia entre percentiles de valor dentro del mismo segmento |
| **sensibilidad a la retención** | variación del valor de vida ante un cambio de un punto en retención |
| **valor acumulado por cohorte** | margen acumulado por cliente, por cohorte y hito |
| **tendencia entre cohortes** | dirección del cambio entre cohortes sucesivas en el mismo hito |
| **cohortes con datos suficientes** | cohortes con antigüedad mínima para concluir, sobre cohortes analizadas |

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

- Proyectar con retención constante. Deriva la permanencia de curvas por cohorte y presenta el resultado como rango.
- Comparar cohortes en la misma fecha calendario. Compara siempre en el mismo hito de antigüedad desde la incorporación.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Peter Fader y Sarah Toms — *The Customer Centricity Playbook* (2018) — modelos de valor de vida del cliente y decisiones de inversión por cohorte.
- Peter Fader — *Customer Centricity* (2020, 2.ª ed.) — valor heterogéneo del cliente y asignación de recursos por valor esperado.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — pensamiento analítico: formulación del problema, evaluación y valor esperado.

---

[⬅ Laboratorios de la parte 20](./) · [Clases](../../curriculum/part-20-analitica-comercial-y-marketing-science/README.md) · [Evaluación](../../assessments/part-20-assessment.md)
