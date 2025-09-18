<template>
  <nav class="main-nav">
    <ul class="nav-links">
      <li><a href="#">Criaturas</a></li>
      <li><a href="#">Batalla</a></li>
    </ul>
    <div class="user-menu">
      <a href="#">Perfil</a>
      <button @click="logout" class="logout-button">Salir</button>
    </div>
  </nav>
</template>

<script setup>
const emit = defineEmits(['logout']);

const logout = () => {
  emit('logout');
};
</script>

<style scoped>
.main-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 2rem;
  background-color: rgba(20, 20, 20, 0.5);
  border-bottom: 1px solid #D8C0A0;
}

.nav-links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  gap: 3rem; /* Spacing between Criaturas and Batalla */
}

.nav-links a {
  color: #F5E8C7;
  text-decoration: none;
  font-family: 'Cinzel', serif;
  font-size: 1.2rem;
  transition: color 0.2s ease-in-out;
}

.nav-links a:hover {
  color: #E65100;
}

.user-menu {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  align-items: center;
  gap: 1.5rem; /* Spacing between Perfil and Salir */
}

.user-menu a {
  color: #F5E8C7;
  text-decoration: none;
  font-family: 'Cinzel', serif;
  font-size: 1.2rem;
  transition: color 0.2s ease-in-out;
}

.user-menu a:hover {
  color: #E65100;
}

.logout-button {
  background: none;
  border: 1px solid #795548;
  color: #F5E8C7;
  padding: 0.5rem 1rem;
  border-radius: 5px;
  font-family: 'Merriweather', serif;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

.logout-button:hover {
  background-color: #795548;
  color: white;
}
</style>