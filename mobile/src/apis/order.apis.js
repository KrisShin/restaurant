import axios from '../axios'


export function orderAddAPI(data) {
    return axios.post(`/order/0`, data)
}

export function orderGetAPI(data) {
    return axios.get(`/order/${data.id}`, data)
}

export function orderEditAPI(data) {
    return axios.put(`/order/${data.id}`, data)
}

export function orderDelAPI(data) {
    return axios.delete(`/order/${data.id}`, data)
}

export function orderListAPI(data) {
    return axios.get(`/order/list`, data)
}

export function orderStatusAPI(data) {
    return axios.get(`/order/status`, data)
}
