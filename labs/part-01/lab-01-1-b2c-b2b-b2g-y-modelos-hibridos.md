---
title: "Lab 01.1 — B2C, B2B, B2G y modelos híbridos"
type: lab
language: es
part: 01
lab: 1
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-19
---

# Lab 01.1 — B2C, B2B, B2G y modelos híbridos

**Parte 01 · Marketing y ventas: fundamentos del sistema comercial** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Ruta Andina vende en tres frentes con el mismo guion: peluquerías de un local, cadenas de 14 sucursales y municipios. En el frente municipal perdió tres procesos por no adjuntar boletas de garantía y en las cadenas presenta la misma demo de 20 minutos que usa con un local.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **mapa del sistema comercial con supuestos, métricas y puntos de fuga**, aplicando en particular **B2C, B2B, B2G y modelos híbridos** y **propuesta de valor inicial**.

> **Pregunta que debe quedar respondida:** ¿De qué depende realmente que esta empresa gane un cliente rentable y lo conserve?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-01-marketing-y-ventas-fundamentos-del-sistema-comercial/`](../../curriculum/part-01-marketing-y-ventas-fundamentos-del-sistema-comercial/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Identificar quién usa, quién decide, quién paga y quién puede vetar.
2. Estimar el riesgo personal de cada participante.
3. Mapear el proceso formal exigido, si existe.
4. Ajustar evidencia, materiales y plazos a esa estructura.
5. Definir el movimiento comercial coherente con el valor del contrato.
6. Calcular o diseñar la captura de **ciclo de compra mediano**, **número de contactos por negocio ganado** y **tasa de negocios detenidos por proceso formal**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Confundir actividad con resultado y comprometer presupuesto antes de tener un diagnóstico.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **ciclo de compra mediano** | días entre oportunidad calificada y firma, mediana por segmento y por modelo de venta |
| **número de contactos por negocio ganado** | personas distintas del cliente con al menos una interacción registrada, promedio por negocio cerrado |
| **tasa de negocios detenidos por proceso formal** | oportunidades bloqueadas por requisitos administrativos dividido por oportunidades del segmento público |
| **tasa de comprensión sin ayuda** | personas que reformulan correctamente la propuesta dividido por personas expuestas, en prueba de cinco minutos |
| **tasa de avance tras la primera exposición** | reuniones que avanzan a la siguiente etapa dividido por primeras reuniones sostenidas |
| **consistencia entre canales** | porcentaje de piezas activas cuyo mensaje central coincide con la propuesta aprobada |

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

- Usar el mismo material comercial en los tres modelos. Construye una versión por estructura de decisión y verifica qué evidencia pide cada rol.
- Escribir la propuesta para el equipo interno. Prueba la comprensión con personas del segmento que nunca oyeron hablar de la empresa.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Philip Kotler, Kevin Lane Keller y Alexander Chernev — *Marketing Management* (2021, 16.ª ed.) — estructura canónica del marketing: análisis, STP, mezcla comercial y gestión de la demanda.
- Robert B. Miller y Stephen E. Heiman — *The New Strategic Selling* (2005) — mapa de influencias, roles de compra y análisis de posición en cuentas complejas.
- Neil Rackham — *SPIN Selling* (1988) — investigación conductual sobre venta compleja: situación, problema, implicación y necesidad-beneficio.

---

[⬅ Laboratorios de la parte 01](./) · [Clases](../../curriculum/part-01-marketing-y-ventas-fundamentos-del-sistema-comercial/README.md) · [Evaluación](../../assessments/part-01-assessment.md)
