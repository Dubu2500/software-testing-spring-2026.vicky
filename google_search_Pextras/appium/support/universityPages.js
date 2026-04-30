/**
 * URLs canónicas por universidad y sección (sin mailto ni redirects de Google).
 * Ajusta aquí si cambian rutas institucionales.
 */
const OFFICIAL_PAGES = {
  ITESO: {
    carreras: {
      url: 'https://carreras.iteso.mx/',
      urlContains: 'carreras.iteso.mx',
    },
    posgrados: {
      url: 'https://posgrados.iteso.mx/',
      urlContains: 'posgrados.iteso.mx',
    },
    admisiones: {
      url: 'https://carreras.iteso.mx/',
      urlContains: 'carreras.iteso.mx',
    },
    home: {
      url: 'https://www.iteso.mx/',
      urlContains: 'iteso.mx',
    },
  },
  UNE: {
    home: {
      url: 'https://www.universidad-une.com/',
      urlContains: 'universidad-une.com',
    },
    planteles: {
      url: 'https://www.universidad-une.com/planteles/',
      urlContains: 'universidad-une.com',
    },
    admisiones: {
      url: 'https://www.universidad-une.com/acerca/admisiones/',
      urlContains: 'universidad-une.com',
    },
    carreras: {
      url: 'https://www.universidad-une.com/',
      urlContains: 'universidad-une.com',
    },
    posgrados: {
      url: 'https://www.universidad-une.com/',
      urlContains: 'universidad-une.com',
    },
  },
  'CUCEI UDG': {
    home: {
      url: 'https://www.cucei.udg.mx/',
      urlContains: 'cucei.udg.mx',
    },
    licenciaturas: {
      url: 'https://www.cucei.udg.mx/es/oferta-academica/licenciaturas',
      urlContains: 'cucei.udg.mx',
    },
    posgrados: {
      url: 'https://www.cucei.udg.mx/es/oferta-academica/posgrados',
      urlContains: 'cucei.udg.mx',
    },
    carreras: {
      url: 'https://www.cucei.udg.mx/es/oferta-academica/licenciaturas',
      urlContains: 'cucei.udg.mx',
    },
  },
};

/** Selectores extra por host: primero id / aria / name, evitando depender de href. */
const HOST_SEARCH_SELECTORS = {
  'carreras.iteso.mx': [
    '#edit-keys',
    'input#edit-keys',
    'input[id*="edit-keys"]',
    'input[id*="search"]',
    '#search-block-form input[type="text"]',
  ],
  'posgrados.iteso.mx': [
    '#edit-keys',
    'input#edit-keys',
    'input[id*="edit-keys"]',
    'input[id*="search"]',
  ],
  'universidad-une.com': [
    '#search',
    'input#search',
    'input[name="s"]',
    'input[type="search"]',
  ],
  'cucei.udg.mx': [
    'input[name="search_block_form"]',
    '#edit-keys',
    'input[id*="edit-keys"]',
    '.form-search input',
    'header input[type="search"]',
    'input[type="search"]',
  ],
};

function normalizeKey(name) {
  return String(name || '').trim();
}

function getOfficialPage(university, section) {
  const uni = OFFICIAL_PAGES[normalizeKey(university)];
  if (!uni) {
    throw new Error(`Universidad no configurada: "${university}"`);
  }
  const sec = normalizeKey(section).toLowerCase();
  const page = uni[sec];
  if (!page) {
    const keys = Object.keys(uni).join(', ');
    throw new Error(`Sección "${section}" no definida para ${university}. Usa una de: ${keys}`);
  }
  return page;
}

function hostFromUrl(url) {
  try {
    return new URL(url).hostname.replace(/^www\./, '');
  } catch {
    return '';
  }
}

function selectorsForCurrentUrl(currentUrl) {
  const host = hostFromUrl(currentUrl);
  const extra = [];
  for (const [h, list] of Object.entries(HOST_SEARCH_SELECTORS)) {
    if (host === h || host.endsWith(`.${h}`) || host.includes(h)) {
      extra.push(...list);
    }
  }
  return extra;
}

module.exports = {
  getOfficialPage,
  selectorsForCurrentUrl,
};
