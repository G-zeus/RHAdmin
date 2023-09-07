import { computed, ref } from 'vue';
import {defineStore} from 'pinia'

export const auth = defineStore('auth', () =>{
  const tkn = ref(localStorage.getItem('tkn'))
  function setTkn(token) {
    localStorage.setItem('tkn', token);
    tkn.value = token;
  }

  const isAuth = computed(() => {
    return Boolean( tkn.value) ;
  })

  function clear() {
    localStorage.removeItem('tkn');
    tkn.value = '';
  }

  return { tkn, setTkn, isAuth ,clear}


})
