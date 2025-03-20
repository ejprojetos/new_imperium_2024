import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { VueQueryPlugin } from '@tanstack/vue-query'

import App from './App.vue'
import router from './router'

import { FontAwesomeIcon } from './fontawesome'

const app = createApp(App)
const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)

app.use(VueQueryPlugin)
app.use(pinia)
app.use(router)

app.component('font-awesome-icon', FontAwesomeIcon)

app.mount('#app')
