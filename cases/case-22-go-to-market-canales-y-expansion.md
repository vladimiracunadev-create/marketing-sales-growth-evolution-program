---
title: "Caso 22 — Go-to-market, canales y expansión"
type: case
language: es
part: 22
updated: 2026-08-19
---

# Caso 22 — Go-to-market, canales y expansión

## Contexto

Ruta Andina SpA — Empresa chilena que vende una plataforma de agendamiento, pagos y CRM ligero para pymes de servicios (peluquerías, talleres, centros médicos pequeños, estudios contables). Tiene tres líneas de ingreso: suscripción SaaS (CLP 39.000 a CLP 199.000 mensuales por local), venta de hardware complementario por e-commerce y marketplace, y contratos anuales con municipios y corporaciones para digitalizar atención de público.

**Estado de la empresa.** 18 meses de operación, 240 cuentas activas, ARR aproximado de CLP 610 millones, churn mensual de 3,4 %, equipo comercial de 6 personas, CAC mixto de CLP 310.000 y un CRM con datos incompletos. El directorio pide duplicar ingresos en 18 meses sin duplicar el gasto comercial.

**Restricciones.** Presupuesto de marketing y ventas acotado, un solo analista de datos compartido, obligación de cumplir la Ley 19.496 del consumidor y de prepararse para la Ley 21.719 de datos personales, y un competidor regional con más capital.

## Situación

Ruta Andina quiere entrar a Perú y, al mismo tiempo, lanzar un plan self-service y un programa de partners contables. El equipo es el mismo.

El equipo tiene tres semanas para presentar una recomendación al comité. Existen posiciones encontradas dentro de la empresa y la información disponible es incompleta en varios frentes.

## Datos disponibles

| Fuente | Contenido | Limitación conocida |
|---|---|---|
| `datasets/leads.csv` | Origen, estado y fecha de leads | Registro incompleto antes del último trimestre |
| `datasets/customers.csv` | Cuentas, plan, antigüedad y estado | Sin costo de servir por cuenta |
| `datasets/campaigns.csv` | Inversión y resultados por campaña | Atribución de último clic |
| `datasets/ecommerce_orders.csv` | Pedidos, montos y devoluciones | Sin costo logístico desagregado |
| `datasets/experiments.csv` | Pruebas ejecutadas y resultados | Varias sin tamaño de muestra registrado |

## Preguntas de análisis

1. ¿Cuál es el problema real y qué evidencia lo sostiene? Distingue síntoma de causa.
2. ¿Qué información falta y cuánto costaría obtenerla? ¿Vale la pena esperarla?
3. ¿Qué dos alternativas son realmente defendibles y qué sacrifica cada una?
4. ¿Qué señal permitiría saber, en 60 días, si la decisión fue correcta?
5. ¿Qué riesgo legal, ético o reputacional introduce la recomendación?

## Complicación (leer después del primer análisis)

A mitad del trabajo cambia una condición: el presupuesto disponible se reduce 30 %, un competidor anuncia una oferta más agresiva y el equipo pierde a una persona clave. Recalcula la recomendación y explica qué parte del razonamiento se mantiene y cuál cambia.

## Entregable

Un decision brief de dos páginas más anexos:

- hechos, inferencias y supuestos separados;
- dos alternativas con costo de oportunidad;
- recomendación con responsable, fecha y condición de revisión;
- verificación del riesgo: abrir frentes simultáneos sin capacidad, diluir foco y llegar tarde a todos.

## Método de discusión sugerido

1. Lectura individual y registro de la posición inicial (20 minutos).
2. Discusión en grupo con roles asignados: gerencia comercial, finanzas, operaciones y cliente.
3. Presentación de dos posiciones contrapuestas (10 minutos cada una).
4. Red team: el grupo intenta refutar la recomendación ganadora.
5. Cierre con registro de la decisión y de lo que la haría cambiar.

## Vínculo con el currículo

Este caso integra la parte 22 y en particular la clase 22.14 — Plan go-to-market completo. Su artefacto alimenta **plan GTM completo con beachhead, movimiento comercial, canales, economía y plan de lanzamiento**.

---

[⬅ Clases](../curriculum/part-22-go-to-market-canales-y-expansion/README.md) · [Laboratorios](../labs/part-22/) · [Evaluación](../assessments/part-22-assessment.md)
