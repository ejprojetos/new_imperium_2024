<template>
    <LayoutDashboard>
        <div
            class="flex gap-x-4 px-12 mt-12 max-lg:flex-col max-lg:items-start max-lg:gap-x-0 max-lg:w-full max-lg:gap-y-4 max-lg:mt-4">
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
                    <button
                        class="py-2 w-full text-xs text-white min-h-unset btn bg-primary hover:bg-primary">
                        Cadastrar
                    </button>
                </router-link>
            </div>
            <div class="p-4 bg-white rounded-lg shadow-lg min-w-56 max-lg:w-full">
                <h3 class="mb-8 text-xl font-bold">Pagamentos</h3>
                <button
                    class="py-2 w-full text-xs text-white min-h-unset btn bg-primary hover:bg-primary">
                    Acessar Asaas
                </button>
            </div>
        </div>

        <!-- Filter Tabs -->
        <div class="flex gap-x-4 items-center px-12 mt-8">
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

        <div class="px-12 mt-8">
            <div v-if="isLoading" class="text-center">Carregando consultas...</div>
            <div v-else-if="error" class="text-center text-red-600">
                {{ error.message }}
            </div>
            <div
                v-for="appointment in data?.results"
                :key="appointment.uuid"
                class="flex justify-between items-center p-4 mb-4 bg-white rounded-lg shadow">
                <div class="flex items-center space-x-4">
                    <div class="flex flex-col text-xs">
                        <span class="text-xs text-gray-600">
                            {{ new Date(appointment.appointment_date).toLocaleDateString() }}
                        </span>
                        <div class="text-lg font-bold">
                            {{
                                new Date(appointment.appointment_date).toLocaleTimeString([], {
                                    hour: '2-digit',
                                    minute: '2-digit'
                                })
                            }}
                        </div>
                    </div>
                    <div>
                        <div class="flex gap-x-2">
                            <div class="font-semibold">{{ appointment.patient_name }}</div>
                            <span
                                :class="statusClass(appointment.status)"
                                class="px-2 py-1 text-sm rounded-full">
                                {{ appointment.status }}
                            </span>
                        </div>
                        <div class="text-sm text-gray-600">{{ appointment.doctor_name }}</div>
                        <div class="text-sm text-gray-600">Sala: {{ appointment.room }}</div>
                    </div>
                </div>
                <div class="flex items-center space-x-2">
                    <button class="px-4 py-2 text-white bg-blue-700 rounded-lg">
                        Ver Prontuário
                    </button>
                    <RouterLink :to="`/dashboard/medicos/editar-consultas/${appointment.uuid}`">
                        <button class="px-4 py-2 text-blue-700 bg-blue-100 rounded-lg">
                            Editar
                        </button>
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
import { onMounted } from 'vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { Search } from 'lucide-vue-next'
import { RouterLink } from 'vue-router'
import { useQuery } from '@tanstack/vue-query'
import { appointmentService } from '@/services/appointments.service'

const { data, isLoading, error } = useQuery({
    queryKey: ['appointments'],
    queryFn: () => appointmentService.getAll()
})

const statusClass = (status: string) => {
    switch (status.toLowerCase()) {
        case 'scheduled':
            return 'text-green-800 bg-green-200'
        case 'canceled':
            return 'text-red-800 bg-red-200'
        case 'completed':
            return 'text-gray-800 bg-gray-200'
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
