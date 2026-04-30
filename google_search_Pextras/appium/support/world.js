const { setWorldConstructor, setDefaultTimeout } = require('@cucumber/cucumber');

// Increase timeout for Appium operations (mobile automation is slower)
setDefaultTimeout(60 * 1000);

class AppiumWorld {
  constructor({ attach, parameters }) {
    this.attach = attach;
    this.parameters = parameters;
    this.driver = null;
  }
}

setWorldConstructor(AppiumWorld);
