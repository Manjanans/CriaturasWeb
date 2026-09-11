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
    
    const crearNuevaCriatura = async (criatura) =>{
        if(criatura.publico === "false"){
            const response = await apiFetch('/auth/me');
            criatura.id_privado = response.id
        }

        const criaturaBody = {
            "base":{
                "cantdados": criatura.cantdados ? criatura.cantdados : 0,
                "tipodado": criatura.tipodado ? criatura.tipodado : 0,
                "vidatotal": criatura.vidatotal ? criatura.vidatotal : 0,
                "modificadorvida": criatura.modificadorvida ? criatura.modificadorvida : 0,
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

    return {criaturas, verDetalle, abiertos, detalles, actualizaLista, crearNuevaCriatura}
})