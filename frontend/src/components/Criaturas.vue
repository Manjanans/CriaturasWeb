<template>
    <div v-if="show" class="modal-overlay" @click.self="close">
        <div class="modal-content">
            <ol>
                <li v-for="criatura in criaturas" :key="criatura.id">
                    {{criatura.nombre}} - {{criatura.vida}}
                </li>
            </ol>
        </div>
        <div class="modal-actions">
            <button @click="close" class="close-button">Cerrar</button>
        </div>
        
    </div>  
</template>

<script setup>
    import { ref, onMounted } from 'vue'
    const token = localStorage.getItem('accessToken')

    const props = defineProps({
        show: Boolean
    });
    const emit = defineEmits(['close']);
    

    const criaturas = ref([])
    const cargar = async () => {
        const response = await fetch('/criaturas/', {
            headers: {
            'Authorization': `Bearer ${token}`
            }
        })
        const data = await response.json()
        criaturas.value = data
        console.log(data)
    }

    onMounted(() => {
        cargar()
    });

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
  max-width: 600px;
}

h3 {
  color: #3E2723;
  margin-bottom: 1.5rem;
  font-size: 2rem;
  text-align: center;
}

.user-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.user-info p {
  font-size: 1.2rem;
  color: #3E2723;
}

.change-password-button {
  background-color: #E65100;
  color: white;
  padding: 0.8rem 1.2rem;
  border: none;
  border-radius: 5px;
  font-family: 'Cinzel', serif;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.2s ease-in-out;
}

.change-password-button:hover {
  background-color: #F57C00;
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
