<template>
  <div id="addrComp">
    <van-row>
      <van-col v-if="switchable">
        <van-checkbox :name="addr.id"></van-checkbox>
      </van-col>
      <van-col>
        <van-row>
          {{ addr.name }} {{ addr.tel }}
          <van-tag v-if="addr.isDefault" type="danger" round>默认</van-tag>
        </van-row>
        <van-row class="addr-address">
          {{ addr.address }}
        </van-row>
      </van-col>
    </van-row>
  </div>
</template>
<script>
export default {
  name: "AddrComp",
  props: {
    addr: Object,
    switchable: Boolean(false),
  },
};
</script>

<style scoped>
#addrComp {
  padding: 0 0.5rem 0 0.5rem;
}
.addr-address {
  font-size: 0.8rem;
}
</style>