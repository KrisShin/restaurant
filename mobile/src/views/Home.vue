<template>
  <div id="home">
    {{ a }}
    <van-button @click="test_get">get</van-button>
    <van-button @click="test_post">post</van-button>
    <van-button @click="test_put">put</van-button>
    <van-button @click="test_del">del</van-button>
    <img src="http://127.0.0.1:9096/static/avatar/default.jpg">
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
import { getAPI, postAPI, putAPI, delAPI } from "../apis/user.apis";

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
    test_get: function () {
      getAPI({ test: 123 })
        .then((resp) => {
          console.log(resp);
        })
        .catch((resp) => {
          console.error(resp);
        });
    },
    test_post: function () {
      postAPI({ test: 123 })
        .then((resp) => {
          console.log(resp);
        })
        .catch((resp) => {
          console.error(resp);
        });
    },
    test_put: function () {
      putAPI({ test: 123 })
        .then((resp) => {
          console.log(resp);
        })
        .catch((resp) => {
          console.error(resp);
        });
    },
    test_del: function () {
      delAPI({ test: 123 })
        .then((resp) => {
          console.log(resp);
        })
        .catch((resp) => {
          console.error(resp);
        });
    },
  },
};
</script>
