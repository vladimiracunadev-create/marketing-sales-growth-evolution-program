---
title: "Lab 16.2 — Velocidad comercial"
type: lab
language: es
part: 16
lab: 2
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-18
---

# Lab 16.2 — Velocidad comercial

**Parte 16 · CRM, pipeline y sales operations** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** El ciclo mediano de Ruta Andina es 71 días y el 44 % de ese tiempo transcurre entre el envío de la propuesta y la primera respuesta del cliente.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **diseño de sales operations con pipeline, criterios de etapa, forecast y gobierno de datos**, aplicando en particular **velocidad comercial** y **gobierno del CRM**.

> **Pregunta que debe quedar respondida:** ¿El pipeline describe la realidad o solo el optimismo del equipo?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-16-crm-pipeline-y-sales-operations/`](../../curriculum/part-16-crm-pipeline-y-sales-operations/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Calcular las cuatro variables con datos propios.
2. Simular el efecto de mejorar cada una por separado.
3. Identificar la palanca dominante y su costo.
4. Intervenir sobre esa palanca.
5. Medir el efecto y recalcular.
6. Calcular o diseñar la captura de **duración mediana del ciclo**, **valor promedio de oportunidad** y **velocidad comercial calculada**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Tomar decisiones de contratación y presupuesto sobre un pipeline que no representa la realidad.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **duración mediana del ciclo** | días entre creación y cierre de la oportunidad, mediana por segmento |
| **valor promedio de oportunidad** | valor total de negocios ganados, sobre número de negocios ganados |
| **velocidad comercial calculada** | resultado del cálculo combinado, seguido por trimestre |
| **cambios documentados** | modificaciones con solicitud y aprobación registradas, sobre cambios realizados |
| **campos y reglas sin uso** | elementos de configuración sin uso, sobre elementos totales |
| **accesos revisados** | usuarios con permisos revisados en el último semestre, sobre usuarios activos |

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

- Buscar sólo más oportunidades. Simula el efecto de reducir el ciclo y de mejorar la tasa de cierre antes de aumentar la generación.
- Permitir cambios sin registro ni responsable. Designa un responsable del sistema y exige solicitud documentada para cada cambio de configuración.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Mark Roberge — *The Sales Acceleration Formula* (2015) — contratación, formación, gestión y demanda comercial gobernadas por datos.
- Andrew S. Grove — *High Output Management* (1983) — output gerencial, indicadores adelantados y reuniones como herramienta de producción.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — una métrica que importa por etapa y por modelo de negocio.

---

[⬅ Laboratorios de la parte 16](./) · [Clases](../../curriculum/part-16-crm-pipeline-y-sales-operations/README.md) · [Evaluación](../../assessments/part-16-assessment.md)
