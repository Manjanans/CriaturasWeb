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
    <Modal :show="show" @close="cancelar">
        <div class="bg-parchment rounded shadow-xl border-2 border-dnd-gold relative overflow-hidden text-stone-900 w-full">
            <!-- Decorative interior border -->
            <div class="absolute inset-0 border border-stone-200 opacity-60 pointer-events-none m-1"></div>
            
            <div class="px-6 pt-6 pb-4 sm:p-8 sm:pb-6 border-b border-stone-300 relative z-10">
                <div class="sm:flex sm:items-start w-full">
                    <div class="mt-3 text-center sm:mt-0 sm:text-left w-full">
                        <h3 class="text-2xl font-bold tracking-tig mb-6 text-dnd-red font-fantasy" id="modal-title">
                            <span v-if="modo==='crear'">Crear Nuevo Usuario</span>
                            <span v-else-if="modo==='cambiar-password'">Cambiar Contraseña</span>
                        </h3>
                        
                        <form @submit.prevent="ejecutarFuncion" class="space-y-5">
                            <div>
                                <label for="modal-user" class="block text-sm font-bold text-stone-800 uppercase tracking-wider">Usuario</label>
                                <div class="mt-1">
                                    <input v-model="formulario.user" type="text" name="user" id="modal-user" required
                                        class="appearance-none block w-full px-4 py-3 bg-white border border-stone-300 shadow-inner rounded-sm placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-dnd-gold focus:border-dnd-gold sm:text-sm transition-colors text-stone-900">
                                </div>
                            </div>

                            <div>
                                <label for="modal-passw" class="block text-sm font-bold text-stone-800 uppercase tracking-wider">Contraseña</label>
                                <div class="mt-1">
                                    <input v-model="formulario.passw" type="password" name="passw" id="modal-passw" required
                                        class="appearance-none block w-full px-4 py-3 bg-white border border-stone-300 shadow-inner rounded-sm placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-dnd-gold focus:border-dnd-gold sm:text-sm transition-colors text-stone-900">
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
            
            <div class="bg-stone-200/40 px-6 py-4 sm:px-8 sm:flex sm:flex-row-reverse relative z-10">
                <button v-if="modo==='crear'" type="button" @click="ejecutarFuncion"
                    class="w-full inline-flex justify-center border border-dnd-gold shadow-md px-5 py-2.5 bg-dnd-red font-fantasy text-sm font-bold tracking-wider text-parchment hover:bg-[#6b0000] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-dnd-red sm:ml-3 sm:w-auto transition-colors rounded-sm">
                    Crear usuario
                </button>
                <button v-else-if="modo === 'cambiar-password'" type="button" @click="ejecutarFuncion"
                    class="w-full inline-flex justify-center border border-dnd-gold shadow-md px-5 py-2.5 bg-dnd-red font-fantasy text-sm font-bold tracking-wider text-parchment hover:bg-[#6b0000] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-dnd-red sm:ml-3 sm:w-auto transition-colors rounded-sm">
                    Cambiar Contraseña
                </button>
                
                <button type="button" @click="cancelar"
                    class="mt-3 w-full inline-flex justify-center border border-stone-400 shadow-sm px-5 py-2.5 bg-white text-sm font-bold uppercase tracking-wider text-stone-700 hover:bg-stone-100 hover:text-stone-900 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-dnd-gold sm:mt-0 sm:ml-3 sm:w-auto transition-colors rounded-sm">
                    Cancelar
                </button>
            </div>
        </div>
    </Modal>   
</template>