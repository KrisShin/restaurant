import axios from './axios'


export function dishTagsAPI(data) {
    return axios.get(`merchant/dish/tags/`, data)
}

export function dishListAPI(data) {
    return axios.post(`customer/dish/list/`, data)
}

export function tagListAPI(data) {
    return axios.get(`customer/dish/tags/`, data)
}

export function tagAddAPI(data) {
    return axios.post(`customer/dish/tags/`, data)
}

export function dishOperateAPI(data) {
    return axios.post(`merchant/dish/0/`, data)
}

export function dishGetDetailAPI(data) {
    return axios.get(`merchant/dish/${data.id}/`, data)
}
