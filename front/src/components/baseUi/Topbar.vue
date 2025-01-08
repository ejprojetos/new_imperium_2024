<template>
    <!-- Desktop -->
    <div v-if="!isMobile" class="flex items-center justify-end h-12 px-4 bg-white">
        <!-- PARA DEBUGGING  -->
        <div class="flex items-center mr-24 bg-blue-500 gap-x-4">
            <select name="role" id="role" class="bg-red-500" @change="updateRole">
                <option value="admin">Administrador</option>
                <option value="superadmin">Superadmin</option>
                <option value="clinica">Clinica</option>
                <option value="medico">Médico</option>
                <option value="recepcionista">Recepcionista</option>
                <option value="paciente">Paciente</option>
            </select>
        </div>
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

<script setup>
import { storeToRefs } from 'pinia'
import { useScreenSize } from '@/composables/useScreenSize'
import { Menu } from 'lucide-vue-next'
import { useUIStore } from '@/stores/ui/useUIStore'
import { useUserStore } from '@/stores/user/useUserStore'
import { useRoute } from 'vue-router'
import { RouterLink } from 'vue-router'
import { ref, onMounted } from 'vue'


const { isMobile } = useScreenSize()
const { toggleLeftbar } = useUIStore()

const userStore = useUserStore()
const { setRole } = userStore
const { role, name } = storeToRefs(userStore)

// TODO: escrever de para para rotas de perfil para cada tipo de usuário
const profile = [
    { name: 'admin', nameRoute: 'perfil_administrador' },
    { name: 'clinica', nameRoute: 'perfil_clinica' },
    { name: 'paciente', nameRoute: 'perfip_paciente' },
    { name: 'medico', nameRoute: 'perfil_medico' }
]

const getProfileRoute = () => {
    const profileRoute = profile.find((p) => p.name === role.value)
    return profileRoute ? profileRoute.nameRoute : 'perfil_paciente'
    //return profile.find((p) => p.name === role.value).nameRoute
    //return 'perfil_paciente'
}

const updateRole = (event) => {
    // setRole(event.target.value)
    const newRole = event.target.value
    setRole(newRole)
    localStorage.setItem('role', newRole)
}

onMounted(() =>{
    const storedRole = localStorage.getItem('role')
    if(storedRole){
        setRole(storedRole)
    }else{
        setRole('paciente')
    }
})

</script>
