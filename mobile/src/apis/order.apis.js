import axios from '../axios'


export function userLoginAPI(data) {
    return axios.post(`/order`, data)
}