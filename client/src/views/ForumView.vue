<template>
  <div class="forum">
    <div class="forum-container">
      <div class="forum-header">
        <span class="forum-title">
        Todas las publicaciones
        </span>
        <span class="forum-new">
        <router-link :to="{name:'new-post'}">
          <button class="btn btn-primary">
            Crear nueva publicación
          </button>
        </router-link>
        </span>
      </div>
      <div class="content">
        <ForumPost v-for="(post, index) in posts"
                   :key="index"
                   :post="post"
        />
      </div>
    </div>
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
  beforeRouteEnter(to, from, next) {
    fetch('/posts/', {method: "GET"})
        .then(response => response.json())
        .then(res => {
          next(vm => vm.setData(res.posts))
        })
        .catch(error => {
          console.log(error);
        });
  },
  methods: {
    setData(data) {
      this.posts = data;
    }
  }
}

</script>

<style scoped>
.forum-container {
  display: flex;
  flex-direction: column;
  width: 60%;
  margin: auto;
}
.content {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%;
}


.forum {
  margin: auto;
}

.forum-header {
  display: flex;
  justify-content: space-between;
  align-items: center;

}
.forum-new {
  width: fit-content;
}

.forum-title {
  font-size: 2.5em;
  font-weight: bold;
}
</style>

