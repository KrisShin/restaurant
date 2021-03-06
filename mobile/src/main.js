import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import {
  ActionSheet, Tag, Grid, GridItem, Empty, Toast, NavBar,
  Field, Button, Col, Row, Icon, Image as VanImage,
  Lazyload, Swipe, SwipeItem, Tabbar, TabbarItem,
  Notify, Cell, CellGroup, Dialog, Uploader, AddressList,
  AddressEdit, Radio, RadioGroup, SubmitBar, Card, Stepper,
  PullRefresh, List, Checkbox, CheckboxGroup, SwipeCell, GoodsAction,
  GoodsActionIcon, GoodsActionButton
} from "vant";


Vue.config.productionTip = false
Vue.prototype.$BASE_API = 'http://127.0.0.1:9096' // 'http://3.36.97.169:9096'

Vue.use(ActionSheet);
Vue.use(AddressEdit);
Vue.use(AddressList);
Vue.use(Button);
Vue.use(Card);
Vue.use(Cell);
Vue.use(Checkbox);
Vue.use(CheckboxGroup);
Vue.use(CellGroup);
Vue.use(Col);
Vue.use(Dialog);
Vue.use(Empty);
Vue.use(Field)
Vue.use(GoodsAction);
Vue.use(GoodsActionButton);
Vue.use(GoodsActionIcon);
Vue.use(Grid);
Vue.use(GridItem);
Vue.use(Icon);
Vue.use(Lazyload);
Vue.use(List);
Vue.use(NavBar)
Vue.use(Notify);
Vue.use(PullRefresh);
Vue.use(Radio);
Vue.use(RadioGroup);
Vue.use(Row);
Vue.use(Stepper);
Vue.use(SubmitBar);
Vue.use(Swipe);
Vue.use(SwipeCell);
Vue.use(SwipeItem);
Vue.use(Tabbar);
Vue.use(TabbarItem);
Vue.use(Tag);
Vue.use(Toast)
Vue.use(Uploader);
Vue.use(VanImage);

var vue = new Vue({
  store,
  router,
  render: h => h(App),
}).$mount('#app')

export default vue