<template>
    <form @submit.prevent="acceder">
        <label for="user">Ingresa el usuario:</label>
        <input v-model="user" type="text" name="user" id="user">
        <label for="passw">Ingresa la contraseña:</label>
        <input v-model="passw" type="password" name="passw" id="passw">
        <button type="submit">Crear</button>
    </form>
</template>

<script setup>
    import { ref } from 'vue';

    const user = ref('');
    const passw = ref('');

    const crearUsuario = async () =>{
        const nuevo = {"username": user.value, "password":passw.value}

        const response = await fetch('/auth/register', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(nuevo)
        });

        if (!response.ok) {
            const err = await response.json()
            throw new Error(err.detail === 'Incorrect username or password'
            ? 'Usuario o contraseña incorrectos'
            : err.detail
            )
        }

        const data = await response.json();

        console.log(data);
    }

    const acceder = async () => {
        const response = await fetch('/auth/token', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
            },
            
            body: `username=${encodeURIComponent(user.value)}&password=${encodeURIComponent(passw.value)}`
        });

        if (!response.ok) {
            const err = await response.json()
            throw new Error(err.detail === 'Incorrect username or password'
            ? 'Usuario o contraseña incorrectos'
            : err.detail
            )
        }

        const data = await response.json();
        
        localStorage.setItem('accessToken', data.access_token);
    }
</script>