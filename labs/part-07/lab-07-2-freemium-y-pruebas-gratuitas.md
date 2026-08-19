---
title: "Lab 07.2 — Freemium y pruebas gratuitas"
type: lab
language: es
part: 07
lab: 2
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-19
---

# Lab 07.2 — Freemium y pruebas gratuitas

**Parte 07 · Pricing y monetización** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Ruta Andina abrió un plan gratuito sin límites de uso. Tiene 1.900 cuentas gratuitas, 2 % de conversión y el 44 % de los tickets de soporte proviene de ellas.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **arquitectura de monetización con métrica de cobro, planes, price fences y política de descuentos**, aplicando en particular **freemium y pruebas gratuitas** y **experimentación de precios**.

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

1. Definir el objetivo del modelo gratuito.
2. Estimar el costo marginal de servir.
3. Diseñar el gatillo de conversión en torno al valor.
4. Medir conversión y calidad de la cohorte gratuita.
5. Ajustar límites o abandonar el modelo con criterio previo.
6. Calcular o diseñar la captura de **tasa de conversión a pago**, **costo de soporte por usuario gratuito** y **uso del gatillo de conversión**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Erosionar precio con descuentos tácticos y perder capacidad de subir precios después.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **tasa de conversión a pago** | usuarios que pasan a plan pagado, sobre usuarios gratuitos de la cohorte, a 90 días |
| **costo de soporte por usuario gratuito** | horas de soporte valorizadas, dividido por usuarios gratuitos activos |
| **uso del gatillo de conversión** | usuarios que alcanzan el límite definido, sobre usuarios gratuitos activos |
| **efecto en conversión** | diferencia de conversión entre grupos, con intervalo de confianza |
| **efecto en ingreso por visitante** | ingreso total dividido por visitantes, comparado entre grupos |
| **guardarraíl de reclamos** | reclamos por precio en el grupo de prueba, comparados con el de control |

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

- Abrir plan gratuito sin límite ni gatillo. Define el límite que activa la conversión y mide el costo marginal de servir antes de escalar.
- Detener el experimento al ver un resultado favorable. Fija duración y tamaño antes de iniciar y no evalúes resultados parciales como definitivos.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Wes Bush — *Product-Led Growth* (2019) — el producto como principal vehículo de adquisición, activación y expansión.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — una métrica que importa por etapa y por modelo de negocio.
- Madhavan Ramanujam y Georg Tacke — *Monetizing Innovation* (2016) — diseñar el producto alrededor del precio: disposición a pagar antes de construir.

---

[⬅ Laboratorios de la parte 07](./) · [Clases](../../curriculum/part-07-pricing-y-monetizacion/README.md) · [Evaluación](../../assessments/part-07-assessment.md)
