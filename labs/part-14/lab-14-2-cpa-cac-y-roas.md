---
title: "Lab 14.2 — CPA, CAC y ROAS"
type: lab
language: es
part: 14
lab: 2
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-18
---

# Lab 14.2 — CPA, CAC y ROAS

**Parte 14 · Publicidad y performance marketing** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** El retorno publicitario reportado por Ruta Andina es 6,1 e incluye compras de clientes que ya eran clientes y que habrían comprado igual.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **plan de performance con estructura de campañas, presupuestos, medición y salvaguardas**, aplicando en particular **CPA, CAC y ROAS** y **fraude, brand safety y privacidad**.

> **Pregunta que debe quedar respondida:** ¿Qué unidad de resultado estoy comprando y a qué costo marginal deja de tener sentido?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-14-publicidad-y-performance-marketing/`](../../curriculum/part-14-publicidad-y-performance-marketing/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Definir el alcance de cada métrica por escrito.
2. Verificar qué ingreso es incremental y cuál no.
3. Calcular el costo de adquisición completo por canal.
4. Contrastar con margen y periodo de recuperación.
5. Decidir escalamiento sólo con economía verificada.
6. Calcular o diseñar la captura de **costo de adquisición completo por canal**, **proporción de ingreso incremental** y **relación valor de vida a costo de adquisición**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Atribuirse demanda existente, inflar el retorno y decidir presupuesto sobre una ilusión.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **costo de adquisición completo por canal** | gasto total atribuible dividido por clientes nuevos del canal |
| **proporción de ingreso incremental** | ingreso incremental estimado, sobre ingreso atribuido |
| **relación valor de vida a costo de adquisición** | valor de vida dividido por costo de adquisición, por canal |
| **proporción de tráfico no válido** | interacciones marcadas como inválidas, sobre interacciones totales |
| **apariciones en contexto no deseado** | impresiones en sitios excluidos o inapropiados, sobre impresiones totales |
| **tasa de consentimiento válido** | visitantes con consentimiento registrado conforme, sobre visitantes totales |

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

- Reportar retorno publicitario incluyendo ingreso no incremental. Separa clientes nuevos de recurrentes y estima incrementalidad antes de reportar retorno.
- Operar sin listas de exclusión ni revisión de tráfico. Define exclusiones y revisa mensualmente los informes de calidad de tráfico.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — una métrica que importa por etapa y por modelo de negocio.
- Avinash Kaushik — *Web Analytics 2.0* (2009) — medición orientada a decisión, segmentación y crítica del dato de vanidad.
- Ron Kohavi, Diane Tang y Ya Xu — *Trustworthy Online Controlled Experiments* (2020) — diseño estadístico de experimentos, métricas guardrail y trampas de interpretación.

---

[⬅ Laboratorios de la parte 14](./) · [Clases](../../curriculum/part-14-publicidad-y-performance-marketing/README.md) · [Evaluación](../../assessments/part-14-assessment.md)
