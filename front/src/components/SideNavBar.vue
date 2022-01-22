<template>
  <el-menu
    :default-active="chosenItem"
    class="el-menu-vertical-demo"
    @select="handleCollapse"
    :collapse="isCollapse"
  >
    <el-submenu index="1">
      <template slot="title">
        <i class="el-icon-location"></i>
        <span slot="title">菜单管理</span>
      </template>
      <el-menu-item-group>
        <el-menu-item index="/dish">编辑菜单</el-menu-item>
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
    <el-menu-item index="/tag">标签管理</el-menu-item>
    <!-- <el-submenu index="4">
      <template slot="title">
        <i class="el-icon-document"></i>
        <span slot="title">标签管理</span>
      </template>
      <el-menu-item-group>
        <el-menu-item index="3-2">会员管理</el-menu-item>
      </el-menu-item-group>
    </el-submenu> -->
    <el-menu-item index="collapse" class="menu-button-more">
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
    handleCollapse(key) {
      if (key === "collapse") this.isCollapse = !this.isCollapse;
      else this.$router.push(key)
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