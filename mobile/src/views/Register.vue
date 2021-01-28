<template>
  <div id="register">
    <van-nav-bar title="恰了木有-注册" @click-left="onClickReturn" left-arrow />
    <div>
      <van-field
        v-model="user_form.nickname"
        label="昵称"
        error
        required
        clearable
        maxLength="20"
      />
      <van-field
        v-model="user_form.phone"
        type="digit"
        maxLength="11"
        error
        required
        label="手机号"
        clearable
      />
      <van-field
        v-model="user_form.age"
        type="digit"
        error
        required
        :formatter="age_formatter"
        format-trigger="onBlur"
        label="年龄"
      />
      <van-field
        v-model="user_form.email"
        type="email"
        label="邮箱"
        error
        required
        clearable
      />
      <van-field
        v-model="user_form.password"
        type="password"
        error
        required
        label="密码"
        clearable
      />
    </div>
    <van-row type="flex" justify="center">
      <van-button type="primary" @click="onClickRegister"> 注册 </van-button>
    </van-row>
    <van-row type="flex" justify="center">
      <span style="font-size: 11px">
        已有账号?
        <router-link to="/login">登录</router-link>
      </span>
    </van-row>
  </div>
</template>
<script>
import { userRegisterAPI } from "../apis/user.apis";

export default {
  name: "Register",
  data() {
    return {
      user_form: {
        nickname: "",
        phone: "",
        age: 0,
        email: null,
        password: "",
      },
    };
  },
  created() {
    this.phone = this.$route.query.phone;
  },
  methods: {
    age_formatter() {
      console.log(this.user_form.age);
      if (this.user_form.age <= 0) return (this.user_form.age = 0);
      if (this.user_form.age >= 120) return (this.user_form.age = 120);
      return this.user_form.age;
    },
    onClickReturn() {
      this.$router.go(-1);
    },
    onClickRegister() {
      var _this = this;
      userRegisterAPI(this.user_form)
        .then((res) => {
          var data = res.data;
          if (data.success) {
            this.$toast("注册成功");
            setTimeout(_this.$router.push("/login?phone=" + data.phone), 1000);
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>