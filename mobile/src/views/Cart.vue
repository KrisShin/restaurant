<template>
  <div id="cart">
    <van-nav-bar title="恰了木有-购物车" @click-right="tt" fixed placeholder>
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
        <van-icon name="search" size="18" @click="tt" />
      </template>
    </van-nav-bar>
    <div>
      <van-card
        num="82"
        price="12.00"
        desc="黑多鱼香, 黑多茄子"
        title="鱼香茄子"
        :thumb="images[3]"
      >
        <template #tags>
          <van-tag plain type="danger">甜辣</van-tag>
          <van-tag plain type="danger">时蔬</van-tag>
        </template>
        <template #footer>
          <van-button size="mini">加入购物车</van-button>
          <van-button size="mini">按钮</van-button>
        </template>
      </van-card>
      <van-card
        num="82"
        price="12.00"
        desc="黑多鱼香, 黑多茄子"
        title="鱼香茄子"
        :thumb="images[3]"
      >
        <template #tags>
          <van-tag plain type="danger">甜辣</van-tag>
          <van-tag plain type="danger">时蔬</van-tag>
        </template>
        <template #footer>
          <van-button size="mini">加入购物车</van-button>
          <van-button size="mini">按钮</van-button>
        </template>
      </van-card>
      <van-card
        num="82"
        price="12.00"
        desc="黑多鱼香, 黑多茄子"
        title="鱼香茄子"
        :thumb="images[3]"
      >
        <template #tags>
          <van-tag plain type="danger">甜辣</van-tag>
          <van-tag plain type="danger">时蔬</van-tag>
        </template>
        <template #footer>
          <van-button size="mini">加入购物车</van-button>
          <!-- <van-button size="mini">按钮</van-button> -->
        </template>
      </van-card>
    </div>
    <van-tabbar v-model="active" placeholder>
      <van-tabbar-item name="recommend" icon="hot-o" to="/">
        推荐
      </van-tabbar-item>
      <van-tabbar-item name="cart" icon="shopping-cart-o" badge="20" to="/cart">
        购物车
      </van-tabbar-item>
      <van-tabbar-item name="my" icon="user-o" badge="20" to="/profile">
        我的
      </van-tabbar-item>
    </van-tabbar>
  </div>
</template>

<script>
export default {
  name: "Cart",
  data() {
    return {
      active: "cart",
      images: [
        this.$BASE_API + "/static/dish/ftq.jpg",
        this.$BASE_API + "/static/dish/hgr.jpg",
        this.$BASE_API + "/static/dish/tds.jpg",
        this.$BASE_API + "/static/dish/yxqz.jpg",
      ],
      userInfo: {},
    };
  },
  created: function () {
    this.userInfo = this.$store.state.common.userInfo;
  },
  methods: {
    tt() {
      // this.$router.push("/tags");
    },
    onSubmit() {},
  },
};
</script>