<template>
  <div class="profile">
    <img :src="user.image_url" alt="profile picture">
  </div>
  <p class="profile-username">{{ user.username }}</p>
  <p class="profile-email"> {{ user.email }} </p>

</template>

<script>
export default {
  name: "UserProfile",
  props: {
    user: {
      type: Object,
      required: true,
      default: () => ({})
    }
  }
}
</script>

<style scoped>
.profile {
  text-align: center;
  width: 50%;
  display: inline;
}

.profile img {
  border-radius: 100%;
  box-shadow: 0 0 10px;
  width: 400px;
  height: 400px;
}
.profile-username {
  font-size: 40px;
  margin-top: 0em;
}

.profile-email {
  margin-top: -1em;
  font-size: 20px;
}
</style>
