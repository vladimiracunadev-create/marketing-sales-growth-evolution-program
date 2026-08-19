# Política de seguridad

## Alcance

Este repositorio es material educativo: contenido en Markdown, scripts de generación en Python que usan sólo
la biblioteca estándar, notebooks de analítica y un sitio HTML estático sin dependencias externas. No hay
servicios en ejecución, autenticación ni datos de personas reales.

Aun así, hay superficies que importan y que se revisan:

| Superficie | Riesgo | Control |
|---|---|---|
| Scripts de `tools/` | Ejecución de código al construir el material | Sólo biblioteca estándar; sin red ni ejecución dinámica |
| Notebooks | Ejecución al abrirlos | Sin llamadas externas; datos locales sintéticos |
| Sitio generado | Contenido activo en el navegador | HTML autocontenido, sin recursos ni scripts externos |
| Flujos de integración continua | Ejecución con permisos del repositorio | Permisos mínimos y acciones fijadas por versión |
| Datos | Exposición de datos personales | Todos los conjuntos son sintéticos |

## Versiones con soporte

| Versión | Estado |
|---|---|
| 2.x | Con soporte |
| 1.x | Sin soporte |

## Cómo reportar una vulnerabilidad

Si encuentras un problema de seguridad:

1. **No abras un issue público** si el problema podría explotarse.
2. Usa el canal privado de reporte de seguridad de GitHub en este repositorio
   («Security» → «Report a vulnerability»).
3. Incluye: qué componente afecta, cómo reproducirlo, qué impacto tiene y, si la conoces, una corrección
   posible.

**Compromiso de respuesta:** acuse de recibo dentro de 5 días hábiles y evaluación inicial dentro de 15 días
hábiles.

## Qué no es una vulnerabilidad de este repositorio

- Errores de contenido educativo. Repórtalos como issue normal; ver [CONTRIBUTING.md](CONTRIBUTING.md).
- Enlaces rotos a sitios de terceros.
- Desactualización normativa. Es un error de contenido y tiene su propio procedimiento de corrección
  prioritario.
- Problemas de dependencias que este repositorio no usa.

## Datos y privacidad

- Los conjuntos en `datasets/` son **sintéticos**. No contienen datos de personas ni de empresas reales.
- El repositorio no recolecta telemetría ni analítica de uso.
- El sitio generado no incluye rastreadores, cookies ni recursos de terceros.
- No subas datos reales de tu organización a este repositorio. La carpeta `evidence/private/` está excluida
  del control de versiones para trabajo local que no debe publicarse.

## Buenas prácticas al usar el material

- Ejecuta los notebooks en un entorno virtual aislado.
- No pegues datos de clientes en herramientas externas sin verificar la política de tratamiento; ver
  [`docs/DATOS-PERSONALES-Y-ETICA.md`](docs/DATOS-PERSONALES-Y-ETICA.md).
- Si adaptas el caso persistente a tu empresa, anonimiza antes de compartir.

## Divulgación

Las correcciones de seguridad se documentan en [CHANGELOG.md](CHANGELOG.md) una vez publicadas. Se agradece
la divulgación coordinada.
