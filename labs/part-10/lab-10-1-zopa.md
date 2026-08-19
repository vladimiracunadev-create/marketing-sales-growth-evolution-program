# Lab 10.1 — ZOPA

**Parte 10 · Negociación comercial** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** La cadena tiene un techo presupuestario de CLP 1,2 millones mensuales y el costo de servir de Ruta Andina a 14 locales es CLP 1,4 millones. No hay zona con el alcance actual.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **carpeta de negociación con BATNA, ZOPA, concesiones planificadas y acuerdo documentado**, aplicando en particular **ZOPA** y **negociación de precio**.

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

1. Definir el valor de reserva propio.
2. Estimar el de la contraparte con evidencia disponible.
3. Verificar si existe superposición.
4. Si no existe, modificar alcance, plazo o condiciones.
5. Cerrar dentro de la zona y documentar los supuestos.
6. Calcular o diseñar la captura de **negociaciones sin zona identificada**, **tiempo hasta detectar ausencia de zona** y **acuerdos con alcance modificado**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Ceder margen y condiciones bajo presión de cierre de trimestre y crear precedente.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **negociaciones sin zona identificada** | negociaciones abandonadas por ausencia de zona, sobre negociaciones iniciadas |
| **tiempo hasta detectar ausencia de zona** | días entre el inicio de la negociación y la conclusión de que no hay acuerdo posible |
| **acuerdos con alcance modificado** | acuerdos cerrados tras modificar alcance o condiciones, sobre acuerdos cerrados |
| **descuento promedio por segmento** | diferencia entre precio de lista y efectivo, ponderada por ingreso |
| **uso de la palanca de alcance** | negociaciones resueltas con ajuste de alcance, sobre negociaciones con presión de precio |
| **margen conservado** | margen de contribución de los negocios negociados, frente al margen estándar |

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

- Insistir en una negociación sin zona posible. Verifica temprano la superposición y, si no existe, propone modificar el alcance en lugar de bajar el precio.
- Negociar precio antes de establecer valor. Posterga la conversación de precio hasta tener el costo del problema cuantificado por el cliente.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Deepak Malhotra y Max H. Bazerman — *Negotiation Genius* (2007) — preparación analítica, ZOPA, valor creado frente a valor reclamado y ética negociadora.
- Roger Fisher, William Ury y Bruce Patton — *Getting to Yes* (2011, 3.ª ed.) — negociación por principios: intereses, opciones, criterios objetivos y BATNA.
- G. Richard Shell — *Bargaining for Advantage* (2006) — estilos de negociación, autoridad y estándares de legitimidad.

---

[⬅ Laboratorios de la parte 10](./) · [Clases](../../curriculum/part-10-negociacion-comercial/README.md) · [Evaluación](../../assessments/part-10-assessment.md)
