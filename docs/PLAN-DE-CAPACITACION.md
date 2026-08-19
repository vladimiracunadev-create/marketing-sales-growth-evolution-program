---
title: "Plan de migración a capacitación"
type: training-plan
language: es
updated: 2026-08-18
---

# Plan de migración a capacitación

Este repositorio está diseñado para funcionar en dos modos: **autoformación guiada** (leyendo el Markdown o
el sitio HTML) y **capacitación con instructor** (presencial, remota o mixta). Este documento explica cómo
migrar del primero al segundo sin reescribir contenido.

## 1. Qué ya está listo para capacitación

| Elemento | Estado | Dónde |
|---|---|---|
| Contenido en Markdown | 336 clases con estructura idéntica | `curriculum/` |
| Contenido en HTML navegable | Sitio autocontenido con buscador | `site/` (generado) |
| Rúbricas publicadas | En cada clase, laboratorio y evaluación | Todo el repositorio |
| Agenda por clase | Bloques de 150 minutos con evidencia por tramo | Sección «Agenda sugerida» |
| Casos con complicación | 24 casos con giro a mitad de sesión | `cases/` |
| Evaluaciones con ponderación | 24 evaluaciones de cuatro bloques | `assessments/` |
| Datos para ejercicios | 5 conjuntos sintéticos reproducibles | `datasets/` |

## 2. Formatos de entrega

### Formato A — Clase de 150 minutos (estándar)

Corresponde uno a uno con una clase del repositorio. La agenda de cada clase ya está distribuida:

| Tramo | Actividad del instructor | Actividad del participante |
|---|---|---|
| 0–15 | Lanza la pregunta rectora sin dar respuesta | Recuperación previa por escrito |
| 15–45 | Conduce el desarrollo conceptual | Construye tabla `hecho / inferencia / supuesto` |
| 45–75 | Modela una ficha de medición | Construye la ficha de la señal principal |
| 75–110 | Guía el ejemplo trabajado | Ejecuta el método sobre el caso |
| 110–140 | Facilita el caso ejecutivo | Produce dos alternativas y recomienda |
| 140–150 | Cierra con preguntas de comprobación | Registra lo que aún no sabe |

### Formato B — Sesión de 90 minutos

Recorta el ejemplo trabajado y traslada la práctica a trabajo posterior.

| Tramo | Contenido |
|---|---|
| 0–10 | Recuperación y pregunta rectora |
| 10–40 | Conceptos y modelo mental |
| 40–70 | Caso ejecutivo abreviado |
| 70–90 | Cierre, entregable y comprobación |

### Formato C — Sesión de 45 minutos

Sólo para reforzamiento o para introducir un tema. Cubre propósito, conceptos centrales y una pregunta de
comprobación. El trabajo real queda como asignación.

### Formato D — Taller intensivo de una parte (2 días)

| Bloque | Contenido |
|---|---|
| Día 1 mañana | Clases 01 a 05 en modalidad conceptual acelerada |
| Día 1 tarde | Laboratorio 1 completo con acompañamiento |
| Día 2 mañana | Clases 06 a 14 con foco en integración |
| Día 2 tarde | Laboratorio 2 y evaluación de la parte |

### Formato E — Programa completo (12 meses)

Dos clases semanales, un laboratorio quincenal, una evaluación mensual y un proyecto integrador cada dos
meses. Capstone en los últimos dos meses.

## 3. Ruta de migración a una plataforma LMS

El contenido está estructurado para exportarse sin reescritura.

### Paso 1 — Generar el HTML

```bash
python tools/build_site.py
```

Produce `site/` con una página por clase, índice navegable, buscador y hoja de estilo de impresión. Cada
página es autocontenida: no depende de recursos externos.

### Paso 2 — Elegir la unidad de importación

| Unidad LMS | Corresponde a |
|---|---|
| Curso | El programa completo o un nivel |
| Módulo | Una parte (14 clases) |
| Lección | Una clase |
| Tarea | Un laboratorio |
| Cuestionario | Una evaluación de parte |
| Proyecto | Un proyecto integrador |

### Paso 3 — Mapear metadatos

Cada clase incluye un bloque de metadatos en su cabecera que alimenta la importación:

```yaml
title: "..."          # título de la lección
part: "07"            # módulo de destino
class: "04"           # orden dentro del módulo
level: "Oferta comercial"
mastery_threshold: 80 # nota mínima de aprobación
estimated_minutes: 150
sources: [...]        # bibliografía asociada
```

El archivo `curriculum/curriculum.json` entrega el mismo árbol en formato legible por máquina, listo para
alimentar un importador.

### Paso 4 — Cargar evaluación

Las evaluaciones tienen cuatro bloques con ponderación explícita (25/30/30/15) y criterio de aprobación
(80/100, ningún bloque bajo 60 %). Son de respuesta construida, no de selección múltiple: requieren
corrección humana o rúbrica asistida.

Si la plataforma exige selección múltiple, usa las preguntas de comprobación de cada clase como banco de
ítems formativos, pero **no** sustituyas las evaluaciones de parte: la competencia que este programa
desarrolla no se mide con alternativas.

### Paso 5 — Definir el registro de evidencia

Cada clase indica una carpeta de evidencia con la convención `evidence/PXX-CYY-slug/`. En un LMS, esa carpeta
se traduce en el conjunto de archivos que el participante adjunta a la tarea.

## 4. Preparación del instructor

### Antes del programa

- [ ] Leer [`METODOLOGIA.md`](METODOLOGIA.md) y [`ESTANDAR-PEDAGOGICO.md`](ESTANDAR-PEDAGOGICO.md).
- [ ] Recorrer completa la parte que va a dictar, incluidos sus dos laboratorios.
- [ ] Resolver el caso de la parte antes de facilitarlo.
- [ ] Verificar las referencias normativas en su fuente oficial vigente.
- [ ] Preparar dos ejemplos propios que reemplacen o complementen el caso persistente.

### Antes de cada sesión

- [ ] Confirmar que los participantes tienen acceso al material.
- [ ] Preparar la pregunta rectora y resistir la tentación de responderla.
- [ ] Identificar los tres errores frecuentes que espera ver.
- [ ] Tener lista la rúbrica que se aplicará.

### Durante la sesión

- Ante una respuesta correcta, pregunta cuándo dejaría de serlo.
- Ante una respuesta incorrecta, pide el observable que la sostendría.
- No cierres el caso con «la respuesta correcta»: cierra con el criterio de decisión.

## 5. Adaptación por audiencia

| Audiencia | Ajuste recomendado |
|---|---|
| Equipos comerciales en ejercicio | Reemplazar el caso persistente por datos reales de la empresa |
| Formación técnico-profesional | Formato B, más práctica guiada, menos lectura comparada |
| Educación superior | Formato A completo, exigir las cuatro fuentes de la lectura comparada |
| Programas ejecutivos | Partes 16 a 24 con foco en dirección y gobierno |
| Emprendedores | Partes 01 a 07 más 11, 12 y 24 |

## 6. Verificación de calidad de la implementación

Una implementación es fiel al diseño si cumple estas cinco condiciones:

1. Las rúbricas se publican **antes** del trabajo, no después.
2. Cada entregable exige dos alternativas con costo de oportunidad.
3. Cada métrica presentada declara numerador, denominador y ventana.
4. El bloque de cumplimiento normativo se evalúa y es eliminatorio en el Capstone.
5. Los participantes producen artefactos que podrían mostrar a un empleador.

Si alguna falla, la implementación bajó el estándar del programa aunque haya cubierto el contenido.

## 7. Licencia y uso en capacitación

El contenido original del repositorio está bajo licencia MIT: puede usarse en capacitación comercial y no
comercial conservando la atribución. Las obras citadas, las marcas y las normas pertenecen a sus titulares y
no se redistribuyen.

---

[⬅ Documentación](README.md) · [Guía docente](GUIA-DOCENTE.md) ·
[Evaluación y rúbricas](EVALUACION-Y-RUBRICAS.md)
