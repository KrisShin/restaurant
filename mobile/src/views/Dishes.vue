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
        <van-icon name="search" size="18" @click="tt" />
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
      </van-list>
    </van-pull-refresh>
    <van-tabbar v-model="active" placeholder>
      <van-tabbar-item name="recommend" icon="hot-o" to="/">
        推荐
      </van-tabbar-item>
      <van-tabbar-item
        name="dishes"
        icon="records"
        :dot="localDishCnt != dishCnt"
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
  </div>
</template>

<script>
import { dishListAPI } from "../apis/dish.apis";
export default {
  name: "Dishes",
  data() {
    return {
      active: "dishes",
      cartBadge: sessionStorage.getItem("cartBadge"),
      localDishCnt: localStorage.getItem("localDishCnt"),
      dishCnt: 0,
      userInfo: {},
      dishes: [],
      loading: false,
      finished: false,
      refreshing: false,
      point: 0,
    };
  },
  created: function () {
    this.userInfo = this.$store.state.common.userInfo;
  },
  methods: {
    tt() {
      // this.$router.push("/tags");
    },
    onclickToProfile() {
      this.$router.push("/profile");
    },
    onLoad() {
      dishListAPI({ point: this.point })
        .then((resp) => {
          if (resp.data.success) {
            resp.data.data.forEach((dish) => {
              this.dishes.push(dish);
            });
            console.log(this.dishes);
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
    onRefresh() {
      // 清空列表数据
      this.finished = false;

      // 重新加载数据
      // 将 loading 设置为 true，表示处于加载状态
      this.loading = true;
      this.onLoad();
    },
    changeDishCount() {
      var count = 0;
      this.pushDish.forEach((dish) => {
        count += dish.count;
      });
      sessionStorage.setItem("cartBadge", count);
      this.cartBadge = count || null;
    },
  },
};
</script>