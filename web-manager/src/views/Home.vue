<!--
 * @Author: windyGu
 * @Date: 2022-01-16 20:18:52
 * @LastEditors: windyGu
 * @LastEditTime: 2022-01-25 00:40:39
 * @FilePath: \restaurant\web-manager\src\views\Home.vue
 * @Description: 
-->
<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import { testGet } from "@/api/requests";

async function fuck() {
  const test = await testGet();
  console.log(test);
}

fuck();

export default {
  name: "Home",
  components: {
    HelloWorld,
  },
};
</script>
