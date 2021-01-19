<template>
  <div id="home">
    {{ a }}
    <Button @click="hello">123</Button>
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
import { Button } from "vant";
import { Col, Row } from "vant";

export default {
  name: "Home",
  data: function () {
    return {
      a: true,
    };
  },
  components: {
    Button,
    Col,
    Row,
  },
  methods: {
    hello: function () {
      this.a = !this.a;
    },
  },
};
</script>
