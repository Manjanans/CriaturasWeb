<script setup>
import { useInmunidadStore } from '@/stores/inmunidadStore';
import { ref, reactive, onMounted, watch } from 'vue';
import Modal from '@/Components/shared/Modal.vue';
import ModalCreate from '@/Components/shared/ModalCreate.vue';
import ModalDelete from '@/Components/shared/ModalDelete.vue';

const store = useInmunidadStore();
const agregar = ref(false);
const cid = ref(0);
const elimn = ref(false);
const aidi = ref('');
const title = ref('');

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

onMounted(() => {
    store.cargarTipos();
});

watch(
    [() => props.show, () => props.id],
    ([nuevoShow, nuevoId]) => {
        if (nuevoShow && nuevoId !== 0) {
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

const verElimn = (id, titul) => {
    aidi.value = id;
    title.value = titul;
    elimn.value = !elimn.value;
}

const eliminar = (id) => {
    store.eliminarInmunidad(id, cid.value);
    elimn.value = !elimn.value;
}

const emit = defineEmits(['cancelar']);
</script>

<template>
    <Modal :show="show && !agregar && !elimn" title="Inmunidades" @close="emit('cancelar')">
        <div class="flex justify-between items-center pb-2 mb-4">
            <h2 class="text-2xl font-fantasy text-dnd-red font-bold uppercase tracking-widest"></h2>
            <button @click="formulario"
                class="px-3 py-1 bg-dnd-red text-parchment text-xs font-bold uppercase tracking-wider rounded-sm border border-dnd-gold hover:bg-[#6b0000] transition-colors shadow-sm">+
                Agregar</button>
        </div>

        <div class="max-h-64 overflow-y-auto pr-2 space-y-2 mb-4">
            <div v-for="a in store.inmunidades" :key="a.id"
                class="flex justify-between items-center bg-white p-2 rounded-sm border border-stone-200 shadow-sm hover:border-dnd-gold transition-colors">
                <div class="font-bold text-stone-800 text-sm">
                    {{ a.inmunidad }}
                </div>
                <div class="flex space-x-2">
                    <button @click="verElimn(a.id, a.inmunidad)"
                        class="text-[10px] uppercase tracking-wider text-dnd-red hover:text-[#6b0000] font-bold">Eliminar</button>
                </div>
            </div>
            <div v-if="store.inmunidades.length === 0" class="text-center text-stone-400 italic text-sm py-4">No hay
                inmunidades registradas.</div>
        </div>
    </Modal>

    <ModalCreate :show="agregar" title="Agregar Inmunidad" @close="formulario">
        <form @submit.prevent="inmunidad">
            <div class="space-y-4 mb-6">
                <div>
                    <label class="block text-xs font-bold uppercase tracking-wider text-stone-700 mb-1">Selecciona el
                        Estado/Daño:</label>
                    <select v-model="accion.idtipo" name="tipo"
                        class="w-full p-2 bg-white border border-stone-400 rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner">
                        <option value="">Elige una opción...</option>
                        <option v-for="a in store.tipos" :key="a.id" :value="a.id">{{ a.descripcion }}</option>
                    </select>
                </div>
            </div>

            <div class="flex flex-row-reverse space-x-2 space-x-reverse">
                <button type="submit"
                    class="px-4 py-2 bg-dnd-red text-parchment font-bold text-xs tracking-wider uppercase border border-dnd-gold hover:bg-[#6b0000] transition-colors shadow-md rounded-sm">
                    Confirmar
                </button>
                <button type="button" @click="formulario"
                    class="px-4 py-2 bg-white text-stone-700 font-bold text-xs tracking-wider uppercase border border-stone-300 hover:bg-stone-50 transition-colors shadow-sm rounded-sm">
                    Cancelar
                </button>
            </div>
        </form>
    </ModalCreate>

    <ModalDelete :show="elimn" title="Eliminar Inmunidad" @close="verElimn('', '')">
        <p class="mb-6">¿Estás seguro de eliminar <span class="font-bold text-dnd-red">{{ title }}</span>?</p>
        <div class="flex flex-row-reverse space-x-2 space-x-reverse">
            <button @click="eliminar(aidi)"
                class="px-5 py-2.5 bg-dnd-red text-parchment font-bold text-sm tracking-wider uppercase border border-dnd-gold hover:bg-[#6b0000] transition-colors shadow-md rounded-sm">Sí,
                Eliminar</button>
            <button @click="verElimn('', '')"
                class="px-5 py-2.5 bg-white text-stone-700 font-bold text-sm tracking-wider uppercase border border-stone-300 hover:bg-stone-50 transition-colors shadow-sm rounded-sm">No,
                Cancelar</button>
        </div>
    </ModalDelete>
</template>