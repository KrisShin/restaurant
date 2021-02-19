<template>
  <div id="profile">
    <van-nav-bar title="恰了木有-我的" />
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
      <span></span>
    </div>
    <van-cell-group title="个人管理">
      <van-cell title="编辑信息" is-link to="/" />
      <van-cell
        v-if="!userInfo.is_email_active"
        title="激活邮箱"
        @click="clickToShowActive"
      >
        <van-action-sheet
          v-model="showActiveModal"
          :actions="actions"
          cancel-text="取消"
          close-on-click-action
          @select="clickToActive"
          @cancel="clickToShowActive"
        />
      </van-cell>
      <van-cell title="会员充值" is-link to="/" />
    </van-cell-group>
    <van-cell-group title="订单管理">
      <van-cell title="我的订单" :value="orderCount" />
      <van-cell title="我的评价" :value="commentCount" />
      <van-cell title="Demo" value="内容" label="描述信息" />
    </van-cell-group>
    <van-tabbar v-model="active">
      <van-tabbar-item name="recommend" icon="hot-o" to="/">
        推荐
      </van-tabbar-item>
      <van-tabbar-item name="cart" icon="shopping-cart-o" badge="20">
        购物车
      </van-tabbar-item>
      <van-tabbar-item name="my" icon="user-o" badge="20" to="/profile">
        我的
      </van-tabbar-item>
    </van-tabbar>
  </div>
</template>
<script>
import { userSendCaptchaAPI } from "../apis/user.apis.js";
export default {
  name: "Profile",
  data() {
    return {
      active: "my",
      userInfo: "",
      orderCount: 0,
      commentCount: 0,
      showActiveModal: false,
      actions: [{ name: "确认激活" }],
    };
  },
  created: function () {
    this.userInfo = this.$store.state.common.userInfo;
  },
  methods: {
    clickToShowActive() {
      // console.log("123");
      this.actions[0].subname = this.userInfo.email;
      this.showActiveModal = !this.showActiveModal;
    },
    clickToActive() {
      userSendCaptchaAPI()
      this.$router.push("/auth");
    },
  },
};
</script>