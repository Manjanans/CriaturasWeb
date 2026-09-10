<script setup>
import { ref, onMounted } from 'vue';
import CrearCriaturaModal from '@/components/criaturas/CrearCriaturaModal.vue';
import { useCriaturaStore } from '@/stores/criaturaStore';
import AccionesCriaturaModal from '@/components/criaturas/AccionesCriaturaModal.vue';

const mostrarModal = ref(false);
const store = useCriaturaStore();
const crear = ref(false);
const accion = ref(false);
const idCriatura = ref(0);

onMounted(store.actualizaLista)

const crearCriatura = () => {
    mostrarModal.value = !mostrarModal.value;
    crear.value = !crear.value;
}

const calcularModificador = (atr) =>{
    return Math.floor((atr-10)/2)
}

const calcularVida = (tipo, dados, vida) => {
    if (vida!=0){
        return vida
    }else{
        let life = 0;
        for(let i=0; i<dados; i++){
            let valor = Math.floor(Math.random()*tipo);
            life+=valor
        }
        return life
    }
}

const acciones = (id) => {
    idCriatura.value = id;
    accion.value = !accion.value;
    mostrarModal.value = !mostrarModal.value
}
</script>

<template>
    <div v-if="!mostrarModal" class="">
        <div class="">
            <button @click="crearCriatura">Crear criatura</button>
        </div>
        <div v-for="c in store.criaturas" class="" :key="c.id">
            <div class="" name="general">
                {{ c.nombre }} - <span v-if="c.tipo!=0">Tipo dado: {{ c.tipo }} - Cantidad de dados: {{ c.dados }} -</span> Vida Total: {{ calcularVida(c.tipo, c.dados, c.vida) }} <button @click="store.verDetalle(c.id)">Ver detalle</button>
            </div>
            <div v-if="store.abiertos.includes(c.id)" class="" name="detalle">
                <div class="grid grid-cols-5 gap-5">
                    <div class="">
                        <button @click="acciones(c.id)">Acciones de la Criatura</button>
                    </div>
                </div>
                <div class="grid grid-cols-2 gap-4">
                    <div class="">
                        Clase Armadura (CA): {{ store.detalles[c.id]?.armadura }}
                    </div>
                    <div class="">
                        Velocidad (pies): {{ store.detalles[c.id]?.velocidad }}
                    </div>
                </div>
                <div class="grid grid-cols-3 gap-4">
                    <div class="">
                        Fuerza (STR): {{ store.detalles[c.id]?.fuerza }}
                        Modificador: {{ calcularModificador( store.detalles[c.id]?.fuerza ) }}
                    </div>
                    <div class="">
                        Destreza (DEX): {{ store.detalles[c.id]?.destreza }}
                        Modificador: {{ calcularModificador( store.detalles[c.id]?.destreza ) }}
                    </div>
                    <div class="">
                        Constitucion (con): {{ store.detalles[c.id]?.constitucion }}
                        Modificador: {{ calcularModificador( store.detalles[c.id]?.constitucion ) }}
                    </div>
                    <div class="">
                        Inteligencia (INT): {{ store.detalles[c.id]?.inteligencia }}
                        Modificador: {{ calcularModificador( store.detalles[c.id]?.inteligencia ) }}
                    </div>
                    <div class="">
                        Sabiduría (WIS): {{ store.detalles[c.id]?.sabiduria }}
                        Modificador: {{ calcularModificador( store.detalles[c.id]?.sabiduria ) }}
                    </div>
                    <div class="">
                        Carisma (CHA): {{ store.detalles[c.id]?.carisma }}
                        Modificador: {{ calcularModificador( store.detalles[c.id]?.carisma ) }}
                    </div>
                </div>
            </div>
        </div>
    </div>

    <CrearCriaturaModal :show="crear" @cancelar="crearCriatura" />
    <AccionesCriaturaModal :show="accion" :id="idCriatura" @cancelar="acciones" />
</template>
