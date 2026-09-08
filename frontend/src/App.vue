<template>
    <Navbar :show="auth.isAuthenticated" />
    <RouterView />
</template>

<script setup>
import Navbar from '@/components/shared/Navbar.vue';
import { useAuthStore } from '@/utils/auth.js'

const auth = useAuthStore()
</script>

<style>
</style>