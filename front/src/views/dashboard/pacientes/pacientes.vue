<template>
    <LayoutDashboard>
        <!-- cards -->
        <div class="flex gap-4 px-12 mt-12">
            <div class="p-4 bg-blue-100 rounded-lg shadow-lg min-w-56">
                <h3 class="text-3xl font-bold">60</h3>
                <p class="mt-2">Consultas</p>
                <p class="font-bold">Hoje</p>
            </div>
            <div class="p-4 bg-red-100 rounded-lg shadow-lg min-w-56">
                <h3 class="text-3xl font-bold">2</h3>
                <p class="mt-2">Consultas Atrasadas</p>
                <p class="font-bold">Hoje</p>
            </div>
            <div class="p-4 bg-green-100 rounded-lg shadow-lg min-w-56">
                <h3 class="mb-8 text-xl font-bold">Cadastrar Consultas</h3>
                <RouterLink to="/dashboard/pacientes/cadastrar-consulta">
                    <button class="py-2 w-full text-xs text-white btn bg-primary hover:bg-primary">
                        Cadastrar
                    </button>
                </RouterLink>
            </div>
            <div class="p-4 bg-white rounded-lg shadow-lg min-w-56">
                <h3 class="mb-8 text-xl font-bold">Cadastrar Pacientes</h3>
                <RouterLink to="/dashboard/pacientes/cadastrar">
                    <button class="py-2 w-full text-xs text-white btn bg-primary hover:bg-primary">
                        Cadastrar
                    </button>
                </RouterLink>
            </div>
        </div>

        <!-- filtros -->
        <div class="flex gap-x-4 items-center px-12 mt-8">
            <span class="font-bold">Pacientes</span>
            <button class="px-4 py-2 text-white bg-blue-700 rounded-full">Hoje</button>
            <select class="px-4 py-2 bg-white rounded-full">
                <option>Cidade</option>
            </select>
            <select class="px-4 py-2 bg-white rounded-full">
                <option>Bairro</option>
            </select>
            <input
                type="text"
                v-model="searchCpf"
                class="px-4 py-2 bg-white rounded-full"
                placeholder="CPF" />
            <input
                type="text"
                v-model="searchName"
                class="px-4 py-2 bg-white rounded-full"
                placeholder="Nome" />
            <button class="p-2 bg-white rounded-full">
                <Search />
            </button>
        </div>

        <!-- pacientes -->
        <div class="grid grid-cols-3 gap-4 px-12 mt-8">
            <div v-if="userStore.loading" class="col-span-3 text-center">
                Carregando pacientes...
            </div>
            <div v-else-if="userStore.error" class="col-span-3 text-center text-red-600">
                {{ userStore.error }}
            </div>
            <div
                v-else
                v-for="patient in filteredPatients"
                :key="patient.id"
                class="flex flex-col p-4 bg-white rounded-lg shadow">
                <div class="flex items-center mb-4">
                    <img
                        :src="`src/assets/images/avatar.png`"
                        alt="Paciente"
                        class="mr-4 w-16 h-16 rounded-full" />
                    <div>
                        <h4 class="font-bold">{{ patient.first_name }} {{ patient.last_name }}</h4>
                        <p class="text-sm">CPF: {{ patient.cpf }}</p>
                        <p class="text-sm">{{ patient.endereco }}</p>
                    </div>
                </div>
                <div class="flex items-center mb-2">
                    <Phone class="mr-2 w-5 h-5 text-blue-700" />
                    <p class="text-sm">{{ patient.telefone }}</p>
                </div>
                <RouterLink
                    :to="`/dashboard/pacientes/${patient.id}`"
                    class="px-4 py-2 mt-4 w-full text-center text-white bg-blue-700 rounded-lg">
                    Ver Perfil
                </RouterLink>
            </div>
        </div>

        <div
            v-if="!filteredPatients.length && !userStore.loading && !userStore.error"
            class="mt-12">
            <div class="flex flex-col justify-center items-center w-full">
                <img src="../../../assets/pacientes404.svg" alt="Pacientes" class="w-64" />
                <h2>Nenhum paciente encontrado</h2>
            </div>
        </div>

        <!-- paginacao -->
        <div class="flex justify-center mt-8">
            <button class="px-3 py-1 mx-1 bg-gray-200 rounded-full">&lt;</button>
            <button class="px-3 py-1 mx-1 bg-gray-200 rounded-full">1</button>
            <button class="px-3 py-1 mx-1 bg-gray-200 rounded-full">2</button>
            <button class="px-3 py-1 mx-1 text-white bg-blue-700 rounded-full">3</button>
            <button class="px-3 py-1 mx-1 bg-gray-200 rounded-full">4</button>
            <button class="px-3 py-1 mx-1 bg-gray-200 rounded-full">5</button>
            <button class="px-3 py-1 mx-1 bg-gray-200 rounded-full">&gt;</button>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { Search, Phone } from 'lucide-vue-next'
import { useRoute } from 'vue-router'
import { useUserStore } from '@/stores/users/users.store'
import type { User } from '@/types/users.types'

const route = useRoute()
const userStore = useUserStore()

// referencia para armazenar os pacientes
const patients = ref<User[]>([])

// referencias para os campos de busca
const searchCpf = ref('')
const searchName = ref('')

// computed property para filtrar os pacientes
const filteredPatients = computed(() => {
    return patients.value.filter((patient) => {
        const matchCpf = patient.cpf.toLowerCase().includes(searchCpf.value.toLowerCase())
        const fullName = `${patient.first_name} ${patient.last_name}`.toLowerCase()
        const matchName = fullName.includes(searchName.value.toLowerCase())

        // retorna true se o cpf ou nome corresponderem à busca
        return (searchCpf.value === '' || matchCpf) && (searchName.value === '' || matchName)
    })
})

// busca os pacientes quando o componente é montado
onMounted(async () => {
    try {
        await userStore.fetchPatients()
        patients.value = userStore.patients
    } catch (error) {
        console.error('Erro ao carregar pacientes:', error)
    }
})
</script>
