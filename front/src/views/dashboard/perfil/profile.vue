<script setup lang="ts">
import { useUserStore } from '@/stores/user/useUserStore'
import AdminProfile from './admin-profile/admin-profile.vue'
import DoctorProfile from './doctor-profile/doctor-profile.vue'
import ReceptionistProfile from './receptionist-profile/receptionist-profile.vue'
import PatientProfile from './patient-profile/patient-profile.vue'
import { storeToRefs } from 'pinia'
import { useQuery } from '@tanstack/vue-query'
import type { User } from '@/types/users.types'
import { fetcher } from '@/services/fetcher.service'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { Loader } from 'lucide-vue-next'

const userStore = useUserStore()
const { id } = storeToRefs(userStore)

const { data, isLoading } = useQuery<User, Error>({
    queryKey: ['user', id.value],
    queryFn: async () => {
        const response = await fetcher<User>(`/users/${id.value}`)
        if (!response) throw new Error('User not found')
        return response
    },
    staleTime: Infinity
})
</script>
<template>
    <LayoutDashboard>
        <div v-if="isLoading" class="flex justify-center items-center h-full">
            <Loader class="animate-spin text-zinc-400 size-4" />
        </div>
        <div v-else>
            <DoctorProfile v-if="data?.roles[0].name === 'DOCTOR'" />
            <ReceptionistProfile v-if="data?.roles[0].name === 'RECEPTIONIST'" />
            <AdminProfile v-if="data?.roles[0].name === 'ADMIN'" />
            <PatientProfile v-if="data?.roles[0].name === 'PATIENT'" />
        </div>
    </LayoutDashboard>
</template>
