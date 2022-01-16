<template>
  <div class="home">
    <el-container style="height: 100%">
      <el-aside style="width: auto"><SideNavBar /></el-aside>
      <el-container>
        <el-header>
          <el-row type="flex" justify="space-between" style="margin: 0">
            <el-col :span="6">恰了木有-管理端</el-col>
            <el-col :span="6">
              <div @click="onClickAvatar">
                <el-avatar size="large" :src="userInfo.avatar"></el-avatar>
                {{ userInfo.nickname }}
              </div>
            </el-col>
          </el-row>
        </el-header>
        <router-view name="Views" />
      </el-container>
    </el-container>
  </div>
</template>

<script>
// @ is an alias to /src
import SideNavBar from "@/components/SideNavBar.vue";
import { userInfoAPI } from "@/apis/user.apis";

export default {
  name: "Home",
  components: {
    SideNavBar,
  },
  data() {
    return {
      dishes: Array(),
      page: 1,
      userInfo: null,
    };
  },
  created() {
    this.userInfo = this.$store.state.userInfo;
    this.defaultAvatar = this.$BASE_API + "/static/avatar/default.jpg";

    if (!this.userInfo) {
      userInfoAPI().then((resp) => {
        if (resp.data.code === 200) {
          var userInfo = resp.data.data;
          this.$store.dispatch("setUserInfo", userInfo);
          this.userInfo = userInfo;
        }
        this.$router.replace("/dish");
      });
    } else {
      this.$router.replace("/dish");
    }
  },
  methods: {
    onClickAvatar() {
      console.log("fuck");
    },
  },
};
</script>
<style>
.el-header {
  color: black;
  padding: 10px 0 0 10%;
  background: rgb(114, 222, 255);
}
.el-main {
  background: whitesmoke;
  padding: 0;
}
.home {
  height: 100%;
}
.img-avatar {
  width: 40px;
}
</style>