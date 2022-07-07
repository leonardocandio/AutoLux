<template>
    <CarDetail :car="car" v-if="car"/>
</template>

<script>
import CarDetail from '@/components/CarDetail.vue'
export default {
    name: "CarDetailView",
    components: {
        CarDetail
    },
    props: {
        id: String
    },
    data(){
        return {
            car: null
        }
    },
    beforeRouteEnter(to, from, next){
        fetch(`/cars/${to.params.id}`, {method: "GET"})
        .then(response => response.json())
        .then(res => {
            next(vm => vm.setData(res.cars))
        })
        .catch(error => {
            console.log(error);
        });
    },
    methods: {
        setData(data) {
            this.car = data;
        }
    }
}

</script>

<style>

</style>
