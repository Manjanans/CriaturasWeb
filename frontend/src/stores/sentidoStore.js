import { apiFetch } from '@/utils/shared';
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { useToast } from 'vue-toastification';

// apiFetch(ruta, body: JSON.stringify(datos))

export const useSentidoStore = defineStore('sentido', () => {
    const sentidos = ref([]);
    const tipos = ref([]);
    const toast = useToast();

    const actualizaSentidos = async (id) => {
        sentidos.value = await apiFetch(`/sentidos/ver_sentidos/${id}`);
    }

    const cargarTipos = async () => {
        tipos.value = await apiFetch('/catalogos/ver_sentidos');
        return tipos
    }

    const agregarSentido = async (accion) => {
        const agregar = {
            "idcriatura": accion.idcriatura,
            "idtiposentido": accion.idtipo,
            "cantidad": accion.cantidad
        }
        const response = await apiFetch(
            "/sentidos/crear_sentido", 
            {
            method: 'POST',
            body: JSON.stringify(agregar)
            }
        );
        toast.success("Sentido agregado exitosamente");
        actualizaSentidos(accion.idcriatura);
    }

    return { sentidos, tipos, actualizaSentidos, cargarTipos, agregarSentido }
});