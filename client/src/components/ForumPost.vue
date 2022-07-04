<template>
  <div class="post">
    <div class="post-header">
      <div class="post-img">
        <img :src="post.author.image_url" alt="profile picture">
      </div>
      <div class="post-title">
        <h2><a href="">{{ post.title }}</a></h2>
        <h4>{{ post.created_at }}</h4>
      </div>
    </div>
    <div class="post-body">
      <a href="/posts/{{ post.id }}">
        <h3>
          {{ post.author.username }}
        </h3>
      </a>
      <p class="post-text">
        {{ post.body }}
      </p>
    </div>
  </div>
</template>


<script>
export default {
  name: "ForumPost",
  data() {
    return {

    };
  },
  props: {
    post: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>
.post {
  background: var(--color-background);
  border-radius: 1.5rem;
  box-shadow: 0 11px 35px 2px rgb(0 0 0 / 14%);
  margin: 20px auto;
  height: 300px;
  width: 70%;
}

.post:hover {
  box-shadow: 0 11px 35px 2px rgba(2, 2, 2, 0.14);
  transition: all 0.5s;
}

.post-header {
  display: flex;
  height: 50%;
  margin: 10px 10px;
}

.post-body {
  margin: 15px 15px;
}

.post-header {
  display: flex;
  height: 50%;
  margin: 10px 10px;
}

.post-img {
  height: 100%;
  padding: 10px 10px;
  margin: 0 10px;
}

.post-img img {
  border-radius: 200px;
  height: 100%;
}

.post-body {
  margin: 15px 15px;
}

.post-body p {
  overflow: hidden;
  white-space: nowrap;
  margin: 5px 0 0 20px;
}

.post-body h3 {
  font-size: 30px;
  margin: 10px 0 0 20px;
}

.post-title {
  height: 100%;
  width: 100%;
  margin: 10px 10px;
}

.post-text {
  text-overflow: ellipsis;
  font-family: 'Lato', sans-serif;
  font-size: 18px;
}
</style>
