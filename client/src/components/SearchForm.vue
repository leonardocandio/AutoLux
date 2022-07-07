<template>

    <div class="input-group flex-nowrap search-input">
        <span class="input-group-text" id="addon-wrapping">Buscar</span>
        <input v-model="message" id="search" type="text" class="form-control" placeholder="Encuentra tu carro">
    </div>

    <ul class="search-content">
        <li class="search-item" v-for="(car, index) in cars" :key="index">
            <a class="item-box" href="#">
                <img class="image" :src="car.image_url" :alt="car.name">
                <router-link :to="{name: 'car-details', params: {id:car.id}}">
                    <p class="name">{{ car.name }}</p>
                </router-link>
                
            </a>
            <hr>
        </li>
    </ul>

</template>


<script>
export default {
  name: 'SearchForm',
  data(){
    return {
        message: '',
        cars: []
    }
  },

  updated(){
    if(this.message != ''){
        fetch("/cars?search="+this.message+"&nitems=4", {method: "POST"})
        .then(response => response.json()).then(data => {
            this.cars = data.cars;
        }).catch(error => {
            console.log(error);
        });
    } else {
        this.cars = []; 
    }
  }
}
</script>


<style scoped>
    .search-input {
        width: 400px;
    }

    .search-content {
        z-index: 1000;
        width: 400px;
        margin: 0;
        position: absolute;
        background-color: #ffffff;
        border: 1px solid gray;
        padding: 0;
    }

    .image {
        width: 200px;
        padding: 0;
    }

    .item-box {
        display: flex;
    }

    .search-item {
    }

    .name {
        padding-top: 10px;
        font-weight: bold;
        padding: 40px 30px 10px 30px;
    }
</style>