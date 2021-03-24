import axios from '../axios'


export function addrListAPI(data) {
    return axios.get(`/addr/list`, data)
}

export function addrGetAPI(data) {
    return axios.get(`/addr/${data.id}`, data)
}

export function addrAddAPI(data) {
    return axios.post(`/addr/0`, data)
}

export function addrEditAPI(data) {
    return axios.put(`/addr/${data.id}`, data)
}

export function addrDelAPI(data) {
    return axios.delete(`/addr/${data.id}`, data)
}
