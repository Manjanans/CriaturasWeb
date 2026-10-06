<script setup>
import { reactive, ref, watch } from 'vue';
import { useCriaturaStore } from '@/stores/criaturaStore';
import Modal from '@/components/shared/Modal.vue';

const vidita = ref(true);
const mode = ref('');

const vida = () =>{
    vidita.value = !vidita.value;
}

const criatura = reactive({
    'cantdados': null,
    'tipodado': null,
    'vidatotal': null,
    'modificadorvida': null,
    'nombre': '',
    'cantexp': null,
    'publico': true,
    'id_privado': null,
    'idcriatura': null,
    'clasearmadura': null,
    'velocidad': null,
    'fuerza': null,
    'destreza': null,
    'constitucion': null,
    'inteligencia': null,
    'sabiduria': null,
    'carisma': null,
    'idcriatura': null,
    'idstat': null
});

const props = defineProps({
    show: Boolean,
    modo: String,
    id: Number
});

const limpieza = () => {
    criatura.cantdados = null;
    criatura.tipodado = null;
    criatura.vidatotal = null;
    criatura.modificadorvida = null;
    criatura.nombre = '';        
    criatura.cantexp = null;
    criatura.publico = true;
    criatura.id_privado = null;
    criatura.idcriatura = null;
    criatura.clasearmadura = null;
    criatura.velocidad = null;
    criatura.fuerza = null;
    criatura.destreza = null;
    criatura.constitucion = null;
    criatura.inteligencia = null;
    criatura.sabiduria = null;
    criatura.carisma = null;
    vidita.value = true;
    criatura.idcriatura = null;
    criatura.idstat = null;
}

const emit = defineEmits(['cancelar']);

const verificarVida = () =>{
    if(vidita.value === true){
        criatura.vidatotal = 0;
    }

    if(vidita.value === false){
        criatura.tipodado = 0;
        criatura.cantdados = 0;
        criatura.modificadorvida = 0;
    }
}

const crearCriatura = () => {
    verificarVida();
    useCriaturaStore().crearNuevaCriatura(criatura);
    limpieza();
    emit('cancelar');
}

const editar = () =>{
    verificarVida();
    useCriaturaStore().editarCriatura(criatura);
    limpieza();
    emit('cancelar');
}

watch(
        [() => props.modo, () => props.id],
        async ([nuevoModo, nuevoId]) => {
            vidita.value = true;
            mode.value = nuevoModo;

            if (nuevoModo === 'editar') {

                const edicion = await useCriaturaStore().detalleCriatura(nuevoId);

                criatura.cantdados = edicion.dados
                criatura.tipodado = edicion.tdado
                criatura.vidatotal = edicion.vida
                criatura.modificadorvida = edicion.modificador
                criatura.nombre = edicion.nombre
                criatura.cantexp = edicion.exp
                criatura.idcriatura = edicion.idcriatura
                criatura.idstat = edicion.id
                criatura.clasearmadura = edicion.armadura
                criatura.velocidad = edicion.velocidad
                criatura.fuerza = edicion.fuerza
                criatura.destreza = edicion.destreza
                criatura.constitucion = edicion.constitucion
                criatura.inteligencia = edicion.inteligencia
                criatura.sabiduria = edicion.sabiduria
                criatura.carisma = edicion.carisma
                criatura.id_privado = edicion.duenio
                criatura.publico = edicion.publico

                if (edicion.vida > 0){
                    vidita.value=false;
                }

            } else {
                limpieza();      
            }
    });

const execute = (mode) =>{
    if (mode === 'crear'){
        crearCriatura();
    }
    if (mode === 'editar'){
        editar();
    }
}

</script>
<template>
    <Modal :show="show" :title="modo === 'crear' ? 'Crear Nueva Criatura' : 'Editar Criatura'" @close="emit('cancelar')">
        <form @submit.prevent="execute(mode)">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6 p-4 bg-white border border-stone-300 rounded shadow-sm">
                <div>
                    <label class="block text-xs font-bold uppercase tracking-wider text-stone-700 mb-1">¿Quieres dejarlo público?</label>
                    <select v-model="criatura.publico" required class="w-full p-2 bg-white border border-stone-400 rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner">
                        <option :value="true">Sí</option>
                        <option :value="false">No</option>
                    </select>
                </div>
                    <div>
                        <label class="block text-xs font-bold uppercase tracking-wider text-stone-700 mb-1">¿Usar fórmula de dados para HP?</label>
                        <select @change="vida" required class="w-full p-2 bg-white border border-stone-400 rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner">
                            <option :value="true">Sí</option>
                            <option :value="false">No</option>
                        </select>
                    </div>
                </div>

                <!-- Basic Info -->
                <h3 class="text-lg font-bold text-stone-700 uppercase tracking-widest border-b border-stone-300 pb-1 mb-4">Información General</h3>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
                    <div class="md:col-span-2">
                        <label class="block text-xs font-bold uppercase tracking-wider text-stone-700 mb-1">Nombre:</label>
                        <input v-model="criatura.nombre" type="text" placeholder="Ej: Dragón Rojo Anciano" required class="w-full p-2.5 bg-white border border-stone-400 rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner font-bold text-lg text-dnd-red">
                    </div>
                    <div>
                        <label class="block text-xs font-bold uppercase tracking-wider text-stone-700 mb-1">Experiencia (XP):</label>
                        <input v-model.number="criatura.cantexp" type="number" placeholder="50" required class="w-full p-2 bg-white border border-stone-400 rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner">
                    </div>
                    
                    <!-- Health Logic -->
                    <template v-if="vidita">
                        <div>
                            <label class="block text-xs font-bold uppercase tracking-wider text-stone-700 mb-1">Cant. de Dados:</label>
                            <input v-model.number="criatura.cantdados" type="number" placeholder="Ej: 8" class="w-full p-2 bg-white border border-stone-400 rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner">
                        </div>
                        <div>
                            <label class="block text-xs font-bold uppercase tracking-wider text-stone-700 mb-1">Tipo de Dado:</label>
                            <select v-model.number="criatura.tipodado" class="w-full p-2 bg-white border border-stone-400 rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner">
                                <option value="4">d4</option>
                                <option value="6">d6</option>
                                <option value="8">d8</option>
                                <option value="10">d10</option>
                                <option value="12">d12</option>
                                <option value="20">d20</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-xs font-bold uppercase tracking-wider text-stone-700 mb-1">Mod. de Vida (+):</label>
                            <input v-model.number="criatura.modificadorvida" type="number" placeholder="Ej: 16" class="w-full p-2 bg-white border border-stone-400 rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner">
                        </div>
                    </template>
                    <template v-else>
                        <div class="md:col-span-3">
                            <label class="block text-xs font-bold uppercase tracking-wider text-stone-700 mb-1">Vida Total (Fija):</label>
                            <input v-model.number="criatura.vidatotal" type="number" placeholder="Ej: 20" class="w-full p-2 bg-white border border-stone-400 rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner max-w-xs">
                        </div>
                    </template>
                </div>

                <!-- Attributes -->
                <h3 class="text-lg font-bold text-stone-700 uppercase tracking-widest border-b border-stone-300 pb-1 mb-4">Atributos y Estadísticas</h3>
                <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
                    <div>
                        <label class="block text-xs font-bold uppercase tracking-wider text-stone-700 mb-1">Armadura (CA):</label>
                        <input v-model.number="criatura.clasearmadura" type="number" placeholder="10" required class="w-full p-2 bg-white border border-stone-400 rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner font-bold text-center">
                    </div>
                    <div>
                        <label class="block text-xs font-bold uppercase tracking-wider text-stone-700 mb-1">Velocidad (pies):</label>
                        <input v-model.number="criatura.velocidad" type="number" placeholder="30" required class="w-full p-2 bg-white border border-stone-400 rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner text-center">
                    </div>
                </div>
                
                <div class="grid grid-cols-2 md:grid-cols-6 gap-3 mb-8 bg-stone-100 p-4 border border-stone-300 rounded-sm">
                    <div>
                        <label class="block text-[10px] font-bold uppercase tracking-widest text-dnd-red mb-1 text-center">STR</label>
                        <input v-model.number="criatura.fuerza" type="number" placeholder="10" required class="w-full p-2 bg-white border border-dnd-gold rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner font-bold text-center text-lg">
                    </div>
                    <div>
                        <label class="block text-[10px] font-bold uppercase tracking-widest text-dnd-red mb-1 text-center">DEX</label>
                        <input v-model.number="criatura.destreza" type="number" placeholder="10" required class="w-full p-2 bg-white border border-dnd-gold rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner font-bold text-center text-lg">
                    </div>
                    <div>
                        <label class="block text-[10px] font-bold uppercase tracking-widest text-dnd-red mb-1 text-center">CON</label>
                        <input v-model.number="criatura.constitucion" type="number" placeholder="10" required class="w-full p-2 bg-white border border-dnd-gold rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner font-bold text-center text-lg">
                    </div>
                    <div>
                        <label class="block text-[10px] font-bold uppercase tracking-widest text-dnd-red mb-1 text-center">INT</label>
                        <input v-model.number="criatura.inteligencia" type="number" placeholder="10" required class="w-full p-2 bg-white border border-dnd-gold rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner font-bold text-center text-lg">
                    </div>
                    <div>
                        <label class="block text-[10px] font-bold uppercase tracking-widest text-dnd-red mb-1 text-center">WIS</label>
                        <input v-model.number="criatura.sabiduria" type="number" placeholder="10" required class="w-full p-2 bg-white border border-dnd-gold rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner font-bold text-center text-lg">
                    </div>
                    <div>
                        <label class="block text-[10px] font-bold uppercase tracking-widest text-dnd-red mb-1 text-center">CHA</label>
                        <input v-model.number="criatura.carisma" type="number" placeholder="10" required class="w-full p-2 bg-white border border-dnd-gold rounded-sm focus:border-dnd-red focus:ring-1 focus:ring-dnd-red outline-none text-stone-900 shadow-inner font-bold text-center text-lg">
                    </div>
                </div>

                <!-- Footer Actions -->
                <div class="flex flex-row-reverse space-x-3 space-x-reverse border-t-2 border-stone-300 pt-4 mt-6">
                    <button type="submit" class="px-6 py-3 bg-dnd-red text-parchment font-bold text-sm tracking-widest uppercase border border-dnd-gold hover:bg-[#6b0000] transition-colors shadow-lg rounded-sm">
                        {{ modo === 'crear' ? 'Guardar Criatura' : 'Actualizar Criatura' }}
                    </button>
                </div>
            </form>
    </Modal>
</template>