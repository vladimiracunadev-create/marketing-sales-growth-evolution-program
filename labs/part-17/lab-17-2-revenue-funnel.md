---
title: "Lab 17.2 — Embudo de ingresos"
type: lab
language: es
part: 17
lab: 2
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-19
---

# Lab 17.2 — Embudo de ingresos

**Parte 17 · Marketing automation y revenue operations** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** El embudo de Ruta Andina termina en la firma. La mayor pérdida de valor ocurre entre la firma y el día 90, y no aparece en ningún informe.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **operating model de RevOps con lifecycle, scoring, SLA, integraciones y observabilidad**, aplicando en particular **embudo de ingresos** y **gobernanza de automatizaciones**.

> **Pregunta que debe quedar respondida:** ¿Qué automatizo porque mejora el sistema y qué estaría solo escalando un desorden?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-17-marketing-automation-y-revenue-operations/`](../../curriculum/part-17-marketing-automation-y-revenue-operations/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Definir las etapas del recorrido completo.
2. Acordar criterios entre áreas.
3. Medir volumen, conversión y valor por tramo.
4. Identificar la mayor pérdida de valor.
5. Asignar responsable por tramo.
6. Calcular o diseñar la captura de **conversión por tramo**, **valor perdido por tramo** y **cobertura de definiciones compartidas**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **conversión por tramo** | unidades que avanzan, sobre unidades que ingresaron al tramo |
| **valor perdido por tramo** | ingreso anual estimado que se pierde en cada transición |
| **cobertura de definiciones compartidas** | etapas con criterio acordado entre áreas, sobre etapas totales |
| **flujos con base legal documentada** | automatizaciones con finalidad y base registradas, sobre automatizaciones activas |
| **flujos retirados por revisión** | automatizaciones desactivadas por obsolescencia, por semestre |
| **cambios con aprobación registrada** | modificaciones con aprobación documentada, sobre modificaciones realizadas |

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

- Terminar el embudo en la venta. Extiende el análisis hasta renovación y expansión, y mide el valor perdido en cada tramo.
- Mantener flujos activos sin propósito ni base documentada. Audita las automatizaciones cada semestre y retira las que no tengan finalidad vigente.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) — integración de datos, procesos y equipos que producen ingreso como un solo sistema.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — una métrica que importa por etapa y por modelo de negocio.
- Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) — disciplina operativa de éxito de cliente: salud, renovación y expansión.

---

[⬅ Laboratorios de la parte 17](./) · [Clases](../../curriculum/part-17-marketing-automation-y-revenue-operations/README.md) · [Evaluación](../../assessments/part-17-assessment.md)
