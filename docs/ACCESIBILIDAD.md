# Accesibilidad

Compromisos de accesibilidad del material, decisiones tomadas y limitaciones conocidas.

## 1. Compromiso

El material debe poder usarse con lector de pantalla, con navegación por teclado, con visión reducida y en
condiciones de conectividad limitada. Estas no son características añadidas: son restricciones de diseño del
repositorio.

## 2. Decisiones de contenido

| Decisión | Razón |
|---|---|
| Todo el contenido en Markdown plano | Legible por lector de pantalla sin capa intermedia |
| Jerarquía de encabezados sin saltos | Permite navegación estructural con lector de pantalla |
| Tablas con encabezado explícito | Asocia cada celda con su columna |
| Enlaces con texto descriptivo | Evita «haz clic aquí», que no informa fuera de contexto |
| Sin dependencia del color para transmitir significado | Funciona en monocromo y con daltonismo |
| Diagramas Mermaid acompañados de texto | El contenido no se pierde si el diagrama no se renderiza |
| Sin recursos externos en el sitio | Funciona sin conexión y sin bloqueadores |

## 3. Decisiones del sitio HTML

| Decisión | Efecto |
|---|---|
| HTML semántico (`nav`, `main`, `article`, `footer`) | Navegación por regiones con lector de pantalla |
| Enlace «saltar al contenido» | Evita recorrer la navegación en cada página |
| Contraste mínimo AA en ambos temas | Legibilidad con visión reducida |
| Tema claro y oscuro según preferencia del sistema | Reduce fatiga visual |
| Tipografía del sistema, tamaño base 17 px | Legible sin descargar fuentes |
| Ancho de línea máximo de 74 caracteres | Facilita el seguimiento de línea |
| Buscador operable por teclado | No requiere puntero |
| Hoja de estilo de impresión | Permite estudiar en papel |
| Sin JavaScript obligatorio para leer | El contenido se lee aunque el script falle |

## 4. Diseño de las evaluaciones

- Las rúbricas se publican antes del trabajo: reduce la carga cognitiva de adivinar el criterio.
- Las evaluaciones son de respuesta construida, sin límite de tiempo estricto.
- Los formatos de sesión de 45, 90 y 150 minutos permiten adaptar la carga.
- Los entregables aceptan formato escrito, tabla o cálculo: no se exige un único medio.

## 5. Lenguaje

- Español neutro, con la variante chilena sólo donde el contexto normativo lo exige.
- Se evita la jerga innecesaria; los anglicismos usuales del dominio se conservan pero se definen.
- Frases directas y párrafos cortos.
- Los conceptos se definen antes de usarse.

## 6. Limitaciones conocidas

| Limitación | Estado |
|---|---|
| Diagramas Mermaid sin descripción textual completa | Parcial: cada diagrama tiene contexto en prosa, no descripción exhaustiva |
| Notebooks con salidas gráficas | Requieren lectura de código para interpretar sin visión |
| Sin versión en audio | No disponible |
| Sin subtítulos ni video | El programa no incluye material audiovisual |
| Sin traducción a otros idiomas | Sólo español |

Estas limitaciones están declaradas, no resueltas. Ver [`../ROADMAP.md`](../ROADMAP.md) para el estado de las
mejoras planificadas.

## 7. Cómo reportar un problema de accesibilidad

Abre un issue indicando:

- qué página o archivo;
- qué tecnología de asistencia y versión;
- qué esperabas y qué ocurrió;
- si conoces una corrección posible.

Los reportes de accesibilidad tienen prioridad sobre las mejoras de contenido.

## 8. Verificación

```bash
python tools/build_site.py     # regenera el sitio
python tools/check_links.py    # verifica enlaces internos
```

Para verificación manual del sitio: navega una página completa sólo con teclado y recórrela con un lector de
pantalla. Si se pierde el orden o falta contexto, es un defecto.

---

[⬅ Documentación](README.md) · [Plan de capacitación](PLAN-DE-CAPACITACION.md)
