const {
  setWorldConstructor,
  World,
  Before,
  After,
  setDefaultTimeout,
} = require("@cucumber/cucumber");
const { chromium } = require("playwright");

setDefaultTimeout(60 * 1000);

class PlaywrightWorld extends World {
  constructor(options) {
    super(options);
  }
}

setWorldConstructor(PlaywrightWorld);

Before(async function () {
  const headed = process.env.HEADED === "true";
  this.browser = await chromium.launch({
    headless: !headed,
    args: [
      "--disable-blink-features=AutomationControlled",
      "--no-sandbox",
      "--disable-dev-shm-usage",
    ],
  });
  this.context = await this.browser.newContext({
    viewport: { width: 1280, height: 900 },
    userAgent:
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
  });
  this.page = await this.context.newPage();
});

After(async function () {
  await this.context?.close();
  await this.browser?.close();
});
