<template>
  <div id="Login">
    <van-nav-bar title="恰了木有-登录" @click-left="onClickReturn" left-arrow />
    <div>
      <!-- 输入手机号，调起手机号键盘 -->
      <van-field v-model="phone" type="text" maxlength="11" label="手机号" />
      <!-- 输入密码 -->
      <van-field v-model="password" type="password" label="密码" />
    </div>

    <van-row type="flex" justify="center">
      <van-button type="primary" @click="onClickLogin"> 登录 </van-button>
    </van-row>
    <van-row type="flex" justify="center">
      <span style="font-size: 11px">
        没有账号?
        <router-link to="/register">注册</router-link>
        {{ this.$store.state.token }}
      </span>
    </van-row>
    <div></div>
  </div>
</template>
<script>
import Vue from "vue";
import { Field, NavBar, Button, Col, Row, Toast } from "vant";
import { userLoginAPI } from "../apis/user.apis";

Vue.use(NavBar);
Vue.use(Field);
Vue.use(Button);
Vue.use(Col);
Vue.use(Row);

export default {
  name: "Login",
  data() {
    return {
      phone: "",
      password: "",
    };
  },

  methods: {
    onClickReturn() {
      this.$router.go(-1);
    },
    onClickLogin() {
      var _this = this;
      this.$store.dispatch("common/setToken", { token: "123" });
      userLoginAPI({ phone: this.phone, password: this.password, login: true })
        .then((resp) => {
          if (resp.data.success) {
            Toast("登陆成功");
            _this.$store.dispatch({ type: "setToken" });
            
            // _this.userToken = res.data.data.body.token;
            // // 将用户token保存到vuex中
            // _this.changeLogin({ Authorization: _this.userToken });
            // this.$router.push("/");
          }
          if (resp.data.code == 1001) {
            // 用户不存在
            Toast("用户不存在");
            this.$router.push("/register?phone=" + _this.phone);
          } else if (resp.data.code == 1004) {
            // 密码错误
            _this.password = "";
            Toast("密码错误");
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>