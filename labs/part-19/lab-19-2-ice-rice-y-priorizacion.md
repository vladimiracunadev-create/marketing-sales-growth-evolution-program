---
title: "Lab 19.2 — ICE, RICE y priorización"
type: lab
language: es
part: 19
lab: 2
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-18
---

# Lab 19.2 — ICE, RICE y priorización

**Parte 19 · Growth marketing y growth engineering** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** El equipo de Ruta Andina puntúa el impacto con una escala sin criterios. La misma iniciativa recibe 8 y 3 de dos personas distintas.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **growth model con North Star, bucles, backlog priorizado y resultados de experimentos**, aplicando en particular **ICE, RICE y priorización** y **product-led growth**.

> **Pregunta que debe quedar respondida:** ¿Qué bucle hace que el crecimiento se retroalimente en lugar de depender del gasto?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-19-growth-marketing-y-growth-engineering/`](../../curriculum/part-19-growth-marketing-y-growth-engineering/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Definir la escala de cada componente con criterios.
2. Puntuar con participación de más de una persona.
3. Revisar los casos donde el puntaje contradice la intuición.
4. Ejecutar en orden y registrar el resultado.
5. Calibrar las estimaciones con los resultados observados.
6. Calcular o diseñar la captura de **calibración de estimaciones**, **dispersión entre evaluadores** y **orden de ejecución respetado**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **calibración de estimaciones** | diferencia entre impacto estimado y observado, por experimento |
| **dispersión entre evaluadores** | diferencia de puntajes asignados por distintas personas al mismo ítem |
| **orden de ejecución respetado** | experimentos ejecutados según prioridad, sobre experimentos ejecutados |
| **tasa de conversión autoservicio** | cuentas que pagan sin intervención comercial, sobre cuentas registradas |
| **tiempo hasta el valor sin asistencia** | días hasta el primer resultado en cuentas autoservicio, mediana |
| **expansión por uso** | aumento de ingreso por crecimiento de uso, sobre ingreso de la cohorte |

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

- Puntuar sin criterios definidos por escala. Define qué significa cada valor de la escala y calibra las estimaciones con resultados reales.
- Adoptar el modelo sin verificar el autoservicio real. Comprueba que un cliente pueda obtener valor sin intervención antes de lanzar el plan.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Sean Ellis y Morgan Brown — *Hacking Growth* (2017) — equipo multifuncional, ciclo de experimentación y aha moment.
- Douglas W. Hubbard — *How to Measure Anything* (2014, 3.ª ed.) — medir lo que parece inmedible: valor de la información y reducción de incertidumbre.
- Marty Cagan — *Inspired* (2017, 2.ª ed.) — descubrimiento de producto y riesgos de valor, usabilidad, viabilidad y factibilidad.

---

[⬅ Laboratorios de la parte 19](./) · [Clases](../../curriculum/part-19-growth-marketing-y-growth-engineering/README.md) · [Evaluación](../../assessments/part-19-assessment.md)
