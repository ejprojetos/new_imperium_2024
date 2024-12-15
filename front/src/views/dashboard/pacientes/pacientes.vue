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
                    <button class="w-full py-2 text-xs text-white btn bg-primary hover:bg-primary">
                        Cadastrar
                    </button>
                </RouterLink>
            </div>
            <div class="p-4 bg-white rounded-lg shadow-lg min-w-56">
                <h3 class="mb-8 text-xl font-bold">Cadastrar Pacientes</h3>
                <RouterLink to="/dashboard/pacientes/cadastrar">
                    <button class="w-full py-2 text-xs text-white btn bg-primary hover:bg-primary">
                        Cadastrar
                    </button>
                </RouterLink>
            </div>
        </div>

        <!-- filtros -->
        <div class="flex items-center px-12 mt-8 gap-x-4">
            <span class="font-bold">Pacientes</span>
            <button class="px-4 py-2 text-white bg-blue-700 rounded-full">Hoje</button>
            <select class="px-4 py-2 bg-white rounded-full">
                <option>Cidade</option>
            </select>
            <select class="px-4 py-2 bg-white rounded-full">
                <option>Bairro</option>
            </select>
            <input type="text" class="px-4 py-2 bg-white rounded-full" placeholder="CPF" />
            <input type="text" class="px-4 py-2 bg-white rounded-full" placeholder="Nome" />
            <button class="p-2 bg-white rounded-full">
                <Search />
            </button>
        </div>

        <!-- pacientes -->
        <div v-if="patients.length" class="grid grid-cols-3 gap-4 px-12 mt-8">
            <div v-for="patient in patients" :key="patient.id" class="flex flex-col p-4 bg-white rounded-lg shadow">
                <div class="flex items-center mb-4">
                    <img :src="patient.image" alt="Paciente" class="w-16 h-16 mr-4 rounded-full" />
                    <div>
                        <h4 class="font-bold">{{ patient.name }}</h4>
                        <p class="text-sm">CPF: {{ patient.cpf }}</p>
                        <p class="text-sm">{{ patient.address }}</p>
                    </div>
                </div>
                <div class="flex items-center mb-2">
                    <Phone class="w-5 h-5 mr-2 text-blue-700" />
                    <p class="text-sm">{{ patient.phone }}</p>
                </div>
                <div class="flex justify-between mt-2">
                    <div class="p-4 mb-2 bg-blue-100 rounded-lg shadow-lg">
                        <p class="text-sm font-bold">Próxima Consulta:</p>
                        <p class="text-sm">Data: {{ patient.nextAppointment.date }}</p>
                        <p class="text-sm">Hora: {{ patient.nextAppointment.time }}</p>
                        <p class="text-sm">{{ patient.nextAppointment.doctor }}</p>
                    </div>
                    <div class="p-4 mb-2 bg-blue-100 rounded-lg shadow-lg">
                        <p class="text-sm font-bold">Última Consulta:</p>
                        <p class="text-sm">Data: {{ patient.lastAppointment.date }}</p>
                        <p class="text-sm">Hora: {{ patient.lastAppointment.time }}</p>
                        <p class="text-sm">{{ patient.lastAppointment.doctor }}</p>
                    </div>
                </div>
                <RouterLink
                    :to="`/dashboard/pacientes/${patient.id}`"
                    class="w-full px-4 py-2 mt-4 text-white bg-blue-700 rounded-lg">
                    Ver Perfil
                </RouterLink>
            </div>
        </div>

        <div v-else class="mt-12">
            <div class="flex flex-col items-center justify-center w-full">
                <!-- <img src="../../../src/assets/empty-list.svg" alt="Empty List" class="w-40" />
                    <p class="text-sm text-gray-500">Nenhum paciente encontrado</p> -->

                <img src="../../../assets/pacientes404.svg" alt="Pacientes" class="w-64" />
                <h2>Paciente não encontrado</h2>
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
import { ref } from 'vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { Search, Phone } from 'lucide-vue-next'

const patients = ref([
    {
        id: 1,
        name: 'Maria Luiza Gomes Bastos',
        cpf: '000.000.000-00',
        address: 'Endereço: Av. dos Pinheirais, 12, Neópolis - Natal/RN. 59080-150',
        phone: '(00) 00000-0000',
        nextAppointment: { date: '20/02/20', time: '14h00min', doctor: 'Dra. Rafaela V.' },
        lastAppointment: { date: '20/11/19', time: '14h00min', doctor: 'Dra. Rafaela V.' },
        image: '/path/to/image.jpg'
    }
])
</script>
