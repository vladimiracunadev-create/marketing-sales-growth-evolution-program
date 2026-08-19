---
title: "Lab 15.2 — Venta cruzada y venta incremental"
type: lab
language: es
part: 15
lab: 2
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-19
---

# Lab 15.2 — Venta cruzada y venta incremental

**Parte 15 · E-commerce y marketplaces** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Ruta Andina recomienda su impresora térmica más cara a todos los compradores de lector de tarjetas. La aceptación es 3 % y la conversión del carrito cayó 8 %.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **simulación de tienda rentable con catálogo, checkout, costos y plan postventa**, aplicando en particular **venta cruzada y venta incremental** y **economía del e-commerce**.

> **Pregunta que debe quedar respondida:** ¿Dónde se pierde el pedido y cuánto queda después de comisión, envío y devolución?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-15-e-commerce-y-marketplaces/`](../../curriculum/part-15-e-commerce-y-marketplaces/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Analizar patrones reales de compra conjunta.
2. Definir el momento donde la sugerencia ayuda.
3. Priorizar pertinencia sobre margen.
4. Medir aceptación, conversión global y devoluciones.
5. Retirar las recomendaciones que dañan la conversión.
6. Calcular o diseñar la captura de **tasa de aceptación de la recomendación**, **efecto en conversión global** y **devoluciones de productos recomendados**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **tasa de aceptación de la recomendación** | recomendaciones aceptadas, sobre recomendaciones mostradas |
| **efecto en conversión global** | variación de la tasa de compra total con y sin recomendación |
| **devoluciones de productos recomendados** | devoluciones de productos añadidos por recomendación, sobre unidades añadidas |
| **contribución por pedido** | ingreso menos costos variables, dividido por pedidos |
| **frecuencia de recompra por cohorte** | compras por cliente en 12 meses, por cohorte de incorporación |
| **proporción de ingreso de clientes recurrentes** | ingreso de clientes con más de una compra, sobre ingreso total |

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

- Recomendar por margen y no por pertinencia. Construye las recomendaciones desde patrones reales de compra conjunta y mide el efecto en conversión global.
- Invertir en retención donde la categoría no permite recompra. Clasifica el modelo por frecuencia observada antes de asignar presupuesto de fidelización.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Peter Fader — *Customer Centricity* (2020, 2.ª ed.) — valor heterogéneo del cliente y asignación de recursos por valor esperado.
- Kevin Hillstrom — *Hillstrom's Multichannel Forensics* (2007) — diagnóstico de comportamiento de compra multicanal y migración de clientes.
- Robert B. Cialdini — *Influence: The Psychology of Persuasion, New and Expanded* (2021) — principios de influencia y su uso ético en contextos comerciales.

---

[⬅ Laboratorios de la parte 15](./) · [Clases](../../curriculum/part-15-e-commerce-y-marketplaces/README.md) · [Evaluación](../../assessments/part-15-assessment.md)
