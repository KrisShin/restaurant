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
  created() {
    if (sessionStorage.getItem("store")) {
      this.$store.replaceState(
        Object.assign({}, JSON.parse(sessionStorage.getItem("store")))
      );
    }

    window.addEventListener("beforeunload", () => {
      sessionStorage.setItem("store", JSON.stringify(this.$store.state));
    });
  },
};
</script>
