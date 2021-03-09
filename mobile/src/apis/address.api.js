export function addrListAPI(data) {
    return this.$axios.get(`/addr/`, data)
}
export function addrGetAPI(data) {
    return this.$axios.get(`/addr/${data.id}`, data)
}
export function addrAddAPI(data) {
    return this.$axios.post(`/addr/${0}`, data)
}
export function addrEditAPI(data) {
    return this.$axios.put(`/addr/${data.id}`, data)
}
export function addrDelAPI(data) {
    return this.$axios.delete(`/addr/${data.id}`, data)
}
