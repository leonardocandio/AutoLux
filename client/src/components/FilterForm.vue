<template>
    
    <div style="width: 20%" class="filter-container">
        <div class="filter-content">
            <p class="filter-title">Filtros</p>
            <ul>
                <form id="filter-form" method="GET">
                    <li class="filter">
                        <label>Rango de precios</label>
                        <div style="display:flex;">
                            <input name="start_price_filter" v-model="start_price" placeholder="Desde" type="number" step="1000"  max="100000" class="form-control" style="width: 50%; margin-left: 0px;">

                            <input name="end_price_filter" v-model="end_price" placeholder="Hasta" type="number" step="1000" max="100000" class="form-control" style="width: 50%; margin-left: 0px;">
                        </div>
                    </li>

                    <li class="filter">
                        <label for="model_filter">Modelo del carro</label><br>
                        <input name="model_filter" v-model="model" type="text" class="form-control" style="width: 50%; margin-left: 0px;" placeholder="Buscar">
                    </li>

                    <li class="filter">
                        <label for="brand_filter">Marca del carro</label><br>
                        <input name="brand_filter" v-model="brand" type="text" class="form-control" style="width: 50%; margin-left: 0px;" placeholder="Buscar">
                    </li>

                    <li class="filter">
                        <label for="year_filter">Año del carro</label><br>
                        <input name="year_filter" v-model="year" type="number" max="2022" min="2000" class="form-control" style="width: 50%; margin-left: 0px;" placeholder="Buscar">
                    </li>

                    <li>
                        <button v-on:click="filter_func" class="btn btn-primary" type="submit">Filtrar</button>
                    </li>

                    <li>
                        <button v-on:click="delete_func" class="btn btn-danger" type="submit">Eliminar Filtros</button>
                    </li>

                </form>
            </ul>
        </div>
    </div>   
</template>


<script>

export default {
  name: "FilterForm",
  data(){
    return {
        start_price: '',
        end_price: '',
        model: '',
        brand: '',
        year: ''
    };
  },
  methods: {
    filter_func(){
        const form = document.getElementById("filter-form");
        form.addEventListener('submit', (e) => {
            e.preventDefault();
        });

        if(this.start_price != '' || this.end_price != '' || this.model != '' || this.brand != '' || this.year != ''){
            const body = {
                'start_price': this.start_price,
                'end_price': this.end_price,
                'model': this.model,
                'brand': this.brand,
                'year': this.year
            };
            this.$emit("filter_func", body);
        }
    },
    delete_func(){
            const form = document.getElementById("filter-form");
            form.addEventListener('submit', (e) => {
                e.preventDefault();
            });
            form.reset();
            this.$emit("delete_func");
        }
        
    }
}
</script>

<style scoped>
.filter-container{
    widows: 500px;
    height: 800px;
    border-left: 10px solid var(--color-accent);
}

.filter-title {
    font-weight: 500;
    font-size: 50px;
}

label {
   font-weight: 400;
   font-size: 18px;
}

.filter {
    width: 400px;
    padding-top: 20px;
}

input {
    padding: 10px;
    margin-top: 10px;
}

</style>
