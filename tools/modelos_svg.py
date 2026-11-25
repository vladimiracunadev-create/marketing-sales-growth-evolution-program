# -*- coding: utf-8 -*-
"""Generador de modelos mentales en SVG a partir de la especificación de cada clase.

Cada diagrama se construye con el contenido real de su clase, no con una plantilla de
sustantivos intercambiables:

* el **método** se dibuja con una de cuatro disposiciones (flujo en serpentina, escalera, anillo o
  columna central) elegida según la cantidad de pasos y el contenido de la clase;
* los **conceptos** se enlazan con los pasos del método donde su vocabulario aparece de verdad: la
  insignia ``↔ 2, 4`` de un concepto significa que sus palabras se usan en esos pasos;
* las **señales de medición** se dibujan como fracciones con numerador y denominador reales;
* la **frontera de aplicación** y el **error frecuente** cierran el diagrama con su texto propio;
* el color cambia por parte para que cada parte del programa se reconozca.

Sin dependencias externas. El SVG es autocontenido, lleva ``<title>`` y ``<desc>`` y su texto
equivalente se publica junto a la imagen en la clase.
"""

from __future__ import annotations

import colorsys
import hashlib
import html
import math
import re
import unicodedata

ANCHO = 900
MARGEN = 40
FUENTE = "Segoe UI, Helvetica, Arial, sans-serif"
VACIAS = {
    "para", "como", "cada", "esta", "este", "esos", "estos", "entre", "sobre", "desde", "hasta", "donde",
    "cuando", "porque", "pero", "sino", "mismo", "misma", "otro", "otra", "otros", "otras", "tiene",
    "tienen", "puede", "pueden", "debe", "deben", "sobre", "segun", "cual", "cuales", "todo", "toda",
    "todos", "todas", "mas", "menos", "solo", "sin", "con", "los", "las", "una", "uno", "del", "por",
}


def esc(texto):
    return html.escape(str(texto), quote=False)


def sin_tildes(texto):
    return "".join(c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn")


def raices(texto):
    """Raíces de 5 letras de las palabras con contenido, para detectar vocabulario compartido."""
    salida = set()
    for palabra in re.findall(r"[a-záéíóúñü]+", texto.lower()):
        p = sin_tildes(palabra)
        if len(p) >= 5 and p not in VACIAS:
            salida.add(p[:5])
    return salida


def paleta(num_parte):
    h = (int(num_parte) * 47 % 360) / 360.0

    def hsl(s, l):
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        return "#{:02x}{:02x}{:02x}".format(int(r * 255), int(g * 255), int(b * 255))

    return dict(oscuro=hsl(0.55, 0.28), medio=hsl(0.5, 0.45), claro=hsl(0.6, 0.93), suave=hsl(0.45, 0.82),
                borde=hsl(0.4, 0.68))


def envolver(texto, ancho, fs, max_lineas=None):
    por_linea = max(8, int(ancho / (fs * 0.55)))
    lineas, actual = [], ""
    for palabra in texto.split():
        if len(actual) + len(palabra) + (1 if actual else 0) <= por_linea:
            actual = (actual + " " + palabra).strip()
        else:
            if actual:
                lineas.append(actual)
            actual = palabra
    if actual:
        lineas.append(actual)
    if max_lineas and len(lineas) > max_lineas:
        lineas = lineas[:max_lineas]
        lineas[-1] = lineas[-1][: max(0, por_linea - 1)].rstrip(" ,;.:") + "…"
    return lineas


def texto_svg(x, y, lineas, fs=12, color="#1f2933", peso=400, ancla="start", interlinea=1.32):
    if not lineas:
        return ""
    partes = ['<text x="{}" y="{}" font-size="{}" fill="{}" font-weight="{}" text-anchor="{}">'.format(
        round(x, 1), round(y, 1), fs, color, peso, ancla)]
    for k, linea in enumerate(lineas):
        if k == 0:
            partes.append("<tspan x=\"{}\">{}</tspan>".format(round(x, 1), esc(linea)))
        else:
            partes.append("<tspan x=\"{}\" dy=\"{}\">{}</tspan>".format(round(x, 1), round(fs * interlinea, 1), esc(linea)))
    partes.append("</text>")
    return "".join(partes)


def alto_texto(lineas, fs, interlinea=1.32):
    return len(lineas) * fs * interlinea


def caja(x, y, w, h, relleno, borde, radio=10, grosor=1.4, extra=""):
    return '<rect x="{}" y="{}" width="{}" height="{}" rx="{}" fill="{}" stroke="{}" stroke-width="{}"{}/>'.format(
        round(x, 1), round(y, 1), round(w, 1), round(h, 1), radio, relleno, borde, grosor, extra)


def flecha(x1, y1, x2, y2, color, grosor=2.2):
    ang = math.atan2(y2 - y1, x2 - x1)
    pa = (x2 - 9 * math.cos(ang - 0.45), y2 - 9 * math.sin(ang - 0.45))
    pb = (x2 - 9 * math.cos(ang + 0.45), y2 - 9 * math.sin(ang + 0.45))
    return ('<line x1="{:.1f}" y1="{:.1f}" x2="{:.1f}" y2="{:.1f}" stroke="{}" stroke-width="{}" stroke-linecap="round"/>'
            '<polygon points="{:.1f},{:.1f} {:.1f},{:.1f} {:.1f},{:.1f}" fill="{}"/>').format(
        x1, y1, x2 - 5 * math.cos(ang), y2 - 5 * math.sin(ang), color, grosor,
        x2, y2, pa[0], pa[1], pb[0], pb[1], color)


def numero(x, y, n, p, r=14):
    return ('<circle cx="{:.1f}" cy="{:.1f}" r="{}" fill="{}"/>'
            '<text x="{:.1f}" y="{:.1f}" font-size="13" fill="#ffffff" font-weight="700" text-anchor="middle">{}</text>'
            ).format(x, y, r, p["oscuro"], x, y + 4.5, n)


# ---------------------------------------------------------------------------------------------
# método: cuatro disposiciones
# ---------------------------------------------------------------------------------------------

def _preparar_pasos(pasos, ancho_caja, fs=12.5):
    bloques = []
    for paso in pasos:
        lineas = envolver(paso[0].upper() + paso[1:], ancho_caja - 24, fs)
        bloques.append((lineas, alto_texto(lineas, fs) + 26))
    return bloques


def metodo_flujo(pasos, p, y0):
    n = len(pasos)
    cols = n if n <= 3 else (2 if n == 4 else 3)
    sep = 40
    ancho = (ANCHO - 2 * MARGEN - (cols - 1) * sep) / cols
    bloques = _preparar_pasos(pasos, ancho)
    filas = [list(range(i, min(i + cols, n))) for i in range(0, n, cols)]
    partes, y = [], y0
    posiciones = {}
    for r, fila in enumerate(filas):
        alto = max(bloques[i][1] for i in fila)
        orden = fila if r % 2 == 0 else list(reversed(fila))
        # columna visual de cada paso: en filas impares se recorre de derecha a izquierda
        for c, i in enumerate(orden):
            colvis = c if r % 2 == 0 else (cols - 1 - (len(fila) - 1 - c))
            x = MARGEN + colvis * (ancho + sep)
            posiciones[i] = (x, y, ancho, alto)
        y += alto + 38
    for i in range(n):
        x, yy, w, h = posiciones[i]
        partes.append(caja(x, yy, w, h, p["claro"], p["borde"]))
        partes.append(texto_svg(x + 14, yy + 22, bloques[i][0], 12.5, "#1f2933"))
        partes.append(numero(x + 2, yy + 2, i + 1, p))
    for i in range(n - 1):
        x1, y1, w1, h1 = posiciones[i]
        x2, y2, w2, h2 = posiciones[i + 1]
        if abs(y1 - y2) < 1:
            if x2 > x1:
                partes.append(flecha(x1 + w1 + 3, y1 + h1 / 2, x2 - 3, y2 + h2 / 2, p["medio"]))
            else:
                partes.append(flecha(x1 - 3, y1 + h1 / 2, x2 + w2 + 3, y2 + h2 / 2, p["medio"]))
        else:
            partes.append(flecha(x1 + w1 / 2, y1 + h1 + 2, x2 + w2 / 2, y2 - 3, p["medio"]))
    return "".join(partes), y - 38 + 10, posiciones


def metodo_escalera(pasos, p, y0):
    n = len(pasos)
    ancho = 330
    bloques = _preparar_pasos(pasos, ancho)
    alto = max(b[1] for b in bloques)
    paso_x = (ANCHO - 2 * MARGEN - ancho) / max(1, n - 1)
    posiciones, partes = {}, []
    for i in range(n):
        x = MARGEN + i * paso_x
        y = y0 + i * (alto + 14)
        posiciones[i] = (x, y, ancho, alto)
    for i in range(n - 1):
        x1, y1, w1, h1 = posiciones[i]
        x2, y2, w2, h2 = posiciones[i + 1]
        partes.append('<path d="M{:.1f},{:.1f} V{:.1f} H{:.1f}" fill="none" stroke="{}" stroke-width="2.2" '
                      'stroke-linecap="round" stroke-linejoin="round"/>'.format(
                          x1 + 26, y1 + h1, y2 + h2 / 2, x2 - 4, p["medio"]))
        partes.append('<polygon points="{:.1f},{:.1f} {:.1f},{:.1f} {:.1f},{:.1f}" fill="{}"/>'.format(
            x2 - 2, y2 + h2 / 2, x2 - 11, y2 + h2 / 2 - 5, x2 - 11, y2 + h2 / 2 + 5, p["medio"]))
    for i in range(n):
        x, y, w, h = posiciones[i]
        partes.append(caja(x, y, w, h, p["claro"], p["borde"]))
        partes.append(texto_svg(x + 14, y + 22, bloques[i][0], 12.5, "#1f2933"))
        partes.append(numero(x + 2, y + 2, i + 1, p))
    return "".join(partes), y0 + n * (alto + 14), posiciones


def metodo_anillo(pasos, p, y0, titulo):
    n = len(pasos)
    ancho = 178
    bloques = _preparar_pasos(pasos, ancho)
    alto = max(b[1] for b in bloques)
    rx, ry = 330, 150 + alto * 1.1
    cx, cy = ANCHO / 2, y0 + ry + alto / 2 + 6
    posiciones, partes = {}, []
    centros = []
    for i in range(n):
        ang = -math.pi / 2 + 2 * math.pi * i / n
        centros.append((cx + rx * math.cos(ang), cy + ry * math.sin(ang)))
    partes.append('<ellipse cx="{:.1f}" cy="{:.1f}" rx="{:.1f}" ry="{:.1f}" fill="none" stroke="{}" '
                  'stroke-width="2" stroke-dasharray="3 8" stroke-linecap="round"/>'.format(cx, cy, rx, ry, p["borde"]))
    for i in range(n):
        a0 = -math.pi / 2 + 2 * math.pi * i / n
        a1 = -math.pi / 2 + 2 * math.pi * (i + 1) / n
        am = (a0 + a1) / 2
        mx, my = cx + rx * math.cos(am), cy + ry * math.sin(am)
        ang = math.atan2(ry * math.cos(am), -rx * math.sin(am))
        partes.append('<polygon points="{:.1f},{:.1f} {:.1f},{:.1f} {:.1f},{:.1f}" fill="{}"/>'.format(
            mx + 11 * math.cos(ang), my + 11 * math.sin(ang),
            mx + 8 * math.cos(ang + 2.4), my + 8 * math.sin(ang + 2.4),
            mx + 8 * math.cos(ang - 2.4), my + 8 * math.sin(ang - 2.4), p["medio"]))
    radio = min(rx - ancho / 2 - 30, 100)
    partes.append('<circle cx="{:.1f}" cy="{:.1f}" r="{:.1f}" fill="{}" stroke="{}" stroke-width="1.6"/>'.format(
        cx, cy, radio, p["suave"], p["borde"]))
    lineas = envolver(titulo, radio * 1.6, 15, 4)
    partes.append(texto_svg(cx, cy - alto_texto(lineas, 15) / 2 + 12, lineas, 15, p["oscuro"], 700, "middle"))
    for i in range(n):
        x = centros[i][0] - ancho / 2
        h = bloques[i][1]
        y = centros[i][1] - h / 2
        posiciones[i] = (x, y, ancho, h)
        partes.append(caja(x, y, ancho, h, p["claro"], p["borde"]))
        partes.append(texto_svg(x + 12, y + 22, bloques[i][0], 12.5, "#1f2933"))
        partes.append(numero(x + 2, y + 2, i + 1, p))
    return "".join(partes), cy + ry + alto / 2 + 14, posiciones


def metodo_columna(pasos, p, y0):
    n = len(pasos)
    ancho = 350
    bloques = _preparar_pasos(pasos, ancho)
    cx = ANCHO / 2
    ys = []
    for i in range(n):
        y = y0 if i == 0 else ys[-1] + 38
        if i >= 2:
            y = max(y, ys[i - 2] + bloques[i - 2][1] + 14)
        ys.append(y)
    fin = max(ys[i] + bloques[i][1] for i in range(n))
    partes = ['<line x1="{}" y1="{:.1f}" x2="{}" y2="{:.1f}" stroke="{}" stroke-width="3" stroke-linecap="round"/>'.format(
        cx, y0 - 6, cx, fin + 6, p["borde"])]
    posiciones = {}
    for i in range(n):
        izq = i % 2 == 0
        x = cx - 44 - ancho if izq else cx + 44
        y, h = ys[i], bloques[i][1]
        posiciones[i] = (x, y, ancho, h)
        yc = y + min(h / 2, 30)
        partes.append('<line x1="{}" y1="{:.1f}" x2="{}" y2="{:.1f}" stroke="{}" stroke-width="2"/>'.format(
            cx, yc, x + ancho if izq else x, yc, p["borde"]))
        partes.append(caja(x, y, ancho, h, p["claro"], p["borde"]))
        partes.append(texto_svg(x + 14, y + 22, bloques[i][0], 12.5, "#1f2933"))
        partes.append(numero(cx, yc, i + 1, p, 15))
    return "".join(partes), fin + 14, posiciones


# ---------------------------------------------------------------------------------------------
# paneles auxiliares
# ---------------------------------------------------------------------------------------------

def rotulo(x, y, texto, p):
    return ('<text x="{}" y="{}" font-size="11.5" fill="{}" font-weight="700" letter-spacing="1.4">{}</text>'
            ).format(x, y, p["medio"], esc(texto.upper()))


def vinculos(conceptos, pasos):
    """Para cada concepto, los pasos cuyo vocabulario comparte de verdad con él."""
    raices_pasos = [raices(s) for s in pasos]
    salida = []
    for nombre, definicion in conceptos:
        propias = raices(nombre)
        extra = raices(definicion)
        enlaces = []
        for i, rp in enumerate(raices_pasos):
            if len(propias & rp) >= 1 or len(extra & rp) >= 2:
                enlaces.append(i + 1)
        salida.append(enlaces[:4])
    return salida


def panel_conceptos(conceptos, pasos, p, y0):
    if not conceptos:
        return "", y0
    enlaces = vinculos(conceptos, pasos)
    cols = 2
    gap = 18
    ancho = (ANCHO - 2 * MARGEN - (cols - 1) * gap) / cols
    tarjetas = []
    for (nombre, definicion), enl in zip(conceptos, enlaces):
        nl = envolver(nombre[0].upper() + nombre[1:], ancho - 32 - (62 if enl else 0), 13.5, 2)
        dl = envolver(definicion[0].upper() + definicion[1:], ancho - 28, 11.5, 4)
        tarjetas.append((nl, dl, alto_texto(nl, 13.5) + alto_texto(dl, 11.5) + 30, enl))
    partes = [rotulo(MARGEN, y0, "Conceptos y dónde actúan en el método", p)]
    y = y0 + 14
    for fila in range(0, len(tarjetas), cols):
        grupo = tarjetas[fila:fila + cols]
        alto = max(t[2] for t in grupo)
        for c, (nl, dl, h, enl) in enumerate(grupo):
            x = MARGEN + c * (ancho + gap)
            partes.append(caja(x, y, ancho, alto, "#ffffff", p["borde"], 8))
            partes.append('<rect x="{:.1f}" y="{:.1f}" width="5" height="{:.1f}" rx="2" fill="{}"/>'.format(
                x, y + 8, alto - 16, p["medio"]))
            partes.append(texto_svg(x + 16, y + 22, nl, 13.5, p["oscuro"], 700))
            yy = y + 22 + alto_texto(nl, 13.5) - 4
            partes.append(texto_svg(x + 16, yy + 6, dl, 11.5, "#3e4c59"))
            if enl:
                insignia = "↔ " + ", ".join(str(k) for k in enl)
                partes.append(caja(x + ancho - 62, y + 8, 54, 20, p["suave"], p["borde"], 10, 1))
                partes.append('<text x="{:.1f}" y="{:.1f}" font-size="11" fill="{}" font-weight="700" '
                              'text-anchor="middle">{}</text>'.format(x + ancho - 35, y + 22, p["oscuro"], esc(insignia)))
        y += alto + 14
    return "".join(partes), y


def dividir_ficha(definicion):
    """Devuelve (numerador, denominador, nota) a partir de los formatos de ficha del programa."""
    m = re.search(r"numerador:\s*(.*?);\s*denominador[^:;]*:\s*(.*?)(?:;\s*(.*))?$", definicion, re.S | re.I)
    if m:
        nota = m.group(3) or ""
        nota = re.sub(r";\s*(fuente|responsable|lectura|limitaci)[^;]*", "", "; " + nota).strip("; ").strip()
        return m.group(1).strip(), m.group(2).strip(), nota
    for corte in (" dividido por ", " dividido entre ", ", sobre ", " sobre "):
        if corte in definicion:
            a, b = definicion.split(corte, 1)
            return a.strip(), b.strip(), ""
    return definicion.strip(), "", ""


def panel_senales(senales, p, y0):
    if not senales:
        return "", y0
    cols = min(3, len(senales))
    gap = 18
    ancho = (ANCHO - 2 * MARGEN - (cols - 1) * gap) / cols
    items = []
    for nombre, definicion in senales:
        num, den, nota = dividir_ficha(definicion)
        nl = envolver(nombre[0].upper() + nombre[1:], ancho - 28, 13, 2)
        numl = envolver(num[0].upper() + num[1:], ancho - 28, 11.5, 5)
        denl = envolver(den[0].upper() + den[1:], ancho - 28, 11.5, 4) if den else []
        notl = envolver(nota[0].upper() + nota[1:], ancho - 28, 10.5, 2) if nota else []
        h = (alto_texto(nl, 13) + alto_texto(numl, 11.5) + (alto_texto(denl, 11.5) + 22 if denl else 0)
             + (alto_texto(notl, 10.5) + 8 if notl else 0) + 36)
        items.append((nl, numl, denl, h, notl))
    partes = [rotulo(MARGEN, y0, "Qué se mide: numerador sobre denominador", p)]
    y = y0 + 14
    for fila in range(0, len(items), cols):
        grupo = items[fila:fila + cols]
        alto = max(i[3] for i in grupo)
        for c, (nl, numl, denl, h, notl) in enumerate(grupo):
            x = MARGEN + c * (ancho + gap)
            partes.append(caja(x, y, ancho, alto, p["claro"], p["borde"], 8))
            partes.append(texto_svg(x + 14, y + 22, nl, 13, p["oscuro"], 700))
            yy = y + 22 + alto_texto(nl, 13) + 6
            partes.append(texto_svg(x + 14, yy + 6, numl, 11.5, "#1f2933"))
            yy += alto_texto(numl, 11.5) + 8
            if denl:
                partes.append('<line x1="{:.1f}" y1="{:.1f}" x2="{:.1f}" y2="{:.1f}" stroke="{}" stroke-width="2"/>'.format(
                    x + 14, yy + 4, x + ancho - 14, yy + 4, p["medio"]))
                partes.append(texto_svg(x + 14, yy + 22, denl, 11.5, "#52606d"))
                yy += alto_texto(denl, 11.5) + 22
            if notl:
                partes.append(texto_svg(x + 14, yy + 14, notl, 10.5, "#7b8794"))
        y += alto + 14
    return "".join(partes), y


def panel_cierre(clase, p, y0):
    limite = clase.get("limite")
    if not limite and clase.get("riesgos"):
        elegido = next((r for r in clase["riesgos"] if r[0] == "Reputacional"), clase["riesgos"][-1])
        limite = "Riesgo {}: {}".format(elegido[0].lower(), re.sub(r"\{n:[^}]+\}", "la norma aplicable", elegido[1]))
    error = clase.get("error")
    if not error and clase.get("errores"):
        error = clase["errores"][0]
    partes, y = [], y0
    if limite:
        ll = envolver(limite, ANCHO - 2 * MARGEN - 90, 12.5, 5)
        h = alto_texto(ll, 12.5) + 32
        partes.append(rotulo(MARGEN, y + 2, "Frontera de aplicación", p))
        y += 12
        partes.append(caja(MARGEN, y, ANCHO - 2 * MARGEN, h, "#fff7ed", "#c2410c", 8, 1.4))
        partes.append('<polygon points="{},{} {},{} {},{}" fill="#c2410c"/>'.format(
            MARGEN + 30, y + h / 2 - 15, MARGEN + 12, y + h / 2 + 14, MARGEN + 48, y + h / 2 + 14))
        partes.append('<text x="{}" y="{}" font-size="15" fill="#ffffff" font-weight="700" text-anchor="middle">!</text>'.format(
            MARGEN + 30, y + h / 2 + 11))
        partes.append(texto_svg(MARGEN + 66, y + 24, ll, 12.5, "#7c2d12"))
        y += h + 26
    if error:
        sint, corr = error
        mitad = (ANCHO - 2 * MARGEN - 60) / 2
        sl = envolver(sint, mitad - 28, 12.5, 3)
        cl = envolver(corr, mitad - 28, 12.5, 5)
        h = max(alto_texto(sl, 12.5), alto_texto(cl, 12.5)) + 44
        partes.append(rotulo(MARGEN, y + 2, "Error frecuente y su corrección", p))
        y += 12
        partes.append(caja(MARGEN, y, mitad, h, "#fef2f2", "#b91c1c", 8, 1.4))
        partes.append(texto_svg(MARGEN + 14, y + 22, ["Síntoma"], 11, "#b91c1c", 700))
        partes.append(texto_svg(MARGEN + 14, y + 40, sl, 12.5, "#7f1d1d"))
        partes.append(flecha(MARGEN + mitad + 6, y + h / 2, MARGEN + mitad + 54, y + h / 2, p["medio"], 2.6))
        x2 = MARGEN + mitad + 60
        partes.append(caja(x2, y, mitad, h, "#f0fdf4", "#15803d", 8, 1.4))
        partes.append(texto_svg(x2 + 14, y + 22, ["Corrección"], 11, "#15803d", 700))
        partes.append(texto_svg(x2 + 14, y + 40, cl, 12.5, "#14532d"))
        y += h + 14
    return "".join(partes), y


# ---------------------------------------------------------------------------------------------
# composición
# ---------------------------------------------------------------------------------------------

def disposicion(clave, n):
    candidatos = ["flujo", "escalera", "columna"]
    if 5 <= n <= 8:
        candidatos.append("anillo")
    if n <= 4:
        candidatos = ["flujo", "columna", "escalera"]
    digest = int(hashlib.sha1(clave.encode("utf-8")).hexdigest(), 16)
    return candidatos[digest % len(candidatos)]


def modelo_svg(clase, num_parte, referencia, titulo_parte=""):
    """Devuelve el SVG del modelo mental de una clase y la disposición usada."""
    p = paleta(num_parte)
    pasos = list(clase["metodo"])
    conceptos = list(clase.get("conceptos", []))
    senales = list(clase.get("senales", []))
    forma = disposicion(referencia + clase["slug"], len(pasos))
    cabecera = 78
    cuerpo = [rotulo(MARGEN, cabecera + 6, "Método paso a paso", p)]
    y = cabecera + 22
    if forma == "flujo":
        grafico, y, pos = metodo_flujo(pasos, p, y)
    elif forma == "escalera":
        grafico, y, pos = metodo_escalera(pasos, p, y)
    elif forma == "anillo":
        grafico, y, pos = metodo_anillo(pasos, p, y, clase["titulo"])
    else:
        grafico, y, pos = metodo_columna(pasos, p, y)
    cuerpo.append(grafico)
    y += 28
    extra, y = panel_conceptos(conceptos, pasos, p, y)
    cuerpo.append(extra)
    y += 18 if extra else 0
    extra, y = panel_senales(senales, p, y)
    cuerpo.append(extra)
    y += 18 if extra else 0
    extra, y = panel_cierre(clase, p, y)
    cuerpo.append(extra)
    alto = int(y + 24)
    descripcion = "Modelo mental de la clase {}: {}. Método en {} pasos; {} conceptos; {} señales de medición.".format(
        referencia, clase["titulo"], len(pasos), len(conceptos), len(senales))
    cab = (
        '<rect x="0" y="0" width="{w}" height="{h}" rx="14" fill="#ffffff"/>'
        '<rect x="0" y="0" width="{w}" height="64" rx="14" fill="{osc}"/>'
        '<rect x="0" y="40" width="{w}" height="24" fill="{osc}"/>'
        '<text x="{m}" y="28" font-size="12" fill="{sua}" font-weight="700" letter-spacing="1.6">{ref}</text>'
        '<text x="{m}" y="52" font-size="21" fill="#ffffff" font-weight="700">{tit}</text>'
    ).format(w=ANCHO, h=alto, osc=p["oscuro"], sua=p["suave"], m=MARGEN,
             ref=esc("MODELO MENTAL · CLASE " + referencia + (" · " + titulo_parte.upper() if titulo_parte else "")),
             tit=esc(clase["titulo"]))
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
        'aria-labelledby="t d" font-family="{f}">'
        '<title id="t">Modelo mental · {tit}</title><desc id="d">{desc}</desc>{cab}{cuerpo}</svg>'
    ).format(w=ANCHO, h=alto, f=FUENTE, tit=esc(clase["titulo"]), desc=esc(descripcion), cab=cab,
             cuerpo="".join(cuerpo))
    return svg, forma
