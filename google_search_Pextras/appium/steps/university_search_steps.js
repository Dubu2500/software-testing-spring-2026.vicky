const { Given, When, Then, Before, After } = require("@cucumber/cucumber");
const { remote } = require("webdriverio");
const assert = require("assert");
const {
  getOfficialPage,
  selectorsForCurrentUrl,
} = require("../support/universityPages");

let driver;
const udid = process.env.ANDROID_UDID || "GQFIR469AMW4D6AM";
const allowManualCaptcha = process.env.ALLOW_MANUAL_CAPTCHA === "true";

function hasCaptcha(html) {
  const lower = html.toLowerCase();
  return lower.includes("acerca de esta pagina") || lower.includes("recaptcha");
}

Before(async function () {
  try {
    console.log("Intentando conectar a Appium...");

    driver = await remote({
      hostname: "localhost",
      port: 4723,
      path: "/",
      logLevel: "info",
      capabilities: {
        platformName: "Android",
        "appium:deviceName": "Android Device",
        "appium:udid": udid,
        "appium:automationName": "UiAutomator2",
        "appium:browserName": "Chrome",
        "appium:chromedriverAutodownload": true,
        "appium:newCommandTimeout": 120,
        "appium:chromeOptions": {
          args: ["--disable-blink-features=AutomationControlled"],
        },
      },
    });

    this.driver = driver;
    console.log("Sesion creada");
  } catch (error) {
    console.error("Error:", error.message);
    throw error;
  }
});

After(async function () {
  if (driver) {
    await driver.deleteSession();
  }
});

// El resto de tus steps quedan igual
Given("I open Google in the browser", async function () {
  await driver.url("https://www.google.com");
  try {
    const acceptBtn = await driver.$(
      'button[id*="accept"], button[aria-label*="Aceptar"]',
    );
    const displayed = await acceptBtn.isDisplayed();
    if (displayed) await acceptBtn.click();
  } catch (_) {}
});

When("I search for {string} on Google", async function (university) {
  const searchBox = await driver.$('textarea[name="q"], input[name="q"]');
  await searchBox.clearValue();
  // Sending Enter from the same input is less likely to trigger anti-bot checks.
  await searchBox.setValue(`${university}\n`);
  await driver.pause(3000);
});

When(
  "I open the official {string} page for {string}",
  async function (section, university) {
    let html = await driver.getPageSource();
    if (hasCaptcha(html)) {
      if (!allowManualCaptcha) {
        throw new Error(
          "Google mostró un CAPTCHA por tráfico automático. Ejecuta con ALLOW_MANUAL_CAPTCHA=true para resolverlo manualmente o cambia de red/IP.",
        );
      }
      console.log("CAPTCHA detectado. Resuelvelo manualmente en el celular...");
      await driver.waitUntil(
        async () => {
          const source = await driver.getPageSource();
          return !hasCaptcha(source);
        },
        {
          timeout: 180000,
          interval: 2000,
          timeoutMsg: "CAPTCHA no fue resuelto en 3 minutos.",
        },
      );
    }

    const page = getOfficialPage(university, section);
    this.__expectedOfficialHost = page.urlContains;
    await driver.url(page.url);
    await driver.pause(3000);
  },
);

Then(
  "the current URL should contain the expected official host",
  async function () {
    const expected = this.__expectedOfficialHost;
    assert.ok(
      expected,
      'Falta host esperado: ejecuta antes "I open the official ... page".',
    );
    const currentUrl = await driver.getUrl();
    assert.ok(
      currentUrl.includes(expected),
      `Se esperaba URL que contenga "${expected}" pero se obtuvo: "${currentUrl}"`,
    );
  },
);

/** Orden: id / aria-label / name conocidos por sitio, luego genéricos (sin usar mailto). */
When(
  "I search for {string} within the page using id-first selectors",
  async function (searchTerm) {
    const currentUrl = await driver.getUrl();
    const searchSelectors = [
      ...selectorsForCurrentUrl(currentUrl),
      "#search-input",
      "input#search",
      "input#q",
      "input#s",
      "textarea#search",
      '#search input[type="text"]',
      "#buscador input",
      'input[id*="search" i]',
      'input[id*="buscar" i]',
      'textarea[id*="search" i]',
      'input[type="search"]',
      'input[name="s"]',
      'input[name="q"]',
      'input[placeholder*="buscar" i]',
      'input[placeholder*="search" i]',
      'input[aria-label*="buscar" i]',
      'input[aria-label*="search" i]',
      'textarea[aria-label*="buscar" i]',
      ".search-input",
    ];

    let searchBox = null;
    for (const selector of searchSelectors) {
      try {
        const el = await driver.$(selector);
        const displayed = await el.isDisplayed();
        if (displayed) {
          searchBox = el;
          break;
        }
      } catch (_) {}
    }

    if (!searchBox) {
      const urlObj = new URL(currentUrl);
      await driver.url(`${urlObj.origin}/?s=${encodeURIComponent(searchTerm)}`);
      await driver.pause(2000);
      return;
    }

    await searchBox.clearValue();
    await searchBox.setValue(searchTerm);
    await driver.keys(["Enter"]);
    await driver.pause(2000);
  },
);

Then("I should see results related to {string}", async function (searchTerm) {
  const pageSource = await driver.getPageSource();
  const lowerSource = pageSource.toLowerCase();
  const lowerTerm = searchTerm.toLowerCase();
  assert.ok(
    lowerSource.includes(lowerTerm),
    `Expected page to contain "${searchTerm}" but it was not found`,
  );
});
