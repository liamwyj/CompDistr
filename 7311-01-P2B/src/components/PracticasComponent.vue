<template>
  <div>
    <HeaderComponent />

    <section class="practicas">
      <h2>Lista de Prácticas</h2>

      <!-- Barra de búsqueda -->
      <input type="text" v-model="searchTerm" placeholder="Buscar proyectos..." class="search-bar"/>

      <!-- Tarjetas de proyectos filtradas -->
      <CardComponent 
        v-for="(card, index) in filteredCards" 
        :key="index" 
        :image="card.image" 
        :title="card.title" 
        :description="card.description" 
        :links="card.links" 
        @delete="deleteCard(card.id)" 
      />

      <!-- Botón para mostrar el formulario -->
      <button @click="showForm" class="add-button"><p> Agregar + </p></button>

      <!-- Formulario para agregar nuevo proyecto -->
      <AddProjectForm v-if="isFormVisible" @add-project="addProject" />

      <!-- Lista de prácticas -->
      <h1>Prácticas</h1>
      <ul>
        <li v-for="practica in practicas" :key="practica.id">
          {{ practica.name }} <button @click="eliminarPractica(practica.id)">Eliminar</button>
        </li>
      </ul>
      <input v-model="nuevaPractica" placeholder="Nueva práctica" />
      <button @click="agregarPractica">Agregar</button>
    </section>

    <FooterComponent />
  </div>
</template>

<script>
import HeaderComponent from './HeaderComponent.vue';
import FooterComponent from './FooterComponent.vue';
import CardComponent from './CardComponent.vue'; 
import AddProjectForm from './AddProjectForm.vue'; 
import Solicitudes from '@/plugins/solicitudes'; // Importa la clase Solicitudes
import { obtenerPracticas, agregarPractica, eliminarPractica } from '@/plugins/servidorAPI'; // Importa las funciones del API

export default {
  name: 'PracticasComponent',
  components: { 
    HeaderComponent, 
    FooterComponent, 
    CardComponent, 
    AddProjectForm,
  },
  data() {
    return {
      cards: [], // Inicialmente vacío, cargaremos los datos al montar
      practicas: [], // Almacena las prácticas
      nuevaPractica: '', // Para agregar nuevas prácticas
      isFormVisible: false,
      searchTerm: '' // Propiedad para el término de búsqueda
    };
  },
  computed: {
    filteredCards() {
      // Filtramos las tarjetas según el término de búsqueda
      return this.cards.filter(card =>
        card.title.toLowerCase().includes(this.searchTerm.toLowerCase())
      );
    }
  },
  methods: {
    async loadCards() {
      try {
        this.cards = await Solicitudes.fetchPracticas(); // Cargar las tarjetas desde la clase Solicitudes
      } catch (error) {
        console.error('Error al cargar las tarjetas:', error);
      }
    },
    async loadPracticas() {
      try {
        this.practicas = await obtenerPracticas(); // Carga las prácticas desde la API
      } catch (error) {
        console.error('Error al cargar prácticas:', error);
      }
    },
    showForm() {
      this.isFormVisible = !this.isFormVisible; // Alternar la visibilidad del formulario
    },
    async addProject(newProject) {
      try {
        const addedCard = await Solicitudes.addPractica(newProject); // Agregar el nuevo proyecto
        this.cards.push(addedCard); // Agregar la tarjeta a la lista localmente
        this.isFormVisible = false; // Ocultar el formulario después de agregar el proyecto
      } catch (error) {
        console.error('Error al agregar el proyecto:', error);
      }
    },
    async agregarPractica() {
      const practica = { id: this.practicas.length + 1, name: this.nuevaPractica }; // Crea un objeto de práctica
      await agregarPractica(practica);
      this.nuevaPractica = ''; // Limpia el input
      await this.loadPracticas(); // Recarga las prácticas
    },
    async eliminarPractica(id) {
      await eliminarPractica(id); // Llama a la función para eliminar la práctica
      await this.loadPracticas(); // Recarga las prácticas
    },
    async deleteCard(id) {
      try {
        await Solicitudes.deletePractica(id); // Eliminar la tarjeta a través de Solicitudes
        this.cards = this.cards.filter(card => card.id !== id); // Filtrar localmente la tarjeta eliminada
      } catch (error) {
        console.error('Error al eliminar la tarjeta:', error);
      }
    }
  },
  mounted() {
    this.loadCards(); // Cargar las tarjetas al montar el componente
    this.loadPracticas(); // Cargar las prácticas al montar el componente
  }
};
</script>

<style scoped>
.practicas {
  max-width: 800px;
  margin: 0 auto;
}

.search-bar {
  padding: 10px;
  margin-bottom: 20px;
  font-size: 16px;
  width: 100%;
}

.add-button p {
  font-size: 20px;
}

.add-button {
  margin-top: 20px;
  background-color: #593a71;
  color: white;
  padding: 20px 30px;
  height: 70px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.add-button:hover {
  background-color: #78489d;
}
</style>
