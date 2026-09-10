<template>
    <div v-if="!mostrarModal" class="">
        <form @submit.prevent="acceder">
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
            <button type="submit">Iniciar Sesión</button>
        </form>

        <div class="mb-3">
            <button @click="abrirCambiarContrasenia">Cambiar contraseña</button>
        </div>
        <div class="mb-3">
            <button @click="abrirCrear">Crear usuario</button>
        </div>
    </div>
    <ModalUsuario :show="mostrarModal" :modo="modoModal" @cancelar="cerrarModal" @exito="cerrarModal"/>
</template>

<script setup>
    // Importaciones
    import { reactive, ref } from 'vue';
    // Autorización con Pinia, para mostrar navbar después de iniciar sesión
    import { useAuthStore } from '@/stores/authStore.js';
    //Modal
    import ModalUsuario from '@/components/account/ModalUsuario.vue';

    // Creación del objeto auth, para usar validaciones de Pinia
    const auth = useAuthStore()

    
    const formulario = reactive({
        user: '',
        passw: ''
    });

    const mostrarModal = ref(false);
    const modoModal = ref('');

    const abrirCrear = () => {
        modoModal.value = 'crear'
        mostrarModal.value = true
    }

    const abrirCambiarContrasenia = () => {
        modoModal.value = 'cambiar-password'
        mostrarModal.value = true
    }

    const cerrarModal = () => {
        mostrarModal.value = false
        modoModal.value = ''
    }

    const acceder = async () => {
        await auth.login(formulario);
    }
</script>