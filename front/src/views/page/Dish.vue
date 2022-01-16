<template>
  <el-main>
    <el-row type="flex" justify="space-between">
      <el-col :span="5">
        <el-input placeholder="请输入内容" v-model="searchDish">
          <el-button slot="append" icon="el-icon-search"></el-button>
        </el-input>
      </el-col>
      <el-col :span="3"><el-button type="primary">新增菜品</el-button></el-col>
    </el-row>
    <el-table :data="dishes" border>
      <el-table-column fixed prop="name" label="菜品名称" width="150">
      </el-table-column>
      <el-table-column label="图片" width="200">
        <template slot-scope="scope">
          <img class="dishImg" :src="scope.row.index_img" alt="" />
        </template>
      </el-table-column>
      <el-table-column prop="price" label="单价" width="120"> </el-table-column>
      <el-table-column prop="amount" label="销量" width="120">
      </el-table-column>
      <el-table-column prop="description" label="简介" width="600">
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
    <el-pagination
      layout="sizes, prev, pager, next, total"
      :total="total"
      :current-page="page"
      :page-size="pageSize"
    >
    </el-pagination>
  </el-main>
</template>

<script>
// @ is an alias to /src
import { dishListAPI } from "@/apis/dish.apis";

export default {
  name: "Dish",
  data() {
    return {
      dishes: Array(),
      page: 1,
      pageSize: 5,
      total: 0,
      searchDish: "",
    };
  },
  created() {
    this.loadDishList();
  },
  methods: {
    loadDishList() {
      dishListAPI({ page: this.page, pageSize: this.pageSize }).then((resp) => {
        if (resp.data.code === 200) {
          if (resp.data.data) {
            resp.data.data.forEach((dish) => {
              this.dishes.push(dish);
            });
            this.page = resp.data.data.page;
            this.pageSize = resp.data.data.pageSize;
            this.total = resp.data.data.total;
          }
        }
        this.loading = false;
        this.finished = true;
      });
    },
    onClickDeleteDish() {
      console.log("delete");
    },
  },
};
</script>
<style>
.dishImg {
  max-width: 180px;
}
</style>