import { createApp } from 'vue'
import App from './App.vue'
/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUser, faPhone, faDroplet, faNotesMedical } from '@fortawesome/free-solid-svg-icons'

import router from './router/router'

library.add(faUser,faPhone, faDroplet, faNotesMedical)

createApp(App)
  .component('font-awesome-icon', FontAwesomeIcon)

  .use(router)
  .mount('#app')
