# Estándar de evidencia

Qué cuenta como evidencia en este programa, cómo se organiza y cómo se audita. Este estándar aplica a
clases, laboratorios, proyectos y Capstone.

## 1. Jerarquía de evidencia

No toda afirmación tiene el mismo respaldo. El programa exige clasificar explícitamente:

| Nivel | Qué es | Cómo se marca |
|---|---|---|
| **Hecho verificado** | Dato con fuente, periodo y método conocidos | `[H]` + fuente |
| **Observación** | Registro directo de un comportamiento o evento | `[O]` + cuándo y dónde |
| **Inferencia** | Conclusión derivada de hechos, con razonamiento explícito | `[I]` + razonamiento |
| **Supuesto** | Afirmación no verificada de la que depende la conclusión | `[S]` + plan de validación |
| **Opinión** | Juicio sin respaldo, admisible si se declara como tal | `[P]` |

Un entregable que no distingue estos niveles no cumple el estándar, aunque sus conclusiones sean correctas.

## 2. Estructura de la carpeta de evidencia

```text
evidence/
├── P01-C01-marketing-ventas-y-crecimiento-como-sistema/
│   ├── decision-brief.md
│   ├── ficha-metricas.md
│   ├── nota-de-lectura.md
│   └── red-team.md
├── P01-LAB-1/
│   ├── memo-decision.md
│   ├── calculo.md
│   ├── ficha-metricas.md
│   ├── escenario-adverso.md
│   └── riesgo-y-cumplimiento.md
├── P01-EVAL/
│   └── evaluacion-parte-01.md
└── portfolio/
    └── 01-mapa-del-sistema-comercial.md
```

Convención: `P<parte>-C<clase>-<slug>` para clases, `P<parte>-LAB-<n>` para laboratorios, `P<parte>-EVAL`
para evaluaciones.

> `evidence/private/` está excluido del control de versiones. Úsalo para material que no debe publicarse.

## 3. Anatomía de un decision brief

Todo entregable de decisión contiene, en este orden:

```markdown
# <Decisión en una frase>

## Recomendación
<Qué se propone hacer, en dos líneas, al inicio del documento>

## Contexto y problema
<Qué está en juego y por qué ahora>

## Evidencia
| Afirmación | Nivel | Fuente | Fecha |
|---|---|---|---|

## Supuestos críticos
| Supuesto | De qué depende | Cómo se validaría | Costo de validar |
|---|---|---|---|

## Alternativas
| Opción | Beneficio esperado | Costo | Riesgo | Reversibilidad |
|---|---|---|---|---|

## Efecto sobre cliente, operación, caja y riesgo

## Condición de cambio
<Qué información nueva modificaría la recomendación>

## Gobierno
Responsable · Fecha de revisión · Señal de éxito · Condición de detención
```

La recomendación va **al inicio**. Un lector ejecutivo debe encontrarla en los primeros quince segundos.

## 4. Anatomía de una ficha de métricas

```text
Métrica:               <nombre>
Decisión que informa:  <qué se decide con ella>
Numerador:             <qué se cuenta>
Denominador:           <sobre qué base>
Ventana:               <periodo y criterio de corte>
Segmentación:          <cortes obligatorios>
Fuente:                <sistema y campo>
Frecuencia:            <cada cuánto se calcula>
Responsable:           <quién responde por el número>
Línea base:            <valor actual y fecha>
Lectura permitida:     <qué se puede concluir>
Lectura prohibida:     <qué NO se puede concluir>
```

La última línea es la más importante y la que casi nunca se escribe.

## 5. Anatomía de una nota de lectura

```markdown
## <Obra> — <autoría>
**Edición y páginas consultadas:** <referencia exacta>

**Tesis utilizada:** <qué afirma que resulta pertinente al caso>

**Cómo modifica mi diagnóstico:** <cambio concreto>

**Tensión con <otra obra>:** <dónde entregan recomendaciones distintas>

**Decisión que cambia:** <qué haría distinto después de leer>
```

Una nota de lectura sin la última línea no acredita uso.

## 6. Anatomía de un red team

```markdown
## Objeción más fuerte a mi recomendación
<Formulada de la forma más convincente posible, no como hombre de paja>

## Dato que invalidaría mi conclusión
<Qué tendría que ser cierto para que me haya equivocado>

## Efecto de segundo orden que no consideré
<Consecuencia lateral fuera del indicador principal>

## Qué haría si la objeción resulta correcta
<Plan alternativo>
```

El criterio de calidad: si la objeción es fácil de refutar, no se buscó la objeción real.

## 7. Reglas de trazabilidad

1. Toda cifra debe poder rastrearse hasta su fuente en menos de dos pasos.
2. Toda fuente lleva fecha de consulta.
3. Toda norma citada indica su identificador oficial.
4. Todo dato de terceros lleva la autorización que permite usarlo.
5. Todo contenido generado con IA se declara y se indica cómo se verificó.

## 8. Auditoría de evidencia

Un tercero debe poder tomar el entregable y responder, sin consultar al autor:

- [ ] ¿Cuál es la decisión y quién la toma?
- [ ] ¿Qué es hecho y qué es supuesto?
- [ ] ¿De dónde salió cada cifra?
- [ ] ¿Cuál era la alternativa y por qué se descartó?
- [ ] ¿Qué señal indicará si la decisión fue correcta?
- [ ] ¿Qué obligación normativa se verificó?

Si alguna respuesta requiere preguntarle al autor, el entregable no cumple el estándar.

## 9. Del entregable al portafolio

Al cerrar cada parte, selecciona el artefacto que mejor muestra competencia y muévelo a `evidence/portfolio/`
con:

- contexto del problema en tres líneas;
- método aplicado;
- decisiones tomadas y descartadas;
- resultado o, si no lo hubo, qué se aprendió.

Seis artefactos documentados muestran más competencia que veinte incompletos.

---

[⬅ Documentación](README.md) · [Evaluación y rúbricas](EVALUACION-Y-RUBRICAS.md) ·
[Fórmulas y métricas](FORMULAS-Y-METRICAS.md)
