# Lab 11.2 — Lead magnets

**Parte 11 · Prospección y generación de demanda** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** El ebook «Tendencias digitales 2026» de Ruta Andina genera 300 descargas mensuales y 2 % de leads en perfil. Una calculadora de costo de inasistencias generó 40 descargas y 55 % en perfil.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **sistema de prospección con listas, secuencias multicanal, mensajes y métricas por etapa**, aplicando en particular **lead magnets** y **secuencias multicanal**.

> **Pregunta que debe quedar respondida:** ¿De dónde vendrá la próxima oportunidad calificada y a qué costo por unidad?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-11-prospeccion-y-generacion-de-demanda/`](../../curriculum/part-11-prospeccion-y-generacion-de-demanda/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Elegir un problema específico del perfil objetivo.
2. Construir un recurso útil por sí mismo.
3. Solicitar sólo los datos necesarios.
4. Informar con claridad el uso posterior.
5. Medir calidad del lead y no sólo volumen.
6. Calcular o diseñar la captura de **tasa de conversión del recurso**, **calidad del lead por recurso** y **conversión a oportunidad**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Infringir normas de datos personales y consumo, y quemar el activo reputacional del dominio.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **tasa de conversión del recurso** | descargas o registros, sobre visitas a la página del recurso |
| **calidad del lead por recurso** | leads que cumplen criterios de perfil, sobre leads capturados por ese recurso |
| **conversión a oportunidad** | oportunidades calificadas, sobre leads capturados por el recurso |
| **respuesta por paso de la secuencia** | respuestas obtenidas en cada paso, sobre contactos entregados en ese paso |
| **tasa de salida por solicitud** | solicitudes de no contacto, sobre contactos de la secuencia |
| **costo por reunión agendada** | horas y gastos de la secuencia, dividido por reuniones agendadas |

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

- Priorizar volumen de descargas sobre calidad. Mide leads en perfil y conversión a oportunidad, no descargas totales.
- Repetir el mismo mensaje en varios canales. Asigna un aporte distinto a cada paso y define condiciones de salida explícitas.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Seth Godin — *This Is Marketing* (2018) — marketing como servicio a un público mínimo viable y construcción de confianza.
- Ann Handley — *Everybody Writes* (2022, 2.ª ed.) — estándar editorial: claridad, utilidad y empatía en la escritura comercial.
- Joe Pulizzi — *Content Inc.* (2021, 2.ª ed.) — construcción de audiencia propia antes de monetizar y modelo editorial sostenido.

---

[⬅ Laboratorios de la parte 11](./) · [Clases](../../curriculum/part-11-prospeccion-y-generacion-de-demanda/README.md) · [Evaluación](../../assessments/part-11-assessment.md)
