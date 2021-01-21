<template>
  <div id="Register">
    <van-nav-bar title="恰了木有-注册" @click-left="onClickReturn" left-arrow />
    <div>
      <!-- 输入任意文本 -->
      <van-field v-model="text" label="昵称" />
      <!-- 输入手机号，调起手机号键盘 -->
      <van-field v-model="phone" type="tel" label="手机号" />
      <!-- 允许输入正整数，调起纯数字键盘 -->
      <van-field v-model="digit" type="digit" label="年龄" />
      <!-- 允许输入数字，调起带符号的纯数字键盘 -->
      <van-field v-model="number" type="email" label="邮箱" />
      <!-- 输入密码 -->
      <van-field v-model="password" type="password" label="密码" />
      <button>注册</button
      ><span>已有账号?<router-link to="/login">登录</router-link></span>
    </div>
  </div>
</template>
<script>
import Vue from "vue";
import { Field, NavBar } from "vant";

Vue.use(NavBar);
Vue.use(Field);

export default {
  name: "Register",
  data() {
    return {
      text: "",
      phone: "",
      digit: null,
      number: null,
      password: "",
    };
  },
  created(){
    this.phone = this.$route.query.phone
  },
  methods: {
    onClickReturn() {
      this.$router.go(-1);
    },
  },
};
</script>