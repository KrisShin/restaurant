/*
 * @Author: windyGu
 * @Date: 2022-01-16 20:18:52
 * @LastEditors: windyGu
 * @LastEditTime: 2022-01-24 22:49:09
 * @FilePath: \restaurant\web-manager\src\store\index.js
 * @Description: 
 */
import Vue from 'vue'
import Vuex from 'vuex'
import * as mutations from './mutations'
import * as getters from './getters'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: ''
  },
  mutations,
  getters,
})
