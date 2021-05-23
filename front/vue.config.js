module.exports = {
  // 部署应用包时的基本 URL
  publicPath: '',
  // 打包输出文件夹名
  outputDir: 'dist',
  // 禁用 eslint
  lintOnSave: false,
  pages: {
    'index': {
      // page 的入口
      entry: 'src/main.js',
      // 模板来源
      template: 'public/index.html',
      // 在 dist/index.html 的输出
      filename: 'index.html',
      // 当使用 title 选项时，
      // template 中的 title 标签需要是 <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'Restaurant',
    }
  },
  devServer: {
    host: '0.0.0.0', // 允许外部ip访问
    port: 9091,
    https: false, // 启用https
    open: true,
    disableHostCheck: true,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:9096/merchant',
        changeOrigin: true,
        secure: false,
        pathRewrite: {
          '^/api': '/api'
        }
      }
    }
  },  
}