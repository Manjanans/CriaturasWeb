import { defineStore } from 'pinia';
import { useToast } from 'vue-toastification';
import { useRouter } from 'vue-router';
import { ref, computed } from 'vue';

export const useAuthStore = defineStore('auth', () => 
{
        const toast = useToast();
        const router = useRouter();
        
        const accessToken = ref(localStorage.getItem('accessToken'));
        const isAuthenticated =  computed( () => {
                if (accessToken.value === null) {
                        return false
                }
                else {
                        return true
                }
        });

        async function login(formulario) {
                try{
                        const response = await fetch('/auth/token', {
                                method: 'POST',
                                headers: {
                                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
                                },
                                
                                body: `username=${encodeURIComponent(formulario.user)}&password=${encodeURIComponent(formulario.passw)}`
                        });

                        if (!response.ok) {
                                const err = await response.json()
                                throw new Error(err.detail)
                        }

                        const data = await response.json();
                        localStorage.setItem('accessToken', data.access_token)
                        toast.success("Cuenta validada");
                        accessToken.value = data.access_token;
                        router.push({name: 'dashboard'});
                }catch (e){
                        toast.error("Usuario o contraseña incorrectos, intenta nuevamente");
                        console.error('No se pudo', e);
                        formulario.user = '';
                        formulario.passw = '';
                }
        };

        async function createUser(formulario){
                const nuevo = {"username": formulario.user, "password":formulario.passw}

                try{
                        const response = await fetch('/auth/register', {
                                method: 'POST',
                                headers: {
                                'Content-Type': 'application/json'
                                },
                                body: JSON.stringify(nuevo)
                        });

                        if (!response.ok) {
                        const err = await response.json()
                        toast.error(err.detail)
                        throw new Error(err.detail);
                        }

                        toast.success("Usuario creado exitosamente");
                        formulario.user = '';
                        formulario.passw = '';
                } catch(e){
                        console.error("Hubo un error", e);
                        formulario.user = '';
                        formulario.passw = '';
                }
        }

        async function changePassword(formulario){
                const nuevo = {"username": formulario.user, "password":formulario.passw}

                try{
                        const response = await fetch('/auth/change-password', {
                                method: 'POST',
                                headers: {
                                'Content-Type': 'application/json'
                                },
                                body: JSON.stringify(nuevo)
                        });

                        if (!response.ok) {
                                const err = await response.json()
                                toast.error(err.detail);
                                throw new Error(err.detail);
                        }

                        toast.success("Contraseña cambiada exitosamente");
                        

                } catch(e){
                        console.error("Hubo un error", e);
                        formulario.user = '';
                        formulario.passw = '';
                }
        }

        function logout() {
                localStorage.removeItem('accessToken');
                accessToken.value = null;
                toast.success("Sesión cerrada correctamente");
        };

        async function verUsuario(){
                const response = await fetch('/auth/me', {
                        method: 'GET',
                        headers: {
                                'Authorization': `Bearer ${accessToken.value}`,
                                'Content-Type': 'application/json'
                        }       
                });

                const data = await response.json();

                return data
        }

    return {accessToken, isAuthenticated, login, logout, verUsuario, changePassword, createUser}
});