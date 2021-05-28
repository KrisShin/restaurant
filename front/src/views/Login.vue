<template>
  <div class="login">
    <el-container>
      <el-header>恰了木有-管理端</el-header>
      <el-main>
        <el-row>
          <el-input v-model="username" placeholder="请输入帐号"></el-input>
        </el-row>
        <el-row>
          <el-col span="3">
            <el-input
              v-model="password"
              type="password"
              clearable
              placeholder="请输入密码"
            ></el-input>
          </el-col>
        </el-row>
        <el-row>
          <el-button type="primary"> 登录 </el-button>/
          <el-button type="primary" plain> 找回密码 </el-button>
        </el-row>
      </el-main>
      <el-footer>Footer</el-footer>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
    };
  },
};
</script>
