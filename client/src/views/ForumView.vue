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
      <PaginationComp @pagination_func="pagination_posts" :num_of_pages="n_pages" :page="page"/>
    </div>
  </div>
</template>

<script>
import ForumPost from "@/components/ForumPost";
import PaginationComp from "@/components/PaginationComp";

export default {
  name: "ForumView",
  components: {PaginationComp, ForumPost},
  data() {
    return {
      posts: [],
      n_pages: 0,
      page: 1,
    };
  },
  mounted() {
    this.get_all_posts();
  },
  methods: {
    get_all_posts() {
      fetch(`/posts?page=${this.page}`, {method: "GET"})
          .then(response => response.json())
          .then(res => {
            this.posts = res.posts;
            this.n_pages = parseInt(res.n_pages);
          })
          .catch(error => {
            console.log(error);
          });
    },
    setData(data) {
      this.posts = data;
    },
    pagination_posts(page) {
      this.page = page;
      this.get_all_posts();
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

