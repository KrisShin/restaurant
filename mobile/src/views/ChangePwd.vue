<template>
  <div id="changePwd">
    <van-nav-bar
      title="恰了木有-修改密码"
      @click-left="onClickReturn"
      left-arrow
    />
    <div>
      <van-row type="flex" justify="space-around">
        <van-col span="17">
          <van-field v-model="email" palceholder="请输入验证码" readonly />
        </van-col>
        <van-col span="5">
          <van-button type="primary" size="small" @click="onClickSendCaptcha">
            发送
          </van-button>
        </van-col>
      </van-row>
      <van-field
        v-model="captcha"
        label="验证码"
        palceholder="请输入验证码"
        required
        clearable
        maxLength="8"
      />
      <van-field
        v-model="oldPassword"
        type="password"
        required
        label="旧密码"
        palceholder="请输入旧密码"
        maxLength="20"
        clearable
      />
      <van-field
        v-model="newPassword"
        type="password"
        required
        label="新密码"
        palceholder="请输入新密码"
        maxLength="20"
        clearable
      />
      <van-field
        v-model="cfmPassword"
        type="password"
        required
        label="新密码"
        palceholder="请确认新密码"
        maxLength="20"
        clearable
      />
    </div>
    <van-row type="flex" justify="center">
      <van-button type="primary" @click="onClickChangePwd">
        提交修改
      </van-button>
    </van-row>
  </div>
</template>
<script>
import { userSendCaptchaAPI, userChangePwdAPI } from "../apis/user.apis";

export default {
  name: "ChangePwd",
  data() {
    return {
      email: "",
      captcha: "",
      oldPassword: "",
      newPassword: "",
      cfmPassword: "",
    };
  },
  created() {
    this.email = this.$store.state.common.userInfo.email;
  },
  methods: {
    onClickReturn() {
      this.$router.replace("/");
    },
    onClickChangePwd() {
      if (
        this.captcha &&
        this.oldPassword &&
        this.newPassword &&
        this.cfmPassword
      ) {
        userChangePwdAPI();
      }
    },
    onClickSendCaptcha() {
      if (this.email) {
        var reg = /^\w+((-\w+)|(\.\w+))*@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/;

        var isEmail = reg.test(this.email);
        if (!isEmail) {
          this.$toast.fail("邮箱格式错误");
        } else {
          var _this = this;
          userSendCaptchaAPI({ email: this.email }).then((resp) => {
            if (resp.data.success) {
              this.$toast.success("发送成功");
              // _this.$router.push("/auth?email=" + this.userInfo.email);
            } else if (resp.data.code === 1006) {
              _this.$notify({
                message: "请勿频繁申请验证邮件",
                type: "warning",
                duration: 800,
              });
            }
          });
        }
      } else {
        this.$toast("邮箱不能为空");
      }
    },
  },
};
</script>