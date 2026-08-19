# Datos personales y ética comercial

Material educativo, no asesoría legal. Verifica la norma vigente en su fuente oficial antes de aplicar
cualquier contenido a una operación real.

## 1. Por qué esto no es un apéndice

En marketing y ventas, casi toda actividad toca datos personales: una lista de contactos, un formulario, un
registro de navegación, una grabación de llamada, un modelo que puntúa clientes. Tratar el cumplimiento como
revisión final produce dos costos: rediseñar campañas ya construidas y, peor, dañar la confianza de personas
reales.

Este programa trata la protección de datos como **restricción de diseño**: condiciona qué listas se pueden
construir, qué mensajes se pueden enviar y qué decisiones se pueden automatizar.

## 2. Preguntas obligatorias antes de cualquier tratamiento

Antes de construir una lista, activar una campaña o desplegar una automatización:

1. **¿Qué datos personales estoy tratando?** Enumera categorías, no «datos de clientes».
2. **¿Cuál es la finalidad?** Debe ser determinada, explícita y previa al tratamiento.
3. **¿Cuál es la base de licitud?** Consentimiento, ejecución de contrato, interés legítimo u otra prevista.
4. **¿El titular fue informado?** Debe poder saber quién trata sus datos, para qué y cómo ejercer derechos.
5. **¿Puede ejercer sus derechos?** Acceso, rectificación, cancelación y oposición con procedimiento real.
6. **¿Por cuánto tiempo los conservo?** La retención debe corresponder a la finalidad.
7. **¿Quién más accede?** Encargados, plataformas y transferencias deben estar identificados.
8. **¿Hay decisiones automatizadas?** Requieren documentación y supervisión humana.

Si alguna pregunta no tiene respuesta escrita, el tratamiento no debe iniciarse.

## 3. Casos frecuentes en operaciones comerciales

| Práctica | Problema | Alternativa correcta |
|---|---|---|
| Comprar bases de contactos | Sin base de licitud ni información al titular | Construir lista propia desde el perfil objetivo con origen documentado |
| Cargar la base de clientes en una plataforma publicitaria | Finalidad distinta a la informada | Verificar finalidad declarada; informar y obtener base adecuada |
| Grabar llamadas sin avisar | Tratamiento sin información ni consentimiento | Informar al inicio de la llamada y registrar el consentimiento |
| Enviar comunicaciones tras solicitud de baja | Incumplimiento del derecho de oposición | Procedimiento de exclusión efectivo en todos los canales |
| Personalizar con inferencias no declaradas | Uso fuera de la finalidad informada | Personalizar sólo con datos entregados conscientemente |
| Puntuar clientes con un modelo que decide sin revisión | Decisión automatizada sin supervisión | Documentar el proceso y mantener supervisión humana |
| Pegar datos de clientes en una herramienta de IA externa | Transferencia no evaluada | Anonimizar y definir qué categorías pueden compartirse |

## 4. Ética comercial más allá del cumplimiento

Cumplir la ley es el piso, no el estándar. El programa aplica tres pruebas adicionales:

### Prueba de publicación

¿La práctica resistiría ser explicada públicamente al cliente afectado? Si la respuesta depende de que el
cliente no se entere, la práctica no debe usarse.

### Prueba de reversibilidad

¿El cliente mantendría su decisión si conociera toda la información relevante? Si el beneficio de la empresa
depende del error del cliente, se cruzó la línea entre persuasión y manipulación.

### Prueba de simetría

¿Aceptarías esta práctica como cliente? No es un criterio suficiente, pero detecta rápidamente los casos más
evidentes.

## 5. Persuasión legítima y manipulación

| Legítimo | Ilegítimo |
|---|---|
| Presentar el beneficio real con evidencia | Exagerar resultados sin base |
| Usar prueba social verificable | Publicar testimonios inventados o no autorizados |
| Comunicar escasez real | Inventar cupos o plazos que se repiten |
| Reducir fricción del proceso | Ocultar costos hasta el último paso |
| Recordar un carrito abandonado con frecuencia acordada | Insistir tras una solicitud de no contacto |
| Ofrecer una garantía clara | Redactar condiciones que limitan derechos legales |

## 6. Uso de IA: reglas del programa

1. Toda afirmación factual generada se verifica en fuente primaria antes de usarse en una decisión.
2. Ninguna salida generada llega al cliente sin revisión humana.
3. Los sistemas que ejecutan acciones no tienen autoridad sobre operaciones irreversibles.
4. Se declara qué contenido fue generado o asistido y quién lo aprobó.
5. Existe un registro que permite reconstruir qué hizo el sistema, cuándo y bajo qué autorización.
6. La responsabilidad siempre es de la empresa y de la persona que aprobó, nunca del sistema.

Detalle completo en la parte 21 y en [`../ai/GUARDRAILS.md`](../ai/GUARDRAILS.md).

## 7. Datos del propio programa

Los conjuntos en `datasets/` son **sintéticos**: no contienen datos de personas reales. Se generan para que
los ejercicios sean reproducibles. Cualquier parecido con una empresa real es casual.

Si en un ejercicio usas datos reales de tu organización:

- verifica la autorización interna para usarlos con fines de formación;
- anonimiza antes de compartir;
- no los subas a este repositorio ni a servicios de terceros sin autorización;
- borra las copias al finalizar el ejercicio.

## 8. Qué hacer ante un incidente

1. **Contener**: detener el tratamiento o la comunicación que causa el daño.
2. **Evaluar**: qué datos, cuántas personas, qué consecuencia posible.
3. **Reparar**: corregir el efecto sobre las personas afectadas.
4. **Informar**: a los afectados y a la autoridad cuando corresponda.
5. **Prevenir**: causa raíz documentada y control que impida la repetición.

El orden importa: comunicar antes de reparar acelera la pérdida de confianza.

---

[⬅ Documentación](README.md) · [Mapa regulatorio](MAPA-REGULATORIO-CHILE.md) ·
[Fuentes oficiales](FUENTES-OFICIALES.md)
