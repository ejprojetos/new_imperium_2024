<template>
    <!-- Desktop -->
    <div v-if="!isMobile" class="flex items-center justify-end h-12 px-4 bg-white">
        <!-- PARA DEBUGGING  -->
        <div class="flex items-center mr-24 bg-blue-500 gap-x-4">
            <select name="role" id="role" class="bg-red-500" @change="updateRole">
                <option value="admin">Administrador</option>
                <option value="superadmin">Superadmin</option>
                <option value="medico">Médico</option>
                <option value="recepcionista">Recepcionista</option>
                <option value="paciente">Paciente</option>
            </select>
        </div>
        <p class="font-bold">Olá, {{ name }}</p>
    </div>

    <!-- Mobile -->
    <div
        v-else
        class="flex items-center justify-between h-12 px-4 bg-white border-b border-gray-200">
        <div class="flex items-center gap-x-4">
            <Menu @click="toggleLeftbar" />
            <p class="font-bold">Olá, {{ name }}</p>
        </div>
        topbar mobile
    </div>
</template>

<script setup>
import { storeToRefs } from 'pinia'
import { useScreenSize } from '@/composables/useScreenSize'
import { Menu } from 'lucide-vue-next'
import { useUIStore } from '@/stores/ui/useUIStore'
import { useUserStore } from '@/stores/user/useUserStore'

const { isMobile } = useScreenSize()
const { toggleLeftbar } = useUIStore()

const userStore = useUserStore()
const { setRole } = userStore
const { role, name } = storeToRefs(userStore)

const updateRole = (event) => {
    setRole(event.target.value)
}
</script>
