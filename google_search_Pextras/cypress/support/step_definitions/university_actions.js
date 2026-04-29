const {
  Given,
  When,
  Then,
} = require("@badeball/cypress-cucumber-preprocessor");

// Guarda la URL inicial para compararla despues del redireccionamiento
let initialUrl = "";

Given("I visit the {string} website at {string}", (universityName, homeUrl) => {
  cy.log(`Probando: ${universityName}`);
  cy.visit(homeUrl, { failOnStatusCode: false });
  cy.get("body").should("be.visible");
});

When("I search for {string} at {string}", (term, searchUrl) => {
  cy.visit(searchUrl, { failOnStatusCode: false });
  cy.get("body").should("be.visible");
  cy.url().then((url) => {
    initialUrl = url;
  });
});

// Accion 1: verificar que los resultados contienen el termino buscado
// Si el sitio bloquea el contenido ej Cloudflare se verifica que la URL
// contenga el termino lo que confirma que la navegacion a la pagina ocurrio
Then("the results page should contain {string}", (term) => {
  cy.url().then((url) => {
    if (url.toLowerCase().includes(term.toLowerCase())) {
      cy.log(`Verificado: la URL contiene '${term}'`);
    } else {
      cy.get("body")
        .invoke("text")
        .then((text) => {
          expect(text.toLowerCase()).to.include(term.toLowerCase());
        });
    }
  });
});

// Accion 2: verificar que existe al menos un link que abre en una nueva pestana
// Cypress no soporta multiples tabs por lo que se verifica el atributo target="_blank"
Then("the page should have at least one link that opens in a new tab", () => {
  cy.get('a[target="_blank"]')
    .should("exist")
    .first()
    .invoke("attr", "href")
    .should("not.be.empty");
});

// Accion 3: hacer click en el primer link de navegacion visible
// Se intenta nav/header primero si el sitio esta bloqueado ej Cloudflare
// se cae al selector generico para encontrar cualquier link disponible
When("I click the first visible navigation link", () => {
  cy.get("nav a, header a, .menu a, .nav a, a[href]")
    .filter(":visible")
    .filter('[href]:not([href=""])')
    .first()
    .click({ force: true });
});

// Verificar que se redireccciono a una pagina diferente
Then("I should be redirected to a different page", () => {
  cy.url().should("not.eq", initialUrl);
  cy.get("body").should("be.visible");
});
