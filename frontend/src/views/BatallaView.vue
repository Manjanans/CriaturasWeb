<script setup>
import { ref, onMounted, reactive } from 'vue';
import { useBatallaStore } from '@/stores/batallaStore';
import { useResistenciaStore } from '@/stores/resistenciaStore';
import CriaturaDisplay from '@/components/batallas/CriaturaDisplay.vue';
import IniciativaDisplay from '@/components/batallas/IniciativaDisplay.vue';

const store = useBatallaStore();
const verCriatura = ref(false);
const enviar = ref({});
const danio = reactive({
    cantidad: '',
    id: '',
    idresistencia: '',
    curar: ''
})

onMounted(async () => {
    await store.actualizaLista();
    await store.verCriaturas();
    await store.batalla();
    useResistenciaStore().cargarTipos();
});

const visualizar = async (idcriatura, id) => {
    if (id) {
        verCriatura.value = true;
        const criatura = store.criaturas.find(criatura => criatura.id === idcriatura);
        enviar.value = criatura.data;
        danio.id = id;
    }
}

const dmg = async () =>{
    await store.realizarDanio(danio);
}
</script>

<template>
    <div class="fixed inset-0 top-20 flex flex-col overflow-hidden bg-stone-900">
        <div class="flex flex-1 overflow-hidden">
            <!-- Iniciativa: 30% -->
            <div class="w-[20%] flex-none flex flex-col overflow-hidden">
                <IniciativaDisplay tipo="batalla" @idCriatura="visualizar" :store="store" />
            </div>

            <!-- Derecha: 70% -->
            <div class="w-[78%] flex-none flex flex-col overflow-hidden">

                <!-- Panel de Daño / Curación -->
                <div class="flex-none border-b border-stone-800 flex items-center px-6 py-3 gap-6">

                    <!-- Grupo: Daño -->
                    <div class="flex items-center gap-3 flex-1">
                        <label for="cantidad" class="text-sm font-fantasy text-stone-300 uppercase tracking-widest flex-none">Daño</label>
                        <input v-model="danio.cantidad" type="number" name="cantidad" placeholder="0"
                            class="w-20 bg-stone-900 text-stone-200 border border-stone-700 rounded-sm px-2 py-1.5 text-sm focus:outline-none focus:border-dnd-red transition-colors" />
                        <select v-model="danio.idresistencia"
                            class="flex-1 min-w-0 bg-stone-900 text-stone-200 border border-stone-700 rounded-sm px-2 py-1.5 text-sm focus:outline-none focus:border-dnd-red transition-colors">
                            <option value="">Tipo de daño</option>
                            <option v-for="resistencia in useResistenciaStore().tipos" :value="resistencia.id">{{ resistencia.descripcion }}</option>
                        </select>
                        <button @click="dmg"
                            class="flex-none px-4 py-1.5 bg-dnd-red/20 text-dnd-red border border-dnd-red/40 hover:bg-dnd-red/30 hover:border-dnd-red/60 rounded-sm text-sm font-bold uppercase tracking-wider transition-colors"
                        >Atacar</button>
                    </div>

                    <!-- Separador -->
                    <div class="w-px h-8 bg-stone-700 flex-none"></div>

                    <!-- Grupo: Curación -->
                    <div class="flex items-center gap-3">
                        <label for="cure" class="text-sm font-fantasy text-stone-300 uppercase tracking-widest flex-none">Curar</label>
                        <input v-model="danio.curar" type="number" name="cure" placeholder="0"
                            class="w-20 bg-stone-900 text-stone-200 border border-stone-700 rounded-sm px-2 py-1.5 text-sm focus:outline-none focus:border-emerald-600 transition-colors" />
                        <button @click="dmg"
                            class="flex-none px-4 py-1.5 bg-emerald-900/20 text-emerald-400 border border-emerald-700/40 hover:bg-emerald-900/30 hover:border-emerald-500/60 rounded-sm text-sm font-bold uppercase tracking-wider transition-colors"
                        >Curar</button>
                    </div>

                </div>

                <CriaturaDisplay :verCriatura="verCriatura" :criatura="enviar" />
            </div>
        </div>
    </div>
</template>