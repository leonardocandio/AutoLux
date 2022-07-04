<template>


    <div class="lista-tienda">
      <CarCard v-for="(car, index) in cars" :key="index"
        v-bind:car="car"/>
    </div>

    
</template>
  
<script>
// @ is an alias to /src
import CarCard from '@/components/CarCard.vue'

export default {
  name: 'ShopView',
  components: {
    CarCard
  },
  data() {
    return {
      cars: []
    };
  },
  mounted(){
    fetch("/cars", {method: "GET"})
        .then(response => response.json()).then(data => (this.cars = data.cars)).then(function () {
      console.log(this.cars)
    }).catch(error => {
      console.log(error);
    });
  }
}
</script>

<style>
.div {
  box-sizing: border-box;
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