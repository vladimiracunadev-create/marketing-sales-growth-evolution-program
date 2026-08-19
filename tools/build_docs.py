# -*- coding: utf-8 -*-
"""Generador de documentación derivada del currículo.

Escribe documentos que no deben editarse a mano porque se calculan desde
`curriculum/spec/`:

* `docs/GLOSARIO.md`            todos los conceptos con definición operacional
* `docs/FORMULAS-Y-METRICAS.md` todas las señales con su definición
* `docs/BIBLIOGRAFIA.md`        bibliografía maestra por categoría
* `docs/MAPA-DEL-CURRICULO.md`  las 24 partes y sus 336 clases
* `docs/MAPA-DE-COMPETENCIAS.md` competencias y roles por parte
* `SYLLABUS.md`                 programa completo en una página
* `FILE_INDEX.md`               índice de archivos del repositorio
* `MANIFEST.md`                 inventario cuantitativo verificable

Sin dependencias externas.
"""

from __future__ import annotations

import importlib
import json
import os
import subprocess
import sys
from collections import defaultdict

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "curriculum"))

from spec import bibliografia as bib  # noqa: E402
from spec.partes import EMPRESA, NIVELES, PARTES  # noqa: E402

FECHA = "2026-08-19"

CATEGORIAS = [
    ("marketing", "Marketing"),
    ("estrategia", "Estrategia"),
    ("cliente", "Cliente y Jobs to Be Done"),
    ("investigacion", "Investigación de mercados"),
    ("comportamiento", "Comportamiento y decisión"),
    ("marca", "Marca"),
    ("comunicacion", "Comunicación"),
    ("contenido", "Contenido y copywriting"),
    ("publicidad", "Publicidad"),
    ("precio", "Precio y monetización"),
    ("oferta", "Oferta y propuesta de valor"),
    ("ventas", "Ventas"),
    ("negociacion", "Negociación"),
    ("digital", "Marketing digital y conversión"),
    ("ecommerce", "Comercio electrónico"),
    ("growth", "Growth"),
    ("producto", "Producto"),
    ("analitica", "Analítica y experimentación"),
    ("retencion", "Retención y éxito de cliente"),
    ("revops", "Revenue operations"),
    ("direccion", "Dirección y gestión"),
    ("ia", "Inteligencia artificial"),
    ("etica", "Ética y riesgo"),
    ("pedagogia", "Pedagogía (estándar del programa)"),
]


def escribir(ruta, contenido):
    os.makedirs(os.path.dirname(ruta) or ".", exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(contenido)


def clases(num):
    return importlib.import_module("spec.clases_p{}".format(num)).CLASES


def cabecera(titulo, tipo):
    return [
        "---",
        'title: "{}"'.format(titulo),
        "type: {}".format(tipo),
        "language: es",
        "generated: true",
        "updated: {}".format(FECHA),
        "---",
        "",
        "> Documento generado por `tools/build_docs.py`. No editar a mano: los cambios se pierden en la "
        "siguiente generación. La fuente de verdad está en `curriculum/spec/`.",
        "",
    ]


def build_glosario(datos):
    entradas = {}
    for parte, cls in datos:
        for c in cls:
            for termino, definicion in c["conceptos"]:
                clave = termino.lower()
                if clave not in entradas:
                    entradas[clave] = (termino, definicion, parte, c)
    lineas = cabecera("Glosario del programa", "glossary")
    lineas += [
        "# Glosario",
        "",
        "{} términos con definición operacional, cada uno vinculado a la clase donde se trabaja. Una "
        "definición operacional indica qué observar, no sólo qué significa.".format(len(entradas)),
        "",
    ]
    por_letra = defaultdict(list)
    for clave in sorted(entradas):
        por_letra[clave[0].upper()].append(entradas[clave])
    for letra in sorted(por_letra):
        lineas += ["## {}".format(letra), "", "| Término | Definición operacional | Clase |", "|---|---|---|"]
        for termino, definicion, parte, c in por_letra[letra]:
            ruta = "../curriculum/{}/class-{}-{}.md".format(parte["slug"], c["n"], c["slug"])
            lineas.append("| **{}** | {} | [{}.{}]({}) |".format(
                termino, definicion, parte["num"], c["n"], ruta))
        lineas.append("")
    lineas += ["---", "", "[⬅ Documentación](README.md) · [Programa](../README.md)", ""]
    return "\n".join(lineas)


def build_formulas(datos):
    entradas = {}
    for parte, cls in datos:
        for c in cls:
            for nombre, definicion in c["senales"]:
                clave = nombre.lower()
                if clave not in entradas:
                    entradas[clave] = (nombre, definicion, parte, c)
    lineas = cabecera("Fórmulas y métricas", "reference")
    lineas += [
        "# Fórmulas y métricas",
        "",
        "{} señales con definición operacional. Cada una indica qué se cuenta, sobre qué base y en qué "
        "ventana. Una métrica sin esos tres elementos no es reproducible y no debe usarse para decidir.".format(
            len(entradas)),
        "",
        "## Regla del programa",
        "",
        "Toda métrica usada en un entregable debe declarar: **numerador**, **denominador**, **ventana "
        "temporal**, **fuente del dato**, **responsable**, **lectura permitida** y **lectura prohibida**. "
        "Una cifra sin esa ficha es una opinión con formato numérico.",
        "",
        "## Catálogo",
        "",
        "| Métrica | Definición operacional | Parte | Clase |",
        "|---|---|---|---|",
    ]
    for clave in sorted(entradas):
        nombre, definicion, parte, c = entradas[clave]
        ruta = "../curriculum/{}/class-{}-{}.md".format(parte["slug"], c["n"], c["slug"])
        lineas.append("| **{}** | {} | {} | [{}]({}) |".format(
            nombre, definicion, parte["num"], c["titulo"], ruta))
    lineas += [
        "",
        "## Ficha de medición (plantilla)",
        "",
        "```text",
        "Métrica:            <nombre>",
        "Pregunta que responde: <decisión que informa>",
        "Numerador:          <qué se cuenta>",
        "Denominador:        <sobre qué base>",
        "Ventana:            <periodo y criterio de corte>",
        "Segmentación:       <cortes obligatorios>",
        "Fuente:             <sistema y campo>",
        "Frecuencia:         <cada cuánto se calcula>",
        "Responsable:        <quién responde por el número>",
        "Lectura permitida:  <qué se puede concluir>",
        "Lectura prohibida:  <qué NO se puede concluir>",
        "```",
        "",
        "---",
        "",
        "[⬅ Documentación](README.md) · [Programa](../README.md)",
        "",
    ]
    return "\n".join(lineas)


def localizadores_publicados():
    """Localizador de cada obra, tomado del registro generado.

    La bibliografía sin localizador obliga a cada lector a repetir la búsqueda
    de la edición correcta. Aquí se enlaza lo que el registro ya resolvió; lo
    que sigue pendiente se dice, no se disimula.
    """
    ruta = os.path.join(RAIZ, "sources", "bibliography.json")
    if not os.path.exists(ruta):
        return {}
    with open(ruta, encoding="utf-8") as fh:
        registro = json.load(fh)
    return {e["id"]: e for e in registro["entries"]}


def build_bibliografia(datos):
    registro = localizadores_publicados()
    # Se cuentan clases, no citas: el núcleo pedagógico aparece al pie de todas
    # y no puede sumar dos veces la clase que además lo cita de forma explícita.
    usos = defaultdict(list)
    for parte, cls in datos:
        for c in cls:
            ref = "{}.{}".format(parte["num"], c["n"])
            for clave in set(list(c["libros"]) + list(bib.NUCLEO_PEDAGOGICO)):
                usos[clave].append(ref)
    usos = {k: sorted(set(v)) for k, v in usos.items()}
    lineas = cabecera("Bibliografía maestra", "bibliography")
    lineas += [
        "# Bibliografía",
        "",
        "{} obras de referencia. El repositorio **no distribuye** ninguna de ellas: cita, contrasta y enseña "
        "a usarlas de forma selectiva. El acceso debe obtenerse por biblioteca, editorial, librería o "
        "suscripción legítima.".format(len(bib.LIBROS)),
        "",
        "## Cómo se usa la bibliografía en este programa",
        "",
        "1. Cada clase indica de dos a cuatro obras con el **lente** que aporta cada una.",
        "2. La lectura se evalúa por **uso**: qué tesis modificó el diagnóstico y qué decisión cambió.",
        "3. Se exige contrastar al menos dos fuentes y registrar una tensión real entre ellas.",
        "4. Toda norma, tarifa o política viva citada en una obra debe revalidarse en su fuente oficial.",
        "",
        "## Qué está comprobado y qué es atribución",
        "",
        "**Comprobado:** que cada obra existe y cuál es la edición. Cada una tiene entrada en "
        "[`sources/bibliography.json`](../sources/bibliography.json) con un localizador que se puede "
        "seguir —**ISBN-13** para libros, **DOI** para artículos, **URL de la fuente primaria** para "
        "normas y documentación oficial— y la columna «Dónde» lo enlaza. Cuando dice «pendiente», es "
        "que no se pudo comprobar y así queda declarado: un hueco declarado es información, uno "
        "rellenado por intuición es una invención con formato de bibliografía. Comprobable con "
        "`python scripts/verify_sources.py`.",
        "",
        "**Atribución:** que la idea que cada clase señala esté en el capítulo que indica. Eso es la "
        "lectura que el programa hace de cada obra y **no está cotejada frase por frase contra el "
        "texto**. Se declara con ese detalle para que se pueda contrastar: si abres la obra y la idea "
        "no está donde se dice, corresponde reportarlo como error del material. En los términos del "
        "[estándar de evidencia](ESTANDAR-DE-EVIDENCIA.md) del propio programa, el localizador es un "
        "hecho verificado y la atribución una inferencia declarada.",
        "",
        "Las normas chilenas son la excepción: se leen completas y gratis, y cada clase enlaza su "
        "texto oficial en Ley Chile.",
        "",
    ]
    for cat, titulo in CATEGORIAS:
        items = [(k, v) for k, v in bib.LIBROS.items() if v[4] == cat]
        if not items:
            continue
        lineas += ["## {}".format(titulo), "",
                   "| Obra | Lente que aporta | Clases que la usan | Dónde |", "|---|---|---|---|"]
        for clave, (autor, obra, edicion, lente, _c) in sorted(items, key=lambda x: x[1][1]):
            refs = usos.get(clave, [])
            resumen = "{} clases".format(len(refs)) if len(refs) > 4 else (", ".join(refs) if refs else "—")
            e = registro.get(clave) or {}
            if e.get("locator"):
                etiqueta = e.get("isbn13") or e.get("doi") or "fuente primaria"
                donde = "[{}]({})".format(etiqueta, e["locator"])
            else:
                donde = "pendiente"
            lineas.append("| {} — *{}* ({}) | {} | {} | {} |".format(
                autor, obra, edicion, lente, resumen, donde))
        lineas.append("")
    lineas += [
        "## Fuentes vivas",
        "",
        "Las obras estructuran las perspectivas de cada materia. Los datos que cambian —normas, impuestos, "
        "tarifas, políticas de plataforma, capacidades de producto— deben verificarse en "
        "[`FUENTES-OFICIALES.md`](FUENTES-OFICIALES.md) y en su fuente primaria vigente.",
        "",
        "---",
        "",
        "[⬅ Documentación](README.md) · [Programa](../README.md)",
        "",
    ]
    return "\n".join(lineas)


def build_mapa_curriculo(datos):
    lineas = cabecera("Mapa del currículo", "curriculum-map")
    lineas += [
        "# Mapa del currículo",
        "",
        "24 partes · 336 clases · 48 laboratorios · 24 evaluaciones · 24 casos · 12 proyectos · 1 Capstone.",
        "",
        "## Niveles",
        "",
        "| Nivel | Partes | Resultado |",
        "|---|---|---|",
    ]
    for nivel, rango, resultado in NIVELES:
        lineas.append("| {} | {} | {} |".format(nivel, rango, resultado))
    lineas += ["", "## Detalle por parte", ""]
    for parte, cls in datos:
        lineas += [
            "### Parte {} — {}".format(parte["num"], parte["titulo"]),
            "",
            "**Nivel:** {} · **Resultado:** {} · **Artefacto:** {}".format(
                parte["nivel"], parte["resultado"], parte["artefacto"]),
            "",
            "| # | Clase | Conceptos | Señal principal |",
            "|---|---|---|---|",
        ]
        for c in cls:
            ruta = "../curriculum/{}/class-{}-{}.md".format(parte["slug"], c["n"], c["slug"])
            lineas.append("| {} | [{}]({}) | {} | {} |".format(
                c["n"], c["titulo"], ruta,
                ", ".join(t for t, _ in c["conceptos"][:2]), c["senales"][0][0]))
        lineas.append("")
    lineas += ["---", "", "[⬅ Documentación](README.md) · [Programa](../README.md)", ""]
    return "\n".join(lineas)


def build_mapa_competencias(datos):
    lineas = cabecera("Mapa de competencias y roles", "competency-map")
    lineas += [
        "# Mapa de competencias y roles",
        "",
        "Qué competencia desarrolla cada parte, a qué rol habilita y con qué artefacto se acredita.",
        "",
        "| Parte | Competencias | Roles que habilita | Artefacto acreditable |",
        "|---|---|---|---|",
    ]
    for parte, _cls in datos:
        lineas.append("| **{}** {} | {} | {} | {} |".format(
            parte["num"], parte["titulo"],
            "; ".join(parte["competencias"]),
            ", ".join(parte["roles"]),
            parte["artefacto"]))
    roles = defaultdict(list)
    for parte, _cls in datos:
        for rol in parte["roles"]:
            roles[rol].append(parte["num"])
    lineas += ["", "## Ruta por rol objetivo", "",
               "| Rol | Partes que lo desarrollan |", "|---|---|"]
    for rol in sorted(roles):
        lineas.append("| {} | {} |".format(rol, ", ".join(roles[rol])))
    lineas += [
        "",
        "> El programa no certifica ni garantiza empleo. Acredita evidencia de trabajo: los artefactos "
        "producidos son la credencial y deben poder defenderse ante preguntas técnicas.",
        "",
        "---",
        "",
        "[⬅ Documentación](README.md) · [Programa](../README.md)",
        "",
    ]
    return "\n".join(lineas)


def build_syllabus(datos):
    total_conceptos = sum(len(c["conceptos"]) for _p, cls in datos for c in cls)
    lineas = cabecera("Syllabus del programa", "syllabus")
    lineas += [
        "# Syllabus",
        "",
        "**Marketing, Sales & Growth Evolution Program** — de fundamentos comerciales a dirección de "
        "ingresos, con práctica realista, evidencia verificable y contexto chileno.",
        "",
        "## Identificación",
        "",
        "| Campo | Valor |",
        "|---|---|",
        "| Modalidad | Autoformación guiada; adaptable a instructor |",
        "| Idioma | Español |",
        "| Duración estimada | 840 a 1.000 horas de estudio dirigido |",
        "| Carga por clase | 150 minutos |",
        "| Aprobación | 80 % por evaluación y artefacto entregado |",
        "| Prerrequisitos | Ninguno formal; se asume lectura analítica y aritmética básica |",
        "",
        "## Resultado de aprendizaje del programa",
        "",
        "Al completar el programa, la persona puede diagnosticar un motor de ingresos, decidir a quién servir "
        "y con qué diferencia, construir y monetizar una oferta, operar un proceso comercial reproducible, "
        "adquirir demanda con economía verificable, retener y expandir clientes, dirigir la función de "
        "ingresos y sostener sus decisiones con evidencia ante un comité.",
        "",
        "## Caso persistente",
        "",
        "**{}** — {}".format(EMPRESA["nombre"], EMPRESA["descripcion"]),
        "",
        "Las decisiones de cada parte condicionan a las siguientes; el estado acumulado vive en "
        "`simulations/state/`.",
        "",
        "## Estructura",
        "",
        "| Nivel | Partes | Resultado |",
        "|---|---|---|",
    ]
    for nivel, rango, resultado in NIVELES:
        lineas.append("| {} | {} | {} |".format(nivel, rango, resultado))
    lineas += [
        "",
        "## Contenido por parte",
        "",
        "| # | Parte | Clases | Pregunta rectora | Artefacto |",
        "|---|---|---:|---|---|",
    ]
    for parte, cls in datos:
        lineas.append("| {} | [{}](curriculum/{}/README.md) | {} | {} | {} |".format(
            parte["num"], parte["titulo"], parte["slug"], len(cls), parte["pregunta"], parte["artefacto"]))
    lineas += [
        "",
        "## Evaluación",
        "",
        "| Instrumento | Cantidad | Peso en la ruta | Aprobación |",
        "|---|---:|---|---|",
        "| Clases con comprobación | 336 | Formativa | Autoevaluación |",
        "| Laboratorios | 48 | 30 % | 80/100 |",
        "| Evaluaciones de parte | 24 | 30 % | 80/100 |",
        "| Proyectos integradores | 12 | 25 % | 80/100 |",
        "| Capstone | 1 | 15 % | 80/100, cumplimiento eliminatorio |",
        "",
        "## Recursos incluidos",
        "",
        "- {} conceptos con definición operacional.".format(total_conceptos),
        "- {} obras de referencia con el lente que aporta cada una.".format(len(bib.LIBROS)),
        "- 5 conjuntos de datos sintéticos y 8 notebooks de analítica.",
        "- Plantillas de artefactos, prompts, especificaciones de agentes y guardarraíles de IA.",
        "- Mapa regulatorio chileno con fuentes oficiales y fecha de consulta.",
        "",
        "## Política de fuentes",
        "",
        "La fuente oficial manda sobre el material pedagógico. Toda norma citada debe revalidarse en su texto "
        "vigente antes de aplicarse a una operación real. Este programa es formación aplicada, no asesoría "
        "legal ni financiera.",
        "",
        "---",
        "",
        "[⬅ Programa](README.md) · [Currículo](curriculum/README.md) · [Documentación](docs/README.md)",
        "",
    ]
    return "\n".join(lineas)


def _archivos_versionados():
    """Lista de archivos bajo control de versiones.

    Se usa `git ls-files` para que el índice describa lo que efectivamente se
    publica y no lo que exista en el directorio de trabajo de quien lo genera.
    Sin git disponible, se recurre a un recorrido del sistema de archivos con
    las mismas exclusiones.
    """
    try:
        # `--cached --others --exclude-standard` incluye lo versionado y lo que
        # aún no se ha confirmado pero sí se publicará, y excluye lo ignorado.
        # Así el índice es idéntico antes y después del commit, que es lo que
        # verifica el trabajo de reproducibilidad en integración continua.
        salida = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard"],
                                cwd=RAIZ, capture_output=True, text=True, timeout=120)
        if salida.returncode == 0 and salida.stdout.strip():
            return sorted(l.strip() for l in salida.stdout.splitlines() if l.strip())
    except Exception:  # noqa: BLE001
        pass
    ignorar = {".git", ".github", "__pycache__", "site", ".pytest_cache", "node_modules", "evidence"}
    rutas = []
    for base, dirs, files in os.walk(RAIZ):
        dirs[:] = sorted(d for d in dirs if d not in ignorar and not d.startswith("."))
        for f in sorted(files):
            if f.startswith("."):
                continue
            rel = os.path.relpath(os.path.join(base, f), RAIZ).replace("\\", "/")
            rutas.append(rel)
    return sorted(rutas)


def build_file_index():
    agrupados = defaultdict(list)
    for ruta in _archivos_versionados():
        carpeta, _, nombre = ruta.rpartition("/")
        agrupados[carpeta or "(raíz)"].append(nombre)
    filas = [(carpeta, len(nombres), sorted(nombres)) for carpeta, nombres in sorted(agrupados.items())]
    lineas = cabecera("Índice de archivos", "file-index")
    lineas += [
        "# Índice de archivos",
        "",
        "Inventario del repositorio, excluyendo artefactos generados de compilación y control de versiones.",
        "",
        "| Directorio | Archivos | Contenido |",
        "|---|---:|---|",
    ]
    for rel, n, visibles in filas:
        muestra = ", ".join(visibles[:6]) + ("…" if len(visibles) > 6 else "")
        lineas.append("| `{}` | {} | {} |".format(rel, n, muestra))
    lineas += ["", "---", "", "[⬅ Programa](README.md)", ""]
    return "\n".join(lineas)


def build_manifest(datos):
    def contar(patron_dir, sufijo=".md", prefijo=""):
        ruta = os.path.join(RAIZ, patron_dir)
        if not os.path.isdir(ruta):
            return 0
        total = 0
        for base, _d, files in os.walk(ruta):
            total += sum(1 for f in files if f.endswith(sufijo) and f.startswith(prefijo))
        return total

    n_clases = contar("curriculum", ".md", "class-")
    n_labs = contar("labs")
    n_assess = contar("assessments")
    n_cases = contar("cases")
    n_proj = contar("projects")
    n_nb = contar("notebooks", ".ipynb")
    n_data = contar("datasets", ".csv")
    n_tpl = contar("templates")
    total_conceptos = sum(len(c["conceptos"]) for _p, cls in datos for c in cls)
    total_senales = sum(len(c["senales"]) for _p, cls in datos for c in cls)
    palabras = 0
    for base, _d, files in os.walk(os.path.join(RAIZ, "curriculum")):
        for f in files:
            if f.startswith("class-") and f.endswith(".md"):
                with open(os.path.join(base, f), encoding="utf-8") as fh:
                    palabras += len(fh.read().split())

    lineas = cabecera("Manifiesto del repositorio", "manifest")
    lineas += [
        "# Manifiesto",
        "",
        "Inventario cuantitativo verificable. Los números se calculan contando archivos reales, no se "
        "declaran a mano. Regenerar con `python tools/build_docs.py`.",
        "",
        "| Elemento | Cantidad |",
        "|---|---:|",
        "| Partes del currículo | {} |".format(len(PARTES)),
        "| Clases | {} |".format(n_clases),
        "| Palabras en las clases | {:,} |".format(palabras).replace(",", "."),
        "| Conceptos con definición operacional | {} |".format(total_conceptos),
        "| Señales y métricas definidas | {} |".format(total_senales),
        "| Obras en la bibliografía | {} |".format(len(bib.LIBROS)),
        "| Laboratorios | {} |".format(n_labs),
        "| Evaluaciones de parte | {} |".format(n_assess),
        "| Casos extendidos | {} |".format(n_cases),
        "| Proyectos integradores | {} |".format(n_proj),
        "| Notebooks de analítica | {} |".format(n_nb),
        "| Conjuntos de datos | {} |".format(n_data),
        "| Plantillas | {} |".format(n_tpl),
        "",
        "## Verificación",
        "",
        "```bash",
        "python tools/validate_repository.py",
        "python -m pytest -q",
        "```",
        "",
        "---",
        "",
        "[⬅ Programa](README.md) · [Estado](STATUS.md)",
        "",
    ]
    return "\n".join(lineas)


def main():
    datos = [(p, clases(p["num"])) for p in PARTES]

    escribir(os.path.join(RAIZ, "docs", "GLOSARIO.md"), build_glosario(datos))
    escribir(os.path.join(RAIZ, "docs", "FORMULAS-Y-METRICAS.md"), build_formulas(datos))
    escribir(os.path.join(RAIZ, "docs", "BIBLIOGRAFIA.md"), build_bibliografia(datos))
    escribir(os.path.join(RAIZ, "docs", "MAPA-DEL-CURRICULO.md"), build_mapa_curriculo(datos))
    escribir(os.path.join(RAIZ, "docs", "MAPA-DE-COMPETENCIAS.md"), build_mapa_competencias(datos))
    escribir(os.path.join(RAIZ, "SYLLABUS.md"), build_syllabus(datos))
    escribir(os.path.join(RAIZ, "MANIFEST.md"), build_manifest(datos))
    escribir(os.path.join(RAIZ, "FILE_INDEX.md"), build_file_index())

    print("Documentación derivada generada: 8 archivos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
