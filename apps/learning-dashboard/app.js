/**
 * Panel de progreso del programa.
 *
 * Sin dependencias y sin red: el avance vive en localStorage de este navegador.
 * Los títulos de las partes se leen de curriculum/curriculum.json cuando el
 * panel se sirve desde el repositorio; si no está disponible, se usan los
 * nombres incorporados para que el panel siga funcionando.
 */
(function () {
  'use strict';

  var CLAVE = 'msg-programa-avance-v2';
  var CLAVE_TEMA = 'msg-programa-tema';
  var CLASES_POR_PARTE = 14;
  var LABS_POR_PARTE = 2;
  var HORAS_CLASE = 2.5;
  var HORAS_LAB = 4;
  var HORAS_EVAL = 2;

  var PARTES = [
    'Marketing y ventas: fundamentos del sistema comercial',
    'Cliente y comportamiento del consumidor',
    'Investigación de mercados e inteligencia competitiva',
    'Segmentación, targeting y posicionamiento',
    'Producto, oferta y propuesta de valor',
    'Marca, branding y comunicación estratégica',
    'Pricing y monetización',
    'Fundamentos profesionales de ventas',
    'Venta consultiva y B2B compleja',
    'Negociación comercial',
    'Prospección y generación de demanda',
    'Marketing digital y adquisición',
    'Contenido, copywriting y comunicación persuasiva',
    'Publicidad y performance marketing',
    'E-commerce y marketplaces',
    'CRM, pipeline y sales operations',
    'Marketing automation y revenue operations',
    'Customer experience, success y fidelización',
    'Growth marketing y growth engineering',
    'Analítica comercial y marketing science',
    'IA aplicada a marketing, ventas y servicio',
    'Go-to-market, canales y expansión',
    'Dirección comercial: CMO, VP Sales y CRO',
    'Empresa real, regulación y Capstone'
  ];

  var estado = cargar();

  function cargar() {
    try {
      var crudo = JSON.parse(localStorage.getItem(CLAVE) || '{}');
      var limpio = {};
      for (var p = 1; p <= 24; p++) {
        var d = crudo[p] || {};
        limpio[p] = {
          clases: acotar(d.clases, 0, CLASES_POR_PARTE),
          labs: acotar(d.labs, 0, LABS_POR_PARTE),
          eval: d.eval === true
        };
      }
      return limpio;
    } catch (e) {
      return inicial();
    }
  }

  function inicial() {
    var vacio = {};
    for (var p = 1; p <= 24; p++) { vacio[p] = { clases: 0, labs: 0, eval: false }; }
    return vacio;
  }

  function acotar(valor, min, max) {
    var n = parseInt(valor, 10);
    if (isNaN(n)) { return min; }
    return Math.max(min, Math.min(max, n));
  }

  function guardar() {
    try { localStorage.setItem(CLAVE, JSON.stringify(estado)); } catch (e) { avisar('No se pudo guardar el avance en este navegador.'); }
  }

  function parteCompleta(d) {
    return d.clases === CLASES_POR_PARTE && d.labs === LABS_POR_PARTE && d.eval;
  }

  function dosDigitos(n) { return (n < 10 ? '0' : '') + n; }

  function render() {
    var grilla = document.getElementById('grilla');
    grilla.innerHTML = '';
    var totalClases = 0, totalLabs = 0, totalEvals = 0, completas = 0;

    for (var p = 1; p <= 24; p++) {
      var d = estado[p];
      totalClases += d.clases;
      totalLabs += d.labs;
      totalEvals += d.eval ? 1 : 0;
      if (parteCompleta(d)) { completas++; }

      var avance = (d.clases / CLASES_POR_PARTE) * 0.6 +
                   (d.labs / LABS_POR_PARTE) * 0.3 +
                   (d.eval ? 1 : 0) * 0.1;

      var tarjeta = document.createElement('article');
      tarjeta.className = 'tarjeta' + (parteCompleta(d) ? ' completa' : '');
      tarjeta.innerHTML =
        '<header class="cabecera-tarjeta">' +
          '<span class="numero">' + dosDigitos(p) + '</span>' +
          '<h3>' + PARTES[p - 1] + '</h3>' +
        '</header>' +
        '<div class="barra"><div class="relleno" style="width:' + (avance * 100).toFixed(1) + '%"></div></div>' +
        '<dl class="detalle">' +
          '<div><dt>Clases</dt><dd>' + d.clases + '/' + CLASES_POR_PARTE + '</dd></div>' +
          '<div><dt>Laboratorios</dt><dd>' + d.labs + '/' + LABS_POR_PARTE + '</dd></div>' +
          '<div><dt>Evaluación</dt><dd>' + (d.eval ? 'aprobada' : 'pendiente') + '</dd></div>' +
        '</dl>' +
        '<div class="controles">' +
          '<div class="grupo" role="group" aria-label="Clases de la parte ' + p + '">' +
            '<button type="button" data-p="' + p + '" data-campo="clases" data-delta="-1" aria-label="Restar una clase a la parte ' + p + '">−</button>' +
            '<span>clases</span>' +
            '<button type="button" data-p="' + p + '" data-campo="clases" data-delta="1" aria-label="Sumar una clase a la parte ' + p + '">+</button>' +
          '</div>' +
          '<div class="grupo" role="group" aria-label="Laboratorios de la parte ' + p + '">' +
            '<button type="button" data-p="' + p + '" data-campo="labs" data-delta="-1" aria-label="Restar un laboratorio a la parte ' + p + '">−</button>' +
            '<span>labs</span>' +
            '<button type="button" data-p="' + p + '" data-campo="labs" data-delta="1" aria-label="Sumar un laboratorio a la parte ' + p + '">+</button>' +
          '</div>' +
          '<label class="check"><input type="checkbox" data-p="' + p + '" data-campo="eval"' + (d.eval ? ' checked' : '') + '> Evaluación aprobada</label>' +
        '</div>';
      grilla.appendChild(tarjeta);
    }

    var horas = totalClases * HORAS_CLASE + totalLabs * HORAS_LAB + totalEvals * HORAS_EVAL;
    var pct = (totalClases / 336) * 0.6 + (totalLabs / 48) * 0.3 + (totalEvals / 24) * 0.1;

    texto('c-clases', totalClases);
    texto('c-labs', totalLabs);
    texto('c-evals', totalEvals);
    texto('c-partes', completas);
    texto('c-horas', Math.round(horas));
    texto('pct-total', (pct * 100).toFixed(1).replace('.', ',') + ' %');
    document.getElementById('barra-total').style.width = (pct * 100).toFixed(1) + '%';
  }

  function texto(id, valor) {
    var el = document.getElementById(id);
    if (el) { el.textContent = valor; }
  }

  function avisar(mensaje) {
    var el = document.getElementById('mensaje');
    el.textContent = mensaje;
    setTimeout(function () { if (el.textContent === mensaje) { el.textContent = ''; } }, 6000);
  }

  document.getElementById('grilla').addEventListener('click', function (e) {
    var b = e.target.closest('button[data-campo]');
    if (!b) { return; }
    var p = b.dataset.p;
    var campo = b.dataset.campo;
    var max = campo === 'clases' ? CLASES_POR_PARTE : LABS_POR_PARTE;
    estado[p][campo] = acotar(estado[p][campo] + parseInt(b.dataset.delta, 10), 0, max);
    guardar();
    render();
  });

  document.getElementById('grilla').addEventListener('change', function (e) {
    if (e.target.dataset.campo !== 'eval') { return; }
    estado[e.target.dataset.p].eval = e.target.checked;
    guardar();
    render();
  });

  document.getElementById('exportar').addEventListener('click', function () {
    var datos = { version: 2, exportado: new Date().toISOString().slice(0, 10), avance: estado };
    var blob = new Blob([JSON.stringify(datos, null, 2)], { type: 'application/json' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'avance-programa.json';
    a.click();
    URL.revokeObjectURL(url);
    avisar('Avance exportado.');
  });

  document.getElementById('importar').addEventListener('change', function (e) {
    var archivo = e.target.files[0];
    if (!archivo) { return; }
    var lector = new FileReader();
    lector.onload = function () {
      try {
        var datos = JSON.parse(lector.result);
        var avance = datos.avance || datos;
        for (var p = 1; p <= 24; p++) {
          var d = avance[p] || {};
          estado[p] = {
            clases: acotar(d.clases, 0, CLASES_POR_PARTE),
            labs: acotar(d.labs, 0, LABS_POR_PARTE),
            eval: d.eval === true
          };
        }
        guardar();
        render();
        avisar('Avance importado correctamente.');
      } catch (err) {
        avisar('El archivo no tiene el formato esperado.');
      }
    };
    lector.readAsText(archivo);
    e.target.value = '';
  });

  document.getElementById('reiniciar').addEventListener('click', function () {
    if (!confirm('Se borrará todo el avance registrado en este navegador. ¿Continuar?')) { return; }
    estado = inicial();
    guardar();
    render();
    avisar('Avance reiniciado.');
  });

  var botonTema = document.getElementById('cambiar-tema');
  function aplicarTema(t) {
    if (t) { document.documentElement.setAttribute('data-tema', t); }
    else { document.documentElement.removeAttribute('data-tema'); }
    botonTema.textContent = t === 'oscuro' ? 'Modo claro' : (t === 'claro' ? 'Según el sistema' : 'Modo oscuro');
  }
  try { aplicarTema(localStorage.getItem(CLAVE_TEMA)); } catch (e) { /* sin almacenamiento */ }
  botonTema.addEventListener('click', function () {
    var actual = document.documentElement.getAttribute('data-tema');
    var siguiente = actual === 'oscuro' ? 'claro' : (actual === 'claro' ? '' : 'oscuro');
    try { siguiente ? localStorage.setItem(CLAVE_TEMA, siguiente) : localStorage.removeItem(CLAVE_TEMA); } catch (e) { /* sin almacenamiento */ }
    aplicarTema(siguiente);
  });

  // Si el panel se sirve desde el repositorio, usa los títulos reales del currículo.
  if (location.protocol !== 'file:') {
    fetch('../../curriculum/curriculum.json')
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (datos) {
        if (!datos || !datos.partes) { return; }
        datos.partes.forEach(function (p, i) { if (p.titulo) { PARTES[i] = p.titulo; } });
        render();
      })
      .catch(function () { /* el panel funciona igual con los títulos incorporados */ });
  }

  render();
})();
