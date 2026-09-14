<script setup>
import { useResistenciaStore } from '@/stores/resistenciaStore';
import { ref, reactive, onMounted, watch } from 'vue';
import Modal from '@/Components/shared/Modal.vue';

const store = useResistenciaStore();
const agregar = ref(false);
const cid  = ref(0);
const modo = ref('');
const aidi = ref('');
const title = ref('');
const elimn = ref(false);

const formulario = (mode) => {
    agregar.value = !agregar.value;
    modo.value = mode;
}

const props = defineProps(
    {
        show: Boolean,
        id: Number
    }
);

const resistencia = reactive({
    'id': '',
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
    if (modo.value === 'crear'){
        store.agregarResistencia(resistencia);
        resistencia.idtipo = '';
        resistencia.cantidad = "";
    }
    if (modo.value === 'editar'){
        store.editarResistencia(resistencia);
        resistencia.idtipo = '';
        resistencia.cantidad = "";
        formulario('');
    }
}

const editar = (id, idh, mod) =>{
    resistencia.id = id;
    resistencia.idtipo = idh;
    resistencia.cantidad = mod;
    formulario('editar');
}

const verElim = (id, hab) =>{
    elimn.value = !elimn.value;
    aidi.value = id;
    title.value = hab;
}

const eliminar = (id) =>{
    store.eliminarResistencia(id, cid.value);
    elimn.value = !elimn.value;
}

const emit = defineEmits(['cancelar']);
</script>

<template>
    <Modal :show="show && !agregar && !elimn">
        <div class="">
            <button @click="formulario('crear')">Agregar resistencia</button>
        </div>
        <h1>Resistencias</h1>
        <div v-for="a in store.resistencias" class="">
            <div class="">
                {{ a.resist }} - <span> {{ a.valor === 0.0 ? 'Inmune': a.valor === 0.5 ? 'Resistente' : 'Débil' }} </span> <button @click="editar(a.id, a.idtipodanio, a.valor)">Editar Resistencia</button> <button @click="verElim(a.id, a.resist)">Eliminar Resistencia</button>
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
                    <div v-if="modo === 'crear'" class="">
                         <div class="">
                            <button type="submit">Agregar Resistencia</button>
                        </div>
                    </div>
                   
                    <div v-else class="">
                        <div class="">
                            <button type="submit">Editar Resistencia</button>
                        </div>
                    </div>
                </div>
            </div>
        </form>
        <div class="">
            <button @click="formulario('')">Volver</button>
        </div>
    </Modal>
    <Modal :show="elimn">
        <div class="">
            <p>¿Estás seguro de eliminar {{ title }}?</p>
        </div>
        <div class="">
            <button @click="eliminar(aidi)">Sí</button>
        </div>
        <div class="">
            <button @click="verElim(aidi, title)">No</button>
        </div>
    </Modal>
</template>