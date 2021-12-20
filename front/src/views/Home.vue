<template>
  <div class="home">
    <el-container>
      <el-aside style="width: auto"><SideNavBar /></el-aside>
      <el-container>
        <el-header>恰了木有-管理端</el-header>
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

export default {
  name: "Home",
  components: {
    SideNavBar,
  },
  data() {
    return {
      dishes: null,
      page: 1,
    };
  },
  created: function() {
    this.loadDishList();
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
              console.log(this.dishes);
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
</style>