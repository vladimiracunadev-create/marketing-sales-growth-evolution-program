---
title: "Lab 22.1 — Crecimiento liderado por ventas"
type: lab
language: es
part: 22
lab: 1
mastery_threshold: 80
estimated_minutes: 240
updated: 2026-08-18
---

# Lab 22.1 — Crecimiento liderado por ventas

**Parte 22 · Go-to-market, canales y expansión** · Duración estimada: 4 horas · Aprobación: 80/100

## Escenario

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Situación específica del laboratorio.** Cada vendedor de Ruta Andina cuesta CLP 24 millones anuales y genera CLP 41 millones de ingreso nuevo. La rampa es de siete meses y nadie la consideró en el plan de contratación.

**Restricciones vigentes.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Misión

Producir un componente defendible de **plan GTM completo con beachhead, movimiento comercial, canales, economía y plan de lanzamiento**, aplicando en particular **crecimiento liderado por ventas** y **canales directos e indirectos**.

> **Pregunta que debe quedar respondida:** ¿Qué movimiento comercial corresponde al valor del contrato, al ciclo y al comprador?

## Insumos

| Insumo | Ruta | Uso |
|---|---|---|
| Clases de la parte | [`curriculum/part-22-go-to-market-canales-y-expansion/`](../../curriculum/part-22-go-to-market-canales-y-expansion/) | Marco conceptual y método |
| Datos sintéticos | [`datasets/`](../../datasets/) | Base cuantitativa reproducible |
| Plantillas | [`templates/`](../../templates/) | Formatos de artefacto |
| Notebooks | [`notebooks/`](../../notebooks/) | Cálculo y verificación |
| Estado de la simulación | [`simulations/state/`](../../simulations/state/) | Continuidad entre partes |
| Fuentes oficiales | [`docs/FUENTES-OFICIALES.md`](../../docs/FUENTES-OFICIALES.md) | Validación normativa |

## Procedimiento

1. Calcular el costo total por vendedor.
2. Medir la productividad actual por persona.
3. Determinar el umbral de ticket viable.
4. Estimar la latencia de escalamiento.
5. Decidir el crecimiento del equipo con esos datos.
6. Calcular o diseñar la captura de **productividad por vendedor**, **relación productividad-costo** y **duración de la rampa**.
7. Construir un escenario adverso: −30 % de presupuesto, −20 % de conversión o +25 % de duración del ciclo.
8. Verificar el riesgo declarado de la parte: Abrir frentes simultáneos sin capacidad, diluir foco y llegar tarde a todos.
9. Redactar la recomendación con responsable, fecha, umbral de éxito y condición de detención.

## Fichas de medición obligatorias

| Señal | Definición operacional |
|---|---|
| **productividad por vendedor** | ingreso nuevo generado, por vendedor y por año |
| **relación productividad-costo** | ingreso generado, sobre costo total del vendedor |
| **duración de la rampa** | meses hasta alcanzar la productividad objetivo, por incorporación |
| **margen por canal** | margen de contribución, sobre ingreso, por canal |
| **conflictos registrados** | disputas de cuenta, sobre cuentas trabajadas por ambos canales |
| **visibilidad del cliente final** | clientes con datos de contacto y uso disponibles, sobre clientes del canal |

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

- Planificar contrataciones sin considerar la rampa. Incorpora la duración de la rampa y la rotación esperada al proyectar capacidad.
- Operar canales mixtos sin reglas de conflicto. Escribe el criterio de asignación de cuentas y el mecanismo de registro antes de activar el canal indirecto.
- Presentar métricas sin numerador, denominador y ventana.
- Omitir el escenario adverso o presentarlo sin recálculo.
- Usar datos personales sin verificar base de licitud y finalidad.

## Fuentes de apoyo

- Aaron Ross y Marylou Tyler — *Predictable Revenue* (2011) — especialización de roles comerciales y generación de pipeline predecible.
- Mark Roberge — *The Sales Acceleration Formula* (2015) — contratación, formación, gestión y demanda comercial gobernadas por datos.
- Andris A. Zoltners, Prabhakant Sinha y Sally E. Lorimer — *The Complete Guide to Sales Force Incentive Compensation* (2006) — diseño de cuotas, territorios e incentivos sin efectos perversos.

---

[⬅ Laboratorios de la parte 22](./) · [Clases](../../curriculum/part-22-go-to-market-canales-y-expansion/README.md) · [Evaluación](../../assessments/part-22-assessment.md)
