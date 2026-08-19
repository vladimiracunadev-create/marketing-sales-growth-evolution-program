---
title: "Lab 05.2 — Portafolio y arquitectura de oferta"
type: lab
language: es
part: 05
lab: 2
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-18
---

# Lab 05.2 — Portafolio y arquitectura de oferta

**Parte 05 · Producto, oferta y propuesta de valor** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Ruta Andina mantiene once combinaciones de plan y hardware. Cuatro representan el 2 % del ingreso y consumen un tercio de las consultas de soporte.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **oferta lista para vender con propuesta de valor, alcance, garantía y prueba de concepto**, aplicando en particular **portafolio y arquitectura de oferta** y **prueba de concepto comercial**.

> **Pregunta que debe quedar respondida:** ¿Qué compra realmente el cliente y por qué elegiría esta oferta frente a no hacer nada?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-05-producto-oferta-y-propuesta-de-valor/`](../../curriculum/part-05-producto-oferta-y-propuesta-de-valor/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Asignar un rol explícito a cada producto.
2. Calcular margen y consumo de capacidad por producto.
3. Diseñar la escalera de crecimiento del cliente.
4. Eliminar o fusionar lo que no cumple rol.
5. Revisar la asignación de capacidad cada trimestre.
6. Calcular o diseñar la captura de **margen y capacidad por producto**, **tasa de ascenso en la escalera** y **productos sin rol definido**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Prometer resultados que la operación no puede sostener y generar churn temprano.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **margen y capacidad por producto** | margen de contribución y horas de equipo consumidas por producto, por trimestre |
| **tasa de ascenso en la escalera** | clientes que migran a un producto superior, sobre clientes elegibles |
| **productos sin rol definido** | productos activos sin rol asignado, sobre productos totales |
| **tasa de aceptación con precio real** | aceptaciones, sobre propuestas presentadas en la prueba |
| **tiempo de decisión** | días entre presentación de la propuesta y respuesta del cliente, mediana |
| **objeciones por categoría** | objeciones clasificadas por causa, sobre propuestas rechazadas |

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

- Lanzar productos sin asignarles un rol. Exige rol, métrica y capacidad asignada antes de aprobar cualquier lanzamiento.
- Probar interés sin mostrar el precio. Presenta el precio efectivo: sin él, la aceptación declarada no predice compra.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Philip Kotler, Kevin Lane Keller y Alexander Chernev — *Marketing Management* (2021, 16.ª ed.) — estructura canónica del marketing: análisis, STP, mezcla comercial y gestión de la demanda.
- Marty Cagan — *Inspired* (2017, 2.ª ed.) — descubrimiento de producto y riesgos de valor, usabilidad, viabilidad y factibilidad.
- Richard Rumelt — *Good Strategy / Bad Strategy* (2011) — diagnóstico, política rectora y acción coherente frente a la estrategia decorativa.

---

[⬅ Laboratorios de la parte 05](./) · [Clases](../../curriculum/part-05-producto-oferta-y-propuesta-de-valor/README.md) · [Evaluación](../../assessments/part-05-assessment.md)
