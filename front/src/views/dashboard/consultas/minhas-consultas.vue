<template>
    <LayoutDashboard>
        <div class="p-8">
            <div class="flex justify-between mb-8">
                <div class="flex items-center">
                    <img
                        src="/src/assets/placeholder.png"
                        alt="Profile"
                        class="w-16 h-16 mr-4 rounded-full" />
                    <h1 class="text-2xl font-bold">Gabriele Rocha de Carvalho</h1>
                </div>
                <div class="p-4 bg-white rounded-lg shadow-md">
                    <h2 class="mb-2 font-bold">Pagamentos</h2>
                    <button class="px-4 py-2 text-white bg-blue-600 rounded">Acessar Asaas</button>
                </div>
            </div>

            <div class="flex items-center mt-8 mb-12 gap-x-4">
                <button class="px-4 py-2 text-white bg-blue-700 rounded-full">Hoje</button>
                <button class="px-4 py-2 bg-gray-200 rounded-full">Amanhã</button>
                <button class="px-4 py-2 bg-gray-200 rounded-full">Dia da Semana</button>
                <button class="px-4 py-2 bg-gray-200 rounded-full">Mês</button>
                <button class="px-4 py-2 bg-gray-200 rounded-full">Confirmadas</button>
                <button class="px-4 py-2 bg-gray-200 rounded-full">Buscar</button>
                <input
                    type="text"
                    class="px-4 py-2 bg-gray-200 rounded-full"
                    placeholder="Buscar" />
                <button class="p-2 bg-gray-200 rounded-full">
                    <Search />
                </button>
            </div>

            <div class="space-y-4">
                <div
                    v-for="appointment in appointments"
                    :key="appointment.id"
                    class="flex items-center justify-between p-4 bg-white rounded-lg shadow-md">
                    <div>
                        <div class="text-sm text-gray-500">{{ appointment.date }}</div>
                        <div class="font-bold">{{ appointment.time }}</div>
                    </div>
                    <div class="flex-grow ml-4">
                        <div class="font-bold">{{ appointment.doctor }}</div>
                        <div class="text-sm">{{ appointment.clinic }}</div>
                        <div class="text-sm">{{ appointment.room }}</div>
                    </div>
                    <button class="px-4 py-2 text-white bg-blue-600 rounded">Ver Prontuário</button>
                </div>
            </div>

            <div class="flex justify-center mt-8">
                <button class="px-3 py-1 mx-1 bg-gray-200 rounded-full">&lt;</button>
                <button class="px-3 py-1 mx-1 bg-gray-200 rounded-full">1</button>
                <button class="px-3 py-1 mx-1 bg-gray-200 rounded-full">2</button>
                <button class="px-3 py-1 mx-1 text-white bg-blue-600 rounded-full">3</button>
                <button class="px-3 py-1 mx-1 bg-gray-200 rounded-full">4</button>
                <button class="px-3 py-1 mx-1 bg-gray-200 rounded-full">5</button>
                <button class="px-3 py-1 mx-1 bg-gray-200 rounded-full">&gt;</button>
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { Search } from 'lucide-vue-next'

const appointments = ref([
    {
        id: 1,
        date: '15/11/2019',
        time: 'Fila: 1º 07h30',
        doctor: 'Oftalmologista: Dra. Rafaela Veríssimo',
        clinic: 'Clínica Dr. Alexandre - Av. Senador Salgado Filho, 373, 59.000 - 000',
        room: 'Sala: 02'
    }
    // Add more appointments here...
])
</script>
