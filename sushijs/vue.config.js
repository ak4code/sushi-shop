const BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  outputDir: 'bundle/dist',
  baseUrl: process.env.NODE_ENV === 'production'
    ? '/'
    : 'http://localhost:8080/',
  css: {
    extract: true
  },
  pages: {
    index: {
      entry: 'src/main.js',
      chunks: ['chunk-vendors', 'chunk-common', 'index']
    },
    products: {
      entry: 'src/pages/products.js'
    }
  },
  configureWebpack: {
    plugins: [
      new BundleTracker({filename: process.env.NODE_ENV === 'production' ? './webpack-prod-stats.json' : './webpack-stats.json'})
    ]
  }
}
