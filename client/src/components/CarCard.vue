<template>
    <div class="cars-shop">
        <img class="card-img-top" :src="car.image_url" :alt="car.name">

        <div class="card-body-shop">
            <h3 class="card-title">{{ car.name }}</h3>
            <p class="card-text">
                {{  car.price }} $
            </p>
            <a :href="car.id" class="btn-shop btn-primary">Ver más</a>
        </div>
    </div>
</template>

<script>
export default {
  name: 'CarCard',
  props: {
    car: {
      type: Object,
      required: true,
      default: () => ({})
    }
  }
}
</script>


<style scoped>
.cars-shop:hover {
box-shadow: 0 11px 35px 2px rgba(2, 2, 2, 0.14);
transition: all 0.5s;
}

.cars-shop > img:hover {
    filter:saturate(2);
    transition: all 0.5s;
}

.cars-shop {
    width: 500px;
    height: 250px;
    margin: 5px;
    display: flex;
    border: 2px solid #e1e1e1;
    padding: 10px 10px;
}

.cars-shop img {
    height: 100%;
    width: 50%;
}

.card-body-shop {
    display: table-cell;
    position: relative;
    vertical-align: middle;
    width: 50%;
    margin: 5px 5px 5px 5px;
    text-align: center;
    padding: 0;
}

.card-body-shop h3 {
    margin: 5px 5px;
    font-size: 100%;
    font-family: 'Share Tech Mono', monospace;
}
</style>
