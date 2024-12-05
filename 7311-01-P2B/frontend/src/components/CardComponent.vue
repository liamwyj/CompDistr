<template>
  <!-- Contenedor principal de la tarjeta -->
  <div class="card" :class="{ editing: isEditing }">
    <!-- Imagen: alterna entre modo de visualización y edición -->
    <img v-if="!isEditing" :src="editableImage" :alt="title" class="card-image" />
    <input v-else v-model="editableImage" placeholder="Image URL" class="edit-input" />

    <div class="card-text">
      <!-- Título: alterna entre modo de visualización y edición -->
      <h2 v-if="!isEditing">{{ editableTitle }}</h2>
      <input v-else v-model="editableTitle" placeholder="Title" class="edit-input" />

      <!-- Descripción: alterna entre modo de visualización y edición -->
      <p v-if="!isEditing">{{ editableDescription }}</p>
      <textarea v-else v-model="editableDescription" placeholder="Description" class="edit-textarea"></textarea>

      <!-- Lista de enlaces -->
      <ul class="nav" v-if="editableLinks.length || isEditing">
        <li>
          <a href="#" class="card-link">Enlaces a las prácticas →</a>
          <ul>
            <!-- Enlaces: iterar sobre la lista de enlaces -->
            <li v-for="(link, index) in editableLinks" :key="index" class="link-item">
              <div v-if="!isEditing">
                <a :href="link.url" target="_blank">{{ link.label }}</a>
              </div>
              <div v-else>
                <input v-model="link.label" placeholder="Link Text" class="edit-input small-input" />
                <input v-model="link.url" placeholder="Link URL" class="edit-input small-input" />
              </div>
            </li>
            <!-- Botón para agregar un nuevo enlace si estamos en modo de edición -->
            <li v-if="isEditing" class="add-practice-container">
              <button @click="addNewPractice" class="add-practice-button">Agregar práctica</button>
            </li>
          </ul>
        </li>
      </ul>
    </div>

    <!-- Botón de eliminar con imagen, visible solo cuando no estamos editando -->
    <button v-if="!isEditing" @click="deleteCard" class="delete-button">
      <img src="https://cdn-icons-png.freepik.com/512/1345/1345874.png" alt="Eliminar" class="delete-icon" />
    </button>

    <!-- Ícono de lápiz para alternar entre modo de edición y visualización, visible solo cuando no estamos editando -->
    <img 
      v-if="!isEditing"
      src="https://cdn-icons-png.flaticon.com/512/764/764599.png"
      alt="Editar" 
      class="edit-icon" 
      @click="toggleEditMode" 
    />

    <!-- Botón para guardar los cambios, visible solo cuando estamos editando -->
    <button v-if="isEditing" @click="saveChanges" class="save-button">Guardar</button>
  </div>
</template>

<script>
export default {
  props: {
    image: String,
    title: String,
    description: String,
    links: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      isEditing: false,
      editableImage: this.image,
      editableTitle: this.title,
      editableDescription: this.description,
      editableLinks: [...this.links],
    };
  },
  methods: {
    toggleEditMode() {
      this.isEditing = !this.isEditing;
    },
    saveChanges() {
      this.isEditing = false;
      this.$emit('save', {
        image: this.editableImage,
        title: this.editableTitle,
        description: this.editableDescription,
        links: this.editableLinks,
      });
    },
    deleteCard() {
      this.$emit('delete');
    },
    addNewPractice() {
      this.editableLinks.push({ label: '', url: '' });
    },
  },
};
</script>

<style scoped>
/* Estilos de la tarjeta */
.card {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 15px;
  background-color: #fff;
  padding: 20px;
  border-radius: 20px;
  box-shadow: 0 5px 10px rgba(76, 76, 144, 0.2);
  position: relative;
  transition: transform 0.3s ease;
  width: 100%;
}

.card.editing {
  background-color: #f3e5f5;
  border: 1px solid #d8b4e2;
}

.card:hover {
  transform: scale(1.02);
}

.card img {
  width: 180px;
  height: auto;
  border-radius: 8px;
}

.card-text {
  flex-grow: 1;
}

.card-text h2 {
  font-size: 1.5rem;
  color: rgb(112, 72, 186);
}

.card-text p {
  font-weight: 650;
  font-size: 1rem;
  color: #333;
}

.card-link {
  font-weight: bold;
  text-decoration: none;
  color: rgb(126, 104, 146);
}

/* Botón de eliminar con imagen */
.delete-button {
  background-color: transparent;
  border: none;
  cursor: pointer;
}

.delete-icon {
  width: 24px;
  height: 24px;
  padding: 70px;
  position: absolute;
  bottom: -45px;
  right: 50px;
  transition: transform 0.3s ease;
}

.delete-icon:hover {
  transform: scale(1.2);
}

.edit-input,
.edit-textarea {
  width: 100%;
  padding: 10px;
  font-size: 1rem;
  box-sizing: border-box;
  background-color: #f3e5f5;
  border: 1px solid #d8b4e2;
  border-radius: 5px;
}

.edit-icon {
  width: 24px;
  height: 24px;
  position: absolute;
  padding: 70px;
  bottom: -45px;
  right: -45px;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.edit-icon:hover {
  transform: scale(1.2);
}

.save-button {
  margin-top: 10px;
  padding: 10px 20px;
  background-color: #593a71;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.save-button:hover {
  background-color: #78489d;
}

.add-practice-container {
  display: flex;
  justify-content: center;
}

.add-practice-button {
  padding: 5px 10px;
  background-color: #593a71;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10px;
}

.add-practice-button:hover {
  background-color: #78489d;
}
</style>
