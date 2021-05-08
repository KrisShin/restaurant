<template>
  <div id="register">
    <van-nav-bar
      title="恰了木有-注册"
      @click-left="onClickReturn"
      left-arrow
      fixed
      placeholder
    />
    <div>
      <van-field
        v-model="user_form.nickname"
        label="昵称"
        placeholder="请输入昵称"
        required
        clearable
        maxLength="20"
      />
      <van-field
        v-model="user_form.phone"
        type="digit"
        maxLength="11"
        placeholder="请输入手机号"
        required
        label="手机号"
        clearable
      />
      <van-field
        v-model="user_form.age"
        type="digit"
        required
        placeholder="请输入年龄"
        :formatter="age_formatter"
        format-trigger="onBlur"
        label="年龄"
      />
      <van-radio-group
        v-model="user_form.gender"
        direction="horizontal"
        style="padding: 10px 10px 10px 7px; font-size: 14px"
        class="van-hairline--bottom"
      >
        <span style="color: red">*</span>
        <span style="margin: 0 70px 0 3px; color: #646566">性别</span>
        <van-radio name=''>女</van-radio>
        <van-radio name='1'>男</van-radio>
      </van-radio-group>

      <van-field
        v-model="user_form.email"
        type="email"
        label="邮箱"
        placeholder="请输入邮箱"
        required
        clearable
      />
      <van-field
        v-model="user_form.password"
        type="password"
        required
        label="密码"
        placeholder="请输入密码"
        clearable
      />
    </div>
    <van-row type="flex" justify="center">
      <van-button type="primary" @click="onClickRegister"> 注册 </van-button>
    </van-row>
    <van-row type="flex" justify="center">
      <span style="font-size: 11px; margin-top: 20px">
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
        gender: '',
        age: 0,
        email: null,
        password: "",
      },
    };
  },
  created() {
    this.user_form.phone = this.$route.query.phone;
  },
  methods: {
    age_formatter() {
      if (this.user_form.age <= 0) return (this.user_form.age = 0);
      if (this.user_form.age >= 120) return (this.user_form.age = 120);
      return this.user_form.age;
    },
    onClickReturn() {
      this.$router.replace("/");
    },
    onClickRegister() {
      var _this = this;
      userRegisterAPI(this.user_form)
        .then((res) => {
          var data = res.data;
          if (data.success) {
            this.$toast.success("注册成功");
            setTimeout(_this.$router.push("/login?phone=" + _this.user_form.phone), 1000);
          } else if (data.code == 1002) {
            this.$toast.fail("手机号已注册");
            setTimeout(_this.$router.push("/login?phone=" + _this.user_form.phone), 1000);
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>