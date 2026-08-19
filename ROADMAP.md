# Roadmap

Plan de evolución del programa. Cada versión declara qué agrega y qué problema resuelve.

## v1.0 — Programa completo (publicado, 2026-08-19)

24 partes y 336 clases bajo el estándar `clase-profunda-v2`, capa de práctica con 48 laboratorios y 24
evaluaciones, 17 rutas profesionales, documentación completa, portal HTML e integración continua.

Ver [CHANGELOG.md](CHANGELOG.md) para el detalle.

## v1.1 — Paquete de instructor

**Problema que resuelve:** hoy un instructor debe construir sus propios materiales de sesión a partir de las
clases.

- Guiones de sesión por clase con preguntas de conducción y tiempos.
- Presentaciones de apoyo en HTML para los tres formatos (45, 90 y 150 minutos).
- Ejemplares de trabajos corregidos en los tres niveles de la rúbrica.
- Banco de variantes de caso por parte, para grupos que repiten el programa.
- Revisión de accesibilidad con lector de pantalla sobre el portal completo.

## v1.2 — Motor de simulación

**Problema que resuelve:** el estado de la empresa simulada se actualiza a mano y no produce consecuencias
automáticas.

- Motor de estado que propaga decisiones entre partes: leads, campañas, negocios, clientes, churn y caja.
- Escenarios parametrizables: entrada de competidor, caída de presupuesto, cambio regulatorio.
- Informe de consecuencias por decisión, para retroalimentación inmediata.
- Datos derivados del estado, en lugar de conjuntos estáticos.

## v1.3 — Evaluación asistida

**Problema que resuelve:** la corrección con rúbrica es lenta y varía entre evaluadores.

- Banco de ítems con variantes por concepto.
- Validador de entregables: verifica presencia de fichas de métricas, alternativas y fuentes.
- Guía de calibración entre evaluadores con ejemplos anclados.
- Seguimiento de progreso por competencia en el panel local.

## v1.4 — Ampliación de contexto jurisdiccional

**Problema que resuelve:** el marco normativo es sólo chileno.

- Paquetes jurisdiccionales separados y versionados: LatAm, España, Estados Unidos.
- Estructura que permita mantener el contenido conceptual común y el legal separado.
- Revisión de casos para que funcionen fuera del contexto chileno sin perder concreción.

## v2.0 — Programa multiformato

**Problema que resuelve:** el material sólo existe como texto.

- Versión imprimible completa por nivel.
- Recorridos guiados interactivos por parte.
- Exportación directa a formatos de LMS de uso común.
- Versión de bolsillo con las fichas de medición y los modelos mentales.

> Un cambio de versión mayor implica revisar el estándar pedagógico. Si los requisitos R1 a R13 cambian, el
> estándar pasa a `clase-profunda-v2` y el currículo se regenera completo.

## Criterios de priorización

Una funcionalidad entra al roadmap si cumple al menos dos de estas condiciones:

1. Resuelve un problema declarado por quien estudia o enseña.
2. Reduce la deriva del contenido o mejora su verificabilidad.
3. Amplía el acceso: accesibilidad, idioma o formato.
4. Mejora la fidelidad entre lo que el programa enseña y lo que la práctica exige.

## Fuera de alcance

Decisiones tomadas deliberadamente y que no se revisarán sin un cambio de contexto:

- **Certificación con validez formal.** Requiere estructura institucional que este proyecto no tiene.
- **Contenido en video.** El costo de mantenimiento supera el beneficio para material que se actualiza.
- **Dependencias de infraestructura de pago.** El material debe poder construirse y estudiarse sin costo.
- **Redistribución de obras protegidas.** Se citan, no se incluyen.
- **Promesas de resultados comerciales.** El programa enseña criterio, no garantiza desempeño de mercado.

---

Ver [CHANGELOG.md](CHANGELOG.md) para el historial y [STATUS.md](STATUS.md) para el estado actual.
