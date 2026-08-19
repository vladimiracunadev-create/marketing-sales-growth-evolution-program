# Conjuntos de datos

Cinco conjuntos sintéticos que sostienen los cálculos del programa. **No contienen datos de personas ni de
empresas reales**: se generaron para que los ejercicios sean reproducibles sin comprometer a nadie.

## Contenido

| Archivo | Qué representa | Uso principal |
|---|---|---|
| `leads.csv` | Leads con origen, estado, fecha y calificación | Partes 11, 12, 16, 17 |
| `customers.csv` | Cuentas con plan, antigüedad, uso y estado | Partes 05, 18, 20 |
| `campaigns.csv` | Inversión y resultados por campaña y canal | Partes 12, 14, 20 |
| `ecommerce_orders.csv` | Pedidos, montos, despacho y devoluciones | Parte 15 |
| `experiments.csv` | Pruebas ejecutadas con muestra y resultado | Partes 19, 20 |

## Limitaciones deliberadas

Los datos incluyen defectos que existen en operaciones reales, porque aprender a detectarlos es parte del
programa:

- Registro incompleto de leads antes del último trimestre.
- Ausencia de costo de servir por cuenta.
- Atribución de último clic en campañas.
- Costo logístico no desagregado en pedidos.
- Varios experimentos sin tamaño de muestra registrado.

Un análisis que no declare estas limitaciones no cumple el estándar de evidencia del programa.

## Uso

```bash
python -c "import csv;print(next(csv.reader(open('datasets/leads.csv',encoding='utf-8'))))"
```

Los notebooks en [`notebooks/`](../notebooks/) los cargan directamente. Para trabajar con hoja de cálculo,
los archivos usan codificación UTF-8 y separador de coma.

## Regla

Antes de usar estos datos en un entregable, declara: qué archivo, qué campos, qué periodo y qué limitación
afecta tu conclusión.

---

[⬅ Programa](../README.md) · [Simulación](../simulations/README.md) ·
[Estándar de evidencia](../docs/ESTANDAR-DE-EVIDENCIA.md)
