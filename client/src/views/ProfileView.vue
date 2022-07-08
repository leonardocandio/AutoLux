<template>
  <div class="profile-container">
    <UserProfile :user="user" v-if="user"/>

  </div>
</template>

<script>
import UserProfile from "@/components/UserProfile";


export default {

  data() {
    return {
      user: null
    };

  },
  name: "ProfileView",
  components: {UserProfile},
  beforeRouteEnter(to, from, next) {
    fetch(`/users/${to.params.id}`, {method: "GET"})
        .then(response => response.json())
        .then(res => {
          next(vm => vm.setData(res.user))
        })
        .catch(error => {
          console.log(error);
        });
  },
  methods: {
    setData(data) {
      this.user = data;
    }
  }
}


</script>

<style scoped>
.profile-container {
  margin: 10%;
  display: flex;
  flex-direction: column;
    text-align: center;
}

</style>
