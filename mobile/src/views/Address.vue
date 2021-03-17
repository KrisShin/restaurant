<template>
  <div id="address">
    <van-nav-bar
      title="恰了木有-地址管理"
      @click-left="onClickReturn"
      left-arrow
      fixed
      placeholder
    />
    <div>
      <van-address-list
        v-model="chosenAddressId"
        :list="list"
        :switchable="false"
        default-tag-text="默认"
        @add="onAdd"
        @edit="onEdit"
      />
    </div>
  </div>
</template>
<script>
import { addrListAPI } from "../apis/address.api";
export default {
  name: "Address",
  data() {
    return {
      chosenAddressId: "1",
      list: [],
    };
  },
  created() {
    addrListAPI()
      .then((res) => {
        if (res.data.success) {
          this.list = res.data.data.addresses;
        }
      })
      .catch((err) => {
        console.error(err);
      });
  },
  methods: {
    onClickReturn() {
      this.$router.go(-1);
    },
    onAdd() {
      this.$router.push("/addrEdit?id=");
    },
    onEdit(item) {
      this.$router.push("/addrEdit?id=" + item.id);
    },
  },
};
</script>