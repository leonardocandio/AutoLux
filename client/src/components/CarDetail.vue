<template>

    <div class="namecar">
        <h1 style="color: #fff;">{{ car.name }}</h1>
    </div>

    <div class="cont">
        <div class="padre">
            <div class="image_car">
                <img class="imgcr" :src="car.image_url">
            </div>
            <table class="infocar" cellspacing="0" cellpading="0">
                <tbody>
                    <tr>
                        <th>
                        Precio
                        </th>
                        <td v-if="car.price==0">
                            Consultar
                        </td>
                        <td v-else>
                            {{ car.price }}
                    </td>
                    </tr>
                    
                    <tr>
                        <th>
                            Marca
                        </th>
                        <td>
                            {{ car.brand }}
                        </td>
                    </tr>
                    <tr>
                        <th>
                            Modelo
                        </th>
                        <td>
                            {{ car.model }}
                        </td>
                    </tr>
                    <tr>
                        <th>
                            Categoría
                        </th>
                        <td>
                            {{ car.category }}
                        </td>
                    </tr>
                    <tr>
                        <th>
                            Año
                        </th>
                        <td>
                            {{ car.year }}
                        </td>
                    </tr>
                    <tr>
                        <th>
                            Año de fabricación
                        </th>
                        <td>
                            {{ car.year_production }}
                        </td>
                    </tr>
                    <tr>
                        <th>
                            Kilometraje
                        </th>
                        <td>
                            {{ car.mileage }}
                        </td>
                    </tr>
                    <tr>
                        <th>
                            Transmisión
                        </th>
                        <td>
                            {{ car.transmission }}
                        </td>
                    </tr>
                    <tr>
                        <th>
                            Combustible
                        </th>
                        <td>
                            {{ car.fuel }}
                        </td>
                    </tr>
                    <tr>
                        <th>
                            Cilindrada
                        </th>
                        <td>
                            {{ car.engine_displacement }}
                        </td>
                    </tr>
                    <tr>
                        <th>
                            Número de puertas
                        </th>
                        <td>
                            {{ car.doors }}
                        </td>
                    </tr>
                    <tr>
                        <th>
                            Tipo de tracción
                        </th>
                        <td>
                            {{ car.drivetrain }}
                        </td>
                    </tr>
                    <tr>
                        <th>
                            Color
                        </th>
                        <td>
                            {{ car.color }}
                        </td>
                    </tr>
                    <tr>
                        <th>
                            Ubicación
                        </th>
                        <td>
                            {{ car.location }}
                        </td>
                    </tr>
                    <tr>
                        <th>
                            Compra por Whatsapp
                        </th>
                        <td>
                            <a href="https://web.whatsapp.com/send?phone=51946107893">
                                <img style="width:50px;" src="https://cdn-icons-png.flaticon.com/512/124/124034.png?w=360" alt="">
                            </a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    <div class="card">
        <h4 class="p-3">Descripción</h4>
        <p class="p-3">{{ car.description }}</p>
    </div>
</template>

<script>
export default {
  name: 'CarDetail',
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
.container {
    width: 100%;
    text-align: center;
    display: block;
}

.padre {
    display: flex;
    margin: auto auto;
    border: 30px;
}

.infocar {
    text-align: left;
    font-size: 20px;
    width: 50%;
}

.cont {
    margin: 50px;
    width: auto;
    height: 600px;
}

.image_car {
    padding: 1px 100px;
}

.imgcr {
    border-radius: 15px;
}

.namecar {
    background-color: #000;
}

h1 {
    padding: 30px 350px;
}

</style>