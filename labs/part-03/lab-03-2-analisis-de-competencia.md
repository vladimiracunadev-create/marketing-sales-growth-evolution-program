# Lab 03.2 — Análisis de competencia

**Parte 03 · Investigación de mercados e inteligencia competitiva** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** El competidor regional de Ruta Andina levantó capital y bajó precios 30 %. La reacción propuesta es igualar el precio, sin considerar que el competidor puede sostener pérdidas y Ruta Andina no.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **informe de oportunidad de mercado con método, muestra, límites y decisión recomendada**, aplicando en particular **análisis de competencia** y **validación de hipótesis comerciales**.

> **Pregunta que debe quedar respondida:** ¿Qué evidencia mínima necesito para decidir, y qué sesgo podría estar produciéndola?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-03-investigacion-de-mercados-e-inteligencia-competitiva/`](../../curriculum/part-03-investigacion-de-mercados-e-inteligencia-competitiva/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Reconstruir el modelo económico de los dos competidores principales.
2. Identificar sus restricciones observables.
3. Anticipar sus movimientos probables en 12 meses.
4. Evaluar el efecto de esos movimientos sobre el margen propio.
5. Definir la respuesta y su condición de activación.
6. Calcular o diseñar la captura de **participación en negocios enfrentados**, **cambios de precio del competidor** y **velocidad de respuesta**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Investigar para confirmar una decisión ya tomada y presentar el resultado como hallazgo.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **participación en negocios enfrentados** | negocios ganados frente a cada competidor, sobre negocios donde estuvo presente |
| **cambios de precio del competidor** | variaciones de lista detectadas por trimestre y su efecto en la tasa de descuento propia |
| **velocidad de respuesta** | días entre un movimiento del competidor y la respuesta documentada de la empresa |
| **hipótesis con criterio previo** | hipótesis con criterio de refutación escrito antes de la prueba, sobre hipótesis probadas |
| **tasa de refutación** | hipótesis refutadas, sobre hipótesis probadas en el periodo |
| **costo por aprendizaje** | costo total de las pruebas dividido por número de aprendizajes documentados |

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

- Reaccionar a un precio sin comparar estructuras de costo. Modela cuánto tiempo puede sostener cada parte esa política antes de responder.
- Cambiar el criterio de éxito después de ver el resultado. Registra el criterio en un documento fechado antes de iniciar la prueba.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Michael E. Porter — *Competitive Strategy* (1980) — estructura de industria, fuerzas competitivas y elección de una posición defendible.
- Richard Rumelt — *Good Strategy / Bad Strategy* (2011) — diagnóstico, política rectora y acción coherente frente a la estrategia decorativa.
- W. Chan Kim y Renée Mauborgne — *Blue Ocean Strategy* (2015, ed. ampliada) — reconstrucción de las fronteras del mercado y curva de valor.

---

[⬅ Laboratorios de la parte 03](./) · [Clases](../../curriculum/part-03-investigacion-de-mercados-e-inteligencia-competitiva/README.md) · [Evaluación](../../assessments/part-03-assessment.md)
