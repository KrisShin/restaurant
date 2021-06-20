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
      title: '恰了木有App',
    }
  },
  devServer: {
    host: '0.0.0.0', // 允许外部ip访问
    port: 9093,
    https: false, // 启用https
    disableHostCheck: true,
    proxy: {
      '/api': {
        target: 'http://3.36.97.169:9096/customer',
        // target: 'http://127.0.0.1:9096/customer',
        changeOrigin: true,
        secure: false,
        pathRewrite: {
          '^/api': '/api'
        }
      }
    }
  },
  css: {
    loaderOptions: {
      less: {
        // 若 less-loader 版本小于 6.0，请移除 lessOptions 这一级，直接配置选项。
        lessOptions: {
          modifyVars: {
            // 直接覆盖变量
            'text-color': '#111',
            'border-color': '#eee',
            'uploader-size': '180px',
            // 或者可以通过 less 文件覆盖（文件路径为绝对路径）
            hack: `true; @import "your-less-file-path.less";`,
          },
        },
      },
    },
  },
}