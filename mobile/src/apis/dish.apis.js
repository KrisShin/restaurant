import http from '../utils/http'
import BASE_API from '../utils/settings'
/**
 *  @parms resquest 请求地址 例如：http://197.82.15.15:8088/request/...
 *  @param '/testIp'代表vue-cil中config，index.js中配置的代理
 */

export function dishTagsAPI(data) {
    return http.get(`${BASE_API}/dish/tags`, data)
}
