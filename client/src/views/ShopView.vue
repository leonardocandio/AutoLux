<template>

  <div class="container-shop">
    <div class="filter">
        <FilterForm @filter_func="filter_cars" @delete_func="delete_filter" />
    </div>

    <div class="lista-tienda">
      <CarCard v-for="(car, index) in cars" :key="index"
        :car="car"/>
    </div>

   
  </div>

  <PaginationComp @pagination_func="pagination_cars" :num_of_pages="n_pages" :page="page" ></PaginationComp>
  
</template>
  
<script>
// @ is an alias to /src
import CarCard from '@/components/CarCard.vue'
import FilterForm from '@/components/FilterForm.vue'
import PaginationComp from '@/components/PaginationComp.vue'

export default {
  name: 'ShopView',
  components: {
    CarCard, FilterForm, PaginationComp
  },
  data() {
    return {
      cars: [],
      n_pages: 0,
      page: 1,
      filter_body: {}
    };
  },
  mounted(){
    this.get_all_cars();
  },
  methods: {
    get_all_cars(){
      fetch("/cars?page="+this.page, {method: "GET"})
      .then(response => response.json()).then(data => {
        this.cars = data.cars;
        this.n_pages = parseInt(data.n_pages);
      }).catch(error => {
      console.log(error);
      });
    },
    filter_cars(body){
      if(Object.keys(this.filter_body).length == 0){
        this.page = 1;
      }
      this.filter_body = body;
      fetch("/cars?page="+this.page, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(this.filter_body)
      }).then(response => {
          return response.json()
      }).then(data => {
          let res = JSON.parse(JSON.stringify(data))
          this.cars = res.cars;
          this.n_pages = parseInt(data.n_pages);
      }).catch(error => {
          console.log(error);
      });
    },
    delete_filter(){
      this.page = 1;
      this.filter_body = {};
      fetch("/cars", {method: "GET"})
      .then(response => response.json()).then(data => {
          this.cars = data.cars;
          this.n_pages = parseInt(data.n_pages);
      }).catch(error => {
        console.log(error);
      });
    },
    change_page(){
      if(Object.keys(this.filter_body).length != 0){
        this.filter_cars(this.filter_body);
      } else {
        this.get_all_cars();
      }
    },
    pagination_cars(page){
      this.page = page;
      this.change_page();
    },
  },
  
}
</script>

<style>
.div {
  box-sizing: border-box;
}

.container-shop{
  width: 100%;
  display: flex;
}

.filter {
  min-width: 400px;
}

.cont-shop {
    padding: 0 15px;
    height: 80%;
}

.lista-tienda {
    display: flex;
    flex-wrap: wrap;
    margin: 0;
}

</style>