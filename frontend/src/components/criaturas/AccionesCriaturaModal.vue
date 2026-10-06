<script setup>
import { useAccioneStore } from '@/stores/accioneStore';
import { ref, reactive, onMounted, watch } from 'vue';
import Modal from '@/Components/shared/Modal.vue';
import ModalCreate from '@/Components/shared/ModalCreate.vue';
import ModalDelete from '@/Components/shared/ModalDelete.vue';

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

    if (tipo === '') {
        accion.id = null,
            accion.idcriatura = cid,
            accion.idtipo = "",
            accion.titulo = null,
            accion.descripcion = null
    }
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

onMounted(() => {
    store.cargarTipos();
});

watch(
    [() => props.show, () => props.id],
    ([nuevoShow, nuevoId]) => {
        if (nuevoShow && nuevoId !== 0) {
            store.actualizaHabilidades(nuevoId);
            cid.value = nuevoId;
        }
    }
);

const acciones = () => {
    if (modo.value === 'crear') {
        store.agregarAccion(accion);
        accion.idtipo = '';
        accion.titulo = null;
        accion.descripcion = null;
        store.actualizaHabilidades(cid.value);
    }
    if (modo.value === 'editar') {
        store.agregarAccion(accion);
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

const eliminar = (id) => {
    store.eliminarAccion(id);
    store.actualizaHabilidades(cid.value);
    elimn.value = !elimn.value;
}

const verElim = (id, titulo) => {
    elimn.value = !elimn.value;
    aidi.value = id;
    title.value = titulo
}

const emit = defineEmits(['cancelar']);
</script>

<template>
    <Modal :show="show && !agregar && !elimn" title="Acciones y Habilidades" @close="emit('cancelar')">
        <div class="flex justify-between items-center pb-2 mb-4">
            <h2 class="text-2xl font-fantasy text-dnd-red font-bold uppercase tracking-widest"></h2>
            <button @click="formulario('crear')"
                class="px-3 py-1 bg-dnd-red text-parchment text-xs font-bold uppercase tracking-wider rounded-sm border border-dnd-gold hover:bg-[#6b0000] transition-colors shadow-sm">+
                Agregar</button>
        </div>

        <div class="max-h-96 overflow-y-auto pr-3 space-y-6 mb-4">
            <!-- Habilidades Section -->
            <div>
                <h3
                    class="text-lg font-bold text-stone-700 uppercase tracking-widest border-b border-stone-300 pb-1 mb-3">
                    Habilidades de Combate
                </h3>
                <div class="space-y-3">
                    <div v-for="a in store.habilidades" :key="a.id"
                        class="bg-white p-3 rounded-sm border border-stone-200 shadow-sm relative group">
                        <div class="pr-16">
                            <span class="font-bold text-dnd-red">{{ a.titulo }}.</span>
                            <span class="italic text-stone-800 text-sm ml-1">{{ a.detalle }}</span>
                        </div>
                        <div
                            class="absolute top-3 right-3 flex flex-col space-y-1 opacity-0 group-hover:opacity-100 transition-opacity">
                            <button @click="editar(a.id, a.titulo, a.detalle, 1)"
                                class="text-[10px] uppercase tracking-wider text-stone-500 hover:text-dnd-gold-light font-bold text-right">Editar</button>
                            <button @click="verElim(a.id, a.titulo)"
                                class="text-[10px] uppercase tracking-wider text-dnd-red hover:text-[#6b0000] font-bold text-right">Eliminar</button>
                        </div>
                    </div>
                    <div v-if="store.habilidades.length === 0" class="text-stone-400 italic text-sm py-2">No hay
                        habilidades registradas.</div>
                </div>
            </div>

            <!-- Acciones Section -->
            <div>
                <h3
                    class="text-lg font-bold text-stone-700 uppercase tracking-widest border-b border-stone-300 pb-1 mb-3">
                    Acciones</h3>
                <div class="space-y-3">
                    <div v-for="a in store.acciones" :key="a.id"
                        class="bg-white p-3 rounded-sm border border-stone-200 shadow-sm relative group">
                        <div class="pr-16">
                            <span class="font-bold text-dnd-red">{{ a.titulo }}.</span>
                            <span class="italic text-stone-800 text-sm ml-1">{{ a.detalle }}</span>
                        </div>
                        <div
                            class="absolute top-3 right-3 flex flex-col space-y-1 opacity-0 group-hover:opacity-100 transition-opacity">
                            <button @click="editar(a.id, a.titulo, a.detalle, 2)"
                                class="text-[10px] uppercase tracking-wider text-stone-500 hover:text-dnd-gold-light font-bold text-right">Editar</button>
                            <button @click="verElim(a.id, a.titulo)"
                                class="text-[10px] uppercase tracking-wider text-dnd-red hover:text-[#6b0000] font-bold text-right">Eliminar</button>
                        </div>
                    </div>
                    <div v-if="store.acciones.length === 0" class="text-stone-400 italic text-sm py-2">No hay acciones
                        registradas.</div>
                </div>
            </div>
        </div>
    </Modal>

    <ModalCreate :show="agregar" :title="modo === 'crear' ? 'Agregar Acción/Habilidad' : 'Editar Acción/Habilidad'"
        @close="formulario('')">
        <form @submit.prevent="acciones">
            <div class="space-y-4 mb-6">
                <div>
                    <label class="block text-xs font-bold uppercase tracking-wider text-stone-700 mb-1">Tipo:</label>
                    <select v-model="accion.idtipo" name="tipo"
                        class="w-full p-2 bg-white border border-stone-400 rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner">
                        <option value="">Elige una opción...</option>
                        <option v-for="a in store.tipos" :key="a.id" :value="a.id">{{ a.descripcion }}</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-bold uppercase tracking-wider text-stone-700 mb-1">Título:</label>
                    <input v-model="accion.titulo" type="text" placeholder="Ej: Multiataque" required
                        class="w-full p-2 bg-white border border-stone-400 rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner font-bold">
                </div>
                <div>
                    <label
                        class="block text-xs font-bold uppercase tracking-wider text-stone-700 mb-1">Descripción:</label>
                    <textarea v-model="accion.descripcion" rows="4"
                        placeholder="Ej: El goblin realiza dos ataques cuerpo a cuerpo..." required
                        class="w-full p-2 bg-white border border-stone-400 rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner italic"></textarea>
                </div>
            </div>

            <div class="flex flex-row-reverse space-x-2 space-x-reverse">
                <button type="submit"
                    class="px-4 py-2 bg-dnd-red text-parchment font-bold text-xs tracking-wider uppercase border border-dnd-gold hover:bg-[#6b0000] transition-colors shadow-md rounded-sm">
                    Guardar
                </button>
                <button type="button" @click="formulario('')"
                    class="px-4 py-2 bg-white text-stone-700 font-bold text-xs tracking-wider uppercase border border-stone-300 hover:bg-stone-50 transition-colors shadow-sm rounded-sm">
                    Cancelar
                </button>
            </div>
        </form>
    </ModalCreate>

    <ModalDelete :show="elimn" title="Eliminar Elemento" @close="verElim(aidi, title)">

        <p class="mb-6">¿Estás seguro de eliminar <span class="font-bold text-dnd-red">{{ title }}</span>?</p>
        <div class="flex flex-row-reverse space-x-2 space-x-reverse">
            <button @click="eliminar(aidi)"
                class="px-5 py-2.5 bg-dnd-red text-parchment font-bold text-sm tracking-wider uppercase border border-dnd-gold hover:bg-[#6b0000] transition-colors shadow-md rounded-sm">Sí,
                Eliminar</button>
            <button @click="verElim(aidi, title)"
                class="px-5 py-2.5 bg-white text-stone-700 font-bold text-sm tracking-wider uppercase border border-stone-300 hover:bg-stone-50 transition-colors shadow-sm rounded-sm">No,
                Cancelar</button>
        </div>
    </ModalDelete>
</template>