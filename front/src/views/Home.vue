<template>
  <div class="home">
    <SideNavBar />
  </div>
</template>

<script>
// @ is an alias to /src
import SideNavBar from "@/components/SideNavBar.vue";

export default {
  name: "Home",
  components: {
    SideNavBar,
  },
};
</script>
<style>
.el-header,
.el-footer {
  background-color: #1d79f0;
  color: #333;
  text-align: center;
  line-height: 60px;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 160px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
.home{
  height: 100%;
}
</style>