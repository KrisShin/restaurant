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
              <el-button type="primary" plain> 找回密码 </el-button>
            </el-col>
          </el-row>
        </div>
      </el-main>
    </el-container>
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
          if (resp.data.success) {
            _this.$message("登陆成功");
            _this.$store.dispatch("common/setToken", resp.data.token);
            setTimeout(() => {
              _this.$router.push("/");
            }, 500);
          }
          if (resp.data.code == 1001) {
            // 用户不存在
            _this.$message("用户不存在");
          } else if (resp.data.code == 1004) {
            // 密码错误
            _this.password = "";
            _this.$message("密码错误");
          }
        })
        .catch((err) => {
          console.error(err);
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
.el-row{
  margin: 1%;
  line-height: initial;
}
</style>