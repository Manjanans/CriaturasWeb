<script setup>
import { ref, onMounted, reactive, watch } from 'vue';
import { useCriaturaStore } from '@/stores/criaturaStore';
import { useIniciativaStore } from '@/stores/iniciativaStore';
import IniciativaDisplay from '@/components/batallas/IniciativaDisplay.vue';
import CriaturaDisplay from '@/components/batallas/CriaturaDisplay.vue';

const store = useCriaturaStore();
const iniciativa = useIniciativaStore();
const buscador = ref('');
const verCriatura = ref(false);
const current = ref(0);

const crear = reactive({
    'name': '',
    'tipo': '',
    'vida': '',
    'iniciativa': '',
    'idcriatura': ''
})

const busqueda = () => {
    store.buscarCriatura(buscador.value);
}

const addIniciativa = () => {
    crear.idcriatura = current.value;
    iniciativa.agregarIniciativa(crear);
    crear.name = '';
    crear.tipo = '';
    crear.vida = '';
    crear.iniciativa = '';
}

const visualizar = (numero) => {
    verCriatura.value = true;
    current.value = numero.id;
}

function nombreUnico(nombre, criaturas) {
    if (!criaturas.some(c => c.nombrecriatura === nombre)) {
        return nombre;
    }

    const regex = new RegExp(`^${nombre} (\\d+)$`);

    const numeros = criaturas
        .map(c => c.nombrecriatura.match(regex)?.[1])
        .filter(Boolean)
        .map(Number);

    return `${nombre} ${Math.max(0, ...numeros) + 1}`;
}

watch(current, async (numero) => {
    if (numero === 0) {
        return
    }
    await store.verDetalle(numero);
    const des = await store.calcularModificador(store.detalles[numero].base.destreza)
    const life = await store.calcularVida(store.detalles[numero].base.dados, store.detalles[numero].base.tdado, store.detalles[numero].base.vida, store.detalles[numero].base.modificador)
    const preeliminar = await store.detalles[numero].base.nombre;
    const listado = await iniciativa.iniciativa;
    crear.name = nombreUnico(preeliminar, listado);
    crear.tipo = '2';
    crear.vida = `${life}`;
    crear.iniciativa = `${Math.floor(Math.random() * 20) + 1 + des}`;
});

const rollDice = () => {
    crear.iniciativa = Math.floor(Math.random() * 20) + 1
}

onMounted(() => { store.actualizaLista(); iniciativa.actualizaLista() });

</script>

<template>
    <div class="fixed inset-0 top-20 flex flex-col overflow-hidden bg-stone-900">

        <div class="h-[2px] bg-stone-800 flex-none"></div>
        <div class="flex flex-1 overflow-hidden">

            <div class="w-[18%] flex-none flex flex-col border-r border-stone-800 overflow-hidden">

                <div class="px-3 pt-4 pb-3 border-b border-stone-800">
                    <input v-model="buscador" @input="busqueda" type="text" placeholder="Buscar criatura..."
                        class="w-full bg-stone-700 text-stone-100 text-sm placeholder-stone-400 border border-stone-500 rounded-sm px-3 py-1.5 focus:outline-none focus:border-dnd-red transition-colors" />
                </div>

                <div class="flex-1 overflow-y-auto">
                    <div v-for="c in store.criaturas" :key="c.id" @click="visualizar(c)"
                        class="flex items-center justify-between px-3 py-2.5 border-b border-stone-800/60 cursor-pointer hover:bg-stone-800/50 transition-colors group"
                        :class="current === c.id ? 'bg-stone-800 border-l-2 border-l-dnd-red' : 'border-l-2 border-l-transparent'">
                        <div class="min-w-0">
                            <p class="text-stone-100 font-bold text-sm truncate font-fantasy tracking-wide">{{ c.nombre }}</p>
                            <p class="text-stone-500 text-xs mt-0.5">{{ store.calcularVida(c.dados, c.tipo, c.vida, c.modificador) }} PG | {{ c.publico === true ? 'Criatura compartida' : 'Criatura personal' }}</p>
                        </div>
                        <span
                            class="text-stone-600 group-hover:text-dnd-red transition-colors text-xs flex-none ml-1">▶</span>
                    </div>
                    <div v-if="store.criaturas.length === 0"
                        class="px-4 py-8 text-center text-stone-600 text-sm italic">
                        Sin criaturas
                    </div>
                </div>
            </div>

            <div class="flex-1 flex flex-col overflow-hidden">
                <CriaturaDisplay :verCriatura="verCriatura" :criatura="store.detalles[current]"></CriaturaDisplay>

                <div class="flex-none border-t-2 border-stone-700 bg-stone-950/80 px-6 py-5">
                    <form @submit.prevent="addIniciativa" class="flex flex-wrap items-end gap-4">

                        <div class="flex flex-col gap-1.5 min-w-[180px] flex-1">
                            <label for="nombre"
                                class="text-xs font-bold uppercase tracking-widest text-stone-400">Nombre</label>
                            <input v-model="crear.name" type="text" name="nombre" placeholder="Indica el nombre aquí"
                                class="bg-stone-800 text-stone-100 text-sm placeholder-stone-600 border border-stone-700 rounded-sm px-3 py-2.5 focus:outline-none focus:border-dnd-red transition-colors">
                        </div>

                        <div class="flex flex-col gap-1.5">
                            <label for="pjc"
                                class="text-xs font-bold uppercase tracking-widest text-stone-400">Tipo</label>
                            <select v-model="crear.tipo" name="pjc"
                                class="bg-stone-800 text-stone-300 text-sm border border-stone-700 rounded-sm px-3 py-2.5 focus:outline-none focus:border-dnd-red transition-colors cursor-pointer">
                                <option value="">Selecciona...</option>
                                <option value="1">Jugador</option>
                                <option value="2">Criatura</option>
                            </select>
                        </div>

                        <div v-if="crear.tipo === '2'" class="flex flex-col gap-1.5 w-28">
                            <label for="life"
                                class="text-xs font-bold uppercase tracking-widest text-stone-400">Vida</label>
                            <input v-model="crear.vida" type="number" name="life" placeholder="10"
                                class="bg-stone-800 text-stone-100 text-sm placeholder-stone-600 border border-stone-700 rounded-sm px-3 py-2.5 focus:outline-none focus:border-dnd-red transition-colors">
                        </div>

                        <div class="flex flex-col gap-1.5 w-28">
                            <label for="dice"
                                class="text-xs font-bold uppercase tracking-widest text-stone-400">Iniciativa</label>
                            <input v-model="crear.iniciativa" type="number" name="dice" placeholder="0"
                                class="bg-stone-800 text-stone-100 text-sm placeholder-stone-600 border border-stone-700 rounded-sm px-3 py-2.5 focus:outline-none focus:border-dnd-red transition-colors">
                        </div>

                        <button type="button" @click="rollDice"
                            class="text-xs font-bold uppercase tracking-widest text-stone-400 border border-stone-700 hover:border-dnd-red hover:text-dnd-red bg-stone-800 hover:bg-stone-700 rounded-sm px-4 py-2.5 transition-all">🎲
                            Aleatorio</button>

                        <button type="submit"
                            class="text-xs font-bold uppercase tracking-widest text-stone-100 bg-dnd-red hover:bg-red-700 border border-dnd-red rounded-sm px-5 py-2.5 transition-all shadow-md shadow-black/30">+
                            Agregar</button>

                    </form>
                </div>
            </div>

            <div class="w-[20%] flex-none h-full overflow-hidden border-l border-stone-800">
                <IniciativaDisplay tipo="dashboard" :store="iniciativa"></IniciativaDisplay>
            </div>
        </div>
    </div>
</template>