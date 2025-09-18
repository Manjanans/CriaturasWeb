<template>
  <div class="app-container">
    <Navbar @logout="handleLogout" />
    <main class="content-area">
      <h1>Bienvenido, Aventurero</h1>
      <p>Selecciona una opción del menú para comenzar.</p>
    </main>
  </div>
</template>

<script setup>
import Navbar from './Navbar.vue';

const emit = defineEmits(['logout']);

const handleLogout = () => {
  emit('logout');
};
</script>

<style scoped>
.app-container {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.content-area {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #F5E8C7;
  text-align: center;
}

h1 {
  font-size: 3rem;
}
</style>