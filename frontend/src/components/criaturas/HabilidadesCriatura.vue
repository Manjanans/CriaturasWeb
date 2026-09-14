<script setup>
import { useHabilidadStore } from '@/stores/habilidadStore'; 
import { ref, reactive, onMounted, watch } from 'vue';
import Modal from '@/Components/shared/Modal.vue';

const store = useHabilidadStore();
const agregar = ref(false);
const cid  = ref(0);
const elimn = ref(false);
const aidi = ref(0);
const title = ref('');
const modo = ref('');

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
    'id': "",
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
            store.actualizaHabilidades(nuevoId);
            cid.value = nuevoId;
        }
    }
)

const acciones = () => {
    if (modo.value === 'crear'){
        store.agregarHabilidad(resistencia);
        resistencia.idtipo = '';
        resistencia.cantidad = "";
    }
    if (modo.value === 'editar'){
        store.editarHabilidad(resistencia);
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
    store.eliminarHabilidad(id, cid.value);
    elimn.value = !elimn.value;
}

const emit = defineEmits(['cancelar']);
</script>

<template>
    <Modal :show="show && !agregar && !elimn">
        <div class="">
            <button @click="formulario('crear')">Agregar Habilidad</button>
        </div>
        <h1>Habilidades</h1>
        <div v-for="a in store.habilidades" class="" :key="a.id">
            <div class="">
                {{ a.habilidad }}: {{a.modif}} <button @click="editar(a.id, a.idhabilidad, a.modif)">Editar Habilidad</button> <button @click="verElim(a.id, a.habilidad)"> Eliminar Habilidad</button>
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
                        <label for="">Selecciona la Habilidad:</label>
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
                    <div v-if="modo === 'crear'" class="">
                         <div class="">
                            <button type="submit">Agregar Habilidad</button>
                        </div>
                    </div>
                   
                    <div v-else class="">
                        <div class="">
                            <button type="submit">Editar Habilidad</button>
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