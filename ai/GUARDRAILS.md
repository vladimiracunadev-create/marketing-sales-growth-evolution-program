# Guardarraíles de IA comercial

Reglas operativas para usar sistemas de inteligencia artificial en marketing, ventas y servicio, dentro del
programa y en operaciones reales. Complementan la parte 21 y
[`docs/DATOS-PERSONALES-Y-ETICA.md`](../docs/DATOS-PERSONALES-Y-ETICA.md).

## 1. Principio

> **La responsabilidad no se automatiza.** Ante un error, la empresa responde. El sistema no es una parte a
> la que se pueda trasladar la consecuencia, ni ante un cliente ni ante una autoridad.

## 2. Aprobación humana obligatoria

Ninguna de estas acciones puede ejecutarse sin revisión y aprobación de una persona identificada:

| Acción | Motivo |
|---|---|
| Publicación externa de contenido | Compromete a la empresa ante el mercado y ante la ley del consumidor |
| Comunicación a prospectos o clientes | Genera obligaciones y afecta la reputación |
| Cambios de precio o de condiciones comerciales | Tiene efecto contractual y económico directo |
| Segmentación que use datos personales | Requiere base de licitud y finalidad declarada |
| Compromisos contractuales de cualquier tipo | Obliga jurídicamente a la empresa |
| Conclusiones normativas o legales | Exige verificación en fuente oficial |
| Escritura en sistemas de registro (CRM, facturación) | Altera la fuente de verdad operacional |

## 3. Reglas de contenido

1. **Verificación factual.** Toda afirmación de hecho generada por un sistema debe comprobarse en fuente
   primaria antes de usarse en una decisión o publicarse.
2. **Sin invención de evidencia.** Está prohibido generar investigación de cliente, resultados de campaña,
   testimonios, cifras de mercado o datos de CRM.
3. **Promesas verificables.** Ninguna pieza puede afirmar una capacidad, plazo o resultado que la operación
   no pueda sostener y acreditar.
4. **Declaración de origen.** Se registra qué contenido fue generado o asistido, con qué herramienta y quién
   lo aprobó.

## 4. Reglas de datos

1. **Antes de compartir contexto**, verificar qué categorías de datos pueden salir de la organización.
2. **Anonimizar** cuando el caso de uso no requiera identificación.
3. **No enriquecer** perfiles de personas con datos obtenidos fuera de la finalidad declarada.
4. **Registrar el tratamiento**: qué datos, con qué finalidad, con qué base y por cuánto tiempo.
5. **Decisiones automatizadas** que afecten a personas requieren documentación y supervisión humana.

## 5. Claim Gate para contenido regulado

```text
AI GENERATION → CLAIM EXTRACTION → SOURCE VERIFICATION → FACT CHECK
→ REGULATORY CHECK → HUMAN APPROVAL → PUBLICATION → MONITORING → AUDIT LOG
```

La pieza se bloquea antes de publicar si ocurre cualquiera de estas condiciones:

- un claim no tiene fuente o la fuente no corresponde al producto, población, dosis o resultado;
- el texto o la imagen sugieren aprobación, seguridad, eficacia o autoridad profesional no demostradas;
- aparece un testimonio, identidad, afiliado, dominio o creatividad sin registro verificable;
- falta aprobación clínica, regulatoria o humana exigida por la matriz de riesgo;
- la versión publicada no coincide con la versión aprobada.

Después de publicar, reclamos, reembolsos, infracciones de afiliados, incidentes regulatorios o caída de la
revisión humana activan los umbrales de pausa definidos en el brief. El audit log enlaza claim, evidencia,
versión, aprobador, afiliado, canal, fecha de publicación y fecha de retirada.

## 6. Reglas de agentes que ejecutan acciones

| Regla | Detalle |
|---|---|
| Autoridad acotada | El agente sólo puede ejecutar las acciones enumeradas explícitamente |
| Acciones irreversibles excluidas | Enviar comunicaciones, comprometer condiciones o borrar registros exige aprobación humana |
| Registro completo | Traza de qué hizo, cuándo, sobre qué registro y bajo qué autorización |
| Detención inmediata | Debe existir y estar probado un mecanismo para interrumpir la operación |
| Lista de exclusión respetada | Ninguna acción sobre contactos que solicitaron no ser contactados |

## 7. Gobierno de afiliados

Todo tercero que distribuya marketing en nombre de la empresa debe tener identidad verificada, contrato,
dominios y canales declarados, claims autorizados y prohibidos, creatividades versionadas, aprobación previa,
monitoreo, alertas, reglas de suspensión y un kill switch probado. Externalizar marketing no externaliza la
responsabilidad de gobernarlo.

## 8. Prácticas prohibidas

- Correo no solicitado masivo sin base de licitud.
- Persuasión engañosa, urgencia artificial y patrones oscuros.
- Testimonios, reseñas o casos falsos.
- Enriquecimiento de datos personales sin autorización.
- Conclusiones legales presentadas como definitivas sin verificación.
- Publicación de contenido generado sin control de afirmaciones.
- Uso de datos de clientes en herramientas externas sin evaluación previa.
- Imágenes o personajes que aparenten una credencial médica no verificable.
- Equiparar un medicamento compuesto con uno falsificado o insinuar aprobación inexistente.

## 9. Evaluación antes de desplegar

Ningún sistema entra en producción sin:

- [ ] Conjunto de evaluación con casos representativos y resultado esperado.
- [ ] Umbral de aceptación definido **antes** de medir.
- [ ] Guardarraíles implementados sobre los riesgos identificados.
- [ ] Responsable humano nombrado.
- [ ] Monitoreo posterior con alerta.
- [ ] Registro de incidentes habilitado.

## 10. Uso de IA en los entregables del programa

Permitido y sujeto a declaración:

```markdown
## Declaración de uso de IA
- Herramienta y versión:
- Qué se generó o asistió:
- Cómo se verificó:
- Qué se descartó por no poder verificarse:
```

Un entregable con afirmaciones generadas y no verificadas se considera insuficiente, con independencia de su
calidad de redacción.

## 11. Ante un incidente

1. Detener el sistema.
2. Evaluar alcance: qué salió, a quién llegó, qué consecuencia tiene.
3. Reparar el efecto sobre las personas afectadas.
4. Comunicar a los afectados y, cuando corresponda, a la autoridad.
5. Documentar causa raíz y el control que impide la repetición.

---

[⬅ Parte 21](../curriculum/part-21-ia-aplicada-a-marketing-ventas-y-servicio/README.md) ·
[Ética y datos](../docs/DATOS-PERSONALES-Y-ETICA.md) · [Programa](../README.md)
