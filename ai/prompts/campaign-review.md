# Prompt — revisión de campaña

Para auditar una campaña antes de lanzarla y después de ejecutarla.

## Antes de lanzar

```text
Te entrego el plan de campaña: [objetivo, audiencia, mensaje, canal, presupuesto, medición].

Audita y responde:
1. ¿El objetivo de optimización coincide con la métrica con que se evaluará? Si no, señálalo.
2. ¿La promesa del anuncio aparece literalmente en la página de destino?
3. ¿Qué afirmación del mensaje carece de evidencia documentada? Enumera cada una.
4. ¿Qué dato personal se está tratando y con qué finalidad declarada?
5. ¿Cuál es el costo por resultado que haría inviable la campaña? Calcúlalo desde la economía unitaria.
6. ¿Qué umbral de qué métrica debería detener la campaña, y qué se haría entonces?
7. ¿Qué está midiendo el plan que no informa ninguna decisión?
8. Extrae cada claim y enlázalo con evidencia para el mismo producto, población, dosis, resultado y ventana.
9. Clasifica cada hallazgo: persuasión sustentada, claim no sustentado, posible publicidad engañosa,
   alucinación generativa, dark pattern, falsa autoridad o información clínica.
10. ¿Qué afiliado, dominio, creatividad y versión distribuirán la pieza? ¿Están registrados y aprobados?
11. ¿Quién aprueba clínica, regulatoria y comercialmente, y qué falta para detener la publicación?
12. Define umbrales posteriores para refund rate, complaint rate, claim rejection rate, affiliate violation
    rate, regulatory incident rate, AI-generated-content rate y human-review rate.

No propongas mejoras creativas hasta responder los doce puntos. Si una fuente, identidad, aprobación o versión
no puede verificarse, responde `BLOQUEAR` y no redactes una alternativa publicable.
```

## Después de ejecutar

```text
Te entrego resultados: [gasto, impresiones, clics, conversiones, oportunidades, cierres, periodo].

Analiza:
1. Calcula costo por oportunidad calificada y costo por cliente ganado, no sólo costo por conversión.
2. Estima qué proporción del resultado pudo ser no incremental y explica por qué.
3. Distingue variación normal de variación atribuible al cambio; si no puedes, dilo.
4. Señala qué conclusión NO se puede sostener con estos datos.
5. Propón la prueba más barata que reduciría la incertidumbre principal.
```

## Regla

Una campaña sin condición de detención definida antes del lanzamiento no debe aprobarse.

---

[⬅ Guardarraíles](../GUARDRAILS.md) · [Parte 14](../../curriculum/part-14-publicidad-y-performance-marketing/README.md)
