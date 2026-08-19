# Notebooks

Ocho notebooks que reproducen los cálculos centrales del programa sobre los datos sintéticos. Están pensados
para ejecutarse y modificarse, no para leerse.

| Notebook | Qué calcula | Parte asociada |
|---|---|---|
| `01-funnel-metrics.ipynb` | Conversión por etapa, volumen y tiempo | 16, 20 |
| `02-campaign-economics.ipynb` | Costo por oportunidad, por cliente y retorno | 14, 20 |
| `03-customer-retention.ipynb` | Curvas de retención por cohorte | 18, 20 |
| `04-ecommerce-unit-economics.ipynb` | Contribución por pedido con costos completos | 15 |
| `05-ab-testing.ipynb` | Tamaño de muestra, potencia e interpretación | 19, 20 |
| `06-sales-velocity.ipynb` | Velocidad comercial y palanca dominante | 16 |
| `07-cohort-thinking.ipynb` | Matriz de cohortes y efecto de mezcla | 18, 20 |
| `08-executive-dashboard.ipynb` | Consolidación y coherencia aritmética | 20, 23 |

## Ejecución

```bash
python -m venv .venv
. .venv/bin/activate        # en Windows: .venv\Scripts\activate
pip install jupyter pandas matplotlib
jupyter notebook
```

Los notebooks no requieren conexión ni servicios externos: leen los archivos de
[`datasets/`](../datasets/).

## Regla del programa

Un cálculo sin definición operacional de sus términos no es evidencia. Antes de reportar cualquier resultado
de estos notebooks, completa la ficha de medición descrita en
[`docs/FORMULAS-Y-METRICAS.md`](../docs/FORMULAS-Y-METRICAS.md).

---

[⬅ Programa](../README.md) · [Conjuntos de datos](../datasets/README.md)
