/**
 * First we will load all of this project's JavaScript dependencies which
 * includes Vue and other libraries. It is a great starting point when
 * building robust, powerful web applications using Vue and Laravel.
 */

require('./bootstrap');

import { createApp } from 'vue';
import App from './App.vue'
import router from './router'

// createApp(App).use(router).mount("#app")
const app = createApp(App)
app.use(router)
app.mount('#app')