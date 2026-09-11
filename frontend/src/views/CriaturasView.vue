<script setup>
import { ref, onMounted } from 'vue';
import CrearCriaturaModal from '@/components/criaturas/CrearCriaturaModal.vue';
import { useCriaturaStore } from '@/stores/criaturaStore';
import AccionesCriaturaModal from '@/components/criaturas/AccionesCriaturaModal.vue';
import ResistenciasCriaturaModal from '@/components/criaturas/ResistenciasCriaturaModal.vue';
import InmunidadesCriatura from '@/components/criaturas/InmunidadesCriatura.vue';
import SalvacionesCriatura from '@/components/criaturas/SalvacionesCriatura.vue';
import HabilidadesCriatura from '@/components/criaturas/HabilidadesCriatura.vue';
import SentidosCriatura from '../components/criaturas/SentidosCriatura.vue';

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
    mostrarModal.value = !mostrarModal.value;
}

const resistencias = (id) =>{
    idCriatura.value = id;
    resistencia.value = !resistencia.value;
    mostrarModal.value = !mostrarModal.value;
}

const inmunidades = (id) => {
    idCriatura.value = id;
    inmunidad.value = !inmunidad.value;
    mostrarModal.value = !mostrarModal.value;
}

const salvaciones = (id) => {
    idCriatura.value = id;
    salvacion.value = !salvacion.value;
    mostrarModal.value = !mostrarModal.value;
}

const habilidades = (id) => {
    idCriatura.value = id;
    habilidad.value = !habilidad.value;
    mostrarModal.value = !mostrarModal.value;
}

const sentidos = (id) => {
    idCriatura.value = id;
    sentido.value = !sentido.value;
    mostrarModal.value = !mostrarModal.value;
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
                <div class="grid grid-cols-6 gap-5">
                    <div class="">
                        <button @click="acciones(c.id)">Acciones/Habilidades de {{c.nombre}}</button>
                    </div>
                    <div class="">
                        <button @click="resistencias(c.id)">Resistencias de {{c.nombre}}</button>
                    </div>
                    <div class="">
                        <button @click="inmunidades(c.id)">Inmunidades de estado de {{c.nombre}}</button>
                    </div>
                    <div class="">
                        <button @click="salvaciones(c.id)">Tiradas de salvacion de {{c.nombre}}</button>
                    </div>
                    <div class="">
                        <button @click="habilidades(c.id)">Habilidades de {{c.nombre}}</button>
                    </div>
                    <div class="">
                        <button @click="sentidos(c.id)">Sentidos de {{c.nombre}}</button>
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

    <SentidosCriatura :show="sentido" :id="idCriatura" @cancelar="sentidos" />
    <HabilidadesCriatura :show="habilidad" :id="idCriatura" @cancelar="habilidades" />
    <SalvacionesCriatura :show="salvacion" :id="idCriatura" @cancelar="salvaciones" />
    <InmunidadesCriatura :show="inmunidad" :id="idCriatura" @cancelar="inmunidades" />
    <ResistenciasCriaturaModal :show="resistencia" :id="idCriatura" @cancelar="resistencias" />
    <CrearCriaturaModal :show="crear" @cancelar="crearCriatura" />
    <AccionesCriaturaModal :show="accion" :id="idCriatura" @cancelar="acciones" />

</template>
