<template>
  <div id="tags">
    <van-nav-bar title="恰了木有-标签" @click-left="onClickReturn" left-arrow />
    <div id="choosen" flex="1">
      <van-row>
        <van-col>
          <span>已选标签</span>
        </van-col>
        <van-col>
          <van-button size="mini" type="success" @click="onClickTags"
            >提交</van-button
          >
        </van-col>
      </van-row>
      <div v-if="ex_tags.length > 0">
        <van-tag
          v-for="(tag, index) in ex_tags"
          :key="tag.id"
          :color="tag.color"
          round
          type="primary"
          size="medium"
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
        :color="tag.color"
        plain
        round
        size="medium"
        @click="onClickAddTag(tag, index)"
      >
        {{ tag.name }}
      </van-tag>
    </div>
  </div>
</template>
<script>
import { dishTagsAPI } from "../apis/dish.apis";
import { userTagsAPI } from "../apis/user.apis";

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
    onClickTags() {
      if (this.ex_tags.length < 1) {
        this.$toast.fail("请至少选择一个标签");
        return;
      }
      var tagIds = [];
      this.ex_tags.forEach((tag) => {
        tagIds.push(tag.id);
      });
      userTagsAPI({ ex_tags: tagIds }).then((resp) => {
        if (resp.data.success) {
          this.$notify({ message: "添加成功", background: "green" });
        }
      });
    },
  },
};
</script>