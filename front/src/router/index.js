import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login.vue'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [{
  path: '/',
  name: 'Login',
  component: Login
}]

const router = new VueRouter({
  // mode: 'history',
  // base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some((r) => r.meta.requireAuth)) {
    let isLogin = JSON.parse(sessionStorage.getItem('isLogin'));
    if (isLogin) { //判断是否已经登录
      next();
    } else {
      next({
        path: '/login',
        // query: { redirect: to.fullPath }   //登录成功后重定向到当前页面
      });
    }
  } else {
    next();
  }
  //如果本地 存在 token 则 不允许直接跳转到 登录页面
  if (to.fullPath === "/login") {
    if (JSON.parse(sessionStorage.getItem('isLogin'))) {
      next({
        path: from.fullPath
      });
    } else {
      next();
    }
  }
});

export default router