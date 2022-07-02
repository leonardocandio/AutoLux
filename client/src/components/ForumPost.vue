<template>
  <div class="post">
    <div class="post-header"> aaaa</div>
    <div class="post-body"> bbbb</div>
  </div>
</template>

<script>
export default {
  name: "ForumPost",
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

.post-header{
  display: flex;
  height: 50%;
  margin: 10px 10px;
}
.post-body{
  margin: 15px 15px;
}
</style>
