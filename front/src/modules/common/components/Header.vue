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

export default {
  methods: {
    logOut() {
      localStorage.clear();
      this.$router.push('/login');

    },


  }
}

</script>
