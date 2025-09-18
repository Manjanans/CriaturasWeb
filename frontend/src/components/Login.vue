<template>
  <div class="login-container">
    <h2>Iniciar Sesión</h2>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="username">Nombre de Usuario</label>
        <input type="text" id="username" v-model="username" required>
      </div>
      <div class="form-group">
        <label for="password">Contraseña</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <button type="submit" class="login-button">Entrar a la 4ta Dimensión</button>
    </form>
  </div>
  <ErrorModal :show="showModal" :message="modalMessage" @close="closeModal" />
</template>

<script setup>
import { ref } from 'vue';
import ErrorModal from './ErrorModal.vue';

const emit = defineEmits(['login-success']);

const username = ref('');
const password = ref('');
const modalMessage = ref('');
const showModal = ref(false);

const handleLogin = async () => {
  try {
    const details = {
      'username': username.value,
      'password': password.value
    };

    const formBody = Object.keys(details).map(key => encodeURIComponent(key) + '=' + encodeURIComponent(details[key])).join('&');

    const response = await fetch('/api/v1/auth/token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
      },
      body: formBody
    });

    if (!response.ok) {
      let errorMessage = 'Fallo de inicio de sesión.';
      try {
        // Try to parse the error response as JSON, which is expected for 4xx errors
        const data = await response.json();
        if (data.detail === 'Incorrect username or password') {
          errorMessage = 'Usuario o contraseña incorrectos.';
        } else {
          errorMessage = data.detail || errorMessage;
        }
      } catch (jsonError) {
        // If parsing fails, it's likely a 5xx error with an HTML response
        errorMessage = 'Ocurrió un error inesperado en el servidor. Por favor, intente más tarde.';
      }
      throw new Error(errorMessage);
    }

    const data = await response.json();
    localStorage.setItem('accessToken', data.access_token);
    emit('login-success'); // Notify parent component of successful login

  } catch (err) {
    modalMessage.value = err.message;
    showModal.value = true;
  }
};

const closeModal = () => {
  showModal.value = false;
};
</script>

<style scoped>
.login-container {
  background-color: #F5E8C7;
  padding: 2rem 3rem;
  border-radius: 5px;
  border: 2px solid #D8C0A0;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
  width: 100%;
  max-width: 400px;
  text-align: center;
}

h2 {
  color: #3E2723;
  margin-bottom: 1.5rem;
  font-size: 2.5rem;
}

.form-group {
  text-align: left;
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
  font-weight: bold;
}

.form-group input {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #BCAAA4;
  border-radius: 3px;
  background-color: #FFF8E1;
  font-family: 'Merriweather', serif;
  font-size: 1rem;
  box-sizing: border-box;
}

.login-button {
  width: 100%;
  padding: 1rem;
  border: none;
  border-radius: 5px;
  background-color: #E65100;
  color: white;
  font-family: 'Cinzel', serif;
  font-size: 1.2rem;
  font-weight: 700;
  cursor: pointer;
  transition: background-color 0.2s ease-in-out;
  margin-top: 1rem;
}

.login-button:hover {
  background-color: #F57C00;
}

/* The old error message p tag is no longer needed */
</style>