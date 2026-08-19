# -*- coding: utf-8 -*-
"""Generador de las rutas profesionales por rol.

Lee `curriculum/spec/roles.py` y escribe una página por rol en `rutas/`, más el
índice `rutas/README.md`. Cada página describe el puesto, el día a día, las
competencias, el recorrido concreto dentro del programa, los artefactos que lo
acreditan, la progresión de carrera y los mitos habituales.

Uso:
    python tools/build_rutas.py
"""

from __future__ import annotations

import importlib
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "curriculum"))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from spec.partes import PARTES, por_numero  # noqa: E402
from spec.roles import FAMILIAS, ROLES  # noqa: E402

FECHA = "2026-08-19"
SALIDA = os.path.join(RAIZ, "rutas")

_CACHE_CLASES = {}


def clases_de(num):
    if num not in _CACHE_CLASES:
        _CACHE_CLASES[num] = importlib.import_module("spec.clases_p{}".format(num)).CLASES
    return _CACHE_CLASES[num]


def clase(num_parte, n):
    for c in clases_de(num_parte):
        if c["n"] == n:
            return c
    raise KeyError("Clase {}.{} inexistente".format(num_parte, n))


def escribir(ruta, contenido):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(contenido.rstrip() + "\n")


def enlace_parte(num):
    p = por_numero(num)
    return "[**Parte {} — {}**](../curriculum/{}/README.md)".format(num, p["titulo"], p["slug"])


def enlace_clase(num_parte, n):
    p = por_numero(num_parte)
    c = clase(num_parte, n)
    return "[{}.{} · {}](../curriculum/{}/class-{}-{}.md)".format(
        num_parte, n, c["titulo"], p["slug"], n, c["slug"])


def render_rol(rol):
    p = []
    a = p.append

    a("---")
    a('title: "Ruta profesional — {}"'.format(rol["titulo"]))
    a("type: career-path")
    a("language: es")
    a("role: {}".format(rol["slug"]))
    a("family: {}".format(rol["familia"]))
    a("updated: {}".format(FECHA))
    a("---")
    a("")
    a("# {} {}".format(rol["emoji"], rol["titulo"]))
    a("")
    a("> {}".format(rol["resumen"]))
    a(">")
    a("> **Nivel de entrada:** {} · **Foco:** {} · **Señal de mercado:** {}".format(
        rol["nivel"], rol["foco"], rol["credencial"]))
    a("")

    a("## 🧭 Qué es y por qué importa")
    a("")
    for parrafo in rol["que_es"]:
        a(parrafo)
        a("")

    a("## 🗓️ Un día en el puesto")
    a("")
    for item in rol["dia"]:
        a("- {}".format(item))
    a("")

    a("## 🧠 Qué necesitas saber")
    a("")
    a("### Conocimiento del oficio")
    a("")
    for item in rol["tecnico"]:
        a("- {}".format(item))
    a("")
    a("### Herramientas")
    a("")
    a("```text")
    a(rol["herramientas"])
    a("```")
    a("")
    a("La herramienta no hace al profesional. Lo que el mercado paga es el **criterio** para decidir qué "
      "medir, qué descartar y qué recomendar cuando la evidencia es incompleta.")
    a("")
    a("### Habilidades no técnicas")
    a("")
    for item in rol["blandas"]:
        a("- {}".format(item))
    a("")

    a("## 📚 Tu ruta en el programa")
    a("")
    a("Orden recomendado. Todas las rutas asumen que empiezas por la "
      "[parte 01](../curriculum/part-01-marketing-y-ventas-fundamentos-del-sistema-comercial/README.md), "
      "que entrega el mapa del sistema comercial completo.")
    a("")
    for i, (num, por_que) in enumerate(rol["ruta"], start=1):
        a("{}. 📚 {} · {}".format(i, enlace_parte(num), por_que))
    a("")
    a("### Clases por las que empezar")
    a("")
    for num_parte, n, por_que in rol["clases"]:
        a("- 🎯 {} — {}".format(enlace_clase(num_parte, n), por_que))
    a("")

    a("## 🧪 Práctica y evaluación")
    a("")
    a("| Recurso | Ruta |")
    a("|---|---|")
    for num in rol["labs"]:
        pt = por_numero(num)
        a("| 🧪 Laboratorios de la parte {} — {} | [`labs/part-{}/`](../labs/part-{}/) |".format(
            num, pt["titulo"], num, num))
    for num in rol["labs"][:2]:
        a("| ✅ Evaluación de la parte {} | [`assessments/part-{}-assessment.md`](../assessments/part-{}-assessment.md) |".format(
            num, num, num))
    a("| 📋 Rúbricas y criterios | [`docs/EVALUACION-Y-RUBRICAS.md`](../docs/EVALUACION-Y-RUBRICAS.md) |")
    a("| 📂 Estándar de evidencia | [`docs/ESTANDAR-DE-EVIDENCIA.md`](../docs/ESTANDAR-DE-EVIDENCIA.md) |")
    a("")

    a("## 📥 Artefactos que acreditan este rol")
    a("")
    a("Estos son los entregables que conviene llevar a una postulación. No describen responsabilidades: "
      "muestran trabajo que alguien puede auditar.")
    a("")
    for art in rol["artefactos"]:
        a("- [ ] {}".format(art))
    a("")

    a("## 🎓 Credenciales y señales de mercado")
    a("")
    for cred in rol["credenciales"]:
        a("- {}".format(cred))
    a("")

    a("## 📈 Progresión de carrera y rangos")
    a("")
    a(rol["progresion"])
    a("")
    a("Rangos **orientativos y aproximados**. Varían mucho por sector, tamaño de empresa, industria y "
      "experiencia; son referencia de mercado, no promesa:")
    a("")
    a("```text")
    a(rol["salario"])
    a("```")
    a("")

    a("## ⚠️ Mitos y errores comunes")
    a("")
    a("| Mito | Realidad |")
    a("|---|---|")
    for mito, realidad in rol["mitos"]:
        a("| {} | {} |".format(mito, realidad))
    a("")

    a("## ⚖️ Nota de honestidad")
    a("")
    a(rol["honestidad"])
    a("")
    a("> El programa **no certifica ni garantiza empleo**. Acredita evidencia de trabajo: los artefactos son "
      "la credencial y deben poder defenderse ante preguntas técnicas.")
    a("")

    a("---")
    a("")
    a("[⬅ Todas las rutas](README.md) · [Currículo](../curriculum/README.md) · "
      "[Ruta de aprendizaje](../docs/RUTA-DE-APRENDIZAJE.md) · [Programa](../README.md)")
    return "\n".join(p)


def render_indice():
    p = []
    a = p.append

    a("---")
    a('title: "Rutas profesionales por rol"')
    a("type: career-index")
    a("language: es")
    a("updated: {}".format(FECHA))
    a("---")
    a("")
    a("# 🧭 Rutas profesionales por rol")
    a("")
    a("El programa tiene **336 clases**; no todas son para todos a la vez. Estas {} rutas ordenan el "
      "recorrido según el puesto al que apuntas: qué partes hacer, en qué orden, con qué laboratorios "
      "practicar y qué artefactos llevar a una postulación.".format(len(ROLES)))
    a("")
    a("> Cada ruta asume que empiezas por la "
      "[parte 01](../curriculum/part-01-marketing-y-ventas-fundamentos-del-sistema-comercial/README.md): "
      "el mapa del sistema comercial es el cimiento común de todos los roles.")
    a("")
    a("## Elegir en un minuto")
    a("")
    a("| Si te interesa… | Mira esta ruta |")
    a("|---|---|")
    a("| Que los números signifiquen lo que dicen | [{} Analista de marketing]({}.md) |".format("📊", "analista-de-marketing"))
    a("| Decidir dónde compite la empresa | [{} Marketing manager]({}.md) |".format("🎯", "marketing-manager"))
    a("| Traducir producto en oferta que se vende | [{} Product marketing]({}.md) |".format("🧩", "product-marketing"))
    a("| Experimentar sobre todo el recorrido | [{} Growth manager]({}.md) |".format("🚀", "growth-manager"))
    a("| Abrir conversaciones desde cero | [{} SDR / BDR]({}.md) |".format("📞", "sdr-bdr"))
    a("| Responder por un número de cierre | [{} Ejecutivo comercial]({}.md) |".format("🤝", "ejecutivo-comercial"))
    a("| Que el cliente obtenga lo que compró | [{} Customer Success]({}.md) |".format("🔁", "customer-success"))
    a("| Que las tres áreas usen la misma cifra | [{} RevOps]({}.md) |".format("⚙️", "revops"))
    a("| Invertir en medios y responder por ello | [{} Performance marketer]({}.md) |".format("📈", "performance-marketer"))
    a("| Escribir lo que informa y convierte | [{} Content manager]({}.md) |".format("✍️", "content-manager"))
    a("| Operar una tienda que deje margen | [{} E-commerce manager]({}.md) |".format("🛒", "ecommerce-manager"))
    a("| Que el mercado te recuerde | [{} Brand manager]({}.md) |".format("🎨", "brand-manager"))
    a("| Decidir cómo llega la oferta al mercado | [{} Head of GTM]({}.md) |".format("🗺️", "head-of-gtm"))
    a("| Dirigir marketing ante un directorio | [{} CMO]({}.md) |".format("🏛️", "cmo"))
    a("| Dirigir un equipo comercial | [{} VP de ventas]({}.md) |".format("🏅", "vp-sales"))
    a("| Dirigir el motor de ingresos completo | [{} CRO]({}.md) |".format("👑", "cro"))
    a("| Vender lo que estás construyendo | [{} Founder]({}.md) |".format("🚩", "founder"))
    a("")

    for familia in FAMILIAS:
        roles = [r for r in ROLES if r["familia"] == familia]
        if not roles:
            continue
        a("## {}".format(familia))
        a("")
        for rol in roles:
            a("### {} [{}]({}.md)".format(rol["emoji"], rol["titulo"], rol["slug"]))
            a("")
            a(rol["resumen"])
            a("")
            a("**Nivel:** {} · **Foco:** {}".format(rol["nivel"], rol["foco"]))
            a("")
            partes = ", ".join(n for n, _ in rol["ruta"])
            a("📚 Partes: {} · 🧪 Labs: {} · 📖 **[Guía completa del rol →]({}.md)**".format(
                partes, ", ".join(rol["labs"]), rol["slug"]))
            a("")

    a("## Cobertura del programa por rol")
    a("")
    a("| Rol | Familia | Partes principales | Artefacto faro |")
    a("|---|---|---|---|")
    for rol in ROLES:
        partes = ", ".join(n for n, _ in rol["ruta"][:4])
        a("| {} [{}]({}.md) | {} | {} | {} |".format(
            rol["emoji"], rol["titulo"], rol["slug"], rol["familia"], partes, rol["artefactos"][0]))
    a("")

    a("## Cómo usar una ruta")
    a("")
    a("1. **Lee la guía completa del rol** antes de empezar: describe el día a día real, no una lista de "
      "temas.")
    a("2. **Sigue el orden de partes** indicado; cada una supone la anterior.")
    a("3. **Produce los artefactos** de la sección de portafolio. Son la credencial.")
    a("4. **Aprueba las evaluaciones** de las partes de tu ruta con 80/100 o más.")
    a("5. **Documenta cada artefacto** con problema, método, decisiones tomadas y descartadas.")
    a("")
    a("> Seis artefactos documentados muestran más competencia que veinte incompletos.")
    a("")
    a("---")
    a("")
    a("[⬅ Programa](../README.md) · [Currículo](../curriculum/README.md) · "
      "[Ruta de aprendizaje](../docs/RUTA-DE-APRENDIZAJE.md) · "
      "[Mapa de competencias](../docs/MAPA-DE-COMPETENCIAS.md)")
    return "\n".join(p)


def main():
    os.makedirs(SALIDA, exist_ok=True)
    esperados = {"README.md"} | {"{}.md".format(r["slug"]) for r in ROLES}
    for existente in os.listdir(SALIDA):
        if existente.endswith(".md") and existente not in esperados:
            os.remove(os.path.join(SALIDA, existente))
            print("Eliminado obsoleto: rutas/{}".format(existente))

    for rol in ROLES:
        escribir(os.path.join(SALIDA, "{}.md".format(rol["slug"])), render_rol(rol))
    escribir(os.path.join(SALIDA, "README.md"), render_indice())

    print("Rutas generadas: {} roles + índice".format(len(ROLES)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
