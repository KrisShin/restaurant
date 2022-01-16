// 引入 axios 库
import axios from 'axios'
import store from '../store'
import vue from '../main'

const service = axios.create({
  baseURL: 'http://127.0.0.1:9096/', // 'http://3.36.97.169:9096/customer',
  timeout: 60000 // 超时
})

// 请求拦截
service.interceptors.request.use(config => {
  config.data = JSON.stringify(config.data);
  config.headers = {
    // 'Content-Type': 'application/x-www-form-urlencoded' //配置请求头
    'Content-Type': 'application/json;charset=utf-8', //配置请求头
    "Authorization": store.state.token
  }
  return config
}, error => {
  Promise.reject(error)
})

// 响应拦截
service.interceptors.response.use(resp => {
  const {
    code
  } = resp.data
  if (code === 10010 || code === 10011) {
    // 1. 提示
    if (code === 10010) vue.$message.error('登录过期, 请重新登录')
    else if (code === 10011) vue.$message.error('口令无效, 请重新登录')

    // 2. 删除本地token 和 user_info
    store.dispatch("setToken", null);
    store.dispatch("setUserInfo", null);

    // 3. 跳转 login
    vue.$router.replace('/login')
    return
  } else if (code != 200) {
    vue.$message.error(resp.data.msg)
  }
  return resp
}, (error) => {
  Promise.reject(error)
})

export default service