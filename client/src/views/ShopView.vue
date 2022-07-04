<template>
    
    <div class="container-shop">
      <div class="filter">
        <FilterForm/>
      </div>
         
      <div class="lista-tienda">
        <CarCard v-for="(car, index) in cars" :key="index"
          v-bind:car="car"/>
      </div>
    </div>

    
    <PaginationComp></PaginationComp>
    
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
      page: 5
    };
  },
  mounted(){
    fetch("/cars", {method: "GET"})
        .then(response => response.json()).then(data => (this.cars = data.cars)).then(function () {
      console.log(this.cars)
    }).catch(error => {
      console.log(error);
    });
  },
  methods: {

  }
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

.cont-shop {
    padding: 0 15px;
    height: 80%;
}

.filter {
  min-width: 400px;
}

.lista-tienda {
    width: auto;
    display: flex;
    flex-wrap: wrap;
    margin: 0;
}

</style>