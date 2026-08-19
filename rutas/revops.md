# ⚙️ RevOps / Sales Operations

> Quien hace que marketing, ventas y éxito de cliente funcionen como un solo sistema. Su valor no está en producir más informes sino en que las decisiones dejen de discutirse sobre cifras que nadie puede reconciliar.
>
> **Nivel de entrada:** Intermedio a senior; suele venir de analítica, de ventas o de administración de CRM · **Foco:** Modelo de datos, pipeline, forecast, automatización gobernada y acuerdos entre áreas · **Señal de mercado:** Un operating model donde cada indicador tiene una cifra única con su definición

## 🧭 Qué es y por qué importa

RevOps existe porque los sistemas de marketing, ventas y servicio evolucionaron por separado y produjeron tres versiones incompatibles de la verdad. El síntoma clásico: marketing informa 300 leads, ventas trabaja 60 y la reunión mensual se consume discutiendo cuál cifra es la real.

El trabajo tiene dos capas. La visible es la técnica: configurar el CRM, diseñar el pipeline, construir automatizaciones e integraciones. La invisible y más difícil es la de acuerdos: lograr que dos áreas con incentivos distintos usen la misma definición de lead calificado.

Es un rol de apalancamiento silencioso. Nadie felicita a quien evitó que el forecast se construyera sobre un pipeline con 44 % de oportunidades sin actividad, pero esa corrección cambia decisiones de contratación y de presupuesto.

## 🗓️ Un día en el puesto

- **Higiene de datos:** duplicados, campos críticos incompletos, oportunidades sin actividad y etapas sin evidencia.
- **Monitoreo de integraciones:** si el flujo entre CRM y facturación se detuvo, hay que saberlo hoy y no cuando reclame un cliente.
- **Preparación de forecast:** consolidar ingreso nuevo, renovación, expansión y contracción, y reportar la precisión histórica junto a la proyección.
- **Gobierno de cambios:** aprobar o rechazar modificaciones de configuración con procedimiento y registro.
- **Acuerdos entre áreas:** medir el cumplimiento del acuerdo de servicio y llevar el dato a la conversación, no la opinión.

## 🧠 Qué necesitas saber

### Conocimiento del oficio

- **Modelo de datos de ingresos.** Entidades, estados válidos, fuente autoritativa por dato y jerarquía de cuentas.
- **Diseño de pipeline.** Etapas por evidencia del cliente, criterios de salida verificables y probabilidades calculadas con datos históricos.
- **Forecast unificado.** Ingreso nuevo, renovación, expansión y contracción modelados por separado, con precisión medida por componente.
- **Automatización gobernada.** Documentación, prueba controlada, responsable y capacidad de detención inmediata.
- **Observabilidad.** Indicadores de salud por proceso; enterarse de las fallas por reclamo es la forma más cara de enterarse.
- **Cumplimiento de datos.** Base de licitud, retención, eliminación efectiva y registro del tratamiento.

### Herramientas

```text
CRM:              Salesforce, HubSpot (administración avanzada)
Automatización:   flujos, enrutamiento, lifecycle stages
Datos:            SQL, herramientas de integración, conciliación
Reporte:          tableros operativos y de dirección
Gobierno:         procedimiento de cambio y registro de configuración
```

La herramienta no hace al profesional. Lo que el mercado paga es el **criterio** para decidir qué medir, qué descartar y qué recomendar cuando la evidencia es incompleta.

### Habilidades no técnicas

- **Mediar entre áreas con incentivos opuestos.** El acuerdo de servicio es una negociación permanente, no un documento.
- **Resistir la petición de más campos.** Cada campo obligatorio adicional degrada la calidad del conjunto.
- **Explicar la diferencia entre dos cifras** sin que ninguna área quede como culpable.
- **Documentar.** Un sistema sin registro de por qué está configurado así se vuelve inmanejable en dos años.

## 📚 Tu ruta en el programa

Orden recomendado. Todas las rutas asumen que empiezas por la [parte 01](../curriculum/part-01-marketing-y-ventas-fundamentos-del-sistema-comercial/README.md), que entrega el mapa del sistema comercial completo.

1. 📚 [**Parte 01 — Marketing y ventas: fundamentos del sistema comercial**](../curriculum/part-01-marketing-y-ventas-fundamentos-del-sistema-comercial/README.md) · el motor de ingresos completo, que es exactamente el objeto del rol
2. 📚 [**Parte 16 — CRM, pipeline y sales operations**](../curriculum/part-16-crm-pipeline-y-sales-operations/README.md) · **el núcleo operativo**: CRM, pipeline, forecast, cuotas y capacidad
3. 📚 [**Parte 17 — Marketing automation y revenue operations**](../curriculum/part-17-marketing-automation-y-revenue-operations/README.md) · **el núcleo de integración**: lifecycle, scoring, SLA, datos y observabilidad
4. 📚 [**Parte 20 — Analítica comercial y marketing science**](../curriculum/part-20-analitica-comercial-y-marketing-science/README.md) · analítica: definiciones, cohortes y coherencia aritmética
5. 📚 [**Parte 18 — Customer experience, success y fidelización**](../curriculum/part-18-customer-experience-success-y-fidelizacion/README.md) · retención y renovación, la mitad del forecast que suele estimarse a ojo
6. 📚 [**Parte 23 — Dirección comercial: CMO, VP Sales y CRO**](../curriculum/part-23-direccion-comercial-cmo-vp-sales-y-cro/README.md) · dirección comercial: para hablar el idioma de quien recibe tus informes

### Clases por las que empezar

- 🎯 [16.03 · Etapas y criterios de salida](../curriculum/part-16-crm-pipeline-y-sales-operations/class-03-etapas-y-criterios-de-salida.md) — Etapas y criterios de salida: la evidencia del cliente, no la intención propia
- 🎯 [16.07 · Forecast](../curriculum/part-16-crm-pipeline-y-sales-operations/class-07-forecast.md) — Forecast: método declarado y sesgo corregido
- 🎯 [17.07 · Acuerdo de servicio entre marketing y ventas](../curriculum/part-17-marketing-automation-y-revenue-operations/class-07-sla-marketing-ventas.md) — Acuerdo de servicio entre marketing y ventas: la definición compartida
- 🎯 [17.08 · Modelo de datos de RevOps](../curriculum/part-17-marketing-automation-y-revenue-operations/class-08-modelo-de-datos-revops.md) — Modelo de datos: fuente autoritativa por dato
- 🎯 [17.12 · Calidad y observabilidad](../curriculum/part-17-marketing-automation-y-revenue-operations/class-12-calidad-y-observabilidad.md) — Calidad y observabilidad: no enterarse por reclamo
- 🎯 [17.13 · Gobernanza de automatizaciones](../curriculum/part-17-marketing-automation-y-revenue-operations/class-13-gobernanza-de-automatizaciones.md) — Gobernanza de automatizaciones: poder explicar qué hizo el sistema
- 🎯 [16.05 · Higiene de datos](../curriculum/part-16-crm-pipeline-y-sales-operations/class-05-higiene-de-datos.md) — Higiene de datos: degradación, deduplicación y retención

## 🧪 Práctica y evaluación

| Recurso | Ruta |
|---|---|
| 🧪 Laboratorios de la parte 16 — CRM, pipeline y sales operations | [`labs/part-16/`](../labs/part-16/) |
| 🧪 Laboratorios de la parte 17 — Marketing automation y revenue operations | [`labs/part-17/`](../labs/part-17/) |
| ✅ Evaluación de la parte 16 | [`assessments/part-16-assessment.md`](../assessments/part-16-assessment.md) |
| ✅ Evaluación de la parte 17 | [`assessments/part-17-assessment.md`](../assessments/part-17-assessment.md) |
| 📋 Rúbricas y criterios | [`docs/EVALUACION-Y-RUBRICAS.md`](../docs/EVALUACION-Y-RUBRICAS.md) |
| 📂 Estándar de evidencia | [`docs/ESTANDAR-DE-EVIDENCIA.md`](../docs/ESTANDAR-DE-EVIDENCIA.md) |

## 📥 Artefactos que acreditan este rol

Estos son los entregables que conviene llevar a una postulación. No describen responsabilidades: muestran trabajo que alguien puede auditar.

- [ ] Diseño de sales operations con pipeline, criterios y gobierno
- [ ] Operating model de RevOps con cifra única por indicador
- [ ] Acuerdo de servicio entre marketing y ventas con cumplimiento medido
- [ ] Modelo de datos con fuente autoritativa declarada por campo

## 🎓 Credenciales y señales de mercado

- **Salesforce Administrator / HubSpot Operations** — sí pesan en este rol, porque acreditan operación real de la plataforma.
- **SQL** — no hay credencial, pero se evalúa en entrevista.
- **Portafolio** — un modelo de datos y un diseño de pipeline documentados demuestran criterio.

## 📈 Progresión de carrera y rangos

Sales ops o marketing ops → **RevOps manager** → head of revenue operations → [CRO](cro.md) o dirección de operaciones. Es uno de los caminos más directos hacia la dirección comercial para perfiles no vendedores.

Rangos **orientativos y aproximados**. Varían mucho por sector, tamaño de empresa, industria y experiencia; son referencia de mercado, no promesa:

```text
Región                      Con 3–5 años          Senior / liderazgo
--------------------------  --------------------  ------------------------
Chile                       CLP 1,8M – 2,8M/mes   CLP 3,2M – 5,0M/mes
LATAM (regional)            USD 1.800 – 3.200/mes USD 3.500 – 6.000/mes
España                      EUR 33k – 45k/año     EUR 48k – 70k/año
Remoto (USD)                USD 55k – 90k/año     USD 95k – 150k/año
```

## ⚠️ Mitos y errores comunes

| Mito | Realidad |
|---|---|
| «Es administrar el CRM.» | Administrar la herramienta es el 30 %. El resto son definiciones, acuerdos y gobierno. |
| «Más automatización es mejor.» | Automatizar un proceso desordenado produce desorden a escala. Primero estandarizar. |
| «El forecast es un cálculo.» | Es consecuencia de la disciplina de calificación. Ningún método corrige criterios de etapa débiles. |
| «Los conflictos entre áreas se arreglan con datos.» | Los datos hacen visible el conflicto de incentivos; resolverlo exige cambiar la compensación. |

## ⚖️ Nota de honestidad

El programa entrega el diseño completo del sistema. No entrega experiencia administrando una instancia real de Salesforce o HubSpot con miles de registros, que es lo que muchas ofertas piden. Complementa con la certificación de administrador de la plataforma que uses.

> El programa **no certifica ni garantiza empleo**. Acredita evidencia de trabajo: los artefactos son la credencial y deben poder defenderse ante preguntas técnicas.

---

[⬅ Todas las rutas](README.md) · [Currículo](../curriculum/README.md) · [Ruta de aprendizaje](../docs/RUTA-DE-APRENDIZAJE.md) · [Programa](../README.md)
