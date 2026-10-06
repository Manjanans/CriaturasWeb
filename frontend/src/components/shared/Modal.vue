<script setup>
defineProps({
    show:    { type: Boolean, default: false },
    title:   { type: String,  default: '' },
    tipo:    { type: String,  default: 'normal' }, // 'normal' | 'criatura'
    btnLabel:{ type: String,  default: '+ Agregar' },
});
const emit = defineEmits(['close', 'agregar']);
</script>

<template>
    <Teleport to="body">
        <Transition
            enter-active-class="transition-opacity duration-200"
            enter-from-class="opacity-0"
            leave-active-class="transition-opacity duration-150"
            leave-to-class="opacity-0"
        >
            <div
                v-if="show"
                class="fixed inset-0 z-[9999] bg-black/85 backdrop-blur-sm flex items-center justify-center p-4"
                @click="$emit('close')"
            >
                <div
                    class="relative flex flex-col w-full md:w-[70vw] h-[70vh] bg-[#f5efe0] rounded border-2 border-amber-700 shadow-2xl text-stone-900 overflow-hidden"
                    @click.stop
                >
                    <div class="flex-none flex items-center justify-between px-6 py-4 border-b-2 border-red-800 bg-[#f5efe0]">
                        <h2 class="text-2xl font-bold uppercase tracking-widest text-red-800 font-serif truncate pr-4">
                            {{ title }}
                        </h2>
                        <button
                            v-if="tipo === 'criatura'"
                            @click="$emit('agregar')"
                            class="flex-none px-3 py-1.5 bg-red-800 text-amber-100 text-xs font-bold uppercase tracking-wider rounded border border-amber-700 hover:bg-red-900 transition-colors shadow-sm cursor-pointer"
                        >
                            {{ btnLabel }}
                        </button>
                    </div>

                    <div class="flex-1 overflow-y-auto px-6 py-4">
                        <slot />
                    </div>

                    <div class="flex-none px-6 py-4 border-t border-stone-300 bg-[#f5efe0]">
                        <button
                            @click="$emit('close')"
                            class="w-full py-2 border border-stone-300 text-stone-600 bg-stone-100 hover:bg-stone-200 hover:text-stone-900 rounded font-bold uppercase text-xs tracking-widest transition-colors cursor-pointer"
                        >
                            Volver
                        </button>
                    </div>
                </div>
            </div>
        </Transition>
    </Teleport>
</template>