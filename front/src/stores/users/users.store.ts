import { defineStore } from 'pinia'
import { ref } from 'vue'
import { userService } from '@/services/users.service'
import type { User } from '@/types/users.types'

export const useUserStore = defineStore('users', () => {
    const doctors = ref<User[]>([])
    const patients = ref<User[]>([])
    const loading = ref(false)
    const error = ref<string | null>(null)

    const fetchDoctors = async () => {
        try {
            loading.value = true
            doctors.value = await userService.getDoctors()
        } catch (error) {
            console.error('erro ao buscar médicos:', error)
            error.value = 'erro ao buscar médicos'
            throw error
        } finally {
            loading.value = false
        }
    }

    const fetchPatients = async () => {
        try {
            loading.value = true
            patients.value = await userService.getPatients()
        } catch (error) {
            console.error('erro ao buscar pacientes:', error)
            error.value = 'erro ao buscar pacientes'
            throw error
        } finally {
            loading.value = false
        }
    }

    return {
        doctors,
        patients,
        loading,
        error,
        fetchDoctors,
        fetchPatients
    }
})
