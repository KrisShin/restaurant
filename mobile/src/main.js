import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import BASE_API from './utils/settings'
import {
  Tag, Grid, GridItem, Empty, Toast, NavBar,
  Field, Button, Col, Row, Icon, Image as VanImage,
  Lazyload, Swipe, SwipeItem, Tabbar, TabbarItem,
  Notify
} from "vant";


Vue.config.productionTip = false
Vue.prototype.$BASE_API = BASE_API

Vue.use(Button);
Vue.use(Col);
Vue.use(Row);
Vue.use(Empty);
Vue.use(Grid);
Vue.use(GridItem);
Vue.use(Tag);
Vue.use(Field)
Vue.use(NavBar)
Vue.use(Tabbar);
Vue.use(TabbarItem);
Vue.use(Swipe);
Vue.use(SwipeItem);
Vue.use(Icon);
Vue.use(VanImage);
Vue.use(Lazyload);
Vue.use(Toast)
Vue.use(Notify);

new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')
