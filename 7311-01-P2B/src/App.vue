<template>
  <div id="app">
    <HeaderComponent />
    <main class="main-content-wrapper">
      <MainContent />
    </main>
    <FooterComponent />
  </div>
</template>

<script>
import HeaderComponent from './components/HeaderComponent.vue';
import MainContent from './components/MainContent.vue';
import FooterComponent from './components/FooterComponent.vue';

export default {
  components: {
    HeaderComponent,
    MainContent,
    FooterComponent
  }
};
</script>

<style>
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* Hace que el contenido abarque toda la altura de la ventana */
}

.main-content-wrapper {
  flex: 1; /* Esto hace que el MainContent ocupe todo el espacio restante entre el header y el footer */
  padding: 20px;
  background-color: white;
}

header, footer {
  background-color: #f0f0f0;
  padding: 20px;
}

footer {
  text-align: center;
}
</style>