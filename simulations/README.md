# Simulación persistente — Ruta Andina SpA

El programa completo trabaja sobre una empresa simulada. No es un ejemplo distinto por clase: es la misma
operación, con el mismo estado, atravesando las 24 partes. Esa continuidad es lo que hace posible la
acumulación: una decisión de pricing tomada en la parte 07 restringe lo posible en la parte 22.

## La empresa

**Ruta Andina SpA** vende una plataforma de agendamiento, pagos y CRM ligero a pymes de servicios en Chile
—peluquerías, talleres mecánicos, centros médicos pequeños y estudios contables—. Tiene tres líneas de
ingreso:

| Línea | Modelo | Ticket |
|---|---|---|
| Suscripción SaaS | Recurrente mensual por local | CLP 39.000 a 199.000 |
| Hardware complementario | Venta única por tienda propia y marketplace | CLP 39.900 a 189.900 |
| Contratos con sector público | Anual, con licitación | CLP 4 a 18 millones |

Esa combinación permite recorrer venta B2B recurrente, comercio electrónico, marketplace y venta al Estado
sin cambiar de contexto.

## Estado inicial

| Dimensión | Valor |
|---|---|
| Meses de operación | 18 |
| Cuentas activas | 240 |
| Ingreso recurrente anual | CLP 610 millones |
| Churn mensual de cuentas | 3,4 % |
| Churn mensual de ingreso | 5,1 % |
| Ingreso neto retenido | 84 % |
| Oportunidades abiertas | 380 (167 sin actividad en 30 días) |
| Costo de adquisición reportado | CLP 310.000 |
| Costo de adquisición con alcance completo | CLP 705.000 estimado |
| Periodo de recuperación | 14 meses |
| Vida media del cliente | 11 meses |
| Equipo comercial | 3 ejecutivos, 2 SDR, 1 customer success |
| Ciclo mediano | 71 días |
| Activación a 14 días | 22 % |

El dato incómodo está a la vista: **el periodo de recuperación supera la vida media del cliente**. Cada
cliente nuevo destruye caja antes de aportar. Ese es el problema que el programa enseña a diagnosticar antes
de invertir en más adquisición.

## Restricciones vigentes

- Un solo analista de datos, compartido con finanzas.
- Competidor regional con capital de riesgo y precio 30 % menor.
- Obligación de cumplir la Ley 19.496 y de prepararse para la Ley 21.719.
- El directorio pide duplicar ingresos en 18 meses sin duplicar el gasto comercial.

## Deuda operativa acumulada

- Tres definiciones distintas de «propuesta enviada» en el CRM.
- 31 % de la base de contactos con rebote.
- Migración de datos entregada sin cobro en el 40 % de los proyectos.
- Integración entre CRM y facturación sin monitoreo.

## Cómo se usa el estado

1. Cada proyecto integrador actualiza `state/initial-state.json` con las decisiones tomadas.
2. Las decisiones se registran en `decisiones_tomadas` con fecha, responsable y supuesto.
3. Los efectos observados se anotan en `historial`.
4. Las partes siguientes parten del estado actualizado, no del inicial.

Formato de una decisión registrada:

```json
{
  "parte": "07",
  "fecha": "2026-09-15",
  "decision": "Cambiar la métrica de cobro de local a profesional activo",
  "supuesto_critico": "Las cadenas tienen más locales que profesionales por local",
  "efecto_esperado": "Aumento de 18 % en ARPA de cuentas multi-local",
  "condicion_de_revision": "Si la conversión cae más de 5 puntos en 60 días, revertir"
}
```

## Reemplazar la simulación por una empresa propia

Es válido y recomendable si trabajas en una operación real. Dos condiciones:

1. El caso propio debe tener restricciones reales: presupuesto acotado, información incompleta, competencia.
2. Debe mantenerse la acumulación: las decisiones de una parte condicionan las siguientes.

Si usas datos reales, revisa antes [`docs/DATOS-PERSONALES-Y-ETICA.md`](../docs/DATOS-PERSONALES-Y-ETICA.md)
y no los subas a este repositorio.

## Advertencia

Los datos de esta simulación son **sintéticos**. Sirven para razonar y calcular, no para inferir el estado
real de ningún mercado ni de ninguna empresa.

---

[⬅ Programa](../README.md) · [Conjuntos de datos](../datasets/README.md)
