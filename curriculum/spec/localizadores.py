# -*- coding: utf-8 -*-
"""Localizador verificable de cada obra de la bibliografía.

`bibliografia.py` dice **qué** obra es y **para qué** sirve dentro del programa.
Este módulo dice **dónde se resuelve** y **quién responde** por ella. Están
separados a propósito: el lente pedagógico de una obra no cambia cuando cambia
su edición, y el localizador no debería obligar a tocar la bibliografía.

Se admiten exactamente tres formas de localizador, y ninguna otra:

* ``book``      ISBN-13 con dígito de control válido -> ``openlibrary.org/isbn/{isbn13}``
* ``paper``     DOI -> ``doi.org/{doi}``
* ``standard`` / ``reference``   URL https de la fuente primaria, con fecha de consulta

Reglas que este archivo obedece:

1. **Nada se inventa.** Cada ISBN-13 procede de un registro real de
   OpenLibrary, comprobado uno a uno contra el título, la autoría, la editorial
   y el año de la edición que el programa declara. Lo que no se pudo resolver
   queda con ``"estado": "pendiente"`` y una nota que dice qué falta. Un hueco
   declarado es información; un hueco rellenado por intuición es una invención
   con formato de bibliografía.
2. **Nada se borra.** Una fuente que deja de resolver se marca y se corrige a
   mano; no se elimina para que el recuento quede bonito.
3. **Las cifras no se escriben.** `scripts/verify_sources.py` las cuenta y
   comprueba que el README publique exactamente esas.

Claves de cada entrada:

===============  ==========================================================
``tipo``         book | paper | standard | reference | dataset
``autores``      autoría normalizada, «Apellido, Nombre»
``publicado``    año de la edición de referencia que citan las clases
``isbn13``       libros
``doi``          artículos y normas que tienen DOI
``url``          normas y documentación oficial
``autoridad``    editorial u organismo que responde por la fuente
``consultado``   fecha de la última comprobación de una URL
``comprobacion`` "manual" si el sitio rechaza clientes automatizados
``nota``         qué hay que saber al usar esta entrada
``estado``       verificada | pendiente
===============  ==========================================================

La revalidación en red la hace `scripts/refresh_sources.py`, que escribe
`sources/verification-log.json` y nunca bloquea el CI.
"""

from __future__ import annotations

# Fecha de la última revalidación completa contra openlibrary.org y las fuentes
# oficiales. La actualiza `scripts/refresh_sources.py`.
VERIFICADO_EN = "2026-08-19"

POLITICA = (
    "Toda afirmación del programa se apoya en una entrada de este registro. "
    "Ninguna entrada se acepta sin localizador verificable: ISBN-13 con dígito "
    "de control válido para libros, DOI para artículos, y URL de la fuente "
    "primaria con fecha de consulta para normas y documentación oficial. Lo que "
    "no resuelve se marca como pendiente; no se borra ni se rellena."
)

LOCALIZADORES = {
    # --- Marca ---------------------------------------------------------------
    "aaker": {
        "tipo": "book",
        "autores": ["Aaker, David A."],
        "publicado": "1996",
        "isbn13": "9780029001516",
        "autoridad": "Free Press",
        "estado": "verificada",
    },
    "keller-brand": {
        "tipo": "book",
        "autores": ["Keller, Kevin Lane", "Swaminathan, Vanitha"],
        "publicado": "2019",
        "isbn13": "9780134892498",
        "autoridad": "Pearson",
        "estado": "verificada",
    },
    "wheeler": {
        "tipo": "book",
        "autores": ["Wheeler, Alina", "Meyerson, Rob"],
        "publicado": "2024",
        "isbn13": "9781119984825",
        "autoridad": "John Wiley & Sons",
        "estado": "verificada",
    },

    # --- Pedagogía del programa ----------------------------------------------
    "ambrose": {
        "tipo": "book",
        "autores": [
            "Ambrose, Susan A.",
            "Bridges, Michael W.",
            "DiPietro, Michele",
            "Lovett, Marsha C.",
            "Norman, Marie K.",
        ],
        "publicado": "2010",
        "isbn13": "9780470484104",
        "autoridad": "Jossey-Bass",
        "estado": "verificada",
    },
    "brown-mis": {
        "tipo": "book",
        "autores": ["Brown, Peter C.", "Roediger III, Henry L.", "McDaniel, Mark A."],
        "publicado": "2014",
        "isbn13": "9780674419377",
        "autoridad": "Harvard University Press",
        "estado": "verificada",
    },
    "ellet": {
        "tipo": "book",
        "autores": ["Ellet, William"],
        "publicado": "2018",
        "isbn13": "9781633696150",
        "autoridad": "Harvard Business Review Press",
        "estado": "verificada",
    },
    "ericsson": {
        "tipo": "book",
        "autores": ["Ericsson, Anders", "Pool, Robert"],
        "publicado": "2016",
        "isbn13": "9781473513143",
        "autoridad": "Penguin Random House",
        "estado": "verificada",
    },
    "wiggins": {
        "tipo": "book",
        "autores": ["Wiggins, Grant", "McTighe, Jay"],
        "publicado": "2005",
        "isbn13": "9781416600350",
        "autoridad": "ASCD",
        "estado": "verificada",
    },

    # --- Comportamiento y decisión -------------------------------------------
    "ariely": {
        "tipo": "book",
        "autores": ["Ariely, Dan"],
        "publicado": "2008",
        "isbn13": "9780061353239",
        "autoridad": "HarperCollins",
        "estado": "verificada",
    },
    "cialdini": {
        "tipo": "book",
        "autores": ["Cialdini, Robert B."],
        "publicado": "2021",
        "isbn13": "9780062937650",
        "autoridad": "Harper Business",
        "estado": "verificada",
    },
    "kahneman": {
        "tipo": "book",
        "autores": ["Kahneman, Daniel"],
        "publicado": "2011",
        "isbn13": "9780141918921",
        "autoridad": "Penguin Books",
        "estado": "verificada",
    },
    "solomon": {
        "tipo": "book",
        "autores": ["Solomon, Michael R."],
        "publicado": "2019",
        "isbn13": "9781292318103",
        "autoridad": "Pearson",
        "estado": "verificada",
    },
    "thaler": {
        "tipo": "book",
        "autores": ["Thaler, Richard H.", "Sunstein, Cass R."],
        "publicado": "2021",
        "isbn13": "9780143137009",
        "autoridad": "Penguin Books",
        "estado": "verificada",
    },

    # --- Ventas --------------------------------------------------------------
    "bertuzzi": {
        "tipo": "book",
        "autores": ["Bertuzzi, Trish"],
        "publicado": "2016",
        "isbn13": "9780692622032",
        "autoridad": "Moore-Lake",
        "estado": "verificada",
    },
    "blount": {
        "tipo": "book",
        "autores": ["Blount, Jeb"],
        "publicado": "2015",
        "isbn13": "9781119176305",
        "autoridad": "John Wiley & Sons",
        "estado": "verificada",
    },
    "dixon-challenger": {
        "tipo": "book",
        "autores": ["Dixon, Matthew", "Adamson, Brent"],
        "publicado": "2011",
        "isbn13": "9781591844358",
        "autoridad": "Portfolio/Penguin",
        "estado": "verificada",
    },
    "dixon-customer": {
        "tipo": "book",
        "autores": ["Adamson, Brent", "Dixon, Matthew"],
        "publicado": "2015",
        "isbn13": "9780241196564",
        "autoridad": "Penguin Books",
        "estado": "verificada",
    },
    "keenan": {
        "tipo": "book",
        "autores": ["Keenan"],
        "publicado": "2018",
        "isbn13": "9781732891005",
        "autoridad": "A Sales Guy Publishing",
        "estado": "verificada",
    },
    "miller-heiman": {
        "tipo": "book",
        "autores": ["Miller, Robert B.", "Heiman, Stephen E."],
        "publicado": "2005",
        "isbn13": "9780446695190",
        "autoridad": "Business Plus",
        "estado": "verificada",
    },
    "rackham": {
        "tipo": "book",
        "autores": ["Rackham, Neil"],
        "publicado": "1988",
        "isbn13": "9780070511132",
        "autoridad": "McGraw-Hill",
        "estado": "verificada",
    },
    "roberge": {
        "tipo": "book",
        "autores": ["Roberge, Mark"],
        "publicado": "2015",
        "isbn13": "9781119047018",
        "autoridad": "John Wiley & Sons",
        "estado": "verificada",
    },
    "ross": {
        "tipo": "book",
        "autores": ["Ross, Aaron", "Tyler, Marylou"],
        "publicado": "2011",
        "isbn13": "9780984380213",
        "autoridad": "Pebble Storm Inc.",
        "estado": "verificada",
    },
    "vaynerchuk": {
        "tipo": "book",
        "autores": ["Vaynerchuk, Gary"],
        "publicado": "2013",
        "isbn13": "9780062273079",
        "autoridad": "HarperCollins Publishers",
        "estado": "verificada",
    },
    "weinberg-sales": {
        "tipo": "book",
        "autores": ["Weinberg, Mike"],
        "publicado": "2012",
        "isbn13": "9780814431788",
        "autoridad": "AMACOM",
        "estado": "verificada",
    },

    # --- Marketing -----------------------------------------------------------
    "binet-field": {
        "tipo": "book",
        "autores": ["Binet, Les", "Field, Peter"],
        "publicado": "2013",
        "isbn13": "9780852941348",
        "autoridad": "Institute of Practitioners in Advertising",
        "estado": "verificada",
    },
    "godin": {
        "tipo": "book",
        "autores": ["Godin, Seth"],
        "publicado": "2018",
        "isbn13": "9780525540830",
        "autoridad": "Portfolio/Penguin",
        "estado": "verificada",
    },
    "kotler": {
        "tipo": "book",
        "autores": ["Kotler, Philip", "Keller, Kevin Lane", "Chernev, Alexander"],
        "publicado": "2021",
        "isbn13": "9780136708643",
        "autoridad": "Pearson Education",
        "estado": "verificada",
    },
    "levitt": {
        "tipo": "reference",
        "autores": ["Levitt, Theodore"],
        "publicado": "1960",
        "url": "https://hbr.org/2004/07/marketing-myopia",
        "autoridad": "Harvard Business Review",
        "consultado": "2026-08-19",
        "nota": "Artículo de 1960; HBR lo republica en esta dirección permanente.",
        "estado": "verificada",
    },
    "ries-trout": {
        "tipo": "book",
        "autores": ["Ries, Al", "Trout, Jack"],
        "publicado": "2001",
        "isbn13": "9780071359160",
        "autoridad": "McGraw-Hill",
        "estado": "verificada",
    },
    "sharp": {
        "tipo": "book",
        "autores": ["Sharp, Byron"],
        "publicado": "2010",
        "isbn13": "9780195573565",
        "autoridad": "Oxford University Press",
        "estado": "verificada",
    },
    "sharp2": {
        "tipo": "book",
        "autores": ["Romaniuk, Jenni", "Sharp, Byron"],
        "publicado": "2015",
        "isbn13": "9780195596267",
        "autoridad": "Oxford University Press",
        "estado": "verificada",
    },

    # --- Investigación de mercados -------------------------------------------
    "blank": {
        "tipo": "book",
        "autores": ["Blank, Steve", "Dorf, Bob"],
        "publicado": "2012",
        "isbn13": "9780984999385",
        "autoridad": "K&S Ranch Publishing",
        "estado": "verificada",
    },
    "fitzpatrick": {
        "tipo": "book",
        "autores": ["Fitzpatrick, Rob"],
        "publicado": "2013",
        "isbn13": "9781492180746",
        "autoridad": "CreateSpace",
        "estado": "verificada",
    },
    "malhotra": {
        "tipo": "book",
        "autores": ["Malhotra, Naresh K."],
        "publicado": "2019",
        "isbn13": "9781292265636",
        "autoridad": "Pearson",
        "estado": "verificada",
    },
    "portigal": {
        "tipo": "book",
        "autores": ["Portigal, Steve"],
        "publicado": "2023",
        "isbn13": "9781959029823",
        "autoridad": "Rosenfeld Media, LLC",
        "estado": "verificada",
    },

    # --- Crecimiento y experimentación ---------------------------------------
    "bush-plg": {
        "tipo": "book",
        "autores": ["Bush, Wes"],
        "publicado": "2019",
        "isbn13": "9781777119317",
        "autoridad": "Product-Led Institute",
        "estado": "verificada",
    },
    "ellis-brown": {
        "tipo": "book",
        "autores": ["Ellis, Sean", "Brown, Morgan"],
        "publicado": "2017",
        "isbn13": "9780451497215",
        "autoridad": "Crown Business",
        "estado": "verificada",
    },
    "ries-lean": {
        "tipo": "book",
        "autores": ["Ries, Eric"],
        "publicado": "2011",
        "isbn13": "9780670921607",
        "autoridad": "Portfolio Penguin",
        "estado": "verificada",
    },
    "weinberg-traction": {
        "tipo": "book",
        "autores": ["Weinberg, Gabriel", "Mares, Justin"],
        "publicado": "2015",
        "isbn13": "9780241242551",
        "autoridad": "Penguin Books",
        "estado": "verificada",
    },

    # --- Gestión de producto -------------------------------------------------
    "cagan": {
        "tipo": "book",
        "autores": ["Cagan, Marty"],
        "publicado": "2017",
        "isbn13": "9781119387541",
        "autoridad": "John Wiley & Sons",
        "estado": "verificada",
    },
    "hulick": {
        "tipo": "book",
        "autores": ["Hulick, Samuel"],
        "publicado": "2014",
        "autoridad": "Samuel Hulick (publicación independiente)",
        "nota": "No aparece en OpenLibrary con ISBN-13 y su venta independiente en "
                  "useronboard.com no expone una dirección estable que identifique la "
                  "obra. Queda declarada sin localizador hasta comprobarla a mano.",
        "estado": "pendiente",
    },

    # --- Marketing digital y conversión --------------------------------------
    "chaffey": {
        "tipo": "book",
        "autores": ["Chaffey, Dave", "Ellis-Chadwick, Fiona"],
        "publicado": "2022",
        "isbn13": "9781292400990",
        "autoridad": "Pearson",
        "estado": "verificada",
    },
    "eisenberg": {
        "tipo": "book",
        "autores": ["Eisenberg, Bryan", "Eisenberg, Jeffrey"],
        "publicado": "2005",
        "isbn13": "9781932226393",
        "autoridad": "Wizard Academy Press",
        "estado": "verificada",
    },
    "enge-seo": {
        "tipo": "book",
        "autores": ["Enge, Eric", "Spencer, Stephan", "Stricchiola, Jessie"],
        "publicado": "2023",
        "isbn13": "9781098102616",
        "autoridad": "O'Reilly Media",
        "estado": "verificada",
    },
    "krug": {
        "tipo": "book",
        "autores": ["Krug, Steve"],
        "publicado": "2014",
        "isbn13": "9780321965516",
        "autoridad": "Pearson",
        "estado": "verificada",
    },
    "laja": {
        "tipo": "reference",
        "autores": ["Laja, Peep"],
        "publicado": "2024",
        "url": "https://cxl.com/institute/",
        "autoridad": "CXL Institute",
        "consultado": "2026-08-19",
        "nota": "Corpus vivo de la plataforma, sin edición fija: el localizador apunta "
                  "al editor, no a una edición concreta.",
        "estado": "verificada",
    },

    # --- Cliente y trabajo por resolver --------------------------------------
    "christensen": {
        "tipo": "book",
        "autores": ["Christensen, Clayton M.", "Hall, Taddy", "Dillon, Karen", "Duncan, David S."],
        "publicado": "2016",
        "isbn13": "9780062435613",
        "autoridad": "HarperBusiness",
        "estado": "verificada",
    },
    "ulwick": {
        "tipo": "book",
        "autores": ["Ulwick, Anthony W."],
        "publicado": "2016",
        "isbn13": "9780990576747",
        "autoridad": "IDEA BITE PRESS",
        "estado": "verificada",
    },

    # --- Dirección y organización --------------------------------------------
    "collins": {
        "tipo": "book",
        "autores": ["Collins, Jim"],
        "publicado": "2001",
        "isbn13": "9780066620992",
        "autoridad": "HarperBusiness",
        "estado": "verificada",
    },
    "doerr": {
        "tipo": "book",
        "autores": ["Doerr, John"],
        "publicado": "2018",
        "isbn13": "9780525536222",
        "autoridad": "Portfolio",
        "estado": "verificada",
    },
    "grove": {
        "tipo": "book",
        "autores": ["Grove, Andrew S."],
        "publicado": "1983",
        "isbn13": "9780394532349",
        "autoridad": "Random House",
        "estado": "verificada",
    },
    "kaplan-norton": {
        "tipo": "book",
        "autores": ["Kaplan, Robert S.", "Norton, David P."],
        "publicado": "1996",
        "isbn13": "9780875846514",
        "autoridad": "Harvard Business School Press",
        "estado": "verificada",
    },
    "lencioni": {
        "tipo": "book",
        "autores": ["Lencioni, Patrick"],
        "publicado": "2002",
        "isbn13": "9780787960759",
        "autoridad": "Jossey-Bass",
        "estado": "verificada",
    },
    "sinek": {
        "tipo": "book",
        "autores": ["Sinek, Simon"],
        "publicado": "2009",
        "isbn13": "9781591844518",
        "autoridad": "Penguin Publishing Group",
        "estado": "verificada",
    },
    "zoltners": {
        "tipo": "book",
        "autores": ["Zoltners, Andris A.", "Sinha, Prabhakant", "Lorimer, Sally E."],
        "publicado": "2006",
        "isbn13": "9780814473245",
        "autoridad": "AMACOM",
        "estado": "verificada",
    },

    # --- Analítica y medición ------------------------------------------------
    "croll-yoskovitz": {
        "tipo": "book",
        "autores": ["Croll, Alistair", "Yoskovitz, Benjamin"],
        "publicado": "2013",
        "isbn13": "9781449335670",
        "autoridad": "O'Reilly Media",
        "estado": "verificada",
    },
    "hubbard": {
        "tipo": "book",
        "autores": ["Hubbard, Douglas W."],
        "publicado": "2014",
        "isbn13": "9781118836446",
        "autoridad": "John Wiley & Sons",
        "estado": "verificada",
    },
    "kaushik": {
        "tipo": "book",
        "autores": ["Kaushik, Avinash"],
        "publicado": "2009",
        "isbn13": "9780470596425",
        "autoridad": "John Wiley & Sons, Ltd.",
        "estado": "verificada",
    },
    "kohavi": {
        "tipo": "book",
        "autores": ["Kohavi, Ron", "Tang, Diane", "Xu, Ya"],
        "publicado": "2020",
        "isbn13": "9781108601375",
        "autoridad": "Cambridge University Press",
        "estado": "verificada",
    },
    "provost": {
        "tipo": "book",
        "autores": ["Provost, Foster", "Fawcett, Tom"],
        "publicado": "2013",
        "isbn13": "9781449374280",
        "autoridad": "O'Reilly Media",
        "estado": "verificada",
    },
    "wheeler-dv": {
        "tipo": "book",
        "autores": ["Wheeler, Donald J."],
        "publicado": "2000",
        "isbn13": "9780945320531",
        "autoridad": "SPC Press, Inc.",
        "estado": "verificada",
    },

    # --- Operaciones de ingresos ---------------------------------------------
    "diorio": {
        "tipo": "book",
        "autores": ["Diorio, Stephen G.", "Hummel, Chris K."],
        "publicado": "2022",
        "isbn13": "9781119871132",
        "autoridad": "John Wiley & Sons",
        "estado": "verificada",
    },

    # --- Retención y éxito de cliente ----------------------------------------
    "dixon-effort": {
        "tipo": "book",
        "autores": ["Dixon, Matthew", "Toman, Nick", "DeLisi, Rick"],
        "publicado": "2013",
        "isbn13": "9780241003305",
        "autoridad": "Penguin Books",
        "estado": "verificada",
    },
    "fader": {
        "tipo": "book",
        "autores": ["Fader, Peter"],
        "publicado": "2020",
        "isbn13": "9781613631447",
        "autoridad": "Wharton School Press",
        "estado": "verificada",
    },
    "fader-ltv": {
        "tipo": "book",
        "autores": ["Fader, Peter", "Toms, Sarah"],
        "publicado": "2018",
        "isbn13": "9781613630914",
        "autoridad": "Wharton School Press",
        "estado": "verificada",
    },
    "mehta": {
        "tipo": "book",
        "autores": ["Mehta, Nick", "Steinman, Dan", "Murphy, Lincoln"],
        "publicado": "2016",
        "isbn13": "9781119168294",
        "autoridad": "John Wiley & Sons",
        "estado": "verificada",
    },
    "reichheld": {
        "tipo": "book",
        "autores": ["Reichheld, Fred", "Darnell, Darci", "Burns, Maureen"],
        "publicado": "2021",
        "isbn13": "9781647821784",
        "autoridad": "Harvard Business Review Press",
        "estado": "verificada",
    },

    # --- Estrategia y competencia --------------------------------------------
    "drucker": {
        "tipo": "book",
        "autores": ["Drucker, Peter F."],
        "publicado": "1954",
        "isbn13": "9780060110956",
        "autoridad": "HarperCollins Publishers",
        "estado": "verificada",
    },
    "kim-mauborgne": {
        "tipo": "book",
        "autores": ["Kim, W. Chan", "Mauborgne, Renée"],
        "publicado": "2015",
        "isbn13": "9781625274496",
        "autoridad": "Harvard Business Review Press",
        "estado": "verificada",
    },
    "moore": {
        "tipo": "book",
        "autores": ["Moore, Geoffrey A."],
        "publicado": "2014",
        "isbn13": "9780062293008",
        "autoridad": "HarperCollins Publishers",
        "estado": "verificada",
    },
    "osterwalder-bmg": {
        "tipo": "book",
        "autores": ["Osterwalder, Alexander", "Pigneur, Yves"],
        "publicado": "2010",
        "isbn13": "9780470876411",
        "autoridad": "John Wiley and Sons Ltd",
        "estado": "verificada",
    },
    "porter": {
        "tipo": "book",
        "autores": ["Porter, Michael E."],
        "publicado": "1980",
        "isbn13": "9780029253601",
        "autoridad": "Free Press",
        "estado": "verificada",
    },
    "porter-hbr": {
        "tipo": "reference",
        "autores": ["Porter, Michael E."],
        "publicado": "1996",
        "url": "https://hbr.org/1996/11/what-is-strategy",
        "autoridad": "Harvard Business Review",
        "consultado": "2026-08-19",
        "estado": "verificada",
    },
    "rumelt": {
        "tipo": "book",
        "autores": ["Rumelt, Richard"],
        "publicado": "2011",
        "isbn13": "9781846684807",
        "autoridad": "Profile Books",
        "estado": "verificada",
    },

    # --- Negociación ---------------------------------------------------------
    "fisher-ury": {
        "tipo": "book",
        "autores": ["Fisher, Roger", "Ury, William", "Patton, Bruce"],
        "publicado": "2011",
        "isbn13": "9781101539545",
        "autoridad": "Penguin Books",
        "estado": "verificada",
    },
    "malhotra-neg": {
        "tipo": "book",
        "autores": ["Malhotra, Deepak", "Bazerman, Max H."],
        "publicado": "2007",
        "isbn13": "9780553804881",
        "autoridad": "Bantam",
        "estado": "verificada",
    },
    "shell": {
        "tipo": "book",
        "autores": ["Shell, G. Richard"],
        "publicado": "2006",
        "isbn13": "9780143036975",
        "autoridad": "Penguin Books",
        "estado": "verificada",
    },
    "ury": {
        "tipo": "book",
        "autores": ["Ury, William"],
        "publicado": "2007",
        "isbn13": "9780553903645",
        "autoridad": "Random House Publishing Group",
        "estado": "verificada",
    },
    "voss": {
        "tipo": "book",
        "autores": ["Voss, Chris", "Raz, Tahl"],
        "publicado": "2016",
        "isbn13": "9781473535169",
        "autoridad": "Penguin Random House",
        "estado": "verificada",
    },

    # --- Comercio digital ----------------------------------------------------
    "flint": {
        "tipo": "book",
        "autores": ["Hillstrom, Kevin"],
        "publicado": "2007",
        "isbn13": "9780977148950",
        "autoridad": "Campbell & lewis Publishers",
        "estado": "verificada",
    },

    # --- Publicidad ----------------------------------------------------------
    "geddes": {
        "tipo": "book",
        "autores": ["Geddes, Brad"],
        "publicado": "2014",
        "isbn13": "9781118819647",
        "autoridad": "John Wiley & Sons",
        "estado": "verificada",
    },
    "ogilvy": {
        "tipo": "book",
        "autores": ["Ogilvy, David"],
        "publicado": "1983",
        "isbn13": "9780517550755",
        "autoridad": "Crown",
        "estado": "verificada",
    },

    # --- Contenido y copywriting ---------------------------------------------
    "handley": {
        "tipo": "book",
        "autores": ["Handley, Ann"],
        "publicado": "2022",
        "isbn13": "9781119854319",
        "autoridad": "John Wiley & Sons",
        "estado": "verificada",
    },
    "pulizzi": {
        "tipo": "book",
        "autores": ["Pulizzi, Joe"],
        "publicado": "2021",
        "isbn13": "9781264257546",
        "autoridad": "McGraw-Hill Education",
        "estado": "verificada",
    },
    "sugarman": {
        "tipo": "book",
        "autores": ["Sugarman, Joseph"],
        "publicado": "2007",
        "isbn13": "9780470051245",
        "autoridad": "John Wiley & Sons",
        "estado": "verificada",
    },

    # --- Comunicación e identidad --------------------------------------------
    "heath": {
        "tipo": "book",
        "autores": ["Heath, Chip", "Heath, Dan"],
        "publicado": "2007",
        "isbn13": "9781400064281",
        "autoridad": "Random House",
        "estado": "verificada",
    },

    # --- Ética y consecuencias -----------------------------------------------
    "iso-31000": {
        "tipo": "standard",
        "autores": ["International Organization for Standardization"],
        "publicado": "2018",
        "url": "https://www.iso.org/standard/65694.html",
        "autoridad": "International Organization for Standardization (ISO)",
        "nota": "iso.org responde 403 a cualquier cliente automatizado, y responde 403 "
                  "también a rutas inexistentes: desde fuera no hay forma de distinguir "
                  "la ficha correcta de una equivocada. La dirección queda propuesta, no "
                  "confirmada, hasta que alguien la abra en un navegador y compruebe que "
                  "corresponde a ISO 31000:2018.",
        "estado": "pendiente",
    },
    "oneil": {
        "tipo": "book",
        "autores": ["O'Neil, Cathy"],
        "publicado": "2016",
        "isbn13": "9780141985428",
        "autoridad": "Penguin Books",
        "estado": "verificada",
    },

    # --- Precio y monetización -----------------------------------------------
    "nagle": {
        "tipo": "book",
        "autores": ["Nagle, Thomas T.", "Müller, Georg"],
        "publicado": "2018",
        "isbn13": "9781138737501",
        "autoridad": "Taylor & Francis Group",
        "estado": "verificada",
    },
    "ramanujam": {
        "tipo": "book",
        "autores": ["Ramanujam, Madhavan", "Tacke, Georg"],
        "publicado": "2016",
        "isbn13": "9781119240877",
        "autoridad": "John Wiley & Sons",
        "estado": "verificada",
    },
    "simon": {
        "tipo": "book",
        "autores": ["Simon, Hermann"],
        "publicado": "2015",
        "isbn13": "9783319204000",
        "autoridad": "Springer",
        "estado": "verificada",
    },
    "smith-pricing": {
        "tipo": "book",
        "autores": ["Smith, Tim J."],
        "publicado": "2011",
        "isbn13": "9781111571290",
        "autoridad": "SWCP",
        "estado": "verificada",
    },

    # --- Inteligencia artificial y riesgo ------------------------------------
    "ng-mlyearning": {
        "tipo": "reference",
        "autores": ["Ng, Andrew"],
        "publicado": "2018",
        "url": "https://info.deeplearning.ai/machine-learning-yearning-book",
        "autoridad": "DeepLearning.AI",
        "consultado": "2026-08-19",
        "nota": "Obra de distribución gratuita por el propio autor; no tiene ISBN.",
        "estado": "verificada",
    },
    "nist-airmf": {
        "tipo": "standard",
        "autores": ["National Institute of Standards and Technology"],
        "publicado": "2023",
        "doi": "10.6028/NIST.AI.100-1",
        "url": "https://doi.org/10.6028/NIST.AI.100-1",
        "autoridad": "National Institute of Standards and Technology (NIST), Estados Unidos",
        "consultado": "2026-08-19",
        "estado": "verificada",
    },
    "russell-norvig": {
        "tipo": "book",
        "autores": ["Russell, Stuart J.", "Norvig, Peter"],
        "publicado": "2021",
        "isbn13": "9780136958420",
        "autoridad": "Pearson",
        "estado": "verificada",
    },

    # --- Oferta y producto ---------------------------------------------------
    "osterwalder-vpd": {
        "tipo": "book",
        "autores": ["Osterwalder, Alexander", "Pigneur, Yves", "Bernarda, Greg", "Smith, Alan"],
        "publicado": "2014",
        "isbn13": "9781118968055",
        "autoridad": "John Wiley & Sons",
        "estado": "verificada",
    },

}


def localizador(clave):
    """Dirección donde se resuelve la obra, o None si sigue pendiente.

    Es la misma función para todos los generadores: el registro JSON, la
    bibliografía del README, la de cada parte y la de cada clase. Si la forma
    canónica cambiara, cambia en un solo sitio.
    """
    datos = LOCALIZADORES[clave]
    if datos.get("estado", "verificada") != "verificada":
        return None
    if datos["tipo"] == "book" and datos.get("isbn13"):
        return "https://openlibrary.org/isbn/{}".format(datos["isbn13"])
    if datos["tipo"] == "paper" and datos.get("doi"):
        return "https://doi.org/{}".format(datos["doi"])
    return datos.get("url") or None


def etiqueta(clave):
    """Qué se enseña como localizador: el ISBN, el DOI o «fuente primaria»."""
    datos = LOCALIZADORES[clave]
    if datos.get("isbn13"):
        return "ISBN {}".format(datos["isbn13"])
    if datos.get("doi"):
        return "DOI {}".format(datos["doi"])
    return "fuente primaria"


def enlace(clave, texto):
    """`texto` enlazado a su localizador; sin enlace si la obra está pendiente.

    Una obra pendiente no se disfraza de obra localizada: se muestra tal cual,
    y quien lea sabe que ahí falta algo.
    """
    url = localizador(clave)
    return "[{}]({})".format(texto, url) if url else texto
