// 引入 axios 库
import axios from 'axios'
import store from '../store'

import { Message } from 'element-ui'

const Ajax = axios.create({
  timeout: 5000 // 超时
})

// 使用Axios的拦截器来实现用户token注入，拦截非法请求
Ajax.interceptors.request.use(config => {
  // 注入 token
  let token = store.getters['common/getToken'] || ''
  // 对不是要求登录后才能进行接口请求的接口进行放行
  let paths = ['/user/app/code', '/user/app/login', '/user/app/register']
  if (paths.includes(config.url)) return config
  // 对有拦截需求的接口进行拦截，并把 token 添加到请求头中，因为系统中是使用 token 来对当前用户进行验证
  if (!!token) {
    config.headers.token = token
    return config
  } else {
    return Promise.reject({ code: 998, message: '没有token' })
  }
})

// 响应拦截
Ajax.interceptors.response.use(response => {
  let _d = response.data
  if (!_d) {
    Message.error('请求无响应')
  } else {
    if (_d.code === 403) {
      Message.error('用户登录失效，请重新登录')
    }
  }
  return response
})

export default req => {
  return new Promise(resolve => {
    Ajax({
      url: req.url,
      method: req.method || 'GET',
      data: req.data || {},
      // GET 请求传参
      params: req.params || {},
      baseURL: req.baseURL || window.BASE_URL
    }).then(res => {
      // 返回的是 response 对象，前端接口需要 response.data
      resolve(res.data)
    }).catch(e => {
      if (e.code === 998) {
        resolve(e)
      } else {
        resolve({ code: 999, message: '本地错误' })
      }
    })
  })
}