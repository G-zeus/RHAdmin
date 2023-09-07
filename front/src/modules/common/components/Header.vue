<template>
  <ul class="nav justify-content-end">
    <li class="nav-item">
      <a class="nav-link " href="#/dashboard">Inicio</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" v-on:click="logOut()">logOut</a>
    </li>

  </ul>

</template>
<script>
import {auth} from '../../auth/stores/auth'
export default {
  methods: {
    logOut() {
      auth().clear()
        this.$router.push('/login');

    },


  },
    mounted() {

      if (!auth().isAuth){
          this.$router.push('/login');

      }


    }
}

</script>
