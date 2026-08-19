# Lab 02.2 — Riesgo percibido y confianza

**Parte 02 · Cliente y comportamiento del consumidor** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Los clientes de Ruta Andina temen perder el historial de citas al migrar. La empresa nunca documentó su proceso de migración ni ofreció rollback, y esa ausencia explica un tercio de las pérdidas.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **expediente de cliente con ICP, unidad de decisión, journey y fricciones priorizadas**, aplicando en particular **riesgo percibido y confianza** y **segmentos conductuales**.

> **Pregunta que debe quedar respondida:** ¿Quién decide, quién usa, quién paga y qué progreso intenta lograr cada uno?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-02-cliente-y-comportamiento-del-consumidor/`](../../curriculum/part-02-cliente-y-comportamiento-del-consumidor/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Enumerar los riesgos percibidos por cada rol.
2. Clasificarlos en económico, operativo, reputacional y personal.
3. Asignar a cada riesgo una señal de confianza verificable.
4. Aumentar la reversibilidad donde el riesgo es alto.
5. Medir el efecto sobre avance y sobre calidad del cliente ganado.
6. Calcular o diseñar la captura de **objeciones de riesgo por negocio**, **uso de referencias en negocios ganados** y **tasa de conversión con garantía**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Construir personas ficticias sin datos y usarlas para justificar decisiones caras.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **objeciones de riesgo por negocio** | objeciones clasificadas como riesgo, sobre objeciones totales registradas en el periodo |
| **uso de referencias en negocios ganados** | negocios donde se entregó una referencia verificable, sobre negocios cerrados |
| **tasa de conversión con garantía** | conversión de la oferta con garantía explícita frente a la oferta sin garantía |
| **tamaño y estabilidad del segmento** | clientes en el segmento y porcentaje que permanece en él entre dos periodos consecutivos |
| **diferencial de respuesta** | diferencia de conversión o retención entre segmentos ante el mismo tratamiento |
| **valor promedio por segmento** | ingreso y margen promedio por cliente en cada segmento conductual |

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

- Responder al riesgo con más argumentos de beneficio. Atiende el riesgo con evidencia y reversibilidad, no con entusiasmo adicional.
- Crear segmentos que no se pueden alcanzar. Verifica que exista un canal y un dato de contacto para tratar al segmento de forma distinta.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Robert B. Cialdini — *Influence: The Psychology of Persuasion, New and Expanded* (2021) — principios de influencia y su uso ético en contextos comerciales.
- Neil Rackham — *SPIN Selling* (1988) — investigación conductual sobre venta compleja: situación, problema, implicación y necesidad-beneficio.
- Matthew Dixon, Nick Toman y Rick DeLisi — *The Effortless Experience* (2013) — reducción del esfuerzo del cliente como motor de lealtad frente al deleite.

---

[⬅ Laboratorios de la parte 02](./) · [Clases](../../curriculum/part-02-cliente-y-comportamiento-del-consumidor/README.md) · [Evaluación](../../assessments/part-02-assessment.md)
