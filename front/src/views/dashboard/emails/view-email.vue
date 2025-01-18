<template>
    <LayoutDashboard>
        <div class="p-8">
            <h1 class="text-4xl font-bold">{{ emailInfo.nome }}</h1>
            <p class="mb-6 text-xl">Recebido dia {{ formatDate(emailInfo.respondido_data) }}</p>

            <div class="min-h-[60vh] p-6 mb-4 bg-white rounded-lg shadow-lg">
                <div class="flex flex-col mb-6 gap-y-4">
                    <!-- email, subject, telefone, message -->
                    <div class="flex items-center gap-x-2">
                        <p class="text-xl font-bold">Email:</p>
                        <p class="text-md">{{ emailInfo.email }}</p>
                    </div>

                    <div class="flex items-center gap-x-2">
                        <p class="text-xl font-bold">Assunto:</p>
                        <p class="text-md">{{ emailInfo.assunto }}</p>
                         <!-- <p>Assunto</p> -->
                    </div>

                    <div class="flex items-center gap-x-2">
                        <p class="text-xl font-bold">Telefone:</p>
                        <p class="text-md">{{ emailInfo.telefone }}</p>
                    </div>

                    <div class="flex items-center gap-x-2">
                        <p class="text-xl font-bold">Mensagem:</p>
                        <p class="text-md">{{ emailInfo.mensagem }}</p>
                    </div>
                </div>
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { useRoute } from 'vue-router'
// import { fetchContatoById } from '@/services/contato.service'
import type { Contato } from '@/types/contato.types'
import { contatoService } from '@/services/contato.service'

const route = useRoute()
const emailId = route.params.id


function formatDate(data: string): string{
    if(!data) return '';
    const date = new Date(data);
    return isNaN(date.getTime())?'': date.toLocaleDateString('pt-BR')
}

const emailInfo = reactive<Contato>({
    id:0,
    nome:'',
    email:'',
    telefone:'',
    assunto:'',
    mensagem:'',
    respondido: false,
    respondido_data:'',
    envio_data: ''
})

onMounted(async () =>{
    try{
        if(emailId){
            const contato = await contatoService.getContato(emailId as string)
            Object.assign(emailInfo, contato)
        }
    }catch (error){
        console.error("Erro ao buscar dados", error)
    }
})

</script>
