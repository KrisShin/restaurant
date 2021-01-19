<template>
  <div id="home">
    {{ a }}
    <van-button @click="hello">123</van-button>
    <div v-if="a">
      <router-link to="/login">login</router-link> /
      <router-link to="/register">register</router-link>
    </div>
    <div v-else>
      <van-row type="flex">
        <van-col span="6">span: 6</van-col>
        <van-col span="6">span: 6</van-col>
        <van-col span="6">span: 6</van-col>
      </van-row>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import { Button, Col, Row } from "vant";

export default {
  name: "Home",
  data: function () {
    return {
      a: true,
    };
  },
  components: {
    [Button.name]: Button,
    [Row.name]: Row,
    [Col.name]: Col,
  },
  methods: {
    hello: function () {
      this.a = !this.a;
    },
  },
};
</script>
