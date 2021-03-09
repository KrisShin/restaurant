import axios from 'axios'
import store from '../store'
import router from '../router'
import { Toast } from 'vant'

const service = axios.create({
    baseURL: process.env.BASE_API,
    timeout: 3 * 1000
})

// 请求拦截
service.interceptors.request.use(config => {
    config.data = JSON.stringify(config.data);
    config.headers = {
        // 'Content-Type': 'application/x-www-form-urlencoded' //配置请求头
        'Content-Type': 'application/json;charset=utf-8', //配置请求头
        "Authorization": store.state.common.token
    }
    return config
}, error => {
    Promise.reject(error)
})

// 响应拦截
service.interceptors.response.use(res => {
    console.log('响应被截胡了', res)
    const { success, code } = res.data
    if (success === false && (code === 10010 || code === 10011)) {
        // 1. 提示
        if (code === 10010) Toast.fail('token失效')
        else if (code === 10011) Toast.fail('token无效')

        // 2. 删除本地token 和 user_info
        store.dispatch("common/setToken", null);
        store.dispatch("common/setUserInfo", null);

        // 3. 跳转 login
        router.push('/login')
    }
    return res
}, error => {
    Promise.reject(error)
})

export default service