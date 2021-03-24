<template>
  <div id="profile">
    <van-nav-bar title="恰了木有-我的" fixed placeholder />
    <div
      style="padding: 10px; background: aliceblue"
      class="van-hairline--top-bottom"
    >
      <van-row type="flex" justify="center">
        <van-image
          width="50"
          height="50"
          round
          fit="cover"
          lazy-load
          :src="userInfo.avatar"
          to="/editInfo"
        />
      </van-row>
      <van-row type="flex" justify="center" gutter="8">
        <van-col>{{ userInfo.age }} |</van-col>
        <van-col>{{ userInfo.nickname }} |</van-col>
        <van-col v-if="userInfo.gender" style="color: skyblue">♂</van-col>
        <van-col v-else style="color: pink">♀</van-col>
      </van-row>
      <van-row type="flex" justify="center" gutter="8">
        <van-col v-if="userInfo.is_new">
          <van-tag type="danger">新用户</van-tag>
        </van-col>
        <van-col v-if="userInfo.is_email_active">
          <van-tag type="success">已认证</van-tag>
        </van-col>
        <van-col v-else @click="clickToShowActive">
          <van-tag>未认证</van-tag>
        </van-col>
        <van-col>余额:{{ userInfo.balance }}</van-col>
      </van-row>
      <van-row type="flex" justify="center">
        <van-tag
          v-for="(tag, index) in userInfo.tags"
          :key="index"
          :color="tag.color"
          round
          size="medium"
          plain
        >
          {{ tag.name }}
        </van-tag>
      </van-row>
    </div>
    <van-tabbar
      v-model="orderActive"
      active-color="#7777FF"
      inactive-color="#EF6611"
      :fixed="false"
    >
      <van-tabbar-item
        name="waitPay"
        icon="card"
        :badge="orderStatus.waitPay || null"
      >
        待支付
      </van-tabbar-item>
      <van-tabbar-item name="paid" icon="bag" :badge="orderStatus.paid || null">
        已支付
      </van-tabbar-item>
      <van-tabbar-item
        name="gotOrder"
        icon="goods-collect"
        :badge="orderStatus.gotOrder || null"
      >
        已接单
      </van-tabbar-item>
      <van-tabbar-item
        name="waitComment"
        icon="checked"
        :badge="orderStatus.waitComment || null"
      >
        待评价
      </van-tabbar-item>
      <van-tabbar-item name="allOrder" icon="balance-list">
        全部订单
      </van-tabbar-item>
    </van-tabbar>
    <van-cell-group title="个人管理">
      <van-cell title="编辑信息" is-link to="/editInfo" />
      <van-cell
        v-if="!userInfo.is_email_active"
        title="激活邮箱"
        @click="clickToShowActive"
      />
      <van-cell title="会员充值" is-link to="/" />
      <van-cell title="修改密码" is-link to="/changePwd" />
      <van-cell title="地址管理" is-link to="/address" />
    </van-cell-group>
    <van-cell-group title="订单管理">
      <van-cell title="我的订单" :value="orderCount" />
      <van-cell title="我的评价" :value="commentCount" />
      <!-- <van-cell title="Demo" value="内容" label="描述信息" /> -->
    </van-cell-group>
    <van-button type="danger" block @click="clickToLogout">
      退出登录
    </van-button>
    <van-tabbar v-model="active" placeholder>
      <van-tabbar-item name="recommend" icon="hot-o" to="/">
        推荐
      </van-tabbar-item>
      <van-tabbar-item
        name="dishes"
        icon="records"
        :dot="localDishCount != dishCount"
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
    <van-dialog
      v-model="showActiveModal"
      title="确认邮箱"
      show-cancel-button
      @confirm="confirmToActive"
    >
      <van-row type="flex" justify="center">
        <span class="dialog-tip-msg">(点击邮箱可编辑)</span>
      </van-row>
      <van-field v-model="email" />
    </van-dialog>
  </div>
</template>
<script>
import { userSendCaptchaAPI, userLogoutAPI } from "../apis/user.apis.js";
import { orderStatusAPI } from "../apis/order.apis";
export default {
  name: "Profile",
  data() {
    return {
      active: "my",
      userInfo: "",
      orderCount: 0,
      commentCount: 0,
      showActiveModal: false,
      email: "",
      cartBadge: localStorage.getItem("cartBadge")
        ? JSON.parse(localStorage.getItem("cartBadge"))
        : null,
      localDishCount: localStorage.getItem("localDishCount"),
      dishCount: this.$store.state.common.dishCount,
      orderActive: null,
      orderStatus: {},
    };
  },
  created() {
    this.userInfo = this.$store.state.common.userInfo;
    this.loadOrderStatus();
  },
  methods: {
    clickToShowActive() {
      this.email = this.userInfo.email;
      this.showActiveModal = !this.showActiveModal;
    },
    confirmToActive() {
      if (this.email) {
        var reg = /^\w+((-\w+)|(\.\w+))*@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/;

        var isEmail = reg.test(this.email);
        if (!isEmail) {
          this.$toast("邮箱格式错误");
        } else {
          var _this = this;
          userSendCaptchaAPI({ email: this.userInfo.email }).then((resp) => {
            if (resp.data.success) {
              _this.$router.push("/auth?email=" + this.email);
            } else if (resp.data.code === 1006) {
              _this.$notify({
                message: "请勿频繁申请验证邮件",
                type: "warning",
              });
            }
          });
        }
      } else {
        this.$toast("邮箱不能为空");
      }
    },
    clickToLogout() {
      userLogoutAPI().then((resp) => {
        if (resp.data.success) {
          this.$notify({
            message: "退出登录",
            type: "success",
            duration: 1000,
          });
        }
        this.$store.dispatch("common/setToken", null);
        this.$store.dispatch("common/setUserInfo", null);
        this.$router.replace("/");
      });
    },
    loadOrderStatus() {
      orderStatusAPI()
        .then((resp) => {
          if (resp.data.success) {
            this.orderStatus = resp.data.data.orderStatus;
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>
<style>
.dialog-tip-msg {
  font-size: 0.6em;
}
</style>