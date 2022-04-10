const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

module.exports = {
  lintOnSave: false,
  configureWebpack: {
    experiments: {
      syncWebAssembly: true,
    },
  },
  outputDir: 'dist',
  publicPath: process.env.NODE_ENV === 'production'
    ? '/video_storage/'
    : '/'
}
