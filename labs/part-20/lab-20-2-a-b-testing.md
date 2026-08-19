---
title: "Lab 20.2 — A/B testing"
type: lab
language: es
part: 20
lab: 2
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-19
---

# Lab 20.2 — A/B testing

**Parte 20 · Analítica comercial y marketing science** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Ruta Andina evaluó siete métricas en un mismo test y declaró victoria por la única que resultó favorable. Con siete comparaciones, ese resultado es esperable por azar.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **caso analítico integral con árbol de métricas, cohortes, incrementalidad y dashboard ejecutivo**, aplicando en particular **A/B testing** y **dashboards ejecutivos**.

> **Pregunta que debe quedar respondida:** ¿Esta cifra mide lo que creo que mide, y qué decisión cambiaría si estuviera equivocada?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-20-analitica-comercial-y-marketing-science/`](../../curriculum/part-20-analitica-comercial-y-marketing-science/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Definir hipótesis, métrica principal y guardarraíles.
2. Calcular muestra y duración antes de iniciar.
3. Ejecutar sin mirar resultados parciales.
4. Analizar con el criterio previo y corregir por comparaciones múltiples.
5. Replicar los resultados que sostienen decisiones importantes.
6. Calcular o diseñar la captura de **potencia calculada antes de iniciar**, **tasa de replicación** y **tests detenidos anticipadamente**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Escalar inversión sobre una economía unitaria que no resiste una revisión financiera.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **potencia calculada antes de iniciar** | tests con cálculo previo de muestra, sobre tests ejecutados |
| **tasa de replicación** | resultados confirmados al repetir, sobre resultados positivos |
| **tests detenidos anticipadamente** | pruebas interrumpidas antes del plazo, sobre pruebas ejecutadas |
| **tiempo de lectura** | minutos que tarda un ejecutivo en identificar el estado y las decisiones |
| **indicadores con banda definida** | métricas con rango esperado, sobre métricas del tablero |
| **decisiones tomadas con el tablero** | decisiones documentadas que lo citan, por trimestre |

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

- Evaluar múltiples métricas y declarar victoria por la favorable. Declara una métrica principal antes de iniciar y corrige por comparaciones múltiples.
- Presentar cifras sin meta ni comparación. Agrega contexto comparativo y banda de variación esperada a cada indicador.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) — diseño estadístico de experimentos, métricas guardrail y trampas de interpretación.
- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — pensamiento analítico: formulación del problema, evaluación y valor esperado.
- Peep Laja y el equipo de CXL — *Conversion Optimization Playbooks (CXL)* (2024) — método CRO basado en investigación previa al test y validez estadística.

---

[⬅ Laboratorios de la parte 20](./) · [Clases](../../curriculum/part-20-analitica-comercial-y-marketing-science/README.md) · [Evaluación](../../assessments/part-20-assessment.md)
