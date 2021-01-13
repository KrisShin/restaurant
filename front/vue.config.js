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
    port: 9527,
    open: true,
    openPage: '/index.html',
    proxy: {
      '/apis': {
        target: 'http://www.shuiyue.info:12600',
        pathRewrite: {'/apis': ''}
      }
    }
  }
}