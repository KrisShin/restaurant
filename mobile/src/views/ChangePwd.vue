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
        :error-message="cmfErrMsg"
        @input="checkCfmPassword"
        maxLength="20"
        clearable
      />
    </div>
    <van-row type="flex" justify="center">
      <van-button
        type="primary"
        @click="onClickChangePwd"
        :disabled="isSubmitAllowed"
      >
        提交修改
      </van-button>
    </van-row>
  </div>
</template>
<script>
import {
  userSendCaptchaAPI,
  userChangePwdAPI,
  userLogoutAPI,
} from "../apis/user.apis";

export default {
  name: "ChangePwd",
  data() {
    return {
      email: null,
      captcha: null,
      oldPassword: null,
      newPassword: null,
      cfmPassword: null,
      isSubmitAllowed: true,
      cmfErrMsg: "",
    };
  },
  created() {
    this.email = this.$store.state.common.userInfo.email;
  },
  methods: {
    onClickReturn() {
      this.$router.go("-1");
    },
    onClickChangePwd() {
      if (
        this.captcha &&
        this.oldPassword &&
        this.newPassword &&
        this.cfmPassword
      ) {
        userChangePwdAPI({
          captcha: this.captcha,
          old_password: this.oldPassword,
          new_password: this.newPassword,
          cfm_password: this.cfmPassword,
        }).then((resp) => {
          console.log(resp.data.code == 1008);
          if (resp.data.success) {
            this.$notify({
              message: "密码修改成功, 请重新登录",
              type: "success",
              duration: 800,
            });
            userLogoutAPI().then((resp) => {
              if (resp.data.success) {
                this.$notify({
                  message: "退出登录",
                  type: "success",
                  duration: 1000,
                });
              }
              this.$store.dispatch("common/setToken", null);
              this.$store.dispatch("common/setUserInfo", null);
              this.$router.replace("/");
            });
          } else if (resp.data.code == 10012) {
            this.isSubmitAllowed = true;
            this.cmfErrMsg = "与新密码不一致";
          } else if (resp.data.code == 1007) {
            this.$toast.fail("新密码不能与原密码相同");
          } else if (resp.data.code == 1009) {
            this.$toast.fail("验证码过期, 请重新发送");
          } else if (resp.data.code == 1004) {
            this.$toast.fail("原密码错误");
          } else if (resp.data.code == 1008) {
            this.$toast.fail("验证码错误");
          }
        });
      }
    },
    checkCfmPassword() {
      if (!this.newPassword) {
        console.log(1);
        this.isSubmitAllowed = true;
        return;
      }
      if (!this.cfmPassword) {
        console.log(2);
        this.isSubmitAllowed = true;
        return;
      }
      if (this.newPassword !== this.cfmPassword) {
        this.isSubmitAllowed = true;
        this.cmfErrMsg = "与新密码不一致";
      } else {
        this.isSubmitAllowed = false;
        this.cmfErrMsg = "";
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