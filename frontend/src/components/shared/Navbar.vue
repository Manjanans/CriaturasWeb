<script setup>
    import { useAuthStore } from '@/utils/auth.js'
    import { RouterLink } from 'vue-router'
    
    const auth = useAuthStore();
    

    const props = defineProps({
        show:{ type: Boolean }
    });
    const logout = () => {
        auth.logout();
    }
</script>
<template>
    <div v-if="show" class="pb-6 pt-6">
        Hola :D
        <div class="pb-6 pt-6">
            <RouterLink to="/">
                <button @click="logout">Cerrar Sesión</button>
            </RouterLink>
            
        </div>
    </div>
    
</template>