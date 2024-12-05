<template>
  <footer>
    <img src="https://upload.wikimedia.org/wikipedia/commons/d/dc/Logotipo_Escuela_Polit%C3%A9cnica_Superior_%28UAM%29.svg" alt="Eps logo" class="footer-image" />
    <p>Grado: Ciencias e Ingeniería de Datos <br> Miembros: Yijun Wang, Jimena de Prado, Geer Wang</p>
  </footer>
</template>

<script>
export default {
  name: 'FooterComponent'
};
</script>

<style scoped>
footer {
  background-color: rgb(76, 76, 144);
  padding: 20px 25px;
  position: relative;
  color: #ffffff;
}

footer p {
  font-size: 1rem;
  margin-right: 100px;
}

footer img {
  width: 100px;
  height: auto;
  float: right;
  margin-left: 20px;
  border-radius: 8px;
}
</style>