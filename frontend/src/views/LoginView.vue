<template>
    <div class="min-h-screen flex flex-col justify-center py-12 sm:px-6 lg:px-8 relative">
        <div class="sm:mx-auto sm:w-full sm:max-w-md">
            <h2 class="mt-6 text-center text-4xl font-extrabold text-dnd-red tracking-tight font-fantasy">
                Iniciar Sesión
            </h2>
            <p class="mt-2 text-center text-sm text-stone-400 font-semibold uppercase tracking-widest">
                Bienvenido al Compendio
            </p>
        </div>

        <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md relative z-10">
            <!-- Parchment Container -->
            <div class="bg-parchment py-8 px-4 shadow-[0_0_20px_-3px_rgba(0,0,0,0.7)] sm:rounded sm:px-10 border-2 border-dnd-gold relative overflow-hidden">
                <!-- Decorative border effect -->
                <div class="absolute inset-0 border border-stone-200 opacity-60 pointer-events-none m-1"></div>
                
                <form @submit.prevent="acceder" class="space-y-6 relative z-10">
                    <div>
                        <label for="user" class="block text-sm font-bold text-stone-800 uppercase tracking-wider">Usuario</label>
                        <div class="mt-1">
                            <input v-model="formulario.user" type="text" name="user" id="user" required
                                class="appearance-none block w-full px-4 py-3 bg-white border border-stone-300 shadow-inner rounded-sm placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-dnd-gold focus:border-dnd-gold sm:text-sm transition-all duration-200 text-stone-900">
                        </div>
                    </div>

                    <div>
                        <label for="passw" class="block text-sm font-bold text-stone-800 uppercase tracking-wider">Contraseña</label>
                        <div class="mt-1">
                            <input v-model="formulario.passw" type="password" name="passw" id="passw" required
                                class="appearance-none block w-full px-4 py-3 bg-white border border-stone-300 shadow-inner rounded-sm placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-dnd-gold focus:border-dnd-gold sm:text-sm transition-all duration-200 text-stone-900">
                        </div>
                    </div>

                    <div class="pt-2">
                        <button type="submit" class="w-full flex justify-center py-3 px-4 border border-dnd-gold shadow-md text-base font-bold text-parchment bg-dnd-red hover:bg-[#6b0000] font-fantasy tracking-wider focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-dnd-red transition-all duration-200 rounded-sm">
                            Entrar a mi cuenta
                        </button>
                    </div>
                </form>

                <div class="mt-6 flex items-center justify-between relative z-10 pt-4 border-t border-stone-300/60">
                    <button type="button" @click="abrirCambiarContrasenia" class="text-xs font-bold text-dnd-gold-light hover:text-dnd-gold uppercase tracking-wider transition-colors">
                        ¿Olvidaste tu contraseña?
                    </button>
                    <button type="button" @click="abrirCrear" class="text-xs font-bold text-dnd-gold-light hover:text-dnd-gold uppercase tracking-wider transition-colors">
                        Crear usuario
                    </button>
                </div>
            </div>
        </div>
        
        <ModalUsuario :show="mostrarModal" :modo="modoModal" @cancelar="cerrarModal" @exito="cerrarModal"/>
    </div>
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