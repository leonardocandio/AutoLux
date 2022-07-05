<template>
  <div class="comment-box">
    <FormKit>

    </FormKit>
    <div class="comment-container">
      <ul class="comments">
        <CommentBubble v-for="(comment, index) in post.comments" :comment="comment" :key="index"/>
      </ul>
    </div>
  </div>
</template>

<script>
import CommentBubble from "@/components/CommentBubble";

export default {
  name: "CommentBox",
  components: {CommentBubble},
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
.comment-box {
  display: flex;
  flex-direction: column;
  width: 50%;
  align-items: center;
}
.comment-container {
  width: 650px;
  overflow: auto;
}
.comments {
  display: flex;
  flex-direction: column;
}
</style>
