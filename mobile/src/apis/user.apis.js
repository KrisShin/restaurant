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

export function userInfoAPI(data) {
    return http.get(`${BASE_API}/user/profile`, data)
}

export function userEditInfoAPI(data) {
    return http.put(`${BASE_API}/user/profile`, data)
}

export function userChangeEmailAPI(data) {
    return http.put(`${BASE_API}/user/change_email`, data)
}

export function userRegisterAPI(data) {
    return http.post(`${BASE_API}/user/register`, data)
}

export function userTagsAPI(data) {
    return http.put(`${BASE_API}/user/tags`, data)
}

export function userSendCaptchaAPI(data) {
    return http.post(`${BASE_API}/user/email_captcha`, data)
}

// export function uploadAvatarAPI(params) {
//     return http.post(`${BASE_API}/user/upload_avatar`, params)
// }