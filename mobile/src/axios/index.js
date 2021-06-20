import axios from 'axios'
import store from '../store'
import vue from '../main'

const service = axios.create({
    baseURL: 'http://3.36.97.169:9096/customer',  // 'http://127.0.0.1:9096/customer', 
    timeout: 3000
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
    const { success, code } = res.data
    if (success === false && (code === 10010 || code === 10011)) {
        // 1. 提示
        if (code === 10010) vue.$toast.fail('登录过期, 请重新登录')
        else if (code === 10011) vue.$toast.fail('口令无效, 请重新登录')

        // 2. 删除本地token 和 user_info
        vue.$store.dispatch("common/setToken", null);
        vue.$store.dispatch("common/setUserInfo", null);

        // 3. 跳转 login
        vue.$router.replace('/login')
        return
    }
    return res
}, (error) => {
    Promise.reject(error)
})

export default service