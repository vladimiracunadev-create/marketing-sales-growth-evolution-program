---
title: "Lab 07.1 — Pricing basado en valor"
type: lab
language: es
part: 07
lab: 1
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-19
---

# Lab 07.1 — Pricing basado en valor

**Parte 07 · Pricing y monetización** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Para un taller que pierde 6 citas semanales a CLP 45.000 cada una, el valor diferencial de reducir inasistencias a la mitad es del orden de CLP 540.000 mensuales. El plan cuesta CLP 79.000.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **arquitectura de monetización con métrica de cobro, planes, price fences y política de descuentos**, aplicando en particular **pricing basado en valor** y **van Westendorp y técnicas de investigación de precio**.

> **Pregunta que debe quedar respondida:** ¿Cuánto vale esto para quién, y qué estructura de cobro alinea precio con valor entregado?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-07-pricing-y-monetizacion/`](../../curriculum/part-07-pricing-y-monetizacion/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Identificar la alternativa de referencia del segmento.
2. Cuantificar el valor diferencial en unidades del cliente.
3. Verificar la cuantificación con clientes reales.
4. Definir la regla de captura y justificarla.
5. Probar el precio resultante antes de generalizarlo.
6. Calcular o diseñar la captura de **valor diferencial verificado**, **tasa de aceptación al nuevo precio** y **proporción de valor capturado**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **valor diferencial verificado** | clientes que confirman la magnitud estimada, sobre clientes consultados |
| **tasa de aceptación al nuevo precio** | aceptaciones, sobre propuestas presentadas con el precio basado en valor |
| **proporción de valor capturado** | precio cobrado, sobre valor diferencial estimado, por segmento |
| **amplitud del rango aceptable** | diferencia entre los extremos del rango identificado, por segmento |
| **coincidencia entre métodos** | diferencia entre el rango declarado y el precio de aceptación observado |
| **tamaño de muestra por segmento** | respuestas válidas por segmento, comparadas con el mínimo definido |

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

- Cuantificar el valor sin verificarlo con clientes. Presenta el cálculo a cinco clientes y ajusta los supuestos que rechacen.
- Fijar el precio en el extremo inferior del rango. Contrasta el rango declarado con el valor diferencial cuantificado antes de decidir.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Thomas T. Nagle y Georg Müller — *The Strategy and Tactics of Pricing* (2018, 6.ª ed.) — pricing basado en valor, estructura de precios, métrica de cobro y política de descuentos.
- Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) — diseñar el producto alrededor del precio: disposición a pagar antes de construir.
- Hermann Simon — *Confessions of the Pricing Man* (2015) — el precio como la palanca de utilidad más rápida y su relación con el valor percibido.

---

[⬅ Laboratorios de la parte 07](./) · [Clases](../../curriculum/part-07-pricing-y-monetizacion/README.md) · [Evaluación](../../assessments/part-07-assessment.md)
