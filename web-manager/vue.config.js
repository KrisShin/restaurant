module.exports = {

    devServer: {

        publicPath: "/",  //根域上下文
        outputDir: "dist",  //构建输出目录
        assetsDir: "assets",    //静态文件目录
        lintOnSave: true,       //eslint保存检测，有效值：ture | false | 'error'
        runtimeCompiler: true, // 运行时版本是否需要编译
        productionSourceMap: false,  //在构建生产包时生成 sourceMap 文件，false将提高构建速度

        port: 8901,
        disableHostCheck: true,
        proxy: {
            "/api": {
                target: "http://101.34.137.128:9096",
                ws: true,
                changeOrigin: true
            }
        }
    }

}