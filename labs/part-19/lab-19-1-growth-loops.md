# Lab 19.1 — Growth loops

**Parte 19 · Growth marketing y growth engineering** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Cada cliente de Ruta Andina envía recordatorios de cita a sus propios clientes finales. Ese mensaje podría incluir una referencia visible y convertirse en un bucle.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **growth model con North Star, bucles, backlog priorizado y resultados de experimentos**, aplicando en particular **growth loops** y **bucles de referencia**.

> **Pregunta que debe quedar respondida:** ¿Qué bucle hace que el crecimiento se retroalimente en lugar de depender del gasto?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-19-growth-marketing-y-growth-engineering/`](../../curriculum/part-19-growth-marketing-y-growth-engineering/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Identificar qué produce el usuario al usar el producto.
2. Evaluar si ese output puede atraer a otros.
3. Diseñar el mecanismo que cierra el bucle.
4. Medir velocidad y factor de amplificación.
5. Decidir si conviene invertir en el bucle o en canales directos.
6. Calcular o diseñar la captura de **factor de amplificación**, **velocidad del bucle** y **proporción de adquisición por bucle**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Declarar victorias con muestras insuficientes y optimizar métricas locales que dañan el sistema.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **factor de amplificación** | nuevos usuarios generados por usuario existente, por ciclo |
| **velocidad del bucle** | días entre la incorporación de un usuario y la del usuario que trae, mediana por cohorte |
| **proporción de adquisición por bucle** | usuarios originados por el bucle, sobre usuarios nuevos totales |
| **tasa de participación** | clientes que refieren al menos una vez, sobre clientes elegibles |
| **calidad del referido** | referidos que cumplen el perfil objetivo, sobre referidos recibidos |
| **retención de clientes referidos** | retención a 12 meses de referidos frente a clientes de otros orígenes |

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

- Forzar un bucle donde el producto no lo permite. Verifica que exista un output visible para terceros antes de invertir en el mecanismo.
- Invitar a referir antes de que el cliente obtenga valor. Condiciona la invitación al resultado acreditado y mide la calidad del referido.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Sean Ellis y Morgan Brown — *Hacking Growth* (2017) — equipo multifuncional, ciclo de experimentación y aha moment.
- Wes Bush — *Product-Led Growth* (2019) — el producto como principal vehículo de adquisición, activación y expansión.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — una métrica que importa por etapa y por modelo de negocio.

---

[⬅ Laboratorios de la parte 19](./) · [Clases](../../curriculum/part-19-growth-marketing-y-growth-engineering/README.md) · [Evaluación](../../assessments/part-19-assessment.md)
