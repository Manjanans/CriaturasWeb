<script setup>
import { useAccioneStore } from '@/stores/accioneStore';
import { ref, reactive, onMounted, watch } from 'vue';
import Modal from '@/Components/shared/Modal.vue';

const store = useAccioneStore();
const agregar = ref(false);
const cid = ref(0);
const modo = ref(''); 
const aidi = ref(0);
const title = ref('');
const elimn = ref(false);

const formulario = (tipo) => {
    agregar.value = !agregar.value;
    modo.value = tipo;
}

const props = defineProps(
    {
        show: Boolean,
        id: Number
    }
);

const accion = reactive({
    'id': null,
    'idcriatura': cid,
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
            cid.value = nuevoId;
        }
    }
);

const acciones = () => {
    if (modo.value === 'crear'){
        store.agregarHabilidad(accion);
        accion.idtipo = '';
        accion.titulo = null;
        accion.descripcion = null;
        store.actualizaHabilidades(cid.value);
    }
    if (modo.value === 'editar'){
        store.editarHabilidad(accion);
        accion.idtipo = '';
        accion.titulo = null;
        accion.descripcion = null;
        store.actualizaHabilidades(cid.value);
        formulario('');
    }
}

const editar = (id, titulo, detalle, tipo) => {
    accion.titulo = titulo;
    accion.descripcion = detalle;
    accion.id = id;
    accion.idtipo = tipo;
    formulario('editar');
}

const eliminar = (id) =>{
    store.eliminarAccion(id);
    store.actualizaHabilidades(cid.value);
    elimn.value = !elimn.value;
}

const verElim = (id, titulo) =>{
    elimn.value = !elimn.value;
    aidi.value = id;
    title.value = titulo
}

const emit = defineEmits(['cancelar']);
</script>

<template>
    <Modal :show="show && !agregar && !elimn">
        <div class="">
            <button @click="formulario('crear')">Agregar acción/habilidad</button>
        </div>
        <h1>Habilidades</h1>
        <div v-for="a in store.habilidades" class="" :key="a.id">
            <div class="">
                <div class="">
                    <button @click="editar(a.id, a.titulo, a.detalle, 1)">Editar Habilidad</button>
                </div>
                <div class="">
                    <button @click="verElim(a.id, a.titulo)">Eliminar Habilidad</button>
                </div>
            </div>
            <div class="">
                {{ a.titulo }}
            </div>
            <div class="">
                {{ a.detalle }}
            </div>
        </div>
        <h1>Acciones</h1>
        <div v-for="a in store.acciones" class="" :key="a.id">
            <div class="">
                <div class="">
                    <button @click="">Editar Acción</button>
                </div>
                <div class="">
                    <button @click="verElim(a.id, a.titulo)">Eliminar Acción</button>
                </div>
            </div>
            <div class="">
                {{ a.titulo }}
            </div>
            <div class="">
                {{ a.detalle }}
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
                    <div v-if="modo === 'crear'" class="">
                        <button type="submit">Agregar acción/habilidad</button>
                    </div>
                    <div v-else class="">
                        <button type="submit">Editar acción/habilidad</button>
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