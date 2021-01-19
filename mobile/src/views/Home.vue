<template>
  <div id="home">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    {{ a }}
    <div v-if="a">
      <router-link to="/login">login</router-link> /
      <router-link to="/register">register</router-link>
      <Button @click="hello">123</Button>
    </div>
    <div v-else>Welcome</div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import { Button } from "vant";

export default {
  name: "Home",
  data: function () {
    return {
      a: true,
    };
  },
  components: {
    // HelloWorld
    Button,
  },
  methods: {
    hello: function () {
      this.a = !this.a;
    },
  },
};
</script>
