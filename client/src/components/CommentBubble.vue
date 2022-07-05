<template>
  <li class="comment">
    <img :src="comment.author.image_url"
         alt="comment-author"
         class="comment-img">
    <span class="comment-author">
      <router-link to="">
        {{ comment.author.username }}
      </router-link>
    </span>
    <span class="comment-date">
      {{ comment.created_at }}
    </span>
    <span class="comment-body">
      {{ comment.body }}
    </span>
  </li>
</template>

<script>
export default {
  name: "CommentBubble",
  props: {
    comment: {
      type: Object,
      required: true,
      default: () => ({})
    }
  },
}
</script>

<style scoped>
.comment {
  display: grid;
  align-self: center;
  width: 70%;
  grid-template-columns: max-content auto auto;
  grid-template-rows: 30px auto;
  grid-template-areas: "pic a time" "pic b b";
  background: var(--color-background);
  border-radius: 1.5em;
  box-shadow: 0 11px 35px 2px rgba(0, 0, 0, 0.14);
  margin: 2%;
}
.comment-img {
  grid-area: pic;
  border-radius: 50%;
  height: 50px;
  width: 50px;
  margin: 10px;
  align-self: start;
  justify-self: center;
}

.comment-author {
  grid-area: a;
  width: auto;
  height: 10%;
  margin: 15px 10px 20px;
}

.comment-date {
  grid-area: time;
  color: #a7a5a5;
  width: auto;
  margin: 15px 0 20px 10px;
}

.comment-body {
  grid-area: b;
  width: 87%;
  margin: 10px 0 20px 10px;
  text-align: justify;
}
</style>
