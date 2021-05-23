import Vue from 'vue'
import router from './router'
import store from './store'
import { Button, Select, Container, Header, Main,Footer } from 'element-ui';
import App from './App.vue';

Vue.use(Button)
Vue.use(Container)
Vue.use(Footer)
Vue.use(Header)
Vue.use(Main)
Vue.use(Select)
 

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
