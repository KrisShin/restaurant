<template>
  <div id="addrComp">
    <div v-if="switchable" class="border-none">
      <van-radio :name="addr.id">
        <van-row gutter="20">
          <van-col>姓名: {{ addr.name }}</van-col>
          <van-col>电话: {{ addr.tel }}</van-col>
          <van-col>
            <van-tag v-if="addr.isDefault" type="danger" round>默认</van-tag>
          </van-col>
        </van-row>
        <van-row gutter="3">
          <van-col> 地址:</van-col>
          <van-col class="addr-address">
            {{ addr.address }}
          </van-col>
        </van-row>
      </van-radio>
    </div>
    <div v-else class="border-dashed">
      <van-row gutter="20">
        <van-col>姓名: {{ addr.name }}</van-col>
        <van-col>电话: {{ addr.tel }}</van-col>
        <van-col>
          <van-tag v-if="addr.isDefault" type="danger" round>默认</van-tag>
        </van-col>
      </van-row>
      <van-row gutter="3">
        <van-col> 地址:</van-col>
        <van-col class="addr-address">
          {{ addr.address }}
        </van-col>
      </van-row>
    </div>
  </div>
</template>
<script>
export default {
  name: "AddrComp",
  props: {
    addr: Object,
    switchable: Boolean,
    is_border: Boolean,
  },
};
</script>

<style scoped>
.border-none {
  border-bottom: solid;
  border-width: 0.1rem;
  padding: 0.2rem 0 0.3rem 0;
}
.border-dashed {
  border: dashed;
  border-width: 0.1rem;
  padding: 0.2rem 0 0.3rem 0;
}
.addr-address {
  height: 100%;
}
.addr-address {
  max-width: 89%;
}
</style>