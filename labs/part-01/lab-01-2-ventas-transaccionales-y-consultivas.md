---
title: "Lab 01.2 — Ventas transaccionales y consultivas"
type: lab
language: es
part: 01
lab: 2
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-19
---

# Lab 01.2 — Ventas transaccionales y consultivas

**Parte 01 · Marketing y ventas: fundamentos del sistema comercial** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Ruta Andina atiende con el mismo proceso de cinco reuniones a un cliente de CLP 39.000 mensuales y a una cadena de CLP 2,4 millones anuales. El primero consume más costo comercial del que aportará en dos años.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **mapa del sistema comercial con supuestos, métricas y puntos de fuga**, aplicando en particular **ventas transaccionales y consultivas** y **ética comercial y confianza**.

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

1. Clasificar el negocio por valor del contrato y complejidad de decisión.
2. Calcular el costo de adquisición admisible para ese ticket.
3. Elegir el modelo de venta que cabe dentro de ese costo.
4. Diseñar el proceso mínimo suficiente para ese modelo.
5. Revisar la clasificación cuando cambian ticket o ciclo.
6. Calcular o diseñar la captura de **costo de venta sobre valor del contrato**, **ciclo mediano por modelo** y **tasa de descuento por modelo**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Confundir actividad con resultado y comprometer presupuesto antes de tener un diagnóstico.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **costo de venta sobre valor del contrato** | horas comerciales valorizadas más gastos directos dividido por el valor del primer año del contrato |
| **ciclo mediano por modelo** | días entre oportunidad calificada y cierre, mediana separada por modelo transaccional y consultivo |
| **tasa de descuento por modelo** | descuento promedio ponderado por ingreso, comparado entre ambos modelos |
| **tasa de reclamos por información** | reclamos vinculados a publicidad, precio o condiciones, sobre transacciones del periodo |
| **promesas sin respaldo documentado** | afirmaciones comerciales activas sin evidencia asociada, sobre total auditado |
| **bajas por expectativa incumplida** | bajas cuyo motivo declarado es diferencia entre lo prometido y lo recibido, sobre bajas totales |

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

- Atender todo con el proceso más caro. Define umbrales de ticket y complejidad que determinan qué proceso se aplica, y audítalos cada trimestre.
- Tratar el cumplimiento como revisión final. Incorpora la verificación de promesa y de datos en el diseño de la campaña, no en la aprobación.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Neil Rackham — *SPIN Selling* (1988) — investigación conductual sobre venta compleja: situación, problema, implicación y necesidad-beneficio.
- Mark Roberge — *The Sales Acceleration Formula* (2015) — contratación, formación, gestión y demanda comercial gobernadas por datos.
- Keenan — *Gap Selling* (2018) — vender la brecha entre estado actual y estado futuro con diagnóstico riguroso.

---

[⬅ Laboratorios de la parte 01](./) · [Clases](../../curriculum/part-01-marketing-y-ventas-fundamentos-del-sistema-comercial/README.md) · [Evaluación](../../assessments/part-01-assessment.md)
