<template>
  <div id="order">
    <van-nav-bar
      title="恰了木有-订单"
      @click-left="onClickReturn"
      left-arrow
      fixed
      placeholder
    >
      <template #right>
        <van-icon name="close" size="18" @click="onClickCancelOrder" />
      </template>
    </van-nav-bar>
  </div>
</template>
<script>
import { addrGetDefaultAPI } from "../apis/address.api";
export default {
  name: "Order",
  created() {
    addrGetDefaultAPI()
      .then((resp) => {
        console.log(resp.data);
      })
      .catch((err) => {
        console.error(err);
      });
  },
  methods: {
    onClickReturn() {
      this.$router.go(-1);
    },
    onClickCancelOrder() {
      this.$dialog
        .confirm({ title: "确认取消订单" })
        .then(() => {
          this.$toast("取消订单");
        })
        .catch(() => {
          this.$toast("不取消");
        });
    },
  },
};
</script>