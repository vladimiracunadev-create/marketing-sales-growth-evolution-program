# Lab 18.2 — Renovación

**Parte 18 · Customer experience, success y fidelización** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Ruta Andina gestiona la renovación la semana previa al vencimiento. El 38 % de las cuentas ya tomó su decisión antes de esa conversación.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **sistema de retención y expansión con onboarding, health score, renovación y advocacy**, aplicando en particular **renovación** y **voice of Customer continuo**.

> **Pregunta que debe quedar respondida:** ¿En qué momento el cliente obtiene valor y qué lo hace quedarse o irse?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-18-customer-experience-success-y-fidelizacion/`](../../curriculum/part-18-customer-experience-success-y-fidelizacion/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Iniciar el ciclo con anticipación suficiente.
2. Documentar la evidencia del resultado obtenido.
3. Detectar y trabajar los riesgos identificados.
4. Sostener la conversación de valor antes del vencimiento.
5. Cumplir el deber de información sobre la renovación.
6. Calcular o diseñar la captura de **tasa de renovación**, **anticipación del ciclo** y **renovaciones con evidencia de resultado**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Retener con castigos contractuales en lugar de valor entregado y dañar reputación.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **tasa de renovación** | contratos renovados, sobre contratos con vencimiento en el periodo |
| **anticipación del ciclo** | días entre el inicio de la gestión y el vencimiento, mediana |
| **renovaciones con evidencia de resultado** | renovaciones con documentación de resultado, sobre renovaciones gestionadas |
| **cobertura de entrevistas de baja** | bajas con entrevista realizada, sobre bajas totales |
| **hallazgos con acción asignada** | hallazgos con responsable y acción, sobre hallazgos registrados |
| **cambios implementados por voz de cliente** | modificaciones de producto o proceso originadas en el sistema, por trimestre |

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

- Gestionar la renovación en la semana del vencimiento. Inicia el ciclo con al menos 90 días de anticipación y documenta la evidencia de resultado.
- Registrar el motivo de baja con una lista cerrada. Ejecuta entrevistas estructuradas y contrasta el motivo declarado con datos de uso previos.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Nick Mehta, Dan Steinman y Lincoln Murphy — *Customer Success* (2016) — disciplina operativa de éxito de cliente: salud, renovación y expansión.
- Fred Reichheld, Darci Darnell y Maureen Burns — *Winning on Purpose* (2021) — lealtad, economía del cliente ganado y usos correctos e incorrectos del NPS.
- Peter Fader y Sarah Toms — *The Customer Centricity Playbook* (2018) — modelos de valor de vida del cliente y decisiones de inversión por cohorte.

---

[⬅ Laboratorios de la parte 18](./) · [Clases](../../curriculum/part-18-customer-experience-success-y-fidelizacion/README.md) · [Evaluación](../../assessments/part-18-assessment.md)
