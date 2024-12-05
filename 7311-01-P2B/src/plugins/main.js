// src/main.js
import { createApp } from 'vue';
import App from './App.vue';
import axiosInstance from './plugins/axios'; // Asegúrate de que este archivo exista y esté configurado

const app = createApp(App);

// Permite que axios esté disponible globalmente con this.$axios
app.config.globalProperties.$axios = axiosInstance;

app.mount('#app');
