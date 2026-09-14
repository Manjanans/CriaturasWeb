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
    <Modal :show="show">
        <form @submit.prevent="execute(mode)" >
            <div class="grid grid-cols-2 gap-4 pb-6">
                <div class="pb-5">
                    <label for="">¿Quieres dejarlo público?</label>
                    <select v-model="criatura.publico" required>
                        <option value="true">Sí</option>
                        <option value="false">No</option>
                    </select>
                </div>
                <div class="pb-5">
                    <label for="">¿Quieres hacer la criatura con dados y tipo de dado?</label>
                    <select @change="vida" required>
                        <option value="true">Sí</option>
                        <option value="false">No</option>
                    </select>
                </div>
            </div>
            <div class="grid grid-cols-3 gap-4 pb-6">
                <div class="">
                    <label for="nombre">Nombre</label>
                    <input v-model="criatura.nombre" type="text" name="nombre" placeholder="Ingresa el nombre" required>
                </div>
                <div class="">
                    <label for="exp">Cantidad de Experiencia:</label>
                    <input v-model.number="criatura.cantexp" type="number" name="exp" placeholder="50" required>
                </div>
                <div v-if="vidita" class="">
                    <div class="pb-5">
                        <label for="dice">Cantidad de Dados:</label>
                        <input v-model.number="criatura.cantdados" type="number" name="dice" placeholder="8">
                    </div>
                    <div class="pb-5">
                        <label for="type">Tipo de Dado:</label>
                        <select v-model.number="criatura.tipodado">
                            <option value="4">d4</option>
                            <option value="6">d6</option>
                            <option value="8">d8</option>
                            <option value="10">d10</option>
                            <option value="12">d12</option>
                        </select>
                    </div>
                    <div class="pb-5">
                        <label for="lifemod">Modificador de Vida:</label>
                        <input v-model.number="criatura.modificadorvida" type="number" name="lifemod" placeholder="8">
                    </div>
                </div>
                <div v-else class="">
                    <div class="">
                        <label for="life">Ingresa la vida total:</label>
                        <input v-model.number="criatura.vidatotal" type="number" name="life" placeholder="20">
                    </div>
                </div>
            </div>
            <div class="grid grid-cols-4 gap-4">
                <div class="pb-5">
                    <label for="ac">Clase de Armadura:</label>
                    <input v-model.number="criatura.clasearmadura" type="number" name="ac" placeholder="10" required>
                </div>
                <div class="pb-5">
                    <label for="speed">Velocidad:</label>
                    <input v-model.number="criatura.velocidad" type="number" name="speed" placeholder="10" required>
                </div>
                <div class="pb-5">
                    <label for="str">Fuerza:</label>
                    <input v-model.number="criatura.fuerza" type="number" name="str" placeholder="10" required>
                </div>
                <div class="pb-5">
                    <label for="dex">Destreza:</label>
                    <input v-model.number="criatura.destreza" type="number" name="dex" placeholder="10" required>
                </div>
                <div class="pb-5">
                    <label for="con">Constitución:</label>
                    <input v-model.number="criatura.constitucion" type="number" name="con" placeholder="10" required>
                </div>
                <div class="pb-5">
                    <label for="int">Inteligencia:</label>
                    <input v-model.number="criatura.inteligencia" type="number" name="int" placeholder="10" required>
                </div>
                <div class="pb-5">
                    <label for="wis">Sabiduría:</label>
                    <input v-model.number="criatura.sabiduria" type="number" name="wis" placeholder="10" required>
                </div>
                <div class="pb-5">
                    <label for="cha">Carisma:</label>
                    <input v-model.number="criatura.carisma" type="number" name="cha" placeholder="10" required>
                </div>
            </div>
            <div v-if="modo === 'crear'" class="">
                <button type="submit" >Crear Criatura</button>
            </div>
            <div v-else class="">
                <button type="submit">Editar Criatura</button>
            </div>
        </form>
        <button @click="emit('cancelar')">Cancelar</button>
    </Modal>
</template>