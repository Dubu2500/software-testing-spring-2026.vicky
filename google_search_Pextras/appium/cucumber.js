module.exports = {
  default: {
    require: [
      'steps/**/*.js',
      'support/**/*.js',
    ],
    format: [
      'progress-bar',
      'html:reports/cucumber-report.html',
      'json:reports/cucumber-report.json',
    ],
    formatOptions: {
      snippetInterface: 'async-await',
    },
  },
};
