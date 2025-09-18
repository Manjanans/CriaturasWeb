<template>
  <div v-if="show" class="modal-overlay" @click.self="close">
    <div class="modal-content">
      <h4>Error de Autenticación</h4>
      <p>{{ message }}</p>
      <button @click="close" class="close-button">Cerrar</button>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  show: Boolean,
  message: String
});

const emit = defineEmits(['close']);

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
  z-index: 1000;
}

.modal-content {
  background-color: #F5E8C7; /* Parchment */
  padding: 2rem;
  border-radius: 5px;
  border: 2px solid #D8C0A0;
  box-shadow: 0 5px 15px rgba(0,0,0,0.5);
  width: 90%;
  max-width: 350px;
  text-align: center;
}

h4 {
  color: #B71C1C; /* Deep Red */
  margin-top: 0;
  font-size: 1.5rem;
}

p {
  color: #3E2723; /* Dark Brown */
  margin-bottom: 1.5rem;
}

.close-button {
  padding: 0.7rem 1.5rem;
  border: none;
  border-radius: 5px;
  background-color: #795548; /* Brown */
  color: white;
  font-family: 'Cinzel', serif;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.2s ease-in-out;
}

.close-button:hover {
  background-color: #5D4037;
}
</style>