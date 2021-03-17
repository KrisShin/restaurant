<template>
  <div id="dishDetail">
    <van-nav-bar
      title="恰了木有-菜品"
      @click-left="onClickReturn"
      left-arrow
      fixed
      placeholder
    />
    <div>
      <van-swipe :autoplay="3000" height="200">
        <van-swipe-item v-for="(img, index) in images" :key="index">
          <img class="dish-swipe-img" v-lazy="img" />
        </van-swipe-item>
      </van-swipe>
      <div class="dish-desc-content">
        <van-row>
          <span class="dish-name-text">{{ dish.name }}</span>
        </van-row>
        <van-row>
          <span class="dish-desc-text">{{ dish.description }}</span>
        </van-row>
        <van-row>
          <van-tag
            v-for="(tag, index) in dish.tags"
            :key="index"
            :color="tag.color"
            round
            size="medium"
            class="dish-tag"
            plain
          >
            {{ tag.name }}
          </van-tag>
        </van-row>
        <van-row type="flex" justify="space-between">
          <van-col class="dish-price-text">
            现价: {{ (dish.price * dish.discount) | numFilter }}
          </van-col>
          <van-col>
            <span class="dish-amount-text">销量{{ dish.amount }}</span>
          </van-col>
          <van-col v-if="dish.discount_desc">
            <van-tag type="danger" size="medium">
              {{ dish.discount_desc }}
            </van-tag>
          </van-col>
          <van-col class="dish-amount-text text-line-through">
            原价: {{ dish.price | numFilter }}
          </van-col>
        </van-row>
        <van-row>客户评价:</van-row>
      </div>
    </div>
    <van-goods-action>
      <van-goods-action-icon
        :badge="cartBadge"
        icon="cart-o"
        text="购物车"
        to="/cart"
      />
      <van-goods-action-icon
        :icon="isStar ? 'star' : 'star-o'"
        text="收藏"
        @click="onClickStar"
      />
      <van-goods-action-button
        type="danger"
        text="加入购物车"
        @click="onClickButton"
      />
    </van-goods-action>
  </div>
</template>
<script>
import { dishCartAPI } from "../apis/dish.apis";
export default {
  name: "DishDetail",
  data() {
    return {
      isStar: false,
      images: [],
      dish: {},
      cartBadge: localStorage.getItem("cartBadge")
        ? JSON.parse(localStorage.getItem("cartBadge"))
        : null,
      cart: {},
      dish_id: 0,
    };
  },
  filters: {
    numFilter(value) {
      let realVal = Number(value).toFixed(2);
      return Number(realVal);
    },
  },
  created() {
    var dish_id = this.$route.query.dish;
    this.cart = JSON.parse(localStorage.getItem("cart"));
    dishCartAPI({ dishes: [dish_id] })
      .then((resp) => {
        if (resp.data.success) {
          this.dish = resp.data.data[0];
          this.dish.images.forEach((img) => {
            this.images.push(img.uri);
          });
          this.images.push(this.dish.index_img);
        }
      })
      .catch((err) => {
        console.error(err);
      });
  },
  beforeRouteLeave(to, form, next) {
    localStorage.setItem("cart", JSON.stringify(this.cart));
    localStorage.setItem("cartBadge", JSON.stringify(this.cartBadge));
    next();
  },
  methods: {
    onClickReturn() {
      this.$router.go(-1);
    },
    onClickStar() {
      this.isStar = !this.isStar;
      if (this.isStar) {
        this.$toast("收藏成功");
      } else {
        this.$toast("取消收藏");
      }
    },
    onClickButton() {
      this.cart[this.dish.id] += 1;
      this.cartBadge += 1;
    },
  },
};
</script>
<style>
#dishDetail {
  background: rgb(238, 243, 248);
}
.dish-swipe-img {
  width: 100%;
  max-height: 12em;
}
.dish-name-text {
  margin: 0 0 0.2rem 0;
  font-size: 1.5rem;
}
.dish-desc-text {
  margin: 0 0 0.2rem 0;
  font-size: 1rem;
}
.dish-amount-text {
  margin: 0 0 0.2rem 0;
  font-size: 0.8rem;
  color: gray;
}
.dish-desc-content {
  padding: 0 0.4rem 0 0.4rem;
}
.text-line-through {
  text-decoration: line-through;
}
.dish-tag {
  margin: 0.1rem;
}
.dish-price-text {
  margin: 0.2rem 0 0.1rem 0;
  font-size: 1.2rem;
  color: red;
  font-weight: 600;
}
</style>