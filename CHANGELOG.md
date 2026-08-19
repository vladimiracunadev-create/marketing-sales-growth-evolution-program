# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).
Versionado semántico aplicado al contenido: **mayor** = cambio del estándar pedagógico, **menor** = contenido
nuevo, **parche** = correcciones.

## [1.6.0] — 2026-08-19

Nueva página [`docs/FUENTES.md`](docs/FUENTES.md): las obras y los enlaces que sostienen el programa, sin
recuentos y sin explicaciones sobre el método. Quien abre un repositorio de curso quiere ver de qué libros
sale el contenido; el README anterior le daba en su lugar cuatro párrafos sobre verificación y una tabla de
estadísticas.

- **`docs/FUENTES.md`** lista, con enlace: qué obras sostienen cada una de las 24 partes, los libros
  agrupados por área con lo que aporta cada uno, las cinco normas chilenas con su texto oficial, los cuatro
  organismos que fiscalizan y las obras que se pueden leer gratis.
- El README pasa de una sección de más de cien líneas a una corta que enlaza esa página y publica las
  normas, que son lo único que cualquiera puede abrir y leer completo sin pagar. Fuera las estadísticas del
  registro.
- `scripts/verify_sources.py` cambia lo que exige del README: ya no contrasta cifras, ahora **falla si
  alguna obra del registro no aparece en `docs/FUENTES.md`** con su título y su enlace. Un registro completo
  no sirve de nada si la página que la gente lee deja obras fuera.
- Una prueba nueva; el repositorio pasa de 84 a **85 pruebas**.

## [1.5.0] — 2026-08-19

Retirado el front matter YAML de todo el material. GitHub lo pinta como una tabla de metadatos justo encima
del título —`title`, `type`, `language`, `part`, `updated`—, es decir en el lugar donde el lector busca el
contenido y donde no le dice nada. Era la misma ficha que se había quitado del cuerpo de las clases,
sobreviviendo en la cabecera del archivo.

- Sin front matter: las **336 clases**, los **24 índices de parte**, el índice del currículo, los 48
  laboratorios, las 24 evaluaciones, los 24 casos, los 12 proyectos, las 17 rutas de rol, los 15 documentos
  de `docs/`, las 13 plantillas y el resto de READMEs. Ahora cada documento empieza por su título.
- **Excepción deliberada:** `.github/ISSUE_TEMPLATE/` conserva el suyo. Ahí el front matter no es
  decoración: es lo que GitHub lee para construir el formulario de la incidencia.
- Lo que ese bloque declaraba —idioma, estándar, umbral de aprobación, minutos estimados, obras citadas y
  anclajes de cada clase— no se pierde: vive en
  [`curriculum/curriculum.json`](curriculum/curriculum.json), que es donde una máquina lo lee sin ensuciar lo
  que lee una persona. El validador y las pruebas lo comprueban ahí.
- El portal se sigue construyendo igual: el título de cada página cae al primer encabezado del documento.
- Dos pruebas nuevas —una exige que ninguna clase abra con front matter, otra que el índice conserve los
  metadatos de las 336—; el repositorio pasa de 83 a **84 pruebas**.

## [1.4.0] — 2026-08-19

Una bibliografía puede estar completa, enlazada y verificada y seguir afirmando algo que no se comprobó. El
localizador demuestra que el libro existe y cuál es su edición; **no demuestra que lo que dice la clase esté
en ese libro**. El README anterior mezclaba las dos cosas y llegaba a escribir «ninguna afirmación de estas
336 clases es invención del programa», una frase que este repositorio no puede respaldar: de las 96 obras,
90 son libros comerciales que el material no ha cotejado frase por frase. Esta versión separa lo comprobado
de lo atribuido y añade fuentes que sí se pueden comprobar sin pagar.

### Lo comprobado y lo atribuido, separados

- El README, cada índice de parte, cada clase y `docs/BIBLIOGRAFIA.md` distinguen ahora dos capas: **lo
  comprobado** —la obra existe, ésta es la edición, el localizador resuelve— y **la atribución del
  programa** —que la idea señalada esté en el capítulo que se indica—, declarada como lectura del material
  y no como cita cotejada. En los términos del propio
  [estándar de evidencia](docs/ESTANDAR-DE-EVIDENCIA.md): hecho verificado frente a inferencia declarada.
- Retirada la afirmación «ninguna afirmación es invención del programa» del README y la equivalente de la
  política del registro.
- Cada obra declara ahora su **acceso**: de las 96, **2** se leen completas y gratis, **3** tienen acceso
  restringido por su editor, **1** es una norma de pago y **90** son libros comerciales. Aparece en el
  README, en cada parte, en cada clase y en `sources/bibliography.json`.

### Fuentes que sí se pueden comprobar

- Las 336 clases nombraban la Ley 19.496 y la Ley 21.719 y **ninguna enlazaba su texto**: cero enlaces a
  `bcn.cl` en todo el currículo. Ahora cada clase enlaza el texto oficial y gratuito de las cinco normas que
  cita.
- Nuevo módulo [`curriculum/spec/normas.py`](curriculum/spec/normas.py) con esas cinco normas. El título de
  cada una no está escrito de memoria: es el que devuelve el servicio de metadatos de la Biblioteca del
  Congreso Nacional, contrastado el 19 de agosto de 2026.
- `scripts/verify_sources.py` gana una comprobación: **una clase que nombre una norma sin enlazar su texto
  hace fallar el CI**. Dos pruebas nuevas; el repositorio pasa de 81 a **83 pruebas**.

## [1.3.0] — 2026-08-19

La versión 1.2.0 dejó cada obra con un localizador comprobable, pero lo hizo sacando la bibliografía del
README y dejándola en un JSON. El efecto práctico fue el contrario del buscado: quien abría el repositorio ya
no veía en ninguna parte de qué libros salía el contenido. Un registro que nadie encuentra no es una fuente,
es un archivo. Esta versión pone la bibliografía a la vista en los tres sitios donde alguien la busca y
reescribe en prosa lo que se había convertido en fichas.

### La bibliografía, visible

- El README vuelve a mostrar **las 96 obras**, ahora agrupadas por categoría y con lo que faltaba en la
  versión original: **el enlace donde se resuelve cada edición** y en cuántas de las 336 clases se cita. Ya
  no está plegada dentro de un `<details>` que había que descubrir.
- **Cada una de las 24 partes** abre su índice con su propia bibliografía: las obras que sostienen esa parte,
  cuántas de sus clases citan cada una y el mismo enlace al localizador.
- **Cada clase** enlaza ahora el título de cada obra que cita y muestra su ISBN junto a la idea concreta que
  esa obra aporta.
- Corregido un recuento que declaraba hasta 347 clases sobre 336: las obras del núcleo pedagógico sumaban dos
  veces las clases que además las citaban de forma explícita. Se cuentan clases, no citas.

### Fuera las fichas, dentro la prosa

- **Se elimina la tabla de requisitos que abría las 336 clases.** Una ficha de cinco filas al empezar no
  enseña nada: obliga a leer casillas antes de saber de qué trata la sesión. Lo que decía —de dónde vienes,
  con qué datos vas a trabajar, cuánto dura, cómo sabrás que terminaste— se dice ahora en prosa, y explica
  además *por qué* importa cada cosa.
- La línea de metadatos bajo el título de cada clase pasa a ser una frase que sitúa la sesión dentro de su
  parte y enlaza al índice.
- **Los 24 índices de parte se reescriben.** Eran encabezados con listas debajo; ahora explican qué se
  estudia en la parte, de qué parte vienes, hacia cuál va lo que produzcas, sobre qué caso se trabaja, qué
  vas a saber hacer, dónde se practica y qué puede salir mal.

## [1.2.0] — 2026-08-19

Trazabilidad de las fuentes. La versión 1.1.0 ancló cada cita a una idea concreta de la obra, pero las 96
obras seguían viviendo en el README, sin un solo localizador: ni un ISBN, ni un DOI, ni una dirección. Quien
quisiera comprobar una cita tenía que buscar la obra por su cuenta y adivinar si daba con la edición que el
programa usó. Esta versión cierra ese hueco.

### Registro de fuentes

- Nuevo registro [`sources/bibliography.json`](sources/bibliography.json) con las **96 obras**, cada una con
  autoría normalizada, año, editorial u organismo responsable, uso clase a clase y **localizador resoluble**:
  ISBN-13 para libros, DOI para artículos y URL de la fuente primaria para normas y documentación oficial.
- Nuevo módulo [`curriculum/spec/localizadores.py`](curriculum/spec/localizadores.py): el localizador vive en
  la especificación, separado del lente pedagógico, y el registro se genera con
  [`tools/build_bibliography_json.py`](tools/build_bibliography_json.py). El JSON es contenido generado; el
  `used_in` de cada obra se cuenta recorriendo las 336 clases, no se declara.
- **89 libros con ISBN-13** comprobado uno a uno contra `openlibrary.org`: los 89 resuelven y el título
  devuelto coincide con el declarado.
- **Dos entradas quedan `pendiente`, declaradas y no rellenadas**: *The Elements of User Onboarding*
  (Hulick), sin ISBN-13 localizable, e *ISO 31000:2018*, cuya ficha de catálogo no se puede confirmar desde
  fuera porque `iso.org` responde 403 tanto a rutas válidas como a rutas inexistentes. La dirección que se
  tenía queda en `proposed_locator`: marcar no es borrar.

### Verificación

- Nuevo verificador [`scripts/verify_sources.py`](scripts/verify_sources.py) —con envoltorio
  `scripts/verify-sources`—, **offline y determinista**, incorporado al CI. Comprueba el esquema, el dígito
  de control de cada ISBN-13, la forma canónica de cada localizador, que toda obra citada tenga entrada, que
  ninguna entrada sobre, que ningún bloque de fuentes se repita entre clases y que **las cifras del README
  coincidan con el recuento del registro**.
- Nuevo revalidador [`scripts/refresh_sources.py`](scripts/refresh_sources.py) —con envoltorio
  `scripts/refresh-sources`—, **en red y sin bloquear**, programado en
  [`fuentes.yml`](.github/workflows/fuentes.yml). Resuelve cada ISBN contra `openlibrary.org` y cada DOI
  contra `api.crossref.org`, compara títulos, escribe `sources/verification-log.json` e informa de lo que
  dejó de resolver **sin borrarlo**. La red no entra en el CI que bloquea: un rojo por causas ajenas se
  aprende a ignorar.
- Once pruebas nuevas en [`tests/test_registro_fuentes.py`](tests/test_registro_fuentes.py); el repositorio
  pasa de 70 a **81 pruebas**.

### Contenido

- El README ya no lleva las 96 filas de la bibliografía. Publica las cifras del registro —producidas por el
  verificador, no escritas a mano—, enlaza el registro y muestra **la obra que manda en cada una de las 24
  partes**. La lista completa, ahora con la columna «Dónde», vive en
  [`docs/BIBLIOGRAFIA.md`](docs/BIBLIOGRAFIA.md).
- Cada clase remite al registro para localizar sus obras.
- Dos pares de clases —`12.11` con `20.08` y `18.09` con `20.07`— declaraban el mismo aparato bibliográfico
  palabra por palabra. Cuando la clase aplicada declara la misma idea que la introductoria, ninguna de las
  dos está declarando su propio uso: se repartieron los anclajes según lo que cada una hace de la obra.

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
- Extensión media por clase de 3.400 a **5.033 palabras**; total del currículo de 1.290.000 a **1.691.227**.
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
