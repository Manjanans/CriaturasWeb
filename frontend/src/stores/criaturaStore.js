import { apiFetch } from '@/utils/shared';
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { useToast } from 'vue-toastification';

export const useCriaturaStore = defineStore('criatura', () => 
{
    const toast = useToast();
    const criaturas = ref([]);
    const detalles = ref([]);
    const abiertos = ref([]);

    const actualizaLista = async () => {
        criaturas.value = await apiFetch('/criaturas/');
    }

    const verDetalle = async (id) => {
        if (!detalles.value[id]) {
            detalles.value[id] = await apiFetch(
                `/criaturas/ver_criatura/${id}`
            );
        }
        if (abiertos.value.includes(id)) {
            abiertos.value = abiertos.value.filter(i => i !== id);
        } else {
            abiertos.value.push(id);
        }
    }

    const detalleEliminacion = async (id) => {
        const det = await apiFetch(
                `/criaturas/ver_criatura/${id}`
        );
        const valores = {
            'nombre' : det.nombre,
            'id' : det.id
        }
        return valores;
    }

    const detalleCriatura = async(id) => {
        const det = await apiFetch(
                `/criaturas/edicion_criatura/${id}`
        );

        return det
    }
    
    const crearNuevaCriatura = async (criatura) =>{
        if(criatura.publico === "false"){
            const response = await apiFetch('/auth/me');
            criatura.id_privado = response.id
        }

        const criaturaBody = {
            "base":{
                "cantdados": criatura.cantdados ? criatura.cantdados:0,
                "tipodado": criatura.tipodado ? criatura.tipodado:0,
                "vidatotal": criatura.vidatotal ? criatura.vidatotal:0,
                "modificadorvida": criatura.modificadorvida ? criatura.modificadorvida:0,
                "nombre": criatura.nombre,
                "cantexp": criatura.cantexp,
                "publico": criatura.publico,
                "id_privado": criatura.id_privado
            },
            "stats":{
                "clasearmadura": criatura.clasearmadura,
                "velocidad": criatura.velocidad,
                "fuerza": criatura.fuerza,
                "destreza": criatura.destreza,
                "constitucion": criatura.constitucion,
                "inteligencia": criatura.inteligencia,
                "sabiduria": criatura.sabiduria,
                "carisma": criatura.carisma
            }
        }

        const response = await apiFetch('/criaturas/crear', {
            method:'POST',
            body: JSON.stringify(criaturaBody)
        });

        toast.success("Criatura creada exitosamente");
        await actualizaLista();    
    }

    const eliminarCriatura = async (id) =>{
        await apiFetch(`/criaturas/eliminar_criatura/${id}`, {
            method: 'DELETE'
        });
        toast.success("Criatura eliminada exitosamente");
        await actualizaLista();
    }

    const editarCriatura = async(criatura) =>{
        const base = {
            "id": criatura.idcriatura,
            "cantdados": criatura.cantdados,
            "tipodado": criatura.tipodado,
            "vidatotal": criatura.vidatotal,
            "modificadorvida": criatura.modificadorvida,
            "nombre": criatura.nombre,
            "cantexp": criatura.cantexp,
            "publico": criatura.publico,
            "id_privado": criatura.id_privado ? criatura.id_privado : null
        }

        const stats = {
            "id": criatura.idstat,
            "idcriatura": criatura.idcriatura,
            "clasearmadura": criatura.clasearmadura,
            "velocidad": criatura.velocidad,
            "fuerza": criatura.fuerza,
            "destreza": criatura.destreza,
            "constitucion": criatura.constitucion,
            "inteligencia": criatura.inteligencia,
            "sabiduria": criatura.sabiduria,
            "carisma": criatura.carisma
        }

        const actualizaBase = await apiFetch('/criaturas/actualizar_criatura', {
            method: 'PUT',
            body: JSON.stringify(base)
        });
        const actualizaStats = await apiFetch('/criaturas/actualizar_detalle', {
            method: 'PUT',
            body: JSON.stringify(stats)
        });

        
        toast.success("Criatura actualizada exitosamente");
        await actualizaLista();
    }

    const calcularModificador = (atr) =>{
        return Math.floor((atr-10)/2)
    }

    const calcularVida = (dados, tipo, vida, mod) => {
        if (vida!=0){
            return vida
        }else{
            let life = mod;
            for(let i=0; i<dados; i++){
                let valor = Math.floor(Math.random()*tipo)+1;
                life+=valor
            }
            return life
        }
    }

    const buscarCriatura = async (nombre) => {
        if(nombre === '')
        {
            await actualizaLista()
            return
        }
        try{
            criaturas.value = await apiFetch(`/criaturas/buscar_criatura/${nombre}`);
        }catch
        {
            criaturas.value = [];
        }
        
    }

    return { buscarCriatura, calcularModificador, calcularVida, criaturas, verDetalle, abiertos, detalles, actualizaLista, crearNuevaCriatura, eliminarCriatura, detalleEliminacion, detalleCriatura, editarCriatura }
})