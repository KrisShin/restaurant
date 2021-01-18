<template>
  <div id="home">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <router-link to="/login">login</router-link> / 
    <router-link to="/register">register</router-link>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: "Home",
  components: {
    // HelloWorld
  },
};
</script>
