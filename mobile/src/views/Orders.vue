<template>
  <div id="orders">
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
    };
  },
  created() {
    this.loadOrders();
  },
  methods: {
    loadOrders() {
      orderListAPI()
        .then((resp) => {
          if (resp.data.success) {
            console.log(resp.data);
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>