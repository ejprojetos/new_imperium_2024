<template>
    <LayoutDashboard>
        <div class="p-8">
            <h1 class="text-4xl font-bold">{{ emailInfo.userName }}</h1>
            <p class="mb-6 text-xl">Recebido dia {{ emailInfo.recebidoDate }}</p>

            <div class="min-h-[60vh] p-6 mb-4 bg-white rounded-lg shadow-lg">
                <div class="flex flex-col mb-6 gap-y-4">
                    <!-- email, subject, telefone, message -->
                    <div class="flex items-center gap-x-2">
                        <p class="text-xl font-bold">Email:</p>
                        <p class="text-md">{{ emailInfo.email }}</p>
                    </div>

                    <div class="flex items-center gap-x-2">
                        <p class="text-xl font-bold">Assunto:</p>
                        <p class="text-md">{{ emailInfo.subject }}</p>
                    </div>

                    <div class="flex items-center gap-x-2">
                        <p class="text-xl font-bold">Telefone:</p>
                        <p class="text-md">{{ emailInfo.telefone }}</p>
                    </div>

                    <div class="flex items-center gap-x-2">
                        <p class="text-xl font-bold">Mensagem:</p>
                        <p class="text-md">{{ emailInfo.message }}</p>
                    </div>
                </div>
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { toast } from 'vue-sonner'
import { useRoute } from 'vue-router'

const route = useRoute()
const emailId = route.params.id

const emailInfo = reactive({
    id: emailId,
    userName: 'Beatriz',
    recebidoDate: '28/04/2022',
    email: 'beatriz@gmail.com',
    subject: 'Consulta de Paciente',
    message: 'Olá, tudo bem?',
    telefone: '(11) 99999-9999',
    status: 'Não lida'
})
</script>
