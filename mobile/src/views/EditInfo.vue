<template>
  <div id="editInfo">
    <van-nav-bar
      title="恰了木有-编辑信息"
      @click-left="onClickReturn"
      left-arrow
      fixed
      placeholder
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
      <van-field label="昵称" v-model="nickname" required size="mini" />
      <van-field
        label="年龄"
        type="digit"
        required
        v-model="age"
        :formatter="age_formatter"
        format-trigger="onBlur"
      />
      <van-field label="性别" :value="userInfo.gender ? '男' : '女'" readonly />
      <van-field label="邮箱" :value="userInfo.email" readonly />
      <van-field label="手机号" :value="userInfo.phone" readonly />
      <van-cell title="标签" is-link to="/tags" :value='userInfo.tags.length' />
    </van-cell-group>

    <van-button type="primary" block @click="test_upavatar">
      确认修改
    </van-button>
  </div>
</template>

<script>
import { userEditInfoAPI } from "../apis/user.apis";
export default {
  name: "EditInfo",
  data() {
    return {
      userInfo: {},
      avatarContent: "",
      nickname: "",
      age: "",
      avatars: [],
    };
  },
  created () {
    this.userInfo = this.$store.state.common.userInfo;
    this.avatars.push({ url: this.userInfo.avatar });
    this.nickname = this.userInfo.nickname;
    this.age = this.userInfo.age;
  },
  methods: {
    onClickReturn() {
      this.$router.go(-1);
    },
    age_formatter() {
      if (this.age <= 0) return (this.age = 0);
      if (this.age >= 120) return (this.age = 120);
      return this.age;
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
      userEditInfoAPI({
        avatar: this.avatarContent,
        nickname: this.nickname,
        age: this.age,
      })
        .then((resp) => {
          if (resp.data.success) {
            this.userInfo.avatar = resp.data.data.avatar;
            this.userInfo.nickname = this.nickname;
            this.userInfo.age = this.age;
            this.$store.dispatch("common/setUserInfo", this.userInfo);
            this.$notify({
              message: "修改成功",
              type: "success",
              duration: 1000,
            });
          } else {
            // this.$toast.fail("修改失败");
            this.$notify({
              message: "修改失败",
              type: "warning",
              duration: 1000,
            });
          }
        })
        .catch((err) => {
          this.$toast.fail("修改失败");
          console.error(err);
        });
    },
  },
};
</script>