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