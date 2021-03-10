<template>
  <div id="cart">
    <van-nav-bar title="恰了木有-购物车" @click-right="tt" fixed placeholder>
      <template #right>
        <van-icon name="search" size="18" @click="tt" />
      </template>
    </van-nav-bar>
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
    };
  },
  methods: {
    tt() {
      // this.$router.push("/tags");
    },
    onSubmit() {},
  },
};
</script>