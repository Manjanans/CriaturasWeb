<template>
  <div class="dashboard-container">
    <Navbar @logout="handleLogout" @open-profile-modal="toggleProfileModal" @open-criaturas-modal="toggleCriaturasModal" />
    <main class="main-content">
      <h1>Bienvenido, Maestro</h1>
      <p>Selecciona una opción del menú para comenzar.</p>
    </main>
    <Criaturas :show="showCriaturasModal" @close="toggleCriaturasModal" />
    <Profile :show="showProfileModal" @close="toggleProfileModal" @open-change-password-modal="toggleChangePasswordModal" />
    <ChangePasswordModal :show="showChangePasswordModal" @close="toggleChangePasswordModal" @password-changed="handlePasswordChanged" />
    <SuccessModal :show="showSuccessModal" message="Contraseña cambiada con éxito" @close="toggleSuccessModal" />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import Navbar from './Navbar.vue';
import Profile from './Profile.vue';
import ChangePasswordModal from './ChangePasswordModal.vue';
import SuccessModal from './SuccessModal.vue';
import Criaturas from './Criaturas.vue';

const emit = defineEmits(['logout']);

const showProfileModal = ref(false);
const showChangePasswordModal = ref(false);
const showSuccessModal = ref(false);
const showCriaturasModal = ref(false);

const handleLogout = () => {
  emit('logout');
};

const toggleCriaturasModal = () =>{
  showCriaturasModal.value = !showCriaturasModal.value;
}

const toggleProfileModal = () => {
  showProfileModal.value = !showProfileModal.value;
};

const toggleChangePasswordModal = () => {
  showChangePasswordModal.value = !showChangePasswordModal.value;
};

const toggleSuccessModal = () => {
  showSuccessModal.value = !showSuccessModal.value;
};

const handlePasswordChanged = () => {
  showChangePasswordModal.value = false;
  showSuccessModal.value = true;
};
</script>

<style scoped>
.dashboard-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background-image: url('https://wallpapercave.com/wp/wp4588423.jpg');
  background-size: cover;
  background-position: center;
}

.main-content {
  flex-grow: 1;
  padding: 2rem;
  background-color: rgba(0, 0, 0, 0.5); /* Add a semi-transparent overlay to make the text more readable */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #fff;
  text-align: center;
}

h1 {
  font-size: 3rem;
}
</style>