<script setup>
import { useInmunidadStore } from '@/stores/inmunidadStore';
import { ref, reactive, onMounted, watch } from 'vue';
import Modal from '@/Components/shared/Modal.vue';

const store = useInmunidadStore();
const agregar = ref(false);
const cid = ref(0); 

const formulario = () => {
    agregar.value = !agregar.value;
}

const props = defineProps(
    {
        show: Boolean,
        id: Number
    }
);

const accion = reactive({
    'idcriatura': cid,
    'idtipo': ""
});

const cerrar = () => {
    agregar.value = false;
    emit('cancelar');
}

onMounted(()=>{
    store.cargarTipos(); 
});

watch(
    [() => props.show, () => props.id],
    ([nuevoShow, nuevoId]) => {
        if (nuevoShow && nuevoId!==0) {
            store.actualizaInmunidades(nuevoId);
            cid.value = nuevoId;
        }
    }
)

const inmunidad = () => {
    store.agregarInmunidad(accion);
    accion.idtipo = '';
    accion.titulo = null;
    accion.descripcion = null;
}

const emit = defineEmits(['cancelar']);
</script>

<template>
    <Modal :show="show && !agregar">
        <div class="">
            <button @click="formulario">Agregar Inmunidad</button>
        </div>
        <h1>Inmunidades de Estado</h1>
        <div v-for="a in store.inmunidades" class="">
            <div class="">
                {{ a.inmunidad }}
            </div>
        </div>
        <div class="">
            <button @click="cerrar">Volver</button>
        </div>
    </Modal>
    <Modal :show="agregar">
        <form @submit.prevent="inmunidad">
            <div class="grid grid-cols-2 gap-6">
                <div class="">
                    <div class="">
                        <select v-model="accion.idtipo" name="tipo">
                            <option value="">Elige una opción...</option>
                            <option v-for="a in store.tipos" :key="a.id" :value="a.id">{{a.descripcion}}</option>
                        </select>
                        <div class="">
                            <button type="submit">Agregar Inmunidad</button>
                        </div>
                    </div>
                </div>
            </div>
        </form>
        <div class="">
            <button @click="formulario">Volver</button>
        </div>
    </Modal>
</template>