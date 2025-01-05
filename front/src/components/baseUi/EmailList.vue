<template>
    <div class="space-y-6">
        <div class="overflow-hidden bg-white shadow-lg rounded-3xl">
            <div class="p-4 text-white bg-primary">
                <h2 class="text-lg font-semibold">Emails respondidos</h2>
            </div>
            <ul>
                <li
                    v-for="email in respondedEmails"
                    :key="email.id"
                    class="border-b last:border-b-0">
                    <div class="flex items-center justify-between p-4 hover:bg-blue-200">
                        <div class="flex-grow">
                            <span class="font-semibold">{{ email.nome }}</span>
                            <div class="text-sm text-gray-500">
                                <span>Respondido dia {{ email.respondido_data }}</span>
                                <span class="mx-2">|</span>
                                <span>Recebido dia {{ email.envio_data }}</span>
                            </div>
                        </div>
                        <button
                            @click="openEmail(email.id)"
                            class="px-4 py-2 text-white transition-colors bg-blue-600 rounded-md hover:bg-blue-600">
                            Abrir
                        </button>
                    </div>
                </li>
            </ul>
        </div>

        <div class="overflow-hidden bg-white shadow-lg rounded-3xl">
            <div class="p-4 text-white bg-red-700">
                <h2 class="text-lg font-semibold">Emails Pendentes</h2>
            </div>
            <ul>
                <li v-for="email in pendingEmails" :key="email.id" class="border-b last:border-b-0">
                    <div class="flex items-center justify-between p-4 hover:bg-blue-200">
                        <div class="flex-grow">
                            <span class="font-semibold">{{ email.nome }}</span>
                            <div class="text-sm text-gray-500">
                                <span>Recebido dia {{ email.envio_data }}</span>
                            </div>
                        </div>
                        <button
                            @click="openEmail(email.id)"
                            class="px-4 py-2 text-white transition-colors bg-blue-600 rounded-md hover:bg-blue-600">
                            Abrir
                        </button>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { fetchContatos } from '@/services/contato.service'
import { Contato } from '@/types/contato.types'


const router = useRouter()

interface Email {
    id: number
    nome: string
    telefone?: string
    email?: string
    mensagem?: string
    respondido?: boolean
    envio_data?: string
    respondido_data?:string
}



// const respondedEmails = ref<Email[]>([
//     { id: 1, name: 'Norma Andrade Silva', respondedDate: '28/02/20', receivedDate: '28/02/20' },
//     { id: 2, name: 'Eduardo Maxado de Assis', respondedDate: '28/02/20', receivedDate: '28/02/20' },
//     {
//         id: 3,
//         name: 'Roberta Nunes Brito de Fa...',
//         respondedDate: '28/02/20',
//         receivedDate: '28/02/20'
//     },
//     { id: 4, name: 'Ana Claudia Barbosa', respondedDate: '28/02/20', receivedDate: '28/02/20' }
// ])

const respondedEmails = ref<Email[]>([]);
const pendingEmails = ref<Email[]>([]);
const error = ref<string | null>(null);
// const pendingEmails = ref<Email[]>([
//     { id: 5, name: 'Beatriz Guedes', receivedDate: '28/02/20' },
//     { id: 6, name: 'Andre Luis da Silva', receivedDate: '28/02/20' },
//     { id: 7, name: 'Alexandre de Castro', receivedDate: '28/02/20' }
// ])

const openEmail = (id: number) => {
    router.push(`/dashboard/emails/${id}`)
}



//Requisição HTTP

onMounted(async () => {
    try{
        const contatos = await fetchContatos();

        //Mapear dados

        respondedEmails.value = contatos.filter((contato) => contato.respondido).map((contato) => ({
            id: contato.id,
            nome: contato.nome,
            respondido_data: new Date().toLocaleDateString(),
            envio_data: new Date().toLocaleDateString(),
        }))

        pendingEmails.value = contatos.filter((contato) => !contato.respondido).map((contato) => ({
            id: contato.id,
            nome: contato.nome,
            envio_data: new Date().toLocaleDateString(),
        }));
    } catch(err){
        error.value = 'Erro ao carregar emails';
        console.error(err)
    }
})
</script>

<style scoped>
ul {
    list-style: none;
    padding: 0;
}

ul li:nth-child(even) {
    background-color: #deecfa;
}
</style>
