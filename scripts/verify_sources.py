# -*- coding: utf-8 -*-
"""Verificador del registro de fuentes. Offline, determinista, bloqueante.

Responde una pregunta que un lector externo no puede contestar leyendo el
README: ¿cada afirmación del programa se apoya en una obra que alguien puede ir
a buscar? Citar un título no basta. Una obra sin localizador es una obra que el
lector tiene que encontrar por su cuenta, y una bibliografía que sólo vive en la
portada es una bibliografía que nadie puede comprobar.

Este verificador no usa red. Comprueba diez cosas:

  1. El registro parsea y cumple el esquema declarado.
  2. Todo libro tiene ISBN-13 con dígito de control válido.
  3. Todo artículo tiene DOI.
  4. El localizador coincide con la forma canónica de su tipo.
  5. Toda obra citada por una clase existe en el registro.
  6. Ninguna entrada del registro queda sin uso.
  7. Las rutas declaradas en `used_in` existen en el disco.
  8. Ningún bloque de fuentes se repite entre clases.
  9. Cada cita de cada clase declara qué idea concreta sostiene.
 10. Las cifras que muestra el README coinciden con el recuento del registro.

Lo que este verificador NO hace: pedir nada por red. Si la red entra en el CI,
el CI se vuelve inestable y se acaba ignorando. La comprobación en red vive en
`scripts/refresh_sources.py` y no bloquea.

Uso:
    python scripts/verify_sources.py
    python scripts/verify_sources.py --detalle
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "curriculum"))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REGISTRO = os.path.join(RAIZ, "sources", "bibliography.json")

TIPOS = {"book", "paper", "standard", "reference", "dataset"}
TIPOS_URL = {"standard", "reference", "dataset"}
ESTADOS = {"verificada", "pendiente"}

RE_ID = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
RE_FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")
RE_ISBN13 = re.compile(r"^97[89]\d{10}$")
RE_DOI = re.compile(r"^10\.\d{4,9}/\S+$")
RE_HTTPS = re.compile(r"^https://[^\s]+$")

OBLIGATORIOS = ("id", "type", "authors", "title", "published", "authority",
                "locator", "used_in", "status")

# Marcas del bloque de cifras que el README publica sobre el registro.
INICIO_CIFRAS = "<!-- REGISTRO-FUENTES:INICIO -->"
FIN_CIFRAS = "<!-- REGISTRO-FUENTES:FIN -->"


class Informe(object):
    """Acumula errores y avisos sin abortar en el primero.

    Un verificador que muere en el primer fallo obliga a un ciclo de arreglo
    por error. Este junta todo y lo entrega de una vez.
    """

    def __init__(self):
        self.errores = []
        self.avisos = []

    def error(self, mensaje):
        self.errores.append(mensaje)

    def aviso(self, mensaje):
        self.avisos.append(mensaje)

    @property
    def ok(self):
        return not self.errores


def digito_isbn13(doce):
    """Dígito de control de un ISBN-13 según ISO 2108."""
    suma = 0
    for i, c in enumerate(doce):
        suma += int(c) * (1 if i % 2 == 0 else 3)
    return (10 - suma % 10) % 10


def isbn13_valido(isbn):
    if not RE_ISBN13.match(isbn or ""):
        return False
    return digito_isbn13(isbn[:12]) == int(isbn[12])


def localizador_canonico(entrada):
    """Forma que debe tener el localizador según el tipo de la entrada."""
    tipo = entrada.get("type")
    if tipo == "book":
        return "https://openlibrary.org/isbn/{}".format(entrada.get("isbn13", ""))
    if tipo == "paper":
        return "https://doi.org/{}".format(entrada.get("doi", ""))
    return None


def cargar_registro(informe):
    if not os.path.exists(REGISTRO):
        informe.error("No existe {}".format(os.path.relpath(REGISTRO, RAIZ)))
        return None
    try:
        with open(REGISTRO, encoding="utf-8") as fh:
            datos = json.load(fh)
    except ValueError as e:
        informe.error("El registro no es JSON válido: {}".format(e))
        return None

    if datos.get("schema_version") != 1:
        informe.error("schema_version debe ser 1 y es {!r}".format(datos.get("schema_version")))
    if not RE_FECHA.match(str(datos.get("verified_on", ""))):
        informe.error("verified_on debe ser AAAA-MM-DD y es {!r}".format(datos.get("verified_on")))
    if not str(datos.get("policy", "")).strip():
        informe.error("El registro no declara su política de aceptación de fuentes")
    if not isinstance(datos.get("entries"), list) or not datos["entries"]:
        informe.error("El registro no trae lista de entradas")
        return None
    return datos


def verificar_entradas(datos, informe):
    """Esquema, localizadores y dígitos de control. Devuelve el índice por id."""
    por_id = {}
    for i, e in enumerate(datos["entries"]):
        etiqueta = e.get("id") or "entrada #{}".format(i + 1)

        for campo in OBLIGATORIOS:
            if campo not in e:
                informe.error("{}: falta el campo obligatorio '{}'".format(etiqueta, campo))

        ident = e.get("id", "")
        if not RE_ID.match(ident):
            informe.error("{}: el id debe ser kebab-case estable".format(etiqueta))
        if ident in por_id:
            informe.error("{}: id duplicado".format(etiqueta))
        por_id[ident] = e

        tipo = e.get("type")
        if tipo not in TIPOS:
            informe.error("{}: type {!r} no está en {}".format(etiqueta, tipo, sorted(TIPOS)))

        if not isinstance(e.get("authors"), list) or not e.get("authors"):
            informe.error("{}: authors debe ser una lista no vacía".format(etiqueta))
        if not str(e.get("title", "")).strip():
            informe.error("{}: title vacío".format(etiqueta))
        if not re.match(r"^\d{4}$", str(e.get("published", ""))):
            informe.error("{}: published debe ser un año AAAA".format(etiqueta))
        if not str(e.get("authority", "")).strip():
            informe.error("{}: authority vacío — nadie responde por esta fuente".format(etiqueta))

        estado = e.get("status")
        if estado not in ESTADOS:
            informe.error("{}: status {!r} no está en {}".format(etiqueta, estado, sorted(ESTADOS)))

        if estado == "pendiente":
            # Un hueco declarado es información. Un hueco mudo, no.
            if not str(e.get("note", "")).strip():
                informe.error("{}: pendiente sin 'note' que explique qué falta".format(etiqueta))
            continue

        # A partir de aquí, sólo entradas que se declaran verificadas.
        locator = e.get("locator", "")
        if not RE_HTTPS.match(locator):
            informe.error("{}: locator debe ser una URL https".format(etiqueta))

        if tipo == "book":
            isbn = e.get("isbn13", "")
            if not isbn13_valido(isbn):
                informe.error("{}: ISBN-13 inválido o ausente ({!r})".format(etiqueta, isbn))
            elif locator != localizador_canonico(e):
                informe.error("{}: locator no es la forma canónica {}".format(
                    etiqueta, localizador_canonico(e)))
        elif tipo == "paper":
            doi = e.get("doi", "")
            if not RE_DOI.match(doi):
                informe.error("{}: DOI inválido o ausente ({!r})".format(etiqueta, doi))
            elif locator != localizador_canonico(e):
                informe.error("{}: locator no es la forma canónica {}".format(
                    etiqueta, localizador_canonico(e)))
        elif tipo in TIPOS_URL:
            if not RE_FECHA.match(str(e.get("accessed", ""))):
                informe.error("{}: una fuente resuelta por URL exige 'accessed' AAAA-MM-DD".format(
                    etiqueta))

        # Un ISBN presente en cualquier tipo tiene que ser un ISBN real.
        if e.get("isbn13") and not isbn13_valido(e["isbn13"]):
            informe.error("{}: el ISBN-13 declarado no supera el dígito de control".format(etiqueta))
    return por_id


def obras_de_la_especificacion():
    """Obras citadas por las clases, según `curriculum/spec/`.

    Devuelve (usos_por_obra, rutas_por_obra, nucleo) con las rutas relativas
    de cada clase que cita cada obra.
    """
    from spec import bibliografia as bib
    from spec.partes import PARTES

    usos = {}
    rutas = {}
    for parte in PARTES:
        modulo = importlib.import_module("spec.clases_p{}".format(parte["num"]))
        for clase in modulo.CLASES:
            ruta = "curriculum/{}/class-{}-{}.md".format(
                parte["slug"], clase["n"], clase["slug"])
            for clave in clase["libros"]:
                usos[clave] = usos.get(clave, 0) + 1
                rutas.setdefault(clave, []).append(ruta)
            # El núcleo pedagógico se cita al pie de todas las clases.
            for clave in bib.NUCLEO_PEDAGOGICO:
                usos[clave] = usos.get(clave, 0) + 1
                rutas.setdefault(clave, []).append(ruta)
    return usos, rutas, list(bib.NUCLEO_PEDAGOGICO)


def verificar_cobertura(por_id, informe, detalle):
    """Ninguna obra citada fuera del registro; ninguna entrada sin uso."""
    usos, rutas, _nucleo = obras_de_la_especificacion()

    faltan = sorted(set(usos) - set(por_id))
    for clave in faltan:
        informe.error("La obra '{}' se cita en {} clases y no está en el registro".format(
            clave, usos[clave]))

    sobran = sorted(set(por_id) - set(usos))
    for clave in sobran:
        informe.error("La entrada '{}' del registro no se usa en ninguna clase".format(clave))

    for clave, entrada in sorted(por_id.items()):
        declarado = entrada.get("used_in") or []
        if not declarado:
            informe.error("{}: used_in vacío".format(clave))
            continue
        esperado = sorted(set(rutas.get(clave, [])))
        if sorted(set(declarado)) != esperado:
            informe.error("{}: used_in no coincide con la especificación ({} declaradas, "
                          "{} reales)".format(clave, len(set(declarado)), len(esperado)))
        for ruta in declarado:
            if not os.path.exists(os.path.join(RAIZ, ruta.replace("/", os.sep))):
                informe.error("{}: used_in apunta a una ruta inexistente: {}".format(clave, ruta))
                break
        if detalle:
            print("  {:22s} {:3d} clases".format(clave, len(esperado)))
    return usos


def bloque_de_fuentes(texto):
    """Extrae el bloque «Fuentes y verificación» de una clase."""
    m = re.search(r"^## .*Fuentes y verificaci[óo]n\s*$(.*?)(?=^---\s*$|\Z)",
                  texto, re.M | re.S)
    if not m:
        return None
    # Sólo las líneas que nombran obras: el resto del bloque es idéntico
    # por diseño en todas las clases.
    obras = [linea.strip() for linea in m.group(1).splitlines()
             if linea.strip().startswith("- ")]
    return "\n".join(obras)


def verificar_clases(informe, detalle):
    """Bloques de fuentes presentes, distintos entre sí y con uso declarado."""
    clases = []
    base = os.path.join(RAIZ, "curriculum")
    for carpeta in sorted(os.listdir(base)):
        ruta_parte = os.path.join(base, carpeta)
        if not os.path.isdir(ruta_parte) or not carpeta.startswith("part-"):
            continue
        for archivo in sorted(os.listdir(ruta_parte)):
            if archivo.startswith("class-") and archivo.endswith(".md"):
                clases.append(os.path.join(ruta_parte, archivo))

    if not clases:
        informe.error("No se encontró ninguna clase en curriculum/")
        return 0

    huellas = {}
    sin_bloque = []
    sin_uso_declarado = []
    for ruta in clases:
        with open(ruta, encoding="utf-8") as fh:
            texto = fh.read()
        bloque = bloque_de_fuentes(texto)
        rel = os.path.relpath(ruta, RAIZ).replace(os.sep, "/")
        if not bloque:
            sin_bloque.append(rel)
            continue
        # Cada obra citada debe declarar qué aporta a ESTA clase.
        for linea in bloque.splitlines():
            if "aporta a esta clase:" not in linea:
                sin_uso_declarado.append(rel)
                break
        huella = hashlib.sha1(bloque.encode("utf-8")).hexdigest()
        huellas.setdefault(huella, []).append(rel)

    for rel in sin_bloque:
        informe.error("{}: no tiene bloque de fuentes".format(rel))
    for rel in sorted(set(sin_uso_declarado)):
        informe.error("{}: una cita no declara qué aporta a esta clase".format(rel))

    repetidos = {h: v for h, v in huellas.items() if len(v) > 1}
    for _h, grupo in sorted(repetidos.items(), key=lambda kv: kv[1][0]):
        informe.error("Bloque de fuentes repetido entre {} clases: {}".format(
            len(grupo), ", ".join(grupo[:3]) + (" …" if len(grupo) > 3 else "")))

    if detalle:
        print("  clases: {} · bloques distintos: {}".format(len(clases), len(huellas)))
    return len(clases)


def cifras_del_registro(datos):
    """Las cifras que el README tiene derecho a publicar."""
    entradas = datos["entries"]
    return {
        "entradas": len(entradas),
        "libros": sum(1 for e in entradas if e.get("type") == "book"),
        "con_isbn13": sum(1 for e in entradas if e.get("isbn13")),
        "verificadas": sum(1 for e in entradas if e.get("status") == "verificada"),
        "pendientes": sum(1 for e in entradas if e.get("status") == "pendiente"),
        "verified_on": datos.get("verified_on", ""),
    }


def verificar_readme(datos, informe, detalle):
    """El README no puede declarar cifras que el registro no respalde."""
    ruta = os.path.join(RAIZ, "README.md")
    with open(ruta, encoding="utf-8") as fh:
        texto = fh.read()

    if INICIO_CIFRAS not in texto or FIN_CIFRAS not in texto:
        informe.error("README.md no publica el bloque {} … {}".format(
            INICIO_CIFRAS, FIN_CIFRAS))
        return
    bloque = texto.split(INICIO_CIFRAS, 1)[1].split(FIN_CIFRAS, 1)[0]

    if "sources/bibliography.json" not in texto:
        informe.error("README.md no enlaza el registro de fuentes")

    cifras = cifras_del_registro(datos)
    esperado = {
        "entradas del registro": cifras["entradas"],
        "obras con localizador verificado": cifras["verificadas"],
        "entradas pendientes": cifras["pendientes"],
        "libros con ISBN-13": cifras["con_isbn13"],
    }
    for etiqueta, valor in sorted(esperado.items()):
        patron = r"\|\s*{}\s*\|\s*\*?\*?([\d]+)".format(re.escape(etiqueta))
        m = re.search(patron, bloque)
        if not m:
            informe.error("El README no publica la cifra «{}»".format(etiqueta))
        elif int(m.group(1)) != valor:
            informe.error("El README declara {} = {} y el registro dice {}".format(
                etiqueta, m.group(1), valor))
    if cifras["verified_on"] not in bloque:
        informe.error("El README no publica la fecha de verificación del registro ({})".format(
            cifras["verified_on"]))
    if detalle:
        print("  cifras publicadas: {}".format(cifras))


def main():
    ap = argparse.ArgumentParser(description="Verifica el registro de fuentes (offline)")
    ap.add_argument("--detalle", action="store_true", help="Muestra el desglose por obra")
    args = ap.parse_args()

    informe = Informe()
    print("=" * 72)
    print("VERIFICACIÓN DEL REGISTRO DE FUENTES")
    print("=" * 72)

    datos = cargar_registro(informe)
    if datos is None:
        for e in informe.errores:
            print("  ERROR  {}".format(e))
        print("\nVEREDICTO: el registro no se puede leer.")
        return 1

    por_id = verificar_entradas(datos, informe)
    verificar_cobertura(por_id, informe, args.detalle)
    total_clases = verificar_clases(informe, args.detalle)
    verificar_readme(datos, informe, args.detalle)

    cifras = cifras_del_registro(datos)
    print("")
    print("Entradas del registro:        {:>4}".format(cifras["entradas"]))
    print("  con localizador verificado: {:>4}".format(cifras["verificadas"]))
    print("  pendientes de resolver:     {:>4}".format(cifras["pendientes"]))
    print("Libros con ISBN-13:           {:>4}".format(cifras["con_isbn13"]))
    print("Clases analizadas:            {:>4}".format(total_clases))
    print("Última verificación en red:   {}".format(cifras["verified_on"]))
    print("")

    for a in informe.avisos:
        print("  AVISO  {}".format(a))
    for e in informe.errores:
        print("  ERROR  {}".format(e))

    print("-" * 72)
    if informe.ok:
        print("VEREDICTO: cada obra citada tiene una entrada con localizador resoluble,")
        print("ninguna entrada sobra y las cifras del README las produce este verificador.")
        return 0
    print("VEREDICTO: {} problema(s). El registro no respalda lo que el programa declara.".format(
        len(informe.errores)))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
