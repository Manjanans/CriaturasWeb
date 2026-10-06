<script setup>
defineProps({
    show:  { type: Boolean, default: false },
    title: { type: String,  default: '' },
});
defineEmits(['close']);
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
                class="fixed inset-0 z-[10000] bg-black/85 backdrop-blur-sm flex items-center justify-center p-4"
                @click="$emit('close')"
            >
                <div
                    class="relative flex flex-col w-full md:w-[420px] bg-[#f5efe0] rounded border-2 border-amber-700 shadow-2xl text-stone-900 overflow-hidden"
                    @click.stop
                >
                    <!-- HEADER -->
                    <div class="flex-none px-6 py-4 border-b-2 border-red-800">
                        <h2 class="text-xl font-bold uppercase tracking-widest text-red-800 font-serif">
                            {{ title }}
                        </h2>
                    </div>

                    <!-- CONTENT -->
                    <div class="px-6 py-5">
                        <slot />
                    </div>
                </div>
            </div>
        </Transition>
    </Teleport>
</template>
