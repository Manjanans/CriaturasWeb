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
    <div v-if="show" class="">
        <div class="grid gap-3 mb-3 md:grid-cols-3">
            <div class="pb-3 pt-3">
                <RouterLink to="/">
                    <button>Inicio</button>
                </RouterLink>
            </div>

            <div class="pb-3 pt-3">
                <RouterLink :to="{ name: 'creatures' }">
                    <button>Criaturas</button>
                </RouterLink>
            </div>
        
            <div class="pb-3 pt-3">
                <RouterLink to="/">
                    <button @click="logout">Cerrar Sesión</button>
                </RouterLink>
            </div>
        </div>
    </div>
    
</template>