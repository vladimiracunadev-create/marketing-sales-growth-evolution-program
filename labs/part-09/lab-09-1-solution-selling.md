---
title: "Lab 09.1 — Solution Selling"
type: lab
language: es
part: 09
lab: 1
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-18
---

# Lab 09.1 — Solution Selling

**Parte 09 · Venta consultiva y B2B compleja** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Una cadena pidió a Ruta Andina «un sistema de turnos con pantalla». El problema real era la percepción de espera, que se resolvía con confirmación previa y no con hardware.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **deal review completo con mapa de cuenta, criterios de decisión y plan mutuo**, aplicando en particular **solution Selling** y **comité de compra**.

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

1. Documentar el estado actual con datos verificables.
2. Definir el estado futuro en métricas del cliente.
3. Cuantificar la brecha y su valor.
4. Cuestionar los requerimientos formulados como solución.
5. Comprometer sólo lo que la operación puede sostener.
6. Calcular o diseñar la captura de **brecha cuantificada por negocio**, **cumplimiento del estado futuro** y **requerimientos reformulados**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Confundir entusiasmo de un contacto con avance real y sostener un forecast falso.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **brecha cuantificada por negocio** | oportunidades con brecha estimada en cifras del cliente, sobre oportunidades calificadas |
| **cumplimiento del estado futuro** | clientes que alcanzaron la métrica comprometida, sobre clientes implementados |
| **requerimientos reformulados** | casos donde el requerimiento inicial fue reformulado, sobre licitaciones y pedidos recibidos |
| **cobertura del comité** | miembros con contacto o evidencia de postura, sobre miembros identificados |
| **negocios detenidos por bloqueador** | oportunidades detenidas por un actor específico, sobre oportunidades estancadas |
| **tiempo de decisión por tamaño de comité** | días hasta la decisión, segmentados por número de participantes |

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

- Responder al requerimiento sin cuestionar su formulación. Reconstruye el problema detrás del pedido antes de cotizar la solución solicitada.
- Trabajar sólo con el contacto más accesible. Planifica el acceso a cada rol crítico y registra la evidencia de su postura.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Keenan — *Gap Selling* (2018) — vender la brecha entre estado actual y estado futuro con diagnóstico riguroso.
- Neil Rackham — *SPIN Selling* (1988) — investigación conductual sobre venta compleja: situación, problema, implicación y necesidad-beneficio.
- Matthew Dixon y Brent Adamson — *The Challenger Sale* (2011) — enseñar, adaptar y tomar el control; el insight comercial como diferenciador.

---

[⬅ Laboratorios de la parte 09](./) · [Clases](../../curriculum/part-09-venta-consultiva-y-b2b-compleja/README.md) · [Evaluación](../../assessments/part-09-assessment.md)
