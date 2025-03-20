<template>
    <LayoutDashboard>
        <div class="container mx-auto px-4 py-8">
            <h1 class="text-2xl font-bold text-center text-blue-900 mb-12">Políticas</h1>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 max-w-4xl mx-auto">
                <!-- Administrador -->
                <div class="bg-white rounded-lg shadow-md p-6 flex flex-col items-center">
                    <img :src="administradorIcon" alt="Administrador" class="w-20 h-20 mb-4" />
                    <span class="text-lg font-medium mb-4">Administrador</span>

                    <RouterLink to="/dashboard/suporte/cadastrar-politicas">

                        <button
                            class="bg-blue-600 text-white px-6 py-1 rounded-full text-sm hover:bg-blue-600 transition-colors">
                            Editar
                        </button>
                    </RouterLink>
                </div>

                <!-- Paciente -->
                <div class="bg-white rounded-lg shadow-md p-6 flex flex-col items-center">
                    <img :src="pacienteIcon" alt="Paciente" class="w-20 h-20 mb-4" />
                    <span class="text-lg font-medium mb-4">Paciente</span>
                    <button
                        class="bg-blue-600 text-white px-6 py-1 rounded-full text-sm hover:bg-blue-600 transition-colors">
                        Editar
                    </button>
                </div>

                <!-- Clínica -->
                <div class="bg-white rounded-lg shadow-md p-6 flex flex-col items-center">
                    <img :src="clinicaIcon" alt="Clínica" class="w-20 h-20 mb-4" />
                    <span class="text-lg font-medium mb-4">Clínica</span>
                    <button
                        class="bg-blue-600 text-white px-6 py-1 rounded-full text-sm hover:bg-blue-600 transition-colors">
                        Editar
                    </button>
                </div>

                <!-- Médico -->
                <div class="bg-white rounded-lg shadow-md p-6 flex flex-col items-center">
                    <img :src="medicoIcon" alt="Médico" class="w-20 h-20 mb-4" />
                    <span class="text-lg font-medium mb-4">Médico</span>
                    <button
                        class="bg-blue-600 text-white px-6 py-1 rounded-full text-sm hover:bg-blue-600 transition-colors">
                        Editar
                    </button>
                </div>

                <!-- Recepcionista -->
                <div class="bg-white rounded-lg shadow-md p-6 flex flex-col items-center">
                    <img :src="recepcionistaIcon" alt="Recepcionista" class="w-20 h-20 mb-4" />
                    <span class="text-lg font-medium mb-4">Recepcionista</span>
                    <button
                        class="bg-blue-600 text-white px-6 py-1 rounded-full text-sm hover:bg-blue-600 transition-colors">
                        Editar
                    </button>
                </div>
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'

import administradorIcon from '@/assets/icons/principal.svg'
import pacienteIcon from '@/assets/icons/pacientes.svg'
import clinicaIcon from '@/assets/icons/clinicas.svg'
import medicoIcon from '@/assets/icons/institucional.svg'
import recepcionistaIcon from '@/assets/icons/recepcionistas.svg'
</script>

<style scoped>
.bg-white {
    @apply transition-all duration-200;
}

.bg-white:hover {
    @apply shadow-lg;
}
</style>
