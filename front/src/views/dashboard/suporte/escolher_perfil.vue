<template>
    <LayoutDashboard>
        <div class="container mx-auto px-4 py-8">
            <h1 class="text-2xl font-bold text-center text-blue-900 mb-12">Escolha o perfil</h1>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 max-w-4xl mx-auto">
                <RouterLink to="/dashboard/suporte/administrador" class="profile-card">
                    <div class="flex flex-col items-center p-6" @click="emitPerfil('ADMIN')">
                        <img :src="administradorIcon" alt="Administrador" class="w-20 h-20 mb-4" />
                        <span class="text-lg font-medium">Administrador</span>
                    </div>
                </RouterLink>

                <RouterLink to="/dashboard/suporte/administrador" class="profile-card">
                    <div class="flex flex-col items-center p-6" @click="emitPerfil('PATIENT')">
                        <img :src="pacienteIcon" alt="Paciente" class="w-20 h-20 mb-4" />
                        <span class="text-lg font-medium">Paciente</span>
                    </div>
                </RouterLink>

                <RouterLink to="/dashboard/suporte/administrador" class="profile-card">
                    <div class="flex flex-col items-center p-6" @click="emitPerfil('CLINIC')">
                        <img :src="clinicaIcon" alt="Clínica" class="w-20 h-20 mb-4" />
                        <span class="text-lg font-medium">Clínica</span>
                    </div>
                </RouterLink>

                <RouterLink to="/dashboard/suporte/administrador" class="profile-card">
                    <div class="flex flex-col items-center p-6" @click="emitPerfil('DOCTOR')">
                        <img :src="medicoIcon" alt="Médico" class="w-20 h-20 mb-4" />
                        <span class="text-lg font-medium">Médico</span>
                    </div>
                </RouterLink>

                <RouterLink to="/dashboard/suporte/administrador" class="profile-card">
                <div class="flex flex-col items-center p-6" @click="emitPerfil('RECEPTIONIST')">
                        <img :src="recepcionistaIcon" alt="Recepcionista" class="w-20 h-20 mb-4" />
                        <span class="text-lg font-medium">Recepcionista</span>
                    </div>
                </RouterLink>
            </div>

            <div class="flex justify-end mt-12">
                <img :src="imperiumLogo" alt="Imperium Logo" class="w-32" />
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'

import administradorIcon from '@/assets/icons/administrador.png'
import pacienteIcon from '@/assets/icons/pacientes.svg'
import clinicaIcon from '@/assets/icons/clinicas.svg'
import medicoIcon from '@/assets/icons/institucional.svg'
import recepcionistaIcon from '@/assets/icons/recepcionistas.svg'
import imperiumLogo from '@/assets/logo.svg'


import { perfilSelecionado } from '@/stores/ajuda/perfilStore'


function emitPerfil(perfil: string) {
    console.log(perfil)
    perfilSelecionado.value = perfil
}

</script>

<style scoped>
.profile-card {
    @apply bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 cursor-pointer;
}

.profile-card:hover {
    @apply transform scale-105 transition-transform duration-200;
}
</style>
