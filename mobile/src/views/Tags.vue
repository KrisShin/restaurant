<template>
  <div id="tags">
    <van-nav-bar
      title="恰了木有-标签"
      @click-left="onClickReturn"
      left-arrow
      fixed
      placeholder
    />
    <div id="content" style="padding: 2%">
      <div id="allTags">
        <span>选择标签</span>
        <div>
          <van-tag
            v-for="(tag, index) in tags"
            :key="tag.id"
            :color="tag.color"
            :plain="!tag.is_chosen"
            round
            size="medium"
            @click="onClickTaggleTag(tag, index)"
          >
            {{ tag.name }}
          </van-tag>
        </div>
      </div>
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
      this.tags = resp.data.data.tags;
    });
  },
  beforeRouteLeave(to, form, next) {
    this.onChangeTags();
    next();
  },
  methods: {
    onClickReturn() {
      this.$router.go(-1);
    },
    onClickTaggleTag(tag, index) {
      console.log(this.tags.length);
      var ex_index = this.ex_tags.indexOf(tag.id);
      if (tag.is_chosen) {
        tag.is_chosen = false;
        if (ex_index != -1) {
          this.ex_tags.splice(index, 1);
          this.tags.splice(index, 1);
          this.tags.push(tag);
        }
      } else {
        tag.is_chosen = true;
        if (ex_index == -1) {
          this.ex_tags.push(tag.id);
          this.tags.splice(index, 1);
          this.tags.unshift(tag);
        }
      }
    },
    onChangeTags() {
      if (this.ex_tags.length < 1) {
        this.$toast.fail("请至少选择一个标签");
        return;
      }
      var userInfo = this.$store.state.common.userInfo;
      userInfo.tags = this.ex_tags;

      userTagsAPI({ ex_tags: this.ex_tags }).then((resp) => {
        if (resp.data.code === 200) {
          this.$store.dispatch("common/setUserInfo", userInfo);
          this.$notify({
            message: "添加成功",
            background: "green",
            duration: 800,
          });
        }
      });
    },
  },
};
</script>