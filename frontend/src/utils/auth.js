import { defineStore } from 'pinia'
import { useToast } from 'vue-toastification';

const toast = useToast();

export const useAuthStore = defineStore('auth', {
    state: () => ({
        accessToken: localStorage.getItem('accessToken')
    }),

    getters: {
        isAuthenticated: (state) => !!state.accessToken
    },

    actions: {
        login(token) {
            this.accessToken = token
            localStorage.setItem('accessToken', token)
        },

        logout() {
            this.accessToken = null;
            localStorage.removeItem('accessToken');
            toast.success("Sesión cerrada correctamente");
        }
    }
})