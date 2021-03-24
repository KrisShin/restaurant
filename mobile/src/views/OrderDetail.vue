<template>
  <div id="orderDetail">
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
        <div>收货地址:</div>
        <div @click="onClickShowAddrs">
          <AddrComp :addr="address" :switchable="false" :is_border="true" />
        </div>
      </div>
      <div class="order-subTitle">菜品列表:</div>
      <van-list :loading="listLoading">
        <van-cell v-for="dish in dishes" :key="dish.id" :title="dish.name">
          <template #title>
            <span>{{ dish.name }}</span>
            <van-tag type="danger">{{ dish.discount_desc }}</van-tag>
          </template>
          <template #label>
            <span>
              共计:
              {{ (dish.price * dish.count * dish.discount) | numFilter }}元
            </span>
          </template>
          <template #right-icon>
            <span>×{{ dish.count }}</span>
            <span></span>
          </template>
        </van-cell>
      </van-list>
      <div class="order-subTitle">消费结算:</div>
      <div>
        <van-row>消费时间: {{ orderTime }}</van-row>
        <van-row>消费金额: {{ originMoney | numFilter }}</van-row>
        <van-row>活动优惠: {{ (total - originMoney) | numFilter }}</van-row>
        <van-row>实际金额: {{ total | numFilter }}</van-row>
      </div>
      <div class="order-subTitle">留言备注:</div>
      <van-field
        v-model="note"
        rows="2"
        class="margin-b3"
        autosize
        type="textarea"
        maxlength="120"
        placeholder="请输入留言"
        show-word-limit
        :readonly="!!id"
      />
      <van-goods-action>
        <van-goods-action-button
          type="warning"
          text="我再想想"
          @click="onClickReturn"
        />
        <van-goods-action-button
          v-if="!id"
          type="danger"
          text="立即购买"
          @click="onClickSubmitOrder"
        />
        <van-goods-action-button
          v-if="id && order.status == 1"
          type="danger"
          text="立即付款"
          @click="onClickPayOrder"
        />
        <van-goods-action-button
          v-if="id && order.status == 2"
          type="danger"
          text="取消订单"
          @click="onClickCancelOrder"
        />
        <van-goods-action-button
          v-if="id && [3,4,5].includes(order.status)"
          type="danger"
          text="申请退款"
          @click="onClickCancelOrder"
        />
      </van-goods-action>
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
import { addrGetAPI, addrListAPI } from "../apis/address.apis";
import { dishCartAPI } from "../apis/dish.apis";
import {
  orderAddAPI,
  orderCancelAPI,
  orderGetAPI,
  orderPayAPI,
} from "../apis/order.apis";
import AddrComp from "../components/AddrComp.vue";

export default {
  name: "OrderDetail",
  components: { AddrComp },
  data() {
    return {
      list: [],
      address: {},
      showAddressList: false,
      userInfo: {},
      addrId: 0,
      dishes: [],
      listLoading: true,
      orderTime: new Date().toLocaleString(),
      originMoney: 0,
      total: 0,
      note: "",
      id: null,
      order: {},
    };
  },
  created() {
    this.id = this.$route.query.id;
    this.userInfo = this.$store.state.common.userInfo;
    this.addrId = this.userInfo.default_addr;
    if (this.id) {
      this.loadOrder();
    } else {
      this.cart = JSON.parse(localStorage.getItem("cart"));
      this.loadDishes();
      this.loadAddr();
    }
  },
  filters: {
    numFilter(value) {
      let realVal = Number(value).toFixed(2);
      return Number(realVal);
    },
  },
  methods: {
    onClickReturn() {
      this.$router.go(-1);
    },
    onClickCancelOrder() {
      this.$dialog
        .confirm({ title: "确认取消订单" })
        .then(() => {
          orderCancelAPI({ id: this.id })
            .then((resp) => {
              if (resp.data.success) {
                this.$toast.success("取消订单成功");
                this.userInfo.balance += this.total
                this.$store.dispatch("common/setUserInfo", this.userInfo);
                this.$router.replace("/orders?type=all");
              } else {
                this.$toast.fail("resp.data.data.msg");
                this.$toast.fail("取消订单失败");
              }
            })
            .catch((err) => {
              console.error(err);
              this.$toast.fail("取消订单失败");
            });
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
      if (this.id) return;
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
    loadDishes() {
      if (this.id) return;

      this.listLoading = true;
      this.total = 0;
      this.originMoney = 0;
      var dishes = [];
      for (var key in this.cart) {
        if (this.cart[key] > 0) {
          dishes.push(key);
        }
      }
      dishCartAPI({ dishes })
        .then((resp) => {
          if (resp.data.success) {
            const data = resp.data.data;
            if (data && data.length > 0) {
              this.dishes = data;
              this.dishes.forEach((dish) => {
                dish.count = this.cart[dish.id];
                this.total += dish.price * dish.count * dish.discount;
                this.originMoney += dish.price * dish.count;
              });
            }
            this.listLoading = false;
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
    onClickSubmitOrder() {
      orderAddAPI({
        note: this.note,
        cart: JSON.stringify(this.cart),
        addrId: this.addrId,
      })
        .then((resp) => {
          if (resp.data.success) {
            this.$toast.success("提交成功");
            this.$router.replace("/orderDetail?id=" + resp.data.data.id);
            for (var key in this.cart) {
              this.cart[key] = 0;
            }
            localStorage.setItem("cart", JSON.stringify(this.cart));
            if (!this.cartBadge) {
              this.cartBadge = null;
            }
            localStorage.removeItem("cartBadge");
            window.location.reload();
          }
        })
        .catch((err) => {
          this.$notify({
            message: "订单提交失败, 请稍后重试",
            type: "danger",
          });
          console.error(err);
        });
    },
    onClickPayOrder() {
      this.$dialog
        .confirm({ title: "确认支付", message: "共计:" + this.total + "元" })
        .then(() => {
          orderPayAPI({ id: this.id })
            .then((resp) => {
              if (resp.data.success) {
                this.userInfo.balance -= this.total
                this.$store.dispatch("common/setUserInfo", this.userInfo);
                this.$toast.success("支付成功");
                this.$router.replace("/orders?type=all");
              } else {
                this.$toast.fail("支付失败");
              }
            })
            .catch((err) => {
              console.error(err);
              this.$toast.fail("支付失败");
            });
        })
        .catch(() => {
          this.$toast("取消支付");
        });
    },
    loadOrder() {
      this.originMoney = 0;
      this.total = 0;
      orderGetAPI({ id: this.id })
        .then((resp) => {
          if (resp.data.success) {
            this.order = resp.data.data.order;
            this.address = this.order.address;
            this.dishes = this.order.dishes;
            this.dishes.forEach((dish) => {
              this.originMoney += dish.price * dish.count;
            });
            this.total = this.order.money;
            this.orderTime = this.order.create_time;
            this.note = this.order.note;
          }
          this.listLoading = false;
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
.order-subTitle {
  margin: 1.2rem 0 0.3rem 0;
  border-bottom: dashed grey;
  border-width: 0.1rem;
}
.margin-b3 {
  margin-bottom: 3rem;
}
</style>