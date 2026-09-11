<script setup>
import { useResistenciaStore } from '@/stores/resistenciaStore';
import { ref, reactive, onMounted, watch } from 'vue';
import Modal from '@/Components/shared/Modal.vue';

const store = useResistenciaStore();
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
            store.actualizaResistencias(nuevoId);
            cid.value = nuevoId;
        }
    }
)

const acciones = () => {
    store.agregarResistencia(resistencia);
    resistencia.idtipo = '';
    resistencia.cantidad = "";
}

const emit = defineEmits(['cancelar']);
</script>

<template>
    <Modal :show="show && !agregar">
        <div class="">
            <button @click="formulario">Agregar resistencia</button>
        </div>
        <h1>Resistencias</h1>
        <div v-for="a in store.resistencias" class="">
            <div class="">
                {{ a.resist }} - <span> {{ a.valor === 0.0 ? 'Inmune': a.valor === 0.5 ? 'Resistente' : 'Débil' }} </span>
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
                        <label for="">Selecciona un tipo de daño:</label>
                        <select v-model="resistencia.idtipo" name="tipo">
                            <option value="">Elige una opción...</option>
                            <option v-for="a in store.tipos" :key="a.id" :value="a.id">{{a.descripcion}}</option>
                        </select>
                    </div>
                    <div class="">
                        <label for="">Selecciona el tipo:</label>
                        <select v-model="resistencia.cantidad" name="" id="">
                            <option value="">Inm/res/wea</option>
                            <option value="0">Inmune</option>
                            <option value="0.5">Resistente</option>
                            <option value="2.0">Débil</option>
                        </select>
                    </div>

                    <br>
                    <div class=""></div>
                </div>
                <div class="">
                    <div class="">
                        <button type="submit">Agregar resistencia</button>
                    </div>
                </div>
            </div>
        </form>
        <div class="">
            <button @click="formulario">Volver</button>
        </div>
    </Modal>
</template>