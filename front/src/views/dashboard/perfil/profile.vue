<script setup lang="ts">
import { useUserStore } from '@/stores/user/useUserStore'
import AdminProfile from './admin-profile/admin-profile.vue'
import DoctorProfile from './doctor-profile/doctor-profile.vue'
import ReceptionistProfile from './receptionist-profile/receptionist-profile.vue'
import { storeToRefs } from 'pinia'
import { useQuery } from '@tanstack/vue-query'
import type { User } from '@/types/users.types'
import { fetcher } from '@/services/fetcher.service'

const userStore = useUserStore()
const { id } = storeToRefs(userStore)

const { data } = useQuery<User, Error>({
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
    <DoctorProfile v-if="data?.roles[0].name === 'DOCTOR'" />
    <ReceptionistProfile v-if="data?.roles[0].name === 'RECEPTIONIST'" />
    <AdminProfile v-if="data?.roles[0].name === 'ADMIN'" />
</template>
