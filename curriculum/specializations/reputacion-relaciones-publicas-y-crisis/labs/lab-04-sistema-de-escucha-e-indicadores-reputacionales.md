# Laboratorio 04 — Sistema de escucha social e indicadores reputacionales

[⬅ Anterior](lab-03-matriz-de-partes-interesadas-y-mapa-de-controversias.md) · [Especialización](../README.md) · [Siguiente ➡](lab-05-protocolo-de-crisis-y-plantillas-de-declaracion.md)

## 🎯 Objetivo

Diseñar un sistema de escucha con consultas, umbrales de alerta, revisión humana e indicadores reputacionales con ficha completa.

## 📌 Contexto

Diseñar un sistema de escucha obliga a decidir qué se quiere saber y qué se hará con lo que se descubra. Las doscientas menciones sintéticas del laboratorio mezclan críticas reales, consultas, rumores, abuso y cuentas anómalas, de modo que la clasificación tenga consecuencias. Los cinco indicadores se completan con ficha entera para que nadie confunda una cifra con una conclusión.

## 🧰 Insumos

- Un conjunto sintético de 200 menciones con fecha, plataforma, antigüedad de la cuenta y tema.
- Lista de términos de la marca, productos, ejecutivos y variantes de escritura.
- [Indicadores reputacionales](../../../../templates/reputation/indicadores-reputacionales.csv).

## 🪜 Procedimiento

1. Define consultas incluyendo variantes, errores comunes y exclusiones
2. Clasifica las 200 menciones en crítica legítima, consulta, rumor, abuso y posible amplificación artificial
3. Fija umbrales de volumen, velocidad y severidad que activan revisión humana
4. Verifica una muestra de alertas contra registros internos
5. Completa cinco indicadores con numerador, denominador, ventana, fuente y responsable
6. Define qué decisión cambia cada indicador

## 🗂️ Datos de práctica

Datos sintéticos de práctica: 200 menciones en 48 horas. Volumen típico de 8 por hora y pico de 60. Composición verificada: 26 críticas con comprobante, 31 consultas, 47 rumores sin evidencia, 18 abusos y 78 menciones de 12 cuentas creadas hace menos de siete días. Los reclamos internos de soporte muestran 5 cobros duplicados confirmados en las mismas 48 horas.

## 📥 Entregable

Sistema de escucha documentado con umbrales y cinco indicadores con ficha completa.

## 📏 Criterios de calidad

- Los umbrales combinan al menos dos variables.
- Las alertas críticas pasan por verificación humana.
- Los indicadores declaran su limitación.
- Se reconoce lo que el sistema no puede detectar.

### Lectura por niveles de logro

| Criterio | Logrado | Por mejorar |
|---|---|---|
| Los umbrales combinan al menos dos variables | se cumple y deja evidencia en el entregable | se declara sin evidencia o no aparece |
| Las alertas críticas pasan por verificación humana | se cumple y deja evidencia en el entregable | se declara sin evidencia o no aparece |
| Los indicadores declaran su limitación | se cumple y deja evidencia en el entregable | se declara sin evidencia o no aparece |
| Se reconoce lo que el sistema no puede detectar | se cumple y deja evidencia en el entregable | se declara sin evidencia o no aparece |

## ⏱️ Agenda de trabajo

Reserva unos 120 minutos: 15 para leer el contexto y los datos, 60 para el procedimiento, 25 para redactar el entregable y 20 para contrastarlo con la solución orientadora y registrar qué corregirías.


## 🗝️ Solución orientadora

Un sistema útil emite alerta cuando el volumen supera tres veces la mediana horaria y al menos una mención describe un perjuicio verificable. Revisa manualmente las menciones críticas y registra precisión de alertas. Reconoce que ironía y modismos reducen la exactitud del análisis de sentimiento.

## ⚠️ Errores habituales

- Fijar umbrales con una sola variable.
- Responder a alertas sin verificarlas.
- Escribir indicadores sin denominador o sin ventana.
- No registrar la precisión de las alertas emitidas.

## ➕ Extensión

Extensión: simula una segunda ola de menciones con el doble de volumen y distinto reparto. Comprueba si tus umbrales habrían activado la alerta a tiempo y qué ajustarías.

## 🔗 Clases que lo sostienen

[Clase 05](../clase-05-escucha-social-percepcion-y-alertas.md).
