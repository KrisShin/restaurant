<template>
  <div id="editInfo">
    <van-nav-bar
      title="恰了木有-编辑信息"
      @click-left="onClickReturn"
      left-arrow
    />
    <van-cell-group title="头像">
      <van-row type="flex" justify="center">
        <van-uploader
          v-model="avatars"
          multiple="false"
          :max-count="1"
          :before-read="beforeRead"
          :after-read="afterRead"
          :max-size="500 * 1024"
          @oversize="onOversize"
        />
      </van-row>
    </van-cell-group>
    <van-cell-group title="基本信息">
      <van-field label="昵称" :value="userInfo.nickname" size="mini" />
      <van-field label="年龄" :value="userInfo.age" readonly />
      <van-field label="性别" :value="userInfo.gender ? '男' : '女'" readonly />
      <van-field label="邮箱" :value="userInfo.email" />
      <van-field label="手机号" :value="userInfo.phone" />
    </van-cell-group>

    <van-button @click="test_upavatar">submit</van-button>
  </div>
</template>

<script>
import { uploadAvatarAPI } from "../apis/user.apis";
export default {
  name: "EditInfo",
  data() {
    return {
      userInfo: {},
      avatarContent: "",
      avatars: [],
    };
  },
  created: function () {
    this.userInfo = this.$store.state.common.userInfo;
    this.avatars.push({ url: this.userInfo.avatar, previewSize: 200 });
  },
  methods: {
    onClickReturn() {
      this.$router.go(-1);
    },
    beforeRead(file) {
      var typeArr = ["image/jpeg", "image/png"];
      if (typeArr.indexOf(file.type) == -1) {
        this.$toast("请上传 jpg或png 格式图片");
        return false;
      }
      return true;
    },
    afterRead(file) {
      this.avatarContent = file.content; // 获取图片base
    },
    onOversize() {
      this.$toast("文件大小不能超过 500kb");
    },
    test_upavatar() {
      if (this.userInfo.avatar.length < 1) return;
      uploadAvatarAPI({ avatar: this.avatarContent })
        .then((resp) => {
          this.$toast("success");
          console.log(resp.data);
        })
        .catch(() => {
          this.$toast("failed");
        });
    },
  },
};
</script>