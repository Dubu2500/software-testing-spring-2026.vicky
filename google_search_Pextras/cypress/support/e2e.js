// Archivo de soporte de Cypress - se ejecuta antes de cada spec

// Ignora errores de JavaScript de los sitios de terceros
// (por ejemplo errores de plugins de jQuery en UDG)
Cypress.on("uncaught:exception", () => false);
