<template>
  <div class="post-container">
    <div class="post">
      <div class="post-title">
        {{ post.title }}
      </div>
      <div class="post-author-image">
        <img :src="post.author.image_url" alt="profile picture">
      </div>
      <div class="post-author">
        <router-link to="">
          {{ post.author.username }}
        </router-link>
      </div>
      <div class="post-created-at">
        {{ post.created_at }}
      </div>
      <div class="post-body">
        {{ post.body }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ForumPostDetail",
  props: {
    post: {
      type: Object,
      required: true,
      default: () => ({})
    }
  }
}
</script>

<style scoped>
.post {
  margin: 2%;
  display: grid;
  width: 600px;
  align-items: center;
  background: var(--color-background);
  box-shadow: 0 11px 35px 2px rgba(0, 0, 0, 0.14);
  border-radius: 1.5em;
  grid-gap: 10px;
  grid-template-columns: auto auto auto 1fr;
  grid-template-rows: 15% auto 1fr;
  grid-template-areas: "title title title title"
                        "photo author date . "
                        "body body body body";
}
.post-container{
  width: 50%;
  display: flex;
  justify-content: center;
}
.post-title {
  text-align: center;
  grid-area: title;
  color: var(--color-accent);
  font-size: 300%;
}

.post-author-image {
  padding-left: 30px;
  grid-area: photo;
}

.post-author-image img {
  width: 40px;
  height: auto;
  border-radius: 50%
}

.post-created-at {
  grid-area: date;
  color: #a7a5a5;
}

.post-body {
  overflow: scroll;
  height: 400px;
  text-align: justify;
  margin: 5% 30px;
  grid-area: body;
  align-self: start;
}

.post-author {
  text-align: left;
  grid-area: author;
}

</style>
