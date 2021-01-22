import axios from 'axios'
import store from '../store'
const service = axios.create({
    baseURL: process.env.BASE_API,
    timeout: 3 * 1000
})
service.interceptors.request.use(config => {
    // config.data = JSON.stringify(config.data);
    config.headers = {
        // 'Content-Type': 'application/x-www-form-urlencoded' //配置请求头
        'Content-Type': 'application/json;charset=UTF-8', //配置请求头
        "Authorization": store.state.token
    }
    return config
}, error => {
    Promise.reject(error)
})
//4.导入文件
export default service