<script setup>
import { useSentidoStore } from '@/stores/sentidoStore'; 
import { ref, reactive, onMounted, watch } from 'vue';
import Modal from '@/components/shared/Modal.vue';

const store = useSentidoStore();
const agregar = ref(false);
const cid  = ref(0);

const formulario = () => {
    agregar.value = !agregar.value;
}

const props = defineProps(
    {
        show: Boolean,
        id: Number
    }
);

const resistencia = reactive({
    'idcriatura': cid,
    'idtipo': "",
    'cantidad': ""
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
            store.actualizaSentidos(nuevoId);
            cid.value = nuevoId;
        }
    }
)

const acciones = () => {
    store.agregarSentido(resistencia);
    resistencia.idtipo = '';
    resistencia.cantidad = "";
}

const emit = defineEmits(['cancelar']);
</script>

<template>
    <Modal :show="show && !agregar">
        <div class="">
            <button @click="formulario">Agregar Sentido</button>
        </div>
        <h1>Sentidos</h1>
        <div v-for="a in store.sentidos" class="">
            <div class="">
                {{ a.tiposentido }}: {{a.valor}}
            </div>
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
                        <label for="">Selecciona el sentido:</label>
                        <select v-model="resistencia.idtipo" name="tipo">
                            <option value="">Elige una opción...</option>
                            <option v-for="a in store.tipos" :key="a.id" :value="a.id">{{a.descripcion}}</option>
                        </select>
                    </div>
                    <div class="">
                        <label for="cantidad">Ingresa el modificador (solo el número):</label>
                        <input v-model.number="resistencia.cantidad" type="number" name="cantidad" placeholder="0">
                    </div>

                    <br>
                    <div class=""></div>
                </div>
                <div class="">
                    <div class="">
                        <button type="submit">Agregar Sentido</button>
                    </div>
                </div>
            </div>
        </form>
        <div class="">
            <button @click="formulario">Volver</button>
        </div>
    </Modal>
</template>