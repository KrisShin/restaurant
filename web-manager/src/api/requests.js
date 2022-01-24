/*
 * @Author: windyGu
 * @Date: 2022-01-16 20:18:52
 * @LastEditors: windyGu
 * @LastEditTime: 2022-01-25 00:22:44
 * @FilePath: \restaurant\web-manager\src\api\requests.js
 * @Description: interface management
 */

import httpRequest from './index'


// test for  method get
export const testGet = () => httpRequest({
    type: 'get',
    url: '/user/test/',
})


