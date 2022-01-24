/*
 * @Author: windyGu
 * @Date: 2022-01-16 20:18:52
 * @LastEditors: windyGu
 * @LastEditTime: 2022-01-25 00:20:08
 * @FilePath: \restaurant\web-manager\src\api\index.js
 * @Description: 
 */

import Axios from "axios";
import { baseUrl } from '../../env.config'
import store from "@/store/index"




//config init
let token = store.state.token
const baseApi = baseUrl


let axios = Axios.create({
    // axios init
    baseURL: baseApi,
    timeout: 1000 * 10,
    headers: {
        Authorization: token,
    }
})






// TODO:interceptors for request && response

// service.interceptors.request.use(
//     config => {
//         // do something before request is sent

//         if (store.getters.token) {
//             // let each request carry token
//             // ['X-Token'] is a custom headers key
//             // please modify it according to the actual situation
//             config.headers['Authorization'] = getToken()
//         }
//         return config
//     },
//     error => {
//         // do something with request error
//         console.log(error) // for debug
//         return Promise.reject(error)
//     }
// )


// axios.interceptors.response.use(function (response) {

// }, function (error) {

// })

// 封装请求（预留） 
export default function httpRequest(config) {

    return axios.request(config)
}




