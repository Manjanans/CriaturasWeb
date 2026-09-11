import { apiFetch } from '@/utils/shared';
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { useToast } from 'vue-toastification';

// apiFetch(ruta, body: JSON.stringify(datos))

export const useHabilidadStore = defineStore('habilidad', () => {
    const habilidades = ref([]);
    const tipos = ref([]);
    const toast = useToast();

    const actualizaHabilidades = async (id) => {
        habilidades.value = await apiFetch(`/habilidades/ver_habilidades/${id}`);
    }

    const cargarTipos = async () => {
        tipos.value = await apiFetch('/catalogos/ver_habilidades');
        return tipos
    }

    const agregarHabilidad = async (accion) => {
        const agregar = {
            "idcriatura": accion.idcriatura,
            "idhabilidad": accion.idtipo,
            "modificador": accion.cantidad
        }
        const response = await apiFetch(
            "/habilidades/crear_habilidad", 
            {
            method: 'POST',
            body: JSON.stringify(agregar)
            }
        );
        toast.success("Habilidad agregada exitosamente");
        actualizaHabilidades(accion.idcriatura);
    }

    return { habilidades, tipos, actualizaHabilidades, cargarTipos, agregarHabilidad }
});