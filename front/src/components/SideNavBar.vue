<template>
  <el-menu
    :default-active="chosenItem"
    class="el-menu-vertical-demo"
    @open="handleOpen"
    @close="handleClose"
    @select="handleCollapse"
    :collapse="isCollapse"
  >
    <el-submenu index="1">
      <template slot="title">
        <i class="el-icon-location"></i>
        <span slot="title">菜单管理</span>
      </template>
      <el-menu-item-group>
        <el-menu-item index="1-1">编辑菜单</el-menu-item>
        <el-menu-item index="1-2">折扣管理</el-menu-item>
      </el-menu-item-group>
    </el-submenu>
    <el-submenu index="2">
      <template slot="title">
        <i class="el-icon-menu"></i>
        <span slot="title">订单管理</span>
      </template>
      <el-menu-item-group>
        <el-menu-item index="2-1">订单处理</el-menu-item>
        <el-menu-item index="2-2">退款处理</el-menu-item>
      </el-menu-item-group>
    </el-submenu>
    <el-submenu index="3">
      <template slot="title">
        <i class="el-icon-document"></i>
        <span slot="title">用户管理</span>
      </template>
      <el-menu-item-group>
        <el-menu-item index="3-1">用户列表</el-menu-item>
        <el-menu-item index="3-2">会员管理</el-menu-item>
      </el-menu-item-group>
    </el-submenu>
    <el-menu-item index="10" class="menu-button-more">
      <i class="el-icon-more"></i>
    </el-menu-item>
  </el-menu>
</template>

<script>
export default {
  name: "SideNavBar",
  props: {},
  data() {
    return {
      chosenItem: "1",
      isCollapse: false,
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    handleCollapse(key) {
      console.log(key);
      if (key === "10") this.isCollapse = !this.isCollapse;
      else this.chosenItem = key;
    },
  },
};
</script>


<style>
.el-menu-vertical-demo {
  height: 100%;
}
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
}
.menu-button-more {
  position: absolute;
  bottom: 3%;
}
</style>