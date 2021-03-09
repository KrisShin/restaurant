export default {
  // 启用命名空间
  namespaced: true,
  state: {
    token: '',
    isLogin: '',
    userInfo: ''
  },
  getters: {
    getToken: state => state.token,
    getUserInfo: state => state.userInfo
  },
  actions: {
    // 定义一个设置 token 值的动作，第一个参数为 action 的形参 store 对象
    setToken({ commit }, token) {
      commit('mutationToken', token)
    },
    setUserInfo({ commit }, user) {
      commit('mutationUserInfo', user)
    }
  },
  mutations: {
    mutationToken(state, token) {
      state.token = token
      state.isLogin = state.token ? true : false
      // localStorage.setItem('token', token)
      sessionStorage.setItem('isLogin', state.token ? true : false)
    },
    mutationUserInfo(state, user) {
      state.userInfo = user
      // localStorage.setItem('userInfo', user)
    }
  }
}