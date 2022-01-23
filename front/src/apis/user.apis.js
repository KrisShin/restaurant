import axios from './axios'


export function userLoginAPI(data) {
    return axios.post(`merchant/user/login/`, data)
}

export function userLogoutAPI(data) {
    return axios.post(`merchant/user/logout/`, data)
}

export function userChangeEmailAPI(data) {
    return axios.put(`merchant/user/change_email/`, data)
}

export function userTagsAPI(data) {
    return axios.put(`merchant/user/tags/`, data)
}

export function userSendCaptchaAPI(data) {
    return axios.post(`merchant/user/email_captcha/`, data)
}

export function userChangePwdAPI(data) {
    return axios.put(`merchant/user/change_pwd/`, data)
}

export function userResetPwdAPI(data) {
    return axios.put(`merchant/user/reset_pwd/`, data)
}

// export function uploadAvatarAPI(params) {
//     return axios.post(`/user/upload_avatar`, params)
// }