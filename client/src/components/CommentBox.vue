<template>
  <div class="comment-box">
    <div class="comment-container">
      <div class="comment-form">
        <FormKit
            :actions="false"
            type="form"
            id="comment-form"
            @submit="submitComment"
            validation-visibility="submit"
        >
          <FormKit
              type="text"
              name="comment"
              placeholder="Escribe un comentario"
              validation="required|length:3,1000"
              input-class="$reset form-control"
              v-model="comment"
          />
          <FormKit
              type="submit"
              label="Comentar"
              input-class="$reset btn btn-submit"
          />
        </FormKit>
      </div>
      <ul class="comments">
        <CommentBubble v-for="(comment, index) in comments" :comment="comment" :key="index"/>
      </ul>
    </div>
  </div>
</template>

<script>
import CommentBubble from "@/components/CommentBubble";

export default {
  data() {
    return {
      comment: '',
      res: {},
      comments: this.post.comments
    }
  },
  name: "CommentBox",
  components: {CommentBubble},
  props: {
    post: {
      type: Object,
      required: true,
      default: () => ({})
    }
  },
  methods: {
    async submitComment() {
      console.log("submitComment: " + this.comment);
      fetch(`/posts/${this.$route.params.id}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          'comment_body': this.comment,
          'post_id': this.post.id
        })
      }).then(response => response.json())
          .then(res => {
            this.res = res;
            if (this.res.code === 200) {
              this.comments = this.res.comments;
            }
          });
    }
  }
}
</script>

<style scoped>
.comment-box {
  display: block;
  flex-direction: column;
  width: 80%;
  align-items: flex-start;
  overflow-y: scroll;
  height: 85vh;
}

.comment-container {
  overflow-y: scroll;
}

.comments {
  display: flex;
  flex-direction: column-reverse;
}

.formkit-wrapper{
  margin: 10px 0;
}
</style>
