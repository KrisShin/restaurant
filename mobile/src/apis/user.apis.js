import axios from '../axios'


export function userLoginAPI(data) {
    return axios.post(`/user/login`, data)
}

export function userLogoutAPI(data) {
    return axios.post(`/user/logout`, data)
}

export function userInfoAPI(data) {
    return axios.get(`/user/profile`, data)
}

export function userEditInfoAPI(data) {
    return axios.put(`/user/profile`, data)
}

export function userChangeEmailAPI(data) {
    return axios.put(`/user/change_email`, data)
}

export function userRegisterAPI(data) {
    return axios.post(`/user/register`, data)
}

export function userTagsAPI(data) {
    return axios.put(`/user/tags`, data)
}

export function userSendCaptchaAPI(data) {
    return axios.post(`/user/email_captcha`, data)
}

export function userChangePwdAPI(data) {
    return axios.put(`/user/change_pwd`, data)
}

export function userTestAPI(data) {
    return axios.post(`/user/test`, data)
}

// export function uploadAvatarAPI(params) {
//     return axios.post(`/user/upload_avatar`, params)
// }