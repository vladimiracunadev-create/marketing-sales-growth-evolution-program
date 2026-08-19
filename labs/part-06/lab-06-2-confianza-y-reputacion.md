---
title: "Lab 06.2 — Confianza y reputación"
type: lab
language: es
part: 06
lab: 2
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-18
---

# Lab 06.2 — Confianza y reputación

**Parte 06 · Marca, branding y comunicación estratégica** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Una caída de ocho horas dejó a 120 clientes de Ruta Andina sin agenda. La empresa no comunicó nada hasta que los reclamos aparecieron en un grupo gremial.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **brand book mínimo viable con activos distintivos, promesa y sistema de medición**, aplicando en particular **confianza y reputación** y **medición de marca**.

> **Pregunta que debe quedar respondida:** ¿Qué debe recordar el mercado sobre nosotros cuando aparece la necesidad?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-06-marca-branding-y-comunicacion-estrategica/`](../../curriculum/part-06-marca-branding-y-comunicacion-estrategica/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Monitorear señales públicas de reputación.
2. Definir el protocolo de respuesta ante incidentes.
3. Reconocer y reparar antes de comunicar.
4. Documentar la causa raíz y la prevención.
5. Medir la recuperación en indicadores de confianza.
6. Calcular o diseñar la captura de **tiempo de respuesta ante incidente**, **tasa de reclamos resueltos en primera instancia** y **evolución de menciones negativas**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Confundir gusto estético del equipo con construcción de memoria en el mercado.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **tiempo de respuesta ante incidente** | horas entre la detección del incidente y la comunicación al cliente afectado |
| **tasa de reclamos resueltos en primera instancia** | reclamos cerrados sin escalamiento, sobre reclamos recibidos |
| **evolución de menciones negativas** | variación del volumen de menciones negativas tras el incidente |
| **notoriedad espontánea por ola** | proporción que nombra la marca sin ayuda, por ola y por segmento |
| **consideración por ola** | proporción que incluiría la marca en su evaluación, por ola |
| **relación marca-costo de adquisición** | correlación observada entre indicadores de marca y costo por cliente ganado |

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

- Comunicar antes de reparar. Define el protocolo: contención, reparación, comunicación y prevención documentada, en ese orden.
- Usar métricas de redes como métricas de marca. Levanta notoriedad y consideración con método comparable entre olas.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Fred Reichheld, Darci Darnell y Maureen Burns — *Winning on Purpose* (2021) — lealtad, economía del cliente ganado y usos correctos e incorrectos del NPS.
- Seth Godin — *This Is Marketing* (2018) — marketing como servicio a un público mínimo viable y construcción de confianza.
- Matthew Dixon, Nick Toman y Rick DeLisi — *The Effortless Experience* (2013) — reducción del esfuerzo del cliente como motor de lealtad frente al deleite.

---

[⬅ Laboratorios de la parte 06](./) · [Clases](../../curriculum/part-06-marca-branding-y-comunicacion-estrategica/README.md) · [Evaluación](../../assessments/part-06-assessment.md)
