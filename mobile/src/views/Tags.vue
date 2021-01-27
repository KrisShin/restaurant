<template>
  <div id="tags">
    <span>选择标签</span>
    <div id="choosen">
      <van-tag
        v-for="(index, tag) in ex_tags"
        :key="tag.id"
        round
        type="primary"
        @click="onClickRemoveTag(index, tag)"
      >
        {{ tag.name }}
      </van-tag>
    </div>
    <div id="allTags">
      <van-tag
        v-for="(index, tag) in tags"
        :key="tag.id"
        round
        mark
        type="primary"
        @click="onClickAddTag(index, tag)"
      >
        {{ tag.name }}
      </van-tag>
    </div>
  </div>
</template>
<script>
import Vue from "vue";
import { Tag } from "vant";
import { dishTagsAPI } from "../apis/dish.apis";

Vue.use(Tag);
export default {
  name: "Tags",
  data() {
    return {
      tags: [],
      ex_tags: [],
    };
  },
  created() {
    var _this = this;
    dishTagsAPI().then((resp) => {
      _this.ex_tags = resp.data.data.exist_tags;
      _this.tags = resp.data.data.tags;
    });
  },
  methods: {
    onClickAddTag(index, tag) {
      this.$toast.success(tag.name);
      this.tags.splice(index, 0);
      this.ex_tags.push(tag);
    },
    onClickRemoveTag(index, tag) {
      this.$toast.fail(tag.name);
      this.ex_tags.splice(index, 0);
      this.tags.push(tag);
    },
  },
};
</script>