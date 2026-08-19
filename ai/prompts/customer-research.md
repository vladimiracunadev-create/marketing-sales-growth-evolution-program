---
title: "Prompt — investigación de cliente"
type: prompt
language: es
updated: 2026-08-18
---

# Prompt — investigación de cliente

Para preparar, conducir y sintetizar entrevistas sin contaminarlas con la propia hipótesis.

## Preparación

```text
Contexto: [segmento, problema que creo que existe, decisión que debo tomar]

Tarea: diseña una guía de entrevista de 30 minutos que cumpla estas condiciones:
- Sólo preguntas sobre comportamiento pasado y hechos concretos.
- Ninguna pregunta sobre el futuro, sobre mi idea ni sobre disposición hipotética a pagar.
- Empieza por la última vez que enfrentó el problema, no por generalidades.
- Incluye preguntas de implicación: qué consecuencia tuvo, cuánto costó, qué hizo después.
- Termina buscando un compromiso verificable (dato, acceso, presentación a otra persona).
- Marca qué pregunta busca refutar mi hipótesis, no confirmarla.

Entrega la guía y, por separado, las tres preguntas que NO debo hacer y por qué.
```

## Síntesis

```text
Te entrego notas literales de [N] entrevistas.

Tarea:
1. Codifica en categorías, sin interpretar todavía.
2. Reporta frecuencia por categoría en números absolutos, nunca en porcentajes.
3. Identifica al menos un caso que contradiga la interpretación dominante.
4. Separa lo que dijeron de lo que yo estoy infiriendo.
5. Formula dos hipótesis refutables y el dato que refutaría cada una.
6. Declara qué NO se puede concluir con esta muestra.

No inventes citas. Si una categoría aparece en menos de tres entrevistas, márcala como señal débil.
```

## Verificación obligatoria

- Ninguna cifra de la síntesis puede provenir del modelo: todas deben rastrearse a las notas.
- Las notas no deben contener datos personales innecesarios para el análisis.
- El compromiso verificable es el único indicador confiable de interés real.

---

[⬅ Prompts](../GUARDRAILS.md) · [Parte 03](../../curriculum/part-03-investigacion-de-mercados-e-inteligencia-competitiva/README.md)
