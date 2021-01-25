import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import BASE_API from './utils/settings'


Vue.config.productionTip = false
Vue.prototype.$BASE_API = BASE_API

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')
