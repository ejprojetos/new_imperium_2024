<script setup lang="ts">
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { Search, Mail, Phone, Loader } from 'lucide-vue-next'

import type { Doctor } from '@/types/users.types'
import { fetcher } from '@/services/fetcher.service'
import { useQuery } from '@tanstack/vue-query'
import { ref } from 'vue'

const { data, isLoading, error } = useQuery({
    queryKey: ['doctors'],
    queryFn: async () => await fetcher<Doctor[]>(`/users/users_doctors`),
    staleTime: 5 * 1000
})

// referencias para os campos de busca
const searchCrm = ref('')
const searchName = ref('')

const cadastro_consultas = {
    name: 'Cadastro de Consultas',
    path: '/dashboard/medicos/cadastrar-consultas',
    roles: ['medico']
}
</script>

<template>
    <LayoutDashboard>
        <!-- Summary Cards -->
        <div class="flex gap-4 px-12 mt-12">
            <div class="p-4 bg-blue-100 rounded-lg shadow-lg min-w-56">
                <h3 class="text-3xl font-bold">10</h3>
                <p class="mt-2">Recepcionistas</p>
                <p class="font-bold">Hoje</p>
            </div>
            <div class="p-4 bg-yellow-100 rounded-lg shadow-lg min-w-56">
                <h3 class="text-3xl font-bold">3</h3>
                <p class="mt-2">Plantão hoje</p>
                <!-- Add small circular images here -->
            </div>
            <div class="p-4 bg-green-100 rounded-lg shadow-lg min-w-56">
                <h3 class="mb-8 text-xl font-bold">Cadastrar Consultas</h3>

                <RouterLink :to="cadastro_consultas.path">
                    <button class="py-2 w-full text-xs text-white btn bg-primary hover:bg-primary">
                        Cadastrar
                    </button>
                </RouterLink>
            </div>
            <div class="p-4 bg-white rounded-lg shadow-lg min-w-56">
                <h3 class="mb-8 text-xl font-bold">Cadastrar Médicos</h3>
                <RouterLink to="/dashboard/medicos/cadastrar">
                    <button class="py-2 w-full text-xs text-white btn bg-primary hover:bg-primary">
                        Cadastrar
                    </button>
                </RouterLink>
            </div>
        </div>

        <!-- Filter Tabs -->
        <div class="flex gap-x-4 items-center px-12 mt-8">
            <span class="font-bold">Médicos</span>
            <button class="px-4 py-2 text-white bg-blue-700 rounded-full">Hoje</button>
            <select class="px-4 py-2 bg-gray-200 rounded-full">
                <option>Dias da semana</option>
            </select>
            <select class="px-4 py-2 bg-gray-200 rounded-full">
                <option>Médico</option>
            </select>
            <select class="px-4 py-2 bg-gray-200 rounded-full">
                <option>Turno</option>
            </select>
            <input
                type="text"
                v-model="searchCrm"
                class="px-4 py-2 bg-gray-200 rounded-full"
                placeholder="CRM" />
            <input
                type="text"
                v-model="searchName"
                class="px-4 py-2 bg-gray-200 rounded-full"
                placeholder="Nome" />
            <button class="p-2 bg-gray-200 rounded-full">
                <Search />
            </button>
        </div>

        <!-- Doctors Grid -->
        <div class="grid grid-cols-4 gap-4 px-12 mt-8 w-full">
            <div
                v-if="isLoading"
                class="col-span-full flex-1 min-h-36 flex justify-center items-center h-full">
                <Loader class="animate-spin text-gray-400" />
            </div>
            <div v-else-if="error" class="col-span-4 text-center text-red-600">
                {{ error?.message }}
            </div>
            <div
                v-else
                v-for="doctor in data"
                :key="doctor.id"
                class="flex flex-col items-center p-4 bg-white rounded-lg shadow">
                <img
                    :src="`src/assets/images/avatar.png`"
                    alt="Médico"
                    class="mx-auto w-24 h-24 rounded-full" />
                <h4 class="mt-2 font-bold text-center">
                    {{ doctor.first_name }} {{ doctor.last_name }}
                </h4>
                <p class="text-sm text-center">CRM: {{ doctor.crm }}</p>
                <p class="text-sm text-center">Formação: {{ doctor.formacao }}</p>
                <div class="flex gap-x-2 mt-2">
                    <Mail class="mx-auto w-6 h-6 text-blue-700" />
                    <p class="text-sm text-center">{{ doctor.email }}</p>
                </div>
                <RouterLink
                    :to="`/dashboard/medicos/${doctor.id}`"
                    class="px-4 py-2 mt-2 w-full text-center text-white bg-blue-700 rounded-lg">
                    Ver Perfil
                </RouterLink>
            </div>
        </div>

        <!-- mensagem quando nao ha resultados -->
        <!-- <div
            v-if="!filteredDoctors.length && !userStore.loading && !userStore.error"
            class="flex flex-col justify-center items-center mt-12 w-full">
            <img src="../../../assets/pacientes404.svg" alt="Médicos" class="w-64" />
            <h2>Nenhum médico encontrado</h2>
        </div> -->
    </LayoutDashboard>
</template>
