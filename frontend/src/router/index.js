import { createRouter, createWebHistory } from 'vue-router';

import LoginView from '@/views/LoginView.vue';
import DashboardView from '@/views/DashboardView.vue';

const routes = [
    {
        path: '/',
        name: 'login',
        component:LoginView
    },
    {
        path: '/dashboard',
        name: 'dashboard',
        component: DashboardView,
        meta: { requiresAuth: true }
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

router.beforeEach((to) => {
  const token = localStorage.getItem('accessToken');
  if (to.meta.requiresAuth && !token) {
    return { name: 'login' }    // redirige al login
  }
  if (to.name === 'login' && token) {
    return { name: 'dashboard' }
  }
});

export default router;