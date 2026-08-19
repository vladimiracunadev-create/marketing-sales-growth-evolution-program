---
title: "Lab 04.2 — Mapas perceptuales"
type: lab
language: es
part: 04
lab: 2
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-19
---

# Lab 04.2 — Mapas perceptuales

**Parte 04 · Segmentación, targeting y posicionamiento** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** El mapa que Ruta Andina usa en su plan fue dibujado por el equipo de marketing en una jornada de trabajo. Ninguna de las posiciones proviene de una medición con clientes.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **arquitectura STP con criterios de atractivo, accesibilidad y declaración de posicionamiento probada**, aplicando en particular **mapas perceptuales** y **prueba de posicionamiento**.

> **Pregunta que debe quedar respondida:** ¿Qué segmento puedo servir mejor que nadie y con qué diferencia comprobable?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-04-segmentacion-targeting-y-posicionamiento/`](../../curriculum/part-04-segmentacion-targeting-y-posicionamiento/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Identificar los criterios de decisión con investigación previa.
2. Medir la percepción con una muestra del segmento.
3. Construir el mapa con datos y no con juicio interno.
4. Evaluar si los espacios vacantes tienen demanda.
5. Definir el movimiento de posición y su costo.
6. Calcular o diseñar la captura de **consistencia de la percepción**, **distancia con el competidor principal** y **cambio de posición en el tiempo**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Segmentar con variables decorativas que no cambian oferta, canal ni mensaje.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **consistencia de la percepción** | dispersión de las respuestas sobre la ubicación de la marca en cada eje |
| **distancia con el competidor principal** | diferencia media de puntuación entre ambas marcas en los ejes relevantes |
| **cambio de posición en el tiempo** | variación de la posición medida entre dos olas de medición |
| **comprensión correcta** | personas que reformulan la promesa sin error, sobre personas expuestas |
| **recuerdo del beneficio central** | personas que recuerdan el beneficio tras 24 horas, sobre expuestas |
| **preferencia declarada frente a alternativa** | proporción que elige la propuesta sobre la alternativa, con intervalo reportado |

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

- Dibujar el mapa sin medición. Recoge percepción con una muestra del segmento antes de ubicar cualquier marca en el mapa.
- Elegir el mensaje por votación del equipo. Prueba con el segmento destinatario y decide por comprensión y recuerdo, no por gusto interno.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Al Ries y Jack Trout — *Positioning: The Battle for Your Mind* (2001, ed. revisada) — posicionamiento como lugar en la mente del cliente y no como declaración interna.
- Kevin Lane Keller y Vanitha Swaminathan — *Strategic Brand Management* (2019, 5.ª ed.) — modelo CBBE: notoriedad, significado, respuesta y resonancia de marca.
- Naresh K. Malhotra — *Marketing Research: An Applied Orientation* (2019, 7.ª ed.) — diseño de investigación, muestreo, medición y análisis con rigor metodológico.

---

[⬅ Laboratorios de la parte 04](./) · [Clases](../../curriculum/part-04-segmentacion-targeting-y-posicionamiento/README.md) · [Evaluación](../../assessments/part-04-assessment.md)
