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
                <el-avatar size="large" :src="userInfo.avatar"></el-avatar>
                {{ userInfo.nickname }}
              </div>
            </el-col>
          </el-row>
        </el-header>
        <el-main>
          <el-table :data="dishes" border>
            <el-table-column fixed prop="name" label="菜品名称" width="150">
            </el-table-column>
            <el-table-column label="图片" width="200">
              <template slot-scope="scope">
                <img class="dishImg" :src="scope.row.index_img" alt="" />
              </template>
            </el-table-column>
            <el-table-column prop="price" label="单价" width="120">
            </el-table-column>
            <el-table-column prop="amount" label="销量" width="120">
            </el-table-column>
            <el-table-column prop="description" label="简介" width="500">
            </el-table-column>
            <el-table-column prop="discount_desc" label="折扣" width="120">
            </el-table-column>
            <el-table-column prop="tags" label="标签" width="120">
              <template slot-scope="scope">
                <el-tag
                  v-for="(tag, index) in scope.row.tags"
                  :key="index"
                  effect="plain"
                  size="mini"
                  >{{ tag.name }}</el-tag
                >
              </template>
            </el-table-column>
            <el-table-column label="操作" width="100">
              <template slot-scope="scope">
                <el-button type="text" size="small">编辑</el-button>
                <el-button
                  @click="onClickDeleteDish(scope.row)"
                  type="text"
                  size="small"
                  style="color: red"
                  >删除</el-button
                >
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
        this.loadDishList();
      });
    } else {
      this.userInfo = this.$store.state.userInfo;
      this.loadDishList();
    }
  },
  methods: {
    loadDishList() {
      dishListAPI({ page: this.page }).then((resp) => {
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
      });
    },
    onClickAvatar() {
      console.log("fuck");
    },
    onClickDeleteDish() {
      console.log("delete");
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
.dishImg {
  max-width: 180px;
}
</style>