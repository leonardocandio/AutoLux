<template>
  <AuthForm action="register"/>
</template>

<script>
import AuthForm from "@/components/AuthForm";
export default {
  name: "RegisterView",
  components: {AuthForm}
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
