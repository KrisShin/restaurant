// 导入封装好的axios实例
import request from './request'

const http = {
    /**
     * methods: 请求
     * @param url 请求地址 
     * @param params 请求参数
     */
    get(url, data) {
        const config = {
            method: 'get',
            url: url,
            params: data
        }
        // if (params) config.data = params
        return request(config)
    },
    post(url, data) {
        const config = {
            method: 'post',
            url: url,
            data
        }
        // if (params) config.data = params
        return request(config)
    },
    put(url, data) {
        const config = {
            method: 'put',
            url: url,
            data
        }
        // if (params) config.data = params
        return request(config)
    },
    delete(url, data) {
        const config = {
            method: 'delete',
            url: url,
            data
        }
        // if (params) config.data = params
        return request(config)
    }
}
//导出
export default http
