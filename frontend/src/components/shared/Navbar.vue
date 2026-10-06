<script setup>
    import { useAuthStore } from '@/stores/authStore'
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
    <nav v-if="show" class="bg-dnd-dark border-b-2 border-dnd-gold shadow-[0_4px_20px_rgba(0,0,0,0.8)] sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <!-- Brand / Logo Area -->
                <div class="flex items-center">
                    <RouterLink to="/" class="text-3xl font-fantasy text-dnd-red tracking-widest font-bold hover:text-[#a00000] transition-colors">
                        Inicio
                    </RouterLink>
                </div>
                
                <!-- Navigation Links -->
                <div class="flex space-x-6 sm:space-x-10 items-center">
                    <RouterLink :to="{ name: 'creatures' }" class="text-stone-300 hover:text-dnd-gold font-bold uppercase tracking-widest transition-colors duration-200 text-sm sm:text-base">
                        Criaturas
                    </RouterLink>
                </div>

                <div class="flex space-x-6 sm:space-x-10 items-center">
                    <RouterLink :to="{ name: 'battle' }" class="text-stone-300 hover:text-dnd-gold font-bold uppercase tracking-widest transition-colors duration-200 text-sm sm:text-base">
                        Batalla
                    </RouterLink>
                </div>
                
                <!-- Actions -->
                <div class="flex items-center">
                    <RouterLink to="/" @click="logout" class="px-4 py-2 sm:px-5 sm:py-2.5 border border-dnd-red text-dnd-red hover:bg-[#8b0000] hover:text-parchment transition-all duration-200 uppercase tracking-wider font-bold text-xs sm:text-sm rounded-sm shadow-md">
                        Cerrar Sesión
                    </RouterLink>
                </div>
            </div>
        </div>
    </nav>
</template>