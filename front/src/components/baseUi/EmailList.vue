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
                            <span class="font-semibold">{{ email.name }}</span>
                            <div class="text-sm text-gray-500">
                                <span>Respondido dia {{ email.respondedDate }}</span>
                                <span class="mx-2">|</span>
                                <span>Recebido dia {{ email.receivedDate }}</span>
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
                            <span class="font-semibold">{{ email.name }}</span>
                            <div class="text-sm text-gray-500">
                                <span>Recebido dia {{ email.receivedDate }}</span>
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
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

interface Email {
    id: number
    name: string
    respondedDate?: string
    receivedDate: string
}

const respondedEmails = ref<Email[]>([
    { id: 1, name: 'Norma Andrade Silva', respondedDate: '28/02/20', receivedDate: '28/02/20' },
    { id: 2, name: 'Eduardo Maxado de Assis', respondedDate: '28/02/20', receivedDate: '28/02/20' },
    {
        id: 3,
        name: 'Roberta Nunes Brito de Fa...',
        respondedDate: '28/02/20',
        receivedDate: '28/02/20'
    },
    { id: 4, name: 'Ana Claudia Barbosa', respondedDate: '28/02/20', receivedDate: '28/02/20' }
])

const pendingEmails = ref<Email[]>([
    { id: 5, name: 'Beatriz Guedes', receivedDate: '28/02/20' },
    { id: 6, name: 'Andre Luis da Silva', receivedDate: '28/02/20' },
    { id: 7, name: 'Alexandre de Castro', receivedDate: '28/02/20' }
])

const openEmail = (id: number) => {
    router.push(`/dashboard/emails/${id}`)
}
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
