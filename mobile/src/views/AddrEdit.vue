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
} from "../apis/address.apis";
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
        if (resp.data.code === 200) {
          const data = resp.data.data;
          this.address = data;
        }else if (resp.data.code==1103){
          this.$toast.fail('地址不存在')
          this.$router.go(-1)
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
        addrEditAPI(val)
          .then((res) => {
            if (res.data.success) {
              this.$router.go(-1);
              this.$toast.success("新增地址成功");
            } else if (res.data.code == 1101) {
              this.$toast.fail("地址数据有误");
            } else if (res.data.code == 1102) {
              this.$toast.fail("地址数据不完整");
            }
          })
          .catch((err) => {
            console.error(err);
          });
      } else {
        addrAddAPI(val)
          .then((res) => {
            if (res.data.success) {
              this.$router.go(-1);
              this.$toast.success("新增地址成功");
            } else if (res.data.code == 1101) {
              this.$toast.fail("地址数据有误");
            } else if (res.data.code == 1102) {
              this.$toast.fail("地址数据不完整");
            }
          })
          .catch((err) => {
            console.error(err);
          });
      }
    },
    onDelete(val) {
      if (val.id == 0) {
        return;
      }
      addrDelAPI(val).then((resp) => {
        if (resp.data.code === 200) {
          this.$router.go(-1);
          this.$toast.success("删除完成");
        } else {
          this.$toast.fail("删除失败");
        }
      });
    },
  },
};
</script>