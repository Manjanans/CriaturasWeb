<script setup>
import { ref, onMounted } from 'vue';
import { apiFetch } from '@/utils/shared';
import { useAuthStore } from '@/utils/auth';
import CriaturaModal from '@/components/criaturas/CriaturaModal.vue';

const auth = useAuthStore();
const token = auth.accessToken;

const mostrarModal = ref(false);
const criaturas = ref([]);
const detalles = ref([]);
const abiertos = ref([]);

onMounted(async () => {
    const token = auth.accessToken;
    criaturas.value = await apiFetch(token, '/criaturas/');
});

const verDetalle = async (id) => {
   
    if (!detalles.value[id]) {
        detalles.value[id] = await apiFetch(
            token,
            `/criaturas/ver_criatura/${id}`
        );        
    }

    if (abiertos.value.includes(id)) {
        abiertos.value = abiertos.value.filter(i => i !== id);
    } else {
        abiertos.value.push(id);
    }
}

const crearCriatura = ()=>{
    mostrarModal.value = !mostrarModal.value;
}
</script>

<template>
    <div v-if="!mostrarModal" class="">
        <div class="">
            <button @click="crearCriatura">Crear criatura</button>
        </div>
        <div v-for="c in criaturas" class="" :key="c.id">
            <div class="" name="general">
                {{ c.nombre }} - Tipo dado: {{ c.tipo }} - Cantidad de dados: {{ c.dados }} - Vida Total: {{ c.vida }} <button @click="verDetalle(c.id)">Ver detalle</button>
            </div>
            <div v-if="abiertos.includes(c.id)" class="" name="detalle">Clase Armadura (CA): {{ detalles[c.id]?.armadura }}</div>
        </div>
    </div>

    <CriaturaModal :show="mostrarModal" @cancelar="crearCriatura" />
</template>
