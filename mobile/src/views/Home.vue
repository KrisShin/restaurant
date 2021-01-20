<template>
  <div id="home">
    {{ a }}
    <van-button @click="test_get">get</van-button>
    <van-button @click="test_post">post</van-button>
    <van-button @click="test_put">put</van-button>
    <van-button @click="test_del">del</van-button>
    <van-uploader
      v-model="avatar"
      multiple
      :max-count="1"
      :before-read="beforeRead"
      :after-read="afterRead"
      :max-size="500 * 1024"
      @oversize="onOversize"
    />
    <van-button @click="test_upavatar">submit</van-button>
    <img :src="a666" />
    {{ a666 }}
    <div v-if="a">
      <router-link to="/login">login</router-link> /
      <router-link to="/register">register</router-link>
    </div>
    <div v-else>
      <van-row type="flex">
        <van-col span="6">span: 6</van-col>
        <van-col span="6">span: 6</van-col>
        <van-col span="6">span: 6</van-col>
      </van-row>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import { Button, Col, Row, Uploader, Toast } from "vant";
import {
  getAPI,
  postAPI,
  putAPI,
  delAPI,
  uploadAvatarApi,
} from "../apis/user.apis";

export default {
  name: "Home",
  data: function () {
    return {
      a: true,
      avatar: [],
      avatarContent: "",
      a666: "",
    };
  },
  components: {
    [Button.name]: Button,
    [Row.name]: Row,
    [Col.name]: Col,
    [Uploader.name]: Uploader,
  },
  methods: {
    test_get: function () {
      getAPI({ test: 123 })
        .then((resp) => {
          console.log(resp);
        })
        .catch((resp) => {
          console.error(resp);
        });
    },
    test_post: function () {
      postAPI({ test: 123 })
        .then((resp) => {
          console.log(resp);
        })
        .catch((resp) => {
          console.error(resp);
        });
    },
    test_put: function () {
      putAPI({ test: 123 })
        .then((resp) => {
          console.log(resp);
        })
        .catch((resp) => {
          console.error(resp);
        });
    },
    test_del: function () {
      delAPI({ test: 123 })
        .then((resp) => {
          console.log(resp);
        })
        .catch((resp) => {
          console.error(resp);
        });
    },
    beforeRead(file) {
      var typeArr = ["image/jpeg", "image/png"];
      if (typeArr.indexOf(file.type) == -1) {
        Toast("请上传 jpg或png 格式图片");
        return false;
      }
      return true;
    },
    afterRead(file) {
      this.avatarContent = file.content; // 获取图片base
    },
    onOversize() {
      Toast("文件大小不能超过 500kb");
      uploadAvatarApi();
    },
    test_upavatar() {
      var that = this;
      if (this.avatar.length < 1) return;
      uploadAvatarApi({ avatar: this.avatarContent })
        .then((resp) => {
          Toast("success");
          that.a666 = "http://127.0.0.1:9096" + resp.data.avatar;
        })
        .catch(() => {
          Toast("failed");
        });
    },
  },
};
</script>
