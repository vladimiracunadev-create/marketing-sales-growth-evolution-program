# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).
Versionado semántico aplicado al contenido: **mayor** = cambio del estándar pedagógico, **menor** = contenido
nuevo, **parche** = correcciones.

## [1.0.0] — 2026-08-19

Primera versión pública del programa. Currículo completo, capa de práctica, documentación, rutas
profesionales, portal HTML e integración continua.

### Currículo

- **24 partes y 336 clases** en español, de 3.000 a 4.100 palabras cada una, bajo el estándar
  [`clase-profunda-v1`](docs/ESTANDAR-PEDAGOGICO.md) con 18 secciones obligatorias: propósito, resultados de
  aprendizaje, agenda por tramos, conceptos operacionales, modelo mental, desarrollo en seis bloques,
  lectura comparada, ejemplo trabajado, comparación de caminos, escalamiento por rol, caso ejecutivo,
  práctica, errores frecuentes, comprobación, contexto chileno, entregable, rúbrica y fuentes.
- **1.344 conceptos con definición operacional**: dos personas independientes deben clasificar el mismo caso
  de la misma forma.
- **1.008 señales con ficha de medición**: numerador, denominador, ventana, fuente y lectura prohibida.
- **96 obras de referencia** con el lente que aporta cada una y trazabilidad por clase, desde Drucker y
  Kotler hasta Kohavi, Fader, Ramanujam y el marco de gestión de riesgo de IA del NIST.
- **Caso persistente Ruta Andina SpA** con estado inicial, restricciones y continuidad entre partes: las
  decisiones de una parte condicionan las siguientes.

### Práctica y evaluación

- 48 laboratorios con rúbrica de 100 puntos y escenario adverso obligatorio.
- 24 evaluaciones de parte con cuatro bloques ponderados y criterio de aprobación explícito.
- 24 casos extendidos con complicación a mitad de sesión.
- 12 proyectos integradores que conectan dos partes y exigen resolver su contradicción.
- Capstone con bloque de cumplimiento normativo **eliminatorio**.

### Rutas profesionales

- **17 guías de carrera** en [`rutas/`](rutas/README.md): analista de marketing, marketing manager, product
  marketing, growth, SDR/BDR, ejecutivo comercial, customer success, RevOps, performance marketer, content
  manager, e-commerce manager, brand manager, head of GTM, CMO, VP de ventas, CRO y founder.
- Cada guía describe qué es el puesto, cómo es un día real, competencias del oficio, herramientas, el
  recorrido concreto del programa, artefactos que lo acreditan, credenciales que pesan, progresión, rangos
  orientativos por región, mitos frecuentes y una nota honesta sobre lo que el programa no cubre.

### Documentación

- Metodología, estándar pedagógico, estándar de evidencia, evaluación y rúbricas, arquitectura, ruta de
  aprendizaje, guía docente, plan de capacitación y migración a LMS, rutas profesionales, accesibilidad y
  preguntas frecuentes.
- Mapa regulatorio chileno, registro de fuentes oficiales y ética de datos personales.
- Documentación derivada generada desde la especificación: glosario, fórmulas y métricas, bibliografía, mapa
  del currículo, mapa de competencias, syllabus, manifiesto, índice de archivos y estado.

### Herramientas y portal

- Generadores de currículo, práctica, rutas, documentación, estado y sitio, **sin dependencias externas**:
  construir y validar el material no exige instalar nada.
- Validadores de estructura, profundidad, enlaces internos y artefacto del portal.
- Portal HTML autocontenido de 632 páginas con buscador, tema claro y oscuro, hoja de estilo de impresión y
  panel de progreso exportable.
- 59 pruebas y cuatro flujos de integración continua: validación multi-OS y multi-versión de Python,
  publicación con verificación del sitio ya desplegado, análisis estático y revisión de seguridad e higiene.

### Datos y recursos

- 5 conjuntos de datos sintéticos con limitaciones declaradas.
- 8 notebooks de analítica comercial.
- 12 plantillas de artefacto y 6 planillas operativas.
- Prompts, especificaciones de agentes y guardarraíles de IA comercial.

[1.0.0]: https://github.com/vladimiracunadev-create/marketing-sales-growth-evolution-program/releases/tag/v1.0.0
