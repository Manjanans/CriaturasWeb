<template>
  <div v-if="show" class="modal-overlay" @click.self="close">
    <div class="modal-content">
      <h4>{{ message }}</h4>
      <div class="modal-actions">
        <button @click="close" class="close-button">Cerrar</button>
      </div>
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
}

.modal-content {
  background-color: #F5E8C7;
  padding: 2rem;
  border-radius: 5px;
  border: 2px solid #D8C0A0;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
  width: 100%;
  max-width: 400px;
  text-align: center;
}

h4 {
  color: #3E2723;
  margin-bottom: 1.5rem;
  font-size: 1.8rem;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
}

.close-button {
  background-color: #795548;
  color: white;
  padding: 0.8rem 1.2rem;
  border: none;
  border-radius: 5px;
  font-family: 'Cinzel', serif;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.2s ease-in-out;
}

.close-button:hover {
  background-color: #5D4037;
}
</style>
