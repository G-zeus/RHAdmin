<template>
  <router-view/>
</template>

<script>
import Login from "@/modules/auth/pages/Login.vue";
export default {
  name: 'App',
  components: {
      Login
  }
}
</script>


