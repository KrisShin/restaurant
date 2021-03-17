<template>
  <div id="home">
    <van-nav-bar title="恰了木有" fixed placeholder>
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
    </van-nav-bar>
    <div>
      <span>推荐菜品</span>
      <van-swipe :autoplay="3000" height="200">
        <van-swipe-item v-for="(dish, index) in pushSwiper" :key="index">
          <img width="100%" v-lazy="dish.index_img" />
        </van-swipe-item>
      </van-swipe>
    </div>
    <div>
      <van-card
        v-for="(dish, index) in pushDish"
        :key="index"
        :num="dish.amount"
        :price="dish.price"
        :desc="dish.description"
        :title="dish.name"
        :thumb="dish.index_img"
        :tag="dish.discount_desc"
        lazy-load
        @click-thumb="onClickToDetail(dish.id)"
      >
        <template #tags>
          <van-tag
            plain
            :color="tag.color"
            v-for="(tag, index) in dish.tags"
            :key="index"
            >{{ tag.name }}</van-tag
          >
        </template>
        <template #footer>
          <van-stepper
            v-model="dish.count"
            @change="changeDishCount"
            theme="round"
            default-value="0"
            button-size="20"
            min="0"
            max="99"
            integer
          />
        </template>
      </van-card>
    </div>
    <div>
      <van-tabbar v-model="active" v-if="isLogin" placeholder>
        <van-tabbar-item name="recommend" icon="hot-o" to="/">
          推荐
        </van-tabbar-item>
        <van-tabbar-item
          name="dishes"
          icon="records"
          :dot="localDishCount != dishCount"
          to="/dishes"
        >
          点餐
        </van-tabbar-item>
        <van-tabbar-item
          name="cart"
          icon="shopping-cart-o"
          :badge="cartBadge"
          to="/cart"
        >
          结算
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
  </div>
</template>

<script>
import { userInfoAPI } from "../apis/user.apis";
import { dishPushAPI } from "../apis/dish.apis";

export default {
  name: "Home",
  data: function () {
    return {
      isLogin: "",
      userInfo: "",
      active: "login",
      pushDish: [],
      pushSwiper: [],
      cartBadge: localStorage.getItem("cartBadge")
        ? JSON.parse(localStorage.getItem("cartBadge"))
        : null,
      localDishCount: localStorage.getItem("localDishCount")
        ? JSON.parse(localStorage.getItem("localDishCount"))
        : 0,
      dishCount: this.$store.state.common.dishCount,
    };
  },
  created() {
    this.isLogin = this.$store.state.common.isLogin;
    this.userInfo = this.$store.state.common.userInfo;
    var cart = JSON.parse(localStorage.getItem("cart"));

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
    dishPushAPI()
      .then((resp) => {
        if (resp.data.success) {
          this.pushDish = resp.data.data.pushDish;
          this.pushSwiper = resp.data.data.pushSwiper;
          this.pushDish.forEach((dish) => {
            dish.count = cart[dish.id];
          });
          this.dishCount = resp.data.data.dishCount;
          this.$store.dispatch("common/setDishCount", this.dishCount);
        }
      })
      .catch((err) => {
        console.error(err);
      });
  },
  beforeRouteLeave(to, form, next) {
    var cart = {};
    this.pushDish.forEach((dish) => {
      cart[dish.id] = dish.count;
    });
    localStorage.setItem("cart", JSON.stringify(cart));
    localStorage.setItem("cartBadge", JSON.stringify(this.cartBadge));
    next();
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
    changeDishCount() {
      var count = 0;
      this.pushDish.forEach((dish) => {
        count += dish.count;
      });
      sessionStorage.setItem("cartBadge", count);
      this.cartBadge = count || null;
    },
    onClickToDetail(id) {
      if (!this.isLogin) {
        this.$toast("请先登录");
        setTimeout(() => {
          this.$router.push("/login");
        }, 300);
      } else {
        this.$router.push("/dishDetail?dish=" + id);
      }
    },
  },
};
</script>
