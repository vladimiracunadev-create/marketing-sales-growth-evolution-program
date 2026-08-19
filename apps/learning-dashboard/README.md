---
title: "Panel local de progreso"
type: app
language: es
updated: 2026-08-18
---

# Panel local de progreso

Panel de seguimiento del programa que funciona en el navegador, sin dependencias, sin servidor y sin envío
de datos.

## Uso

```bash
# Opción 1: abrir el archivo directamente
#   apps/learning-dashboard/index.html

# Opción 2: servirlo, para que lea los títulos reales del currículo
python -m http.server 8000
# luego abrir http://localhost:8000/apps/learning-dashboard/
```

## Qué registra

| Elemento | Por parte | Total |
|---|---:|---:|
| Clases | 14 | 336 |
| Laboratorios | 2 | 48 |
| Evaluación aprobada | 1 | 24 |

El avance total pondera clases (60 %), laboratorios (30 %) y evaluaciones (10 %). Una parte se considera
completa sólo cuando sus catorce clases, sus dos laboratorios y su evaluación están registrados: es el mismo
criterio de avance descrito en [`docs/RUTA-DE-APRENDIZAJE.md`](../../docs/RUTA-DE-APRENDIZAJE.md).

La estimación de horas usa 2,5 horas por clase, 4 por laboratorio y 2 por evaluación.

## Privacidad

- El avance se guarda en `localStorage` de tu navegador.
- No hay cuentas, servidores, cookies de terceros ni telemetría.
- Nada sale de tu equipo, ni siquiera al exportar: el archivo se genera localmente.

Para trasladar tu avance a otro equipo, usa **Exportar avance** y luego **Importar avance**. El archivo es
un JSON legible que puedes revisar antes de importarlo.

## Accesibilidad

- Operable por teclado, con enlace para saltar al contenido.
- Etiquetas descriptivas en cada control de suma y resta.
- Región de estado anunciada para los mensajes de confirmación.
- Tema claro, oscuro y según el sistema.
- Hoja de estilo de impresión para llevar el avance en papel.

## Límite

El panel registra lo que tú declaras. No verifica que hayas producido la evidencia ni que hayas aprobado las
evaluaciones: eso lo determina la rúbrica, no el contador.

---

[⬅ Programa](../../README.md) · [Ruta de aprendizaje](../../docs/RUTA-DE-APRENDIZAJE.md)
