import { apiFetch } from '@/utils/shared';
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { useToast } from 'vue-toastification';

// apiFetch(ruta, body: JSON.stringify(datos))

export const useAccioneStore = defineStore('catalogo', () => {
    const habilidades = ref([]);
    const acciones = ref([]);
    const tipos = ref([]);
    const toast = useToast();

    const actualizaHabilidades = async (id) => {
        const todo = await apiFetch(`/acciones/ver_acciones/${id}`);
        try{
            acciones.value = todo.filter(accion => accion.tipo === "Acción")
            habilidades.value = todo.filter(accion => accion.tipo === "Habilidad")
        }catch (e){
            console.error(e)
        }
    }

    const cargarTipos = async () => {
        tipos.value = await apiFetch('/catalogos/ver_descripciones');
        return tipos
    }

    const agregarAccion = async (accion) => {
        console.log(accion.idcriatura)
        const agregar = {
            "idcriatura": accion.idcriatura,
            "idtipodesc": accion.idtipo,
            "titulodetalle": accion.titulo,
            "descripciondetalle": accion.descripcion
        }
        const response = await apiFetch(
            "acciones/agregar_accion", 
            {
            method: 'POST',
            body: JSON.stringify(agregar)
            }
        );
        toast.success("Habilidad agregada exitosamente")
    }

    return {actualizaHabilidades, tipos, agregarAccion, cargarTipos, habilidades, acciones}
});