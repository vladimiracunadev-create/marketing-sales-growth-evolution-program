# Lab 08.2 — Seguimiento

**Parte 08 · Fundamentos profesionales de ventas** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** El 44 % de las oportunidades de Ruta Andina no tiene actividad en 30 días y ninguna tiene siguiente paso agendado en el CRM.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **playbook comercial con etapas, criterios de salida, guiones y materiales**, aplicando en particular **seguimiento** y **disciplina de CRM**.

> **Pregunta que debe quedar respondida:** ¿Qué debe ocurrir en cada etapa para que la siguiente sea probable y no accidental?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-08-fundamentos-profesionales-de-ventas/`](../../curriculum/part-08-fundamentos-profesionales-de-ventas/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Acordar el siguiente paso y su fecha en cada interacción.
2. Definir el ritmo de seguimiento con el cliente.
3. Preparar un aporte concreto para cada contacto.
4. Registrar cada intento y su resultado.
5. Aplicar la regla de cierre cuando corresponda.
6. Calcular o diseñar la captura de **oportunidades con siguiente paso agendado**, **tasa de respuesta al seguimiento** y **edad media del pipeline**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Presionar por cierre sin diagnóstico y vender a clientes que no pueden obtener valor.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **oportunidades con siguiente paso agendado** | oportunidades abiertas con fecha comprometida, sobre oportunidades abiertas |
| **tasa de respuesta al seguimiento** | respuestas obtenidas, sobre contactos de seguimiento realizados |
| **edad media del pipeline** | días promedio desde la creación de las oportunidades abiertas |
| **completitud de campos críticos** | registros con todos los campos críticos completos, sobre registros creados |
| **oportunidad del registro** | interacciones registradas dentro del plazo definido, sobre interacciones registradas |
| **duplicados detectados** | registros duplicados, sobre registros totales de la base |

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

- Hacer seguimiento sin aporte. Prepara un dato, un caso o una respuesta concreta para cada contacto de seguimiento.
- Exigir registro sin devolver valor. Reduce los campos obligatorios al mínimo y entrega vistas que el vendedor use para trabajar.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Jeb Blount — *Fanatical Prospecting* (2015) — disciplina de prospección, cadencia y gestión del rechazo.
- Mike Weinberg — *New Sales. Simplified.* (2012) — proceso de nueva venta: lista objetivo, relato comercial y actividad sostenida.
- Mark Roberge — *The Sales Acceleration Formula* (2015) — contratación, formación, gestión y demanda comercial gobernadas por datos.

---

[⬅ Laboratorios de la parte 08](./) · [Clases](../../curriculum/part-08-fundamentos-profesionales-de-ventas/README.md) · [Evaluación](../../assessments/part-08-assessment.md)
