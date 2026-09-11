import { apiFetch } from '@/utils/shared';
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { useToast } from 'vue-toastification';

// apiFetch(ruta, body: JSON.stringify(datos))

export const useInmunidadStore = defineStore('inmunidad', () => {
    const inmunidades = ref([]);
    const tipos = ref([]);
    const toast = useToast();

    const actualizaInmunidades = async (id) => {
        inmunidades.value = await apiFetch(`/inmunidades/ver_inmunidades/${id}`);
    }

    const cargarTipos = async () => {
        tipos.value = await apiFetch('/catalogos/ver_condiciones');
        return tipos
    }

    const agregarInmunidad = async (accion) => {
        const agregar = {
            "idcriatura": accion.idcriatura,
            "idtipocondicion": accion.idtipo
        }
        const response = await apiFetch(
            "/inmunidades/crear_inmunidad", 
            {
            method: 'POST',
            body: JSON.stringify(agregar)
            }
        );
        toast.success("Inmunidad agregada exitosamente");
        actualizaInmunidades(accion.idcriatura);
    }

    return { inmunidades, tipos, actualizaInmunidades, cargarTipos, agregarInmunidad }
});