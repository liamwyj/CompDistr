<template>
  <div class="form-container">  
    <h3>Añadir Nuevo Proyecto</h3>
    <form @submit.prevent="submitForm">
      <label for="title">Título:</label>
      <input type="text" id="title" v-model="title" required />

      <label for="description">Descripción:</label>
      <textarea id="description" v-model="description" required></textarea>

      <label for="image">URL de la Imagen:</label>
      <input type="text" id="image" v-model="image" required />

      <label for="alt">Texto Alternativo de la Imagen:</label>
      <input type="text" id="alt" v-model="alt" required />

      <label for="links">Enlaces (separar por comas):</label>
      <input type="text" id="links" v-model="linksInput" />

      <button type="submit">Agregar Proyecto</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'AddProjectForm',
  data() {
    return {
      title: '', 
      description: '',
      image: '',
      alt: '',
      linksInput: '',
    };
  },
  methods: {
    submitForm() {
      const newProject = {
        title: this.title,
        description: this.description,
        image: this.image,
        alt: this.alt,
        links: this.linksInput.split(',').map((link) => ({
          label: `Práctica ${link.trim()}`,
          url: `practicas/${link.trim()}.pdf`
        }))
      };
      this.$emit('add-project', newProject);  // Asegúrate de que esto se emita correctamente
      this.resetForm();
    },
    resetForm() {
      this.title = '';
      this.description = '';
      this.image = '';
      this.alt = '';
      this.linksInput = '';
    }
  }
};
</script>


<style scoped>
.form-container {
  background-color: rgb(76, 76, 144);
  width: 500px;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-top: 20px;
}

h3 {
  color: white; /* Título en blanco */
  margin-bottom: 10px;
}

form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

label {
  color: #ffffff; /* Color morado claro */
  font-weight: bold;
}

input, textarea {
  padding: 10px;
  border: 1px solid #d8b4e2;
  border-radius: 5px;
  font-size: 1rem;
  background-color: #f3e5f5; /* Fondo morado claro */
  color: #4a235a; /* Texto morado */
}

input::placeholder, textarea::placeholder {
  color: #a084af; /* Color de los placeholders */
}

button {
  background-color: #593a71;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
}

button:hover {
  background-color: #78489d;
}
</style>
