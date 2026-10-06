<script setup>
import { ref, onMounted, watch } from 'vue';
import ModalDelete from '@/Components/shared/ModalDelete.vue';
import { useIniciativaStore } from '@/stores/iniciativaStore';

const editar = (tipo, id, cambio) => {
    store.editarIniciativa(tipo, id, cambio);
}

const props = defineProps({
    tipo: String,
    store: Object
})

watch([() => props.store], async (nstore) => {
    await nstore.batalla();
});

const elimn = ref(false);
const finish = ref(false);
const nombre = ref('');
const id = ref(0);

const eliminar = (aidi, name) => {
    nombre.value = name;
    id.value = aidi;
    elimn.value = !elimn.value;
}

const quitar_iniciativa = async (aidi) => {
    await useIniciativaStore().eliminarIniciativa(aidi);
    await props.store.actualizaLista();
    elimn.value = !elimn.value;
}

const emit = defineEmits(['idCriatura']);

const visualizar = (idcriatura, tipo, id) => {
    if (tipo === 'batalla') {
        emit('idCriatura', idcriatura, id);
    }
}

const finalizar = () =>{
    finish.value = !finish.value;
}

const finishBattle = async () =>{
    await props.store.finalizarBatalla();
    finalizar();
}

const nextTurn = async () => {
    const total = props.store.iniciativa.length;
    if (total === 0) return;
    const currentIndex = props.store.turno?.index_tabla ?? 0;
    const nextIndex = (currentIndex + 1) % total;
    await props.store.siguienteTurno(props.store.turno.id, nextIndex);
}
</script>

<template>
    <div class="w-full h-full border-r border-stone-800 flex flex-col overflow-hidden">
        <div class="px-4 pt-4 pb-3 border-b border-stone-800 flex items-center justify-between">
            <h3 class="text-stone-300 font-fantasy font-bold uppercase tracking-widest text-[16px]">Iniciativa</h3>
            <span v-if="props.tipo === 'dashboard'" class="text-[12px] text-stone-600 font-bold uppercase tracking-widest">{{ store.iniciativa.length }} en cola</span>
        </div>

        <div v-if="props.tipo === 'batalla'" class="px-3 py-2 border-b border-stone-800">
            <div class="flex items-center justify-center gap-2 py-1 mb-2">
                <span class="text-stone-500 font-fantasy font-bold uppercase tracking-widest text-[13px]">Turno</span>
                <span class="text-dnd-gold-light font-fantasy font-black text-[20px]">{{ store.turno?.numturno }}</span>
            </div>
            <button
                @click="nextTurn"
                class="w-full flex items-center justify-center gap-2 px-3 py-2 bg-dnd-gold/10 hover:bg-dnd-gold/20 text-dnd-gold-light border border-dnd-gold/30 hover:border-dnd-gold/60 rounded-sm text-[14px] font-black uppercase tracking-widest transition-colors"
            >
                <span>▶</span> Siguiente turno
            </button>
        </div>

        <div v-if="store.iniciativa.length === 0" class="flex-1 flex flex-col items-center justify-center gap-3">
            <span class="text-3xl opacity-20">⚔️</span>
            <p class="text-stone-600 text-[14px] font-bold uppercase tracking-widest text-center px-4 leading-relaxed">El orden de<br>iniciativa aparecerá aquí</p>
        </div>

        <div v-else class="flex-1 overflow-y-auto divide-y divide-stone-800/60">
            <div
                v-for="(i, idx) in store.iniciativa"
                :key="i.id"
                :class="[
                    'group px-3 py-3 transition-colors',
                    idx === store.turno?.index_tabla
                        ? 'bg-dnd-red/10 border-l-2 border-dnd-red'
                        : 'hover:bg-stone-800/40 border-l-2 border-transparent'
                ]"
                @click="visualizar(i.idcriatura, tipo, i.id)"
            >
                <!-- Línea principal: orden + valor + nombre -->
                <div class="flex items-center gap-2">
                    <span
                        :class="[
                            'text-[12px] font-black w-4 text-center flex-none select-none',
                            idx === store.turno?.index_tabla ? 'text-dnd-red' : 'text-stone-600'
                        ]"
                    >{{ idx + 1 }}</span>

                    <div v-if="tipo === 'dashboard'" class="">
                        <input
                            :value="i.valoriniciativa"
                            type="number"
                            @change="editar('value', i.id, $event.target.value)"
                            class="w-11 bg-dnd-red/10 text-dnd-red font-black text-[16px] text-center border border-dnd-red/30 rounded-sm px-1 py-0.5 focus:outline-none focus:border-dnd-red focus:bg-dnd-red/20 transition-colors flex-none"
                        >
                        <input
                            :value="i.nombrecriatura"
                            @change="editar('name', i.id, $event.target.value)"
                            class="flex-1 min-w-0 bg-transparent text-stone-200 text-[14px] font-bold border-b border-transparent hover:border-stone-700 focus:border-dnd-red focus:outline-none transition-colors py-0.5"
                        >
                    </div>

                    <div v-else class="flex items-center gap-2 flex-1 min-w-0">
                        <span class="w-11 bg-dnd-red/10 text-dnd-red font-black text-[16px] text-center border border-dnd-red/30 rounded-sm px-1 py-0.5 flex-none">
                            {{ i.valoriniciativa }}
                        </span>
                        <span
                            :class="[
                                'flex-1 min-w-0 text-[14px] font-bold truncate py-0.5',
                                idx === store.turno?.index_tabla ? 'text-stone-100' : 'text-stone-200'
                            ]"
                        >
                            {{ i.nombrecriatura }}
                        </span>
                    </div>

                    <button @click.stop="eliminar(i.id, i.nombrecriatura)"
                        class="ml-auto text-stone-700 hover:text-dnd-red text-[14px] transition-colors flex-none">✕</button>
                </div>

                <!-- Sub-línea: badge + hp si monstruo -->
                <div class="flex items-center gap-2 mt-1.5 pl-6">
                    <span
                        v-if="i.idcriatura"
                        class="text-[11px] font-black uppercase tracking-widest text-dnd-red bg-dnd-red/10 border border-dnd-red/20 rounded-sm px-1.5 py-0.5 flex-none"
                    >Monstruo</span>
                    <span
                        v-else
                        class="text-[11px] font-black uppercase tracking-widest text-sky-500 bg-sky-500/10 border border-sky-500/20 rounded-sm px-1.5 py-0.5 flex-none"
                    >Jugador</span>

                    <div v-if="i.idcriatura" class="flex items-center gap-1">
                        <span class="text-stone-600 text-[12px]">❤</span>
                        <div v-if="tipo === 'dashboard'" class="">
                            <input
                                :value="i.vida"
                                type="number"
                                @change="editar('hp', i.id, $event.target.value)"
                                class="w-14 bg-stone-900 text-stone-300 text-[14px] text-center border border-stone-700 rounded-sm px-1 py-0.5 focus:outline-none focus:border-dnd-red transition-colors"
                            >
                        </div>
                        <div v-else class="">
                            <span class="w-14 bg-stone-900 text-stone-300 text-[14px] text-center border border-stone-700 rounded-sm px-1 py-0.5">
                                {{ i.vida }}
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="props.tipo === 'batalla'" class="px-3 py-2 border-t border-stone-800">
            <button @click="finalizar"
                class="w-full flex items-center justify-center gap-2 px-3 py-2 bg-red-900/20 hover:bg-red-900/40 text-red-400 border border-red-700/40 hover:border-red-500/60 rounded-sm text-[14px] font-black uppercase tracking-widest transition-colors"
            >Finalizar Batalla</button>
        </div>
    </div>

    <ModalDelete :show="elimn" title="Eliminar de la Iniciativa" @close="eliminar('', '')">
        <p class="mb-6">¿Estás seguro de eliminar <span class="font-bold text-dnd-red">{{ nombre }}</span> de la iniciativa?</p>
        <div class="flex flex-row-reverse space-x-2 space-x-reverse">
            <button @click="quitar_iniciativa(id)"
                class="px-5 py-2.5 bg-dnd-red text-parchment font-bold text-sm tracking-wider uppercase border border-dnd-gold hover:bg-[#6b0000] transition-colors shadow-md rounded-sm">Sí,
                Eliminar</button>
            <button @click="eliminar('', '')"
                class="px-5 py-2.5 bg-white text-stone-700 font-bold text-sm tracking-wider uppercase border border-stone-300 hover:bg-stone-50 transition-colors shadow-sm rounded-sm">No,
                Cancelar</button>
        </div>
    </ModalDelete>
    <ModalDelete :show="finish" title="Finalizar batalla" @close="finalizar">
        <p class="mb-6">¿Estás seguro de finalizar la batalla?</p>
        <div class="flex flex-row-reverse space-x-2 space-x-reverse">
            <button @click="finishBattle"
                class="px-5 py-2.5 bg-dnd-red text-parchment font-bold text-sm tracking-wider uppercase border border-dnd-gold hover:bg-[#6b0000] transition-colors shadow-md rounded-sm">Sí,
                Eliminar</button>
            <button @click="finalizar"
                class="px-5 py-2.5 bg-white text-stone-700 font-bold text-sm tracking-wider uppercase border border-stone-300 hover:bg-stone-50 transition-colors shadow-sm rounded-sm">No,
                Cancelar</button>
        </div>
    </ModalDelete>
</template>