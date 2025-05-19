import './assets/main.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-icons/font/bootstrap-icons.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'

import App from './App.vue'
import router from './router'

// ✅ 禁用缓存
axios.defaults.headers.common['Cache-Control'] = 'no-cache'
axios.defaults.headers.common['Pragma'] = 'no-cache'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
