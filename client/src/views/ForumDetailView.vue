<template>
  <div class="detail-container">
    <ForumPostDetail :post="post" v-if="post"/>
    <CommentBox :post="post" v-if="post"/>
  </div>
</template>

<script>
import ForumPostDetail from "@/components/ForumPostDetail";
import CommentBox from "@/components/CommentBox";

export default {
  data() {
    return {
      post: null
    };
  },
  name: "ForumDetailView",
  components: {CommentBox, ForumPostDetail},
  props: {
    id: {
      type: String,
      default: null
    }
  },
  beforeRouteEnter(to, from, next){
    fetch(`/posts/${to.params.id}`, {method: "GET"})
        .then(response => response.json())
        .then(res => {
          next(vm => vm.setData(res.post))
        })
        .catch(error => {
          console.log(error);
        });
  },
  methods: {
    setData(data) {
      this.post = data;
    }
  }
}
</script>

<style scoped>
.detail-container {
  display: flex;
  flex-direction: row;
  width: 100%;
}
@media (max-width: 768px) {
  .detail-container {
    flex-direction: column;
    align-items: center;
  }
}
</style>
