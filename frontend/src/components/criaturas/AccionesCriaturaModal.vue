<script setup>
import { useAccioneStore } from '@/stores/accioneStore';
import { ref, reactive, onMounted, watch } from 'vue';
import Modal from '@/Components/shared/Modal.vue';

const store = useAccioneStore();
const agregar = ref(false);

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
    'idcriatura': props.id,
    'idtipo': "",
    'titulo': null,
    'descripcion': null
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
            store.actualizaHabilidades(nuevoId);
        }
    }
)

const acciones = () => {
    store.agregarAccion(accion);
    accion.idtipo = '';
    accion.titulo = null;
    accion.descripcion = null;
}

const emit = defineEmits(['cancelar']);
watch(props.id, ()=>{
    console.log(props.id);
})


</script>

<template>
    <Modal :show="show && !agregar">
        <div class="">
            <button @click="formulario">Agregar acción/habilidad</button>
        </div>
        <h1>Habilidades</h1>
        <div v-for="a in store.habilidades" class="">
            <div class="">
                {{ a.id }}
            </div>
            <div class="">{{ a.detalle }}</div>
        </div>
        <h1>Acciones</h1>
        <div v-for="a in store.acciones" class="">
            <div class="">
                {{ a.titulo }}
            </div>
            <div class="">{{ a.detalle }}</div>
        </div>

        <div class="">
            <button @click="cerrar">Volver</button>
        </div>
    </Modal>
    <Modal :show="agregar">
        <form @submit.prevent="acciones">
            <div class="grid grid-cols-2 gap-6">
                <div class="">
                    <div class="">
                        <label for="">Ingresa un título:</label>
                        <input v-model="accion.titulo" type="text" placeholder="Ataque" required>
                    </div>
                    <br>
                    <div class="">
                        <label for="">Ingresa la descripción:</label>
                        <textarea v-model="accion.descripcion" name="" id="" rows="8" placeholder="Hace 2d6" required></textarea>
                    </div>
                </div>
                <div class="">
                    <select v-model="accion.idtipo" name="tipo">
                        <option value="">Elige una opción...</option>
                        <option v-for="a in store.tipos" :key="a.id" :value="a.id">{{a.descripcion}}</option>
                    </select>
                    <div class="">
                        <button type="submit">Agregar habilidad</button>
                    </div>
                </div>
            </div>
        </form>
        <div class="">
            <button @click="formulario">Volver</button>
        </div>
    </Modal>
</template>