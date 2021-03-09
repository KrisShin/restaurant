export function userLoginAPI(data) {
    return this.$axios.post(`/user/login`, data)
}

export function userLogoutAPI(data) {
    return this.$axios.post(`/user/logout`, data)
}

export function userInfoAPI(data) {
    return this.$axios.get(`/user/profile`, data)
}

export function userEditInfoAPI(data) {
    return this.$axios.put(`/user/profile`, data)
}

export function userChangeEmailAPI(data) {
    return this.$axios.put(`/user/change_email`, data)
}

export function userRegisterAPI(data) {
    return this.$axios.post(`/user/register`, data)
}

export function userTagsAPI(data) {
    return this.$axios.put(`/user/tags`, data)
}

export function userSendCaptchaAPI(data) {
    return this.$axios.post(`/user/email_captcha`, data)
}

export function userChangePwdAPI(data) {
    return this.$axios.put(`/user/change_pwd`, data)
}

export function userTestAPI(data) {
    return this.$axios.post(`/user/test`, data)
}

// export function uploadAvatarAPI(params) {
//     return http.post(`/user/upload_avatar`, params)
// }