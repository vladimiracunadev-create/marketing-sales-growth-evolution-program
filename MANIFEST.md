> Documento generado por `tools/build_docs.py`. No editar a mano: los cambios se pierden en la siguiente generación. La fuente de verdad está en `curriculum/spec/`.

# Manifiesto

Inventario cuantitativo verificable. Los números se calculan contando archivos reales, no se declaran a mano. Regenerar con `python tools/build_docs.py`.

| Elemento | Cantidad |
|---|---:|
| Partes del currículo | 24 |
| Clases | 336 |
| Palabras en las clases | 1.799.438 |
| Conceptos con definición operacional | 1344 |
| Señales y métricas definidas | 1008 |
| Obras en la bibliografía | 96 |
| Laboratorios | 48 |
| Evaluaciones de parte | 24 |
| Casos extendidos | 24 |
| Proyectos integradores | 12 |
| Notebooks de analítica | 8 |
| Conjuntos de datos | 5 |
| Plantillas | 14 |

## Verificación

```bash
python tools/validate_repository.py
python -m pytest -q
```

---

[⬅ Programa](README.md) · [Estado](STATUS.md)
