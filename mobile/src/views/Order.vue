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
    <!-- <van-address-list
      :list="list"
      :switchable="false"
      default-tag-text="默认"
      @click-item="onClickToSwitchAddr"
    /> -->
    <div id="orderAddr">
      <AddrComp :addr="addr" :switchable="true" />
    </div>
    <van-action-sheet v-model="showAddressList" title="标题">
      <div class="content">内容</div>
    </van-action-sheet>
  </div>
</template>
<script>
import { addrGetAPI } from "../apis/address.api";
import AddrComp from "../components/AddrComp.vue";

export default {
  name: "Order",
  components: { AddrComp },
  data() {
    return {
      list: [],
      addr: {},
      showAddressList: false,
      userInfo: {},
    };
  },
  created() {
    this.userInfo = this.$store.state.common.userInfo;
    addrGetAPI({ id: this.userInfo.default_addr })
      .then((resp) => {
        if (resp.data.success) {
          this.addr = resp.data.data;
          this.list.push(resp.data.data);
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
    onClickToSwitchAddr() {
      this.showAddressList = true;
    },
  },
};
</script>