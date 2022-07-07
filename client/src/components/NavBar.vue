<template>
  <nav>
    <router-link to="/" class="main-logo">AutoLux</router-link>
    <ul class="router-links">
      <li>
        <SearchForm/>
      </li>
      <li>
        <router-link to="/forum">Foro</router-link>
      </li>
      <li>
        <router-link to="/shop">Tienda</router-link>
      </li>
      <li v-if="Object.keys(user).length !== 0">
        <router-link to="/logout">Logout</router-link>
      </li>
      <li v-if="Object.keys(user).length !== 0">
        <router-link :to="{ name:'profile', params:{id:user.id}}">
          <img :src="user.image_url" class="avatar" alt="current user avatar"/>
        </router-link>
      </li>
      <li v-if="Object.keys(user).length === 0">
        <router-link to="/login">Iniciar sesión</router-link>
      </li>
    </ul>
  </nav>
</template>
<script>
import SearchForm from '@/components/SearchForm.vue'
import {getUser} from '@/store'

export default {
  name: 'NavBar',
  components: {SearchForm},
  data() {
    return {
      user: getUser
    }
  },
}
</script>
<style scoped>

.main-logo {
  position: relative;
  float: left;
  height: 100px;
  line-height: 100px;
  padding: 0 15px;
  font-size: 22px;
  font-weight: 900;
  text-transform: uppercase;
}

.router-links {
  float: right;
  margin-right: 30px;
  position: relative;
}

nav .router-links :hover {
  color: #2688f7b8;
  /* background: var(--color-accent); */
  border-radius: 2px;
}

nav .router-links li {
  list-style: none;
  position: relative;
  margin: 20px 20px 0;
  padding-bottom: 34px;
  display: inline-block;
}

nav .links li > router-link {
  position: relative;
  display: inline-block;
  padding: 0 20px;
  line-height: 30px;
  height: 30px;
}

nav .links li > router-link:hover {
  color: #fff;
  background: var(--color-accent);
  border-radius: 2px;
}

.avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
}

</style>
