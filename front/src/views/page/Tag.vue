<template>
  <el-main>
    <el-row type="flex" justify="space-between">
      <el-col :span="5">
        <el-input placeholder="请输入标签名称搜索" v-model="searchTag">
          <el-button
            slot="append"
            icon="el-icon-search"
            @click="onClickSearchTag"
          ></el-button>
        </el-input>
      </el-col>
      <el-col :span="3"
        ><el-button type="primary" @click="onClickAddTag('add')"
          >新增菜品</el-button
        ></el-col
      >
    </el-row>
    <el-table :data="allTags" border>
      <el-table-column fixed sortable prop="name" label="标签名称" width="250">
        <template slot-scope="scope">
          <el-input
            v-if="scope.row.type == 'add'"
            v-model="scope.row.name"
          ></el-input>
          <span v-else>{{ scope.row.name }}</span>
        </template>
      </el-table-column>
      <el-table-column
        fixed
        sortable
        prop="weight"
        label="标签权重"
        width="250"
      >
      </el-table-column>
      <el-table-column
        fixed
        sortable
        prop="create_time"
        label="创建时间"
        width="250"
      >
      </el-table-column>
      <el-table-column
        fixed
        sortable
        prop="update_time"
        label="编辑时间"
        width="250"
      >
      </el-table-column>
      <el-table-column label="操作" width="100">
        <template slot-scope="scope">
          <el-button
            v-if="scope.row.type == 'add'"
            @click="onClickSubmitTag(scope.row)"
            type="success"
            size="mini"
            >新增</el-button
          >
          <el-button
            v-else
            @click="onClickDeleteTag(scope.row)"
            type="text"
            size="small"
            style="color: red"
            >删除</el-button
          >
        </template>
      </el-table-column>
    </el-table>
  </el-main>
</template>

<script>
// @ is an alias to /src
import { tagListAPI, tagAddAPI } from "@/apis/dish.apis";

export default {
  name: "Tag",
  data() {
    return {
      allTags: Array(),
      page: 1,
      pageSize: 5,
      total: 0,
      searchTag: "",
    };
  },
  created() {
    this.loadTagList();
  },
  onmounted() {
    this.loadTagList();
  },
  methods: {
    loadTagList() {
      tagListAPI({ params: { search: this.searchTag } }).then((resp) => {
        if (resp.data.code == 200) {
          this.allTags = resp.data.data.tags;
        }
      });
    },
    onClickAddTag() {
      this.allTags.unshift({
        name: "",
        weight: 1,
        type: "add",
      });
    },
    onClickSearchTag() {
      this.loadTagList();
    },
    onClickSubmitTag(tag) {
      tagAddAPI({ name: tag.name }).then((resp) => {
        if (resp.data.code == 200) {
          this.$message.success("添加成功");
          this.search = "";
          this.loadTagList();
        }
      });
    },
    onClickDeleteTag() {},
  },
};
</script>
<style>
.dishImg {
  max-width: 180px;
}
</style>