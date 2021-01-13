import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// 通用的状态数据管理对象
import common from './common'

export default new Vuex.Store({
  // state: {
  // },
  // mutations: {
  // },
  // actions: {
  // },
  modules: {
    common
  }
})
