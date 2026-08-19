# -*- coding: utf-8 -*-
"""Conversor mínimo de Markdown a HTML.

Sólo biblioteca estándar. Cubre el subconjunto de Markdown que este repositorio
utiliza: front matter YAML, encabezados, párrafos, listas ordenadas y no
ordenadas, tablas GFM, bloques de código con lenguaje, bloques mermaid, citas,
reglas horizontales, y formato en línea (negrita, cursiva, código, enlaces).

No pretende ser un conversor general: pretende ser correcto para este contenido
y no introducir dependencias externas.
"""

from __future__ import annotations

import html
import re

RE_FRONT = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
RE_ENCABEZADO = re.compile(r"^(#{1,6})\s+(.*)$")
RE_HR = re.compile(r"^\s*(?:---|\*\*\*|___)\s*$")
RE_LISTA_UL = re.compile(r"^(\s*)[-*+]\s+(.*)$")
RE_LISTA_OL = re.compile(r"^(\s*)(\d+)\.\s+(.*)$")
RE_TAREA = re.compile(r"^\[([ xX])\]\s+(.*)$")
RE_CITA = re.compile(r"^>\s?(.*)$")
RE_FENCE = re.compile(r"^```\s*([\w-]*)\s*$")
RE_FILA_TABLA = re.compile(r"^\s*\|(.+)\|\s*$")
RE_SEPARADOR_TABLA = re.compile(r"^\s*\|[\s:|-]+\|\s*$")


def parse_front_matter(texto):
    """Devuelve (metadatos, cuerpo). Metadatos como dict de strings."""
    m = RE_FRONT.match(texto)
    if not m:
        return {}, texto
    meta = {}
    for linea in m.group(1).split("\n"):
        if ":" not in linea or linea.strip().startswith("#"):
            continue
        clave, _, valor = linea.partition(":")
        meta[clave.strip()] = valor.strip().strip('"').strip("'")
    return meta, texto[m.end():]


def _inline(texto):
    """Formato en línea. Protege el código antes de escapar el resto."""
    fragmentos = []

    def guardar(match):
        fragmentos.append(match.group(1))
        return "\x00{}\x00".format(len(fragmentos) - 1)

    texto = re.sub(r"`([^`]+)`", guardar, texto)
    texto = html.escape(texto, quote=False)

    # enlaces [texto](destino)
    def enlace(match):
        etiqueta, destino = match.group(1), match.group(2)
        externo = destino.startswith(("http://", "https://"))
        attrs = ' target="_blank" rel="noopener noreferrer"' if externo else ""
        return '<a href="{}"{}>{}</a>'.format(html.escape(destino, quote=True), attrs, etiqueta)

    texto = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", enlace, texto)
    # autoenlaces <https://...>
    texto = re.sub(r"&lt;(https?://[^&\s]+)&gt;",
                   r'<a href="\1" target="_blank" rel="noopener noreferrer">\1</a>', texto)
    # negrita y cursiva
    texto = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", texto)
    texto = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", texto)

    for i, codigo in enumerate(fragmentos):
        texto = texto.replace("\x00{}\x00".format(i),
                              "<code>{}</code>".format(html.escape(codigo, quote=False)))
    return texto


def _celda(texto):
    return _inline(texto.strip())


def _tabla(lineas, i):
    """Convierte una tabla GFM que empieza en la línea i. Devuelve (html, i_final)."""
    cabecera = [c for c in lineas[i].strip().strip("|").split("|")]
    alineaciones = []
    for spec in lineas[i + 1].strip().strip("|").split("|"):
        spec = spec.strip()
        if spec.startswith(":") and spec.endswith(":"):
            alineaciones.append("center")
        elif spec.endswith(":"):
            alineaciones.append("right")
        else:
            alineaciones.append("left")
    salida = ['<div class="tabla-scroll"><table>', "<thead><tr>"]
    for k, celda in enumerate(cabecera):
        al = alineaciones[k] if k < len(alineaciones) else "left"
        salida.append('<th class="al-{}">{}</th>'.format(al, _celda(celda)))
    salida.append("</tr></thead><tbody>")
    j = i + 2
    while j < len(lineas) and RE_FILA_TABLA.match(lineas[j]):
        celdas = lineas[j].strip().strip("|").split("|")
        salida.append("<tr>")
        for k, celda in enumerate(celdas):
            al = alineaciones[k] if k < len(alineaciones) else "left"
            salida.append('<td class="al-{}">{}</td>'.format(al, _celda(celda)))
        salida.append("</tr>")
        j += 1
    salida.append("</tbody></table></div>")
    return "".join(salida), j


def _lista(lineas, i, ordenada):
    """Convierte una lista simple (sin anidamiento profundo)."""
    etiqueta = "ol" if ordenada else "ul"
    salida = ["<{}>".format(etiqueta)]
    j = i
    while j < len(lineas):
        m = RE_LISTA_OL.match(lineas[j]) if ordenada else RE_LISTA_UL.match(lineas[j])
        if not m:
            if lineas[j].strip() == "" and j + 1 < len(lineas):
                siguiente = RE_LISTA_OL.match(lineas[j + 1]) if ordenada else RE_LISTA_UL.match(lineas[j + 1])
                if siguiente:
                    j += 1
                    continue
            break
        contenido = m.group(3) if ordenada else m.group(2)
        tarea = RE_TAREA.match(contenido)
        if tarea:
            marcado = "checked" if tarea.group(1).lower() == "x" else ""
            salida.append('<li class="tarea"><input type="checkbox" disabled {}> {}</li>'.format(
                marcado, _inline(tarea.group(2))))
        else:
            salida.append("<li>{}</li>".format(_inline(contenido)))
        j += 1
    salida.append("</{}>".format(etiqueta))
    return "".join(salida), j


def render(markdown_texto):
    """Convierte Markdown a HTML. Devuelve (html, metadatos, encabezados)."""
    meta, cuerpo = parse_front_matter(markdown_texto)
    lineas = cuerpo.split("\n")
    salida = []
    encabezados = []
    i = 0
    parrafo = []

    def cerrar_parrafo():
        if parrafo:
            salida.append("<p>{}</p>".format(_inline(" ".join(parrafo).strip())))
            parrafo.clear()

    usados = {}
    while i < len(lineas):
        linea = lineas[i]

        m = RE_FENCE.match(linea)
        if m:
            cerrar_parrafo()
            lenguaje = m.group(1) or "text"
            j = i + 1
            bloque = []
            while j < len(lineas) and not lineas[j].startswith("```"):
                bloque.append(lineas[j])
                j += 1
            contenido = "\n".join(bloque)
            if lenguaje == "mermaid":
                salida.append('<pre class="mermaid">{}</pre>'.format(html.escape(contenido, quote=False)))
            else:
                salida.append('<pre class="codigo" data-lang="{}"><code>{}</code></pre>'.format(
                    html.escape(lenguaje, quote=True), html.escape(contenido, quote=False)))
            i = j + 1
            continue

        m = RE_ENCABEZADO.match(linea)
        if m:
            cerrar_parrafo()
            nivel = len(m.group(1))
            texto = m.group(2).strip()
            base = re.sub(r"[^\w\s-]", "", texto, flags=re.UNICODE).strip().lower()
            base = re.sub(r"[\s_]+", "-", base) or "seccion"
            usados[base] = usados.get(base, 0) + 1
            ancla = base if usados[base] == 1 else "{}-{}".format(base, usados[base])
            salida.append('<h{n} id="{a}">{t}<a class="ancla" href="#{a}" aria-label="Enlace a la sección">#</a></h{n}>'.format(
                n=nivel, a=ancla, t=_inline(texto)))
            if nivel in (2, 3):
                encabezados.append((nivel, texto, ancla))
            i += 1
            continue

        if RE_HR.match(linea) and not parrafo:
            cerrar_parrafo()
            salida.append("<hr>")
            i += 1
            continue

        if RE_FILA_TABLA.match(linea) and i + 1 < len(lineas) and RE_SEPARADOR_TABLA.match(lineas[i + 1]):
            cerrar_parrafo()
            bloque, i = _tabla(lineas, i)
            salida.append(bloque)
            continue

        if RE_LISTA_UL.match(linea):
            cerrar_parrafo()
            bloque, i = _lista(lineas, i, ordenada=False)
            salida.append(bloque)
            continue

        if RE_LISTA_OL.match(linea):
            cerrar_parrafo()
            bloque, i = _lista(lineas, i, ordenada=True)
            salida.append(bloque)
            continue

        m = RE_CITA.match(linea)
        if m:
            cerrar_parrafo()
            bloque = []
            j = i
            while j < len(lineas) and RE_CITA.match(lineas[j]):
                bloque.append(RE_CITA.match(lineas[j]).group(1))
                j += 1
            salida.append("<blockquote><p>{}</p></blockquote>".format(_inline(" ".join(bloque).strip())))
            i = j
            continue

        if linea.strip() == "":
            cerrar_parrafo()
            i += 1
            continue

        parrafo.append(linea.strip())
        i += 1

    cerrar_parrafo()
    return "\n".join(salida), meta, encabezados
