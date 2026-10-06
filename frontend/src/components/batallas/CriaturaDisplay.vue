<script setup>
import {useCriaturaStore} from '@/stores/criaturaStore';
import {ref, onMounted, reactive} from 'vue';

const store = useCriaturaStore();

const props = defineProps({
    verCriatura: Boolean,
    criatura: Object
});
</script>
<template>
    <div class="flex-1 overflow-y-auto p-4 pt-5 md:p-5 md:pt-6 flex flex-col">
        <div v-if="!verCriatura" class="flex-1 flex flex-col items-center justify-center text-center">
            <p class="text-stone-600 font-fantasy text-2xl tracking-widest uppercase">Selecciona una criatura</p>
            <p class="text-stone-700 text-sm mt-2">El detalle aparecerá aquí</p>
        </div>
        <div v-if="verCriatura"
            class="flex-1 bg-[#f2e8d6] rounded border-y-[3px] border-dnd-red/70 shadow-lg shadow-black/30 relative">
            <div class="absolute inset-0 border border-stone-400/10 pointer-events-none m-1 rounded"></div>

            <div class="relative z-10 p-5 md:p-6">

                <h2
                    class="text-3xl font-fantasy text-dnd-red font-black tracking-widest border-b-2 border-dnd-red/60 pb-2 mb-4">
                    {{ criatura?.base.nombre }}
                </h2>

                <div class="grid grid-cols-5 gap-0">

                    <div class="col-span-2 border-r border-dnd-red/25 pr-5">

                        <div class="text-base text-stone-700 border-b-2 border-dnd-red/60 pb-3 mb-4 space-y-1">
                            <p><span class="font-bold text-stone-800">Clase de Armadura</span> {{criatura?.base.armadura || '--' }}</p>
                            <p><span class="font-bold text-stone-800">Puntos de Golpe</span> {{store.calcularVida(criatura?.base.dados, criatura?.base.tdado, criatura?.base.vida, criatura?.base.modificador) }}</p>
                            <p><span class="font-bold text-stone-800">Velocidad</span> {{criatura?.base.velocidad || '--' }} pies</p>
                        </div>

                        <div class="grid grid-cols-6 gap-1 mb-4 border-b-2 border-dnd-red/60 pb-4 text-center">
                            <div class="flex flex-col items-center">
                                <span class="font-bold text-stone-500 text-xs mb-1">FUE</span>
                                <span class="text-stone-800 font-black text-xl">{{criatura?.base.fuerza || '--' }}</span>
                                <span class="text-xs text-stone-500">{{ criatura?.base.fuerza ? store.calcularModificador(criatura?.base.fuerza) : '' }}</span>
                            </div>
                            <div class="flex flex-col items-center">
                                <span class="font-bold text-stone-500 text-xs mb-1">DES</span>
                                <span class="text-stone-800 font-black text-xl">{{
                                    criatura?.base.destreza || '--' }}</span>
                                <span class="text-xs text-stone-500">{{ criatura?.base.destreza ? store.calcularModificador(criatura?.base.destreza) : '' }}</span>
                            </div>
                            <div class="flex flex-col items-center">
                                <span class="font-bold text-stone-500 text-xs mb-1">CON</span>
                                <span class="text-stone-800 font-black text-xl">{{
                                    criatura?.base.constitucion || '--' }}</span>
                                <span class="text-xs text-stone-500">{{ criatura?.base.constitucion ? store.calcularModificador(criatura?.base.constitucion) : ''}}</span>
                            </div>
                            <div class="flex flex-col items-center">
                                <span class="font-bold text-stone-500 text-xs mb-1">INT</span>
                                <span class="text-stone-800 font-black text-xl">{{
                                    criatura?.base.inteligencia || '--' }}</span>
                                <span class="text-xs text-stone-500">{{ criatura?.base.inteligencia ? store.calcularModificador(criatura?.base.inteligencia) : ''}}</span>
                            </div>
                            <div class="flex flex-col items-center">
                                <span class="font-bold text-stone-500 text-xs mb-1">SAB</span>
                                <span class="text-stone-800 font-black text-xl">{{
                                    criatura?.base.sabiduria || '--' }}</span>
                                <span class="text-xs text-stone-500">{{ criatura?.base.sabiduria ? store.calcularModificador(criatura?.base.sabiduria) : ''}}</span>
                            </div>
                            <div class="flex flex-col items-center">
                                <span class="font-bold text-stone-500 text-xs mb-1">CAR</span>
                                <span class="text-stone-800 font-black text-xl">{{
                                    criatura?.base.carisma || '--' }}</span>
                                <span class="text-xs text-stone-500">{{ criatura?.base.carisma ? store.calcularModificador(criatura?.base.carisma) : '' }}</span>
                            </div>
                        </div>

                        <div class="space-y-1 text-sm text-stone-600">
                            <div v-if="criatura?.salvacion?.length" class="px-1 py-0.5">
                                <span class="font-bold text-stone-800">Tiradas de Salvación </span>
                                {{criatura.salvacion.map(h => `${h.carac} ${h.modif >= 0 ? '+' :''}${h.modif}`).join(', ')}}
                            </div>
                            <div v-if="criatura?.habilidad?.length" class="px-1 py-0.5">
                                <span class="font-bold text-stone-800">Habilidades </span> 
                                {{criatura.habilidad.map(h => `${h.habilidad}: ${h.modif >= 0 ? '+': ''}${h.modif}`).join(', ')}}
                            </div>
                            <div v-if="criatura?.sentido?.length" class="px-1 py-0.5">
                                <span class="font-bold text-stone-800">Sentidos </span>
                                {{criatura.sentido.map(h => `${h.tiposentido}: ${h.valor}`).join(',')}}
                            </div>
                            <div v-if="criatura?.resistencia?.weak?.length" class="px-1 py-0.5">
                                <span class="font-bold text-stone-800">Debilidades al daño </span>
                                {{criatura.resistencia.weak.map(h => h.resist).join(', ')}}
                            </div>
                            <div v-if="criatura?.resistencia?.resist?.length" class="px-1 py-0.5">
                                <span class="font-bold text-stone-800">Resistencias al daño </span>
                                {{criatura.resistencia.resist.map(h => h.resist).join(', ')}}
                            </div>
                            <div v-if="criatura?.resistencia?.inmune?.length" class="px-1 py-0.5">
                                <span class="font-bold text-stone-800">Inmunidades al daño </span>
                                {{criatura.resistencia.inmune.map(h => h.resist).join(', ')}}
                            </div>
                            <div v-if="criatura?.inmunidad?.length" class="px-1 py-0.5">
                                <span class="font-bold text-stone-800">Inmunidades de condición </span>
                                {{criatura.inmunidad.map(h => h.inmunidad).join(', ')}}
                            </div>
                        </div>
                    </div>

                    <div class="col-span-3 pl-5">
                        <div class="border-b border-dnd-red/50 pb-1 mb-3">
                            <h3 class="text-sm font-fantasy font-bold text-dnd-red uppercase tracking-widest">
                                Acciones y Habilidades</h3>
                        </div>
                        <div v-if="criatura?.accion?.length" class="space-y-2.5">
                            <p v-for="h in criatura.accion" :key="h.id"
                                class="text-xs text-stone-700 leading-relaxed">
                                <span class="font-bold italic text-stone-800">{{ h.titulo }}.</span> {{ h.detalle }}
                            </p>
                        </div>
                        <p v-else class="text-stone-500 italic text-xs">Sin acciones registradas.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>