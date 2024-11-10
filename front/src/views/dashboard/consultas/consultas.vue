<template>
    <LayoutDashboard>
        <div
            class="flex px-12 mt-12 gap-x-4 max-lg:flex-col max-lg:items-start max-lg:gap-x-0 max-lg:w-full max-lg:gap-y-4 max-lg:mt-4">
            <div class="p-4 bg-blue-100 rounded-lg shadow-lg min-w-56 max-lg:w-full">
                <h3 class="text-3xl font-bold">20</h3>
                <p class="mt-2">Consultas</p>
                <p class="font-bold">Hoje</p>
            </div>
            <div class="p-4 bg-red-200 rounded-lg shadow-lg min-w-56 max-lg:w-full">
                <h3 class="text-3xl font-bold">2</h3>
                <p class="mt-2">Consultas Atrasadas</p>
                <p class="font-bold">Hoje</p>
            </div>
            <div class="p-4 bg-green-100 rounded-lg shadow-lg min-w-56 max-lg:w-full">
                <h3 class="mb-8 text-xl font-bold">Cadastrar Consultas</h3>
                <router-link to="/dashboard/perfil/recepcionista/cadastrar-consulta">
                    <button class="w-full py-2 text-xs text-white min-h-unset btn bg-primary hover:bg-primary">
                        Cadastrar
                    </button>
                </router-link>

            </div>
            <div class="p-4 bg-white rounded-lg shadow-lg min-w-56 max-lg:w-full">
                <h3 class="mb-8 text-xl font-bold">Pagamentos</h3>
                <button class="w-full py-2 text-xs text-white min-h-unset btn bg-primary hover:bg-primary">
                    Acessar Asaas
                </button>
            </div>
        </div>

        <!-- Filter Tabs -->
        <div class="flex items-center px-12 mt-8 gap-x-4">
            <button class="px-4 py-2 text-white bg-blue-700 rounded-full">Hoje</button>
            <button class="px-4 py-2 bg-gray-200 rounded-full">Amanhã</button>
            <button class="px-4 py-2 bg-gray-200 rounded-full">Dia da Semana</button>
            <button class="px-4 py-2 bg-gray-200 rounded-full">Mês</button>
            <button class="px-4 py-2 bg-gray-200 rounded-full">Confirmadas</button>
            <button class="px-4 py-2 bg-gray-200 rounded-full">Buscar</button>
            <input type="text" class="px-4 py-2 bg-gray-200 rounded-full" placeholder="Buscar" />
            <button class="p-2 bg-gray-200 rounded-full">
                <Search />
            </button>
        </div>

        <!-- Appointments List -->
        <div class="px-12 mt-8">
            <div v-for="appointment in appointments" :key="appointment.name"
                class="flex items-center justify-between p-4 mb-4 bg-white rounded-lg shadow">
                <div class="flex items-center space-x-4">
                    <div class="flex flex-col text-xs">
                        <span class="text-xs text-gray-600">{{ appointment.date }}</span>
                        <div class="text-lg font-bold">{{ appointment.time }}</div>
                    </div>
                    <div>
                        <div class="flex gap-x-2">
                            <div class="font-semibold">{{ appointment.name }}</div>
                            <span :class="statusClass(appointment.status)" class="px-2 py-1 text-sm rounded-full">
                                {{ appointment.status }}
                            </span>
                        </div>
                        <div class="text-sm text-gray-600">{{ appointment.doctor }}</div>
                        <div class="text-sm text-gray-600">{{ appointment.room }}</div>
                    </div>
                </div>
                <div class="flex items-center space-x-2">
                    <button class="px-4 py-2 text-white bg-blue-700 rounded-lg">
                        Ver Prontuário
                    </button>
                    <RouterLink to="/dashboard/medicos/editar-consultas">
                        <button class="px-4 py-2 text-blue-700 bg-blue-100 rounded-lg">Editar</button>
                    </RouterLink>
                </div>
            </div>
        </div>

        <!-- Pagination -->
        <div class="flex justify-center mt-8">
            <div class="flex space-x-2">
                <button class="px-3 py-1 bg-gray-200 rounded-full">&lt;</button>
                <button class="px-3 py-1 bg-gray-200 rounded-full">1</button>
                <button class="px-3 py-1 bg-gray-200 rounded-full">2</button>
                <button class="px-3 py-1 text-white bg-blue-700 rounded-full">3</button>
                <button class="px-3 py-1 bg-gray-200 rounded-full">4</button>
                <button class="px-3 py-1 bg-gray-200 rounded-full">5</button>
                <button class="px-3 py-1 bg-gray-200 rounded-full">&gt;</button>
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { Search } from 'lucide-vue-next'
import { RouterLink } from 'vue-router';
import router from '@/router';

const appointments = ref([
    {
        time: '07h30',
        date: '15/11',
        name: 'Fernando Lucas',
        doctor: 'Oftalmologista: Dra. Rafaela Verissimo',
        room: 'Sala: 02',
        status: 'Confirmada'
    },
    {
        time: '08h30',
        date: '15/11',
        name: 'Matheus Alves',
        doctor: 'Cardiologista: Dr. João Silva',
        room: 'Sala: 03',
        status: 'Confirmada'
    },
    {
        time: '09h30',
        date: '15/11',
        name: 'Daniel Castro',
        doctor: 'Pediatra: Dra. Ana Paula',
        room: 'Sala: 01',
        status: 'Atrasada'
    },
    {
        time: '10h30',
        date: '15/11',
        name: 'Ana Beatriz',
        doctor: 'Dermatologista: Dr. Carlos Mendes',
        room: 'Sala: 04',
        status: 'Confirmada'
    },
    {
        time: '11h30',
        date: '15/11',
        name: 'Aroldo Carvalho',
        doctor: 'Ginecologista: Dra. Maria Oliveira',
        room: 'Sala: 05',
        status: 'Confirmada'
    },
    {
        time: '13h00',
        date: '15/11',
        name: 'Juliana Santos',
        doctor: 'Oftalmologista: Dra. Rafaela Verissimo',
        room: 'Sala: 02',
        status: 'Confirmada'
    },
    {
        time: '14h00',
        date: '15/11',
        name: 'Ricardo Lima',
        doctor: 'Ortopedista: Dr. Felipe Costa',
        room: 'Sala: 06',
        status: 'Confirmada'
    },
    {
        time: '15h00',
        date: '15/11',
        name: 'Fernanda Almeida',
        doctor: 'Endocrinologista: Dr. Lucas Pereira',
        room: 'Sala: 07',
        status: 'Atrasada'
    }
])

const statusClass = (status: string) => {
    switch (status) {
        case 'Confirmada':
            return 'text-green-800 bg-green-200'
        case 'Atrasada':
            return 'text-red-800 bg-red-200'
        default:
            return 'text-gray-800 bg-gray-200'
    }
}
</script>

<style scoped>
.min-h-unset {
    min-height: unset;
    height: unset;
}
</style>
