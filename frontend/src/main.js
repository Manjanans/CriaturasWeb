import { createApp } from 'vue'
import App from '@/App.vue'
import router from '@/router/index.js'
import Toast from 'vue-toastification';
import 'vue-toastification/dist/index.css';
import { createPinia } from 'pinia'

import '@/assets/main.css'

const app = createApp(App);
const pinia = createPinia();

app.use(pinia);
app.use(router);
app.use(Toast);
app.mount('#app');