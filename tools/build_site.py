# -*- coding: utf-8 -*-
"""Constructor del sitio HTML del programa.

Convierte todo el Markdown del repositorio en un sitio estático autocontenido,
apto para GitHub Pages y para migrar el programa a una plataforma de
capacitación. Sin dependencias externas y sin recursos de terceros: el sitio
funciona sin conexión.

Uso:
    python tools/build_site.py
    python tools/build_site.py --limpiar
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from markdown_min import render  # noqa: E402

SALIDA = os.path.join(RAIZ, "site")
FECHA = "2026-08-19"
TITULO = "Marketing, Sales & Growth Evolution Program"

DIRECTORIOS = ["curriculum", "rutas", "labs", "assessments", "cases", "projects", "capstone", "docs",
               "datasets", "notebooks", "templates", "simulations", "ai", "apps"]

RAIZ_DOCS = ["README.md", "SYLLABUS.md", "MANIFEST.md", "FILE_INDEX.md", "STATUS.md", "ROADMAP.md",
             "CHANGELOG.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md"]

SECCIONES = [
    ("curriculum", "Currículo"),
    ("rutas", "Rutas por rol"),
    ("labs", "Laboratorios"),
    ("assessments", "Evaluaciones"),
    ("cases", "Casos"),
    ("projects", "Proyectos"),
    ("capstone", "Capstone"),
    ("docs", "Documentación"),
]

CSS = """
:root {
  --fondo: #ffffff;
  --fondo-alt: #f6f7f9;
  --fondo-codigo: #f3f4f6;
  --texto: #1a1d21;
  --texto-suave: #545b64;
  --borde: #dfe3e8;
  --acento: #0b5c8a;
  --acento-suave: #e6f1f7;
  --marca: #b8442a;
  --ancho: 74ch;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-tema="claro"]) {
    --fondo: #14171a;
    --fondo-alt: #1b1f24;
    --fondo-codigo: #1f242a;
    --texto: #e8eaed;
    --texto-suave: #a4acb6;
    --borde: #2c333b;
    --acento: #6cb6e0;
    --acento-suave: #17303f;
    --marca: #e58267;
  }
}
:root[data-tema="oscuro"] {
  --fondo: #14171a; --fondo-alt: #1b1f24; --fondo-codigo: #1f242a;
  --texto: #e8eaed; --texto-suave: #a4acb6; --borde: #2c333b;
  --acento: #6cb6e0; --acento-suave: #17303f; --marca: #e58267;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0; background: var(--fondo); color: var(--texto);
  font: 17px/1.65 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  -webkit-text-size-adjust: 100%;
}
.saltar {
  position: absolute; left: -9999px; top: 0; background: var(--acento); color: #fff;
  padding: .6rem 1rem; z-index: 100; border-radius: 0 0 6px 0;
}
.saltar:focus { left: 0; }
header.superior {
  position: sticky; top: 0; z-index: 50; background: var(--fondo);
  border-bottom: 1px solid var(--borde); padding: .6rem 1.1rem;
  display: flex; gap: 1rem; align-items: center; flex-wrap: wrap;
}
header.superior .marca { font-weight: 700; color: var(--marca); text-decoration: none; font-size: .95rem; }
header.superior nav { display: flex; gap: .9rem; flex-wrap: wrap; margin-left: auto; }
header.superior nav a { color: var(--texto-suave); text-decoration: none; font-size: .88rem; }
header.superior nav a:hover, header.superior nav a:focus { color: var(--acento); text-decoration: underline; }
button.tema {
  background: transparent; border: 1px solid var(--borde); color: var(--texto-suave);
  border-radius: 6px; padding: .25rem .55rem; cursor: pointer; font-size: .82rem;
}
.envoltorio { display: flex; gap: 2rem; max-width: 1240px; margin: 0 auto; padding: 1.5rem 1.1rem 4rem; }
main { flex: 1 1 auto; min-width: 0; max-width: var(--ancho); }
aside.indice {
  flex: 0 0 240px; position: sticky; top: 4.2rem; align-self: flex-start;
  max-height: calc(100vh - 6rem); overflow-y: auto; font-size: .85rem;
}
aside.indice h2 { font-size: .78rem; text-transform: uppercase; letter-spacing: .06em; color: var(--texto-suave); }
aside.indice ol { list-style: none; padding: 0; margin: 0; }
aside.indice li { margin: .28rem 0; }
aside.indice li.n3 { padding-left: .9rem; }
aside.indice a { color: var(--texto-suave); text-decoration: none; }
aside.indice a:hover, aside.indice a:focus { color: var(--acento); text-decoration: underline; }
@media (max-width: 940px) { aside.indice { display: none; } .envoltorio { padding-top: 1rem; } }
h1, h2, h3, h4 { line-height: 1.25; margin: 2rem 0 .7rem; font-weight: 650; }
h1 { font-size: 1.85rem; margin-top: .4rem; }
h2 { font-size: 1.35rem; padding-top: .5rem; border-top: 1px solid var(--borde); }
h3 { font-size: 1.1rem; }
h4 { font-size: .98rem; color: var(--texto-suave); }
a { color: var(--acento); }
a.ancla { opacity: 0; margin-left: .4rem; text-decoration: none; font-weight: 400; }
h1:hover a.ancla, h2:hover a.ancla, h3:hover a.ancla { opacity: .45; }
p { margin: .8rem 0; }
ul, ol { margin: .8rem 0; padding-left: 1.4rem; }
li { margin: .3rem 0; }
li.tarea { list-style: none; margin-left: -1.2rem; }
blockquote {
  margin: 1.2rem 0; padding: .7rem 1.1rem; border-left: 4px solid var(--acento);
  background: var(--acento-suave); border-radius: 0 6px 6px 0;
}
blockquote p { margin: 0; }
code {
  background: var(--fondo-codigo); padding: .12em .38em; border-radius: 4px;
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: .88em;
}
pre.codigo {
  background: var(--fondo-codigo); border: 1px solid var(--borde); border-radius: 8px;
  padding: .9rem 1rem; overflow-x: auto; font-size: .86rem; line-height: 1.5;
}
pre.codigo code { background: none; padding: 0; }
pre.mermaid {
  background: var(--fondo-alt); border: 1px dashed var(--borde); border-radius: 8px;
  padding: .9rem 1rem; overflow-x: auto; font-size: .82rem; color: var(--texto-suave);
}
.tabla-scroll { overflow-x: auto; margin: 1.1rem 0; }
table { border-collapse: collapse; width: 100%; font-size: .92rem; }
th, td { border: 1px solid var(--borde); padding: .5rem .65rem; vertical-align: top; }
th { background: var(--fondo-alt); text-align: left; font-weight: 620; }
tbody tr:nth-child(even) { background: var(--fondo-alt); }
.al-right { text-align: right; }
.al-center { text-align: center; }
hr { border: none; border-top: 1px solid var(--borde); margin: 2rem 0; }
.meta {
  font-size: .82rem; color: var(--texto-suave); background: var(--fondo-alt);
  border: 1px solid var(--borde); border-radius: 8px; padding: .55rem .8rem; margin: .8rem 0 1.4rem;
  display: flex; gap: 1.1rem; flex-wrap: wrap;
}
.tarjetas { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: .9rem; margin: 1.2rem 0; }
.tarjeta {
  border: 1px solid var(--borde); border-radius: 10px; padding: .9rem 1rem; background: var(--fondo-alt);
  text-decoration: none; color: inherit; display: block;
}
.tarjeta:hover, .tarjeta:focus { border-color: var(--acento); }
.tarjeta strong { display: block; margin-bottom: .3rem; color: var(--acento); }
.tarjeta span { font-size: .85rem; color: var(--texto-suave); }
.cifras { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: .8rem; margin: 1.4rem 0; }
.cifra { border: 1px solid var(--borde); border-radius: 10px; padding: .8rem; text-align: center; }
.cifra b { display: block; font-size: 1.5rem; color: var(--marca); }
.cifra span { font-size: .78rem; color: var(--texto-suave); }
#buscador { width: 100%; padding: .6rem .8rem; border: 1px solid var(--borde); border-radius: 8px;
  background: var(--fondo); color: var(--texto); font-size: .95rem; margin: 1rem 0 .4rem; }
#resultados { list-style: none; padding: 0; margin: 0; }
#resultados li { padding: .45rem 0; border-bottom: 1px solid var(--borde); }
#resultados a { text-decoration: none; font-weight: 550; }
#resultados span { display: block; font-size: .8rem; color: var(--texto-suave); }
footer.pie {
  border-top: 1px solid var(--borde); padding: 1.4rem 1.1rem 3rem; text-align: center;
  color: var(--texto-suave); font-size: .84rem;
}
nav.paginacion { display: flex; justify-content: space-between; gap: 1rem; margin-top: 2.5rem;
  border-top: 1px solid var(--borde); padding-top: 1.1rem; font-size: .9rem; flex-wrap: wrap; }
@media print {
  header.superior, aside.indice, nav.paginacion, footer.pie, .saltar, button.tema { display: none !important; }
  body { font-size: 11pt; color: #000; background: #fff; }
  .envoltorio { display: block; padding: 0; max-width: none; }
  main { max-width: none; }
  a { color: #000; text-decoration: underline; }
  h2 { page-break-after: avoid; }
  table, pre, blockquote { page-break-inside: avoid; }
}
"""

JS = """
(function () {
  var clave = 'msg-tema';
  var boton = document.getElementById('cambiar-tema');
  function aplicar(t) {
    if (t) { document.documentElement.setAttribute('data-tema', t); }
    else { document.documentElement.removeAttribute('data-tema'); }
    if (boton) { boton.textContent = t === 'oscuro' ? 'Claro' : (t === 'claro' ? 'Sistema' : 'Oscuro'); }
  }
  try { aplicar(localStorage.getItem(clave)); } catch (e) {}
  if (boton) {
    boton.addEventListener('click', function () {
      var actual = document.documentElement.getAttribute('data-tema');
      var siguiente = actual === 'oscuro' ? 'claro' : (actual === 'claro' ? '' : 'oscuro');
      try { siguiente ? localStorage.setItem(clave, siguiente) : localStorage.removeItem(clave); } catch (e) {}
      aplicar(siguiente);
    });
  }

  var entrada = document.getElementById('buscador');
  var lista = document.getElementById('resultados');
  if (!entrada || !lista) { return; }
  var indice = null;
  var base = entrada.getAttribute('data-base') || '';
  function cargar() {
    if (indice) { return Promise.resolve(indice); }
    return fetch(base + 'search-index.json').then(function (r) { return r.json(); }).then(function (d) {
      indice = d; return d;
    }).catch(function () { return []; });
  }
  function normalizar(s) {
    return s.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g, '');
  }
  function buscar(q) {
    var t = normalizar(q.trim());
    if (t.length < 2) { lista.innerHTML = ''; return; }
    cargar().then(function (datos) {
      var res = [];
      for (var i = 0; i < datos.length && res.length < 40; i++) {
        var d = datos[i];
        if (normalizar(d.t).indexOf(t) !== -1 || normalizar(d.k || '').indexOf(t) !== -1) { res.push(d); }
      }
      lista.innerHTML = res.map(function (d) {
        return '<li><a href="' + base + d.u + '">' + d.t + '</a><span>' + (d.s || '') + '</span></li>';
      }).join('') || '<li><span>Sin resultados</span></li>';
    });
  }
  var temporizador;
  entrada.addEventListener('input', function () {
    clearTimeout(temporizador);
    var v = entrada.value;
    temporizador = setTimeout(function () { buscar(v); }, 120);
  });
})();
"""


def leer(ruta):
    with open(ruta, encoding="utf-8") as fh:
        return fh.read()


def escribir(ruta, contenido):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(contenido)


def reescribir_enlaces(contenido_html, profundidad):
    """Convierte enlaces a .md en enlaces a .html dentro del sitio."""
    def sustituir(match):
        destino = match.group(1)
        if destino.startswith(("http://", "https://", "#", "mailto:")):
            return match.group(0)
        base, sep, ancla = destino.partition("#")
        if base.endswith(".md"):
            base = base[:-3] + ".html"
        elif base.endswith("/"):
            base = base + "index.html"
        elif base in ("", "."):
            base = "index.html"
        return 'href="{}{}{}"'.format(base, sep, ancla)

    return re.sub(r'href="([^"]+)"', sustituir, contenido_html)


def plantilla(titulo, cuerpo, encabezados, profundidad, meta=None, seccion=None,
             anterior=None, siguiente=None, arriba=None):
    prefijo = "../" * profundidad
    nav = "".join(
        '<a href="{}{}/index.html">{}</a>'.format(prefijo, slug, nombre) for slug, nombre in SECCIONES)
    indice_lateral = ""
    if encabezados:
        items = "".join(
            '<li class="n{n}"><a href="#{a}">{t}</a></li>'.format(n=n, a=a, t=html.escape(t))
            for n, t, a in encabezados)
        indice_lateral = ('<aside class="indice" aria-label="Índice de la página">'
                          '<h2>En esta página</h2><ol>{}</ol></aside>'.format(items))
    barra_meta = ""
    if meta:
        piezas = []
        for etiqueta, clave in (("Parte", "part"), ("Clase", "class"), ("Nivel", "level"),
                                ("Duración", "estimated_minutes"), ("Aprobación", "mastery_threshold"),
                                ("Actualizado", "updated")):
            if clave in meta and meta[clave]:
                valor = meta[clave]
                if clave == "estimated_minutes":
                    valor = "{} min".format(valor)
                if clave == "mastery_threshold":
                    valor = "{}/100".format(valor)
                piezas.append("<span><strong>{}:</strong> {}</span>".format(etiqueta, html.escape(str(valor))))
        if piezas:
            barra_meta = '<div class="meta">{}</div>'.format("".join(piezas))
    paginacion = ""
    if anterior or siguiente or arriba:
        izq = '<a href="{}">← {}</a>'.format(anterior[1], html.escape(anterior[0])) if anterior else "<span></span>"
        centro = '<a href="{}">{}</a>'.format(arriba[1], html.escape(arriba[0])) if arriba else ""
        der = '<a href="{}">{} →</a>'.format(siguiente[1], html.escape(siguiente[0])) if siguiente else "<span></span>"
        paginacion = '<nav class="paginacion">{}{}{}</nav>'.format(izq, centro, der)

    return """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} · {marca}</title>
<meta name="description" content="{titulo} — programa educativo de marketing, ventas y crecimiento con evidencia verificable.">
<link rel="stylesheet" href="{p}assets/estilo.css">
</head>
<body>
<a class="saltar" href="#contenido">Saltar al contenido</a>
<header class="superior">
  <a class="marca" href="{p}index.html">{marca}</a>
  <nav aria-label="Secciones principales">{nav}</nav>
  <button class="tema" id="cambiar-tema" type="button">Oscuro</button>
</header>
<div class="envoltorio">
  <main id="contenido">
    {meta}
    {cuerpo}
    {paginacion}
  </main>
  {indice}
</div>
<footer class="pie">
  <p>{marca} · contenido bajo licencia MIT · actualizado {fecha}</p>
  <p>La fuente oficial manda sobre el material pedagógico. Formación aplicada, no asesoría legal.</p>
</footer>
<script src="{p}assets/app.js"></script>
</body>
</html>
""".format(titulo=html.escape(titulo), marca=TITULO, p=prefijo, nav=nav, meta=barra_meta,
           cuerpo=cuerpo, indice=indice_lateral, paginacion=paginacion, fecha=FECHA)


def procesar_markdown(ruta_md, ruta_html, profundidad, seccion=None,
                      anterior=None, siguiente=None, arriba=None, indice=None):
    texto = leer(ruta_md)
    cuerpo, meta, encabezados = render(texto)
    cuerpo = reescribir_enlaces(cuerpo, profundidad)
    titulo = meta.get("title") or _primer_h1(texto) or os.path.basename(ruta_md)
    escribir(ruta_html, plantilla(titulo, cuerpo, encabezados, profundidad, meta, seccion,
                                  anterior, siguiente, arriba))
    if indice is not None:
        rel = os.path.relpath(ruta_html, SALIDA).replace("\\", "/")
        # Índice por encabezados y términos destacados: cubre el documento completo
        # sin arrastrar su texto íntegro, que multiplicaría el peso del sitio.
        claves = re.findall(r"^#{1,4}\s+(.+)$", texto, re.M)
        claves += re.findall(r"\*\*([^*\n]{3,60})\*\*", texto)
        claves += re.findall(r"^\|\s*\*\*([^*|]{3,60})\*\*", texto, re.M)
        vistos = []
        for c in claves:
            c = re.sub(r"[#*`\[\]()]", "", c).strip().lower()
            if c and c not in vistos:
                vistos.append(c)
        indice.append({"t": titulo, "u": rel, "s": seccion or "", "k": " · ".join(vistos)[:2400]})


def _primer_h1(texto):
    for linea in texto.split("\n"):
        if linea.startswith("# "):
            return linea[2:].strip()
    return None


def titulo_de(ruta_md):
    """Título legible de un documento, para la navegación entre clases."""
    texto = leer(ruta_md)
    m = re.search(r'^title:\s*"?(.+?)"?\s*$', texto, re.M)
    if m:
        return m.group(1)
    return _primer_h1(texto) or os.path.basename(ruta_md)[:-3]


def main():
    ap = argparse.ArgumentParser(description="Genera el sitio HTML del programa")
    ap.add_argument("--limpiar", action="store_true", help="Borra site/ antes de construir")
    args = ap.parse_args()

    if args.limpiar and os.path.isdir(SALIDA):
        shutil.rmtree(SALIDA)

    os.makedirs(SALIDA, exist_ok=True)
    escribir(os.path.join(SALIDA, "assets", "estilo.css"), CSS.strip() + "\n")
    escribir(os.path.join(SALIDA, "assets", "app.js"), JS.strip() + "\n")
    escribir(os.path.join(SALIDA, ".nojekyll"), "")

    indice = []
    paginas = 0

    # documentos de la raíz
    for nombre in RAIZ_DOCS:
        origen = os.path.join(RAIZ, nombre)
        if not os.path.isfile(origen):
            continue
        destino = os.path.join(SALIDA, nombre[:-3] + ".html")
        procesar_markdown(origen, destino, 0, seccion="Programa", indice=indice)
        paginas += 1

    # árbol de contenido
    for carpeta in DIRECTORIOS:
        base = os.path.join(RAIZ, carpeta)
        if not os.path.isdir(base):
            continue
        nombre_seccion = dict(SECCIONES).get(carpeta, carpeta.capitalize())
        for actual, dirs, files in os.walk(base):
            dirs[:] = sorted(d for d in dirs if not d.startswith((".", "__")))
            archivos_md = sorted(f for f in files if f.endswith(".md"))
            clases = [f for f in archivos_md if f.startswith("class-")]
            for f in archivos_md:
                origen = os.path.join(actual, f)
                rel = os.path.relpath(origen, RAIZ).replace("\\", "/")
                destino = os.path.join(SALIDA, rel[:-3] + ".html")
                profundidad = rel.count("/")
                anterior = siguiente = arriba = None
                if f in clases:
                    k = clases.index(f)
                    if k > 0:
                        anterior = (titulo_de(os.path.join(actual, clases[k - 1])),
                                    clases[k - 1][:-3] + ".html")
                    if k < len(clases) - 1:
                        siguiente = (titulo_de(os.path.join(actual, clases[k + 1])),
                                     clases[k + 1][:-3] + ".html")
                    arriba = ("Índice de la parte", "README.html")
                procesar_markdown(origen, destino, profundidad, seccion=nombre_seccion,
                                  anterior=anterior, siguiente=siguiente, arriba=arriba, indice=indice)
                paginas += 1
            # Índice de carpeta. Se reescribe siempre: si sólo se generara cuando
            # falta, una reconstrucción sobre un sitio existente conservaría el
            # listado antiguo y ocultaría los archivos nuevos.
            rel_dir = os.path.relpath(actual, RAIZ).replace("\\", "/")
            destino_idx = os.path.join(SALIDA, rel_dir, "index.html")
            enlaces = []
            for d in dirs:
                enlaces.append('<a class="tarjeta" href="{0}/index.html"><strong>{0}</strong>'
                               '<span>Sección</span></a>'.format(d))
            for f in archivos_md:
                titulo = _primer_h1(leer(os.path.join(actual, f))) or f[:-3]
                enlaces.append('<a class="tarjeta" href="{}.html"><strong>{}</strong>'
                               '<span>{}</span></a>'.format(f[:-3], html.escape(titulo), f))
            if "README.md" in archivos_md:
                cuerpo = '<meta http-equiv="refresh" content="0; url=README.html">'
            else:
                cuerpo = "<h1>{}</h1><div class=\"tarjetas\">{}</div>".format(
                    html.escape(nombre_seccion), "".join(enlaces))
            escribir(destino_idx, plantilla(nombre_seccion, cuerpo, [], rel_dir.count("/") + 1))
            paginas += 1

    # panel de progreso: se copia tal cual para que funcione dentro del sitio
    panel_origen = os.path.join(RAIZ, "apps", "learning-dashboard")
    if os.path.isdir(panel_origen):
        panel_destino = os.path.join(SALIDA, "apps", "learning-dashboard")
        os.makedirs(panel_destino, exist_ok=True)
        for nombre in sorted(os.listdir(panel_origen)):
            if nombre.endswith((".html", ".js", ".css")):
                shutil.copy2(os.path.join(panel_origen, nombre), os.path.join(panel_destino, nombre))
        # el panel busca el índice del currículo dos niveles arriba
        os.makedirs(os.path.join(SALIDA, "curriculum"), exist_ok=True)
        origen_json = os.path.join(RAIZ, "curriculum", "curriculum.json")
        if os.path.isfile(origen_json):
            shutil.copy2(origen_json, os.path.join(SALIDA, "curriculum", "curriculum.json"))
        paginas += 1

    # portada
    cifras = [("336", "clases"), ("24", "partes"), ("48", "laboratorios"), ("1.344", "conceptos"),
              ("1.008", "métricas"), ("96", "obras citadas")]
    tarjetas = "".join(
        '<a class="tarjeta" href="{}/index.html"><strong>{}</strong>'
        '<span>{}</span></a>'.format(slug, nombre, descripcion)
        for slug, nombre, descripcion in [
            ("curriculum", "Currículo", "24 partes y 336 clases con definiciones operacionales"),
            ("rutas", "Rutas por rol", "17 guías de carrera con artefactos y progresión"),
            ("labs", "Laboratorios", "48 laboratorios con rúbrica de 100 puntos"),
            ("assessments", "Evaluaciones", "24 evaluaciones de cuatro bloques ponderados"),
            ("cases", "Casos", "24 casos extendidos con complicación"),
            ("projects", "Proyectos", "12 proyectos integradores acumulativos"),
            ("capstone", "Capstone", "Operación comercial completa y defensa"),
            ("docs", "Documentación", "Metodología, estándares, glosario y regulación"),
        ])
    tarjetas += ('<a class="tarjeta" href="apps/learning-dashboard/index.html"><strong>Panel de progreso</strong>'
                 '<span>Seguimiento local, sin cuentas ni envío de datos</span></a>')
    portada = """
<h1>{marca}</h1>
<p>De fundamentos comerciales a dirección de ingresos: <strong>24 partes</strong> y
<strong>336 clases</strong> en español, con bibliografía verificable, fichas de medición y contexto
normativo chileno.</p>
<div class="cifras">{cifras}</div>
<label for="buscador"><strong>Buscar en el programa</strong></label>
<input type="search" id="buscador" data-base="" placeholder="Escribe un concepto, una clase o una métrica…"
 autocomplete="off" aria-describedby="ayuda-buscador">
<p id="ayuda-buscador" style="font-size:.82rem;color:var(--texto-suave);margin:.2rem 0 1rem">
Busca por título o contenido. Mínimo dos caracteres.</p>
<ul id="resultados"></ul>
<h2 id="secciones">Secciones</h2>
<div class="tarjetas">{tarjetas}</div>
<h2 id="empezar">Cómo empezar</h2>
<ol>
<li>Lee la <a href="docs/RUTA-DE-APRENDIZAJE.html">ruta de aprendizaje</a> y elige tu recorrido.</li>
<li>Comienza por la <a href="curriculum/part-01-marketing-y-ventas-fundamentos-del-sistema-comercial/README.html">parte 01</a>.</li>
<li>Guarda tu evidencia según el <a href="docs/ESTANDAR-DE-EVIDENCIA.html">estándar de evidencia</a>.</li>
</ol>
<h2 id="para-instructores">Para instructores</h2>
<p>Cada clase trae agenda por tramos, rúbrica publicada y caso con complicación. Los formatos de sesión y la
migración a plataforma están en el <a href="docs/PLAN-DE-CAPACITACION.html">plan de capacitación</a> y en la
<a href="docs/GUIA-DOCENTE.html">guía docente</a>.</p>
""".format(marca=TITULO,
           cifras="".join('<div class="cifra"><b>{}</b><span>{}</span></div>'.format(v, e) for v, e in cifras),
           tarjetas=tarjetas)
    escribir(os.path.join(SALIDA, "index.html"), plantilla("Inicio", portada, [], 0))
    paginas += 1

    with open(os.path.join(SALIDA, "search-index.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(indice, fh, ensure_ascii=False, separators=(",", ":"))

    escribir(os.path.join(SALIDA, "manifest.webmanifest"), json.dumps({
        "name": TITULO, "short_name": "MSG Program", "start_url": "./index.html",
        "display": "standalone", "background_color": "#ffffff", "theme_color": "#0b5c8a",
    }, ensure_ascii=False, indent=2) + "\n")

    print("Sitio generado: {} páginas · índice de búsqueda: {} entradas".format(paginas, len(indice)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
