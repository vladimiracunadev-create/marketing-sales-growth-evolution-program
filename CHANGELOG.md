# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).
Versionado semántico aplicado al contenido: **mayor** = cambio de estándar pedagógico, **menor** = contenido
nuevo, **parche** = correcciones.

## [2.1.0] — 2026-08-19

Presentación, orientación profesional y refuerzo de la integración continua.

### Agregado

- **17 rutas profesionales con página propia** en [`rutas/`](rutas/README.md), generadas desde
  `curriculum/spec/roles.py`. Cada guía describe qué es el puesto, cómo es un día real, qué hay que saber,
  qué partes del programa lo preparan, qué artefactos lo acreditan, cómo progresa la carrera, qué rangos
  salariales orientativos tiene y qué mitos lo rodean: analista de marketing, marketing manager, product
  marketing, growth, SDR/BDR, ejecutivo comercial, customer success, RevOps, performance marketer, content
  manager, e-commerce manager, brand manager, head of GTM, CMO, VP de ventas, CRO y founder.
- `tools/build_rutas.py` y `tools/validate_site.py`.
- Flujo `codeql.yml` de análisis estático sobre las herramientas.
- Verificación del **sitio ya publicado** en `pages.yml`: comprueba ocho rutas clave en producción con
  reintentos, y falla si alguna no responde.
- Trabajo de **coherencia de cifras** en `ci.yml`: contrasta el README y el manifiesto contra los archivos
  reales del repositorio.
- Trabajo de **construcción y validación del portal** en `ci.yml`.
- 13 pruebas nuevas para las rutas profesionales (59 en total).

### Cambiado

- **README principal rediseñado**: cabecera centrada con insignias de los cuatro flujos, enlaces rápidos,
  aviso de cumplimiento, tabla de estado verificable, diagrama de los ocho niveles, tabla completa de las
  24 partes con su artefacto, estado del caso persistente, tabla de rutas por rol, sección de calidad y CI,
  bibliografía colapsable, comparación de qué es y qué no es, límites honestos y programas hermanos.
- `ci.yml` ejecuta ahora una matriz de Python 3.9 a 3.13 en Linux, más macOS y Windows.
- `security.yml` verifica además que todos los flujos declaren permisos explícitos y que los conjuntos de
  datos no contengan correos personales.
- `docs/RUTAS-PROFESIONALES.md` pasa a ser la guía de selección y remite a las páginas por rol.
- El portal incorpora la sección de rutas y el panel de progreso (632 páginas).

## [2.0.0] — 2026-08-18

Reconstrucción completa del programa sobre el estándar `clase-profunda-v3`.

### Agregado

- **Arquitectura generada.** Fuente de verdad pedagógica en `curriculum/spec/`: bibliografía maestra,
  definición de las 24 partes y 24 archivos de especificación con 14 clases cada uno.
- **336 clases profundas en español**, de 3.000 a 4.100 palabras, con 18 secciones obligatorias: propósito,
  resultados de aprendizaje, agenda por tramos, conceptos operacionales, modelo mental, desarrollo en seis
  bloques, lectura comparada, ejemplo trabajado, comparación de caminos, escalamiento por rol, caso
  ejecutivo, práctica, errores frecuentes, comprobación, contexto chileno, entregable, rúbrica y fuentes.
- **1.344 conceptos con definición operacional** y **1.008 señales con ficha de medición**.
- **96 obras de referencia** con el lente que aporta cada una, desde Drucker y Kotler hasta Kohavi, Fader,
  Ramanujam y el marco de gestión de riesgo de IA del NIST.
- **Caso persistente Ruta Andina SpA**, con estado inicial, restricciones y continuidad entre partes.
- **Capa de práctica regenerada:** 48 laboratorios con rúbrica de 100 puntos, 24 evaluaciones de cuatro
  bloques ponderados, 24 casos con complicación a mitad de sesión, 12 proyectos integradores y Capstone con
  bloque de cumplimiento eliminatorio.
- **Documentación completa en español:** metodología, estándar pedagógico, estándar de evidencia, evaluación
  y rúbricas, arquitectura, ruta de aprendizaje, guía docente, plan de capacitación, rutas profesionales,
  accesibilidad, preguntas frecuentes, mapa regulatorio chileno, fuentes oficiales y ética de datos.
- **Documentación derivada generada:** glosario, fórmulas y métricas, bibliografía, mapa del currículo, mapa
  de competencias, syllabus, manifiesto e índice de archivos.
- **Sitio HTML autocontenido** (`tools/build_site.py`) con navegación, buscador operable por teclado, tema
  claro y oscuro, y hoja de estilo de impresión.
- **Validadores y pruebas:** `validate_repository.py`, `validate_depth.py`, `check_links.py`, `build_status.py`
  y suite de pruebas en `tests/`.
- **Integración continua:** flujos de validación, publicación en GitHub Pages y revisión de seguridad.
- Archivos de proyecto: `VERSION`, `.gitattributes`, `.editorconfig`, `.markdownlint-cli2.jsonc`,
  `CODE_OF_CONDUCT.md`, `STATUS.md`.

### Cambiado

- **Idioma.** El contenido pasó de una mezcla de español e inglés a español íntegro.
- **Profundidad.** Las clases pasaron de ~690 palabras genéricas a 3.000–4.100 palabras con sustancia
  específica por tema.
- **Bibliografía.** De una lista sin uso declarado a 96 obras con lente y trazabilidad por clase.
- **Cumplimiento normativo.** De un anexo de enlaces a una sección obligatoria por clase y un bloque
  eliminatorio en el Capstone.
- **Métricas.** De nombres sueltos a fichas con numerador, denominador, ventana, fuente y lectura prohibida.
- **Caso.** De un enunciado genérico a una empresa simulada con estado, restricciones y continuidad.
- `docs/` reorganizado y reescrito en español; documentos derivados marcados como generados.
- `scripts/` migrado a `tools/`.

### Eliminado

- Documentación en inglés superseded: `CAREER-PATHS.md`, `CHILE-REGULATORY-MAP.md`, `CURRICULUM-MAP.md`,
  `DATA-ETHICS-AND-PRIVACY.md`, `EVIDENCE-STANDARD.md`, `GLOSSARY.md`, `INSTRUCTOR-GUIDE.md`,
  `METHODOLOGY.md`, `PROGRAM-ARCHITECTURE.md`, `SOURCES-2026.md`.
- `books/BIBLIOGRAPHY.md`, reemplazado por `docs/BIBLIOGRAFIA.md` generado.
- `PROJECT_STATUS.md` y `MANIFEST.json`, reemplazados por `STATUS.md` y `MANIFEST.md` generados.

## [1.0.0] — 2026-08-17

### Agregado

- Estructura inicial del programa: 24 partes y 336 clases.
- 48 laboratorios, 24 evaluaciones, 12 proyectos y Capstone.
- 8 notebooks de analítica, 5 conjuntos de datos sintéticos y plantillas.
- Mapa regulatorio chileno y registro de fuentes oficiales.
- Panel de seguimiento local sin dependencias.

[2.1.0]: https://github.com/vladimiracunadev-create/marketing-sales-growth-evolution-program/releases/tag/v2.1.0
[2.0.0]: https://github.com/vladimiracunadev-create/marketing-sales-growth-evolution-program/releases/tag/v2.0.0
[1.0.0]: https://github.com/vladimiracunadev-create/marketing-sales-growth-evolution-program/releases/tag/v1.0.0
