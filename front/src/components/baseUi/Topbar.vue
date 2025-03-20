<template>
    <!-- Desktop -->
    <div v-if="!isMobile" class="flex items-center justify-end h-12 px-4 bg-white">
        <!-- PARA DEBUGGING  -->
        <!--<div class="flex items-center mr-24 bg-blue-500 gap-x-4">
			<select name="role" id="role" class="bg-red-500" @change="updateRole">
				<option value="admin">Administrador</option>
				<option value="superadmin">Superadmin</option>
				<option value="clinica">Clinica</option>
				<option value="medico">Médico</option>
				<option value="recepcionista">Recepcionista</option>
				<option value="paciente">Paciente</option>
			</select>
		</div>-->
        <RouterLink :to="{ name: 'perfil_medico' }" class="">
            <div @click="goToProfile" class="flex items-center cursor-pointer gap-x-4">
                <img
                    src="../../assets/placeholder.png"
                    class="w-10 h-10 rounded-full"
                    alt=""
                    sizes=""
                    srcset="" />
                <p class="font-bold">Olá, {{ name }}</p>
            </div>
        </RouterLink>
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

<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { useScreenSize } from '@/composables/useScreenSize'
import { Menu } from 'lucide-vue-next'
import { useUIStore } from '@/stores/ui/useUIStore'
import { useUserStore } from '@/stores/user/useUserStore'
import { useRouter } from 'vue-router'
import { RouterLink } from 'vue-router'
import { ref, onMounted } from 'vue'

const router = useRouter()
const { isMobile } = useScreenSize()
const { toggleLeftbar } = useUIStore()

const userStore = useUserStore()
const { role, name } = storeToRefs(userStore)

interface Profile {
    role: 'ADMIN' | 'DOCTOR' | 'PATIENT' | 'RECEPTIONIST'
    nameRoute: string
}

// TODO: escrever de para para rotas de perfil para cada tipo de usuário
const profile: Profile[] = [
    { role: 'ADMIN', nameRoute: 'perfil_administrador' },
    { role: 'DOCTOR', nameRoute: 'perfil_medico' },
    { role: 'PATIENT', nameRoute: 'perfil_paciente' }
]

const getProfileRoute = () => {
    const profileRoute = profile.find((p) => p.role === role.value)
    return profileRoute ? profileRoute.nameRoute : 'perfil_paciente'
}

const goToProfile = () => {
    router.push(getProfileRoute())
}

//const updateRole = (event) => {
//	// setRole(event.target.value)
//	const newRole = event.target.value
//	setRole(newRole)
//	localStorage.setItem('role', newRole)
//}
</script>
