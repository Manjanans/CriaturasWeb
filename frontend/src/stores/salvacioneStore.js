import { apiFetch } from '@/utils/shared';
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { useToast } from 'vue-toastification';

// apiFetch(ruta, body: JSON.stringify(datos))

export const useSalvacionStore = defineStore('salvacion', () => {
    const salvaciones = ref([]);
    const tipos = ref([]);
    const toast = useToast();

    const actualizaSalvaciones = async (id) => {
        salvaciones.value = await apiFetch(`/salvaciones/ver_salvaciones/${id}`);
    }

    const cargarTipos = async () => {
        tipos.value = await apiFetch('/catalogos/ver_caracteristicas');
        return tipos
    }

    const agregarSalvacion = async (accion) => {
        const agregar = {
            "idcriatura": accion.idcriatura,
            "idcaracteristica": accion.idtipo,
            "modificador": accion.cantidad
        }
        const response = await apiFetch(
            "/salvaciones/crear_salvacion", 
            {
            method: 'POST',
            body: JSON.stringify(agregar)
            }
        );
        toast.success("Tirada de salvación agregada exitosamente");
        actualizaSalvaciones(accion.idcriatura);
    }

    return { salvaciones, tipos, actualizaSalvaciones, cargarTipos, agregarSalvacion }
});