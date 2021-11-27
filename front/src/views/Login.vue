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
              >发送验证码</el-button
            >
          </el-input>
        </el-form-item>
        <el-form-item label="活动区域" :label-width="formLabelWidth">
          <el-select v-model="form.region" placeholder="请选择活动区域">
            <el-option label="区域一" value="shanghai"></el-option>
            <el-option label="区域二" value="beijing"></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogFormVisible = false"
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
  userChangePwdAPI,
} from "../apis/user.apis";

export default {
  name: "Login",
  data() {
    return {
      phone: "",
      password: "",
      disableSumbmit: true,
      dialogFormVisible: true,
      form: {
        email: "",
        name: "",
        region: "",
        date1: "",
        date2: "",
        delivery: false,
        type: [],
        resource: "",
        desc: "",
      },
      formLabelWidth: "70px",
    };
  },
  created() {
    this.phone = this.$route.query.phone;
  },
  methods: {
    inputCheck() {
      if (this.phone && this.password) this.disableSumbmit = false;
      else this.disableSumbmit = true;
    },
    onClickReturn() {
      this.$router.replace("/");
    },
    onClickLogin() {
      var _this = this;
      userLoginAPI({ phone: this.phone, password: this.password, login: true })
        .then((resp) => {
          if (resp.data.code === 200) {
            _this.$message.success("登陆成功");
            _this.$store.dispatch("common/setToken", resp.data.token);
            _this.$router.push("/home");
          }
          if (resp.data.code == 1001) {
            // 用户不存在
            _this.$message.error("用户不存在");
          } else if (resp.data.code == 1004) {
            // 密码错误
            _this.password = "";
            _this.$message.error("密码错误");
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
    onClickResetPwdDialog() {
      this.dialogFormVisible = true;
    },
    onClickSendCaptcha() {
      userSendCaptchaAPI({ email: this.form.email });
    },
    onClickResetPwd() {
      userChangePwdAPI(this.form);
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