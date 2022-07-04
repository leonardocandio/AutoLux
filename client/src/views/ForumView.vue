<template>
  <div class="header">
    <h1>
      Todas las publicaciones
    </h1>
  </div>
  <div class="content">
    <ForumPost v-for="(post, index) in posts"
               :key="index"
               :post="post"
    />
  </div>
</template>

<script>
import ForumPost from "@/components/ForumPost";

export default {
  name: "ForumView",
  components: {ForumPost},
  data() {
    return {
      posts: []
    };
  },
  mounted() {
    fetch("/posts/", {method: "GET"})
        .then(response => response.json()).then(data => (this.posts = data.posts)).then(function () {
      console.log(this.posts)
    }).catch(error => {
      console.log(error);
    });
  }
}

</script>

<style scoped>

.header {
  height: 100px;
  width: 85%;
  align-items: center;
  margin: 20px 50px;
}

</style>

