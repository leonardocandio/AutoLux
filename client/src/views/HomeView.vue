<template>

  <div class="container-fluid">

    <img src="https://fondosmil.com/fondo/24658.jpg" alt="">

    <div class="centrado">
        <h1 class="index-title">Encuentra el carro de tus sueños</h1>
    </div>

  </div>

  <div class="whatis">
    <h1>Qué es AutoLux</h1>
    <p class="whatiscont">Autolux es un aplicación enfocada a ayudar a nuestros usuarios en su proceso de compra de el auto que más se acomode a sus necesidades</p>
    <hr/>
  </div>

  

  <div class="whatdo">
    <h1>Qué hacemos</h1>
    <p class="whatdocont">Ofrecemos a nuestros usuarios un catalogo con gran variedad de autos de distintas marcas, noticias relacionadas con el mundo de los autos, además de un foro donde podrán encontrar reviews y opiniones de otros usuarios.</p>
    <hr/>
  </div>

</template>

<script>

export default {
  name: 'HomeView',
  components: {
    
  }
}
</script>


<style scoped>
    h1 {
        color: lightslategray;
        border-width: 20px;
    }

    
    .container-fluid {
        width: 100%;
        text-align: center;
        /* Arreglar margen debajo de la imagen */
        display: block;
        height: 900px;
    }
    
    .container-fluid>img {
        max-width: 99vw;
        display: block;
        transform: translate(0px, -300px);
        filter: saturate(1.5);
        background-color: black;
        box-shadow: 0 11px 35px 2px rgba(0, 0, 0, 0.40);
    }
    
    .centrado {
        position: absolute;
        top: 50%;
        left: 42%;
        transform: translate(-50%, -50%);
    }
    
    .index-title {
        width: 100%;
        padding: 0 0 0 28%;
        color: whitesmoke;
        font-size: 90px;
    }
    
    .index-btn {
        width: 20%;
        height: 50px;
        position: absolute;
        top: 51.5%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: rgba(255, 255, 255, 0.8);
    }
    
    .search {
        width: 45px;
        line-height: 40px;
        position: absolute;
        top: 50%;
        left: 60%;
        border-radius: 20px;
        border: 0px;
        background-color: rgba(255, 255, 255, 0.1);
        cursor: pointer;
    }
    
    .whatis {
        padding-top: 50px;
        padding-bottom: 50px;
        margin: auto auto;
        text-align: center;
        width: 600px;
    }
    
    .whatiscont {
        font-size: 2em;
        padding: auto;
    }
    
    .whatdo {
        padding-top: 50px;
        padding-bottom: 50px;
        margin: auto auto;
        text-align: center;
        width: 600px;
    }
    
    .whatdocont {
        font-size: 2em;
        padding: auto;
    }
    
</style>