<template>
    <div class="container">
        <nav>
        <ul class="pagination">
            <li id="pageDown" @click="pageDown" class="page-item"><button class="page-link">Anterior</button></li>
            <li class="page-link" style="padding-top: 10px;">{{ page }} de {{ num_of_pages }}</li>
            <li id="pageUp" @click="pageUp" class="page-item"><button class="page-link">Siguiente</button></li>
        </ul>
        </nav>
    </div>

</template>


<script>
export default {
  name: "PaginationComp",
  props: {
    num_of_pages: Number,
    page: Number,
  },
  data(){
    return {
        num_page: 1
    }
  },
  methods: {
    pagination_func(){
        this.$emit("pagination_func", this.num_page);
    },
    pageUp(){
        if(this.num_page >=this.num_of_pages){
            this.num_page = this.num_of_pages;
        } else {
            this.num_page++;
            this.pagination_func();
        }
    },
    pageDown(){
        if(this.num_page <= 1){
            this.num_page = 1;
        } else {
            this.num_page--;
            this.pagination_func();
        }
    },
    
  }
}
</script>

<style scoped>
.container {
    width: 100%;
    display: block;
    margin-top: 20px;
}

nav {
    width: 500px;
    margin: auto;
}

.pagination {
    max-width: 100%;
    vertical-align: middle;
    justify-content:center;
    justify-content: center;
    overflow: hidden;
}

.page-item {

}

</style>
