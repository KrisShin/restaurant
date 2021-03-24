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
      userInfo: {},
      loading: false,
      finished: false,
      refreshing: false,
      point: 0,
      cart: {},
    };
  },
  created() {
    this.userInfo = this.$store.state.common.userInfo;
    this.loadOrders();
  },
  methods: {
    loadOrders() {
      this.loading = true;
      orderListAPI()
        .then((resp) => {
          if (resp.data.success) {
            console.log(resp.data);
            this.loading = false;
            return;
          }
          this.finished = true;
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
      this.$router.push("/dishDetail?dish=" + id);
    },
  },
};
</script>