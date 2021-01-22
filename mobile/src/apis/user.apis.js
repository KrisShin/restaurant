import http from '../utils/http'
import BASE_API from '../utils/settings'
/**
 *  @parms resquest 请求地址 例如：http://197.82.15.15:8088/request/...
 *  @param '/testIp'代表vue-cil中config，index.js中配置的代理
 */

export function userLoginAPI(data) {
    return http.post(`${BASE_API}/user/login`, data)
}
export function userLogoutAPI(data) {
    return http.post(`${BASE_API}/user/logout`, data)
}
// testAPI
// export function getAPI(params) {
//     return http.get(`${BASE_API}/user/test`, params)
// }
// export function postAPI(params) {
//     return http.post(`${BASE_API}/user/add_tags`, params)
// }
// export function putAPI(params) {
//     return http.put(`${BASE_API}/user/test`, params)
// }
// export function delAPI(params) {
//     return http.delete(`${BASE_API}/user/test`, params)
// }

// export function uploadAvatarApi(params) {
//     return http.post(`${BASE_API}/user/upload_avatar`, params)
// }
