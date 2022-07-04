<template>
<div>
  <ForumDetail/>
  <CommentBox/>
</div>
</template>

<script>
import ForumDetail from "@/components/ForumDetail";
import CommentBox from "@/components/CommentBox";
export default {
  name: "ForumDetailView",
  components: {CommentBox, ForumDetail}
}
</script>

<style scoped>

</style>
