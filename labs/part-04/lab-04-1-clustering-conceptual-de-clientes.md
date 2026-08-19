# Lab 04.1 — Clustering conceptual de clientes

**Parte 04 · Segmentación, targeting y posicionamiento** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Un análisis entrega cinco clusters de clientes de Ruta Andina. Tres son indistinguibles en comportamiento comercial y ninguno puede describirse sin recurrir a coordenadas del modelo.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **arquitectura STP con criterios de atractivo, accesibilidad y declaración de posicionamiento probada**, aplicando en particular **clustering conceptual de clientes** y **estrategias de nicho**.

> **Pregunta que debe quedar respondida:** ¿Qué segmento puedo servir mejor que nadie y con qué diferencia comprobable?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-04-segmentacion-targeting-y-posicionamiento/`](../../curriculum/part-04-segmentacion-targeting-y-posicionamiento/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Elegir variables con justificación de negocio.
2. Normalizar escalas y documentar el criterio.
3. Generar agrupaciones y evaluar cohesión.
4. Describir cada grupo con una regla accionable.
5. Verificar estabilidad en un periodo distinto.
6. Calcular o diseñar la captura de **cohesión y separación**, **estabilidad entre periodos** y **diferencia de valor entre grupos**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Segmentar con variables decorativas que no cambian oferta, canal ni mensaje.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **cohesión y separación** | medida de distancia intragrupo frente a distancia entre grupos |
| **estabilidad entre periodos** | proporción de clientes que permanecen en el mismo grupo al repetir el análisis |
| **diferencia de valor entre grupos** | ingreso y retención promedio por grupo, con su dispersión |
| **participación dentro del nicho** | clientes del nicho atendidos, sobre universo estimado del nicho |
| **tasa de referencia interna** | oportunidades originadas por clientes del mismo nicho, sobre oportunidades del nicho |
| **costo de adquisición en nicho frente a mercado amplio** | comparación del costo por cliente ganado en ambos contextos |

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

- Aceptar grupos que no se pueden describir en lenguaje de negocio. Exige una regla verbal por grupo; si no existe, revisa las variables de entrada.
- Confundir nicho con público pequeño cualquiera. Verifica que el grupo tenga canales propios y circulación interna de referencias.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Foster Provost y Tom Fawcett — *Data Science for Business* (2013) — pensamiento analítico: formulación del problema, evaluación y valor esperado.
- Peter Fader — *Customer Centricity* (2020, 2.ª ed.) — valor heterogéneo del cliente y asignación de recursos por valor esperado.
- Alistair Croll y Benjamin Yoskovitz — *Lean Analytics* (2013) — una métrica que importa por etapa y por modelo de negocio.

---

[⬅ Laboratorios de la parte 04](./) · [Clases](../../curriculum/part-04-segmentacion-targeting-y-posicionamiento/README.md) · [Evaluación](../../assessments/part-04-assessment.md)
