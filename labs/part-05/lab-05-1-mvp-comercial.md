---
title: "Lab 05.1 — MVP comercial"
type: lab
language: es
part: 05
lab: 1
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-19
---

# Lab 05.1 — MVP comercial

**Parte 05 · Producto, oferta y propuesta de valor** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Para probar el interés en un plan por cadena, Ruta Andina puede construir el módulo completo en tres meses o vender el plan y operarlo manualmente durante seis semanas.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **oferta lista para vender con propuesta de valor, alcance, garantía y prueba de concepto**, aplicando en particular **MVP comercial** y **packaging y bundling**.

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

1. Escribir la hipótesis y su criterio de refutación.
2. Elegir el nivel mínimo de fidelidad que la prueba requiere.
3. Definir la medición antes de lanzar.
4. Ejecutar con un grupo acotado y consentido.
5. Decidir perseverar, ajustar o abandonar con el criterio previo.
6. Calcular o diseñar la captura de **tiempo hasta el primer aprendizaje**, **costo por experimento** y **tasa de conversión del MVP**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Prometer resultados que la operación no puede sostener y generar churn temprano.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **tiempo hasta el primer aprendizaje** | días entre el inicio del experimento y la primera conclusión documentada |
| **costo por experimento** | costo directo e indirecto de la prueba, comparado con el valor de la decisión |
| **tasa de conversión del MVP** | usuarios que completaron la acción crítica, sobre usuarios expuestos |
| **distribución de ventas por plan** | unidades y margen por plan, sobre ventas totales del periodo |
| **tasa de migración entre planes** | clientes que cambian de plan, sobre clientes activos, por dirección del cambio |
| **margen por paquete** | ingreso menos costo de servir del paquete, dividido por ingreso del paquete |

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

- Llamar MVP a un producto reducido sin hipótesis. Define hipótesis, criterio de refutación y medición antes de decidir el alcance del MVP.
- Diseñar planes desde la arquitectura técnica. Construye los paquetes desde la disposición a pagar por atributo, medida en el segmento.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Eric Ries — *The Lean Startup* (2011) — construir-medir-aprender, MVP y decisión de perseverar o pivotar.
- Marty Cagan — *Inspired* (2017, 2.ª ed.) — descubrimiento de producto y riesgos de valor, usabilidad, viabilidad y factibilidad.
- Steve Blank y Bob Dorf — *The Startup Owner's Manual* (2012) — customer discovery y validación fuera del edificio como proceso reproducible.

---

[⬅ Laboratorios de la parte 05](./) · [Clases](../../curriculum/part-05-producto-oferta-y-propuesta-de-valor/README.md) · [Evaluación](../../assessments/part-05-assessment.md)
