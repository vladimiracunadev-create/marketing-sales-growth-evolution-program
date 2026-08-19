# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).
Versionado semántico aplicado al contenido: **mayor** = cambio del estándar pedagógico, **menor** = contenido
nuevo, **parche** = correcciones.

## [1.1.0] — 2026-08-19

Reescritura del contenido de las clases y de su fundamentación bibliográfica. La versión 1.0.0 citaba obras
correctamente y declaraba el lente general de cada una; una auditoría propia mostró que ese lente era un
atributo del **libro** y no de la clase —la misma frase servía para las cincuenta y seis clases que citaban
la misma obra—. Esta versión corrige eso y, con ello, reescribe el desarrollo de las 336 clases.

### Estándar

- Nuevo estándar [`clase-profunda-v2`](docs/ESTANDAR-PEDAGOGICO.md), que sustituye a `clase-profunda-v1` y
  añade cuatro requisitos: desarrollo redactado clase a clase (R14), anclaje bibliográfico por idea concreta
  (R8 reformulado), bloque de entrada con prerrequisitos y criterio de término (R15), y criterios de
  respuesta suficiente para cada pregunta de comprobación (R17).
- Las clases pasan de 18 a **20 secciones obligatorias**.

### Fundamentación bibliográfica

- Nuevo catálogo [`curriculum/spec/aportes.py`](curriculum/spec/aportes.py) con **395 ideas concretas**
  atribuidas a las 96 obras: tesis, marcos y distinciones identificables, cada una con la indicación de en
  qué capítulo o sección buscarla. **No se citan números de página**, porque cambian entre ediciones.
- Nuevo mapa [`curriculum/spec/anclajes.py`](curriculum/spec/anclajes.py) con **1.344 anclajes**: para cada
  una de las 336 clases, qué idea de cada una de sus cuatro obras sostiene ese contenido.
- Nuevo auditor [`tools/audit_fuentes.py`](tools/audit_fuentes.py), incorporado a la integración continua.
  Rechaza obras citadas sin anclaje, identificadores inexistentes y anclajes idénticos al lente general.
- El bloque de lectura comparada pasa de una tabla con la misma pregunta crítica en todas las filas a una
  tabla con la idea anclada, dónde buscarla y una pregunta específica para el diagnóstico de esa clase.

### Contenido de las clases

- **1.680 párrafos de desarrollo redactados clase a clase** en 24 módulos
  `curriculum/spec/desarrollo_pNN.py`. El generador se detiene si falta el texto de una clase: ninguna puede
  publicarse con relleno de plantilla.
- Extensión media por clase de 3.400 a **5.053 palabras**; total del currículo de 1.290.000 a **1.697.915**.
- Nuevo bloque **🚦 Antes de empezar**: qué traer resuelto, con qué datos se trabaja, materiales, tiempo real
  y cómo saber que la clase terminó.
- Nuevo bloque **🗝️ Respuestas orientadoras**: qué debe contener una respuesta suficiente a cada pregunta de
  comprobación, sin entregar la respuesta.
- La práctica guiada pasa de una lista de seis pasos a una tabla con qué hacer, con qué material y
  **criterio de término por paso**.

### Pruebas

- Nuevo módulo [`tests/test_fundamentacion.py`](tests/test_fundamentacion.py) con 11 pruebas que hacen
  exigibles R8 y R14: toda obra citada tiene aporte catalogado, todo anclaje apunta a un identificador
  existente, ningún anclaje repite el lente general, ninguna pista de lectura cita páginas numeradas y
  **ningún párrafo de desarrollo se reutiliza entre clases**. El total pasa de 59 a 70 pruebas.

### Documentación

- El README principal publica la **bibliografía completa**: las 96 obras con autoría, edición, aporte y
  número de clases que la citan, más las fuentes normativas oficiales con enlace. El bloque se genera con
  [`tools/build_readme_bibliografia.py`](tools/build_readme_bibliografia.py) y la integración continua
  verifica que liste exactamente 96 obras.
- `docs/ESTANDAR-PEDAGOGICO.md` incorpora la sección de fundamentación bibliográfica con sus tres niveles
  —cita, lente y anclaje— y las prohibiciones asociadas.

### Corregido

- El detector de anglicismos emparejaba mal los asteriscos del énfasis fuerte con los de la cursiva
  siguiente y dejaba títulos en inglés al descubierto, produciendo 99 falsos positivos.
- Un párrafo del desarrollo de la clase 20.07 era una sola frase de 42 palabras; se reescribió al detectarlo
  la nueva prueba de sustancia.
- `tools/build_site.py` sólo escribía el índice de una carpeta cuando el archivo no existía. Al
  reconstruir el portal sobre un sitio ya generado, esos 85 índices conservaban el listado antiguo y
  ocultaban los archivos nuevos. Ahora se reescriben siempre.

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
