---
title: "Preguntas frecuentes"
type: faq
language: es
updated: 2026-08-18
---

# Preguntas frecuentes

## Sobre el programa

**¿Para quién es este programa?**
Para quien quiere construir criterio comercial verificable: personas que entran a marketing o ventas,
especialistas que quieren dirigir, emprendedores que necesitan vender y equipos que quieren un estándar
común. No requiere formación previa formal.

**¿Cuánto tiempo toma?**
La ruta completa son aproximadamente 1.256 horas de trabajo real. A 8 horas semanales, unos tres años; a 20
horas semanales, unos quince meses. Las rutas parciales están descritas en
[`RUTA-DE-APRENDIZAJE.md`](RUTA-DE-APRENDIZAJE.md).

**¿Entrega certificado?**
No. Lo que entrega es evidencia de trabajo: artefactos que pueden mostrarse y defenderse. Esa es
deliberadamente la credencial, porque es la que un empleador puede evaluar.

**¿Sirve fuera de Chile?**
El contenido conceptual es general. El contexto normativo es chileno y está marcado como tal en cada clase.
Para otra jurisdicción, el marco de análisis se conserva y las referencias legales deben sustituirse.

**¿Necesito herramientas de pago?**
No. Los generadores y validadores usan sólo la biblioteca estándar de Python. El sitio HTML no requiere
dependencias. Los notebooks usan bibliotecas de análisis de datos habituales y gratuitas.

## Sobre el contenido

**¿Por qué el contenido está generado y no escrito clase por clase?**
Porque 336 documentos editados a mano derivan: estructuras distintas, métricas inconsistentes, bibliografía
divergente. Generarlos desde una especificación garantiza que todos cumplan el mismo estándar y que un cambio
de definición se propague al glosario, al laboratorio y a la evaluación. La sustancia —tesis, conceptos,
método, casos, límites— está escrita a mano en `curriculum/spec/`.

**¿Puedo editar una clase directamente?**
No, se pierde en la siguiente generación. Edita `curriculum/spec/` y ejecuta los generadores. Ver
[`ARQUITECTURA-DEL-PROGRAMA.md`](ARQUITECTURA-DEL-PROGRAMA.md).

**¿Por qué se cita bibliografía que no se incluye?**
Porque distribuir obras protegidas sería ilícito. El programa cita, explica qué lente aporta cada obra y
enseña a leerlas de forma selectiva. El acceso se obtiene por biblioteca, editorial o suscripción legítima.

**¿Los datos son reales?**
No. Los conjuntos en `datasets/` son sintéticos y así se declaran. Permiten ejercicios reproducibles sin
comprometer datos de personas ni de empresas.

**¿La empresa del caso existe?**
No. **Ruta Andina SpA** es una simulación diseñada para recorrer venta B2B recurrente, comercio electrónico,
marketplace y venta al sector público sin cambiar de contexto.

## Sobre el estudio

**¿Puedo saltarme partes?**
Sí, con costo. Las rutas parciales están documentadas junto con lo que dejan fuera y cuándo conviene
retomarlo.

**¿Cuánto dura una clase?**
150 minutos de trabajo real: lectura, ficha de medición, ejemplo trabajado y caso. Leerla en 20 minutos
produce reconocimiento, no capacidad.

**¿Cómo sé si aprendí?**
Si puedes: distinguir los conceptos por sus observables, operacionalizar la métrica principal, resolver el
caso con dos alternativas y declarar qué evidencia te haría cambiar de opinión.

**¿Qué hago si repruebo una evaluación?**
Identifica el bloque bajo el 60 %, vuelve a las clases correspondientes, rehaz el entregable y repite. El
criterio de avance existe porque las partes posteriores suponen las anteriores.

**¿Puedo usar IA para los entregables?**
Sí, declarándolo. Toda afirmación factual generada debe verificarse en fuente primaria. La regla completa
está en [`EVALUACION-Y-RUBRICAS.md`](EVALUACION-Y-RUBRICAS.md).

## Sobre la enseñanza

**¿Puedo usar esto para capacitar?**
Sí. El contenido original está bajo licencia MIT con atribución. Ver
[`PLAN-DE-CAPACITACION.md`](PLAN-DE-CAPACITACION.md) para formatos de sesión y migración a plataforma.

**¿Cómo lo llevo a un LMS?**
Genera el sitio HTML, usa `curriculum/curriculum.json` como árbol de importación y mapea parte → módulo,
clase → lección, laboratorio → tarea. El procedimiento completo está en el plan de capacitación.

**¿Puedo reemplazar el caso persistente por mi empresa?**
Sí, con dos condiciones: que el caso propio tenga restricciones reales y que se mantenga la acumulación entre
partes. Verifica el tratamiento de datos personales antes de usar información real.

**¿Sirve para educación técnico-profesional?**
Sí, con el formato de sesión de 90 minutos y más práctica guiada. La adaptación por audiencia está en el plan
de capacitación.

## Sobre el repositorio

**¿Cómo verifico que el programa cumple lo que declara?**

```bash
python tools/validate_repository.py
python tools/validate_depth.py
python -m pytest -q
```

El [manifiesto](../MANIFEST.md) cuenta archivos reales, no cifras declaradas a mano.

**¿Cómo contribuyo?**
Ver [`CONTRIBUTING.md`](../CONTRIBUTING.md). Las correcciones de exactitud normativa y los reportes de
accesibilidad tienen prioridad.

**¿Encontré un error normativo, qué hago?**
Abre un issue con la fuente oficial que lo contradice y la fecha de consulta. La regla del programa es que la
fuente oficial manda sobre el material pedagógico.

**¿Con qué frecuencia se actualiza?**
La revisión normativa es al menos anual. El contenido conceptual se actualiza cuando aparece evidencia que
contradice lo enseñado. Ver [`../CHANGELOG.md`](../CHANGELOG.md).

## Límites del programa

**¿Esto reemplaza asesoría legal, tributaria o financiera?**
No. Enseña a identificar obligaciones y a verificarlas en su fuente. Toda operación real requiere revisión
profesional.

**¿Garantiza resultados comerciales?**
No. Ningún programa puede hacerlo. Lo que ofrece es criterio para decidir mejor y evidencia para sostener las
decisiones.

**¿Sustituye la experiencia?**
No. La acelera y la ordena. Un caso simulado con restricciones no equivale a haber perdido dinero real, pero
enseña a reconocer el patrón antes de perderlo.

---

[⬅ Documentación](README.md) · [Programa](../README.md)
