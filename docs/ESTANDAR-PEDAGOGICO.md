---
title: "Estándar pedagógico clase-profunda-v2"
type: standard
language: es
updated: 2026-08-19
---

# Estándar pedagógico `clase-profunda-v2`

Especificación formal que toda clase del programa debe cumplir. Sirve para tres cosas: producir contenido
nuevo, auditar contenido existente y detectar degradación con el tiempo.

## 1. Requisitos obligatorios

Una clase cumple el estándar si y sólo si satisface **todos** estos requisitos:

| # | Requisito | Verificación automatizable |
|---|---|---|
| R1 | Extensión mínima de 2.500 palabras | `tools/validate_depth.py` |
| R2 | Escrita íntegramente en español | `tests/test_contenido_publicado.py` |
| R3 | Al menos 4 conceptos con definición operacional | Estructura de `spec` |
| R4 | Al menos 3 señales con numerador, denominador y ventana | Estructura de `spec` |
| R5 | Un método de al menos 5 pasos ordenados | Estructura de `spec` |
| R6 | Una frontera de aplicación explícita | Sección obligatoria |
| R7 | Un caso situado con datos concretos | Sección obligatoria |
| R8 | Cuatro obras citadas, cada una anclada a una idea concreta | `tools/audit_fuentes.py` |
| R9 | Una tabla de errores frecuentes con corrección | Sección obligatoria |
| R10 | Rúbrica de evaluación publicada en la clase | Sección obligatoria |
| R11 | Sección de contexto normativo chileno | Sección obligatoria |
| R12 | Entregable con ruta de evidencia definida | Sección obligatoria |
| R13 | Navegación a clase anterior, índice y siguiente | Bloque final |
| R14 | Desarrollo redactado para esa clase, no generado por plantilla | `curriculum/spec/desarrollo_pNN.py` |
| R15 | Bloque de entrada con prerrequisitos, materiales y criterio de término | Sección obligatoria |
| R16 | Práctica guiada con criterio de término por paso | Sección obligatoria |
| R17 | Criterios de respuesta suficiente para cada pregunta de comprobación | Sección obligatoria |

## 2. Definición operacional de «definición operacional»

Un concepto cumple R3 si su definición permite que **dos personas independientes clasifiquen el mismo caso de
la misma forma**.

Ejemplos:

| Definición | ¿Cumple? | Por qué |
|---|---|---|
| «Lead calificado: contacto interesado en el producto» | No | «Interesado» no es observable |
| «Lead calificado: contacto que cumple el perfil de cliente ideal y declaró un problema que la oferta resuelve, verificado en conversación registrada» | Sí | Dos personas clasifican igual |
| «Marca: el alma de la empresa» | No | No produce predicción alguna |
| «Disponibilidad mental: probabilidad de que la marca sea recordada ante una situación de compra concreta» | Sí | Medible con recuerdo espontáneo |

## 3. Definición operacional de «señal»

Una señal cumple R4 si declara al menos:

- **qué se cuenta** (numerador),
- **sobre qué base** (denominador),
- **en qué ventana temporal**.

Recomendado adicionalmente: fuente, frecuencia, responsable, lectura permitida y lectura prohibida. La ficha
completa está en [`FORMULAS-Y-METRICAS.md`](FORMULAS-Y-METRICAS.md).

## 4. Definición operacional de «frontera de aplicación»

Una frontera cumple R6 si describe una **condición bajo la cual el método enseñado deja de funcionar o
produce daño**, no una advertencia genérica.

| Formulación | ¿Cumple? |
|---|---|
| «Hay que usarlo con criterio» | No |
| «Este método no aplica cuando el volumen de tráfico no permite alcanzar potencia estadística; en ese caso, decidir con investigación cualitativa» | Sí |

## 5. Progresión entre clases

Dentro de una parte, las 14 clases siguen una progresión definida:

| Clases | Función |
|---|---|
| 01–03 | Fundamentos y distinciones del tema |
| 04–08 | Herramientas y métodos centrales |
| 09–12 | Aplicación, medición y casos límite |
| 13 | Tema transversal: ética, riesgo o gobierno |
| 14 | Integración en el artefacto de la parte |

Cada parte cierra con una clase de síntesis que produce el artefacto de portafolio.

## 6. Progresión entre partes

| Nivel | Partes | Aumento de exigencia |
|---|---|---|
| Fundamentos | 01–04 | Distinguir y describir con evidencia |
| Oferta comercial | 05–07 | Diseñar y cuantificar valor |
| Venta | 08–11 | Ejecutar procesos con criterio |
| Adquisición | 12–15 | Operar sistemas con economía verificable |
| Operación de ingresos | 16–18 | Integrar áreas y gobernar datos |
| Crecimiento y analítica | 19–20 | Establecer causalidad y priorizar |
| IA y expansión | 21–22 | Decidir bajo riesgo tecnológico y de expansión |
| Dirección y Capstone | 23–24 | Dirigir el sistema completo y responder por él |

## 6 bis. Fundamentación bibliográfica

Citar una obra no fundamenta nada. El estándar exige tres niveles y verifica el tercero:

| Nivel | Qué declara | Dónde vive |
|---|---|---|
| **Cita** | Autor, obra, año y edición | `spec/bibliografia.py` |
| **Lente** | Para qué sirve esa obra en general | `spec/bibliografia.py` |
| **Anclaje** | Qué idea concreta de esa obra sostiene **esta** clase y dónde buscarla | `spec/aportes.py` + `spec/anclajes.py` |

`aportes.py` cataloga 395 ideas identificables repartidas entre las 96 obras. `anclajes.py` asigna, para
cada una de las 336 clases, cuál de esas ideas sostiene cada una de sus cuatro citas: 1.344 anclajes.

El validador rechaza tres situaciones: una obra citada sin anclaje, un identificador que no existe en el
catálogo de aportes, y un anclaje cuyo texto coincide con el lente general de la obra —porque si sirve para
cualquier clase, no ancla ninguna—.

**Nunca se citan números de página.** Las páginas cambian entre ediciones y el programa no puede
garantizarlas; el anclaje indica el capítulo o la sección por su nombre dentro de la obra.

## 7. Prohibiciones explícitas

Una clase **no puede**:

- Presentar una táctica sin su condición de aplicación.
- Usar una métrica sin definirla operacionalmente.
- Afirmar un contenido normativo sin remitir a fuente oficial.
- Prometer resultados de mercado a partir de datos simulados.
- Reproducir texto protegido por derechos de autor.
- Presentar una única alternativa como respuesta correcta a un problema de decisión.
- Citar una obra sin declarar qué idea concreta de ella sostiene la clase.
- Atribuir a una obra un número de página o de capítulo que no se haya verificado.
- Reutilizar el mismo párrafo de desarrollo en dos clases distintas.

## 8. Auditoría del estándar

```bash
python tools/validate_depth.py        # R1, extensión por clase
python tools/validate_repository.py   # R2 a R17, estructura y secciones
python tools/audit_fuentes.py         # R8, anclaje bibliográfico clase a clase
python -m pytest -q                   # pruebas completas
```

Cualquier clase que falle un requisito debe corregirse en `curriculum/spec/` y regenerarse. **El Markdown no
se edita a mano**: la fuente de verdad es la especificación.

## 9. Versión del estándar

`clase-profunda-v2` es la versión vigente y la que cumplen las 336 clases del programa. Sustituye a
`clase-profunda-v1` en cuatro puntos: el desarrollo se redacta clase a clase en lugar de generarse por
plantilla (R14), cada cita se ancla a una idea concreta de la obra (R8), la clase abre con prerrequisitos y
criterio de término (R15) y cierra las preguntas de comprobación con criterios de respuesta suficiente
(R17). Cualquier cambio que altere los requisitos R1 a R17 exige una versión nueva, la regeneración completa
del currículo y una entrada en el [changelog](../CHANGELOG.md): un estándar que cambia en silencio deja de
ser auditable.

---

[⬅ Documentación](README.md) · [Metodología](METODOLOGIA.md) · [Guía docente](GUIA-DOCENTE.md)
