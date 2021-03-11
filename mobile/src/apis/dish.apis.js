import axios from '../axios'


export function dishTagsAPI(data) {
    return axios.get(`/dish/tags`, data)
}

export function dishPushAPI(data) {
    return axios.get(`/dish/push`, data)
}

export function dishListAPI(data) {
    return axios.post(`/dish/list`, data)
}
