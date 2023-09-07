import {createApp} from 'vue'
import App from './App.vue'
import {createPinia} from 'pinia'

/* import the fontawesome core */
import {library} from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'

/* import specific icons */
import {faUser, faPhone, faDroplet, faNotesMedical} from '@fortawesome/free-solid-svg-icons'

import router from './router/router'

library.add(faUser, faPhone, faDroplet, faNotesMedical)
const app = createApp(App)

app.use(createPinia())
app.component('font-awesome-icon', FontAwesomeIcon)

app.use(router)
app.mount('#app')
