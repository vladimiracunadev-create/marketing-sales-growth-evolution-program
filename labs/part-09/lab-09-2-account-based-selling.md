---
title: "Lab 09.2 — Account-based selling"
type: lab
language: es
part: 09
lab: 2
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-18
---

# Lab 09.2 — Account-based selling

**Parte 09 · Venta consultiva y B2B compleja** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Ruta Andina identificó 12 cadenas que representan el 40 % del potencial de su región. Hoy las trata igual que a los 900 talleres de su base de correos.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **deal review completo con mapa de cuenta, criterios de decisión y plan mutuo**, aplicando en particular **account-based selling** y **negocios enterprise**.

> **Pregunta que debe quedar respondida:** ¿Quién decide, quién bloquea, qué evidencia necesita cada uno y cuál es el costo de no decidir?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-09-venta-consultiva-y-b2b-compleja/`](../../curriculum/part-09-venta-consultiva-y-b2b-compleja/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Seleccionar cuentas por potencial y ajuste con criterios escritos.
2. Construir un plan por cuenta con actores y mensajes.
3. Coordinar acciones de marketing y ventas sobre la misma lista.
4. Medir penetración y avance por cuenta.
5. Revisar la lista con datos de resultado cada trimestre.
6. Calcular o diseñar la captura de **penetración por cuenta**, **avance de cuentas objetivo** y **costo por cuenta objetivo**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Confundir entusiasmo de un contacto con avance real y sostener un forecast falso.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **penetración por cuenta** | contactos activos en la cuenta, sobre roles críticos identificados |
| **avance de cuentas objetivo** | cuentas que avanzaron de etapa, sobre cuentas objetivo del periodo |
| **costo por cuenta objetivo** | inversión total de marketing y ventas asignada, dividido por cuentas trabajadas |
| **cumplimiento de hitos del plan mutuo** | hitos cumplidos en fecha, sobre hitos acordados |
| **costo de servir de la cuenta** | horas y gastos atribuibles a la cuenta, sobre su ingreso |
| **concentración de ingreso** | ingreso de la mayor cuenta, sobre ingreso total de la empresa |

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

- Declarar cuentas objetivo sin plan ni recursos asignados. Limita la lista a lo que el equipo puede trabajar y exige plan escrito por cuenta.
- Firmar sin costear los requisitos de servicio. Calcula el costo de cumplir los niveles de servicio exigidos antes de comprometer el contrato.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Robert B. Miller y Stephen E. Heiman — *The New Strategic Selling* (2005) — mapa de influencias, roles de compra y análisis de posición en cuentas complejas.
- Aaron Ross y Marylou Tyler — *Predictable Revenue* (2011) — especialización de roles comerciales y generación de pipeline predecible.
- Brent Adamson y Matthew Dixon — *The Challenger Customer* (2015) — comité de compra, mobilizer y construcción de consenso interno del cliente.

---

[⬅ Laboratorios de la parte 09](./) · [Clases](../../curriculum/part-09-venta-consultiva-y-b2b-compleja/README.md) · [Evaluación](../../assessments/part-09-assessment.md)
