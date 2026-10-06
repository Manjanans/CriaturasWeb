<script setup>
import { ref, onMounted } from 'vue';
import CrearCriaturaModal from '@/components/criaturas/CrearCriaturaModal.vue';
import { useCriaturaStore } from '@/stores/criaturaStore';
import AccionesCriaturaModal from '@/components/criaturas/AccionesCriaturaModal.vue';
import ResistenciasCriaturaModal from '@/components/criaturas/ResistenciasCriaturaModal.vue';
import InmunidadesCriatura from '@/components/criaturas/InmunidadesCriatura.vue';
import SalvacionesCriatura from '@/components/criaturas/SalvacionesCriatura.vue';
import HabilidadesCriatura from '@/components/criaturas/HabilidadesCriatura.vue';
import SentidosCriatura from '@/components/criaturas/SentidosCriatura.vue';
import Modal from '@/components/shared/Modal.vue'

const mostrarModal = ref(false);
const store = useCriaturaStore();
const crear = ref(false);
const accion = ref(false);
const idCriatura = ref(0);
const resistencia = ref(false);
const inmunidad = ref(false);
const salvacion = ref(false);
const habilidad = ref(false);
const sentido = ref(false);
const eliminar = ref(false);
const name = ref('');
const crac = ref('');

onMounted(store.actualizaLista)

const crearCriatura = () => {
    mostrarModal.value = !mostrarModal.value;
    crac.value = 'crear';
    crear.value = !crear.value;
}

const acciones = (id) => {
    idCriatura.value = id;
    accion.value = !accion.value;
    mostrarModal.value = !mostrarModal.value;
    store.actualizaLista();
}

const resistencias = (id) =>{
    idCriatura.value = id;
    resistencia.value = !resistencia.value;
    mostrarModal.value = !mostrarModal.value;
    store.actualizaLista();
}

const inmunidades = (id) => {
    idCriatura.value = id;
    inmunidad.value = !inmunidad.value;
    mostrarModal.value = !mostrarModal.value;
    store.actualizaLista();
}

const salvaciones = (id) => {
    idCriatura.value = id;
    salvacion.value = !salvacion.value;
    mostrarModal.value = !mostrarModal.value;
    store.actualizaLista();
}

const habilidades = (id) => {
    idCriatura.value = id;
    habilidad.value = !habilidad.value;
    mostrarModal.value = !mostrarModal.value;
    store.actualizaLista();
}

const sentidos = (id) => {
    idCriatura.value = id;
    sentido.value = !sentido.value;
    mostrarModal.value = !mostrarModal.value;
    store.actualizaLista();
}

const eliminate = (id, nombre) => {
    idCriatura.value = id;
    eliminar.value = !eliminar.value;
    mostrarModal.value = !mostrarModal.value;
    name.value = nombre;
    store.actualizaLista();
}

const elimination = () =>{
    store.eliminarCriatura(idCriatura.value);
    eliminar.value = !eliminar.value;
    mostrarModal.value = !mostrarModal.value;
    store.actualizaLista();
}

const editar = (id) => {
    mostrarModal.value = !mostrarModal.value;
    crac.value = 'editar';
    idCriatura.value = id;
    crear.value = !crear.value;
    store.actualizaLista();
}
</script>

<template>
    <div v-if="!mostrarModal" class="max-w-6xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
        <div class="mb-8 flex justify-between items-center bg-dnd-panel border border-stone-700 p-6 rounded-sm shadow-lg">
            <h1 class="text-3xl font-fantasy text-dnd-gold tracking-widest font-bold">Bestiario</h1>
            <button @click="crearCriatura" class="px-6 py-2 border-2 border-dnd-gold shadow-md text-sm font-bold uppercase tracking-wider text-parchment bg-dnd-red hover:bg-[#6b0000] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-dnd-red transition-all duration-200 rounded-sm">
                + Crear criatura
            </button>
        </div>

        <div class="hidden md:grid grid-cols-12 gap-4 px-4 py-2 font-bold text-xs tracking-wider text-stone-400 border-b-2 border-stone-700/50 mb-4">
            <div class="col-span-4">Nombre</div>
            <div class="col-span-3">Fórmula Vida</div>
            <div class="col-span-2">Vida Total</div>
            <div class="col-span-3 text-right">Acciones</div>
        </div>

        <div class="space-y-4">
            <div v-for="c in store.criaturas" class="bg-white rounded-sm shadow-md border-t-4 border-t-dnd-gold overflow-hidden" :key="c.id">
                <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center p-4 hover:bg-stone-50 transition-colors">
                    <div class="col-span-4 flex items-center space-x-4">
                        <div class="w-12 h-12 bg-dnd-panel border-2 border-dnd-gold rounded flex-shrink-0 flex items-center justify-center shadow-inner">
                            <span class="text-dnd-gold font-fantasy font-bold text-2xl">
                                {{ c.nombre.charAt(0) }}
                            </span>
                        </div>
                        <div>
                            <span class="font-bold text-stone-900 text-lg sm:text-xl font-fantasy tracking-wide">
                                {{ c.nombre }}
                            </span>
                        </div>
                    </div>
                    
                    <div class="col-span-3 text-sm text-stone-600 font-medium">
                        <span v-if="c.tipo!=0" class="tracking-wider text-xs">
                            Tipo: <span class="font-bold">{{ c.tipo }}</span> | Dados: <span class="font-bold">{{ c.dados }}</span></span>
                        <span v-else class="italic text-stone-400">
                            Sin fórmula (No calculable)
                        </span>
                    </div>

                    <div class="col-span-2 text-stone-900 font-black text-lg">
                        <span class="text-xs text-stone-500 block hidden md:inline">HP: </span>{{ store.calcularVida(c.dados, c.tipo, c.vida, c.modificador) }}
                    </div>

                    <div class="col-span-3 flex items-center justify-end space-x-3">
                        <button 
                            @click="editar(c.id)" 
                            class="text-xs tracking-wider text-stone-500 hover:text-dnd-gold-light transition-colors font-bold px-2">
                            Editar
                        </button>
                        <button 
                            @click="eliminate(c.id, c.nombre)" 
                            class="text-xs tracking-wider text-dnd-red hover:text-[#6b0000] transition-colors font-bold px-2">
                            Eliminar
                        </button>
                        
                        <button 
                            @click="store.verDetalle(c.id)" 
                            class="ml-2 w-10 h-10 flex items-center justify-center rounded bg-stone-100 hover:bg-stone-200 text-dnd-red font-bold text-2xl border border-stone-300 transition-colors shadow-sm">
                            {{ store.abiertos.includes(c.id) ? '−' : '+' }}
                        </button>
                    </div>
                </div>

                <div v-if="store.abiertos.includes(c.id)" class="border-t border-stone-200">
                    <div class="bg-[#fdf6e3] p-5 md:p-7 mx-3 my-3 md:mx-5 md:my-4 border-y-4 border-dnd-red shadow-[inset_0_2px_8px_rgba(0,0,0,0.06)] relative">
                        <div class="absolute inset-0 border border-stone-400/20 pointer-events-none m-1"></div>

                        <div class="relative z-10">

                            <!-- Nombre (ancho completo) -->
                            <h2 class="text-3xl sm:text-4xl font-fantasy text-dnd-red font-black tracking-widest border-b-2 border-dnd-red pb-2 mb-4">{{ c.nombre }}</h2>

                            <!-- Layout de dos columnas -->
                            <div class="grid grid-cols-5 gap-0">

                                <!-- COLUMNA IZQUIERDA: stats base -->
                                <div class="col-span-2 border-r border-dnd-red/30 pr-6">

                                    <!-- ZONA 2: CA / HP / Velocidad -->
                                    <div class="text-sm text-stone-800 border-b-2 border-dnd-red pb-3 mb-4 space-y-0.5">
                                        <p><span class="font-bold text-stone-900">Clase de Armadura</span> {{ store.detalles[c.id]?.base.armadura || '--' }}</p>
                                        <p><span class="font-bold text-stone-900">Puntos de Golpe</span> {{ store.calcularVida(c.dados, c.tipo, c.vida, c.modificador) }}</p>
                                        <p><span class="font-bold text-stone-900">Velocidad</span> {{ store.detalles[c.id]?.base.velocidad || '--' }} pies</p>
                                    </div>

                                    <!-- ZONA 3: Características -->
                                    <div class="grid grid-cols-6 gap-1 mb-4 border-b-2 border-dnd-red pb-4 text-center">
                                        <div class="flex flex-col items-center">
                                            <span class="font-bold text-stone-600 tracking-widest text-[10px] mb-1">FUE</span>
                                            <span class="text-stone-900 font-black text-lg">{{ store.detalles[c.id]?.base.fuerza || '--' }}</span>
                                            <span class="text-[10px] font-medium text-stone-500">{{ store.detalles[c.id]?.base.fuerza ? store.calcularModificador(store.detalles[c.id]?.base.fuerza) : '' }}</span>
                                        </div>
                                        <div class="flex flex-col items-center">
                                            <span class="font-bold text-stone-600 tracking-widest text-[10px] mb-1">DES</span>
                                            <span class="text-stone-900 font-black text-lg">{{ store.detalles[c.id]?.base.destreza || '--' }}</span>
                                            <span class="text-[10px] font-medium text-stone-500">{{ store.detalles[c.id]?.base.destreza ? store.calcularModificador(store.detalles[c.id]?.base.destreza) : '' }}</span>
                                        </div>
                                        <div class="flex flex-col items-center">
                                            <span class="font-bold text-stone-600 tracking-widest text-[10px] mb-1">CON</span>
                                            <span class="text-stone-900 font-black text-lg">{{ store.detalles[c.id]?.base.constitucion || '--' }}</span>
                                            <span class="text-[10px] font-medium text-stone-500">{{ store.detalles[c.id]?.base.constitucion ? store.calcularModificador(store.detalles[c.id]?.base.constitucion) : '' }}</span>
                                        </div>
                                        <div class="flex flex-col items-center">
                                            <span class="font-bold text-stone-600 tracking-widest text-[10px] mb-1">INT</span>
                                            <span class="text-stone-900 font-black text-lg">{{ store.detalles[c.id]?.base.inteligencia || '--' }}</span>
                                            <span class="text-[10px] font-medium text-stone-500">{{ store.detalles[c.id]?.base.inteligencia ? store.calcularModificador(store.detalles[c.id]?.base.inteligencia) : '' }}</span>
                                        </div>
                                        <div class="flex flex-col items-center">
                                            <span class="font-bold text-stone-600 tracking-widest text-[10px] mb-1">SAB</span>
                                            <span class="text-stone-900 font-black text-lg">{{ store.detalles[c.id]?.base.sabiduria || '--' }}</span>
                                            <span class="text-[10px] font-medium text-stone-500">{{ store.detalles[c.id]?.base.sabiduria ? store.calcularModificador(store.detalles[c.id]?.base.sabiduria) : '' }}</span>
                                        </div>
                                        <div class="flex flex-col items-center">
                                            <span class="font-bold text-stone-600 tracking-widest text-[10px] mb-1">CAR</span>
                                            <span class="text-stone-900 font-black text-lg">{{ store.detalles[c.id]?.base.carisma || '--' }}</span>
                                            <span class="text-[10px] font-medium text-stone-500">{{ store.detalles[c.id]?.base.carisma ? store.calcularModificador(store.detalles[c.id]?.base.carisma) : '' }}</span>
                                        </div>
                                    </div>

                                    <!-- ZONA 4: Filas clicables -->
                                    <div class="space-y-0.5 text-sm">
                                        <button @click="salvaciones(c.id)" class="w-full text-left flex items-baseline gap-x-2 group hover:bg-stone-900/5 rounded-sm px-2 py-1 transition-colors cursor-pointer">
                                            <span class="font-bold text-stone-900 flex-none text-xs">Tiradas de Salvación</span>
                                            <span class="text-stone-600 flex-1 min-w-0 truncate text-xs">
                                                <template v-if="store.detalles[c.id]?.salvacion?.length">{{ store.detalles[c.id].salvacion.map(h => `${h.carac} ${h.modif >= 0 ? '+' : ''}${h.modif}`).join(', ') }}</template>
                                                <span v-else class="text-stone-400 italic">Sin configurar</span>
                                            </span>
                                            <span class="flex-none text-stone-300 group-hover:text-dnd-red transition-colors text-xs">✎</span>
                                        </button>
                                        <button @click="habilidades(c.id)" class="w-full text-left flex items-baseline gap-x-2 group hover:bg-stone-900/5 rounded-sm px-2 py-1 transition-colors cursor-pointer">
                                            <span class="font-bold text-stone-900 flex-none text-xs">Habilidades</span>
                                            <span class="text-stone-600 flex-1 min-w-0 truncate text-xs">
                                                <template v-if="store.detalles[c.id]?.habilidad?.length">{{ store.detalles[c.id].habilidad.map(h => `${h.habilidad}: ${h.modif >= 0 ? '+' : ''}${h.modif}`).join(', ') }}</template>
                                                <span v-else class="text-stone-400 italic">Sin configurar</span>
                                            </span>
                                            <span class="flex-none text-stone-300 group-hover:text-dnd-red transition-colors text-xs">✎</span>
                                        </button>
                                        <button @click="sentidos(c.id)" class="w-full text-left flex items-baseline gap-x-2 group hover:bg-stone-900/5 rounded-sm px-2 py-1 transition-colors cursor-pointer">
                                            <span class="font-bold text-stone-900 flex-none text-xs">Sentidos</span>
                                            <span class="text-stone-600 flex-1 min-w-0 truncate text-xs">
                                                <template v-if="store.detalles[c.id]?.sentido?.length">{{ store.detalles[c.id].sentido.map(h => `${h.tiposentido}: ${h.valor}`).join(', ') }}</template>
                                                <span v-else class="text-stone-400 italic">Sin configurar</span>
                                            </span>
                                            <span class="flex-none text-stone-300 group-hover:text-dnd-red transition-colors text-xs">✎</span>
                                        </button>
                                        <button @click="resistencias(c.id)" class="w-full text-left flex items-baseline gap-x-2 group hover:bg-stone-900/5 rounded-sm px-2 py-1 transition-colors cursor-pointer">
                                            <span class="font-bold text-stone-900 flex-none text-xs">Resistencias</span>
                                            <span class="text-stone-600 flex-1 min-w-0 truncate text-xs">
                                                <template v-if="store.detalles[c.id]?.resistencia?.weak.length || store.detalles[c.id]?.resistencia?.resist.length || store.detalles[c.id]?.resistencia?.inmune.length">
                                                    <span v-if="store.detalles[c.id]?.resistencia.weak.length != 0">{{ store.detalles[c.id].resistencia.weak.map(h => h.resist).join(', ') }}, </span>
                                                    <span v-if="store.detalles[c.id]?.resistencia.resist.length != 0">{{ store.detalles[c.id].resistencia.resist.map(h => h.resist).join(', ') }}, </span>
                                                    <span v-if="store.detalles[c.id]?.resistencia.inmune.length != 0">{{ store.detalles[c.id].resistencia.inmune.map(h => h.resist).join(', ') }}</span>
                                                </template>
                                                <span v-else class="text-stone-400 italic">Sin configurar</span>
                                            </span>
                                            <span class="flex-none text-stone-300 group-hover:text-dnd-red transition-colors text-xs">✎</span>
                                        </button>
                                        <button @click="inmunidades(c.id)" class="w-full text-left flex items-baseline gap-x-2 group hover:bg-stone-900/5 rounded-sm px-2 py-1 transition-colors cursor-pointer">
                                            <span class="font-bold text-stone-900 flex-none text-xs">Inmunidades</span>
                                            <span class="text-stone-600 flex-1 min-w-0 truncate text-xs">
                                                <template v-if="store.detalles[c.id]?.inmunidad?.length">{{ store.detalles[c.id].inmunidad.map(h => h.inmunidad).join(', ') }}</template>
                                                <span v-else class="text-stone-400 italic">Sin configurar</span>
                                            </span>
                                            <span class="flex-none text-stone-300 group-hover:text-dnd-red transition-colors text-xs">✎</span>
                                        </button>
                                    </div>

                                </div>

                                <!-- COLUMNA DERECHA: Acciones y Habilidades -->
                                <div class="col-span-3 pl-6">
                                    <div class="flex items-center justify-between border-b border-dnd-red pb-1 mb-3">
                                        <h3 class="text-base font-fantasy font-bold text-dnd-red uppercase tracking-widest">Acciones y Habilidades</h3>
                                        <button @click="acciones(c.id)" class="flex items-center gap-1 text-xs font-bold text-stone-400 hover:text-dnd-red transition-colors cursor-pointer uppercase tracking-wider">
                                            ✎ Editar
                                        </button>
                                    </div>
                                    <div v-if="store.detalles[c.id]?.accion?.length" class="space-y-3">
                                        <p v-for="h in store.detalles[c.id]?.accion" :key="h.id" class="text-sm text-stone-800 leading-relaxed">
                                            <span class="font-bold italic text-stone-900">{{ h.titulo }}.</span> {{ h.detalle }}
                                        </p>
                                    </div>
                                    <button v-else @click="acciones(c.id)" class="w-full text-center py-6 border-2 border-dashed border-stone-300 rounded-sm text-stone-400 hover:border-dnd-red hover:text-dnd-red transition-colors text-sm font-bold uppercase tracking-wider cursor-pointer">
                                        + Agregar Acciones y Habilidades
                                    </button>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div v-if="store.criaturas.length === 0" class="text-center py-10 bg-dnd-panel border border-stone-700 rounded-sm shadow-md">
                <p class="text-stone-400 font-bold uppercase tracking-widest font-fantasy text-xl">El bestiario está vacío.</p>
                <p class="text-stone-500 text-sm mt-2">Agrega nuevas criaturas.</p>
            </div>
        </div>
    </div>

    <Modal :show="eliminar" @close="eliminate(idCriatura, name)">
        <div class="bg-parchment rounded border border-dnd-gold p-6 text-stone-900 shadow-xl m-4 md:m-auto">
            <h3 class="text-2xl font-fantasy text-dnd-red font-bold uppercase tracking-widest border-b border-dnd-red pb-2 mb-4">Eliminar Criatura</h3>
            <p class="mb-6 font-medium">¿Estás seguro que deseas eliminar a <span class="font-bold text-dnd-red">{{ name }}</span> permanentemente?</p>
            <div class="flex flex-row-reverse space-x-2 space-x-reverse">
                <button @click="elimination" class="px-5 py-2.5 bg-dnd-red text-parchment font-bold text-sm tracking-wider uppercase border border-dnd-gold hover:bg-[#6b0000] transition-colors shadow-md rounded-sm">
                    Confirmar
                </button>
                <button @click="eliminate(idCriatura, name)" class="px-5 py-2.5 bg-white text-stone-700 font-bold text-sm tracking-wider uppercase border border-stone-300 hover:bg-stone-50 hover:text-stone-900 transition-colors shadow-sm rounded-sm">
                    Cancelar
                </button>
            </div>
        </div>
    </Modal>

    <SentidosCriatura :show="sentido" :id="idCriatura" @cancelar="sentidos" />
    <HabilidadesCriatura :show="habilidad" :id="idCriatura" @cancelar="habilidades" />
    <SalvacionesCriatura :show="salvacion" :id="idCriatura" @cancelar="salvaciones" />
    <InmunidadesCriatura :show="inmunidad" :id="idCriatura" @cancelar="inmunidades" />
    <ResistenciasCriaturaModal :show="resistencia" :id="idCriatura" @cancelar="resistencias" />
    <CrearCriaturaModal :show="crear" :modo="crac" :id="idCriatura" @cancelar="crearCriatura" />
    <AccionesCriaturaModal :show="accion" :id="idCriatura" @cancelar="acciones" />
</template>
