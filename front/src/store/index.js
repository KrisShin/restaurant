import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  // 启用命名空间
  namespaced: true,
  state: {
    token: sessionStorage.getItem('token') || localStorage.getItem('token'),
    isLogin: '',
    userInfo: JSON.parse(sessionStorage.getItem('userInfo') || localStorage.getItem('userInfo'))
  },
  getters: {
    getToken: state => state.token,
    getUserInfo: state => state.userInfo
  },
  actions: {
    // 定义一个设置 token 值的动作，第一个参数为 action 的形参 store 对象
    setToken({
      commit
    }, token) {
      commit('mutationToken', token)
    },
    setUserInfo({
      commit
    }, user) {
      commit('mutationUserInfo', user)
    }
  },
  mutations: {
    mutationToken(state, token) {
      state.token = token
      state.isLogin = state.token ? true : false
      sessionStorage.setItem('token', token)
      localStorage.setItem('token', token)
      sessionStorage.setItem('isLogin', state.isLogin)
    },
    mutationUserInfo(state, user) {
      state.userInfo = user
      localStorage.setItem('userInfo', JSON.stringify(user))
      sessionStorage.setItem('userInfo', JSON.stringify(user))
    }
  }
})