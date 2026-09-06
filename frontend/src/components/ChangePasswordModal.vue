<template>
  <div v-if="show" class="modal-overlay" @click.self="close">
    <div class="modal-content">
      <h4>Cambiar Contraseña</h4>
      <form @submit.prevent="handleChangePassword">
        <div class="form-group">
          <label for="new-password">Nueva Contraseña</label>
          <input type="password" id="new-password" v-model="newPassword" required>
        </div>
        <div class="form-group">
          <label for="confirm-password">Confirmar Contraseña</label>
          <input type="password" id="confirm-password" v-model="confirmPassword" required>
        </div>
        <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
        <div class="modal-actions">
          <button type="submit" class="change-button">Cambiar</button>
          <button type="button" @click="close" class="cancel-button">Cancelar</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
  show: Boolean
});

const emit = defineEmits(['close', 'password-changed']);

const newPassword = ref('');
const confirmPassword = ref('');
const errorMessage = ref('');

const handleChangePassword = async () => {
  if (newPassword.value !== confirmPassword.value) {
    errorMessage.value = 'Las contraseñas no coinciden.';
    return;
  }

  try {
    const token = localStorage.getItem('accessToken');
    const response = await fetch('/auth/change-password', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ new_password: newPassword.value })
    });

    if (!response.ok) {
      const data = await response.json();
      throw new Error(data.detail || 'Error al cambiar la contraseña.');
    }

    emit('password-changed');
  } catch (err) {
    errorMessage.value = err.message;
  }
};

const close = () => {
  emit('close');
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: #F5E8C7;
  padding: 2rem;
  border-radius: 5px;
  border: 2px solid #D8C0A0;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
  width: 100%;
  max-width: 400px;
}

h4 {
  color: #3E2723;
  margin-bottom: 1.5rem;
  font-size: 1.8rem;
  text-align: center;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.form-group input {
  width: 100%;
  padding: 0.8rem;
  border: 1px solid #BCAAA4;
  border-radius: 3px;
  background-color: #FFF8E1;
  box-sizing: border-box;
}

.error-message {
  color: #D32F2F;
  margin-bottom: 1rem;
  text-align: center;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
}

.change-button, .cancel-button {
  padding: 0.8rem 1.2rem;
  border: none;
  border-radius: 5px;
  font-family: 'Cinzel', serif;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.2s ease-in-out;
}

.change-button {
  background-color: #E65100;
  color: white;
}

.change-button:hover {
  background-color: #F57C00;
}

.cancel-button {
  background-color: #795548;
  color: white;
}

.cancel-button:hover {
  background-color: #5D4037;
}
</style>
