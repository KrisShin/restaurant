<template>
  <div id="auth">
    <van-nav-bar
      title="恰了木有-认证"
      @click-left="onClickReturn"
      left-arrow
      fixed
      placeholder
    />
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
    this.email = this.$route.query.email;
  },
  methods: {
    onClickReturn() {
      this.$router.go(-1);
    },
    onClickToSubmit() {
      const _this = this;
      userChangeEmailAPI({ email: this.email, captcha: this.captcha })
        .then((resp) => {
          if (resp.data.success) {
            this.$toast("验证成功");
            var userInfo = _this.$store.state.common.userInfo;
            userInfo.email = _this.email;
            userInfo.is_email_active = true;
            _this.$store.dispatch("common/setUserInfo", userInfo);
            setTimeout(() => {
              _this.$router.push("/profile");
            }, 500);
          } else if (resp.data.code === 1009) {
            this.$toast("验证码已过期");
            this.$router("/profile");
          } else if (resp.data.code === 1008) {
            this.$toast("验证错误");
          } else if (resp.data.code === 1002) {
            this.$toast("邮箱已注册");
            this.$router("/profile");
          } else {
            this.$toast("未知错误");
            this.$router("/profile");
          }
        })
        .catch((err) => {
          console.error(err);
        });
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