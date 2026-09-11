import { apiFetch } from '@/utils/shared';
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { useToast } from 'vue-toastification';

// apiFetch(ruta, body: JSON.stringify(datos))

export const useResistenciaStore = defineStore('resistencia', () => {
    const resistencias = ref([]);
    const tipos = ref([]);
    const toast = useToast();

    const actualizaResistencias = async (id) => {
        resistencias.value = await apiFetch(`/resistencias/ver_resistencias/${id}`);
    }

    const cargarTipos = async () => {
        tipos.value = await apiFetch('/catalogos/ver_danios');
        return tipos
    }

    const agregarResistencia = async (accion) => {
        const agregar = {
            "idcriatura": accion.idcriatura,
            "idtipodanio": accion.idtipo,
            "cantidad": accion.cantidad
        }
        const response = await apiFetch(
            "/resistencias/crear_resistencia", 
            {
            method: 'POST',
            body: JSON.stringify(agregar)
            }
        );
        toast.success("Resistencia agregada exitosamente");
        actualizaResistencias(accion.idcriatura);
    }

    return { resistencias, tipos, actualizaResistencias, cargarTipos, agregarResistencia }
});