import { computed, ref } from 'vue';
import {defineStore} from 'pinia'
import getProfile from '@/modules/auth/helpers/getProfile'
export const auth = defineStore('auth', () =>{
  const tkn = ref(localStorage.getItem('tkn'))
  function setTkn(token) {
    localStorage.setItem('tkn', token);
    tkn.value = token;
  }

  const isAuth = computed(() => {
    return getProfile ;
  })

  function clear() {
    localStorage.removeItem('tkn');
    tkn.value = '';
  }

  return { tkn, setTkn, isAuth ,clear}


})
