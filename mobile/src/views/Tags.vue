<template>
  <div id="tags">
    <van-nav-bar title="恰了木有-标签" @click-left="onClickReturn" left-arrow />
    <div id="choosen">
      <span>已选标签</span>
      <div v-if="ex_tags.length > 0">
        <van-tag
          v-for="(tag, index) in ex_tags"
          :key="tag.id"
          round
          type="primary"
          @click="onClickRemoveTag(tag, index)"
        >
          {{ tag.name }}
        </van-tag>
      </div>
      <van-empty v-else description="选择你的标签" />
    </div>
    <div id="allTags">
      <span>所有标签</span>

      <van-tag
        v-for="(tag, index) in tags"
        :key="tag.id"
        plain
        round
        type="primary"
        @click="onClickAddTag(tag, index)"
      >
        {{ tag.name }}
      </van-tag>
    </div>
  </div>
</template>
<script>
import { dishTagsAPI } from "../apis/dish.apis";

export default {
  name: "Tags",
  data() {
    return {
      tags: [],
      ex_tags: [],
    };
  },
  created() {
    dishTagsAPI().then((resp) => {
      this.ex_tags = resp.data.data.exist_tags;
      this.tags = resp.data.data.tags;
    });
  },
  methods: {
    onClickReturn() {
      this.$router.go(-1);
    },
    onClickAddTag(tag, index) {
      //   this.$toast.success(tag.name);
      this.tags.splice(index, 1);
      this.ex_tags.push(tag);
    },
    onClickRemoveTag(tag, index) {
      //   this.$toast.fail(tag.name);
      this.ex_tags.splice(index, 1);
      this.tags.push(tag);
    },
  },
};
</script>