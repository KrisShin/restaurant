<template>
  <div id="cart">
    <van-nav-bar
      title="恰了木有-结算"
      @click-left="onClickReturn"
      left-arrow
      @click-right="tt"
      fixed
      placeholder
    >
      <template #right>
        <van-icon name="delete-o" size="18" @click="tt" />
      </template>
    </van-nav-bar>
    <div>
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
              <van-tag v-if="dish.discount_desc" type="danger">{{
                dish.discount_desc
              }}</van-tag>
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
    </div>
    <van-submit-bar :price="total" text-align='left' button-text="提交订单" @submit="onSubmit">
      <template v-if="!userInfo.is_vip" #tip>
        成为会员可以享受优惠
        <span @click="onClickToVIP">成为会员</span>
      </template>
    </van-submit-bar>
  </div>
</template>

<script>
import { dishCartAPI } from "../apis/dish.apis";

export default {
  name: "Cart",
  data() {
    return {
      userInfo: {},
      dishes: [],
      loading: false,
      finished: false,
      refreshing: false,
      total: 0,
    };
  },
  created() {
    this.userInfo = this.$store.state.common.userInfo;
    this.cart = JSON.parse(localStorage.getItem("cart"));
    var dishes = [];
    for (var key in this.cart) {
      if (this.cart[key] > 0) {
        dishes.push(key);
      }
    }
    dishCartAPI({ dishes })
      .then((resp) => {
        if (resp.data.success) {
          this.dishes = resp.data.data;
          this.dishes.forEach((dish) => {
            dish.count = this.cart[dish.id];
            this.total += dish.price * dish.count * dish.discount;
          });
          this.total *= 100;
        }
      })
      .catch((err) => {
        console.error(err);
      });
  },
  methods: {
    onClickReturn() {
      this.$router.go(-1);
    },
    tt() {
      // this.$router.push("/tags");
    },
    onLoad() {
      // if (resp.data.success) {
      //   if (resp.data.data) {
      //     resp.data.data.forEach((dish) => {
      //       dish.count = this.cart[dish.id];
      //       this.dishes.push(dish);
      //     });
      //     this.point += resp.data.data.length;
      this.loading = false;
      //     if (resp.data.data.length < 5) {
      //       this.finished = true;
      //     }
      //   } else {
      this.finished = true;
      //   }
      // }
    },
    onRefresh() {
      // 清空列表数据
      this.finished = false;
      this.point = 0;

      // 重新加载数据
      // 将 loading 设置为 true，表示处于加载状态
      this.loading = true;
      this.onLoad();
    },
    changeDishCount() {
      this.total = 0;
      var count = 0;
      this.dishes.forEach((dish) => {
        count += dish.count;
        this.total += dish.price * dish.count * dish.discount;
      });
      sessionStorage.setItem("cartBadge", count);
      this.total *= 100;
      this.cartBadge = count || null;
    },
    onSubmit() {},
    checked() {},
    onClickToVIP() {
      this.$toast("恭喜成为会员");
    },
  },
};
</script>