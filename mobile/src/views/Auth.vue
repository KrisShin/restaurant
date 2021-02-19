<template>
  <div id="auth">
    <van-nav-bar title="恰了木有-认证" @click-left="onClickReturn" left-arrow />
    <van-row type="flex" justify="center">
      <div>邮箱: {{ email }} 验证码已发送</div>
    </van-row>
    <van-row type="flex" justify="center">
      <van-col>
        <van-field
          v-model="captcha"
          type="text"
          maxlength="8"
          label="验证码"
          palceholder="请输入验证码"
          @input="onChangeCaptcha"
        />
      </van-col>
      <van-col>
        <van-button
          size="small"
          round
          type="primary"
          @click="onClickToSubmit"
          :disabled="!enableSubmit"
        >
          提交
        </van-button>
      </van-col>
    </van-row>
  </div>
</template>
<script>
import { userChangeEmailAPI } from "../apis/user.apis.js";
export default {
  name: "Auth",
  data: function () {
    return {
      email: "",
      captcha: "",
      enableSubmit: false,
    };
  },
  created: function () {
    this.email = this.$store.state.common.userInfo.email;
  },
  methods: {
    onClickReturn() {
      this.$router.go(-1);
    },
    onClickToSubmit() {
      userChangeEmailAPI({ email: this.email, captcha: this.captcha });
    },
    onChangeCaptcha() {
      if (this.captcha.length > 0) {
        this.enableSubmit = true;
      } else {
        this.enableSubmit = false;
      }
    },
  },
};
</script>