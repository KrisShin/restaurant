import axios from '../axios'


export function dishTagsAPI(data) {
    return axios.get(`/dish/tags`, data)
}
