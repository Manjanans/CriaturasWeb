import { apiFetch } from '@/utils/shared';
import { useAuthStore } from '@/stores/authStore';
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { useToast } from 'vue-toastification';

export const useIniciativaStore = defineStore('iniciativa', () => {
    const toast = useToast();
    const iniciativa = ref([]);
    const usuario = ref(0);

    const actualizaLista = async () => {
        iniciativa.value = await apiFetch('/batallas/iniciativa');
        const store = useAuthStore()
        const response = await store.verUsuario();
        usuario.value = response.id;
    }

    const editarIniciativa = async (tipo, id, cambio) => {
        const actualizacion = {
            id: id,
            idusuario: usuario.value,
        }
        if (cambio != '') {
            switch (tipo) {
                case 'value':
                    actualizacion.valoriniciativa = cambio;
                    break;
                case 'hp':
                    actualizacion.vida = cambio;
                    break;
                case 'name':
                    actualizacion.nombrecriatura = cambio;
                    break;
            }

            const req = apiFetch(`/batallas//iniciativa/editar_iniciativa`, {
                method: 'PUT',
                body: JSON.stringify(actualizacion)
            })

            toast.success("Iniciativa actualizada exitosamente");
            await actualizaLista();
        }
    }

    const agregarIniciativa = async (objeto) => {
        const {
            name,
            tipo,
            vida,
            iniciativa,
            idcriatura
        } = objeto

        const agregar = {
            idusuario: usuario.value,
            nombrecriatura: name,
            valoriniciativa: iniciativa,
            idcriatura: null,
            vida: null
        }

        if (tipo === '2') {
            agregar.idcriatura = idcriatura
            agregar.vida = vida
        }

        const request = await apiFetch('/batallas/iniciativa/crear', {
            method: 'POST',
            body: JSON.stringify(agregar)
        }
        );

        toast.success("Iniciativa agregada exitosamente");
        await actualizaLista();
    }

    const eliminarIniciativa = async (id) => {
        const response = await apiFetch(
            `/batallas/iniciativa/eliminar_iniciativa/${id}`, 
            {
            method: 'DELETE'
            }
        );
        toast.success("Criatura eliminada exitosamente de la iniciativa");
        actualizaLista();
    }



    return { actualizaLista, iniciativa, agregarIniciativa, editarIniciativa, eliminarIniciativa }

})