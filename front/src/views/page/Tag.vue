<template>
  <el-main>
    <span>Tags ooh yeah !!!</span>
  </el-main>
</template>

<script>
// @ is an alias to /src
import { dishListAPI, tagListAPI, dishOperateAPI } from "@/apis/dish.apis";

export default {
  name: "Tag",
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
        // images:[]
      },
      dialogTitle: "新增菜品",
      allTags: [],
      allDiscount: [],
    };
  },
  created() {
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
    initDishForm() {
      this.dishForm = {
        name: "",
        price: 0,
        description: "",
        discountId: "0",
        discountDate: [],
        tags: [],
        images: [],
      };
      this.allTags = [];
    },
    onClickEditDish(type) {
      this.editType = type;
      this.dialogTitle = type === "add" ? "新增菜品" : "编辑菜品";
      if (!this.showDishEditDialog && type === "add") {
        // this.initDishForm();
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
    onClickSubmitDish() {
      // debugger;
      let dform = new FormData();
      this.$refs.upload.uploadFiles.forEach((file) => {
        dform.append("images", file.raw);
      });
      dform.append("data", JSON.stringify(this.dishForm));
      console.log(dform);
      console.log(dform.get("data"), dform.getAll("images"));

      dishOperateAPI(dform).then((resp) => {
        console.log(resp.data);
        this.initDishForm();
      });
    },
  },
};
</script>
<style>
.dishImg {
  max-width: 180px;
}
</style>