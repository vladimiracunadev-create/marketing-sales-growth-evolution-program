# Auditoría de copyright y licencias

**Repositorio:** `vladimiracunadev-create/marketing-sales-growth-evolution-program`

**Fecha de corte:** 2026-09-22

**HEAD auditado:** `7a80d8efc1054f4d2c3366e1ab03f0c21bc58920`

## Resultado

La evidencia disponible permite atribuir la autoría histórica del repositorio a **Vladimir Acuña**, publicado
desde la cuenta **`vladimiracunadev-create`**. Se corrige el aviso incompleto, se separa software de contenido
educativo y se preservan expresamente los permisos MIT de las revisiones anteriores.

## Pruebas ejecutadas

```bash
git shortlog -sne --all
git log --all --format="%an <%ae>"
git log --all --format="%(trailers:key=Co-Authored-By,valueonly)"
git log --follow --patch -- LICENSE
git remote -v
git tag --format="%(refname:short) %(objectname) %(subject)"
git grep -n -I -E "MIT License|licencia MIT|contenido bajo licencia MIT"
```

Resultados relevantes:

- 23 de 23 commits en todas las referencias locales tienen como autor y committer a
  `Vladimir Acuña <vladimir.acuna.dev@gmail.com>`;
- los 23 commits incluyen el trailer
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`, que registra asistencia de una herramienta de IA y
  no identifica a otra persona natural que haya confirmado un aporte o reclamado titularidad;
- `origin` apunta a `github.com/vladimiracunadev-create/marketing-sales-growth-evolution-program`;
- `LICENSE` fue creado en el commit raíz por Vladimir Acuña con `Copyright (c) 2026`, sin nombre;
- el tag `v1.0.0` apunta al commit `691bdb36e85f01b36d1f132f78b359eb4944f6c5` y contiene el MIT original;
- antes de esta corrección, README, FAQ, plan de capacitación, portal y panel describían MIT como licencia
  global del contenido.

## Decisiones

1. **Titular:** normalizar a `Copyright © 2026 Vladimir Acuña`; conservar
   `vladimiracunadev-create` como identificador de la cuenta de publicación. El trailer de Claude se conserva
   íntegro en el historial y se documenta como asistencia de IA. La política pública actual de Anthropic
   indica que sus clientes conservan los derechos sobre sus entradas y son propietarios de sus salidas; no se
   encontró en el repositorio una reclamación distinta del proveedor.
2. **Software:** mantener MIT en `LICENSE` para código, configuración ejecutable y herramientas.
3. **Contenido original:** aplicar CC BY-NC-SA 4.0 prospectivamente mediante `LICENSE-CONTENT.md`.
4. **Materiales mixtos:** MIT cubre el código identificable; CC BY-NC-SA 4.0 cubre el texto educativo original.
5. **Terceros:** excluirlos de ambas concesiones propias y remitir al registro verificable de 97 obras.
6. **Historia:** no modificar tags ni commits publicados y documentar que las concesiones MIT anteriores
   continúan vigentes.
7. **Marcas y comercio:** separar derechos de marca y explicar que el código MIT y el contenido NC tienen
   permisos comerciales distintos.

## Superficies corregidas

- `LICENSE` y nuevo `LICENSE-CONTENT.md`;
- README y badge de licencia;
- FAQ, plan de capacitación, índice documental y reglas de contribución;
- pie del portal generado y panel de aprendizaje;
- control de licencia del workflow de seguridad;
- nuevos avisos de terceros, marcas, historia y uso comercial.

## Límites de la auditoría

Los metadatos Git y los trailers demuestran una historia técnica coherente, pero no son una prueba
criptográfica de identidad civil, de autoría humana sobre cada fragmento ni del contrato concreto bajo el que
se usó Claude; tampoco sustituyen una revisión jurídica. La conclusión de titularidad se limita a los derechos
que Vladimir Acuña efectivamente posea. La auditoría no determina la registrabilidad de marcas ni resuelve por
sí sola todos los derechos sobre cada método externo; por eso esos elementos quedan excluidos y vinculados a
sus fuentes.

Referencia del proveedor consultada el 2026-09-22:
[Anthropic Transparency Hub](https://www.anthropic.com/transparency/voluntary-commitments).

## Verificación requerida antes de publicar

```bash
python tools/validate_repository.py
python tools/validate_depth.py
python tools/audit_fuentes.py
python scripts/verify_sources.py
python tools/check_links.py
python -m pytest -q
python tools/build_site.py --limpiar
python tools/validate_site.py
```

La auditoría se completa sólo cuando estas comprobaciones, la reproducibilidad de generadores y los workflows
remotos terminan en verde.
