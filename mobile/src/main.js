import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import BASE_API from './utils/settings'
import { Toast } from 'vant'


Vue.config.productionTip = false
Vue.prototype.$BASE_API = BASE_API
Vue.use(Toast)

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')
