<template>
  <div class="profile-posts">
    <ul>
      <li v-for="(post, index) in posts" :key="index">
        <router-link to="forum-detail" :params="{id: post.id}"/>
          <h3>{{ post.title }}</h3>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "UserPosts",
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
.profile-posts {
  border: 2px solid lightgrey;
  text-align: center;
  /* width: 40%; */
  padding: 2em;
  border-radius: 10px;
}

</style>
