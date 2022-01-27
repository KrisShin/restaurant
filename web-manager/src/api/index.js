/*
 * @Author: windyGu
 * @Date: 2022-01-16 20:18:52
 * @LastEditors: windyGu
 * @LastEditTime: 2022-01-28 00:53:44
 * @FilePath: \restaurant\web-manager\src\api\index.js
 * @Description: 
 */

import Axios from "axios";
import { baseUrl } from '../../env.config'
import store from "@/store/index"
import statusCode from "@/config/error.config"




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

axios.interceptors.request.use(
    config => {
        //do something with request config

        return config
    },
    error => {
        // do something with request error
        return Promise.reject(error)
    }
)


axios.interceptors.response.use(
    response => {
        //do something with response config
    },
    error => {

        // do something with response error
        if (statusCode[error.response.status]) {
            ElementUI.Message.error(statusCode[error.response.status])

        }
        else
            ElementUI.Message.error("出错啦，请联系管理员！")
    })

// 封装请求（预留） 
export default function httpRequest(config) {

    return axios.request(config)
}




