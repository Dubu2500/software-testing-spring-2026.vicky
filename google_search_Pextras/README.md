# Actividad Extra - Pruebas de Sistema con BDD

Pruebas de sistema para sitios universitarios usando BDD. Contiene dos implementaciones: Cypress (JavaScript) y Playwright (JavaScript).

---

## Cypress

Pruebas BDD con Cypress y Cucumber para 3 universidades (IPN, UDG, ITESO).
Verifica busqueda de becas, links que abren en nueva pestana y redireccionamiento de navegacion.

### Requisitos

- Node.js 18+

### Instalacion

```bash
cd google_search_Pextras/cypress
npm install
```

### Ejecucion

```bash
# Modo headless (sin navegador visible)
npm test

# Modo headed (con navegador visible)
npx cypress run --headed
```

### Universidades probadas

| Universidad | URL de busqueda               |
| ----------- | ----------------------------- |
| IPN         | https://www.ipn.mx/becas/     |
| UDG         | https://www.udg.mx/?s=becas   |
| ITESO       | https://www.iteso.mx/?s=becas |

---

## Playwright

Pruebas BDD con Playwright y Cucumber para sitios universitarios.

### Requisitos

- Node.js 18+

### Instalacion

```bash
cd google_search_Pextras/playwright
npm install
npx playwright install
```

### Ejecucion

```bash
# Modo headless (sin navegador visible)
npm test

# Modo headed (con navegador visible)
npm run test:headed
```
