import http from '../utils/http'
import BASE_API from '../utils/settings'
/**
 *  @parms resquest 请求地址 例如：http://197.82.15.15:8088/request/...
 *  @param '/testIp'代表vue-cil中config，index.js中配置的代理
 */

export function addrListAPI(data) {
    return http.get(`${BASE_API}/addr/`, data)
}
export function addrGetAPI(data) {
    return http.get(`${BASE_API}/addr/${data.id}`, data)
}
export function addrAddAPI(data) {
    return http.post(`${BASE_API}/addr/${0}`, data)
}
export function addrEditAPI(data) {
    return http.put(`${BASE_API}/addr/${data.id}`, data)
}
export function addrDelAPI(data) {
    return http.delete(`${BASE_API}/addr/${data.id}`, data)
}
