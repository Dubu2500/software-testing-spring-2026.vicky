// wdio.conf.js
exports.config = {
  hostname: "localhost",
  port: 4723,
  path: "/",

  capabilities: [
    {
      platformName: "Android",
      "appium:deviceName": "Android Device",
      "appium:udid": process.env.ANDROID_UDID || "GQFIR469AMW4D6AM",
      "appium:automationName": "UiAutomator2",
      "appium:browserName": "Chrome",
      "appium:chromedriverAutodownload": true,
      "appium:chromeOptions": {
        args: ["--disable-blink-features=AutomationControlled"],
      },
    },
  ],

  specs: ["./features/*.feature"],
  framework: "cucumber",

  cucumberOpts: {
    require: ["./steps/*.js"],
    timeout: 60000,
  },
};
