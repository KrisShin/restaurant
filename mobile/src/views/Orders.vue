<template>
  <div id="orders">
    <van-nav-bar
      title="恰了木有-订单"
      @click-left="onClickReturn"
      left-arrow
      fixed
      placeholder
    >
      <template #right>
        <van-icon name="search" size="18" @click="onClickSearchOrder" />
      </template>
    </van-nav-bar>
    <van-pull-refresh v-model="refreshing" @refresh="onRefresh">
      <van-list
        v-model="loading"
        :finished="finished"
        finished-text="没有更多了"
        @load="loadOrders"
      >
        <van-card
          v-for="(order, index) in list"
          :key="index"
          :num="order.amount"
          :price="order.money"
          :desc="order.address.address"
          :title="order.address.name"
          :thumb="order.index_img"
          lazy-load
          @click="onClickToDetail(order.id)"
        >
          <template #tags>
            <van-tag plain>
              {{ order.create_time.toLocaleString() }}
            </van-tag>
            <van-tag plain type="success" v-if="order.note">
              {{ order.note }}
            </van-tag>
            <van-tag :color="order.status_color">
              {{ order.status_desc }}
            </van-tag>
          </template>
        </van-card>
      </van-list>
    </van-pull-refresh>
  </div>
</template>
<script>
import { orderListAPI } from "../apis/order.apis";
export default {
  name: "Orders",
  data() {
    return {
      list: [],
      active: "dishes",
      loading: false,
      finished: false,
      refreshing: false,
      status: null,
      point: 0,
      cart: {},
    };
  },
  created() {
    this.status = this.$route.query.type;
    this.loadOrders();
  },
  afterRouteEnter(to, form, next) {
    this.point = 0;
    this.list = [];
    next();
  },
  methods: {
    loadOrders() {
      this.loading = true;
      orderListAPI({ point: this.point, status: this.status })
        .then((resp) => {
          if (resp.data.success) {
            resp.data.data.orders.forEach((order) => {
              this.list.push(order);
            });
            this.point = this.list.length;
            if (resp.data.data.orders.length < 5) {
              this.finished = true;
            }
          }
          this.loading = false;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    onClickSearchOrder() {},
    onClickReturn() {
      this.$router.go(-1);
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
    onClickToDetail(id) {
      this.$router.push("/orderDetail?id=" + id);
    },
  },
};
</script>