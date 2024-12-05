import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')

// Seleccionamos todos los contenedores con las flechas y enlaces
const toggleContainers = document.querySelectorAll('.link-arrow-container');

// Iteramos sobre cada contenedor
toggleContainers.forEach(container => {
    // Al hacer clic en el contenedor
    container.addEventListener('click', function() {
        // Alternar la visibilidad de la lista de prácticas
        const practiceList = container.nextElementSibling;
        
        if (practiceList) {
            practiceList.classList.toggle('active');
        }

        // Alternar la rotación de la flecha
        const arrow = container.querySelector('.list__arrow');
        if (arrow) {
            arrow.classList.toggle('arrow-rotate');
        }
    });
});
