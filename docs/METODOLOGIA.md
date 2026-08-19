---
title: "Metodología del programa"
type: methodology
language: es
updated: 2026-08-18
---

# Metodología

Este documento explica **por qué** el programa está construido así. No es una declaración de intenciones:
cada decisión de diseño se traduce en una restricción concreta sobre el contenido, y esa restricción es
verificable en cualquier clase del repositorio.

## 1. El problema que resuelve este diseño

La formación comercial disponible suele fallar de tres maneras conocidas:

1. **Enseña vocabulario en vez de criterio.** Se aprende qué significa «propuesta de valor» sin poder
   distinguir una buena de una mala en un caso concreto.
2. **Presenta tácticas sin condiciones de aplicación.** Se enseña una técnica de cierre sin explicar en qué
   contexto empeora los resultados.
3. **Separa la decisión de su consecuencia.** Se practica sobre casos limpios donde no hay presupuesto
   limitado, competidor agresivo ni obligación legal.

El diseño de este programa ataca las tres directamente.

## 2. Las cinco reglas de construcción

### Regla 1 — Toda afirmación termina en algo observable

Un concepto sólo entra al programa si puede formularse como **definición operacional**: una descripción que
permite a dos personas distintas clasificar el mismo caso de la misma forma. Cuando una definición no produce
predicciones observables, sigue siendo demasiado vaga para dirigir.

Verificación: cada clase tiene una tabla de conceptos donde cada fila declara qué observar para demostrar
comprensión. El [glosario](GLOSARIO.md) reúne 1.344 de esas definiciones.

### Regla 2 — Toda métrica declara su ficha

Ninguna métrica aparece como nombre suelto. Cada señal del programa indica numerador, denominador, ventana
temporal y fuente. El motivo es práctico: la mayor parte de las discusiones comerciales improductivas ocurren
porque dos áreas usan la misma palabra para cosas distintas.

Verificación: [`FORMULAS-Y-METRICAS.md`](FORMULAS-Y-METRICAS.md) contiene 1.008 señales con su definición.

### Regla 3 — Todo método declara su frontera

Cada clase incluye una **frontera de aplicación**: la condición bajo la cual el método enseñado deja de
funcionar o produce daño. Una herramienta presentada sin su límite se aplica donde no corresponde, y ese es
uno de los errores más caros de la práctica comercial.

Verificación: la sección «Comparación de caminos y límites» de cada clase.

### Regla 4 — Toda decisión enfrenta un trade-off explícito

No hay soluciones gratuitas. Cada intervención consume caja, tiempo, atención, capacidad operativa,
reputación o tolerancia al riesgo. El programa exige comparar al menos dos alternativas defendibles y
declarar qué se sacrifica en cada una.

Verificación: los entregables de cada clase, laboratorio y caso exigen dos opciones con costo de oportunidad.

### Regla 5 — Todo cumplimiento es requisito de diseño, no apéndice

La normativa chilena aplicable —consumo, comercio electrónico, datos personales, propiedad industrial,
tributación, libre competencia— aparece como restricción en el diseño de la solución, no como advertencia
final. Un plan que infringe la Ley 19.496 no es un plan con un problema legal: es un plan inválido.

Verificación: la sección «Contexto chileno y cumplimiento» de cada clase y el bloque eliminatorio del
Capstone.

## 3. Estructura de una clase

Todas las clases siguen el estándar `clase-profunda-v2`. La secuencia no es arbitraria: reproduce el orden en
que una persona construye criterio.

| Bloque | Función pedagógica |
|---|---|
| Antes de empezar | Declara prerrequisitos, materiales, tiempo real y criterio de término |
| Propósito | Sitúa el problema antes que la definición |
| Resultados de aprendizaje | Declara el desempeño observable esperado |
| Agenda | Distribuye el tiempo entre recuperación, lectura, medición y decisión |
| Conceptos centrales | Entrega definiciones operacionales y su prueba de comprensión |
| Modelo mental | Presenta el método como secuencia con su frontera |
| Desarrollo | Construye el mecanismo, la distinción, la medición, el intercambio y el gobierno, con prosa escrita para esa clase |
| Lectura comparada | Declara qué idea de cada obra sostiene la clase, dónde buscarla y qué pregunta le hace |
| Ejemplo trabajado | Aplica el método paso a paso sobre el caso persistente |
| Comparación y límites | Explicita cuándo cada camino es preferible y qué arriesga |
| Escalamiento por rol | Muestra cómo cambia la responsabilidad al subir de nivel |
| Caso ejecutivo | Exige una decisión con alternativas y gobierno |
| Práctica guiada | Estructura el trabajo individual con criterio de término por paso |
| Errores frecuentes | Anticipa fallas típicas con su corrección |
| Preguntas de comprobación | Fuerza recuperación activa |
| Respuestas orientadoras | Indica qué debe contener una respuesta suficiente, sin darla |
| Contexto chileno | Traduce la normativa a requisitos de diseño |
| Entregable | Define la evidencia que se produce |
| Evaluación | Publica la rúbrica antes del trabajo |
| Fuentes y verificación | Cierra el circuito de trazabilidad |

## 4. Bases pedagógicas

El diseño aplica cuatro cuerpos de evidencia sobre aprendizaje:

- **Diseño inverso** (Wiggins y McTighe): se define primero el desempeño observable y después el contenido
  que lo hace posible. Por eso cada clase declara sus resultados de aprendizaje antes del desarrollo.
- **Recuperación y dificultad deseable** (Brown, Roediger y McDaniel): el programa abre cada clase con
  recuperación previa y cierra con preguntas de comprobación, en lugar de relectura pasiva.
- **Práctica deliberada** (Ericsson y Pool): cada laboratorio trabaja una habilidad específica con criterio
  explícito y retroalimentación mediante rúbrica publicada.
- **Aprendizaje basado en casos** (Ellet): el caso persistente introduce restricciones, información
  incompleta y consecuencias, que es donde se construye criterio.

Sobre esas bases se agrega una condición propia del dominio comercial: la **acumulación**. Las decisiones de
una parte condicionan las siguientes, igual que en una empresa real.

## 5. El caso persistente

Todo el programa trabaja sobre **Ruta Andina SpA**, una empresa chilena de plataforma de agendamiento, pagos
y CRM ligero para pymes de servicios. La elección no es decorativa: permite recorrer venta B2B recurrente,
comercio electrónico, marketplace y venta al sector público sin cambiar de contexto.

El estado de la simulación vive en [`simulations/state/`](../simulations/state/) y se actualiza en cada
proyecto integrador. Una decisión de pricing tomada en la parte 07 restringe lo posible en la parte 22.

## 6. Qué este programa no hace

- **No certifica ni garantiza empleo.** Acredita evidencia de trabajo: los artefactos son la credencial.
- **No entrega asesoría legal, tributaria ni financiera.** Enseña a identificar obligaciones y a verificarlas
  en su fuente oficial.
- **No promete resultados de mercado.** Los datos del caso son sintéticos y así se declaran.
- **No reproduce contenido protegido.** Cita las obras, enseña a usarlas y no las distribuye.

## 7. Cómo verificar que el programa cumple lo que declara

```bash
python tools/validate_repository.py   # estructura, idioma y profundidad
python -m pytest -q                   # pruebas del repositorio
python tools/build_docs.py            # regenera glosario, métricas y manifiesto
```

El [manifiesto](../MANIFEST.md) cuenta archivos reales, no cifras declaradas a mano.

---

[⬅ Documentación](README.md) · [Estándar pedagógico](ESTANDAR-PEDAGOGICO.md) · [Programa](../README.md)
