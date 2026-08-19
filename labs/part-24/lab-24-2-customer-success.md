---
title: "Lab 24.2 — Customer Success del Capstone"
type: lab
language: es
part: 24
lab: 2
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-18
---

# Lab 24.2 — Customer Success del Capstone

**Parte 24 · Empresa real, regulación y Capstone** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** El Capstone exige mostrar cómo el onboarding produce el resultado prometido en la propuesta comercial y cómo se verificará.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **Capstone completo: empresa, evidencia, números, cumplimiento y defensa ejecutiva**, aplicando en particular **customer Success del Capstone** y **defensa ejecutiva**.

> **Pregunta que debe quedar respondida:** ¿Esta operación resiste una revisión comercial, financiera, legal y ética al mismo tiempo?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-24-empresa-real-regulacion-y-capstone/`](../../curriculum/part-24-empresa-real-regulacion-y-capstone/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Definir el resultado esperado por segmento.
2. Diseñar el onboarding que lo produce.
3. Construir el puntaje de salud con componentes justificados.
4. Definir el ciclo de renovación y el criterio de expansión.
5. Verificar la coherencia con lo prometido en la venta.
6. Calcular o diseñar la captura de **coherencia venta-entrega**, **tiempo hasta el primer valor proyectado** y **componentes del puntaje justificados**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Presentar un plan atractivo que no cumple la Ley 19.496, la Ley 21.719 o las reglas de libre competencia.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **coherencia venta-entrega** | promesas comerciales cubiertas por el proceso de entrega, sobre promesas declaradas |
| **tiempo hasta el primer valor proyectado** | días estimados hasta el primer resultado, por segmento |
| **componentes del puntaje justificados** | componentes con fundamento documentado, sobre componentes del puntaje |
| **respuestas sostenidas en evidencia** | respuestas con dato o razonamiento verificable, sobre preguntas recibidas |
| **límites reconocidos** | limitaciones declaradas espontáneamente, sobre limitaciones identificables |
| **coherencia bajo estrés** | respuestas consistentes ante escenarios adversos, sobre preguntas de estrés recibidas |

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

- Diseñar el onboarding sin verificar la promesa comercial. Contrasta cada promesa de la propuesta con el proceso que la entregaría.
- Defender afirmaciones que no se pueden sostener. Reconoce explícitamente los límites y qué evidencia haría falta para cerrarlos.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) — disciplina operativa de éxito de cliente: salud, renovación y expansión.
- Samuel Hulick — *The Elements of User Onboarding* (2014) — diseño del primer valor percibido y reducción del time-to-value.
- Peter Fader y Sarah Toms — *The Customer Centricity Playbook* (2018) — modelos de valor de vida del cliente y decisiones de inversión por cohorte.

---

[⬅ Laboratorios de la parte 24](./) · [Clases](../../curriculum/part-24-empresa-real-regulacion-y-capstone/README.md) · [Evaluación](../../assessments/part-24-assessment.md)
