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
import { contatoService } from '@/services/contato.service'


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


const respondedEmails = ref<Email[]>([]);
const pendingEmails = ref<Email[]>([]);
const error = ref<string | null>(null);

const openEmail = (id: number) => {
    console.log("Abrindo email com id:", id)
    router.push(`/dashboard/emails/${id}`)
}

const formatDate = (dateString: string): string => {
    const date = new Date(dateString);
    const day = date.getUTCDate().toString().padStart(2, '0');
    const month = (date.getUTCMonth() + 1).toString().padStart(2, '0'); 
    const year = date.getUTCFullYear();
    return `${day}/${month}/${year}`;
};

//Requisição HTTP

onMounted(async () => {
    try{
        const contatos = await contatoService.getAllContatos();

        //Mapear dados

        respondedEmails.value = contatos.filter((contato) => contato.respondido).map((contato) => ({
            id: contato.id,
            nome: contato.nome,
            respondido_data: formatDate(contato.respondido_data),
            envio_data: formatDate(contato.envio_data),
        }))

        pendingEmails.value = contatos.filter((contato) => !contato.respondido).map((contato) => ({
            id: contato.id,
            nome: contato.nome,
            envio_data: formatDate(contato.envio_data),
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
