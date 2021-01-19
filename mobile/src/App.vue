<template>
  <div id="app">
    <router-view>
      <Home />
    </router-view>
  </div>
</template>

<script>
import Home from "./views/Home.vue";

export default {
  name: "App",
  component: [Home],
};
</script>
