/*
 * @Author: windyGu
 * @Date: 2022-01-22 18:18:35
 * @LastEditors: windyGu
 * @LastEditTime: 2022-01-23 00:57:20
 * @FilePath: \restaurant\web-manager\env.config.js
 * @Description: 
 */


let baseUrl = '';

if (process.env.NODE_ENV === 'testing') {
    baseUrl = "http://101.34.234.17:9096/customer"
} else if (process.env.NODE_ENV === 'production') {
    baseUrl = "http://101.34.234.17:9096/customer"

} else {
    baseUrl = "http://101.34.234.17:9096/customer"

}



export { baseUrl } 