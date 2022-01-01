<template>
  <div class="home">
    <el-container>
      <el-aside style="width: auto"><SideNavBar /></el-aside>
      <el-container>
        <el-header>
          <el-row type="flex" justify="space-between" style="margin: 0">
            <el-col :span="6">恰了木有-管理端</el-col>
            <el-col :span="6">
              <div @click="onClickAvatar">
                <el-avatar size="large" :src="defaultAvatar"></el-avatar>
                {{ userInfo.nickname }}
              </div>
            </el-col>
          </el-row>
        </el-header>
        <el-main>
          <el-table :data="dishes" border>
            <el-table-column fixed prop="date" label="日期" width="150">
            </el-table-column>
            <el-table-column prop="name" label="姓名" width="120">
            </el-table-column>
            <el-table-column prop="province" label="省份" width="120">
            </el-table-column>
            <el-table-column prop="city" label="市区" width="120">
            </el-table-column>
            <el-table-column prop="address" label="地址" width="300">
            </el-table-column>
            <el-table-column prop="zip" label="邮编" width="120">
            </el-table-column>
            <el-table-column fixed="right" label="操作" width="100">
              <template slot-scope="scope">
                <el-button
                  @click="handleClick(scope.row)"
                  type="text"
                  size="small"
                  >查看</el-button
                >
                <el-button type="text" size="small">编辑</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
// @ is an alias to /src
import SideNavBar from "@/components/SideNavBar.vue";
import { dishListAPI } from "../apis/dish.apis";
import { userInfoAPI } from "../apis/user.apis";

export default {
  name: "Home",
  components: {
    SideNavBar,
  },
  data() {
    return {
      dishes: null,
      page: 1,
      userInfo: {},
    };
  },
  created() {
    this.userInfo = this.$store.state.common.userInfo;
    this.defaultAvatar = this.$BASE_API + "/static/avatar/default.jpg";
    this.loadDishList();
    this.isLogin = this.$store.state.common.isLogin;

    if (this.isLogin && !this.userInfo) {
      userInfoAPI()
        .then((resp) => {
          if (resp.data.code === 200) {
            var userInfo = resp.data.data;
            this.$store.dispatch("common/setUserInfo", userInfo);
            this.userInfo = userInfo;
          }
        })
        .catch((err) => {
          console.error(err);
        });
    }
  },
  methods: {
    loadDishList() {
      dishListAPI({ page: this.page })
        .then((resp) => {
          if (resp.data.code === 200) {
            if (resp.data.data) {
              resp.data.data.forEach((dish) => {
                this.dishes.push(dish);
              });
              this.page += resp.data.data.length;
              if (resp.data.data.length < 5) {
                this.finished = true;
              }
            } else {
              this.finished = true;
            }
          }
          this.loading = false;
          this.finished = true;
        })
        .catch((err) => {
          console.error(err);
        });
    },
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