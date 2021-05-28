import Vue from 'vue'
import router from './router'
import store from './store'
import {
  Button,
  Select,
  Container,
  Header,
  Main,
  Footer,
  Input,
  Row,
  Col
} from 'element-ui';
import App from './App.vue';

Vue.use(Button)
Vue.use(Col)
Vue.use(Container)
Vue.use(Footer)
Vue.use(Header)
Vue.use(Input)
Vue.use(Main)
Vue.use(Row)
Vue.use(Select)
 

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
