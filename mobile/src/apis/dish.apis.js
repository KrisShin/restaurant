export function dishTagsAPI(data) {
    return this.$axios.get(`/dish/tags`, data)
}
