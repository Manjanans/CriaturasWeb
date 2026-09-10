<template>
    <Navbar :show="useAuthStore().isAuthenticated" />
    <RouterView />
</template>

<script setup>
import Navbar from '@/components/shared/Navbar.vue';
import { useAuthStore } from '@/stores/authStore'
</script>

<style>
</style>