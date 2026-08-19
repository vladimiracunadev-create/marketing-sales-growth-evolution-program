---
title: "Lab 17.1 — Enrutamiento de leads"
type: lab
language: es
part: 17
lab: 1
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-19
---

# Lab 17.1 — Enrutamiento de leads

**Parte 17 · Marketing automation y revenue operations** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** El 31 % de los leads entrantes de Ruta Andina nunca recibe contacto porque la regla de asignación depende de un campo que el formulario no captura.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **operating model de RevOps con lifecycle, scoring, SLA, integraciones y observabilidad**, aplicando en particular **enrutamiento de leads** y **acuerdo de servicio entre marketing y ventas**.

> **Pregunta que debe quedar respondida:** ¿Qué automatizo porque mejora el sistema y qué estaría solo escalando un desorden?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-17-marketing-automation-y-revenue-operations/`](../../curriculum/part-17-marketing-automation-y-revenue-operations/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Definir las reglas de asignación por segmento y territorio.
2. Medir el tiempo de asignación y de primer contacto.
3. Configurar escalamiento por falta de respuesta.
4. Auditar los contactos no asignados.
5. Revisar las reglas cuando cambia la estructura del equipo.
6. Calcular o diseñar la captura de **tiempo de asignación**, **leads sin asignar** y **escalamientos ejecutados**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Automatizar comunicaciones sin base de licitud ni control de calidad y multiplicar el daño.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **tiempo de asignación** | minutos entre creación y asignación, mediana |
| **leads sin asignar** | registros sin responsable en 24 horas, sobre registros creados |
| **escalamientos ejecutados** | escalamientos activados, sobre casos que cumplían la condición |
| **cumplimiento de volumen** | leads calificados entregados, sobre leads comprometidos |
| **cumplimiento de plazo de contacto** | leads contactados dentro del plazo, sobre leads entregados |
| **retroalimentación devuelta** | leads con evaluación de ventas registrada, sobre leads entregados |

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

- Configurar reglas que dependen de datos no capturados. Verifica que cada condición de enrutamiento use un campo efectivamente registrado.
- Operar sin definición compartida de lead calificado. Acuerda la definición con ejemplos concretos y mide el cumplimiento de ambas partes.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Mark Roberge — *The Sales Acceleration Formula* (2015) — contratación, formación, gestión y demanda comercial gobernadas por datos.
- Stephen G. Diorio y Chris K. Hummel — *Revenue Operations* (2022) — integración de datos, procesos y equipos que producen ingreso como un solo sistema.
- Aaron Ross y Marylou Tyler — *Predictable Revenue* (2011) — especialización de roles comerciales y generación de pipeline predecible.

---

[⬅ Laboratorios de la parte 17](./) · [Clases](../../curriculum/part-17-marketing-automation-y-revenue-operations/README.md) · [Evaluación](../../assessments/part-17-assessment.md)
