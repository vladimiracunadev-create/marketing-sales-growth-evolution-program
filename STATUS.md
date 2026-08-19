---
title: "Estado del repositorio"
type: status
language: es
generated: true
updated: 2026-08-19
---

> Documento generado por `tools/build_status.py`. Los números provienen de contar archivos reales.

# Estado del repositorio

**Versión:** 1.3.0 · **Actualizado:** 2026-08-19

## Inventario frente a metas

| Elemento | Actual | Meta | Estado |
|---|---:|---:|:--:|
| Partes del currículo | 24 | 24 | OK |
| Clases | 336 | 336 | OK |
| Laboratorios | 48 | 48 | OK |
| Evaluaciones de parte | 24 | 24 | OK |
| Casos extendidos | 24 | 24 | OK |
| Proyectos integradores | 12 | 12 | OK |
| Documentos de docs/ | 20 | 20 | OK |
| Notebooks | 8 | 8 | OK |
| Conjuntos de datos | 5 | 5 | OK |
| Obras en bibliografía | 96 | 90 | OK |

**Palabras de contenido curricular:** 1.725.626

**Páginas HTML generadas:** 631 · **Módulos de prueba:** 7 · **Plantillas:** 14

## Verificaciones automatizadas

| Verificación | Resultado | Salida |
|---|:--:|---|
| Estructura del repositorio | OK | Repositorio vÃ¡lido: estructura, profundidad, idioma y bibliografÃ­a conformes. |
| Profundidad del contenido | OK | Profundidad conforme: todo el contenido supera su mÃ­nimo. |
| Enlaces internos | OK | Todos los enlaces internos resuelven correctamente. |

## Puertas de calidad

- [x] 24 partes con 14 clases cada una
- [x] Todas las clases superan 2.500 palabras
- [x] Todas las clases en español con secciones obligatorias
- [x] 48 laboratorios con rúbrica de 100 puntos
- [x] 24 evaluaciones de cuatro bloques ponderados
- [x] 12 proyectos integradores
- [x] Capstone con cumplimiento eliminatorio
- [x] Documentación completa en español
- [x] Sitio HTML generado
- [x] Enlaces internos sin roturas

## Cómo reproducir este informe

```bash
python tools/build_curriculum.py
python tools/build_practica.py
python tools/build_docs.py
python tools/build_site.py
python tools/build_status.py
```

---

[⬅ Programa](README.md) · [Manifiesto](MANIFEST.md) · [Roadmap](ROADMAP.md)
