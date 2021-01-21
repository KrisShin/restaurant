<template>
  <div id="home">
    <van-nav-bar title="恰了木有" @click-right="onClickSearch">
      <template #left>
        <van-image
          width="40"
          height="40"
          round
          fit="cover"
          lazy-load
          src="http://127.0.0.1:9096/static/avatar/default.jpg"
        />
      </template>
      <template #right>
        <van-icon name="search" size="18" />
      </template>
    </van-nav-bar>
    <div>
      <div>
        <span>推荐菜品</span>
        <van-swipe :autoplay="3000">
          <van-swipe-item v-for="(image, index) in images" :key="index">
            <img width="100%" v-lazy="image" />
          </van-swipe-item>
        </van-swipe>
      </div>
    </div>
    <div>
      <van-tabbar v-model="active" v-if="is_login">
        <van-tabbar-item icon="hot-o" @click="hello"> 推荐 </van-tabbar-item>
        <van-tabbar-item icon="shopping-cart-o" badge="20">
          购物车
        </van-tabbar-item>
        <van-tabbar-item icon="user-o" badge="20">我的</van-tabbar-item>
      </van-tabbar>
      <van-tabbar v-model="active" v-else>
        <van-tabbar-item icon="hot-o" @click="onClickToLogin">
          登录
        </van-tabbar-item>
        <van-tabbar-item icon="hot-o" @click="onClickToRegister">
          注册
        </van-tabbar-item>
      </van-tabbar>
    </div>
    <!-- <van-button @click="test_get">get</van-button>
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
    </div> -->
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import {
  NavBar,
  Icon,
  Toast,
  Image as VanImage,
  Lazyload,
  Swipe,
  SwipeItem,
  Tabbar,
  TabbarItem,
} from "vant";
import Vue from "vue";
// import {
//   getAPI,
//   postAPI,
//   putAPI,
//   delAPI,
//   uploadAvatarApi,
// } from "../apis/user.apis";

Vue.use(Tabbar);
Vue.use(TabbarItem);

Vue.use(Swipe);
Vue.use(SwipeItem);
Vue.use(Icon);
Vue.use(NavBar);
Vue.use(VanImage);
Vue.use(Lazyload);

export default {
  name: "Home",
  data: function () {
    return {
      is_login: false,
      avatar: [],
      avatarContent: "",
      a666: "",
      images: [
        "http://127.0.0.1:9096/static/dish/ftq.jpg",
        "http://127.0.0.1:9096/static/dish/hgr.jpg",
        "http://127.0.0.1:9096/static/dish/tds.jpg",
        "http://127.0.0.1:9096/static/dish/yxqz.jpg",
      ],
    };
  },
  methods: {
    onClickToLogin() {
      this.$router.push("/login");
    },
    onClickToRegister() {
      this.$router.push("/register");
    },
    onClickSearch() {
      Toast("按钮");
    },
    // test_get: function () {
    //   getAPI({ test: 123 })
    //     .then((resp) => {
    //       console.log(resp);
    //     })
    //     .catch((resp) => {
    //       console.error(resp);
    //     });
    // },
    // test_post: function () {
    //   postAPI({ test: 123 })
    //     .then((resp) => {
    //       console.log(resp);
    //     })
    //     .catch((resp) => {
    //       console.error(resp);
    //     });
    // },
    // test_put: function () {
    //   putAPI({ test: 123 })
    //     .then((resp) => {
    //       console.log(resp);
    //     })
    //     .catch((resp) => {
    //       console.error(resp);
    //     });
    // },
    // test_del: function () {
    //   delAPI({ test: 123 })
    //     .then((resp) => {
    //       console.log(resp);
    //     })
    //     .catch((resp) => {
    //       console.error(resp);
    //     });
    // },
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
    },
    // test_upavatar() {
    //   var that = this;
    //   if (this.avatar.length < 1) return;
    //   uploadAvatarApi({ avatar: this.avatarContent })
    //     .then((resp) => {
    //       Toast("success");
    //       that.a666 = "http://127.0.0.1:9096" + resp.data.avatar;
    //     })
    //     .catch(() => {
    //       Toast("failed");
    //     });
    // },
  },
};
</script>
