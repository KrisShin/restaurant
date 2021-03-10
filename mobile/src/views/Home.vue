<template>
  <div id="home">
    <van-nav-bar
      title="恰了木有"
      @click-right="onClickSearch"
      fixed
      placeholder
    >
      <template #left v-if="isLogin">
        <van-image
          width="35"
          height="35"
          round
          fit="cover"
          lazy-load
          :src="userInfo.avatar"
          @click="onclickToProfile"
        />
        <div>{{ userInfo.nickname }}</div>
      </template>
      <template #left v-else>
        <van-image
          width="40"
          height="40"
          round
          fit="cover"
          lazy-load
          src="http://127.0.0.1:9096/static/avatar/default.jpg"
          @click="onClickToLogin"
        />
        <div @click="onClickToLogin">请登录</div>
      </template>
      <template #right>
        <van-icon name="search" size="18" @click="tt" />
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
        <van-card
          num="2"
          price="2.00"
          desc="描述信息"
          title="商品标题"
          thumb="https://img01.yzcdn.cn/vant/ipad.jpeg"
        >
          <template #tags>
            <van-tag plain type="danger">标签</van-tag>
            <van-tag plain type="danger">标签</van-tag>
          </template>
          <template #footer>
            <van-button size="mini">按钮</van-button>
            <van-button size="mini">按钮</van-button>
          </template>
        </van-card>
      </div>
    </div>
    <div>
      <van-tabbar v-model="active" v-if="isLogin" placeholder>
        <van-tabbar-item name="recommend" icon="hot-o" to="/">
          推荐
        </van-tabbar-item>
        <van-tabbar-item
          name="cart"
          icon="shopping-cart-o"
          badge="20"
          to="/cart"
        >
          购物车
        </van-tabbar-item>
        <van-tabbar-item name="my" icon="user-o" badge="20" to="/profile">
          我的
        </van-tabbar-item>
      </van-tabbar>
      <van-tabbar placeholder v-model="active" v-else>
        <van-tabbar-item name="login" icon="hot-o" @click="onClickToLogin">
          登录
        </van-tabbar-item>
        <van-tabbar-item
          name="register"
          icon="hot-o"
          @click="onClickToRegister"
        >
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
import { userInfoAPI, userTestAPI } from "../apis/user.apis";

export default {
  name: "Home",
  data: function () {
    return {
      isLogin: "",
      userInfo: "",
      images: [
        this.$BASE_API + "/static/dish/ftq.jpg",
        this.$BASE_API + "/static/dish/hgr.jpg",
        this.$BASE_API + "/static/dish/tds.jpg",
        this.$BASE_API + "/static/dish/yxqz.jpg",
      ],
      active: "login",
    };
  },
  created() {
    this.isLogin = this.$store.state.common.isLogin;
    this.userInfo = this.$store.state.common.userInfo;

    this.active = "recommend";
    if (this.isLogin && !this.userInfo) {
      userInfoAPI()
        .then((resp) => {
          if (resp.data.success) {
            var userInfo = resp.data.data;
            this.$store.dispatch("common/setUserInfo", userInfo);
            this.userInfo = userInfo;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    }
  },
  methods: {
    onClickToLogin() {
      this.active = "login";
      this.$router.push("/login");
    },
    onClickToRegister() {
      this.active = "register";
      this.$router.push("/register");
    },
    onclickToProfile() {
      this.$router.push("/profile");
    },
    onClickSearch() {
      // this.$router.push("/tags");
    },
    tt() {
      // this.$toast("退出登录");
      // this.$store.dispatch("common/setToken", null);
      // this.$store.dispatch("common/setUserInfo", null);
      userTestAPI();
      // this.$router.go(0);
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
    // test_upavatar() {
    //   var that = this;
    //   if (this.avatar.length < 1) return;
    //   uploadAvatarApi({ avatar: this.avatarContent })
    //     .then((resp) => {
    //       this.$toast("success");
    //       that.a666 = "http://127.0.0.1:9096" + resp.data.avatar;
    //     })
    //     .catch(() => {
    //       this.$toast("failed");
    //     });
    // },
  },
};
</script>
