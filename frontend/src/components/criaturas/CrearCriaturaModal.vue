<script setup>
import { reactive, ref } from 'vue';
import { useCriaturaStore } from '@/stores/criaturaStore';
import Modal from '@/components/shared/Modal.vue';

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
    'carisma': null
});

const mostrarVida = ref(true);
const mostrar = ()=>{
    mostrarVida.value = !mostrarVida.value
}
const props = defineProps({
    show: Boolean
});

const emit = defineEmits(['cancelar']);

const crearCriatura = () => {
    useCriaturaStore().crearNuevaCriatura(criatura);
    emit('cancelar');
}

</script>
<template>
    <Modal :show="show">
        <form @submit.prevent="crearCriatura">
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
                    <select @input="mostrar" required>
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
                <div v-if="mostrarVida" class="">
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
            <button type="submit">Crear Criatura</button>
        </form>
        <button @click="emit('cancelar')">Cancelar</button>
    </Modal>
</template>