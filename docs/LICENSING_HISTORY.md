# Historia de licenciamiento

Este documento conserva la cadena de decisiones de licencia sin reescribir el pasado.

## Evidencia histórica

| Fecha | Referencia | Estado de licencia |
|---|---|---|
| 2026-08-18 | Commit raíz `9ae187851b9774a1f2fd3f072e658d1b3f26bd58` | Se incorporó `LICENSE` con MIT para el repositorio, sin titular escrito después del año. |
| 2026-08-19 | Tag publicado `v1.0.0` en `691bdb36e85f01b36d1f132f78b359eb4944f6c5` | La versión se publicó bajo el aviso MIT entonces vigente. |
| 2026-08-19 | `7a80d8efc1054f4d2c3366e1ab03f0c21bc58920` | Último commit anterior a la separación; README declaraba MIT para código y contenido original. |
| 2026-09-22 | Commit que introduce `LICENSE-CONTENT.md` | Se identifica al titular, MIT queda para software y CC BY-NC-SA 4.0 se aplica prospectivamente al contenido educativo original. |

El commit de transición se obtiene de forma reproducible con:

```bash
git log --diff-filter=A --format="%H %ad %s" --date=iso-strict -- LICENSE-CONTENT.md
```

## Preservación de permisos anteriores

El cambio actual no revoca ni reduce la licencia MIT que acompañó copias y revisiones ya publicadas. En
particular, `v1.0.0` y todos los commits anteriores al commit de transición siguen disponibles bajo los
términos que los acompañaban.

Cuando un contenido idéntico ya estaba disponible en una revisión histórica bajo MIT, quien obtuvo esa copia
puede seguir usando esa revisión conforme a MIT. CC BY-NC-SA 4.0 gobierna la distribución actual del contenido
original y las aportaciones posteriores cubiertas, sin borrar los permisos históricos.

## Titular identificado

La auditoría del historial encontró un único autor y committer en todas las referencias disponibles:

```text
23  Vladimir Acuña <vladimir.acuna.dev@gmail.com>
```

Los 23 commits conservan además el trailer
`Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. Se registra como asistencia de una herramienta de IA,
no como una segunda persona titular. La auditoría explica esta clasificación, la política pública del proveedor
y sus límites.

El remoto canónico pertenece a `vladimiracunadev-create`. Con esa evidencia se normalizó el aviso a:

```text
Copyright © 2026 Vladimir Acuña
Cuenta de publicación: vladimiracunadev-create
```

Los comandos y límites de esta conclusión están documentados en [`../LICENSING_AUDIT.md`](../LICENSING_AUDIT.md).

## Política futura

- Software nuevo: MIT, salvo aviso específico compatible y documentado.
- Contenido educativo original nuevo: CC BY-NC-SA 4.0.
- Material externo: conserva los derechos y condiciones de su titular; se cita, no se relicencia.
- Cualquier excepción debe declararse junto al archivo y añadirse a `THIRD_PARTY_NOTICES.md`.

---

[⬅ Documentación](README.md) · [Uso comercial](COMMERCIAL_USE.md)
