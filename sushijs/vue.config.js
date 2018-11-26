const BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  baseUrl: process.env.NODE_ENV === 'production'
    ? '/'
    : 'http://localhost:8080/',
  css: {
    extract: true
  },
  configureWebpack: {
    plugins: [
      new BundleTracker({filename: './webpack-stats.json'})
    ]
  }
}
