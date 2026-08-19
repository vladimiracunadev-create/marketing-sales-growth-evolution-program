---
title: "Lab 21.1 — Generación de contenido con controles"
type: lab
language: es
part: 21
lab: 1
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-19
---

# Lab 21.1 — Generación de contenido con controles

**Parte 21 · IA aplicada a marketing, ventas y servicio** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Ruta Andina publicó 40 artículos generados en un mes. Tres afirmaban compatibilidades inexistentes y uno prometía un plazo de implementación que la operación no cumple.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **operating model humano-IA con casos de uso, evaluaciones, guardrails y registro de incidentes**, aplicando en particular **generación de contenido con controles** y **lead scoring asistido por modelos**.

> **Pregunta que debe quedar respondida:** ¿Qué tarea mejora con IA, cómo sé que mejora y quién responde cuando falla?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-21-ia-aplicada-a-marketing-ventas-y-servicio/`](../../curriculum/part-21-ia-aplicada-a-marketing-ventas-y-servicio/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Definir qué tipos de contenido pueden generarse asistidamente.
2. Establecer el control de afirmaciones como paso obligatorio.
3. Asignar responsable humano de publicación.
4. Registrar el origen de cada pieza.
5. Auditar una muestra publicada cada mes.
6. Calcular o diseñar la captura de **piezas con control aplicado**, **afirmaciones corregidas en control** y **incidentes por contenido publicado**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Publicar contenido incorrecto a escala, tratar datos personales sin base legal y perder trazabilidad.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **piezas con control aplicado** | contenidos revisados antes de publicar, sobre contenidos publicados |
| **afirmaciones corregidas en control** | correcciones realizadas, sobre piezas revisadas |
| **incidentes por contenido publicado** | reclamos o correcciones posteriores, sobre piezas publicadas |
| **desempeño frente a la regla actual** | diferencia de precisión entre el modelo y la regla manual |
| **desempeño por segmento** | precisión del modelo, comparada entre segmentos |
| **deriva observada** | variación de la precisión del modelo entre periodos sucesivos |

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

- Publicar contenido generado sin control de afirmaciones. Instala la revisión como paso obligatorio y ajusta el volumen a la capacidad real de control.
- Desplegar el modelo sin revisar el sesgo por segmento. Compara el desempeño entre segmentos y corrige antes de usarlo para priorizar.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Ann Handley — *Everybody Writes* (2022, 2.ª ed.) — estándar editorial: claridad, utilidad y empatía en la escritura comercial.
- NIST — *AI Risk Management Framework 1.0* (2023) — gobernanza de riesgo de IA: mapear, medir, gestionar y gobernar.
- Cathy O'Neil — *Weapons of Math Destruction* (2016) — daños de los modelos opacos a escala y necesidad de auditoría.

---

[⬅ Laboratorios de la parte 21](./) · [Clases](../../curriculum/part-21-ia-aplicada-a-marketing-ventas-y-servicio/README.md) · [Evaluación](../../assessments/part-21-assessment.md)
