---
title: "Lab 10.2 — Negociar con compras y procurement"
type: lab
language: es
part: 10
lab: 2
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-18
---

# Lab 10.2 — Negociar con compras y procurement

**Parte 10 · Negociación comercial** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Compras de la cadena pide igualar la oferta del competidor. La jefa de operaciones sabe que esa oferta no incluye migración ni soporte en terreno, pero no fue invitada a la reunión.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **carpeta de negociación con BATNA, ZOPA, concesiones planificadas y acuerdo documentado**, aplicando en particular **negociar con compras y procurement** y **cierre y documentación**.

> **Pregunta que debe quedar respondida:** ¿Qué intereses hay detrás de las posiciones y cuál es mi alternativa real si no hay acuerdo?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-10-negociacion-comercial/`](../../curriculum/part-10-negociacion-comercial/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Alinear al área usuaria antes de la intervención de compras.
2. Documentar el costo total y los diferenciales.
3. Preparar el paquete de contrapartidas.
4. Responder a la comparabilidad forzada con criterios objetivos.
5. Cerrar con acuerdo escrito y condiciones claras.
6. Calcular o diseñar la captura de **diferencia de margen con y sin intervención de compras**, **respaldo del área usuaria** y **contrapartidas obtenidas**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Ceder margen y condiciones bajo presión de cierre de trimestre y crear precedente.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **diferencia de margen con y sin intervención de compras** | margen promedio de negocios con compras frente a los sin compras |
| **respaldo del área usuaria** | negociaciones con participación activa del usuario, sobre negociaciones con compras |
| **contrapartidas obtenidas** | valor de las contrapartidas conseguidas, sobre el valor de las concesiones otorgadas |
| **acuerdos con resumen enviado** | acuerdos con resumen dentro de 24 horas, sobre acuerdos alcanzados |
| **tasa de confirmación bilateral** | resúmenes confirmados por la contraparte, sobre resúmenes enviados |
| **conflictos por interpretación** | disputas sobre lo acordado, sobre contratos vigentes |

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

- Negociar con compras sin respaldo del área usuaria. Alinea al usuario antes y solicita su participación en la conversación de condiciones.
- Cerrar sin resumen escrito confirmado. Envía el resumen dentro de 24 horas y solicita confirmación explícita antes de iniciar la ejecución.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Deepak Malhotra y Max H. Bazerman — *Negotiation Genius* (2007) — preparación analítica, ZOPA, valor creado frente a valor reclamado y ética negociadora.
- Roger Fisher, William Ury y Bruce Patton — *Getting to Yes* (2011, 3.ª ed.) — negociación por principios: intereses, opciones, criterios objetivos y BATNA.
- G. Richard Shell — *Bargaining for Advantage* (2006) — estilos de negociación, autoridad y estándares de legitimidad.

---

[⬅ Laboratorios de la parte 10](./) · [Clases](../../curriculum/part-10-negociacion-comercial/README.md) · [Evaluación](../../assessments/part-10-assessment.md)
