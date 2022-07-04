<template>
    
    <div style="width: 20%" class="filter-container">
        <div class="filter-content">
            <p class="filter-title">Filtros</p>
            <ul>
                <form method="GET" action="filter">
                    <li class="filter">
                        <label>Rango de precios</label>
                        <div style="display:flex;">
                            <input name="start_price_filter" placeholder="Desde" type="number" step="50" min="100" max="100000" class="form-control" id="search-input" style="width: 50%; margin-left: 0px;">

                            <input name="end_price_filter" placeholder="Hasta" type="number" step="50" min="100" max="100000" class="form-control" id="search-input" style="width: 50%; margin-left: 0px;">
                        </div>
                    </li>

                    <li class="filter">
                        <label for="model_filter">Modelo del carro</label><br>
                        <input name="model_filter" type="text" class="form-control" id="search-input" style="width: 50%; margin-left: 0px;" placeholder="Buscar">
                    </li>

                    <li class="filter">
                        <label for="brand_filter">Marca del carro</label><br>
                        <input name="brand_filter" type="text" class="form-control" id="search-input" style="width: 50%; margin-left: 0px;" placeholder="Buscar">
                    </li>

                    <li class="filter">
                        <label for="year_filter">Año del carro</label><br>
                        <input name="year_filter" type="number" class="form-control" id="search-input" style="width: 50%; margin-left: 0px;" placeholder="Buscar">
                    </li>

                    <li>
                        <button class="btn btn-primary" type="submit">Filtrar</button>
                    </li>
                </form>
            </ul>
        </div>
    </div>
    

</template>


<script>
export default {
  name: "FilterForm",
  
}
</script>

<style scoped>
.filter-container{
    widows: 500px;
    height: 800px;
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
