<template>
  <div class="login">
    <el-container>
      <el-header>恰了木有-管理端</el-header>
      <el-main>
        <el-row>
          <el-col :span="3">
            <el-input v-model="phone" placeholder="请输入手机号"></el-input>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="3">
            <el-input
              v-model="password"
              type="password"
              clearable
              placeholder="请输入密码"
            ></el-input>
          </el-col>
        </el-row>
        <el-row>
          <el-button type="primary" @click="onClickLogin"> 登录 </el-button>/
          <el-button type="primary" plain> 找回密码 </el-button>
        </el-row>
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
    };
  },
  created() {
    this.phone = this.$route.query.phone;
  },
  methods: {
    onClickReturn() {
      this.$router.replace("/");
    },
    onClickLogin() {
      var _this = this;
      userLoginAPI({ phone: this.phone, password: this.password, login: true })
        .then((resp) => {
          if (resp.data.success) {
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
