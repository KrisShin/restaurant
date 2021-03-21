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
    <div id="content">
      <div id="orderAddr">
        <span>收货地址:</span>
        <div @click="onClickShowAddrs">
          <AddrComp :addr="address" :switchable="false" :is_border="true" />
        </div>
      </div>
    </div>
    <van-action-sheet
      v-model="showAddressList"
      cancel-text="完成"
      title="选择收货地址"
      @closed="loadAddr"
    >
      <van-radio-group
        v-model="address.id"
        @change="onClickSwitchAddr(address.id)"
      >
        <AddrComp
          v-for="addr in list"
          :key="addr.id"
          :addr="addr"
          :switchable="true"
          :is_border="false"
        />
      </van-radio-group>
    </van-action-sheet>
  </div>
</template>
<script>
import { addrGetAPI, addrListAPI } from "../apis/address.api";
import AddrComp from "../components/AddrComp.vue";

export default {
  name: "Order",
  components: { AddrComp },
  data() {
    return {
      list: [],
      address: {},
      showAddressList: false,
      userInfo: {},
      addrId: 0,
      dishes: [],
    };
  },
  created() {
    this.userInfo = this.$store.state.common.userInfo;
    this.addrId = this.userInfo.default_addr;
    this.loadAddr();
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
    onClickSwitchAddr(id) {
      this.addrId = id;
    },
    loadAddr() {
      addrGetAPI({ id: this.addrId })
        .then((resp) => {
          if (resp.data.success) {
            this.address = resp.data.data;
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
    onClickShowAddrs() {
      this.showAddressList = true;
      addrListAPI()
        .then((resp) => {
          if (resp.data.success) {
            this.list = resp.data.data.addresses;
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>
<style scoped>
#content {
  padding: 0.1rem 0.3rem 0.1rem 0.3rem;
}
</style>