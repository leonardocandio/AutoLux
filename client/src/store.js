import {computed, ref, watch} from 'vue'

const state = ref({
    user: {}
})
if (localStorage.getItem('state')) {
    setUser(JSON.parse(localStorage.getItem('state')).user)
}


watch(
    state,
    (userVal) => {
        localStorage.setItem('state', JSON.stringify(userVal));
    }, {deep: true}
);


const getUser = computed(() => state.value.user)

function setUser(user) {
    state.value.user = user
}

function clearUser() {
    state.value.user = {}
}

export {getUser, setUser, clearUser}
