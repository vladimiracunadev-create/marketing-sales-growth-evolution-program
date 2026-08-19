# Lab 11.1 — Correo en frío

**Parte 11 · Prospección y generación de demanda** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** El correo estándar de Ruta Andina tiene 340 palabras, tres párrafos sobre la empresa y pide una reunión de 45 minutos. La respuesta es 0,4 %.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **sistema de prospección con listas, secuencias multicanal, mensajes y métricas por etapa**, aplicando en particular **correo en frío** y **networking**.

> **Pregunta que debe quedar respondida:** ¿De dónde vendrá la próxima oportunidad calificada y a qué costo por unidad?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-11-prospeccion-y-generacion-de-demanda/`](../../curriculum/part-11-prospeccion-y-generacion-de-demanda/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Identificar la señal y el problema probable.
2. Redactar asunto informativo y cuerpo breve.
3. Incluir evidencia mínima verificable.
4. Pedir un compromiso proporcional.
5. Medir respuesta y ajustar una variable por vez.
6. Calcular o diseñar la captura de **tasa de respuesta**, **tasa de respuesta positiva** y **tasa de solicitud de baja**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Infringir normas de datos personales y consumo, y quemar el activo reputacional del dominio.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **tasa de respuesta** | respuestas recibidas, sobre correos entregados, por secuencia |
| **tasa de respuesta positiva** | respuestas que aceptan el siguiente paso, sobre respuestas recibidas |
| **tasa de solicitud de baja** | solicitudes de no contacto, sobre correos entregados |
| **oportunidades originadas por red** | oportunidades calificadas atribuidas a relaciones, sobre oportunidades totales |
| **cumplimiento de compromisos informales** | compromisos cumplidos, sobre compromisos adquiridos en instancias de red |
| **participación en instancias del gremio** | eventos o espacios con participación efectiva, por trimestre |

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

- Pedir una reunión larga en el primer contacto. Solicita un compromiso mínimo: una respuesta de una línea o una pregunta concreta.
- Aparecer sólo cuando se necesita vender. Participa con regularidad y entrega aporte verificable antes de pedir cualquier cosa.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Jeb Blount — *Fanatical Prospecting* (2015) — disciplina de prospección, cadencia y gestión del rechazo.
- Ann Handley — *Everybody Writes* (2022, 2.ª ed.) — estándar editorial: claridad, utilidad y empatía en la escritura comercial.
- Trish Bertuzzi — *The Sales Development Playbook* (2016) — estructura, especialización y métricas del equipo de desarrollo de ventas.

---

[⬅ Laboratorios de la parte 11](./) · [Clases](../../curriculum/part-11-prospeccion-y-generacion-de-demanda/README.md) · [Evaluación](../../assessments/part-11-assessment.md)
