<template>
  <div id="login">
    <van-nav-bar
      title="恰了木有-登录"
      @click-left="onClickReturn"
      left-arrow
      fixed
      placeholder
    />
    <div>
      <!-- 输入手机号，调起手机号键盘 -->
      <van-field
        v-model="phone"
        type="text"
        maxlength="11"
        label="手机号"
        placeholder="请输入手机号"
        @change="inputCheck"
      />
      <!-- 输入密码 -->
      <van-field
        v-model="password"
        type="password"
        label="密码"
        placeholder="请输入密码"
        @change="inputCheck"
      />
    </div>

    <van-row type="flex" justify="center">
      <van-button
        type="primary"
        @click="onClickLogin"
        :disabled="disableSumbmit"
      >
        登录
      </van-button>
    </van-row>
    <van-row type="flex" justify="center">
      <span style="font-size: 11px; margin-top: 20px">
        没有账号?
        <router-link to="/register">注册</router-link>
      </span>
    </van-row>
    <div></div>
  </div>
</template>
<script>
import { userLoginAPI } from "../apis/user.apis";

export default {
  name: "Login",
  data() {
    return {
      phone: "",
      password: "",
      disableSumbmit: true,
    };
  },
  created() {
    this.phone = this.$route.query.phone;
  },
  methods: {
    onClickReturn() {
      this.$router.replace("/");
    },
    inputCheck() {
      if (this.phone && this.password) this.disableSumbmit = false;
      else this.disableSumbmit = true;
    },
    onClickLogin() {
      var _this = this;
      userLoginAPI({ phone: this.phone, password: this.password, login: true })
        .then((resp) => {
          if (resp.data.code === 200) {
            this.$toast("登陆成功");
            _this.$store.dispatch("common/setToken", resp.data.token);
            setTimeout(() => {
              _this.$router.push("/");
            }, 500);
          }
          if (resp.data.code == 1001) {
            // 用户不存在
            this.$toast("用户不存在");
            _this.$router.push("/register?phone=" + _this.phone);
          } else if (resp.data.code == 1004) {
            // 密码错误
            _this.password = "";
            this.$toast("密码错误");
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>