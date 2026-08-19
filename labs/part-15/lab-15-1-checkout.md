---
title: "Lab 15.1 — Checkout"
type: lab
language: es
part: 15
lab: 1
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-18
---

# Lab 15.1 — Checkout

**Parte 15 · E-commerce y marketplaces** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** El checkout de Ruta Andina revela el costo de despacho en el último paso. El abandono en ese paso es 63 %.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **simulación de tienda rentable con catálogo, checkout, costos y plan postventa**, aplicando en particular **checkout** y **conversión en comercio digital**.

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

1. Medir el abandono por paso del checkout.
2. Revelar todos los costos antes de iniciar el proceso.
3. Eliminar campos y pasos no indispensables.
4. Ofrecer compra sin registro obligatorio.
5. Probar el flujo en dispositivos reales del segmento.
6. Calcular o diseñar la captura de **tasa de abandono por paso**, **tiempo de finalización** y **tasa de error en pagos**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Incumplir derecho de retracto, garantía legal y reglas de información al consumidor.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **tasa de abandono por paso** | abandonos, sobre entradas a cada paso del checkout |
| **tiempo de finalización** | mediana de segundos para completar el pago, por dispositivo |
| **tasa de error en pagos** | intentos fallidos, sobre intentos de pago |
| **tasa de paso por etapa** | usuarios que avanzan, sobre usuarios que ingresaron a la etapa |
| **pérdida absoluta por etapa** | número de usuarios perdidos en cada etapa, por periodo |
| **conversión por dispositivo** | pedidos, sobre sesiones, comparado entre móvil y escritorio |

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

- Revelar el costo de despacho al final. Muestra el costo total estimado desde la página de producto o el carrito.
- Trabajar sobre el peor porcentaje y no sobre la mayor pérdida. Prioriza por número absoluto de usuarios perdidos y por valor en juego.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Steve Krug — *Don't Make Me Think, Revisited* (2014) — usabilidad, claridad y pruebas baratas con usuarios reales.
- Peep Laja y el equipo de CXL — *Conversion Optimization Playbooks (CXL)* (2024) — método CRO basado en investigación previa al test y validez estadística.
- Bryan Eisenberg y Jeffrey Eisenberg — *Call to Action* (2005) — optimización de conversión con hipótesis, escenarios y persuasión medible.

---

[⬅ Laboratorios de la parte 15](./) · [Clases](../../curriculum/part-15-e-commerce-y-marketplaces/README.md) · [Evaluación](../../assessments/part-15-assessment.md)
