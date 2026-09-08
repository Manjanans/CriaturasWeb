<script setup>
    import {useToast} from 'vue-toastification';
    import {reactive} from 'vue';

    const toast = useToast();
    const props = defineProps({
        show: Boolean,
        modo: String
    })
    const emit = defineEmits(['exito', 'cancelar']);

    const formulario = reactive({
        user : "",
        passw: ""
    });

    const crearUsuario = async () => {
        const nuevo = {"username": formulario.user, "password":formulario.passw}

        try{
            const response = await fetch('/auth/register', {
                method: 'POST',
                headers: {
                'Content-Type': 'application/json'
                },
                body: JSON.stringify(nuevo)
            });

        if (!response.ok) {
            const err = await response.json()
            toast.error(err.detail)
            throw new Error(err.detail);
        }

        toast.success("Usuario creado exitosamente");
        formulario.user = '';
        formulario.passw = '';
        emit("exito");
        } catch(e){
            console.error("Hubo un error", e);
            formulario.user = '';
            formulario.passw = '';
        }
    }

    const cambiarPassw = async () =>{
        const nuevo = {"username": formulario.user, "password":formulario.passw}

        try{
            const response = await fetch('/auth/change-password', {
                method: 'POST',
                headers: {
                'Content-Type': 'application/json'
                },
                body: JSON.stringify(nuevo)
            });

        if (!response.ok) {
            const err = await response.json()
            toast.error(err.detail);
            throw new Error(err.detail);
        }

        toast.success("Contraseña cambiada exitosamente");
        emit("exito");

        } catch(e){
            console.error("Hubo un error", e);
            formulario.user = '';
            formulario.passw = '';
        }
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
    <div  v-if="show" class="">
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
    </div>
    
</template>