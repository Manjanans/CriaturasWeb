import { apiFetch } from '@/utils/shared';
import { useAuthStore } from '@/stores/authStore';
import { defineStore } from 'pinia';
import { ref } from 'vue';
import { useToast } from 'vue-toastification';

export const useBatallaStore = defineStore('batalla', () => {
    const toast = useToast();
    const iniciativa = ref([]);
    const criaturas = ref([]);
    const usuario = ref(0);
    const turno = ref({});

    const actualizaLista = async () => {
        try{
            iniciativa.value = await apiFetch('/batallas/iniciativa');
            const store = useAuthStore()
            const response = await store.verUsuario();
            usuario.value = response.id;
            if(iniciativa.value.length != 0){
                return true
            }
            return false
        }catch(e){
            console.log('No hay iniciativa disponible');
        }
    }

    const verCriaturas = async () => {
        try{
            const flag = await actualizaLista();
            if(flag){
                const params = new URLSearchParams();

                const listado = [...new Set(iniciativa.value.map(criatura => criatura.idcriatura).filter(id => id != null))];

                listado.forEach(id => {
                    params.append('listado', id)
                })

                criaturas.value = await apiFetch(
                    `/batallas/iniciativa/ver_criaturas?${params.toString()}`
                );
            }
        }catch(e){
            console.log('No hay iniciativa disponible');
        }
    }

    const verTurno = async () => {
        turno.value = await apiFetch('/batallas/ver_turno')
    }

    const batalla = async () => {
        try {
            const flag = await actualizaLista();
            if(flag){
                turno.value = await apiFetch('/batallas/crear_turno', { method: 'POST' });
            }
        } catch (e) {
            if (e.message === 'El usuario ya posee una batalla activa.') {
                await verTurno();
                return
            }
            console.log(e)
        }
    }

    const siguienteTurno = async (idt, index) => {
        const cuerpo = {
            'id': idt,
            'index_tabla': index
        }

        await apiFetch('/batallas/siguiente_turno', {
            method: 'PUT',
            body: JSON.stringify(cuerpo)
        });

        await verTurno();
    }

    const realizarDanio = async(cuerpo) => {
        let request = {};
        let string = '';

        const afectado = iniciativa.value.find(criatura => criatura.id === cuerpo.id);
        const datos = criaturas.value.find(criatura => criatura.id === afectado.idcriatura);
        const resistencia = Object.values(datos.data.resistencia).flat().find(r => r.idtipodanio === cuerpo.idresistencia)?.valor ?? 1;

        if(cuerpo.curar != ''){
            request.id = cuerpo.id;
            request.vida = parseInt(afectado.vida) + parseInt(cuerpo.curar);
            string = 'Cura realizada';
        }else{
            request.id = cuerpo.id;
            request.vida = parseInt(afectado.vida) - (parseInt(cuerpo.cantidad)*resistencia);
            if(request.vida <0){
                request.vida = 0
            }
            string = 'Daño realizado';
        }

        await apiFetch('/batallas/realizar_danio', {method:'PUT', body: JSON.stringify(request)});
        await actualizaLista();
        toast.success(string);
    }

    const finalizarBatalla = async () =>{
        await apiFetch('/batallas/finalizar_batalla', {method:'DELETE'});
        await actualizaLista();
        toast.success("Batalla finalizada");
    }

    return { actualizaLista, iniciativa, criaturas, verCriaturas, batalla, verTurno, turno, siguienteTurno, realizarDanio, finalizarBatalla }
});