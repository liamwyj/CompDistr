<template>
  <div>
    <!-- Modal de inicio de sesión para autenticación -->
    <div v-if="showLogin" class="login-modal-overlay" @click.self="closeLogin">
      <div class="login-modal">
        <button class="close-button" @click="closeLogin">✖</button>
        <h3>Iniciar Sesión</h3>
        <input type="text" v-model="username" placeholder="Usuario" class="login-input" />
        <input type="password" v-model="password" placeholder="Contraseña" class="login-input" />
        <button @click="login" class="login-button">Iniciar Sesión</button>
        <p v-if="loginError" class="error-message">{{ loginError }}</p>
      </div>
    </div>

    <section class="main-content">
      <!-- Barra de búsqueda -->
      <div class="search-container">
        <input type="text" v-model="searchTerm" placeholder="Buscar proyectos..." class="search-bar"
        @keydown.enter="searchProjects"/>
        <button @click="searchProjects" class="search-button">Aceptar</button>
      </div>

      <!-- Mensaje de error si no se encontraron resultados -->
      <div v-if="errorMessage" class="error-message">
        {{ errorMessage }}
      </div>

      <!-- Tarjetas de proyectos filtradas -->
      <Card 
        v-for="(card, index) in cards" 
        :key="index" 
        :id="card.id"
        :image="card.image" 
        :title="card.title" 
        :description="card.description" 
        :links="card.links" 
        @delete="deleteCard(card.id)" 
        @update="updateCard"
      ></Card>

      <!-- Botón para mostrar el formulario -->
      <button @click="handleAddButtonClick" class="add-button"><p> Agregar + </p></button>

      <!-- Formulario para agregar nuevo proyecto -->
      <AddProjectForm v-if="isFormVisible && isAuthenticated" @add-project="addProject" />
    </section>
  </div>
</template>

<script>
import AddProjectForm from './AddProjectForm.vue';
import Card from './Card.vue';
import axios from '../plugins/axios.js';

export default {
  name: 'MainContent',
  components: {
    AddProjectForm,
    Card
  },
  data() {
    return {
      username: '',
      password: '',
      isAuthenticated: false, // Estado de autenticación del usuario
      loginError: '',         // Mensaje de error en caso de fallo de autenticación
      showLogin: false,       // Controla si se muestra el modal de inicio de sesión
      cards: [],              // Contenedor para las tarjetas de prácticas
      isFormVisible: false,   // Controla la visibilidad del formulario para agregar prácticas
      searchTerm: '',         // Término de búsqueda
      errorMessage: ''        // Mensaje de error para mostrar si no se encuentran resultados
    };
  },
  methods: {
    // Obtiene todas las tarjetas de prácticas desde la API
    async login() {
      try {
        const response = await axios.post('/login', {
          username: this.username,
          password: this.password
        },{ withCredentials: true });
        
        this.isAuthenticated = true;   // Actualiza el estado de autenticación
        this.showLogin = false;        // Oculta el modal de inicio de sesión
        this.loginError = '';          // Resetea el mensaje de error
        this.isFormVisible = true;     // Muestra el formulario de agregar proyecto
        console.log(response.data.message);
      } catch (error) {
        this.loginError = "Credenciales incorrectas";
        console.error(error);
      }
    },
    // Maneja el clic en el botón de agregar
    handleAddButtonClick() {
      if (this.isAuthenticated) {
        this.isFormVisible = true; // Muestra el formulario si el usuario ya está autenticado
      } else {
        this.showLogin = true; // Muestra el modal de inicio de sesión si no está autenticado
      }
    },
    // Cierra el modal de autenticación
    closeLogin() {
      this.showLogin = false;
      this.loginError = ''; // Resetea el mensaje de error al cerrar
    },
    async fetchCards() {
      try {
        const response = await axios.get('/practicas');
        this.cards = response.data;
      } catch (error) {
        console.error("Error al cargar las prácticas:", error);
        alert("Hubo un problema al cargar las prácticas. Inténtalo de nuevo más tarde.");
      }
    },
    // Método de búsqueda que realiza una llamada a la API
    async searchProjects() {
      this.errorMessage = '';  // Resetea el mensaje de error
      this.cards = [];         // Vacía la lista de tarjetas para comenzar una nueva búsqueda

      try {
        const response = await axios.get('/practicas/buscar', {
          params: { searchTerm: this.searchTerm }
        });
        this.cards = response.data;  // Actualiza las tarjetas con los resultados de la búsqueda
      } catch (error) {
        if (error.response && error.response.status === 404) {
          // Si el backend devuelve un 404, muestra el mensaje de error
          this.errorMessage = error.response.data.error;
          this.cards = [];  // Asegúrate de que no haya tarjetas visibles
        } else {
          console.error("Error en la búsqueda:", error);
          alert("Hubo un problema con la búsqueda. Inténtalo de nuevo.");
        }
      }
    },
    // Alterna la visibilidad del formulario
    showForm() {
      this.isFormVisible = !this.isFormVisible;
    },
    // Agrega una nueva práctica
    async addProject(newProject) {
      if (!this.isAuthenticated) {
        alert("Debes iniciar sesión para agregar un proyecto.");
        return;
      }
      try {
        const response = await axios.post('/practicas', newProject, { withCredentials: true });
        this.cards.push(response.data); // Agrega el nuevo proyecto a la lista local
        this.isFormVisible = false;     // Oculta el formulario después de agregar
      } catch (error) {
        console.error("Error al agregar la práctica:", error);
        alert("Hubo un problema al agregar la práctica. Inténtalo de nuevo.");
      }
    },
    // Elimina una práctica por ID
    async deleteCard(id) {
      try {
        await axios.delete(`/practicas/${id}`);
        this.cards = this.cards.filter(card => card.id !== id); // Filtra el array localmente
      } catch (error) {
        console.error("Error al eliminar la práctica:", error);
        alert("Hubo un problema al eliminar la práctica. Inténtalo de nuevo.");
      }
    },
    // Actualiza una práctica existente
    async updateCard(updatedCard) {
      try {
        const { id, image, title, description, links } = updatedCard;
        if (!id) {
          console.error("Error: el ID de la práctica es undefined");
          return;
        }

        await axios.put(`/practicas/${id}`, { image, title, description, links });
        
        const index = this.cards.findIndex(card => card.id === id);
        if (index !== -1) {
          this.cards.splice(index, 1, updatedCard);
        }
      } catch (error) {
        console.error("Error al actualizar la práctica:", error);
        alert("Hubo un problema al actualizar la práctica. Inténtalo de nuevo.");
      }
    }
  },

  mounted() {
    this.fetchCards(); // Llama a fetchCards al montar el componente
  }
};
</script>


<style scoped>

.login-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.login-modal {
  background-color: #6b3a8a;
  padding: 40px;
  border-radius: 10px;
  max-width: 500px;
  width: 90%;
  text-align: center;
  color: white;
  position: relative;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 15px;
  background: none;
  border: none;
  color: white;
  font-size: 20px;
  cursor: pointer;
}

.login-modal h3 {
  margin-bottom: 20px;
  font-size: 24px;
}

.login-input {
  width: 100%;
  padding: 15px;
  margin-bottom: 15px;
  font-size: 16px;
  border-radius: 5px;
  border: none;
}

.login-button {
  width: 100%;
  padding: 15px;
  background-color: #78489d;
  color: white;
  font-size: 18px;
  font-weight: bold;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.login-button:hover {
  background-color: #9060b4;
}

.main-content {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  justify-items: center;
  padding: 40px;
  background-color: white;
}

.search-container {
  display: flex;
  grid-column: span 2;
  margin-bottom: 20px;
  width: 100%;
}

.search-bar {
  padding: 10px;
  font-size: 16px;
  flex: 1;
}

.search-button {
  background-color: #593a71;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  font-size: 16px;
  border-radius: 5px;
}

.error-message {
  color: red;
  font-size: 16px;
  margin-bottom: 20px;
}

.search-button:hover {
  background-color: #78489d;
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
