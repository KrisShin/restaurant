<template>
  <div id="Login">
    <input placeholder="手机号" />
    <input type="password" placeholder="密码" />
    <div>
      <button>登录</button
      ><span>没有账号?<router-link to="/register">注册</router-link></span>
    </div>
  </div>
</template>
<script>
export default {
  name: "Login",
};
</script>