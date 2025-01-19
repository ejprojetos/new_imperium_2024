import { defineStore } from 'pinia'
import { ref } from 'vue'
import { userService } from '@/services/users.service'
import type { User } from '@/types/users.types'

export const useUserStore = defineStore('user', () => {
    const doctors = ref<User[]>([])

    const fetchDoctors = async () => {
        try {
            doctors.value = await userService.getDoctors()
        } catch (error) {
            console.error('Error fetching doctors:', error)
        }
    }

    return {
        doctors,
        fetchDoctors
    }
})
