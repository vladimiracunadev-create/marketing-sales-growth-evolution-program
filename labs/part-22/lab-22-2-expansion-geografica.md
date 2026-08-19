---
title: "Lab 22.2 — Expansión geográfica"
type: lab
language: es
part: 22
lab: 2
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-18
---

# Lab 22.2 — Expansión geográfica

**Parte 22 · Go-to-market, canales y expansión** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Ruta Andina abrió Perú y Chile simultáneamente en su plan. El equipo es el mismo, el soporte opera en horario chileno y la facturación local no está resuelta.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **plan GTM completo con beachhead, movimiento comercial, canales, economía y plan de lanzamiento**, aplicando en particular **expansión geográfica** y **métricas de go-to-market**.

> **Pregunta que debe quedar respondida:** ¿Qué movimiento comercial corresponde al valor del contrato, al ciclo y al comprador?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-22-go-to-market-canales-y-expansion/`](../../curriculum/part-22-go-to-market-canales-y-expansion/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Validar demanda y camino de acceso en la nueva geografía.
2. Identificar los requisitos de cumplimiento local.
3. Estimar el costo de presencia y el tiempo hasta el primer ingreso.
4. Construir referencias locales antes de escalar.
5. Definir el criterio de abandono con anticipación.
6. Calcular o diseñar la captura de **costo de entrada por geografía**, **tiempo hasta la primera referencia local** y **cumplimiento normativo verificado**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Abrir frentes simultáneos sin capacidad, diluir foco y llegar tarde a todos.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **costo de entrada por geografía** | inversión acumulada hasta el primer ingreso relevante |
| **tiempo hasta la primera referencia local** | meses hasta obtener un caso verificable en la zona |
| **cumplimiento normativo verificado** | requisitos identificados y cumplidos, sobre requisitos aplicables |
| **eficiencia del crecimiento** | ingreso incremental del periodo, sobre gasto comercial incremental |
| **periodo de recuperación por movimiento** | meses hasta recuperar el costo de adquisición, por movimiento |
| **deterioro de eficiencia al escalar** | variación de la eficiencia entre tramos crecientes de inversión |

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

- Tratar la nueva geografía como extensión del mercado actual. Valida demanda, acceso y cumplimiento como si fuera un mercado nuevo, con criterio de abandono definido.
- Reportar crecimiento sin reportar eficiencia. Presenta el ingreso incremental junto al gasto incremental que lo produjo.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Geoffrey A. Moore — *Crossing the Chasm* (2014, 3.ª ed.) — adopción tecnológica, beachhead market y el abismo entre visionarios y pragmáticos.
- Michael E. Porter — *Competitive Strategy* (1980) — estructura de industria, fuerzas competitivas y elección de una posición defendible.
- Richard Rumelt — *Good Strategy / Bad Strategy* (2011) — diagnóstico, política rectora y acción coherente frente a la estrategia decorativa.

---

[⬅ Laboratorios de la parte 22](./) · [Clases](../../curriculum/part-22-go-to-market-canales-y-expansion/README.md) · [Evaluación](../../assessments/part-22-assessment.md)
