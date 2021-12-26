<template>
  <div class="login">
    <el-container>
      <el-header>恰了木有-管理端</el-header>
      <el-main class="mainbox">
        <div class="loginFormBox">
          <el-row type="flex" justify="center">
            <el-col :span="3">
              <el-input
                v-model="phone"
                placeholder="请输入手机号"
                @input="inputCheck"
                maxlength="11"
                clearable
              ></el-input>
            </el-col>
          </el-row>
          <el-row type="flex" justify="center">
            <el-col :span="3">
              <el-input
                v-model="password"
                type="password"
                clearable
                placeholder="请输入密码"
                @input="inputCheck"
              ></el-input>
            </el-col>
          </el-row>
          <el-row type="flex" justify="center">
            <el-col>
              <el-button
                type="primary"
                @click="onClickLogin"
                :disabled="disableSumbmit"
              >
                登录 </el-button
              >/
              <el-button type="primary" plain @click="onClickResetPwdDialog">
                找回密码
              </el-button>
            </el-col>
          </el-row>
        </div>
      </el-main>
    </el-container>
    <el-dialog title="找回密码" :visible.sync="dialogFormVisible" width="400px">
      <el-form :model="form">
        <el-form-item label="邮箱" :label-width="formLabelWidth">
          <el-input v-model="form.email" autocomplete="off">
            <el-button slot="append" @click="onClickSendCaptcha"
              >发送验证码
            </el-button>
          </el-input>
        </el-form-item>
        <el-form-item label="验证码" :label-width="formLabelWidth">
          <el-input v-model="form.captcha" autocomplete="off" />
        </el-form-item>
        <el-form-item label="新密码" :label-width="formLabelWidth">
          <el-input
            type="password"
            v-model="form.new_password"
            @input="pwdCheck"
            autocomplete="off"
          />
        </el-form-item>
        <el-form-item label="确认密码" :label-width="formLabelWidth">
          <el-input
            type="password"
            v-model="form.cfm_password"
            @input="pwdCheck"
            autocomplete="off"
          />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button
          type="primary"
          :disabled="disableChangePwd"
          @click="onClickResetPwd"
          >确 定</el-button
        >
      </div>
    </el-dialog>
  </div>
</template>

<script>
import {
  userLoginAPI,
  userSendCaptchaAPI,
  userResetPwdAPI,
} from "../apis/user.apis";

export default {
  name: "Login",
  data() {
    return {
      phone: "13433334444",
      password: "wer4",
      disableSumbmit: true,
      disableChangePwd: true,
      dialogFormVisible: false,
      form: {
        email: "",
        captcha: "",
        new_password: "",
        cfm_password: "",
      },
      formLabelWidth: "70px",
    };
  },
  created() {
    // this.phone = this.$route.query.phone;
  },
  methods: {
    inputCheck() {
      if (this.phone && this.password) this.disableSumbmit = false;
      else this.disableSumbmit = true;
    },
    pwdCheck() {
      if (this.form.new_password === this.form.cfm_password)
        this.disableChangePwd = false;
      else this.disableChangePwd = true;
    },
    onClickReturn() {
      this.$router.replace("/");
    },
    onClickLogin() {
      userLoginAPI({
        phone: this.phone,
        password: this.password,
        login: true,
      }).then((resp) => {
        if (resp.data.code === 200) {
          this.$message.success("登陆成功");
          this.$store.dispatch("common/setToken", resp.data.token);
          this.$router.push("/home");
        }
      });
    },
    onClickResetPwdDialog() {
      this.dialogFormVisible = true;
    },
    onClickSendCaptcha() {
      userSendCaptchaAPI({ email: this.form.email }).then((resp) => {
        const { code } = resp.data;
        if (code === 200) {
          this.$message.success("邮件发送成功");
        }
      });
    },
    onClickResetPwd() {
      userResetPwdAPI(this.form).then((resp) => {
        const { code } = resp.data;
        if (code === 200) {
          this.$message.success(resp.data.msg);
          this.form = {
            email: "",
            captcha: "",
            new_password: "",
            cfm_password: "",
          };
          this.dialogFormVisible = false;
        }
      });
    },
  },
};
</script>
<style>
.el-main {
  padding: 10%;
}
.el-header {
  color: aliceblue;
  font-size: 30px;
}
.el-row {
  margin: 1%;
  line-height: initial;
}
</style>