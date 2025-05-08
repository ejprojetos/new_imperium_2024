<template>
    <LayoutDashboard>
        <div class="container mx-auto px-4 py-8">
            <h1 class="text-2xl font-bold text-center text-blue-900 mb-12">
                Suporte ao {{ perfil }}
            </h1>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-8 max-w-4xl mx-auto">
                <div class="bg-white rounded-lg shadow-md p-6 flex flex-col items-center">
                    <h2 class="text-2xl font-semibold text-blue-900 mb-6">Manuais</h2>
                    <RouterLink
                        to="/dashboard/suporte/todos-manuais"
                        class="bg-blue-600 text-white px-8 py-2 rounded-full hover:bg-blue-700 transition-colors">
                        Ver
                    </RouterLink>
                </div>

                <div class="bg-white rounded-lg shadow-md p-6 flex flex-col items-center">
                    <h2 class="text-2xl font-semibold text-blue-900 mb-6">FAQ</h2>
                    <RouterLink
                        to="/dashboard/suporte/faq"
                        class="bg-blue-600 text-white px-8 py-2 rounded-full hover:bg-blue-700 transition-colors">
                        Ver
                    </RouterLink>
                </div>
            </div>

            <div class="mt-12">
                <h2 class="text-xl font-semibold text-blue-900 mb-6 text-center">Recursos</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-8 max-w-4xl mx-auto">
                    <!-- Manual do usuário -->
                    <div
                        class="bg-white rounded-lg shadow-md p-6 flex items-center justify-between">
                        <div class="flex items-center">
                            <img :src="manualIcon" alt="Manual" class="w-12 h-12 mr-4" />
                            <span class="text-lg">Manual do usuário</span>
                        </div>
                        <RouterLink
                            to="/dashboard/suporte/manual-usuario"
                            class="bg-blue-600 text-white px-6 py-2 rounded-full hover:bg-blue-700 transition-colors">
                            Ver
                        </RouterLink>
                    </div>

                    <!-- Outros documentos -->
                    <div
                        class="bg-white rounded-lg shadow-md p-6 flex items-center justify-between">
                        <div class="flex items-center">
                            <img :src="documentIcon" alt="Documentos" class="w-12 h-12 mr-4" />
                            <span class="text-lg">Outros documentos</span>
                        </div>
                        <RouterLink
                            to="/dashboard/suporte/documentos"
                            class="bg-blue-600 text-white px-6 py-2 rounded-full hover:bg-blue-700 transition-colors">
                            Ver
                        </RouterLink>
                    </div>
                </div>
            </div>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'

// You'll need to create or import these icons
import manualIcon from '@/assets/icons/manual.png'
import documentIcon from '@/assets/icons/documentos.png'

import { perfilSelecionado } from '@/stores/ajuda/perfilStore'
import { computed } from 'vue'

const perfil = computed(() =>{
    switch(perfilSelecionado.value){
        case 'ADMIN':
            return 'Administrador'
        case 'PATIENT':
            return 'Paciente'
        case 'CLINIC':
            return 'Clínica'
        case 'DOCTOR':
            return 'Médico'
        case 'RECEPTIONIST':
            return 'Recepcionista'
        default:
            return 'Perfil não encontrado'
    }
})
</script>

<style scoped>
.bg-white {
    @apply transition-all duration-200;
}

.bg-white:hover {
    @apply shadow-lg;
}
</style>
