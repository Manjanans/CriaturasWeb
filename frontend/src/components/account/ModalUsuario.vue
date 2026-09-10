<script setup>
    import {reactive} from 'vue';
    import { useAuthStore } from '@/stores/authStore.js';
    import Modal from '@/components/shared/Modal.vue';

    const auth = useAuthStore()

    const props = defineProps({
        show: Boolean,
        modo: String
    });

    const emit = defineEmits(['exito', 'cancelar']);

    const formulario = reactive({
        user : "",
        passw: ""
    });

    const crearUsuario = async () => {
        await auth.createUser(formulario)
        emit("exito");
    }

    const cambiarPassw = async () =>{
        await auth.changePassword(formulario)
        emit("exito");
    }

    const ejecutarFuncion = async () =>{
        if (props.modo === 'crear'){
            await crearUsuario();
        }
        if(props.modo === 'cambiar-password'){
            await cambiarPassw();
        }
    }

    const cancelar = ()=>{
        emit("cancelar")
    }
</script>

<template>
    <Modal :show="show">
        <form @submit.prevent="ejecutarFuncion">
            <div class="grid gap-6 mb-6 mt-6 md:grid-cols-2">
                <div class="pl-8 pr-8">
                    <label for="user">Ingresa el usuario:</label>
                    <input v-model="formulario.user" type="text" name="user" id="user" class="bg-neutral-secondary-medium border border-default-medium text-heading text-sm rounded-base focus:ring-brand focus:border-brand block w-full px-2.5 py-2 shadow-xs placeholder:text-body">
            
                </div>
            </div>
            <div class="grid gap-6 mb-6 mt-6 md:grid-cols-2">
                <div class="pl-8 pr-8">
                    <label for="passw">Ingresa la contraseña:</label>
                    <input v-model="formulario.passw" type="password" name="passw" id="passw" class="bg-neutral-secondary-medium border border-default-medium text-heading text-sm rounded-base focus:ring-brand focus:border-brand block w-full px-2.5 py-2 shadow-xs placeholder:text-body">
                </div>
            </div>
            <div v-if="modo==='crear'" class="">
                <button type="submit">Crear usuario</button>
            </div>
            <div v-else-if="modo === 'cambiar-password'" class="">
                <button type="submit">Cambiar Contraseña</button>
            </div>
        </form>
        <div class="">
            <button @click="cancelar">Cancelar</button>
        </div>
    </Modal>   
</template>