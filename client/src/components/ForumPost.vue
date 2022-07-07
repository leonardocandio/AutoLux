<template>
  <div class="post">
    <div class="post-img">
      <img :src="post.author.image_url" alt="profile picture">
    </div>
    <div class="post-title">
      <h2>
        <router-link :to="{name: 'post-details', params: {id:post.id}}">
          {{ post.title }}
        </router-link>
      </h2>
    </div>
    <div class="post-date">
      <h4>{{ post.created_at }}</h4>
    </div>
    <div class="post-author">
      <router-link :to="{name: 'profile', params: {id:post.author.id}}">
        {{ post.author.username }}
      </router-link>
    </div>
    <div class="post-body">
      <p>
        {{ post.body }}
      </p>
    </div>
  </div>
</template>


<script>
export default {
  name: "ForumPost",
  data() {
    return {};
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
  width: 100%;
  border-radius: 1.5rem;
  box-shadow: 0 6px 20px 2px rgb(0 0 0 / 14%);
  height: 13em;
  margin: 1%;
  display: grid;
  grid-gap: 1em;
  grid-row-gap: 0.6em;
  grid-template-columns: 16% 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr;
  grid-template-areas: "photo title title date"
                        "photo body body body"
                        "author body body body";
}

.post:hover {
  box-shadow: 0 15px 35px 5px rgba(3, 3, 3, 0.14);
  transition: all 0.5s;
}

.post-img {
  grid-area: photo;
  display: flex;
  justify-content: center;
  align-items: center;
}

.post-body {
  grid-area: body;
  display: flex;
}

.post-title {
  grid-area: title;
  height: 100%;
  width: 100%;
}

.post-date {
  display: flex;
  justify-content: center;
  align-items: center;

  grid-area: date;
  margin: 2%;
}

.post-author {
  grid-area: author;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  font-size: 1.3em;
}

.post-body p {
  padding: 0 1% 3%;
  font-size: 1.25em;
  display: inline;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  word-wrap: break-word;
  overflow: hidden;
}

.post-img img {
  padding-top: 5%;
  padding-bottom: 5%;
  max-width: 90%;
  max-height: 90%;
  border-radius: 50%;
}

.post-title h2 {
  font-size: 40px;
  margin: 1%;
}

.post-date h4 {
  color: #a7a5a5;
  font-size: 0.8em;
}

</style>
