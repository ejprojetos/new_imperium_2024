<template>
    <Transition name="slide">
        <div
            v-if="isLeftbarOpen || !isMobile"
            :class="[
                isMobile ? 'fixed bg-white top-0 left-0 z-50 w-[200px] shadow-lg' : '',
                'px-4 py-4'
            ]"
            class="flex flex-col w-[250px] px-4 py-8 items-center justify-between h-full max-lg:px-4 max-lg:items-start">
            <img class="w-32" src="../../assets/logo.svg" alt="" srcset="" />
            <div class="flex flex-col mt-12">
                <RouterLink v-for="item in navItems" :key="item.name" :to="item.path">
                    <div
                        v-if="item.roles.includes(role)"
                        class="flex items-center justify-start mt-4 mb-2 text-sm gap-x-4">
                        <img :src="item.icon" alt="" />
                        <p
                            :class="{ 'text-active': isActive(item.path) }"
                            class="font-bold text-md">
                            {{ item.name }}
                        </p>
                    </div>
                </RouterLink>
            </div>

            <!-- notificacoes -->
            <div class="flex flex-col mt-12 gap-y-1">
                <div class="flex flex-col p-4 bg-blue-200 shadow-lg rounded-2xl">
                    <div class="self-end">
                        <p class="text-xs">Seg 19:30</p>
                    </div>
                    <div class="flex items-start gap-x-2">
                        <Bell fill="#054088" stroke="#054088" class="w-12" />
                        <p class="text-sm">Solicitação aceita pelo paciente.</p>
                    </div>
                </div>
            </div>

            <!-- ajuda (suporte, contatos, politicas) -->
            <div class="flex flex-col items-start w-full">
                <p class="text-sm font-bold">Ajuda</p>
                <RouterLink class="text-sm" to="/suporte">Suporte</RouterLink>
                <RouterLink class="text-sm" to="/contatos">Contatos</RouterLink>
                <RouterLink class="text-sm" to="/politicas">Políticas</RouterLink>
            </div>
        </div>
    </Transition>
    <div
        v-if="isMobile && isLeftbarOpen"
        class="fixed inset-0 z-40 bg-black bg-opacity-50"
        @click="closeLeftbar"></div>
</template>

<script setup lang="ts">
import principalIcon from '@/assets/icons/principal.svg'
import institucionalIcon from '@/assets/icons/institucional.svg'
import clinicasIcon from '@/assets/icons/clinicas.svg'
import emailIcon from '@/assets/icons/email.svg'
import recepcionistasIcon from '@/assets/icons/recepcionistas.svg'
import pacientesIcon from '@/assets/icons/pacientes.svg'
import minhasConsultasIcon from '@/assets/icons/minhas-consultas.svg'

import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { Bell } from 'lucide-vue-next'
import { storeToRefs } from 'pinia'
import { useUIStore } from '@/stores/ui/useUIStore'
import { useUserStore } from '@/stores/user/useUserStore'
import { useScreenSize } from '@/composables/useScreenSize'

const userStore = useUserStore()
const { role, name } = storeToRefs(userStore)

const uiStore = useUIStore()

const route = useRoute()
const { isLeftbarOpen } = storeToRefs(uiStore)
const { isMobile } = useScreenSize()

const isActive = (path: string) => computed(() => route.path === path).value

const closeLeftbar = () => {
    uiStore.toggleLeftbar()
}

const expandLeftbar = () => {
    if (isLeftbarOpen.value) {
        uiStore.toggleLeftbar()
    }
}

const navItems = [
    {
        name: 'Principal',
        icon: principalIcon,
        path: '/dashboard',
        roles: ['admin', 'superadmin', 'paciente']
    },
    {
        name: 'Institucional',
        icon: institucionalIcon,
        path: '/dashboard/institucional',
        roles: ['admin', 'superadmin', 'paciente']
    },
    {
        name: 'Clinicas',
        icon: clinicasIcon,
        path: '/dashboard/clinicas',
        roles: ['admin', 'superadmin', 'paciente']
    },
    {
        name: 'Emails',
        icon: emailIcon,
        path: '/dashboard/emails',
        roles: ['admin', 'superadmin', 'paciente']
    },
    {
        name: 'Médicos',
        icon: clinicasIcon,
        path: '/dashboard/medicos',
        roles: ['admin', 'superadmin', 'recepcionista', 'paciente']
    },
    {
        name: 'Consultas',
        icon: principalIcon,
        path: '/dashboard/consultas',
        roles: ['admin', 'superadmin', 'medico', 'recepcionista']
    },
    {
        name: 'Recepcionistas',
        icon: recepcionistasIcon,
        path: '/dashboard/recepcionistas',
        roles: ['admin', 'superadmin', 'medico', 'paciente']
    },
    {
        name: 'Pacientes',
        icon: pacientesIcon,
        path: '/dashboard/pacientes',
        roles: ['admin', 'superadmin', 'medico', 'recepcionista', 'paciente']
    }
    //{
    //    name: 'Minhas Consultas',
    //    icon: minhasConsultasIcon,
    //    path: '/dashboard/minhas-consultas'
    //}
]
</script>

<style scoped>
.text-active {
    color: #ed5575; /* Color for active item name */
}

.slide-enter-active,
.slide-leave-active {
    transition: transform 0.3s ease;
}

.slide-enter-from,
.slide-leave-to {
    transform: translateX(-100%);
}

.leftbar-container.leftbar-closed .menu :where(li > details > summary):after,
.leftbar-container.leftbar-closed
    .menu
    :where(li > .menu-dropdown-toggle.menu-dropdown-show):after {
    display: none !important;
}

.menu :where(li:not(.menu-title) > *:not(ul, details, .menu-title, .btn)),
.menu :where(li:not(.menu-title) > details > summary:not(.menu-title)) {
    padding-left: 0.2rem;
    padding-right: 0.2rem;
}

.menu li > *:not(ul, .menu-title, details, .btn):active,
.menu li > *:not(ul, .menu-title, details, .btn).active,
.menu li > details > summary:active {
    background-color: unset;
    color: unset;
}

.sidebar-slide-fade-enter-active,
.sidebar-slide-fade-leave-active {
    transition:
        opacity 0.2s cubic-bezier(0.68, -0.55, 0.27, 1.55),
        transform 0.2s cubic-bezier(0.68, -0.55, 0.27, 1.55);
}

.sidebar-slide-fade-enter-from,
.sidebar-slide-fade-leave-to {
    opacity: 0;
    transform: translateX(20px);
}

.sidebar-slide-fade-leave-from,
.sidebar-slide-fade-enter-to {
    opacity: 1;
    transform: translateX(0);
}

.menu {
    padding: 0;
}

.menu :where(li:not(.menu-title) > *:not(ul, details, .menu-title, .btn)),
.menu :where(li:not(.menu-title) > details > summary:not(.menu-title)) {
    padding: 6px 8px;
}

.menu-link {
    color: #334155;
}

.link-transition {
    transition: all 0.1s ease-in-out;
}

.link-transition:focus {
    background-color: unset !important;
}

.active-link {
    background-color: #d6e3ff;
}

.router_link:hover {
    background-color: #f0f0f0;
}
</style>
