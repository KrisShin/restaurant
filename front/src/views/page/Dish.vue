<template>
  <el-main>
    <el-row type="flex" justify="space-between">
      <el-col :span="5">
        <el-input placeholder="请输入菜品名称搜索" v-model="searchDish">
          <el-button
            slot="append"
            icon="el-icon-search"
            @click="onClickSearchDish"
          ></el-button>
        </el-input>
      </el-col>
      <el-col :span="3"
        ><el-button type="primary" @click="onClickEditDish('add')"
          >新增菜品</el-button
        ></el-col
      >
    </el-row>
    <el-table :data="dishes" border>
      <el-table-column fixed prop="name" label="菜品名称" width="150">
      </el-table-column>
      <el-table-column label="图片" width="200">
        <template slot-scope="scope">
          <img class="dishImg" :src="scope.row.index_img" alt="" />
        </template>
      </el-table-column>
      <el-table-column label="单价" width="120">
        <template slot-scope="scope">
          {{ scope.row.price.toFixed(2) }}
        </template>
      </el-table-column>
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
          <el-button type="text" size="small" @click="onClickEditDish('edit')"
            >编辑</el-button
          >
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
    <el-dialog
      :title="dialogTitle"
      :visible.sync="showDishEditDialog"
      width="30%"
    >
      <el-form ref="form" :model="dishForm" label-width="80px">
        <el-form-item label="菜品名称">
          <el-input v-model="dishForm.name"></el-input>
        </el-form-item>
        <el-form-item label="菜品单价">
          <el-input type="number" v-model="dishForm.price"></el-input>
        </el-form-item>
        <el-form-item label="菜品简介">
          <el-input
            type="textarea"
            :rows="2"
            v-model="dishForm.description"
          ></el-input>
        </el-form-item>

        <el-form-item label="菜品折扣">
          <el-select v-model="dishForm.discountId" placeholder="请选择活动区域">
            <el-option label="无折扣" value="0"></el-option>
            <el-option label="打折" value="1"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="打折信息" v-if="dishForm.discountId != '0'">
          <el-row>
            <el-col>
              <el-input
                type="number"
                v-model="dishForm.discount"
                placeholder="0.1-1折"
              ></el-input>
            </el-col>
            <el-col>
              <el-input
                type="number"
                v-model="dishForm.discount_desc"
                placeholder="打折宣传信息"
              ></el-input>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="11">
              <el-date-picker
                type="date"
                placeholder="开始日期"
                v-model="dishForm.discountDate1"
                style="width: 100%"
              ></el-date-picker>
            </el-col>
            <el-col class="line" :span="2">-</el-col>
            <el-col :span="11">
              <el-date-picker
                placeholder="结束日期"
                v-model="dishForm.discountDate2"
                style="width: 100%"
              ></el-date-picker>
            </el-col>
          </el-row>
        </el-form-item>
        <el-form-item label="菜品标签">
          <el-tag
            v-for="(tag, index) in allTags"
            :key="index"
            :effect="tag.is_chosen ? 'dark' : 'plain'"
            @click="onClickTaggleTag(tag, index)"
            size="mini"
            >{{ tag.name }}</el-tag
          >
        </el-form-item>
        <el-form-item label="菜品图片">
          <el-upload
            class="upload-demo"
            ref="upload"
            :action="host + '/merchant/dish/image/upload/'"
            :on-remove="handleRemove"
            :file-list="dishForm.images"
            :auto-upload="false"
            :multiple="true"
            name="images"
          >
            <el-button slot="trigger" size="small" type="primary">
              选取文件
            </el-button>
            <el-button
              style="margin-left: 10px"
              size="small"
              type="success"
              @click="submitUpload"
              >上传到服务器
            </el-button>
          </el-upload>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onClickSubmitDish"
            >立即创建</el-button
          >
          <el-button>取消</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </el-main>
</template>

<script>
// @ is an alias to /src
import { dishListAPI, tagListAPI } from "@/apis/dish.apis";

export default {
  name: "Dish",
  data() {
    return {
      dishes: Array(),
      page: 1,
      pageSize: 5,
      total: 0,
      showDishEditDialog: false,
      editType: "add",
      searchDish: null,
      dishForm: {
        name: "红烧肉",
        price: 68.88,
        description: "非常红的红烧肉",
        discountId: "0",
        discountDate: [],
        tags: [],
        images: [],
        // name: "",
        // price: 0,
        // description: "",
        // discountId: "0",
        // discountDate: [],
        // tags: [],
        // images: [],
      },
      dialogTitle: "新增菜品",
      allTags: [],
      allDiscount: [],
      host: "",
    };
  },
  created() {
    this.host = this.$BASE_API;
    console.log(this.host)
    this.loadDishList();
  },
  onmounted() {
    this.loadDishList();
  },
  methods: {
    loadDishList() {
      dishListAPI({
        page: this.page,
        pageSize: this.pageSize,
        search: this.searchDish,
      }).then((resp) => {
        if (resp.data.code === 200) {
          this.dishes = resp.data.data;
          this.page = resp.data.page;
          this.total = resp.data.total;
        }
        this.searchDish = null;
      });
    },
    onClickDeleteDish() {
      console.log("delete");
    },
    onClickEditDish(type) {
      this.editType = type;
      this.dialogTitle = type === "add" ? "新增菜品" : "编辑菜品";
      if (!this.showDishEditDialog && type === "add") {
        // this.dishForm = {
        //   name: "",
        //   price: 0,
        //   description: "",
        //   discountId: "0",
        //   discountDate: [],
        //   tags: [],
        //   images: [],
        // };
        // this.allTags = [];
      }
      if (!this.allTags.length) {
        tagListAPI().then((resp) => {
          if (resp.data.code == 200) {
            this.allTags = resp.data.data.tags;
          }
          this.showDishEditDialog = !this.showDishEditDialog;
        });
      } else this.showDishEditDialog = !this.showDishEditDialog;
    },
    onClickSearchDish() {
      this.loadDishList();
    },
    onClickSubmitDish() {
      console.log(this.dishForm);
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    onClickTaggleTag(tag, index) {
      var ex_index = this.dishForm.tags.indexOf(tag.id);
      if (tag.is_chosen) {
        tag.is_chosen = false;
        if (ex_index != -1) {
          this.dishForm.tags.splice(ex_index, 1);
          this.allTags.splice(index, 1);
          this.allTags.push(tag);
        }
      } else {
        tag.is_chosen = true;
        if (ex_index == -1) {
          this.dishForm.tags.push(tag.id);
          this.allTags.splice(index, 1);
          this.allTags.unshift(tag);
        }
      }
    },
    submitUpload() {
      var resp = this.$refs.upload.submit();
      console.log(resp);
    },
  },
};
</script>
<style>
.dishImg {
  max-width: 180px;
}
</style>