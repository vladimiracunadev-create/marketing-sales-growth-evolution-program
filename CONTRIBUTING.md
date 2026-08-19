# Cómo contribuir

Gracias por considerar contribuir. Este documento explica qué se acepta, cómo se propone un cambio y qué
estándar debe cumplir.

## Prioridades

Las contribuciones se atienden en este orden:

1. **Correcciones de exactitud normativa.** Si una afirmación legal está desactualizada o es incorrecta, es
   la prioridad más alta. La regla del programa es que la fuente oficial manda sobre el material pedagógico.
2. **Reportes de accesibilidad.** Un problema que impide usar el material con tecnología de asistencia tiene
   prioridad sobre cualquier mejora de contenido.
3. **Errores de contenido.** Definiciones incorrectas, métricas mal formuladas, citas erróneas.
4. **Mejoras de profundidad.** Casos más ricos, límites mejor formulados, bibliografía adicional pertinente.
5. **Mejoras de herramientas.** Generadores, validadores, sitio.

## Regla fundamental: no edites el Markdown generado

> El contenido de `curriculum/part-*/`, `labs/`, `assessments/`, `cases/`, `projects/`, `capstone/` y los
> documentos marcados con `generated: true` **se generan** desde `curriculum/spec/`. Editarlos a mano se
> pierde en la siguiente ejecución.

Para cambiar contenido:

```bash
# 1. Editar la especificación
#    curriculum/spec/clases_pNN.py     una clase
#    curriculum/spec/partes.py         una parte
#    curriculum/spec/bibliografia.py   una obra

# 2. Regenerar
python tools/build_curriculum.py
python tools/build_practica.py
python tools/build_docs.py

# 3. Validar
python tools/validate_repository.py
python tools/validate_depth.py
python -m pytest -q
```

## Estándar de contenido

Toda contribución de contenido debe cumplir el estándar
[`clase-profunda-v3`](docs/ESTANDAR-PEDAGOGICO.md):

- **Definición operacional.** Un concepto entra sólo si dos personas independientes pueden clasificar el
  mismo caso de la misma forma con esa definición.
- **Ficha de medición.** Toda métrica declara numerador, denominador y ventana temporal.
- **Frontera de aplicación.** Todo método declara cuándo deja de funcionar o produce daño.
- **Trade-off explícito.** Todo problema de decisión ofrece al menos dos alternativas defendibles.
- **Fuente verificable.** Toda afirmación normativa o factual cita su fuente con fecha de consulta.

Una contribución que no cumple alguno de estos puntos se devuelve con la indicación específica.

## Idioma y estilo

- **Español.** Todo el contenido del programa está en español. Los anglicismos habituales del dominio se
  conservan cuando son el término de uso profesional, pero se definen.
- **Frases directas.** Sujeto, verbo, complemento. Evita la voz pasiva innecesaria.
- **Sin relleno.** Si un párrafo no cambia lo que el lector puede hacer, se elimina.
- **Sin superlativos.** «Aumenta la conversión» requiere evidencia; «revoluciona el marketing» no dice nada.

## Cómo proponer un cambio

### Para un error normativo

Abre un issue con:

- qué afirma el material y dónde (ruta y línea);
- qué dice la fuente oficial;
- enlace a la fuente y fecha de consulta.

### Para un error de contenido

Abre un issue con:

- qué afirma el material y dónde;
- por qué es incorrecto;
- referencia que lo respalde, si existe.

### Para una mejora

1. Abre un issue describiendo el cambio antes de escribir código o contenido.
2. Si hay acuerdo, crea una rama: `mejora/descripcion-corta`.
3. Edita la especificación, regenera y valida.
4. Abre un pull request que incluya:
   - qué problema resuelve;
   - qué archivos de especificación se modificaron;
   - salida de los validadores;
   - confirmación de que el Markdown generado se regeneró.

## Bibliografía

Para proponer una obra nueva:

- debe aportar un **lente** distinto al de las obras ya citadas;
- debe indicarse en qué clases se usaría y para qué;
- se agrega en `curriculum/spec/bibliografia.py` con autoría, obra, edición de referencia, lente y categoría.

No se aceptan obras citadas por prestigio si no cambian el análisis de alguna clase.

## Datos

- Los conjuntos en `datasets/` son sintéticos y deben seguir siéndolo.
- No se aceptan datos de personas ni de empresas reales, aunque estén anonimizados.
- Los generadores de datos deben ser reproducibles y estar documentados.

## Herramientas

- Los generadores y validadores usan **sólo la biblioteca estándar de Python**. Esa restricción es
  deliberada: construir y validar el material no debe exigir instalar nada.
- El sitio generado no puede depender de recursos externos.
- Las pruebas van en `tests/` y deben ejecutarse con `python -m pytest -q`.

## Convención de commits

```text
tipo(alcance): descripción breve en presente

Cuerpo opcional explicando el porqué del cambio.
```

Tipos: `contenido`, `docs`, `tools`, `tests`, `fix`, `chore`.

Ejemplos:

```text
contenido(p07): corregir definición operacional de elasticidad
docs(regulacion): actualizar vigencia de la Ley 21.719
tools(site): agregar buscador operable por teclado
```

## Qué no se acepta

- Contenido promocional de herramientas o servicios.
- Traducciones automáticas sin revisión.
- Afirmaciones normativas sin fuente oficial.
- Reproducción de texto protegido por derechos de autor.
- Casos que promuevan prácticas comerciales engañosas, aunque sea con fines ilustrativos.
- Datos reales de personas o empresas.

## Código de conducta

Toda participación se rige por el [código de conducta](CODE_OF_CONDUCT.md).

## Licencia de las contribuciones

Al contribuir aceptas que tu aporte se publique bajo la licencia [MIT](LICENSE) del repositorio.
