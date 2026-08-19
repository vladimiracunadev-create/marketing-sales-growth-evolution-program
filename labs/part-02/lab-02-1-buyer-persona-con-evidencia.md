---
title: "Lab 02.1 — Buyer persona con evidencia"
type: lab
language: es
part: 02
lab: 1
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-18
---

# Lab 02.1 — Buyer persona con evidencia

**Parte 02 · Cliente y comportamiento del consumidor** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Ruta Andina tiene tres personas documentadas con nombres, edad y hobbies. Ninguna indica cómo evalúan proveedores, qué objeción aparece primero ni de dónde salió el dato.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **expediente de cliente con ICP, unidad de decisión, journey y fricciones priorizadas**, aplicando en particular **buyer persona con evidencia** y **customer journey**.

> **Pregunta que debe quedar respondida:** ¿Quién decide, quién usa, quién paga y qué progreso intenta lograr cada uno?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-02-cliente-y-comportamiento-del-consumidor/`](../../curriculum/part-02-cliente-y-comportamiento-del-consumidor/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Definir qué decisiones debe informar la persona.
2. Recolectar evidencia de entrevistas, CRM y analítica.
3. Escribir sólo atributos accionables con su fuente.
4. Marcar hipótesis pendientes y su plan de validación.
5. Fijar fecha de revisión del perfil.
6. Calcular o diseñar la captura de **proporción de atributos con fuente**, **uso efectivo del perfil** y **antigüedad del perfil**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Construir personas ficticias sin datos y usarlas para justificar decisiones caras.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **proporción de atributos con fuente** | atributos con fuente y fecha registradas, sobre atributos totales del perfil |
| **uso efectivo del perfil** | piezas o guiones que citan explícitamente un atributo del perfil, sobre piezas producidas |
| **antigüedad del perfil** | meses desde la última validación con datos nuevos |
| **esfuerzo percibido por etapa** | puntuación de esfuerzo declarada por el cliente al completar la etapa, escala uniforme y muestra mínima definida |
| **abandono por etapa** | clientes que no avanzan a la etapa siguiente, sobre los que ingresaron a la etapa actual |
| **brecha de expectativa en onboarding** | diferencia entre plazo prometido y plazo real de puesta en marcha, mediana en días |

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

- Documentar rasgos irrelevantes para la decisión comercial. Elimina todo atributo que no cambie mensaje, canal, oferta o proceso.
- Mapear el proceso interno y llamarlo journey. Reescribe cada etapa empezando por el verbo del cliente, no por el de la empresa.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Rob Fitzpatrick — *The Mom Test* (2013) — entrevistas que producen datos y no cortesía; preguntar por comportamiento pasado.
- Steve Portigal — *Interviewing Users* (2023, 2.ª ed.) — conducción de entrevistas, escucha activa y traducción de observación en decisión.
- Michael R. Solomon — *Consumer Behavior: Buying, Having, and Being* (2019, 13.ª ed.) — marco académico del comportamiento del consumidor: cultura, identidad y proceso de decisión.

---

[⬅ Laboratorios de la parte 02](./) · [Clases](../../curriculum/part-02-cliente-y-comportamiento-del-consumidor/README.md) · [Evaluación](../../assessments/part-02-assessment.md)
