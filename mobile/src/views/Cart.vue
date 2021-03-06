<template>
  <div id="cart">
    <van-nav-bar
      title="恰了木有-结算"
      @click-left="onClickReturn"
      left-arrow
      fixed
      placeholder
    >
      <template #right>
        <van-icon name="delete-o" size="18" @click="onClickClearCart" />
      </template>
    </van-nav-bar>
    <div>
      <van-pull-refresh
        v-if="dishes.length > 0"
        v-model="refreshing"
        @refresh="onRefresh"
      >
        <van-list
          v-model="loading"
          :finished="finished"
          finished-text="没有更多了"
          @load="onLoad"
        >
          <van-swipe-cell
            v-for="(dish, index) in dishes"
            :key="index"
            :name="dish.id"
            :before-close="onClickDelDish"
            stop-propagation
          >
            <van-card
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
                  @change="changeDishCount(dish)"
                  theme="round"
                  default-value="0"
                  button-size="20"
                  min="0"
                  max="99"
                  integer
                />
              </template>
            </van-card>
            <template #right>
              <van-button
                square
                text="删除"
                type="danger"
                class="delete-button"
              />
            </template>
          </van-swipe-cell>
        </van-list>
      </van-pull-refresh>
      <van-row v-else type="flex" justify="center" @click="onClickToDishes">
        <span>购物车为空, 请前往点餐吧</span>
      </van-row>
    </div>
    <van-submit-bar
      :price="total"
      text-align="left"
      button-text="提交订单"
      @submit="onSubmit"
    />
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
      cartBadge: localStorage.getItem("cartBadge")
        ? JSON.parse(localStorage.getItem("cartBadge"))
        : null,
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
    this.loadDishes(dishes);
  },
  beforeRouteLeave(to, form, next) {
    localStorage.setItem("cart", JSON.stringify(this.cart));
    if (!this.cartBadge) {
      this.cartBadge = null;
    }
    localStorage.setItem("cartBadge", JSON.stringify(this.cartBadge));
    next();
  },
  methods: {
    onClickReturn() {
      this.$router.go(-1);
    },
    onClickToDetail(id) {
      this.$router.push("/dishDetail?dish=" + id);
    },
    loadDishes(dishes) {
      dishCartAPI({ dishes })
        .then((resp) => {
          if (resp.data.code === 200) {
            const data = resp.data.data;
            if (data && data.length > 0) {
              this.dishes = data;
              this.dishes.forEach((dish) => {
                dish.count = this.cart[dish.id];
                this.total += dish.price * dish.count * dish.discount;
              });
              this.total *= 100;
            }
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
    onLoad() {
      this.loading = false;
      this.finished = true;
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
    changeDishCount(dish) {
      const lastCount = this.cart[dish.id];
      this.cart[dish.id] = dish.count;
      this.total += (dish.count - lastCount) * dish.price * dish.discount * 100;
      this.cartBadge += dish.count - lastCount;
    },
    onSubmit() {
      // this.$toast.success("下单成功");
      if (this.total > 0) {
        this.$router.push("/orderDetail");
      } else {
        this.$toast.fail("请先点餐吧");
        setTimeout(() => {
          this.$router.replace("dishes");
        }, 300);
      }
    },
    onClickToVIP() {
      this.$toast.success("恭喜成为会员");
    },
    onClickToDishes() {
      this.$router.replace("/dishes");
    },
    onClickDelDish({ position, name, instance }) {
      switch (position) {
        case "right":
          var dish = null;
          this.dishes.forEach((d) => {
            if (d.id == name) {
              dish = d;
            }
          });
          dish.count = 0;

          this.dishes = this.dishes.filter((dish) => {
            return dish.id != name;
          });
          this.changeDishCount(dish);
          break;
        default:
          instance.close();
      }
    },
    onClickClearCart() {
      this.$dialog
        .confirm({
          title: "确认清空购物车吗?",
        })
        .then(() => {
          for (var key in this.cart) {
            this.cart[key] = 0;
          }
          this.dishes = [];
          this.total = 0;
          this.cartBadge = 0;
        })
        .catch();
    },
  },
};
</script>
<style>
.delete-button {
  height: 100%;
}
</style>