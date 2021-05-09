<template>
  <div id="dishes">
    <van-nav-bar title="恰了木有-点餐" fixed placeholder>
      <template #left>
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
      <template #right>
        <van-icon name="search" size="18" @click="onClickSearchDish" />
      </template>
    </van-nav-bar>
    <van-pull-refresh v-model="refreshing" @refresh="onRefresh">
      <van-list
        v-model="loading"
        :finished="finished"
        finished-text="没有更多了"
        @load="onLoad"
      >
        <van-card
          v-for="(dish, index) in dishes"
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
            >
              {{ tag.name }}
            </van-tag>
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
      </van-list>
    </van-pull-refresh>
    <van-tabbar v-model="active" placeholder>
      <van-tabbar-item name="recommend" icon="hot-o" to="/">
        推荐
      </van-tabbar-item>
      <van-tabbar-item name="dishes" icon="records" to="/dishes">
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
      <van-tabbar-item name="my" icon="user-o" :badge="myBadge" to="/profile">
        我的
      </van-tabbar-item>
    </van-tabbar>
  </div>
</template>

<script>
import { dishListAPI } from "../apis/dish.apis";
export default {
  name: "Dishes",
  data() {
    return {
      active: "dishes",
      cartBadge: localStorage.getItem("cartBadge")
        ? JSON.parse(localStorage.getItem("cartBadge"))
        : null,
      userInfo: {},
      dishes: [],
      loading: false,
      finished: false,
      refreshing: false,
      point: 0,
      cart: {},
      myBadge: localStorage.getItem("myBadge")
        ? JSON.parse(localStorage.getItem("myBadge"))
        : null
    };
  },
  created: function () {
    this.userInfo = this.$store.state.common.userInfo;
    this.cart = JSON.parse(localStorage.getItem("cart"));
    localStorage.setItem("localDishCount", this.$store.state.common.dishCount);
  },
  beforeRouteLeave(to, form, next) {
    this.dishes.forEach((dish) => {
      this.cart[dish.id] = dish.count;
    });
    localStorage.setItem("cart", JSON.stringify(this.cart));
    localStorage.setItem("cartBadge", JSON.stringify(this.cartBadge));
    next();
  },
  methods: {
    onClickSearchDish() {
      // this.$router.push("/tags");
    },
    onclickToProfile() {
      this.$router.push("/profile");
    },
    onLoad() {
      dishListAPI({ point: this.point })
        .then((resp) => {
          if (resp.data.success) {
            if (resp.data.data) {
              resp.data.data.forEach((dish) => {
                dish.count = this.cart[dish.id];
                this.dishes.push(dish);
              });
              this.point += resp.data.data.length;
              if (resp.data.data.length < 5) {
                this.finished = true;
              }
            } else {
              this.finished = true;
            }
          }
          this.loading = false;
          this.finished = true;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    onRefresh() {
      // 清空列表数据
      this.finished = false;
      this.point = 0;
      this.dishes = [];

      // 重新加载数据
      // 将 loading 设置为 true，表示处于加载状态
      this.loading = true;
      this.onLoad();
    },
    changeDishCount() {
      var count = 0;
      this.dishes.forEach((dish) => {
        count += dish.count;
      });
      sessionStorage.setItem("cartBadge", count);
      this.cartBadge = count || null;
    },
    onClickToDetail(id) {
      this.$router.push("/dishDetail?dish=" + id);
    },
  },
};
</script>