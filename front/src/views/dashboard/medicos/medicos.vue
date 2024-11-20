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
                    <button class="w-full py-2 text-xs text-white btn bg-primary hover:bg-primary">
                        Cadastrar
                    </button>
                </RouterLink>

            </div>
            <div class="p-4 bg-white rounded-lg shadow-lg min-w-56">
                <h3 class="mb-8 text-xl font-bold">Cadastrar Médicos</h3>
                <RouterLink to="/dashboard/medicos/cadastrar">
                    <button class="w-full py-2 text-xs text-white btn bg-primary hover:bg-primary">
                        Cadastrar
                    </button>
                </RouterLink>
            </div>
        </div>

        <!-- Filter Tabs -->
        <div class="flex items-center px-12 mt-8 gap-x-4">
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
            <input type="text" class="px-4 py-2 bg-gray-200 rounded-full" placeholder="Buscar" />
            <button class="p-2 bg-gray-200 rounded-full">
                <Search />
            </button>
        </div>

        <!-- Receptionists Grid -->
        <div class="grid grid-cols-4 gap-4 px-12 mt-8">
            <div v-for="receptionist in receptionists" :key="receptionist.id"
                class="flex flex-col items-center p-4 bg-white rounded-lg shadow">
                <img :src="receptionist.image" alt="Recepcionista" class="w-24 h-24 mx-auto rounded-full" />
                <h4 class="mt-2 font-bold text-center">{{ receptionist.name }}</h4>
                <p class="text-sm text-center">Atendimento: {{ receptionist.schedule }}</p>
                <p class="text-sm text-center">Turno: {{ receptionist.shift }}</p>
                <div class="flex mt-2 gap-x-2">
                    <Mail class="w-6 h-6 mx-auto text-blue-700" />
                    <p class="text-sm text-center">{{ receptionist.email }}</p>
                </div>
                <div class="flex gap-x-2">
                    <Phone class="w-6 h-6 mx-auto text-blue-700" />
                    <p class="text-sm text-center">{{ receptionist.phone }}</p>
                </div>
                <RouterLink
                    :to="`/dashboard/medicos/${receptionist.id}`"
                    class="w-full px-4 py-2 mt-2 text-center text-white bg-blue-700 rounded-lg">
                    Ver Perfil
                </RouterLink>
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { Search, Mail, Phone } from 'lucide-vue-next'
import { useRoute } from 'vue-router'

const route = useRoute()

import { RouterLink } from 'vue-router'

const receptionists = ref([
    {
        id: 1,
        name: 'Rafaela Veríssimo',
        schedule: '2ª a 5ª',
        shift: 'Manhã e Tarde',
        email: 'rafaelaverissimo@gmail.com',
        phone: '(00) 00000-0000',
        image: '/path/to/image.jpg'
    }
    // Add more receptionists here...
])

const cadastro_consultas = {
    name: 'Cadastro de Consultas',
    path: '/dashboard/medicos/cadastrar-consultas',
    roles: ['medico']
}

</script>
