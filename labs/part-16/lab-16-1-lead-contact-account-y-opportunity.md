---
title: "Lab 16.1 — Lead, contacto, cuenta y oportunidad"
type: lab
language: es
part: 16
lab: 1
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-19
---

# Lab 16.1 — Lead, contacto, cuenta y oportunidad

**Parte 16 · CRM, pipeline y sales operations** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** La cadena de 14 locales aparece como 14 cuentas distintas en el CRM de Ruta Andina. Nadie puede ver el ingreso total ni el riesgo de concentración.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **diseño de sales operations con pipeline, criterios de etapa, forecast y gobierno de datos**, aplicando en particular **lead, contacto, cuenta y oportunidad** y **forecast**.

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

1. Definir cada entidad por escrito y con ejemplos.
2. Establecer las reglas de conversión entre entidades.
3. Configurar el sistema para impedir duplicaciones.
4. Capacitar al equipo con casos límite.
5. Auditar la consistencia del modelo cada trimestre.
6. Calcular o diseñar la captura de **duplicados de cuenta**, **oportunidades sin cuenta asociada** y **consistencia de conversión**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Tomar decisiones de contratación y presupuesto sobre un pipeline que no representa la realidad.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **duplicados de cuenta** | cuentas duplicadas detectadas, sobre cuentas totales |
| **oportunidades sin cuenta asociada** | oportunidades huérfanas, sobre oportunidades activas |
| **consistencia de conversión** | leads convertidos según la regla definida, sobre leads convertidos |
| **precisión del forecast** | diferencia porcentual entre proyección y cierre real, por trimestre |
| **sesgo sistemático** | promedio de la desviación con signo, por vendedor y por periodo |
| **cobertura del pipeline** | valor del pipeline, sobre la meta del periodo |

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

- Registrar sucursales como cuentas independientes. Define la jerarquía de cuentas y consolida las sucursales bajo la organización matriz.
- Mantener el método pese a un sesgo sistemático. Mide la desviación con signo por trimestre y corrige el método con ese factor.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) — integración de datos, procesos y equipos que producen ingreso como un solo sistema.
- Mark Roberge — *The Sales Acceleration Formula* (2015) — contratación, formación, gestión y demanda comercial gobernadas por datos.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — pensamiento analítico: formulación del problema, evaluación y valor esperado.

---

[⬅ Laboratorios de la parte 16](./) · [Clases](../../curriculum/part-16-crm-pipeline-y-sales-operations/README.md) · [Evaluación](../../assessments/part-16-assessment.md)
