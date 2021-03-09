<template>
  <div id="addressEdit">
    <van-nav-bar
      title="恰了木有-地址管理"
      @click-left="onClickReturn"
      left-arrow
      fixed
      placeholder
    />
    <div>
      <van-address-edit
        :area-list="areaList"
        show-delete
        show-set-default
        show-search-result
        :address-info="address"
        @save="onSave"
        @delete="onDelete"
      />
    </div>
  </div>
</template>
<script>
import {
  addrDelAPI,
  addrEditAPI,
  addrAddAPI,
  addrGetAPI,
} from "../apis/address.api";
import areaList from "../assets/Aera.ts";
export default {
  name: "AddrEdit",
  data() {
    return {
      areaList,
      addr: null,
      address: {
        id: 0,
        name: "",
        tel: "",
        addressDetail: "",
        areaCode: "",
        isDefault: false,
      },
      isEdit: false,
    };
  },
  created() {
    this.isEdit = this.$route.query.id ? true : false;
    if (this.isEdit) {
      addrGetAPI({ id: this.$route.query.id }).then((resp) => {
        if (resp.data.success) {
          const data = resp.data.data;
          console.log(data);
        }
      });
    }
  },
  methods: {
    onClickReturn() {
      this.$router.go(-1);
    },
    onSave(val) {
      if (this.isEdit) {
        addrEditAPI(val);
      } else {
        addrAddAPI(val);
      }
    },
    onDelete(val) {
      console.log(val);
      addrDelAPI(val).then((resp) => {
        if (resp.data.success) {
          console.log(resp.data.data);
          this.$toast.success("删除完成");
        }
      });
    },
  },
};
</script>