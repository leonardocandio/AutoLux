<template>
<AuthForm :authRoute="authRoute" v-if="authRoute"/>
</template>

<script>
import AuthForm from "@/components/AuthForm";
import router from "@/router";
export default {
  data(){
    return {
      authRoute: null
    }
  },

  name: "LoginView",
  components: {AuthForm},
  beforeRouteEnter(to, from, next) {
    next(vm => vm.setData(router.currentRoute))
  },
  methods: {
    setData(data) {
      this.authRoute = data;
    }
  }
}
</script>

<style>
.form-control {
  width: 76%;
  color: darkgrey;
  font-weight: 700;
  font-size: 14px;
  letter-spacing: 1px;
  background: lightgrey;
  padding: 10px 20px;
  border-radius: 20px;
  outline: none;
  box-sizing: border-box;
  border: 2px solid lightgrey;
  margin-left: 46px;
  text-align: center;
  margin-bottom: 27px;
}

.form-control:focus {
  border: 2px solid var(--color-accent);
}
</style>
