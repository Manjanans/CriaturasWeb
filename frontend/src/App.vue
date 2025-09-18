<template>
  <div id="app-wrapper" :class="{ 'center-content': !isLoggedIn }">
    <Dashboard v-if="isLoggedIn" @logout="handleLogout" />
    <Login v-else @login-success="handleLoginSuccess" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Login from './components/Login.vue';
import Dashboard from './components/Dashboard.vue';

const isLoggedIn = ref(false);

// Check for an existing token when the app loads
onMounted(() => {
  const token = localStorage.getItem('accessToken');
  if (token) {
    isLoggedIn.value = true;
  }
});

const handleLoginSuccess = () => {
  isLoggedIn.value = true;
};

const handleLogout = () => {
  isLoggedIn.value = false;
};
</script>

<style>
#app-wrapper {
  width: 100%;
  min-height: 100vh;
}

#app-wrapper.center-content {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>