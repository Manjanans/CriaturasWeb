<script setup>
const props = defineProps({
    show: Boolean
});
</script>

<template>
    <div v-if="show" class="pt-5">
        <slot></slot>
    </div>
</template>