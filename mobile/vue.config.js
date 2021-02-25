module.exports = {
  devServer: {
    host: '0.0.0.0', // 允许外部ip访问
    port: 9093,
    https: false, // 启用https
    disableHostCheck: true,
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