# Auditoría e integración de Marketing, Ventas, Growth y Producto

## Diagnóstico inicial

La auditoría confirmó la arquitectura canónica: **24 partes, 336 clases y 14 clases por parte**. La fuente de
verdad vive en `curriculum/spec/`; currículo publicado, prácticas, documentación y portal son derivados. El
caso persistente sigue siendo **Ruta Andina SpA**. MEDVi y los casos de crecimiento responsable son contrastes
secundarios y no lo sustituyen.

Las fortalezas previas eran pricing, ventas, CRM/RevOps, CX/CS, growth, analítica e IA responsable. Las brechas
más altas estaban en Agile, innovación, personalización integral, ficha Buyer Persona y estrategia de entorno.
Había cobertura parcial sin una cadena explícita en creación de valor, entrevistas, producto, marketing mix,
ciclo de vida y productividad comercial.

## Duplicaciones y decisión de arquitectura

Se detectaron solapamientos legítimos en valor, roles de compra, entrevistas, unit economics, cohortes, Voice
of Customer, forecast y experimentación. La corrección no fue repetir el contenido: cada eje tiene una **clase
principal** y referencias cruzadas. El catálogo de conceptos y métricas dejó de ocultar definiciones
contextuales mediante `first-wins`; conserva variantes distintas y sólo deduplica definiciones idénticas.

## Matriz de integración A–N

| Eje | Clase principal | Estado inicial | Brecha integrada | Evidencia esperada | Prioridad |
|---|---|---|---|---|:--:|
| A · Valor | 05.02 | parcial alto | beneficios/sacrificios, valor creado/capturado, ejercicio de tres ofertas | matriz y recomendación condicional | P0 |
| B · Buyer Persona | 02.04 | parcial | tres estados, B2C/B2B/B2G, sesgo y caducidad | matriz atributo–fuente–estado | P0 |
| C · Entrevistas | 03.03 | parcial alto | diez preguntas, consentimiento, SPIN/JTBD, codificación y triangulación | guion, registro y memo | P0 |
| D · Ficha Persona | 02.14 | brecha alta | ficha integral y cuatro contextos | cuatro fichas comparadas | P0 |
| E · Producto | 05.11 | parcial | experiencia–propósito–oportunidad, discovery/delivery, gobierno y retiro | product brief, roadmap y backlog | P0 |
| F · Estrategia | 03.10 | brecha alta | PESTEL, cinco fuerzas, genéricas y modelo de negocio | memo, fuerzas y Canvas | P0 |
| G · Marketing | 01.09 | parcial | evolución, 4P/7P, omnicanalidad y alineación | mix, journey y SLA | P1 |
| H · Ciclo de vida | 05.09 | parcial alto | saturación, renovación, BCG, canibalización y retiro | diagnóstico y escenario | P1 |
| I · Pricing | 07.14 | parcial alto | Revenue Management, rentabilidad segmentada y escenario resuelto | modelo y política | P1 |
| J · Agile | 19.09 | brecha crítica | Manifiesto, Scrum, Kanban, Lean, WIP y flujo sin imponer Scrum | sistema de trabajo | P0 |
| K · Personalización | 21.05 | brecha crítica | niveles, B2B/B2C, vigilancia, explicabilidad, A/B e incrementalidad | protocolo y guardarraíles | P0 |
| L · Relaciones/CX | 18.14 | parcial alto | empatía, momentos de verdad, recuperación y fidelización | journey y plan de recuperación | P1 |
| M · Productividad | 23.14 | parcial alto | productividad sistémica, carteras, cuellos, capacidad y BSC | modelo de capacidad y tablero | P1 |
| N · Innovación | 05.13 | brecha crítica | tipos, Design Thinking, deseabilidad/factibilidad/viabilidad, fracaso y abandono | prototipo y post-mortem | P0 |

## Integración transversal

- La [guía de entrevista](../templates/market-research/interview-guide.md) incorpora las diez áreas,
  consentimiento, enfoques, codificación, triangulación y uso controlado de IA.
- La [ficha Buyer Persona](../templates/customer/buyer-persona-evidence.md) cubre todos los campos, estados,
  confianza, cuatro contextos y criterios de actualización.
- El [proyecto transversal Ruta Andina](PROYECTO-TRANSVERSAL-RUTA-ANDINA.md) enlaza sus 30 entregables con
  clases, reutilización y evidencia.
- Cada ampliación incluye actividad, solución razonada, rúbrica, métrica con ficha completa, transferencia y
  un caso de IA con objetivo, datos, prompt, resultado, validación, riesgos, límites y alternativa sin IA.
- Las cifras de 37 % y 2,5× sobre personalización no se presentan como hechos: quedan excluidas hasta que una
  fuente original documente población, método, año, contexto, magnitud y limitaciones.

## Rutas profesionales

No se duplicaron las 17 rutas existentes. La cobertura se amplía por variantes: Product Manager, Product
Owner y dirección de producto usan Product Marketing + 05.11 + 19.09 + 05.13; investigación de mercados usa
Analista de marketing + 02.04 + 03.03; Customer Experience Manager usa Customer Success + 18.14; KAM y venta
consultiva usan Ejecutivo comercial + partes 09, 16 y 18; CRM specialist usa RevOps + partes 16–17; consultor
de negocios usa Marketing Manager/Founder + 03.10, 05.11, 07.14 y 23.14. Crear rutas separadas sólo se
justifica si el mercado o una evaluación futura demuestra que estas variantes no bastan.

## Riesgos y límites

- Las nuevas subsecciones no convierten ejemplos sintéticos en investigación real.
- PESTEL, ciclo de vida, BCG, Scrum y los marcos de innovación se enseñan con fronteras de aplicación.
- Las métricas no demuestran causalidad salvo que el diseño identifique un contrafactual defendible.
- Una revisión humana sigue siendo obligatoria en decisiones de precio, producto, personalización, personas,
  cumplimiento y comunicaciones externas.

## Validación

Resultados ejecutados el **13 de octubre de 2026**:

| Comprobación | Resultado |
|---|---|
| `tools/build_curriculum.py --check` | 24/24 partes con especificación |
| `tools/validate_repository.py` | 10.056 comprobaciones superadas |
| `tools/validate_depth.py` | 336 clases, 48 labs, 24 evaluaciones y 24 casos conformes |
| `tools/audit_fuentes.py` | 336/336 clases, 1.345 citas, 103 obras y 402 ideas |
| `scripts/verify_sources.py` | 103 entradas: 101 verificadas y 2 pendientes declaradas |
| `tools/check_links.py` | 8.153 enlaces internos válidos |
| `pytest` | 96 pruebas aprobadas |
| `tools/validate_site.py` | 641 páginas y 16 comprobaciones superadas |
| Regeneración completa repetida | mismo hash del diff antes y después |
| Marcadores de conflicto y `git diff --check` | sin incidencias |
| Revisión programática de mojibake | 0 archivos sospechosos |

Las 2 fuentes pendientes ya estaban declaradas como tales en el registro y el verificador las admite; no se
presentan como localizadores comprobados. La publicación remota y sus workflows se verifican por separado
después del `push`.

---

[⬅ Documentación](README.md) · [Currículo](../curriculum/README.md) · [Programa](../README.md)
