<template>
    <LayoutDashboard>
        <div class="container mx-auto px-4 py-8">
            <h1 class="text-2xl font-bold text-center text-blue-900 mb-12">Políticas do usuário</h1>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 gap-6 max-w-4xl mx-auto">
                <!-- Administrador -->

                <!-- Paciente -->
                <RouterLink to="/dashboard/politicas/politicas-usuario-pag">
                    <div class="bg-white rounded-lg shadow-md p-6 flex flex-col items-center">
                        <img :src="pacienteIcon" alt="Paciente" class="w-20 h-20 mb-4" />
                        <span class="text-lg font-medium mb-4">Paciente</span>
                    </div>    
                </RouterLink>

                <!-- Clínica -->
                <div class="bg-white rounded-lg shadow-md p-6 flex flex-col items-center">
                    <img :src="clinicaIcon" alt="Clínica" class="w-20 h-20 mb-4" />
                    <span class="text-lg font-medium mb-4">Clínica</span>
                </div>

                <!-- Médico -->
                <div class="bg-white rounded-lg shadow-md p-6 flex flex-col items-center">
                    <img :src="medicoIcon" alt="Médico" class="w-20 h-20 mb-4" />
                    <span class="text-lg font-medium mb-4">Médico</span>
                </div>

                <!-- Recepcionista -->
                <div class="bg-white rounded-lg shadow-md p-6 flex flex-col items-center">
                    <img :src="recepcionistaIcon" alt="Recepcionista" class="w-20 h-20 mb-4" />
                    <span class="text-lg font-medium mb-4">Recepcionista</span>
                </div>
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'

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
