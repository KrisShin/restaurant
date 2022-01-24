/*
 * @Author: windyGu
 * @Date: 2022-01-20 23:10:15
 * @LastEditors: windyGu
 * @LastEditTime: 2022-01-23 12:49:51
 * @FilePath: \restaurant\web-manager\vue.config.js
 * @Description: 
 */



const path = require('path');
const CompressionPlugin = require("compression-webpack-plugin")

const env = process.env.NODE_ENV

function resolve(dir) {
  return path.join(__dirname, dir)
}

module.exports = {


  publicPath: "/",  //根域上下文
  outputDir: "dist",  //构建输出目录
  assetsDir: "assets",    //静态文件目录
  lintOnSave: true,       //eslint保存检测，有效值：ture | false | 'error'
  runtimeCompiler: true, // 运行时版本是否需要编译
  productionSourceMap: false,  //在构建生产包时生成 sourceMap 文件，false将提高构建速度

  devServer: {

    port: 8901,
    disableHostCheck: true,
    // proxy: {
    //   "/api": {
    //     target: "http://101.34.234.17:9096",
    //     ws: true,
    //     changeOrigin: true
    //   }
    // }
  },

  //简单的配置插件用法
  // configureWebpack: (config) => {
  //   let plugin = [new plugin1({ args }), new plugin2(args)]

  //   config.plugins = [...plugin]
  // },

  //链式操作插件
  chainWebpack: (config) => {

    //定义目录别名
    config.resolve.alias
      .set('@', resolve('src'))
      .set('api', resolve('src/api'))
      .set('common', resolve('src/common'))


    if (env !== 'development') {
      // 移除console 和 debugger
      config.optimization
        .minimize(true)
        .minimizer('terser')
        .tap(args => {
          let { terserOptions } = args[0];
          terserOptions.compress.drop_console = true;
          terserOptions.compress.drop_debugger = true;
          return args;
        })

      //gzip压缩
      config.plugin('CompressionPlugin')
        .use(new CompressionPlugin({
          filename: '[path].gz[query]',
          algorithm: 'gzip',
          test: /\.js$|\.html$|\.css/,
          threshold: 10240,
          minRatio: 0.8,
          deleteOriginalAssets: true
        }));
    }





  }

}