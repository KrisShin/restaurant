module.exports = {
  devServer: {
    host: '127.0.0.1',//'0.0.0.0', // 允许外部ip访问
    port: 9093,
    https: false, // 启用https
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:9096',
        changeOrigin: true,
        secure: false,
        pathRewrite: {
          '^/api': '/api'
        }
      }
    }
  }
}