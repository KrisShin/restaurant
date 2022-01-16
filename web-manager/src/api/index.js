import axios from "axios";


// 配置
let token = "token"
const baseApi = "101.34.234.17:9096/api"


let instence = axios.create({
    // axios init
    baseURL: baseApi,
    timeout: 1000,
    headers: {
        Authorization: token,
    }
})



axios.interceptors.response.use(function (response) {

}, function (error) {

})

export default instence



